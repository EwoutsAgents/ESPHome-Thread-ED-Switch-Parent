#!/usr/bin/env python3
"""Analyze child log timing and failed TX attempts.

Scans all `*.log` files in the testing logs directory using `glob` and reports:
- Parent attach timing for:
  - Send Parent Request
  - Receive Parent Response
  - Send Child ID Request
  - Receive Child ID Response
- The chosen parent IPv6, ext address, and RLOC16
- Failed MAC frame TX attempt counts

Results are grouped by the log family name ending in `_child`, for example:
- `stock_child_20260529-134804.log` -> `stock_child`
- `experiment_a_child_20260601-101500.log` -> `experiment_a_child`
"""

from __future__ import annotations

import argparse
import glob
import json
import re
import statistics
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

LOG_GROUP_RE = re.compile(r"^(.*_child)(?:_.*)?$")

TIMESTAMP_RE = re.compile(r"^\[(\d{2}):(\d{2}):(\d{2})\.(\d{3})\]")
PARENT_REQ_RE = re.compile(r"Send Parent Request to routers")
PARENT_RESP_RE = re.compile(r"Receive Parent Response \(([^,]+),(0x[0-9a-fA-F]+)\)")
CHILD_ID_REQ_RE = re.compile(r"Send Child ID Request \(([^)]+)\)")
CHILD_ID_RESP_RE = re.compile(r"Receive Child ID Response \(([^,]+),(0x[0-9a-fA-F]+)\)")
MESH_FROM_RE = re.compile(r"MeshForwarder-: Received IPv6 UDP msg, .* from:([0-9a-f]+),?")
MESH_TO_RE = re.compile(r"MeshForwarder-: Sent IPv6 UDP msg, .* to:([0-9a-f]+),?")
IP_SRC_DST_RE = re.compile(r"MeshForwarder-:\s+(src|dst):\[([^\]]+)\]")
PARENT_INFO_RE = re.compile(r"Saved ParentInfo \{extaddr:([0-9a-f]+), version:\d+\}")
TX_FAILED_RE = re.compile(
    r"Frame tx attempt (\d+)/(\d+) failed, error:([^,]+), .*?seqnum:(\d+)(?:, .*?dst:([0-9a-f]+))?"
)


@dataclass
class MeshEvent:
    direction: str
    extaddr: str
    ip: str | None
    timestamp_ms: int
    line_no: int


@dataclass
class AttachSequence:
    send_parent_request_ms: int
    receive_parent_response_ms: int | None = None
    send_child_id_request_ms: int | None = None
    receive_child_id_response_ms: int | None = None
    parent_ipv6: str | None = None
    parent_rloc16: str | None = None
    parent_extaddr: str | None = None
    line_no: int = 0

    def to_summary(self) -> dict[str, Any]:
        result = {
            "send_parent_request": format_ms(self.send_parent_request_ms),
            "receive_parent_response": format_ms(self.receive_parent_response_ms),
            "send_child_id_request": format_ms(self.send_child_id_request_ms),
            "receive_child_id_response": format_ms(self.receive_child_id_response_ms),
            "parent_ipv6": self.parent_ipv6,
            "parent_extaddr": self.parent_extaddr,
            "parent_rloc16": self.parent_rloc16,
            "timing_ms": {
                "parent_request_to_response": delta_ms(self.send_parent_request_ms, self.receive_parent_response_ms),
                "parent_response_to_child_id_request": delta_ms(self.receive_parent_response_ms, self.send_child_id_request_ms),
                "child_id_request_to_response": delta_ms(self.send_child_id_request_ms, self.receive_child_id_response_ms),
                "parent_request_to_child_id_response": delta_ms(self.send_parent_request_ms, self.receive_child_id_response_ms),
            },
        }
        return result


@dataclass
class FailedTxSummary:
    total_failed_attempts: int = 0
    by_seqnum: dict[str, int] = field(default_factory=dict)
    by_dst: dict[str, int] = field(default_factory=dict)
    max_attempt_seen: int = 0
    max_attempt_limit_seen: int = 0


def parse_timestamp_ms(line: str) -> int | None:
    match = TIMESTAMP_RE.match(line)
    if not match:
        return None
    hh, mm, ss, ms = map(int, match.groups())
    return (((hh * 60) + mm) * 60 + ss) * 1000 + ms


def format_ms(value: int | None) -> str | None:
    if value is None:
        return None
    total_seconds, ms = divmod(value, 1000)
    hh, rem = divmod(total_seconds, 3600)
    mm, ss = divmod(rem, 60)
    return f"{hh:02d}:{mm:02d}:{ss:02d}.{ms:03d}"


def delta_ms(start: int | None, end: int | None) -> int | None:
    if start is None or end is None:
        return None
    return end - start


def resolve_parent_extaddr(
    seq: AttachSequence,
    *,
    mesh_events: list[MeshEvent],
    parent_info_events: list[tuple[int, int, str]],
) -> str | None:
    if seq.receive_child_id_response_ms is not None:
        for ts, line_no, extaddr in parent_info_events:
            if ts >= seq.receive_child_id_response_ms and ts - seq.receive_child_id_response_ms <= 2000:
                return extaddr

    if seq.parent_ipv6:
        candidates = [
            event
            for event in mesh_events
            if event.ip == seq.parent_ipv6
            and event.timestamp_ms >= seq.send_parent_request_ms - 100
            and (
                seq.receive_child_id_response_ms is None
                or event.timestamp_ms <= seq.receive_child_id_response_ms + 1000
            )
        ]
        if candidates:
            candidates.sort(key=lambda event: (event.timestamp_ms, event.line_no))
            return candidates[0].extaddr

    return None


def log_group_name(path: Path) -> str:
    stem = path.stem
    match = LOG_GROUP_RE.match(stem)
    return match.group(1) if match else stem


def analyze_log(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()

    sequences: list[AttachSequence] = []
    current: AttachSequence | None = None
    mesh_events: list[MeshEvent] = []
    parent_info_events: list[tuple[int, int, str]] = []
    failed = FailedTxSummary()

    pending_mesh_direction: str | None = None
    pending_mesh_extaddr: str | None = None

    for line_no, line in enumerate(lines, start=1):
        timestamp_ms = parse_timestamp_ms(line)
        if timestamp_ms is None:
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
                mesh_events.append(
                    MeshEvent(
                        direction=pending_mesh_direction,
                        extaddr=pending_mesh_extaddr,
                        ip=ip,
                        timestamp_ms=timestamp_ms,
                        line_no=line_no,
                    )
                )
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
                sequences.append(current)
            current = AttachSequence(send_parent_request_ms=timestamp_ms, line_no=line_no)
            continue

        if current is None:
            continue

        if match := PARENT_RESP_RE.search(line):
            current.receive_parent_response_ms = timestamp_ms
            current.parent_ipv6 = match.group(1)
            current.parent_rloc16 = match.group(2)
            continue

        if match := CHILD_ID_REQ_RE.search(line):
            current.send_child_id_request_ms = timestamp_ms
            current.parent_ipv6 = current.parent_ipv6 or match.group(1)
            continue

        if match := CHILD_ID_RESP_RE.search(line):
            current.receive_child_id_response_ms = timestamp_ms
            current.parent_ipv6 = current.parent_ipv6 or match.group(1)
            current.parent_rloc16 = current.parent_rloc16 or match.group(2)
            current.parent_extaddr = resolve_parent_extaddr(current, mesh_events=mesh_events, parent_info_events=parent_info_events)
            sequences.append(current)
            current = None
            continue

    if current is not None:
        current.parent_extaddr = resolve_parent_extaddr(current, mesh_events=mesh_events, parent_info_events=parent_info_events)
        sequences.append(current)

    return {
        "group": log_group_name(path),
        "log_file": str(path),
        "attach_sequences": [seq.to_summary() for seq in sequences],
        "failed_tx": asdict(failed),
    }


def default_logs_dir(script_path: Path) -> Path:
    return script_path.resolve().parent.parent / "logs"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze stock child logs for attach timing and failed TX attempts.")
    parser.add_argument("--logs-dir", type=Path, default=default_logs_dir(Path(__file__)), help="Directory containing *.log files.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--markdown", action="store_true", help="Emit Markdown instead of plain text.")
    parser.add_argument("--write-markdown", type=Path, help="Write the Markdown report to this path.")
    return parser.parse_args(argv)


def mean_and_stdev(values: list[int]) -> tuple[float | None, float | None]:
    if not values:
        return None, None
    if len(values) == 1:
        return float(values[0]), 0.0
    return statistics.mean(values), statistics.stdev(values)


def format_stat(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.2f}"


def format_avg_stdev(mean: float | None, stdev: float | None, *, suffix: str = "") -> str:
    if mean is None:
        return "n/a"
    tail = f" {suffix}" if suffix else ""
    return f"{format_stat(mean)} ± {format_stat(stdev)}{tail}"


def group_summary(group_results: list[dict[str, Any]]) -> dict[str, Any]:
    attach_summaries: dict[int, dict[str, tuple[float | None, float | None, int]]] = {}
    max_attach_count = max((len(result["attach_sequences"]) for result in group_results), default=0)

    for attach_index in range(max_attach_count):
        timing_values: dict[str, list[int]] = {
            "parent_request_to_response": [],
            "parent_response_to_child_id_request": [],
            "child_id_request_to_response": [],
            "parent_request_to_child_id_response": [],
        }
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

    return {
        "attaches": attach_summaries,
        "failed_tx_attempts": (failed_mean, failed_stdev, len(failed_tx_values)),
    }


def group_results(results: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for result in results:
        grouped.setdefault(result["group"], []).append(result)
    return grouped


def render_text_report(results: list[dict[str, Any]]) -> str:
    if not results:
        return "No .log files found.\n"

    grouped = group_results(results)
    out: list[str] = []

    for group_name in sorted(grouped):
        out.append(f"Group: {group_name}")
        summary = group_summary(grouped[group_name])
        out.append("  Group summary:")
        for attach_index in sorted(summary["attaches"]):
            attach = summary["attaches"][attach_index]
            out.append(f"    Attach {attach_index}:")
            out.append(
                "      request -> response: "
                f"avg {format_stat(attach['parent_request_to_response'][0])} ms, "
                f"stdev {format_stat(attach['parent_request_to_response'][1])} ms, "
                f"n={attach['parent_request_to_response'][2]}"
            )
            out.append(
                "      response -> child id request: "
                f"avg {format_stat(attach['parent_response_to_child_id_request'][0])} ms, "
                f"stdev {format_stat(attach['parent_response_to_child_id_request'][1])} ms, "
                f"n={attach['parent_response_to_child_id_request'][2]}"
            )
            out.append(
                "      child id request -> response: "
                f"avg {format_stat(attach['child_id_request_to_response'][0])} ms, "
                f"stdev {format_stat(attach['child_id_request_to_response'][1])} ms, "
                f"n={attach['child_id_request_to_response'][2]}"
            )
            out.append(
                "      full attach quartet: "
                f"avg {format_stat(attach['parent_request_to_child_id_response'][0])} ms, "
                f"stdev {format_stat(attach['parent_request_to_child_id_response'][1])} ms, "
                f"n={attach['parent_request_to_child_id_response'][2]}"
            )
        out.append(
            "    failed tx attempts per log: "
            f"avg {format_stat(summary['failed_tx_attempts'][0])}, "
            f"stdev {format_stat(summary['failed_tx_attempts'][1])}, "
            f"n={summary['failed_tx_attempts'][2]}"
        )

        for result in grouped[group_name]:
            out.append(f"  Log: {result['log_file']}")
            sequences = result["attach_sequences"]
            if not sequences:
                out.append("    No parent attach sequences found.")
            else:
                for index, seq in enumerate(sequences, start=1):
                    out.append(f"    Attach sequence {index}:")
                    out.append(f"      parent request: {seq['send_parent_request']}")
                    out.append(f"      parent response: {seq['receive_parent_response']}")
                    out.append(f"      child id request: {seq['send_child_id_request']}")
                    out.append(f"      child id response: {seq['receive_child_id_response']}")
                    out.append(f"      parent ipv6: {seq['parent_ipv6']}")
                    out.append(f"      parent extaddr: {seq['parent_extaddr']}")
                    out.append(f"      parent rloc16: {seq['parent_rloc16']}")
                    out.append(f"      request -> response: {seq['timing_ms']['parent_request_to_response']} ms")
                    out.append(f"      response -> child id request: {seq['timing_ms']['parent_response_to_child_id_request']} ms")
                    out.append(f"      child id request -> response: {seq['timing_ms']['child_id_request_to_response']} ms")
                    out.append(f"      full attach quartet: {seq['timing_ms']['parent_request_to_child_id_response']} ms")

            failed = result["failed_tx"]
            out.append(f"    failed tx attempts: {failed['total_failed_attempts']}")
            out.append(f"    highest attempt number seen: {failed['max_attempt_seen']}/{failed['max_attempt_limit_seen']}")
            if failed["by_seqnum"]:
                seq_summary = ", ".join(f"seq {seqnum}: {count}" for seqnum, count in sorted(failed["by_seqnum"].items(), key=lambda item: int(item[0])))
                out.append(f"    failed tx by seqnum: {seq_summary}")
            if failed["by_dst"]:
                dst_summary = ", ".join(f"{dst}: {count}" for dst, count in sorted(failed["by_dst"].items()))
                out.append(f"    failed tx by dst: {dst_summary}")
        out.append("")

    return "\n".join(out)


def render_markdown_report(results: list[dict[str, Any]]) -> str:
    if not results:
        return "# Child Log Analysis\n\nNo `.log` files found.\n"

    grouped = group_results(results)
    out = ["# Child Log Analysis", ""]

    for group_name in sorted(grouped):
        summary = group_summary(grouped[group_name])
        out.append(f"## {group_name}")
        out.append("")
        out.append("### Group summary")
        out.append("")
        out.append("| Attach | Parent Request → Response (ms) | Parent Response → Child ID Req (ms) | Child ID Req → Response (ms) | Full attach (ms) | n |")
        out.append("| --- | ---: | ---: | ---: | ---: | ---: |")
        for attach_index in sorted(summary["attaches"]):
            attach = summary["attaches"][attach_index]
            out.append(
                f"| {attach_index} "
                f"| {format_avg_stdev(attach['parent_request_to_response'][0], attach['parent_request_to_response'][1])} "
                f"| {format_avg_stdev(attach['parent_response_to_child_id_request'][0], attach['parent_response_to_child_id_request'][1])} "
                f"| {format_avg_stdev(attach['child_id_request_to_response'][0], attach['child_id_request_to_response'][1])} "
                f"| {format_avg_stdev(attach['parent_request_to_child_id_response'][0], attach['parent_request_to_child_id_response'][1])} "
                f"| {attach['parent_request_to_child_id_response'][2]} |"
            )
        out.append("")
        out.append("| Failed TX attempts per log | n |")
        out.append("| ---: | ---: |")
        out.append(
            f"| {format_avg_stdev(summary['failed_tx_attempts'][0], summary['failed_tx_attempts'][1])} | {summary['failed_tx_attempts'][2]} |"
        )
        out.append("")

        for result in grouped[group_name]:
            out.append(f"### `{Path(result['log_file']).name}`")
            out.append("")
            sequences = result["attach_sequences"]
            if not sequences:
                out.append("No parent attach sequences found.")
                out.append("")
            else:
                for index, seq in enumerate(sequences, start=1):
                    out.append(f"#### Attach sequence {index}")
                    out.append("")
                    out.append(f"- parent request: `{seq['send_parent_request']}`")
                    out.append(f"- parent response: `{seq['receive_parent_response']}`")
                    out.append(f"- child id request: `{seq['send_child_id_request']}`")
                    out.append(f"- child id response: `{seq['receive_child_id_response']}`")
                    out.append(f"- parent ipv6: `{seq['parent_ipv6']}`")
                    out.append(f"- parent extaddr: `{seq['parent_extaddr']}`")
                    out.append(f"- parent rloc16: `{seq['parent_rloc16']}`")
                    out.append(f"- request -> response: **{seq['timing_ms']['parent_request_to_response']} ms**")
                    out.append(f"- response -> child id request: **{seq['timing_ms']['parent_response_to_child_id_request']} ms**")
                    out.append(f"- child id request -> response: **{seq['timing_ms']['child_id_request_to_response']} ms**")
                    out.append(f"- full attach quartet: **{seq['timing_ms']['parent_request_to_child_id_response']} ms**")
                    out.append("")

            failed = result["failed_tx"]
            out.append("#### Failed TX summary")
            out.append("")
            out.append(f"- failed tx attempts: **{failed['total_failed_attempts']}**")
            out.append(f"- highest attempt number seen: **{failed['max_attempt_seen']}/{failed['max_attempt_limit_seen']}**")
            if failed["by_seqnum"]:
                seq_summary = ", ".join(f"seq {seqnum}: {count}" for seqnum, count in sorted(failed["by_seqnum"].items(), key=lambda item: int(item[0])))
                out.append(f"- failed tx by seqnum: {seq_summary}")
            if failed["by_dst"]:
                dst_summary = ", ".join(f"`{dst}`: {count}" for dst, count in sorted(failed["by_dst"].items()))
                out.append(f"- failed tx by dst: {dst_summary}")
            out.append("")

    return "\n".join(out)


def print_text_report(results: list[dict[str, Any]]) -> None:
    print(render_text_report(results), end="")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    logs_dir = args.logs_dir.resolve()
    log_paths = sorted(Path(path) for path in glob.glob(str(logs_dir / "*.log")))
    results = [analyze_log(path) for path in log_paths]

    if args.json:
        output = json.dumps(results, indent=2)
    elif args.markdown or args.write_markdown:
        output = render_markdown_report(results)
    else:
        output = render_text_report(results)

    if args.write_markdown:
        args.write_markdown.parent.mkdir(parents=True, exist_ok=True)
        args.write_markdown.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
