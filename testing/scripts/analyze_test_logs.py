#!/usr/bin/env python3
"""Analyze Thread child attach timing from pcap-derived CSVs only.

Strict rules:
- timing metrics come only from pcap event timestamps
- child-log timestamps are only correlation hints and report metadata
- pcap decoding is delegated to testing/scripts/pcap_to_csv.py
- a counted attach must be a complete pcap sequence:
  Parent Request -> Parent Response -> Child ID Request -> Child ID Response
- Parent Request -> Parent Response and Parent Response -> Child ID Request are matched by MLE Challenge/Response TLVs
- Child ID Request -> Child ID Response is matched by reversed parent/child endpoints, ordering, and timeout
- partial discovery attempts stay visible in the report but are not counted
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re
import statistics
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Literal


LOG_GROUP_RE = re.compile(r"^(.*_child)(?:_.*)?$")
TIMESTAMP_SUFFIX_RE = re.compile(r"-\d{8}-\d{6}$")
RUNCOUNT_SUFFIX_RE = re.compile(r"-\d+runs$")
TIMESTAMP_RE = re.compile(r"^\[(\d{2}):(\d{2}):(\d{2})\.(\d{3})\]")
STARTED_UTC_RE = re.compile(r"^# Started UTC:\s*([^\s]+)")
PARENT_REQ_RE = re.compile(r"Send Parent Request to routers")
PARENT_RESP_RE = re.compile(r"Receive Parent Response \(([^,]+),(0x[0-9a-fA-F]+)\)")
CHILD_ID_REQ_RE = re.compile(r"Send Child ID Request \(([^)]+)\)")
CHILD_ID_RESP_RE = re.compile(r"Receive Child ID Response \(([^,]+),(0x[0-9a-fA-F]+)\)")
MESH_FROM_RE = re.compile(r"MeshForwarder-: Received IPv6 UDP msg, .* from:([0-9a-f]+),?")
MESH_TO_RE = re.compile(r"MeshForwarder-: Sent IPv6 UDP msg, .* to:([0-9a-f]+),?")
IP_SRC_DST_RE = re.compile(r"MeshForwarder-:\s+(src|dst):\[([^\]]+)\]")
PARENT_INFO_RE = re.compile(r"Saved ParentInfo \{extaddr:([0-9a-f]+), version:\d+\}")
RADIO_EXTADDR_RE = re.compile(r"RadioExtAddress:\s*([0-9a-f]+)")
SWITCH_TARGET_RE = re.compile(
    r"(?:Thread parent switch to ExtAddr|Parent discovery attempt \d+/\d+ for ExtAddr)\s+([0-9a-f:]{16,23})",
    re.I,
)
TX_FAILED_RE = re.compile(
    r"Frame tx attempt (\d+)/(\d+) failed, error:([^,]+), .*?seqnum:(\d+)(?:, .*?dst:([0-9a-f]+))?"
)
NETWORK_KEY_RE = re.compile(r"network_key:\s*(?:0x)?([0-9a-fA-F]{32})")
SAVE_PCAP_RE = re.compile(r"Saving (?:test )?capture to (\S+\.pcapng)")

TIMING_LABELS = {
    "parent_request_to_response": "Request -> Response",
    "parent_response_to_child_id_request": "Response -> Child ID Request",
    "child_id_request_to_response": "Child ID Request -> Response",
    "parent_request_to_child_id_response": "Full Attach",
}
PCAP_EVENT_KEYS = (
    "send_parent_request",
    "receive_parent_response",
    "send_child_id_request",
    "receive_child_id_response",
)
DAY_MS = 24 * 60 * 60 * 1000
PARENT_RESPONSE_TIMEOUT_MS = 5000
CHILD_ID_REQUEST_TIMEOUT_MS = 15000
CHILD_ID_RESPONSE_TIMEOUT_MS = 5000


@dataclass
class MeshEvent:
    direction: str
    extaddr: str
    ip: str | None
    timestamp_ms: int
    line_no: int


@dataclass
class PcapEvent:
    frame_number: int
    epoch: float
    local_ms: int
    src64: str | None
    dst64: str | None
    ipv6_src: str | None = None
    ipv6_dst: str | None = None
    challenge: str | None = None
    response: str | None = None


@dataclass
class AttachSequence:
    send_parent_request_ms: int | None
    receive_parent_response_ms: int | None = None
    send_child_id_request_ms: int | None = None
    receive_child_id_response_ms: int | None = None
    parent_ipv6: str | None = None
    parent_rloc16: str | None = None
    parent_extaddr: str | None = None
    child_extaddr: str | None = None
    line_no: int = 0
    timing_source: str = "unavailable"
    pcap_frame_numbers: dict[str, int] = field(default_factory=dict)
    pcap_event_times: dict[str, str | None] = field(default_factory=dict)

    def has_complete_log_attach(self) -> bool:
        return (
            self.send_parent_request_ms is not None
            and self.receive_parent_response_ms is not None
            and self.send_child_id_request_ms is not None
            and self.receive_child_id_response_ms is not None
        )

    def has_complete_pcap_attach(self) -> bool:
        return all(self.pcap_event_times.get(key) is not None for key in PCAP_EVENT_KEYS)

    def to_summary(self) -> dict[str, Any]:
        pcap_start = parse_formatted_ms(self.pcap_event_times.get("send_parent_request"))
        pcap_parent_resp = parse_formatted_ms(self.pcap_event_times.get("receive_parent_response"))
        pcap_child_req = parse_formatted_ms(self.pcap_event_times.get("send_child_id_request"))
        pcap_child_resp = parse_formatted_ms(self.pcap_event_times.get("receive_child_id_response"))
        timing_ms = {
            "parent_request_to_response": delta_ms(pcap_start, pcap_parent_resp),
            "parent_response_to_child_id_request": delta_ms(pcap_parent_resp, pcap_child_req),
            "child_id_request_to_response": delta_ms(pcap_child_req, pcap_child_resp),
            "parent_request_to_child_id_response": delta_ms(pcap_start, pcap_child_resp),
        }
        return {
            "send_parent_request": format_ms(self.send_parent_request_ms),
            "receive_parent_response": format_ms(self.receive_parent_response_ms),
            "send_child_id_request": format_ms(self.send_child_id_request_ms),
            "receive_child_id_response": format_ms(self.receive_child_id_response_ms),
            "parent_ipv6": self.parent_ipv6,
            "parent_extaddr": compact_extaddr(self.parent_extaddr),
            "parent_rloc16": self.parent_rloc16,
            "child_extaddr": compact_extaddr(self.child_extaddr),
            "timing_source": self.timing_source,
            "timing_ms": timing_ms,
            "pcap_event_times": self.pcap_event_times,
            "pcap_frame_numbers": self.pcap_frame_numbers,
            "complete_log_attach": self.has_complete_log_attach(),
            "complete_pcap_attach": self.has_complete_pcap_attach(),
        }


@dataclass
class FailedTxSummary:
    total_failed_attempts: int = 0
    by_seqnum: dict[str, int] = field(default_factory=dict)
    by_dst: dict[str, int] = field(default_factory=dict)
    max_attempt_seen: int = 0
    max_attempt_limit_seen: int = 0


def compact_extaddr(extaddr: str | None) -> str | None:
    if extaddr is None:
        return None
    compact = extaddr.replace(":", "").strip().lower()
    return compact or None


def normalize_hex_value(value: str | None) -> str | None:
    if value is None:
        return None
    compact = value.replace(":", "").replace(" ", "").strip().lower()
    return compact or None


def split_values(value: str | None) -> list[str]:
    if not value:
        return []
    values: list[str] = []
    for part in str(value).split("|"):
        normalized = normalize_hex_value(part)
        if normalized:
            values.append(normalized)
    return values


def first_value(value: str | None) -> str | None:
    values = split_values(value)
    return values[0] if values else None


def values_intersect(left: str | None, right: str | None) -> bool:
    left_values = set(split_values(left))
    right_values = set(split_values(right))
    return bool(left_values and right_values and left_values.intersection(right_values))


def parse_timestamp_ms(line: str) -> int | None:
    match = TIMESTAMP_RE.match(line)
    if not match:
        return None
    hh, mm, ss, ms = map(int, match.groups())
    return (((hh * 60) + mm) * 60 + ss) * 1000 + ms


def format_ms(value: int | None) -> str | None:
    if value is None:
        return None
    value %= DAY_MS
    total_seconds, ms = divmod(value, 1000)
    hh, rem = divmod(total_seconds, 3600)
    mm, ss = divmod(rem, 60)
    return f"{hh:02d}:{mm:02d}:{ss:02d}.{ms:03d}"


def parse_formatted_ms(value: str | None) -> int | None:
    if value is None:
        return None
    hh, mm, rest = value.split(":")
    ss, ms = rest.split(".")
    return (((int(hh) * 60) + int(mm)) * 60 + int(ss)) * 1000 + int(ms)


def delta_ms(start: int | None, end: int | None) -> int | None:
    if start is None or end is None:
        return None
    diff = end - start
    if diff < -12 * 60 * 60 * 1000:
        diff += DAY_MS
    return diff


def score_optional_delta(log_ms: int | None, pcap_ms: int | None, missing_penalty: int = 10_000_000) -> int:
    if log_ms is None or pcap_ms is None:
        return missing_penalty
    diff = delta_ms(log_ms, pcap_ms)
    if diff is None:
        return missing_penalty
    return abs(diff)


def ms_of_utc_time(dt: datetime) -> int:
    return (((dt.hour * 60) + dt.minute) * 60 + dt.second) * 1000 + dt.microsecond // 1000


def nearest_reasonable_offset(diff_ms: int) -> int:
    while diff_ms > 12 * 60 * 60 * 1000:
        diff_ms -= DAY_MS
    while diff_ms < -12 * 60 * 60 * 1000:
        diff_ms += DAY_MS
    quantum = 15 * 60 * 1000
    return round(diff_ms / quantum) * quantum


def log_utc_offset_ms(log_path: Path) -> int:
    started_utc: datetime | None = None
    first_log_ms: int | None = None
    try:
        lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return system_local_offset_ms()

    for line in lines[:200]:
        if started_utc is None and (match := STARTED_UTC_RE.match(line)):
            raw = match.group(1).replace("Z", "+00:00")
            try:
                started_utc = datetime.fromisoformat(raw).astimezone(timezone.utc)
            except ValueError:
                pass
        if first_log_ms is None:
            first_log_ms = parse_timestamp_ms(line)
        if started_utc is not None and first_log_ms is not None:
            return nearest_reasonable_offset(first_log_ms - ms_of_utc_time(started_utc))
    return system_local_offset_ms()


def system_local_offset_ms() -> int:
    now = datetime.now().astimezone()
    offset = now.utcoffset()
    return int(offset.total_seconds() * 1000) if offset else 0


def epoch_to_local_ms(epoch: float, offset_ms: int) -> int:
    dt = datetime.fromtimestamp(float(epoch), tz=timezone.utc)
    return (ms_of_utc_time(dt) + offset_ms) % DAY_MS


def log_group_name(path: Path) -> str:
    match = LOG_GROUP_RE.match(path.stem)
    return match.group(1) if match else path.stem


def batch_dir_name(path: Path) -> str:
    return path.parent.parent.name


def batch_family_name(path: Path) -> str:
    name = batch_dir_name(path)
    name = TIMESTAMP_SUFFIX_RE.sub("", name)
    return RUNCOUNT_SUFFIX_RE.sub("", name)


def format_optional(value: Any) -> str:
    return "n/a" if value is None else str(value)


def format_stat(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.2f}"


def format_mean_sd(mean: float | None, stdev: float | None) -> str:
    if mean is None:
        return "n/a"
    return f"{format_stat(mean)} ({format_stat(stdev)})"


def mean_and_stdev(values: list[int]) -> tuple[float | None, float | None]:
    if not values:
        return None, None
    if len(values) == 1:
        return float(values[0]), 0.0
    return statistics.mean(values), statistics.stdev(values)


def resolve_parent_extaddr(
    seq: AttachSequence,
    *,
    mesh_events: list[MeshEvent],
    parent_info_events: list[tuple[int, int, str]],
) -> str | None:
    lower_bound_ms = (
        seq.send_parent_request_ms
        if seq.send_parent_request_ms is not None
        else seq.receive_parent_response_ms
        if seq.receive_parent_response_ms is not None
        else seq.send_child_id_request_ms
        if seq.send_child_id_request_ms is not None
        else 0
    )
    if seq.receive_child_id_response_ms is not None:
        for ts, _line_no, extaddr in parent_info_events:
            if ts >= seq.receive_child_id_response_ms and ts - seq.receive_child_id_response_ms <= 2000:
                return compact_extaddr(extaddr)
    if seq.parent_ipv6:
        candidates = [
            event
            for event in mesh_events
            if event.ip == seq.parent_ipv6
            and event.timestamp_ms >= lower_bound_ms - 100
            and (
                seq.receive_child_id_response_ms is None
                or event.timestamp_ms <= seq.receive_child_id_response_ms + 1000
            )
        ]
        if candidates:
            candidates.sort(key=lambda event: (event.timestamp_ms, event.line_no))
            return compact_extaddr(candidates[0].extaddr)
    return None


def manifest_for_log(log_path: Path) -> dict[str, Any] | None:
    run_dir = log_path.parent
    resolved_log_path = str(log_path.resolve())
    candidates = sorted(run_dir.glob("*_test_manifest_*.json"), reverse=True)
    if not candidates:
        candidates = sorted(run_dir.glob("*.json"), reverse=True)
    for manifest_path in candidates:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        manifest_child_log = manifest.get("child_log")
        if manifest_child_log:
            manifest_child_path = Path(manifest_child_log)
            if str(manifest_child_path.resolve()) == resolved_log_path or manifest_child_path.name == log_path.name:
                manifest["_manifest_path"] = str(manifest_path)
                return manifest
    return None


def manifest_labels(manifest: dict[str, Any] | None) -> list[str]:
    if not manifest:
        return []
    labels: list[str] = []
    for event in manifest.get("events", []):
        if not isinstance(event, dict):
            continue
        if event.get("type") not in {"label", "skip"}:
            continue
        reason = event.get("reason")
        if isinstance(reason, str) and reason not in labels:
            labels.append(reason)
    return labels


def sniffer_pcap_path(sniffer_log_path: Path) -> str | None:
    try:
        lines = sniffer_log_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None
    for line in lines:
        if match := SAVE_PCAP_RE.search(line):
            return match.group(1)
    return None


def candidate_pcap_paths(manifest: dict[str, Any], log_path: Path) -> Iterable[Path]:
    run_dir = log_path.parent
    raw_values: list[str] = []
    for key in ("local_pcap", "local_pcap_path", "pcap_path", "remote_pcap"):
        value = manifest.get(key)
        if isinstance(value, str):
            raw_values.append(value)
    sniffer = manifest.get("sniffer") or {}
    for key in ("local_pcap", "local_pcap_path", "pcap_path", "remote_pcap"):
        value = sniffer.get(key)
        if isinstance(value, str):
            raw_values.append(value)
    sniffer_log = sniffer.get("log")
    if isinstance(sniffer_log, str):
        for candidate_log in (Path(sniffer_log), run_dir / Path(sniffer_log).name):
            found = sniffer_pcap_path(candidate_log)
            if found:
                raw_values.append(found)

    seen: set[Path] = set()
    for raw in raw_values:
        raw_path = Path(raw)
        candidates = [raw_path, run_dir / raw_path.name]
        candidates.extend(sorted(run_dir.glob(f"{raw_path.stem}*.pcapng")))
        for candidate in candidates:
            if candidate in seen:
                continue
            seen.add(candidate)
            yield candidate

    for candidate in sorted(run_dir.glob("*.pcapng")):
        if candidate not in seen:
            yield candidate


def pcap_path_for_log(manifest: dict[str, Any], log_path: Path) -> Path | None:
    for candidate in candidate_pcap_paths(manifest, log_path):
        if candidate.exists():
            return candidate
    return None


def network_key_for_child_log(manifest: dict[str, Any], log_path: Path) -> str | None:
    if env_key := os.environ.get("THREAD_NETWORK_KEY"):
        if match := re.fullmatch(r"(?:0x)?([0-9a-fA-F]{32})", env_key.strip()):
            return match.group(1).lower()

    config_candidates: list[Path] = []
    config_file = manifest.get("config_file")
    if isinstance(config_file, str):
        config_candidates.append(Path(config_file))
        config_candidates.append(log_path.parent / Path(config_file).name)

    for event in manifest.get("events", []):
        cmd = event.get("cmd") or []
        if len(cmd) >= 3 and cmd[1] == "logs":
            config_candidates.append(Path(cmd[2]))
            config_candidates.append(log_path.parent / Path(cmd[2]).name)

    for config_path in config_candidates:
        try:
            config_text = config_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if match := NETWORK_KEY_RE.search(config_text):
            return match.group(1).lower()
    return None


def pcap_to_csv_script_path() -> Path:
    return Path(__file__).resolve().with_name("pcap_to_csv.py")


def derived_attach_csv_name(pcap: Path) -> str:
    stem = pcap.stem
    if "_sniffer_" in stem:
        prefix, stamp = stem.split("_sniffer_", 1)
        return f"{prefix}_attach_mle_{stamp}.csv"
    return f"{stem}-attach_mle.csv"


def candidate_attach_csv_paths(pcap_path: Path) -> list[Path]:
    run_dir = pcap_path.parent
    candidates = [
        run_dir / derived_attach_csv_name(pcap_path),
        run_dir / "attach_mle.csv",
        run_dir / f"{pcap_path.stem}_attach_mle.csv",
        run_dir / f"{pcap_path.stem}-attach_mle.csv",
    ]
    candidates.extend(sorted(run_dir.glob("*attach_mle*.csv"), key=lambda p: p.stat().st_mtime if p.exists() else 0, reverse=True))
    unique: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        unique.append(candidate)
    return unique


def attach_csv_path_for_pcap(pcap_path: Path) -> Path | None:
    for candidate in candidate_attach_csv_paths(pcap_path):
        if candidate.exists():
            return candidate
    return None


def generate_attach_csv(pcap_path: Path, network_key: str) -> Path:
    script = pcap_to_csv_script_path()
    if not script.exists():
        raise FileNotFoundError(f"{script} not found")

    args = [sys.executable, str(script), str(pcap_path), "--network-key", network_key, "--overwrite"]
    proc = subprocess.run(args, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise subprocess.CalledProcessError(proc.returncode, args, output=proc.stdout, stderr=proc.stderr)

    csv_path = attach_csv_path_for_pcap(pcap_path)
    if csv_path is None:
        raise FileNotFoundError(f"pcap_to_csv.py completed but no attach_mle CSV was found next to {pcap_path}")
    return csv_path


def load_attach_csv_rows(csv_path: Path, *, offset_ms: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with csv_path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            frame_no = row.get("frame.number") or ""
            epoch = row.get("frame.time_epoch") or ""
            cmd = row.get("mle.cmd") or ""
            if not frame_no or not epoch or not cmd:
                continue
            try:
                frame_number = int(frame_no)
                epoch_float = float(epoch)
                cmd_int = int(str(cmd).split("|")[0])
            except ValueError:
                continue
            rows.append(
                {
                    "frame_number": frame_number,
                    "epoch": epoch_float,
                    "cmd": cmd_int,
                    "src64": compact_extaddr(row.get("wpan.src64")),
                    "dst64": compact_extaddr(row.get("wpan.dst64")),
                    "ipv6_src": row.get("ipv6.src") or None,
                    "ipv6_dst": row.get("ipv6.dst") or None,
                    "challenge": row.get("mle.tlv.challenge") or row.get("mle.challenge") or None,
                    "response": row.get("mle.tlv.response") or row.get("mle.response") or None,
                    "local_ms": epoch_to_local_ms(epoch_float, offset_ms),
                }
            )
    return sorted(rows, key=lambda row: (row["epoch"], row["frame_number"]))


def pcap_sequences_from_csv_rows(rows: list[dict[str, Any]]) -> list[dict[str, PcapEvent]]:
    sequences: list[dict[str, PcapEvent]] = []
    used_frame_numbers: set[int] = set()

    for req in rows:
        if req["cmd"] != 9 or req["frame_number"] in used_frame_numbers:
            continue
        if not split_values(req.get("challenge")):
            continue

        child_extaddr = req["src64"]
        response_candidates = [
            row
            for row in rows
            if row["cmd"] == 10
            and row["frame_number"] not in used_frame_numbers
            and row["frame_number"] > req["frame_number"]
            and (not child_extaddr or row["dst64"] == child_extaddr)
            and values_intersect(row.get("response"), req.get("challenge"))
            and delta_ms(req["local_ms"], row["local_ms"]) is not None
            and 0 <= delta_ms(req["local_ms"], row["local_ms"]) <= PARENT_RESPONSE_TIMEOUT_MS
        ]
        if not response_candidates:
            continue
        response_candidates.sort(key=lambda row: (row["epoch"], row["frame_number"]))

        for resp in response_candidates:
            parent_extaddr = resp["src64"]
            if not split_values(resp.get("challenge")):
                continue

            child_req = next(
                (
                    row
                    for row in rows
                    if row["cmd"] == 11
                    and row["frame_number"] not in used_frame_numbers
                    and row["frame_number"] > resp["frame_number"]
                    and (not child_extaddr or row["src64"] == child_extaddr)
                    and (not parent_extaddr or row["dst64"] == parent_extaddr)
                    and values_intersect(row.get("response"), resp.get("challenge"))
                    and delta_ms(resp["local_ms"], row["local_ms"]) is not None
                    and 0 <= delta_ms(resp["local_ms"], row["local_ms"]) <= CHILD_ID_REQUEST_TIMEOUT_MS
                ),
                None,
            )
            if child_req is None:
                continue

            next_parent_request = next(
                (
                    row
                    for row in rows
                    if row["cmd"] == 9
                    and row["frame_number"] > child_req["frame_number"]
                    and (not child_extaddr or row["src64"] == child_extaddr)
                ),
                None,
            )
            child_resp = next(
                (
                    row
                    for row in rows
                    if row["cmd"] == 12
                    and row["frame_number"] not in used_frame_numbers
                    and row["frame_number"] > child_req["frame_number"]
                    and (next_parent_request is None or row["frame_number"] < next_parent_request["frame_number"])
                    and child_id_response_matches(row, child_req, child_extaddr, parent_extaddr)
                    and delta_ms(child_req["local_ms"], row["local_ms"]) is not None
                    and 0 <= delta_ms(child_req["local_ms"], row["local_ms"]) <= CHILD_ID_RESPONSE_TIMEOUT_MS
                ),
                None,
            )
            if child_resp is None:
                continue

            sequence = {
                "send_parent_request": pcap_event_from_row(req),
                "receive_parent_response": pcap_event_from_row(resp),
                "send_child_id_request": pcap_event_from_row(child_req),
                "receive_child_id_response": pcap_event_from_row(child_resp),
            }
            sequences.append(sequence)
            used_frame_numbers.update(
                {req["frame_number"], resp["frame_number"], child_req["frame_number"], child_resp["frame_number"]}
            )
            break

    return sequences


def child_id_response_matches(
    row: dict[str, Any],
    child_req: dict[str, Any],
    child_extaddr: str | None,
    parent_extaddr: str | None,
) -> bool:
    if parent_extaddr and child_extaddr and row.get("src64") == parent_extaddr and row.get("dst64") == child_extaddr:
        return True
    return bool(
        row.get("ipv6_src")
        and row.get("ipv6_dst")
        and row.get("ipv6_src") == child_req.get("ipv6_dst")
        and row.get("ipv6_dst") == child_req.get("ipv6_src")
    )


def pcap_event_from_row(row: dict[str, Any]) -> PcapEvent:
    return PcapEvent(
        frame_number=row["frame_number"],
        epoch=row["epoch"],
        local_ms=row["local_ms"],
        src64=compact_extaddr(row.get("src64")),
        dst64=compact_extaddr(row.get("dst64")),
        ipv6_src=row.get("ipv6_src"),
        ipv6_dst=row.get("ipv6_dst"),
        challenge=first_value(row.get("challenge")),
        response=first_value(row.get("response")),
    )


def pcap_sequences_for_log(
    manifest: dict[str, Any],
    log_path: Path,
    *,
    offset_ms: int,
    reuse_pcap_csv: bool = False,
    generate_pcap_csv: bool = True,
) -> tuple[list[dict[str, PcapEvent]], str, list[str]]:
    warnings: list[str] = []
    pcap_path = pcap_path_for_log(manifest, log_path)
    if pcap_path is None:
        warnings.append("Could not locate a pcap for this run; no pcap-derived timings were produced.")
        return [], "none", warnings

    try:
        attach_csv = attach_csv_path_for_pcap(pcap_path)
        source = "pcap-csv-tlv-existing"

        if attach_csv is None:
            if not generate_pcap_csv:
                expected = ", ".join(str(path.name) for path in candidate_attach_csv_paths(pcap_path))
                warnings.append(
                    f"No existing attach-MLE CSV found next to {pcap_path.name}; expected one of: {expected}. "
                    "CSV generation is disabled, so no pcap-derived timings were produced."
                )
                return [], "none", warnings

            network_key = network_key_for_child_log(manifest, log_path)
            if not network_key:
                warnings.append("Could not determine the Thread network key; no pcap-derived timings were produced.")
                return [], "none", warnings

            attach_csv = generate_attach_csv(pcap_path, network_key)
            source = "pcap-csv-tlv-generated"
        elif not reuse_pcap_csv and generate_pcap_csv:
            # Preserve the original behavior by regenerating unless explicitly told to reuse.
            network_key = network_key_for_child_log(manifest, log_path)
            if not network_key:
                warnings.append("Could not determine the Thread network key; using the existing attach-MLE CSV instead of regenerating it.")
            else:
                attach_csv = generate_attach_csv(pcap_path, network_key)
                source = "pcap-csv-tlv-generated"

        rows = load_attach_csv_rows(attach_csv, offset_ms=offset_ms)
        sequences = pcap_sequences_from_csv_rows(rows)
    except FileNotFoundError as exc:
        warnings.append(f"{exc}; no pcap-derived timings were produced.")
        return [], "none", warnings
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        detail = f": {stderr}" if stderr else ""
        warnings.append(f"pcap_to_csv.py failed while decoding the pcap (exit {exc.returncode}){detail}; no pcap-derived timings were produced.")
        return [], "none", warnings
    except OSError as exc:
        warnings.append(f"Could not read the pcap-derived CSV: {exc}.")
        return [], "none", warnings

    if not sequences:
        warnings.append(
            "No complete TLV-matched Parent Request -> Parent Response -> Child ID Request -> Child ID Response sequences were found in the pcap CSV."
        )
        return [], source, warnings
    return sequences, source, warnings


def pcap_sequence_child_extaddr(matched: dict[str, PcapEvent]) -> str | None:
    return compact_extaddr(matched["send_parent_request"].src64)


def pcap_sequence_parent_extaddr(matched: dict[str, PcapEvent]) -> str | None:
    return compact_extaddr(matched["receive_parent_response"].src64)


def fill_sequence_from_pcap(seq: AttachSequence, matched: dict[str, PcapEvent], *, source: str) -> None:
    seq.timing_source = source
    seq.pcap_frame_numbers = {key: value.frame_number for key, value in matched.items()}
    seq.pcap_event_times = {key: format_ms(value.local_ms) for key, value in matched.items()}
    if seq.child_extaddr is None:
        seq.child_extaddr = compact_extaddr(matched["send_parent_request"].src64)
    if seq.parent_extaddr is None:
        seq.parent_extaddr = compact_extaddr(matched["receive_parent_response"].src64)


def attach_sequence_from_pcap(matched: dict[str, PcapEvent], *, source: str) -> AttachSequence:
    return AttachSequence(
        send_parent_request_ms=None,
        receive_parent_response_ms=None,
        send_child_id_request_ms=None,
        receive_child_id_response_ms=None,
        parent_extaddr=compact_extaddr(matched["receive_parent_response"].src64),
        child_extaddr=compact_extaddr(matched["send_parent_request"].src64),
        timing_source=source,
        pcap_frame_numbers={key: value.frame_number for key, value in matched.items()},
        pcap_event_times={key: format_ms(value.local_ms) for key, value in matched.items()},
    )


def match_pcap_to_log_sequence(
    seq: AttachSequence,
    pcap_sequences: list[dict[str, PcapEvent]],
    used_indexes: set[int],
    *,
    child_extaddr: str | None,
) -> tuple[int, dict[str, PcapEvent]] | None:
    child = compact_extaddr(child_extaddr or seq.child_extaddr)
    parent = compact_extaddr(seq.parent_extaddr)
    candidates: list[tuple[int, int, dict[str, PcapEvent]]] = []

    for index, matched in enumerate(pcap_sequences):
        if index in used_indexes:
            continue
        pcap_child = pcap_sequence_child_extaddr(matched)
        pcap_parent = pcap_sequence_parent_extaddr(matched)
        if child and pcap_child != child:
            continue
        if parent and pcap_parent != parent:
            continue

        if seq.send_child_id_request_ms is not None:
            score = score_optional_delta(seq.send_child_id_request_ms, matched["send_child_id_request"].local_ms)
            threshold = 5000
        elif seq.receive_child_id_response_ms is not None:
            score = score_optional_delta(seq.receive_child_id_response_ms, matched["receive_child_id_response"].local_ms)
            threshold = 5000
        elif seq.receive_parent_response_ms is not None:
            score = score_optional_delta(seq.receive_parent_response_ms, matched["receive_parent_response"].local_ms)
            threshold = 5000
        elif seq.send_parent_request_ms is not None:
            score = score_optional_delta(seq.send_parent_request_ms, matched["send_parent_request"].local_ms)
            threshold = 5000
        else:
            score = 10**9
            threshold = 0
        if score <= threshold:
            candidates.append((score, index, matched))

    if not candidates:
        return None
    candidates.sort(key=lambda item: item[0])
    _, index, matched = candidates[0]
    return index, matched


def enrich_sequences_with_pcap(
    log_path: Path,
    sequences: list[AttachSequence],
    *,
    child_extaddr: str | None,
    reuse_pcap_csv: bool = False,
    generate_pcap_csv: bool = True,
) -> list[str]:
    warnings: list[str] = []
    manifest = manifest_for_log(log_path)
    if manifest is None:
        return ["No matching manifest found; skipping pcap timing enrichment."]

    offset_ms = log_utc_offset_ms(log_path)
    pcap_sequences, source, pcap_warnings = pcap_sequences_for_log(
        manifest,
        log_path,
        offset_ms=offset_ms,
        reuse_pcap_csv=reuse_pcap_csv,
        generate_pcap_csv=generate_pcap_csv,
    )
    warnings.extend(pcap_warnings)
    if not pcap_sequences:
        return warnings

    used_indexes: set[int] = set()
    for seq in sequences:
        matched_pair = match_pcap_to_log_sequence(seq, pcap_sequences, used_indexes, child_extaddr=child_extaddr)
        if matched_pair is None:
            continue
        index, matched = matched_pair
        used_indexes.add(index)
        fill_sequence_from_pcap(seq, matched, source=source)

    child = compact_extaddr(child_extaddr)
    if child is None:
        return warnings
    for index, matched in enumerate(pcap_sequences):
        if index in used_indexes:
            continue
        if pcap_sequence_child_extaddr(matched) != child:
            continue
        sequences.append(attach_sequence_from_pcap(matched, source=source))
    return warnings


def sequence_sort_key(seq: AttachSequence) -> tuple[int, int]:
    pcap_start = parse_formatted_ms(seq.pcap_event_times.get("send_parent_request"))
    if pcap_start is not None:
        return pcap_start, seq.line_no
    for value in (
        seq.send_parent_request_ms,
        seq.receive_parent_response_ms,
        seq.send_child_id_request_ms,
        seq.receive_child_id_response_ms,
    ):
        if value is not None:
            return value, seq.line_no
    return 10**12, seq.line_no


def analyze_log(
    path: Path,
    *,
    reuse_pcap_csv: bool = False,
    generate_pcap_csv: bool = True,
) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()

    raw_sequences: list[AttachSequence] = []
    current: AttachSequence | None = None
    mesh_events: list[MeshEvent] = []
    parent_info_events: list[tuple[int, int, str]] = []
    failed = FailedTxSummary()
    pending_mesh_direction: str | None = None
    pending_mesh_extaddr: str | None = None
    child_extaddr: str | None = None
    switch_targets: list[str] = []
    manifest = manifest_for_log(path)

    for line_no, line in enumerate(lines, start=1):
        timestamp_ms = parse_timestamp_ms(line)
        if match := SWITCH_TARGET_RE.search(line):
            switch_targets.append(compact_extaddr(match.group(1)) or match.group(1).lower())
        if timestamp_ms is None:
            continue

        if child_extaddr is None and (match := RADIO_EXTADDR_RE.search(line)):
            child_extaddr = compact_extaddr(match.group(1))
            continue

        if match := MESH_FROM_RE.search(line):
            pending_mesh_direction = "from"
            pending_mesh_extaddr = match.group(1)
            continue
        if match := MESH_TO_RE.search(line):
            pending_mesh_direction = "to"
            pending_mesh_extaddr = match.group(1)
            continue
        if pending_mesh_direction and pending_mesh_extaddr and (match := IP_SRC_DST_RE.search(line)):
            label, ip = match.groups()
            expected = "src" if pending_mesh_direction == "from" else "dst"
            if label == expected:
                mesh_events.append(MeshEvent(pending_mesh_direction, pending_mesh_extaddr, ip, timestamp_ms, line_no))
                pending_mesh_direction = None
                pending_mesh_extaddr = None
            continue
        if match := PARENT_INFO_RE.search(line):
            parent_info_events.append((timestamp_ms, line_no, match.group(1)))
            continue
        if match := TX_FAILED_RE.search(line):
            attempt, limit, _error, seqnum, dst = match.groups()
            failed.total_failed_attempts += 1
            failed.by_seqnum[seqnum] = failed.by_seqnum.get(seqnum, 0) + 1
            if dst:
                failed.by_dst[dst] = failed.by_dst.get(dst, 0) + 1
            failed.max_attempt_seen = max(failed.max_attempt_seen, int(attempt))
            failed.max_attempt_limit_seen = max(failed.max_attempt_limit_seen, int(limit))
            continue
        if PARENT_REQ_RE.search(line):
            if current is not None:
                current.parent_extaddr = resolve_parent_extaddr(
                    current,
                    mesh_events=mesh_events,
                    parent_info_events=parent_info_events,
                )
                raw_sequences.append(current)
            current = AttachSequence(send_parent_request_ms=timestamp_ms, line_no=line_no, child_extaddr=child_extaddr)
            continue
        if match := CHILD_ID_REQ_RE.search(line):
            if current is None:
                current = AttachSequence(send_parent_request_ms=None, line_no=line_no, child_extaddr=child_extaddr)
            current.send_child_id_request_ms = timestamp_ms
            current.parent_ipv6 = match.group(1)
            continue
        if current is None:
            continue
        if match := PARENT_RESP_RE.search(line):
            if current.receive_parent_response_ms is None:
                current.receive_parent_response_ms = timestamp_ms
            if current.parent_ipv6 is None:
                current.parent_ipv6 = match.group(1)
            if current.parent_rloc16 is None:
                current.parent_rloc16 = match.group(2)
            continue
        if match := CHILD_ID_RESP_RE.search(line):
            current.receive_child_id_response_ms = timestamp_ms
            current.parent_ipv6 = match.group(1)
            current.parent_rloc16 = match.group(2)
            current.parent_extaddr = resolve_parent_extaddr(
                current,
                mesh_events=mesh_events,
                parent_info_events=parent_info_events,
            )
            raw_sequences.append(current)
            current = None
            continue

    if current is not None:
        current.parent_extaddr = resolve_parent_extaddr(
            current,
            mesh_events=mesh_events,
            parent_info_events=parent_info_events,
        )
        raw_sequences.append(current)

    warnings = enrich_sequences_with_pcap(
        path,
        raw_sequences,
        child_extaddr=child_extaddr,
        reuse_pcap_csv=reuse_pcap_csv,
        generate_pcap_csv=generate_pcap_csv,
    )
    raw_sequences.sort(key=sequence_sort_key)

    completed = [seq for seq in raw_sequences if seq.has_complete_pcap_attach()]
    not_counted = [seq for seq in raw_sequences if not seq.has_complete_pcap_attach()]

    return {
        "group": log_group_name(path),
        "batch_dir": batch_dir_name(path),
        "batch_family": batch_family_name(path),
        "log_file": str(path),
        "manifest_status": manifest.get("status") if manifest else None,
        "manifest_path": manifest.get("_manifest_path") if manifest else None,
        "labels": manifest_labels(manifest),
        "child_extaddr": child_extaddr,
        "switch_targets": switch_targets,
        "attach_sequences": [seq.to_summary() for seq in completed],
        "log_only_or_partial_sequences": [seq.to_summary() for seq in not_counted],
        "failed_tx": asdict(failed),
        "warnings": warnings,
    }


GroupByMode = Literal["log-group", "batch-dir", "batch-family"]


def group_key_for_result(result: dict[str, Any], mode: GroupByMode) -> str:
    if mode == "log-group":
        return result["group"]
    if mode == "batch-dir":
        return result["batch_dir"]
    if mode == "batch-family":
        return result["batch_family"]
    raise ValueError(f"Unsupported group mode: {mode}")


def group_results(results: list[dict[str, Any]], *, mode: GroupByMode) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for result in results:
        grouped.setdefault(group_key_for_result(result, mode), []).append(result)
    return grouped


def group_summary(group_results: list[dict[str, Any]]) -> dict[str, Any]:
    attach_summaries: dict[int, dict[str, tuple[float | None, float | None, int]]] = {}
    max_attach_count = max((len(result["attach_sequences"]) for result in group_results), default=0)
    for attach_index in range(max_attach_count):
        timing_values: dict[str, list[int]] = {key: [] for key in TIMING_LABELS}
        for result in group_results:
            sequences = result["attach_sequences"]
            if attach_index >= len(sequences):
                continue
            seq = sequences[attach_index]
            for key in timing_values:
                value = seq["timing_ms"].get(key)
                if value is not None:
                    timing_values[key].append(value)
        attach_summary: dict[str, tuple[float | None, float | None, int]] = {}
        for key, values in timing_values.items():
            mean, stdev = mean_and_stdev(values)
            attach_summary[key] = (mean, stdev, len(values))
        attach_summaries[attach_index + 1] = attach_summary

    failed_tx_values = [result["failed_tx"]["total_failed_attempts"] for result in group_results]
    failed_mean, failed_stdev = mean_and_stdev(failed_tx_values)
    partial_counts = [len(result.get("log_only_or_partial_sequences", [])) for result in group_results]
    partial_mean, partial_stdev = mean_and_stdev(partial_counts)
    return {
        "attaches": attach_summaries,
        "failed_tx_attempts": (failed_mean, failed_stdev, len(failed_tx_values)),
        "log_only_or_partial_sequences": (partial_mean, partial_stdev, len(partial_counts)),
    }


def render_sequence_lines(seq: dict[str, Any], *, include_pcap: bool) -> list[str]:
    out = [
        f"- log parent request: `{format_optional(seq['send_parent_request'])}`",
        f"- log parent response: `{format_optional(seq['receive_parent_response'])}`",
        f"- log child id request: `{format_optional(seq['send_child_id_request'])}`",
        f"- log child id response: `{format_optional(seq['receive_child_id_response'])}`",
        f"- parent ipv6: `{format_optional(seq['parent_ipv6'])}`",
        f"- parent extaddr: `{format_optional(seq['parent_extaddr'])}`",
        f"- parent rloc16: `{format_optional(seq['parent_rloc16'])}`",
        f"- child extaddr: `{format_optional(seq['child_extaddr'])}`",
        f"- timing source: **{seq['timing_source']}**",
        f"- complete log attach: **{seq.get('complete_log_attach', False)}**",
        f"- complete pcap attach: **{seq.get('complete_pcap_attach', False)}**",
        f"- {TIMING_LABELS['parent_request_to_response']}: **{seq['timing_ms']['parent_request_to_response']} ms**",
        f"- {TIMING_LABELS['parent_response_to_child_id_request']}: **{seq['timing_ms']['parent_response_to_child_id_request']} ms**",
        f"- {TIMING_LABELS['child_id_request_to_response']}: **{seq['timing_ms']['child_id_request_to_response']} ms**",
        f"- {TIMING_LABELS['parent_request_to_child_id_response']}: **{seq['timing_ms']['parent_request_to_child_id_response']} ms**",
    ]
    if include_pcap and seq["complete_pcap_attach"]:
        out.extend(
            [
                f"- pcap parent request: `{seq['pcap_event_times'].get('send_parent_request')}` (frame {seq['pcap_frame_numbers'].get('send_parent_request')})",
                f"- pcap parent response: `{seq['pcap_event_times'].get('receive_parent_response')}` (frame {seq['pcap_frame_numbers'].get('receive_parent_response')})",
                f"- pcap child id request: `{seq['pcap_event_times'].get('send_child_id_request')}` (frame {seq['pcap_frame_numbers'].get('send_child_id_request')})",
                f"- pcap child id response: `{seq['pcap_event_times'].get('receive_child_id_response')}` (frame {seq['pcap_frame_numbers'].get('receive_child_id_response')})",
            ]
        )
    return out


def render_markdown_report(
    results: list[dict[str, Any]],
    *,
    group_by: GroupByMode = "log-group",
    summary_only: bool = False,
) -> str:
    if not results:
        return "# Child Log Analysis\n\nNo `.log` files found.\n"
    grouped = group_results(results, mode=group_by)
    out: list[str] = ["# Child Log Analysis", ""]
    if group_by == "batch-family":
        out.extend(
            [
                "Grouped by batch family, combining multiple batch folders that share the same variant/router pattern even when the run counts differ.",
                "",
            ]
        )
    for group_name in sorted(grouped):
        group_items = grouped[group_name]
        summary = group_summary(group_items)
        out.extend([f"## {group_name}", "", f"Files analyzed: **{len(group_items)}**", ""])
        batch_dirs = sorted({result["batch_dir"] for result in group_items})
        if group_by != "batch-dir":
            out.append(f"- batch folders: `{', '.join(batch_dirs)}`")
            out.append("")
        out.extend(["### PCAP-complete child attach summary", "", "| Attach | Metric | M (SD), ms | n |", "| --- | --- | ---: | ---: |"])
        for attach_index in sorted(summary["attaches"]):
            attach = summary["attaches"][attach_index]
            for key, label in TIMING_LABELS.items():
                mean, stdev, n = attach[key]
                out.append(f"| {attach_index} | {label} | {format_mean_sd(mean, stdev)} | {n} |")
        out.extend(["", "| Metric | M (SD) | n |", "| --- | ---: | ---: |"])
        failed = summary["failed_tx_attempts"]
        partial = summary["log_only_or_partial_sequences"]
        out.append(f"| Failed TX Attempts per Log | {format_mean_sd(failed[0], failed[1])} | {failed[2]} |")
        out.append(f"| Log-only or Partial Sequences per Log | {format_mean_sd(partial[0], partial[1])} | {partial[2]} |")
        out.append("")
        if summary_only:
            continue
        for result in group_items:
            out.extend([f"### `{Path(result['log_file']).name}`", ""])
            if result.get("manifest_status") is not None:
                out.append(f"- manifest status: `{result['manifest_status']}`")
            labels = result.get("labels") or []
            if labels:
                out.append(f"- labels: `{', '.join(labels)}`")
            out.append(f"- child extaddr: `{format_optional(result.get('child_extaddr'))}`")
            if result.get("switch_targets"):
                out.append(f"- switch target extaddr(s): `{', '.join(result['switch_targets'])}`")
            out.append("")
            warnings = result.get("warnings", [])
            if warnings:
                out.extend(["#### Warnings", ""])
                for warning in warnings:
                    out.append(f"- {warning}")
                out.append("")
            sequences = result["attach_sequences"]
            if not sequences:
                out.extend(["No PCAP-complete child attach sequences found.", ""])
            else:
                for index, seq in enumerate(sequences, start=1):
                    out.extend([f"#### PCAP-complete child attach {index}", ""])
                    out.extend(render_sequence_lines(seq, include_pcap=True))
                    out.append("")
            leftovers = result.get("log_only_or_partial_sequences", [])
            if leftovers:
                out.extend(["#### Log-only or partial sequences", "", "These are not counted as completed attaches because they do not have a complete pcap sequence.", ""])
                for index, seq in enumerate(leftovers, start=1):
                    out.extend([f"##### Not-counted sequence {index}", ""])
                    out.extend(render_sequence_lines(seq, include_pcap=False))
                    out.append("")
            failed = result["failed_tx"]
            out.extend(["#### Failed TX summary", ""])
            out.append(f"- failed tx attempts: **{failed['total_failed_attempts']}**")
            out.append(f"- highest attempt number seen: **{failed['max_attempt_seen']}/{failed['max_attempt_limit_seen']}**")
            if failed["by_seqnum"]:
                seq_summary = ", ".join(
                    f"seq {seqnum}: {count}"
                    for seqnum, count in sorted(failed["by_seqnum"].items(), key=lambda item: int(item[0]))
                )
                out.append(f"- failed tx by seqnum: {seq_summary}")
            if failed["by_dst"]:
                dst_summary = ", ".join(f"`{dst}`: {count}" for dst, count in sorted(failed["by_dst"].items()))
                out.append(f"- failed tx by dst: {dst_summary}")
            out.append("")
    return "\n".join(out)


def render_text_report(results: list[dict[str, Any]]) -> str:
    return render_markdown_report(results)


def default_logs_dir(script_path: Path) -> Path:
    return script_path.resolve().parent.parent / "logs"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze child attach timing. Metrics are pcap-only.")
    parser.add_argument("--logs-dir", type=Path, default=default_logs_dir(Path(__file__)), help="Directory containing *.log files.")
    parser.add_argument("--run-dir", dest="run_dirs", action="append", type=Path, default=[], help="Specific run directory to include. Repeat for multiple runs.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--markdown", action="store_true", help="Emit Markdown instead of plain text.")
    parser.add_argument("--write-markdown", nargs="?", const=Path("__AUTO__"), type=Path, help="Write the Markdown report to this path.")
    parser.add_argument(
        "--group-by",
        choices=("log-group", "batch-dir", "batch-family"),
        default="log-group",
        help="How to group analyzed runs in the output.",
    )
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Only emit per-group summaries, without the per-log detailed sections.",
    )
    parser.add_argument(
        "--reuse-pcap-csv",
        action="store_true",
        help="Reuse an existing attach-MLE CSV next to each PCAP when present; generate it only when missing.",
    )
    parser.add_argument(
        "--no-generate-pcap-csv",
        action="store_true",
        help="Never call pcap_to_csv.py; require an existing attach-MLE CSV next to each PCAP.",
    )
    return parser.parse_args(argv)


def collect_log_paths(logs_dir: Path, run_dirs: list[Path]) -> list[Path]:
    if run_dirs:
        log_paths: list[Path] = []
        for run_dir in run_dirs:
            log_paths.extend(sorted(run_dir.resolve().glob("*_child_*.log")))
        return sorted({path.resolve() for path in log_paths})
    return sorted(Path(path) for path in glob.glob(str(logs_dir / "**" / "*_child_*.log"), recursive=True))


def default_markdown_path_for_run_dir(run_dir: Path) -> Path:
    run_dir = run_dir.resolve()
    variant_dir = run_dir.parent
    variant_name = variant_dir.name
    return variant_dir / f"{run_dir.name}-{variant_name}-analysis-report.md"


def default_markdown_path_for_logs_dir(logs_dir: Path, *, group_by: GroupByMode, summary_only: bool) -> Path:
    logs_dir = logs_dir.resolve()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    if group_by == "batch-family" and summary_only:
        return logs_dir / f"{timestamp}-all-batches-summary-report.md"
    variant_name = logs_dir.name
    return logs_dir / f"{timestamp}-{variant_name}-analysis-report.md"


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    logs_dir = args.logs_dir.resolve()
    log_paths = collect_log_paths(logs_dir, args.run_dirs)
    if args.reuse_pcap_csv and args.no_generate_pcap_csv:
        raise SystemExit("Use either --reuse-pcap-csv or --no-generate-pcap-csv, not both.")

    results = [
        analyze_log(
            path,
            reuse_pcap_csv=args.reuse_pcap_csv or args.no_generate_pcap_csv,
            generate_pcap_csv=not args.no_generate_pcap_csv,
        )
        for path in log_paths
    ]

    if args.json:
        output = json.dumps(results, indent=2)
    elif args.markdown or args.write_markdown:
        output = render_markdown_report(results, group_by=args.group_by, summary_only=args.summary_only)
    else:
        output = render_text_report(results)

    if args.write_markdown:
        write_path = args.write_markdown
        if write_path == Path("__AUTO__"):
            if args.run_dirs:
                if len(args.run_dirs) != 1:
                    raise SystemExit("--write-markdown without a path supports exactly one --run-dir.")
                write_path = default_markdown_path_for_run_dir(args.run_dirs[0])
            else:
                write_path = default_markdown_path_for_logs_dir(
                    logs_dir,
                    group_by=args.group_by,
                    summary_only=args.summary_only,
                )
        write_path.parent.mkdir(parents=True, exist_ok=True)
        write_path.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
