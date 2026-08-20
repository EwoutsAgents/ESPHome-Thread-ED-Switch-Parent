#!/usr/bin/env bash
set -euo pipefail

CAMPAIGN_REPO="/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent"
CAMPAIGN_TESTING="$CAMPAIGN_REPO/testing"
CAMPAIGN_BRANCH="feature/openthread-native-preferred-parent-controller"
CAMPAIGN_RUNS=50

cd "$CAMPAIGN_TESTING"

echo "Campaign started: $(date -Iseconds)"
echo "Variant: stock_low_power"
echo "Order: 4 routers, 3 routers, 2 routers"
echo "Runs per batch: $CAMPAIGN_RUNS"

test "$(git -C "$CAMPAIGN_REPO" branch --show-current)" = "$CAMPAIGN_BRANCH"
test -x ./run_stock_low_power_test.sh
test -f scripts/analyze_test_logs.py

run_stock_low_power_batch() {
  local router_count="$1"
  local config="stock_low_power_test_devices_${router_count}routers.toml"
  local pattern="stock_low_power-${router_count}router-${CAMPAIGN_RUNS}runs-*"
  local runner_rc=0
  local validation_rc=0
  local batch_name
  local batch_dir
  local report
  local report_rel

  test "$(git -C "$CAMPAIGN_REPO" branch --show-current)" = "$CAMPAIGN_BRANCH"
  test -f "$config"

  mapfile -t before_dirs < <(find logs -maxdepth 1 -mindepth 1 -type d -name "$pattern" -printf '%f\n' | sort)

  echo "Starting ${router_count}-router low-power stock batch: $(date -Iseconds)"
  ./run_stock_low_power_test.sh --config "$config" --runs "$CAMPAIGN_RUNS" || runner_rc=$?
  if [[ $runner_rc -ne 0 ]]; then
    echo "Runner returned ${runner_rc}; preserving and analyzing the generated batch"
  fi

  mapfile -t after_dirs < <(find logs -maxdepth 1 -mindepth 1 -type d -name "$pattern" -printf '%f\n' | sort)
  batch_name="$(comm -13 <(printf '%s\n' "${before_dirs[@]}") <(printf '%s\n' "${after_dirs[@]}") | tail -n 1)"
  test -n "$batch_name"
  batch_dir="logs/$batch_name"

  echo "Analyzing $batch_dir"
  python3 scripts/analyze_test_logs.py --logs-dir "$batch_dir" --write-markdown

  python3 - "$batch_dir" "$CAMPAIGN_RUNS" <<'PY' || validation_rc=$?
import collections
import glob
import json
import sys

batch_dir = sys.argv[1]
expected = int(sys.argv[2])
manifests = glob.glob(f"{batch_dir}/*/*manifest*.json")
statuses = collections.Counter()

for path in manifests:
    with open(path, encoding="utf-8") as handle:
        statuses[json.load(handle).get("status", "missing")] += 1

print(f"Manifest validation: count={len(manifests)} statuses={dict(statuses)}")
terminal = statuses.get("completed", 0) + statuses.get("skipped", 0)
raise SystemExit(0 if len(manifests) == expected and terminal == expected else 1)
PY
  if [[ $validation_rc -ne 0 ]]; then
    echo "Manifest validation failed for $batch_dir"
  fi

  report="$(find "$batch_dir" -maxdepth 1 -type f -name '*analysis-report.md' -printf '%T@ %p\n' | sort -nr | head -n 1 | cut -d' ' -f2-)"
  test -n "$report"
  report_rel="testing/$report"

  git -C "$CAMPAIGN_REPO" add -- "$report_rel"
  git -C "$CAMPAIGN_REPO" commit --only -m "test: record ${router_count}-router low-power stock 50-run campaign" -- "$report_rel"
  git -C "$CAMPAIGN_REPO" push origin "$CAMPAIGN_BRANCH"

  echo "Completed, analyzed, committed, and pushed ${router_count}-router low-power stock batch: $(date -Iseconds)"

  if [[ $runner_rc -ne 0 || $validation_rc -ne 0 ]]; then
    echo "Stopping campaign after non-clean ${router_count}-router batch"
    return 1
  fi
}

run_stock_low_power_batch 4
run_stock_low_power_batch 3
run_stock_low_power_batch 2

echo "Campaign finished: $(date -Iseconds)"
