#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

source testing/benchmark_profile.env

SCENARIO="${1:?usage: run_trials_batch.sh <scenario> <count> [duration] [mode]}"
COUNT="${2:?usage: run_trials_batch.sh <scenario> <count> [duration] [mode]}"
DURATION="${3:-80}"
MODE="${4:-steady}"
STATE_DIR="testing/logs/.batch_state"
mkdir -p "$STATE_DIR" testing/logs

case "$SCENARIO" in
  stock) CONFIG="testing/configs/child_stock.yaml" ;;
  stock-observed) CONFIG="testing/configs/child_stock_observed.yaml" ;;
  variant-mcast) CONFIG="testing/configs/child_variant_multicast.yaml" ;;
  variant-ucast) CONFIG="testing/configs/child_variant_unicast.yaml" ;;
  *) echo "Unknown scenario: $SCENARIO" >&2; exit 1 ;;
esac

if [[ "$MODE" != "steady" && "$MODE" != "forced-failover" ]]; then
  echo "Unknown mode: $MODE (use steady|forced-failover)" >&2
  exit 1
fi

STATE_FILE="$STATE_DIR/${SCENARIO}-${MODE}.state"
DONE=0
VALID_DONE=0
if [[ -f "$STATE_FILE" ]]; then
  DONE="$(cat "$STATE_FILE")"
fi

VALID_STATE_FILE="$STATE_DIR/${SCENARIO}-${MODE}.valid.state"
if [[ -f "$VALID_STATE_FILE" ]]; then
  VALID_DONE="$(cat "$VALID_STATE_FILE")"
fi

if [[ "$SCENARIO" == variant-* ]]; then
  if (( VALID_DONE >= COUNT )); then
    echo "[batch] already complete: $SCENARIO $MODE valid $VALID_DONE/$COUNT (attempts=$DONE)"
    exit 0
  fi
else
  if (( DONE >= COUNT )); then
    echo "[batch] already complete: $SCENARIO $MODE $DONE/$COUNT"
    exit 0
  fi
fi

if [[ "$SCENARIO" == variant-* ]]; then
  TARGET_ATTEMPTS=$(( COUNT * 4 ))
  if (( TARGET_ATTEMPTS < COUNT )); then TARGET_ATTEMPTS=$COUNT; fi
else
  TARGET_ATTEMPTS=$COUNT
fi

if (( DONE >= TARGET_ATTEMPTS )); then
  echo "[batch] attempts exhausted for $SCENARIO $MODE: attempts=$DONE valid=$VALID_DONE target_valid=$COUNT"
  exit 0
fi

# Build/flash once per scenario, then capture trials without extra compile pressure.
echo "[batch] preparing firmware: scenario=$SCENARIO mode=$MODE"
.venv/bin/esphome run "$CONFIG" --device "$CHILD_PORT" --no-logs >"testing/logs/${SCENARIO}-${MODE}-flash.log" 2>&1

for ((i=DONE+1; i<=TARGET_ATTEMPTS; i++)); do
  STAMP="$(date +%Y%m%d-%H%M%S)"
  LOG="testing/logs/${SCENARIO}-${MODE}-${STAMP}-trial${i}.log"
  CSV="testing/logs/${SCENARIO}-${MODE}-${STAMP}-trial${i}.csv"

  if [[ "$SCENARIO" == variant-* ]]; then
    echo "[batch] trial $i/$TARGET_ATTEMPTS (valid $VALID_DONE/$COUNT)"
  else
    echo "[batch] trial $i/$COUNT"
  fi

  CAPTURE_ARGS=(
    --config "$CONFIG"
    --duration "$DURATION"
    --out "$LOG"
    --node child="$CHILD_PORT"
    --node router1="$ROUTER_PRIMARY_PORT"
    --node router2="$ROUTER_SECONDARY_PORT"
    --reset-label child
  )

  if [[ "$MODE" == "forced-failover" ]]; then
    CAPTURE_ARGS+=(--reset-label router1)
  fi

  python3 testing/tools/capture_logs.py "${CAPTURE_ARGS[@]}" >"${LOG%.log}.capture.out" 2>&1

  python3 testing/tools/extract_switch_timings.py \
    --in "$LOG" \
    --label child \
    --scenario "$SCENARIO" \
    --mode "$MODE" \
    --out "$CSV" >"${CSV%.csv}.extract.out" 2>&1

  echo "$i" > "$STATE_FILE"

  if [[ "$SCENARIO" == variant-* ]]; then
    CLASSIFICATION="$(python3 - <<'PY' "$CSV"
import csv,sys
rows=list(csv.DictReader(open(sys.argv[1], newline='', encoding='utf-8')))
print(rows[0]['classification'] if rows else '')
PY
)"
    if [[ "$CLASSIFICATION" == "success_switch_act" ]]; then
      VALID_DONE=$((VALID_DONE + 1))
      echo "$VALID_DONE" > "$VALID_STATE_FILE"
      echo "[batch] valid switch-act trial accepted ($VALID_DONE/$COUNT)"
    else
      echo "[batch] non-switch-act trial classification=$CLASSIFICATION (not counted toward valid target)"
    fi

    if (( VALID_DONE >= COUNT )); then
      break
    fi
  fi
done

if [[ "$SCENARIO" == variant-* ]]; then
  echo "[batch] complete: $SCENARIO $MODE valid $VALID_DONE/$COUNT (attempts=$i)"
else
  echo "[batch] complete: $SCENARIO $MODE $COUNT/$COUNT"
fi
