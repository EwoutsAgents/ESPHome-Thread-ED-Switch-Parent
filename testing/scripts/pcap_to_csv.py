#!/usr/bin/env python3
"""
pcap_to_csv.py

For each input .pcap/.pcapng, write two CSVs alongside the PCAP file by default:

  <pcap_dir>/all_packets.csv
  <pcap_dir>/attach_mle.csv

all_packets.csv:
  one row per packet in that PCAP.

attach_mle.csv:
  only decoded MLE attach packets:
    - Parent Request       mle.cmd == 9
    - Parent Response      mle.cmd == 10
    - Child ID Request     mle.cmd == 11
    - Child ID Response    mle.cmd == 12

This version also auto-adds MLE Challenge/Response TLV fields if your local tshark exposes them.
It discovers them from `tshark -G fields`, so it does not depend on guessing exact Wireshark field names.

Examples:

  export THREAD_NETWORK_KEY=<32_hex_thread_network_key>

  # One run: writes next to the PCAP.
  python3 testing/scripts/pcap_to_csv.py \
    testing/logs/stock-2router-100runs-20260622-141453/20260622-142051-run02/802154-20260622-142110.pcapng

  # Whole experiment: writes all_packets.csv and attach_mle.csv inside each run directory.
  python3 testing/scripts/pcap_to_csv.py \
    testing/logs/stock-2router-100runs-20260622-141453

  # Show which MLE TLV fields were auto-added.
  python3 testing/scripts/pcap_to_csv.py \
    testing/logs/stock-2router-100runs-20260622-141453/20260622-142051-run02/802154-20260622-142110.pcapng \
    --list-added-fields
"""

from __future__ import annotations

import argparse
import csv
import io
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ATTACH_MLE_COMMAND_NAMES = {
    "9": "Parent Request",
    "10": "Parent Response",
    "11": "Child ID Request",
    "12": "Child ID Response",
}


BASE_FIELDS = [
    # Generic packet metadata.
    "frame.number",
    "frame.time_epoch",
    "frame.time",
    "frame.len",
    "frame.protocols",
    "_ws.col.Protocol",
    "_ws.col.Info",

    # IEEE 802.15.4.
    "wpan.frame_type",
    "wpan.seq_no",
    "wpan.src64",
    "wpan.dst64",
    "wpan.src16",
    "wpan.dst16",
    "wpan.src_pan",
    "wpan.dst_pan",
    "wpan.fcs.status",

    # IPv6 / UDP after 6LoWPAN + Thread decryption.
    "ipv6.src",
    "ipv6.dst",
    "udp.srcport",
    "udp.dstport",

    # Thread / MLE.
    "mle.cmd",

    # Useful if exposed by your tshark build.
    "mle.tlv.type",
    "mle.tlv.length",

    # Other useful high-level protocols if present.
    "coap.code",
    "coap.mid",
    "icmpv6.type",
    "icmpv6.code",
]


# Explicit candidates seen across Wireshark versions. Unsupported ones are ignored.
EXPLICIT_MLE_TLV_CANDIDATES = [
    "mle.tlv.challenge",
    "mle.tlv.response",
    "mle.challenge",
    "mle.response",
]


@dataclass(frozen=True)
class TSharkField:
    abbrev: str
    name: str
    parent: str


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def normalize_network_key(key: str) -> str:
    key = key.strip().replace("0x", "").replace("0X", "")
    key = key.replace(":", "").replace("-", "").replace(" ", "")
    if not re.fullmatch(r"[0-9a-fA-F]{32}", key):
        raise SystemExit(
            "Network key must be 16 bytes / 32 hex chars, "
            "e.g. dfd34f0f05cad978ec4e32b0413038ff"
        )
    return key.lower()


def parse_tshark_fields(tshark: str) -> dict[str, TSharkField]:
    proc = run([tshark, "-G", "fields"])
    fields: dict[str, TSharkField] = {}

    for line in proc.stdout.splitlines():
        parts = line.split("\t")
        # Field lines look like:
        # F <name> <abbrev> <type> <parent> ...
        if len(parts) >= 5 and parts[0] == "F":
            name = parts[1]
            abbrev = parts[2]
            parent = parts[4]
            fields[abbrev] = TSharkField(abbrev=abbrev, name=name, parent=parent)

    return fields


def discover_mle_challenge_response_fields(field_map: dict[str, TSharkField]) -> list[str]:
    """
    Find MLE fields related to Challenge/Response TLVs.

    We match both the abbreviation and display name because Wireshark field names can differ
    across versions.
    """
    selected: list[str] = []

    # Start with explicit candidates, preserving this order.
    for candidate in EXPLICIT_MLE_TLV_CANDIDATES:
        if candidate in field_map and candidate not in selected:
            selected.append(candidate)

    # Add discovered MLE fields whose abbrev/name mention challenge/response.
    for abbrev, field in sorted(field_map.items()):
        haystack = f"{abbrev} {field.name}".lower()
        is_mle = abbrev.startswith("mle.") or field.parent == "mle"

        if not is_mle:
            continue

        if ("challenge" in haystack or "response" in haystack) and abbrev not in selected:
            selected.append(abbrev)

    return selected


def build_decode_prefs(network_key: str | None) -> list[str]:
    prefs = [
        "-o", "wpan.802154_fcs_ok:FALSE",
        "-o", "wpan.802154_sec_suite:AES-128 Encryption, 32-bit Integrity Protection",
        "-o", "thread.thr_seq_ctr:00000000",
    ]

    if network_key:
        key = normalize_network_key(network_key)
        prefs.extend(["-o", f'uat:ieee802154_keys:"{key}","1","Thread hash"'])

    return prefs


def discover_pcaps(inputs: list[Path], pattern: str, recursive: bool) -> list[Path]:
    pcaps: list[Path] = []

    for item in inputs:
        if item.is_file():
            pcaps.append(item)
        elif item.is_dir():
            iterator = item.rglob(pattern) if recursive else item.glob(pattern)
            pcaps.extend(p for p in iterator if p.is_file())
        else:
            print(f"Warning: input path does not exist and will be skipped: {item}", file=sys.stderr)

    return sorted({p.resolve() for p in pcaps})


def frame_range_filter(frame_range: str | None) -> str | None:
    if not frame_range:
        return None

    start_s, end_s = frame_range.split(":", 1)
    start = int(start_s)
    end = int(end_s)
    return f"(frame.number >= {start} && frame.number <= {end})"


def and_filter(*terms: str | None) -> str | None:
    kept = [f"({term})" for term in terms if term]
    return " && ".join(kept) if kept else None


def attach_filter(extra_filter: str | None = None, frame_filter: str | None = None) -> str:
    attach = "(mle.cmd == 9 || mle.cmd == 10 || mle.cmd == 11 || mle.cmd == 12)"
    return and_filter(attach, extra_filter, frame_filter) or attach


def all_packets_filter(extra_filter: str | None = None, frame_filter: str | None = None) -> str | None:
    return and_filter(extra_filter, frame_filter)


def tshark_export(
    tshark: str,
    pcap: Path,
    fields: Iterable[str],
    prefs: list[str],
    display_filter: str | None,
    aggregator: str,
) -> list[dict[str, str]]:
    cmd = [tshark, "-r", str(pcap), *prefs]

    if display_filter:
        cmd.extend(["-Y", display_filter])

    cmd.extend([
        "-T", "fields",
        "-E", "header=y",
        "-E", "separator=,",
        "-E", "quote=d",
        "-E", "occurrence=a",
        "-E", f"aggregator={aggregator}",
    ])

    for field in fields:
        cmd.extend(["-e", field])

    proc = run(cmd, check=False)
    if proc.returncode != 0:
        raise RuntimeError(
            f"tshark failed for {pcap}\n\n"
            f"Command:\n{' '.join(cmd)}\n\n"
            f"stderr:\n{proc.stderr}"
        )

    if not proc.stdout.strip():
        return []

    reader = csv.DictReader(io.StringIO(proc.stdout))
    return list(reader)


def add_context_columns(rows: list[dict[str, str]], pcap: Path) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []

    for row in rows:
        enriched = {
            "pcap": str(pcap),
            "pcap_name": pcap.name,
            "run_dir": pcap.parent.name,
        }
        enriched.update(row)

        cmd = (row.get("mle.cmd") or "").strip()
        # occurrence=a can join multiple commands with the aggregator, but for MLE command it should
        # normally be one value.
        enriched["mle.command_name"] = ATTACH_MLE_COMMAND_NAMES.get(cmd, "")

        out.append(enriched)

    return out


def ordered_fieldnames(fields: list[str]) -> list[str]:
    return [
        "pcap",
        "pcap_name",
        "run_dir",
        *fields,
        "mle.command_name",
    ]


def write_rows(path: Path, rows: list[dict[str, str]], fieldnames: list[str], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"{path} already exists. Use --overwrite to replace it.")

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def output_paths_for_pcap(pcap: Path, args: argparse.Namespace) -> tuple[Path, Path]:
    if args.out_dir:
        safe_stem = pcap.with_suffix("").name
        all_path = args.out_dir / f"{pcap.parent.name}-{safe_stem}-{args.all_name}"
        attach_path = args.out_dir / f"{pcap.parent.name}-{safe_stem}-{args.attach_name}"
        return all_path, attach_path

    # Default: write alongside the PCAP.
    return pcap.parent / args.all_name, pcap.parent / args.attach_name


def build_fields(field_map: dict[str, TSharkField], include_mle_challenge_response: bool) -> tuple[list[str], list[str]]:
    supported = set(field_map.keys())

    fields: list[str] = []
    for field in BASE_FIELDS:
        if field in supported and field not in fields:
            fields.append(field)

    added_mle_fields: list[str] = []
    if include_mle_challenge_response:
        added_mle_fields = discover_mle_challenge_response_fields(field_map)
        for field in added_mle_fields:
            if field in supported and field not in fields:
                fields.append(field)

    return fields, added_mle_fields


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write all_packets.csv and attach_mle.csv alongside each input PCAP."
    )
    parser.add_argument("inputs", nargs="+", type=Path, help="Input PCAP file(s) or directory/directories")
    parser.add_argument(
        "--network-key",
        default=os.environ.get("THREAD_NETWORK_KEY"),
        help="Thread network key, 16 bytes / 32 hex chars. Can also use THREAD_NETWORK_KEY env var.",
    )
    parser.add_argument("--glob", default="*.pcapng", help="Glob for directory inputs. Default: *.pcapng")
    parser.add_argument("--no-recursive", action="store_true", help="Do not recursively search directory inputs")
    parser.add_argument("--frame-range", help="Optional frame range applied to both outputs, e.g. 183:194")
    parser.add_argument("--filter", dest="extra_filter", help="Optional extra Wireshark display filter applied to both outputs")
    parser.add_argument("--all-name", default="all_packets.csv", help="Filename for the all-packets CSV")
    parser.add_argument("--attach-name", default="attach_mle.csv", help="Filename for the attach-MLE CSV")
    parser.add_argument("--out-dir", type=Path, help="Optional central output dir. Omit this to write alongside each PCAP.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing CSV files")
    parser.add_argument("--tshark", default="tshark", help="Path to tshark binary")
    parser.add_argument(
        "--no-mle-challenge-response",
        action="store_true",
        help="Do not auto-add MLE challenge/response TLV fields.",
    )
    parser.add_argument(
        "--list-added-fields",
        action="store_true",
        help="Print auto-added MLE challenge/response fields and exit if no input PCAPs are needed.",
    )
    parser.add_argument(
        "--aggregator",
        default="|",
        help="Separator used when tshark returns multiple values for one field. Default: |",
    )
    args = parser.parse_args()

    tshark_path = shutil.which(args.tshark) or args.tshark

    try:
        field_map = parse_tshark_fields(tshark_path)
    except Exception as e:
        raise SystemExit(f"Could not run tshark. Is Wireshark/tshark installed?\n{e}")

    fields, added_mle_fields = build_fields(
        field_map=field_map,
        include_mle_challenge_response=not args.no_mle_challenge_response,
    )

    unsupported_base_fields = [field for field in BASE_FIELDS if field not in field_map]
    if unsupported_base_fields:
        print(f"Warning: unsupported tshark fields omitted: {unsupported_base_fields}", file=sys.stderr)

    if args.list_added_fields:
        print("Auto-added MLE challenge/response fields:")
        if added_mle_fields:
            for field in added_mle_fields:
                meta = field_map[field]
                print(f"  {field}  # {meta.name}")
        else:
            print("  none")

    if "mle.cmd" not in fields:
        print(
            "Warning: this tshark build does not expose 'mle.cmd'. "
            "attach_mle.csv will probably be empty.",
            file=sys.stderr,
        )

    pcaps = discover_pcaps(args.inputs, args.glob, recursive=not args.no_recursive)
    if not pcaps:
        raise SystemExit("No PCAP/PCAPNG files found.")

    prefs = build_decode_prefs(args.network_key)
    frame_filter = frame_range_filter(args.frame_range)
    all_filter = all_packets_filter(args.extra_filter, frame_filter)
    mle_filter = attach_filter(args.extra_filter, frame_filter)
    fieldnames = ordered_fieldnames(fields)

    failures = 0

    for i, pcap in enumerate(pcaps, start=1):
        all_path, attach_path = output_paths_for_pcap(pcap, args)

        try:
            all_rows = add_context_columns(
                tshark_export(tshark_path, pcap, fields, prefs, all_filter, args.aggregator),
                pcap,
            )
            attach_rows = add_context_columns(
                tshark_export(tshark_path, pcap, fields, prefs, mle_filter, args.aggregator),
                pcap,
            )

            write_rows(all_path, all_rows, fieldnames, overwrite=args.overwrite)
            write_rows(attach_path, attach_rows, fieldnames, overwrite=args.overwrite)

        except Exception as e:
            failures += 1
            print(f"[{i}/{len(pcaps)}] FAILED {pcap}: {e}", file=sys.stderr)
            continue

        print(f"[{i}/{len(pcaps)}] {pcap}")
        print(f"  wrote {all_path} ({len(all_rows)} rows)")
        print(f"  wrote {attach_path} ({len(attach_rows)} rows)")

    if added_mle_fields:
        print("\nIncluded MLE challenge/response fields:")
        for field in added_mle_fields:
            print(f"  {field}")

    if failures:
        print(f"\nCompleted with {failures} failed PCAP(s).", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
