#!/usr/bin/env python3
"""
pcap_to_csv.py

Create exactly two aggregate CSV files from one or many IEEE 802.15.4 / Thread PCAPs:

  1. all_packets.csv
     One row per packet from every PCAP.

  2. attach_mle.csv
     One row per decoded MLE attach packet:
       - Parent Request
       - Parent Response
       - Child ID Request
       - Child ID Response

Typical batch use:
  export THREAD_NETWORK_KEY=<32_hex_thread_network_key>

  python3 testing/scripts/pcap_to_csv.py \
    testing/logs/stock-2router-100runs-20260622-141453 \
    --out-dir testing/logs/stock-2router-100runs-20260622-141453/pcap_csv

Typical single-run use:
  python3 testing/scripts/pcap_to_csv.py \
    testing/logs/stock-2router-100runs-20260622-141453/20260622-142051-run02/802154-20260622-142110.pcapng \
    --network-key <32_hex_thread_network_key> \
    --out-dir /tmp/run02_pcap_csv

Notes:
  - "all_packets.csv" means every packet as a CSV row using a useful fixed field set.
  - It does not export every possible nested Wireshark protocol-tree field.
  - If attach_mle.csv is empty, Thread/MLE is probably not decrypted/dissected.
  - Hex key in the test setup is: dfd34f0f05cad978ec4e32b0413038ff
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
from pathlib import Path
from typing import Iterable


ATTACH_MLE_COMMAND_NAMES = {
    "9": "Parent Request",
    "10": "Parent Response",
    "11": "Child ID Request",
    "12": "Child ID Response",
}


# Keep this fixed and practical. Unsupported fields are automatically omitted.
DEFAULT_FIELDS = [
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

    # Other useful high-level protocols if present.
    "coap.code",
    "coap.mid",
    "icmpv6.type",
    "icmpv6.code",
]


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def normalize_network_key(key: str) -> str:
    key = key.strip().replace(":", "").replace("-", "").replace(" ", "")
    if not re.fullmatch(r"[0-9a-fA-F]{32}", key):
        raise SystemExit(
            "Network key must be 16 bytes / 32 hex chars, "
            "e.g. 00112233445566778899aabbccddeeff"
        )
    return key.lower()


def parse_tshark_fields(tshark: str) -> set[str]:
    proc = run([tshark, "-G", "fields"])
    fields: set[str] = set()
    for line in proc.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) >= 3 and parts[0] == "F":
            fields.add(parts[2])
    return fields


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
) -> list[dict[str, str]]:
    cmd = [tshark, "-r", str(pcap), *prefs]

    if display_filter:
        cmd.extend(["-Y", display_filter])

    cmd.extend([
        "-T", "fields",
        "-E", "header=y",
        "-E", "separator=,",
        "-E", "quote=d",
        "-E", "occurrence=f",
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


def add_context_columns(rows: list[dict[str, str]], pcap: Path, root: Path | None) -> list[dict[str, str]]:
    try:
        rel = str(pcap.relative_to(root)) if root else str(pcap)
    except ValueError:
        rel = str(pcap)

    run_dir = pcap.parent.name

    out: list[dict[str, str]] = []
    for row in rows:
        enriched = {
            "pcap": str(pcap),
            "pcap_relative": rel,
            "pcap_name": pcap.name,
            "run_dir": run_dir,
        }
        enriched.update(row)

        cmd = (row.get("mle.cmd") or "").strip()
        enriched["mle.command_name"] = ATTACH_MLE_COMMAND_NAMES.get(cmd, "")

        out.append(enriched)

    return out


def write_rows(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def ordered_fieldnames(fields: list[str]) -> list[str]:
    return [
        "pcap",
        "pcap_relative",
        "pcap_name",
        "run_dir",
        *fields,
        "mle.command_name",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create one all-packets CSV and one attach-MLE CSV from PCAP/PCAPNG files."
    )
    parser.add_argument("inputs", nargs="+", type=Path, help="Input PCAP file(s) or directory/directories")
    parser.add_argument("--network-key", default=os.environ.get("THREAD_NETWORK_KEY"), help="Thread network key, 16 bytes / 32 hex chars. Can also use THREAD_NETWORK_KEY env var.")
    parser.add_argument("--out-dir", type=Path, default=Path("pcap_csv"), help="Output directory")
    parser.add_argument("--all-out", type=Path, help="Output path for every-packet CSV. Default: <out-dir>/all_packets.csv")
    parser.add_argument("--attach-out", type=Path, help="Output path for attach-MLE CSV. Default: <out-dir>/attach_mle.csv")
    parser.add_argument("--glob", default="*.pcapng", help="Glob for directory inputs. Default: *.pcapng")
    parser.add_argument("--no-recursive", action="store_true", help="Do not recursively search directory inputs")
    parser.add_argument("--frame-range", help="Optional frame range applied to both outputs, e.g. 183:194")
    parser.add_argument("--filter", dest="extra_filter", help="Optional extra Wireshark display filter applied to both outputs")
    parser.add_argument("--tshark", default="tshark", help="Path to tshark binary")
    args = parser.parse_args()

    recursive = not args.no_recursive
    pcaps = discover_pcaps(args.inputs, args.glob, recursive)
    if not pcaps:
        raise SystemExit("No PCAP/PCAPNG files found.")

    tshark_path = shutil.which(args.tshark) or args.tshark

    try:
        supported_fields = parse_tshark_fields(tshark_path)
    except Exception as e:
        raise SystemExit(f"Could not run tshark. Is Wireshark/tshark installed?\n{e}")

    fields = [field for field in DEFAULT_FIELDS if field in supported_fields]
    missing_fields = [field for field in DEFAULT_FIELDS if field not in supported_fields]
    if missing_fields:
        print(f"Warning: unsupported tshark fields omitted: {missing_fields}", file=sys.stderr)

    if "mle.cmd" not in fields:
        print(
            "Warning: this tshark build does not expose 'mle.cmd'. "
            "attach_mle.csv will probably be empty unless your extra filter matches other fields.",
            file=sys.stderr,
        )

    prefs = build_decode_prefs(args.network_key)

    dir_inputs = [p for p in args.inputs if p.is_dir()]
    root = dir_inputs[0].resolve() if dir_inputs else pcaps[0].parent.resolve()

    frame_filter = frame_range_filter(args.frame_range)
    all_filter = all_packets_filter(args.extra_filter, frame_filter)
    mle_filter = attach_filter(args.extra_filter, frame_filter)

    all_out = args.all_out or (args.out_dir / "all_packets.csv")
    attach_out = args.attach_out or (args.out_dir / "attach_mle.csv")

    all_rows: list[dict[str, str]] = []
    attach_rows: list[dict[str, str]] = []

    failures = 0

    for i, pcap in enumerate(pcaps, start=1):
        try:
            pcap_all_rows = tshark_export(
                tshark=tshark_path,
                pcap=pcap,
                fields=fields,
                prefs=prefs,
                display_filter=all_filter,
            )
            pcap_attach_rows = tshark_export(
                tshark=tshark_path,
                pcap=pcap,
                fields=fields,
                prefs=prefs,
                display_filter=mle_filter,
            )
        except Exception as e:
            failures += 1
            print(f"[{i}/{len(pcaps)}] FAILED {pcap}: {e}", file=sys.stderr)
            continue

        pcap_all_rows = add_context_columns(pcap_all_rows, pcap, root)
        pcap_attach_rows = add_context_columns(pcap_attach_rows, pcap, root)

        all_rows.extend(pcap_all_rows)
        attach_rows.extend(pcap_attach_rows)

        print(
            f"[{i}/{len(pcaps)}] {pcap.name}: "
            f"all_packets={len(pcap_all_rows)} attach_mle={len(pcap_attach_rows)}"
        )

    fieldnames = ordered_fieldnames(fields)
    write_rows(all_out, all_rows, fieldnames)
    write_rows(attach_out, attach_rows, fieldnames)

    print(f"\nWrote all packets CSV: {all_out} ({len(all_rows)} rows)")
    print(f"Wrote attach MLE CSV:  {attach_out} ({len(attach_rows)} rows)")

    if attach_rows:
        counts: dict[str, int] = {}
        for row in attach_rows:
            name = row.get("mle.command_name") or row.get("mle.cmd") or "unknown"
            counts[name] = counts.get(name, 0) + 1

        print("\nAttach MLE counts:")
        for name, count in sorted(counts.items()):
            print(f"  {name}: {count}")
    else:
        print(
            "\nWarning: attach_mle.csv has zero rows. "
            "If you expected MLE frames, check the Thread network key and Wireshark/tshark decryption settings.",
            file=sys.stderr,
        )

    if failures:
        print(f"\nCompleted with {failures} failed PCAP(s).", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
