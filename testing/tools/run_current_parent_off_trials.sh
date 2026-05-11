#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

source testing/benchmark_profile.env
source testing/router_identity.env

SCENARIO="${1:-stock-observed}"
COUNT="${2:-10}"
DURATION="${3:-80}"
MODE="current-parent-off"
STATE_DIR="testing/logs/.batch_state"
mkdir -p "$STATE_DIR" testing/logs
STATE_FILE="$STATE_DIR/${SCENARIO}-${MODE}.state"
DONE=0
[[ -f "$STATE_FILE" ]] && DONE="$(cat "$STATE_FILE")"

if [[ "$SCENARIO" != "stock-observed" ]]; then
  echo "This runner currently supports only stock-observed" >&2
  exit 1
fi

CHILD_CONFIG="testing/configs/child_stock_observed_current_parent_off.yaml"
ROUTER_CONFIG="testing/configs/router_ftd.yaml"
FLASH_LOG="testing/logs/stock-observed-current-parent-off-flash.log"

echo "[cp-off] build/flash child current-parent-off firmware"
.venv/bin/esphome run "$CHILD_CONFIG" --device "$CHILD_PORT" --no-logs >"$FLASH_LOG" 2>&1

for ((i=DONE+1; i<=COUNT; i++)); do
  STAMP="$(date +%Y%m%d-%H%M%S)"
  LOG="testing/logs/stock-observed-current-parent-off-${STAMP}-trial${i}.log"
  CSV="testing/logs/stock-observed-current-parent-off-${STAMP}-trial${i}.csv"

  echo "[cp-off] trial $i/$COUNT"

  python3 testing/tools/capture_logs.py \
    --config "$CHILD_CONFIG" \
    --duration "$DURATION" \
    --out "$LOG" \
    --node child="$CHILD_PORT" \
    --node router1="$ROUTER_PRIMARY_PORT" \
    --node router2="$ROUTER_SECONDARY_PORT" \
    --reset-label child >"${LOG%.log}.capture.out" 2>&1 &
  CAP_PID=$!

  PREP_DETECTED=0
  CURRENT_EXTADDR=""
  CURRENT_RLOC16=""
  DISABLED_ROUTER_LABEL="unknown"
  DISABLE_METHOD="serial-reset"
  TRIAL_CLASSIFICATION=""
  DISABLE_START=""
  DISABLE_END=""

  for _ in $(seq 1 280); do
    if grep -q "SO0 waiting for current-parent-off action" "$LOG" 2>/dev/null; then
      PREP_DETECTED=1
      break
    fi
    sleep 0.2
  done

  if [[ "$PREP_DETECTED" -eq 1 ]]; then
    line=""
    for _ in $(seq 1 20); do
      line="$(grep -m1 "SO0 initial parent:" "$LOG" || true)"
      [[ -n "$line" ]] && break
      sleep 0.2
    done
    CURRENT_EXTADDR="$(echo "$line" | sed -n 's/.*ExtAddr \([0-9a-fA-F]\{16\}\).*/\1/p' | tr '[:upper:]' '[:lower:]')"
    CURRENT_RLOC16="$(echo "$line" | sed -n 's/.*RLOC16 \(0x[0-9a-fA-F]\{4\}\).*/\1/p')"

    if [[ -z "$CURRENT_EXTADDR" ]]; then
      TRIAL_CLASSIFICATION="invalid_parent_mapping"
    elif [[ "$CURRENT_EXTADDR" == "${ROUTER_PRIMARY_EXTADDR,,}" ]]; then
      DISABLED_ROUTER_LABEL="router1"
      DISABLE_START="$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)"
      if ! timeout 8 .venv/bin/esphome logs "$ROUTER_CONFIG" --device "$ROUTER_PRIMARY_PORT" --reset >/tmp/router1-reset.out 2>&1; then
        TRIAL_CLASSIFICATION="current_parent_shutdown_failed"
      fi
      DISABLE_END="$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)"
    elif [[ "$CURRENT_EXTADDR" == "${ROUTER_SECONDARY_EXTADDR,,}" ]]; then
      DISABLED_ROUTER_LABEL="router2"
      DISABLE_START="$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)"
      if ! timeout 8 .venv/bin/esphome logs "$ROUTER_CONFIG" --device "$ROUTER_SECONDARY_PORT" --reset >/tmp/router2-reset.out 2>&1; then
        TRIAL_CLASSIFICATION="current_parent_shutdown_failed"
      fi
      DISABLE_END="$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)"
    else
      TRIAL_CLASSIFICATION="invalid_parent_mapping"
    fi
  else
    TRIAL_CLASSIFICATION="current_parent_not_disabled"
  fi

  wait "$CAP_PID" || true

  {
    echo "# trial $i"
    [[ -n "$CURRENT_EXTADDR" ]] && echo "# current-parent-extaddr $CURRENT_EXTADDR"
    [[ -n "$CURRENT_RLOC16" ]] && echo "# current-parent-rloc16 $CURRENT_RLOC16"
    echo "# disabled-router-label $DISABLED_ROUTER_LABEL"
    echo "# disable-method $DISABLE_METHOD"
    [[ -n "$DISABLE_START" ]] && echo "# disable-start $DISABLE_START"
    [[ -n "$DISABLE_END" ]] && echo "# disable-end $DISABLE_END"
    if [[ -n "$TRIAL_CLASSIFICATION" ]]; then
      echo "# classification $TRIAL_CLASSIFICATION"
    fi
  } >> "$LOG"

  python3 testing/tools/extract_switch_timings.py \
    --in "$LOG" \
    --label child \
    --scenario stock-observed \
    --mode "$MODE" \
    --out "$CSV" >"${CSV%.csv}.extract.out" 2>&1

  echo "$i" > "$STATE_FILE"
done

echo "[cp-off] complete: $SCENARIO $MODE $COUNT/$COUNT"
