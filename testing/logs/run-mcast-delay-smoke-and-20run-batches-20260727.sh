#!/usr/bin/env bash
set -euo pipefail

CAMPAIGN_REPO="/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent"
CAMPAIGN_TESTING="$CAMPAIGN_REPO/testing"
CAMPAIGN_BRANCH="feature/openthread-native-preferred-parent-controller"
SMOKE_ROUTERS="${SMOKE_ROUTERS-4 3 2}"

cd "$CAMPAIGN_TESTING"

test "$(git -C "$CAMPAIGN_REPO" branch --show-current)" = "$CAMPAIGN_BRANCH"
test -x ./run_mcast_test.sh
test -f scripts/analyze_test_logs.py

run_smoke() {
  local routers="$1"
  local config="mcast_test_devices_${routers}routers.toml"
  local batch_dir
  local report

  mapfile -t before < <(find logs -type f -name '*_test_manifest_*.json' -printf '%h\n' | sort -u)
  echo "Starting ${routers}-router multicast smoke: $(date -Iseconds)"
  ./run_mcast_test.sh --config "$config" --runs 1
  batch_dir="$(comm -13 \
    <(printf '%s\n' "${before[@]}" | sort) \
    <(find logs -type f -name '*_test_manifest_*.json' -printf '%h\n' | sort -u) \
    | tail -n 1)"
  test -n "$batch_dir"

  python3 scripts/analyze_test_logs.py \
    --run-dir "$batch_dir" \
    --subtract-parent-response-random-delay \
    --write-markdown

  report="$(find "$batch_dir" -maxdepth 1 -type f -name '*analysis-report.md' -printf '%T@ %p\n' | sort -nr | head -n 1 | cut -d' ' -f2-)"
  test -n "$report"
  test "$(find "$batch_dir" -maxdepth 1 -type f -name '*manifest*.json' | wc -l)" -eq 1
  test "$(find "$batch_dir" -maxdepth 1 -type f \( -name '*.pcap' -o -name '*.pcapng' \) | wc -l)" -ge 1
  grep -q "selected-parent logged random delay" "$report"
  grep -q "Request -> Response minus Random Delay" "$report"
  echo "Validated ${routers}-router multicast smoke: $batch_dir"
}

run_batch() {
  local routers="$1"
  local runs=20
  local config="mcast_test_devices_${routers}routers.toml"
  local pattern="mcast-${routers}router-${runs}runs-*"
  local batch_dir
  local report
  local report_rel

  mapfile -t before < <(find logs -type d -name "$pattern" -printf '%p\n' | sort)
  echo "Starting ${routers}-router multicast ${runs}-run batch: $(date -Iseconds)"
  ./run_mcast_test.sh --config "$config" --runs "$runs"
  batch_dir="$(comm -13 \
    <(printf '%s\n' "${before[@]}" | sort) \
    <(find logs -type d -name "$pattern" -printf '%p\n' | sort) \
    | tail -n 1)"
  test -n "$batch_dir"

  python3 scripts/analyze_test_logs.py \
    --logs-dir "$batch_dir" \
    --subtract-parent-response-random-delay \
    --write-markdown

  python3 - "$batch_dir" "$runs" <<'PY'
import collections
import glob
import json
import sys

batch_dir = sys.argv[1]
expected = int(sys.argv[2])
paths = glob.glob(f"{batch_dir}/*/*manifest*.json")
statuses = collections.Counter()
for path in paths:
    with open(path, encoding="utf-8") as handle:
        statuses[json.load(handle).get("status", "missing")] += 1
print(f"Manifest validation: count={len(paths)} statuses={dict(statuses)}")
terminal = statuses.get("completed", 0) + statuses.get("skipped", 0)
raise SystemExit(0 if len(paths) == expected and terminal == expected else 1)
PY

  report="$(find "$batch_dir" -maxdepth 1 -type f -name '*analysis-report.md' -printf '%T@ %p\n' | sort -nr | head -n 1 | cut -d' ' -f2-)"
  test -n "$report"
  grep -q "selected-parent logged random delay" "$report"
  grep -q "Request -> Response minus Random Delay" "$report"
  report_rel="testing/$report"

  git -C "$CAMPAIGN_REPO" add -- "$report_rel"
  git -C "$CAMPAIGN_REPO" commit --only \
    -m "test: record ${routers}-router multicast 20-run delay campaign" \
    -- "$report_rel"
  git -C "$CAMPAIGN_REPO" push origin "$CAMPAIGN_BRANCH"
  echo "Completed ${routers}-router multicast batch: $(date -Iseconds)"
}

echo "Campaign started: $(date -Iseconds)"
for routers in $SMOKE_ROUTERS; do
  run_smoke "$routers"
done
for routers in 4 3 2; do
  run_batch "$routers"
done
echo "Campaign finished: $(date -Iseconds)"
