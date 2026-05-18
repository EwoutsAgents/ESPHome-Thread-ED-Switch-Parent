#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class Trial:
    path: Path
    classification: str
    initial_parent_extaddr: str
    target_parent_extaddr: str
    checkpoints: dict[str, dict[str, str]]

    @property
    def is_valid(self) -> bool:
        return (
            bool(self.initial_parent_extaddr)
            and bool(self.target_parent_extaddr)
            and self.initial_parent_extaddr != self.target_parent_extaddr
            and self.classification in {"success_target_reached", "timeout_target_not_reached"}
        )


def load_trial(path: Path) -> Trial | None:
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    if not rows:
        return None
    first = rows[0]
    checkpoints = {row["checkpoint"]: row for row in rows}
    return Trial(
        path=path,
        classification=first.get("classification", ""),
        initial_parent_extaddr=first.get("initial_parent_extaddr", "").lower(),
        target_parent_extaddr=first.get("target_parent_extaddr", "").lower(),
        checkpoints=checkpoints,
    )


def collect_values(trials: Iterable[Trial], checkpoint: str, field: str) -> list[int]:
    values: list[int] = []
    for trial in trials:
        row = trial.checkpoints.get(checkpoint)
        if row and row.get(field):
            values.append(int(row[field]))
    return values


def fmt_median(values: list[int]) -> str:
    return "N/A" if not values else str(statistics.median(values))


def extract_stamp(path: Path) -> str:
    match = re.search(r"(\d{8}-\d{6})-trial\d+$", path.stem)
    return match.group(1) if match else ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize stock-observed CSV batches.")
    parser.add_argument("--glob", required=True, help="Glob relative to repo root, e.g. testing/logs/stock-observed-steady-20260516-12*.csv")
    parser.add_argument("--field", default="delta_ms_from_search_start", choices=["delta_ms_from_c0", "delta_ms_from_search_start", "delta_ms_from_disruption"], help="Timing basis to summarize")
    parser.add_argument("--stamp-min", help="Inclusive minimum run stamp, e.g. 20260516-115511")
    parser.add_argument("--stamp-max", help="Inclusive maximum run stamp, e.g. 20260516-122728")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    paths = sorted(root.glob(args.glob))
    if args.stamp_min or args.stamp_max:
        filtered: list[Path] = []
        for path in paths:
            stamp = extract_stamp(path)
            if args.stamp_min and stamp < args.stamp_min:
                continue
            if args.stamp_max and stamp > args.stamp_max:
                continue
            filtered.append(path)
        paths = filtered
    trials = [trial for path in paths if (trial := load_trial(path)) is not None]
    valid_trials = [trial for trial in trials if trial.is_valid]

    print(f"glob: {args.glob}")
    print(f"timing_field: {args.field}")
    print(f"attempts: {len(trials)}")
    print(f"valid_trials: {len(valid_trials)}")
    print(f"success_target_reached: {sum(t.classification == 'success_target_reached' for t in valid_trials)}/{len(valid_trials)}")
    print(f"timeout_target_not_reached: {sum(t.classification == 'timeout_target_not_reached' for t in valid_trials)}/{len(valid_trials)}")

    checkpoint_names = [
        "SO2_parent_response_observed",
        "SO3_target_parent_response_observed",
        "SO4_parent_changed",
        "SO5_target_parent_reached",
        "SO6_timeout_or_failure",
    ]
    for checkpoint in checkpoint_names:
        values = collect_values(valid_trials, checkpoint, args.field)
        print(f"{checkpoint}: {len(values)}/{len(valid_trials)} median={fmt_median(values)} values={values}")

    print("valid_logs:")
    for trial in valid_trials:
        print(trial.path.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
