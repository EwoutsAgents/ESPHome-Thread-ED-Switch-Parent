#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
from pathlib import Path

VARIANT_PATTERNS = {
    "T0_request": re.compile(r"(T0 request|Requested Thread parent switch)"),
    "T1_discovery_start": re.compile(r"(T1 search started|Parent discovery attempt|Status changed to discovering parents)"),
    "T2_target_observed": re.compile(r"(target observed after|preferred parent .* matched|Thread parent switch succeeded; current parent is)"),
    "T3_attach_start": re.compile(r"(starting selected-parent attach|Starting selected-parent attach|already selected|Attach result: success after 0 ms)"),
    "T4_child_id_req": re.compile(r"(Child ID Request sent|SelectedParent ChildIdRequest sent|SendChildIdRequest|selected-parent attach in progress|Attach result: success after 0 ms)"),
    "T5_attach_done": re.compile(r"(Thread parent switch succeeded|Attach result: success)"),
    "T6_parent_match": re.compile(r"(current parent is)"),
}

STOCK_OBSERVED_PATTERNS = {
    "SO0_request": re.compile(r"SO0 request"),
    "SO1_search_started": re.compile(r"SO1 search started"),
    "SO2_parent_response_observed": re.compile(r"SO2 parent response observed"),
    "SO3_target_parent_response_observed": re.compile(r"SO3 target parent response observed"),
    "SO4_parent_changed": re.compile(r"SO4 parent changed"),
    "SO5_target_parent_reached": re.compile(r"SO5 target parent reached"),
    "SO6_timeout_or_failure": re.compile(r"SO6 (timeout|failure)"),
}

COMMON_PATTERNS = {
    "C0_request": re.compile(r"(SO0 request|T0 request|Requested Thread parent switch)"),
    "C1_workflow_started": re.compile(
        r"(SO1 search started|T1 search started|Parent discovery attempt|Status changed to discovering parents)"
    ),
    "C2_target_reached": re.compile(
        r"(SO5 target parent reached|Thread parent switch succeeded; current parent is)"
    ),
}

TS_PREFIX = re.compile(r"^(?P<ts>\d{4}-\d{2}-\d{2}T[^ ]+)\s+\[(?P<label>[^\]]+)\]\s+(?P<msg>.*)$")

SCENARIOS = {
    "stock-observed": [*STOCK_OBSERVED_PATTERNS.keys(), *COMMON_PATTERNS.keys()],
    "variant-mcast": [*VARIANT_PATTERNS.keys(), *COMMON_PATTERNS.keys()],
    "variant-ucast": [*VARIANT_PATTERNS.keys(), *COMMON_PATTERNS.keys()],
    "stock": ["T0_request", "T1_discovery_start", "C0_request", "C1_workflow_started"],
    "auto": [*VARIANT_PATTERNS.keys(), *STOCK_OBSERVED_PATTERNS.keys(), *COMMON_PATTERNS.keys()],
}


def parse_ts(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract parent-switch timing checkpoints from captured logs.")
    parser.add_argument("--in", dest="infile", type=Path, required=True)
    parser.add_argument("--label", default="child", help="Node label to analyze (from capture prefix).")
    parser.add_argument("--scenario", choices=list(SCENARIOS.keys()), default="auto")
    parser.add_argument("--mode", default="steady")
    parser.add_argument("--out", type=Path, default=Path("testing/logs/switch_timings.csv"))
    args = parser.parse_args()

    events: dict[str, dt.datetime] = {}

    all_patterns: dict[str, re.Pattern[str]] = {}
    all_patterns.update(VARIANT_PATTERNS)
    all_patterns.update(STOCK_OBSERVED_PATTERNS)
    all_patterns.update(COMMON_PATTERNS)

    selected_events = SCENARIOS[args.scenario]

    for line in args.infile.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = TS_PREFIX.match(line)
        if not m or m.group("label") != args.label:
            continue

        ts = parse_ts(m.group("ts"))
        msg = m.group("msg")
        for key in selected_events:
            if key not in events and all_patterns[key].search(msg):
                events[key] = ts

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["scenario", "mode", "checkpoint", "timestamp_utc", "delta_ms_from_c0", "source_log"])
        c0 = events.get("C0_request")
        for key in selected_events:
            ts = events.get(key)
            if ts is None:
                writer.writerow([args.scenario, args.mode, key, "", "", str(args.infile)])
            else:
                delta = "" if c0 is None else int((ts - c0).total_seconds() * 1000)
                writer.writerow([args.scenario, args.mode, key, ts.isoformat(), delta, str(args.infile)])

    print(f"Wrote {args.out}")
    for key in selected_events:
        print(f"{key}: {events.get(key).isoformat() if key in events else '<missing>'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
