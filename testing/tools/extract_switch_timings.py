#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
from pathlib import Path

PATTERNS = {
    'T0_request': re.compile(r'(T0 request|Requested Thread parent switch)'),
    'T1_discovery_start': re.compile(r'(T1 search started|Parent discovery attempt|Status changed to discovering parents)'),
    'T2_target_observed': re.compile(r'(target observed after|preferred parent .* matched|Thread parent switch succeeded; current parent is)'),
    'T3_attach_start': re.compile(r'(starting selected-parent attach|Starting selected-parent attach|already selected|Attach result: success after 0 ms)'),
    'T4_child_id_req': re.compile(r'(Child ID Request sent|SelectedParent ChildIdRequest sent|SendChildIdRequest|selected-parent attach in progress|Attach result: success after 0 ms)'),
    'T5_attach_done': re.compile(r'(Thread parent switch succeeded|Attach result: success)'),
    'T6_parent_match': re.compile(r'(current parent is)'),
}

# Common cross-variant metrics (same schema for stock + variant-mcast + variant-ucast)
COMMON_PATTERNS = {
    'C0_request': re.compile(r'(T0 request|Requested Thread parent switch)'),
    'C1_workflow_start': re.compile(r'(T1 search started|Status changed to discovering parents|Parent discovery attempt)'),
    'C2_switch_success': re.compile(r'(Thread parent switch succeeded|Attach result: success)'),
    'C3_final_parent_match': re.compile(r'(current parent is)'),
}

TS_PREFIX = re.compile(r'^(?P<ts>\d{4}-\d{2}-\d{2}T[^ ]+)\s+\[(?P<label>[^\]]+)\]\s+(?P<msg>.*)$')


def parse_ts(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace('Z', '+00:00'))


def main() -> int:
    parser = argparse.ArgumentParser(description='Extract parent-switch timing checkpoints from captured logs.')
    parser.add_argument('--in', dest='infile', type=Path, required=True)
    parser.add_argument('--label', default='child', help='Node label to analyze (from capture prefix).')
    parser.add_argument('--out', type=Path, default=Path('testing/logs/switch_timings.csv'))
    args = parser.parse_args()

    events: dict[str, dt.datetime] = {}

    for line in args.infile.read_text(encoding='utf-8', errors='ignore').splitlines():
        m = TS_PREFIX.match(line)
        if not m:
            continue
        if m.group('label') != args.label:
            continue

        ts = parse_ts(m.group('ts'))
        msg = m.group('msg')
        for key, pattern in PATTERNS.items():
            if key not in events and pattern.search(msg):
                events[key] = ts
        for key, pattern in COMMON_PATTERNS.items():
            if key not in events and pattern.search(msg):
                events[key] = ts

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['checkpoint', 'timestamp_utc', 'delta_ms_from_t0'])
        t0 = events.get('T0_request')
        for key in [
            'T0_request', 'T1_discovery_start', 'T2_target_observed', 'T3_attach_start', 'T4_child_id_req', 'T5_attach_done', 'T6_parent_match',
            'C0_request', 'C1_workflow_start', 'C2_switch_success', 'C3_final_parent_match',
        ]:
            ts = events.get(key)
            if ts is None:
                writer.writerow([key, '', ''])
            else:
                delta = '' if t0 is None else int((ts - t0).total_seconds() * 1000)
                writer.writerow([key, ts.isoformat(), delta])

    print(f'Wrote {args.out}')
    for k in [*PATTERNS.keys(), *COMMON_PATTERNS.keys()]:
        print(f'{k}: {events.get(k).isoformat() if k in events else "<missing>"}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
