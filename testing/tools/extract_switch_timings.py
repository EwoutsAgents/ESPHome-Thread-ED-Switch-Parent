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
    "T3_attach_start": re.compile(r"T3 selected-parent attach start(?:; target=.*)?"),
    "T4_child_id_req": re.compile(r"(Child ID Request sent|SelectedParent ChildIdRequest sent|SendChildIdRequest|selected-parent attach in progress)"),
    "T5_attach_done": re.compile(r"(Thread parent switch succeeded|Attach result: success)"),
    "T6_parent_match": re.compile(r"(current parent is)"),
    "V_immediate_parent_match": re.compile(r"T_success_immediate_parent_match"),
}

STOCK_OBSERVED_PATTERNS = {
    "SO0_request": re.compile(r"SO0 (request|current-parent-off prepare)"),
    "SO1_search_started": re.compile(r"SO1 search started"),
    "SO2_parent_response_observed": re.compile(r"SO2 parent response observed"),
    "SO3_target_parent_response_observed": re.compile(r"SO3 target parent response observed"),
    "SO4_parent_changed": re.compile(r"SO4 parent changed"),
    "SO5_target_parent_reached": re.compile(r"SO5 target parent reached"),
    "SO6_timeout_or_failure": re.compile(r"SO6 (timeout|failure)"),
    "SO_invalid_instrumentation": re.compile(r"SO6 failure; invalid instrumentation"),
}

COMMON_PATTERNS = {
    "C0_request": re.compile(r"(SO0 request|SO0 current-parent-off prepare|T0 request|Requested Thread parent switch)"),
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

META_PATTERNS = {
    "classification": re.compile(r"^#\s*classification\s+(.+)$"),
    "initial_parent_extaddr": re.compile(r"^#\s*current-parent-extaddr\s+([0-9a-fA-F]{16})$"),
    "initial_parent_rloc16": re.compile(r"^#\s*current-parent-rloc16\s+(0x[0-9a-fA-F]{4})$"),
    "disabled_router_label": re.compile(r"^#\s*disabled-router-label\s+(\S+)$"),
    "disable_method": re.compile(r"^#\s*disable-method\s+(\S+)$"),
    "disable_start": re.compile(r"^#\s*disable-start\s+(.+)$"),
    "disable_end": re.compile(r"^#\s*disable-end\s+(.+)$"),
    "variant_preconditioning_method": re.compile(r"^#\s*variant-preconditioning-method\s+(\S+)$"),
    "variant_target_parent_extaddr": re.compile(r"^#\s*variant-target-parent-extaddr\s+([0-9a-fA-F]{16})$"),
    "variant_initial_parent_extaddr": re.compile(r"^#\s*variant-initial-parent-extaddr\s+([0-9a-fA-F]{16})$"),
    "variant_precondition_result": re.compile(r"^#\s*variant-precondition-result\s+(\S+)$"),
    "variant_target_suppression_start": re.compile(r"^#\s*variant-target-suppression-start\s+(.+)$"),
    "variant_target_suppression_end": re.compile(r"^#\s*variant-target-suppression-end\s+(.+)$"),
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
    meta: dict[str, str] = {
        "classification": "",
        "initial_parent_extaddr": "",
        "initial_parent_rloc16": "",
        "disabled_router_label": "",
        "disable_method": "",
        "disable_start": "",
        "disable_end": "",
        "variant_preconditioning_method": "",
        "variant_target_parent_extaddr": "",
        "variant_initial_parent_extaddr": "",
        "variant_precondition_result": "",
        "variant_target_suppression_start": "",
        "variant_target_suppression_end": "",
    }

    input_text = args.infile.read_text(encoding="utf-8", errors="ignore")

    all_patterns: dict[str, re.Pattern[str]] = {}
    all_patterns.update(VARIANT_PATTERNS)
    all_patterns.update(STOCK_OBSERVED_PATTERNS)
    all_patterns.update(COMMON_PATTERNS)

    selected_events = SCENARIOS[args.scenario]

    for line in input_text.splitlines():
        for key, pat in META_PATTERNS.items():
            mm = pat.match(line)
            if mm:
                meta[key] = mm.group(1).strip()

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
        writer.writerow([
            "scenario", "mode", "checkpoint", "timestamp_utc", "delta_ms_from_c0", "delta_ms_from_attach_start", "disruption_time_utc", "delta_ms_from_disruption", "delta_ms_from_search_start", "source_log", "classification",
            "initial_parent_extaddr", "target_parent_extaddr", "disabled_router_label", "disable_method", "variant_preconditioning_method", "variant_precondition_result", "variant_target_suppression_start", "variant_target_suppression_end"
        ])
        c0 = events.get("C0_request")
        t3 = events.get("T3_attach_start")
        so1 = events.get("SO1_search_started")
        disruption_ts = parse_ts(meta["disable_start"]) if meta["disable_start"] else None

        classification = meta["classification"]
        if not classification:
            if args.scenario == "stock-observed" and "SO_invalid_instrumentation" in events:
                classification = "invalid_instrumentation"
            elif args.mode in ("current-parent-off", "forced-current-parent-off"):
                if "SO5_target_parent_reached" in events:
                    classification = "success_target_reached"
                elif "SO6_timeout_or_failure" in events:
                    classification = "timeout_target_not_reached"
        target_parent_extaddr = ""
        m_target = re.search(r"SO0 (?:current-parent-off prepare; |request; )target=([0-9a-fA-F]{16})", input_text)
        if m_target:
            target_parent_extaddr = m_target.group(1).lower()
        if not target_parent_extaddr and args.scenario.startswith("variant"):
            if meta["variant_target_parent_extaddr"]:
                target_parent_extaddr = meta["variant_target_parent_extaddr"].lower()
            else:
                m_target = re.search(r"Configured preferred parent by extended address: ([0-9a-fA-F]{16})", input_text)
                if m_target:
                    target_parent_extaddr = m_target.group(1).lower()

        if args.scenario.startswith("variant"):
            if meta["variant_initial_parent_extaddr"]:
                meta["initial_parent_extaddr"] = meta["variant_initial_parent_extaddr"].lower()
            else:
                m_initial = re.search(r"V_initial_parent_extaddr=([0-9a-fA-F]{16})", input_text)
                if m_initial:
                    meta["initial_parent_extaddr"] = m_initial.group(1).lower()

            if meta["variant_precondition_result"] == "target_still_current":
                classification = "precondition_failed_initial_parent_is_target"
            elif meta["variant_precondition_result"] == "reset_failed" and not classification:
                classification = "timeout_or_failure"
            elif meta["variant_precondition_result"] == "initial_parent_unknown" and not classification:
                classification = "timeout_or_failure"
            elif meta["variant_precondition_result"] == "non_target_confirmed" and "T3_attach_start" in events and "T6_parent_match" in events:
                classification = "success_switch_act"
            elif "V_immediate_parent_match" in events and "T6_parent_match" in events and "T3_attach_start" not in events:
                classification = "immediate_parent_match_no_switch"
            elif meta["initial_parent_extaddr"] and target_parent_extaddr and meta["initial_parent_extaddr"].lower() == target_parent_extaddr.lower():
                classification = "invalid_initial_parent_is_target"
            elif "T6_parent_match" not in events:
                classification = "timeout_or_failure"
            elif not classification:
                classification = "unclassified"

        for key in selected_events:
            ts = events.get(key)
            if ts is None:
                writer.writerow([
                    args.scenario, args.mode, key, "", "", "", meta["disable_start"], "", "", str(args.infile), classification,
                    meta["initial_parent_extaddr"], target_parent_extaddr, meta["disabled_router_label"], meta["disable_method"], meta["variant_preconditioning_method"], meta["variant_precondition_result"], meta["variant_target_suppression_start"], meta["variant_target_suppression_end"]
                ])
            else:
                delta = "" if c0 is None else int((ts - c0).total_seconds() * 1000)
                delta_attach = "" if t3 is None else int((ts - t3).total_seconds() * 1000)
                delta_disruption = "" if disruption_ts is None else int((ts - disruption_ts).total_seconds() * 1000)
                delta_search = "" if so1 is None else int((ts - so1).total_seconds() * 1000)
                writer.writerow([
                    args.scenario, args.mode, key, ts.isoformat(), delta, delta_attach, meta["disable_start"], delta_disruption, delta_search, str(args.infile), classification,
                    meta["initial_parent_extaddr"], target_parent_extaddr, meta["disabled_router_label"], meta["disable_method"], meta["variant_preconditioning_method"], meta["variant_precondition_result"], meta["variant_target_suppression_start"], meta["variant_target_suppression_end"]
                ])

    print(f"Wrote {args.out}")
    for key in selected_events:
        print(f"{key}: {events.get(key).isoformat() if key in events else '<missing>'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
