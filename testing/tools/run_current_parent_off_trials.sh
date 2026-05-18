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
VALID_STATE_FILE="$STATE_DIR/${SCENARIO}-${MODE}.valid.state"
VALID_DONE=0
[[ -f "$VALID_STATE_FILE" ]] && VALID_DONE="$(cat "$VALID_STATE_FILE")"

if [[ "$SCENARIO" != "stock-observed" ]]; then
  echo "This runner currently supports only stock-observed" >&2
  exit 1
fi

if (( VALID_DONE >= COUNT )); then
  echo "[cp-off] already complete: $SCENARIO $MODE valid $VALID_DONE/$COUNT (attempts=$DONE)"
  exit 0
fi

TARGET_ATTEMPTS=$(( COUNT * 4 ))
if (( TARGET_ATTEMPTS < COUNT )); then TARGET_ATTEMPTS=$COUNT; fi
if (( DONE >= TARGET_ATTEMPTS )); then
  echo "[cp-off] attempts exhausted for $SCENARIO $MODE: attempts=$DONE valid=$VALID_DONE target_valid=$COUNT"
  exit 0
fi

CHILD_CONFIG="testing/configs/child_stock_observed_current_parent_off.yaml"
ROUTER_CONFIG="testing/configs/router_ftd.yaml"
FLASH_LOG="testing/logs/stock-observed-current-parent-off-flash.log"
THREAD_CTL=".venv/bin/python testing/tools/thread_ctl.py"
TARGET_PARENT_EXTADDR_RUNTIME="${TARGET_PARENT_EXTADDR,,}"
ROUTER_PRIMARY_EXTADDR_RUNTIME="${ROUTER_PRIMARY_EXTADDR,,}"
ROUTER_SECONDARY_EXTADDR_RUNTIME="${ROUTER_SECONDARY_EXTADDR,,}"
CURRENT_PARENT_OFF_HOLD_SECONDS="${STOCK_CURRENT_PARENT_OFF_HOLD_TIMEOUT:-25}"
THREAD_OFF_READY_TIMEOUT="${STOCK_CURRENT_PARENT_OFF_READY_TIMEOUT:-12}"
TARGET_SUPPRESSION_HOLD_SECONDS="${STOCK_CURRENT_PARENT_OFF_TARGET_SUPPRESSION_TIMEOUT:-20}"
TARGET_SUPPRESSION_READY_TIMEOUT="${STOCK_CURRENT_PARENT_OFF_TARGET_SUPPRESSION_READY_TIMEOUT:-12}"
AUTO_TRIGGER_DELAY="${STOCK_CURRENT_PARENT_OFF_AUTO_TRIGGER_DELAY:-15s}"
PREPARED_TO_SEARCH_DELAY="${STOCK_CURRENT_PARENT_OFF_PREPARED_TO_SEARCH_DELAY:-1s}"
OBSERVE_TIMEOUT="${STOCK_CURRENT_PARENT_OFF_OBSERVE_TIMEOUT:-45s}"
PROBE_TIMEOUT_MS="${STOCK_CURRENT_PARENT_OFF_PROBE_TIMEOUT_MS:-25000}"
PROBE_RETRY_INTERVAL="${STOCK_CURRENT_PARENT_OFF_PROBE_RETRY_INTERVAL:-2s}"

refresh_target_parent_extaddr() {
  local live_extaddr
  if ! live_extaddr="$($THREAD_CTL --port "$ROUTER_SECONDARY_PORT" extaddr 2>/dev/null | tail -n1 | tr '[:upper:]' '[:lower:]')"; then
    return 1
  fi
  if [[ ! "$live_extaddr" =~ ^[0-9a-f]{16}$ ]]; then
    return 1
  fi
  TARGET_PARENT_EXTADDR_RUNTIME="$live_extaddr"
  return 0
}

refresh_router_identity_extaddrs() {
  local live_primary live_secondary
  if ! live_primary="$($THREAD_CTL --port "$ROUTER_PRIMARY_PORT" extaddr 2>/dev/null | tail -n1 | tr '[:upper:]' '[:lower:]')"; then
    return 1
  fi
  if ! live_secondary="$($THREAD_CTL --port "$ROUTER_SECONDARY_PORT" extaddr 2>/dev/null | tail -n1 | tr '[:upper:]' '[:lower:]')"; then
    return 1
  fi
  if [[ ! "$live_primary" =~ ^[0-9a-f]{16}$ ]] || [[ ! "$live_secondary" =~ ^[0-9a-f]{16}$ ]]; then
    return 1
  fi
  ROUTER_PRIMARY_EXTADDR_RUNTIME="$live_primary"
  ROUTER_SECONDARY_EXTADDR_RUNTIME="$live_secondary"
  return 0
}

echo "[cp-off] build/flash child current-parent-off firmware"
if refresh_target_parent_extaddr; then
  echo "[cp-off] refreshed live target parent extaddr: $TARGET_PARENT_EXTADDR_RUNTIME"
else
  echo "[cp-off] WARNING: failed to refresh live target parent extaddr; using cached $TARGET_PARENT_EXTADDR_RUNTIME" >&2
fi

if refresh_router_identity_extaddrs; then
  echo "[cp-off] refreshed router identities: primary=$ROUTER_PRIMARY_EXTADDR_RUNTIME secondary=$ROUTER_SECONDARY_EXTADDR_RUNTIME"
else
  echo "[cp-off] WARNING: failed to refresh router identities; using cached primary=$ROUTER_PRIMARY_EXTADDR_RUNTIME secondary=$ROUTER_SECONDARY_EXTADDR_RUNTIME" >&2
fi

.venv/bin/esphome \
  -s target_parent_extaddr "$TARGET_PARENT_EXTADDR_RUNTIME" \
  -s auto_trigger_delay "$AUTO_TRIGGER_DELAY" \
  -s prepared_to_search_delay "$PREPARED_TO_SEARCH_DELAY" \
  -s observe_timeout "$OBSERVE_TIMEOUT" \
  -s probe_timeout_ms "$PROBE_TIMEOUT_MS" \
  -s probe_retry_interval "$PROBE_RETRY_INTERVAL" \
  run "$CHILD_CONFIG" --device "$CHILD_PORT" --no-logs >"$FLASH_LOG" 2>&1

LAST_ATTEMPT="$DONE"
for ((i=DONE+1; i<=TARGET_ATTEMPTS; i++)); do
  STAMP="$(date +%Y%m%d-%H%M%S)"
  LOG="testing/logs/stock-observed-current-parent-off-${STAMP}-trial${i}.log"
  CSV="testing/logs/stock-observed-current-parent-off-${STAMP}-trial${i}.csv"

  echo "[cp-off] trial $i/$TARGET_ATTEMPTS (valid $VALID_DONE/$COUNT)"

  TARGET_SUPPRESS_PID=""
  TARGET_SUPPRESS_READY_FILE="/tmp/stock-cpoff-target-suppress.out"
  rm -f "$TARGET_SUPPRESS_READY_FILE"
  echo "[cp-off] preconditioning: hold target router off for ${TARGET_SUPPRESSION_HOLD_SECONDS}s so child starts on non-target parent" | tee -a "${LOG%.log}.capture.out"
  $THREAD_CTL --port "$ROUTER_SECONDARY_PORT" off-verify-disabled-hold --duration-s "$TARGET_SUPPRESSION_HOLD_SECONDS" >"$TARGET_SUPPRESS_READY_FILE" 2>&1 &
  TARGET_SUPPRESS_PID=$!
  TARGET_SUPPRESS_READY="no"
  TARGET_SUPPRESS_DEADLINE=$(( $(date +%s) + TARGET_SUPPRESSION_READY_TIMEOUT ))
  while true; do
    if grep -q 'USB_CTL_READY_DISABLED' "$TARGET_SUPPRESS_READY_FILE" 2>/dev/null; then
      TARGET_SUPPRESS_READY="yes"
      break
    fi
    if ! kill -0 "$TARGET_SUPPRESS_PID" 2>/dev/null; then
      break
    fi
    if (( $(date +%s) >= TARGET_SUPPRESS_DEADLINE )); then
      break
    fi
    sleep 0.2
  done
  if [[ "$TARGET_SUPPRESS_READY" == "yes" ]]; then
    echo "[cp-off] target-router suppression ready; resetting child into non-target attach window" | tee -a "${LOG%.log}.capture.out"
  else
    echo "[cp-off] WARNING: target-router suppression did not confirm ready-disabled; proceeding anyway" | tee -a "${LOG%.log}.capture.out"
  fi

  python3 testing/tools/capture_logs.py \
    --config "$CHILD_CONFIG" \
    --duration "$DURATION" \
    --out "$LOG" \
    --node child="$CHILD_PORT" \
    --reset-label child >"${LOG%.log}.capture.out" 2>&1 &
  CAP_PID=$!

  PREP_DETECTED=0
  CURRENT_EXTADDR=""
  CURRENT_RLOC16=""
  DISABLED_ROUTER_LABEL="unknown"
  DISABLE_METHOD="usb-thread-off-hold"
  TRIAL_CLASSIFICATION=""
  DISABLE_START=""
  DISABLE_END=""
  THREAD_HOLD_PID=""
  THREAD_READY_OBSERVED="no"

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
    elif [[ "$CURRENT_EXTADDR" == "$TARGET_PARENT_EXTADDR_RUNTIME" ]]; then
      TRIAL_CLASSIFICATION="initial_parent_already_target"
    elif [[ "$CURRENT_EXTADDR" == "$ROUTER_PRIMARY_EXTADDR_RUNTIME" ]]; then
      DISABLED_ROUTER_LABEL="router1"
      DISABLE_START="$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)"
      $THREAD_CTL --port "$ROUTER_PRIMARY_PORT" off-verify-disabled-hold --duration-s "$CURRENT_PARENT_OFF_HOLD_SECONDS" > /tmp/router1-reset.out 2>&1 &
      THREAD_HOLD_PID=$!
    elif [[ "$CURRENT_EXTADDR" == "$ROUTER_SECONDARY_EXTADDR_RUNTIME" ]]; then
      DISABLED_ROUTER_LABEL="router2"
      DISABLE_START="$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)"
      $THREAD_CTL --port "$ROUTER_SECONDARY_PORT" off-verify-disabled-hold --duration-s "$CURRENT_PARENT_OFF_HOLD_SECONDS" > /tmp/router2-reset.out 2>&1 &
      THREAD_HOLD_PID=$!
    else
      TRIAL_CLASSIFICATION="invalid_parent_mapping"
    fi
  else
    TRIAL_CLASSIFICATION="current_parent_not_disabled"
  fi

  if [[ -z "$TRIAL_CLASSIFICATION" && -n "$THREAD_HOLD_PID" ]]; then
    READY_DEADLINE=$(( $(date +%s) + THREAD_OFF_READY_TIMEOUT ))
    READY_FILE=""
    if [[ "$DISABLED_ROUTER_LABEL" == "router1" ]]; then
      READY_FILE="/tmp/router1-reset.out"
    elif [[ "$DISABLED_ROUTER_LABEL" == "router2" ]]; then
      READY_FILE="/tmp/router2-reset.out"
    fi

    while true; do
      if [[ -n "$READY_FILE" ]] && grep -q 'USB_CTL_READY_DISABLED' "$READY_FILE" 2>/dev/null; then
        THREAD_READY_OBSERVED="yes"
        break
      fi
      if ! kill -0 "$THREAD_HOLD_PID" 2>/dev/null; then
        break
      fi
      if (( $(date +%s) >= READY_DEADLINE )); then
        break
      fi
      sleep 0.2
    done

    if [[ "$THREAD_READY_OBSERVED" != "yes" ]]; then
      wait "$THREAD_HOLD_PID" || true
      TRIAL_CLASSIFICATION="current_parent_shutdown_failed"
      DISABLE_END="$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)"
      THREAD_HOLD_PID=""
    fi
  fi

  wait "$CAP_PID" || true

  if [[ -n "$TARGET_SUPPRESS_PID" ]]; then
    wait "$TARGET_SUPPRESS_PID" || true
  fi

  if [[ -n "$THREAD_HOLD_PID" ]]; then
    if ! wait "$THREAD_HOLD_PID"; then
      TRIAL_CLASSIFICATION="thread_reenable_failed"
    fi
    DISABLE_END="$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)"
  fi

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
  LAST_ATTEMPT="$i"

  mapfile -t CSV_SUMMARY < <(python3 - <<'PY' "$CSV"
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1], newline='', encoding='utf-8')))
row = rows[0] if rows else {}
classification = row.get('classification', '')
initial_parent = row.get('initial_parent_extaddr', '').lower()
target_parent = row.get('target_parent_extaddr', '').lower()
valid = bool(initial_parent) and bool(target_parent) and initial_parent != target_parent and classification in {'success_target_reached', 'timeout_target_not_reached'}
print(classification)
print('yes' if valid else 'no')
PY
)
  CLASSIFICATION="${CSV_SUMMARY[0]:-}"
  VALID_STOCK_TRIAL="${CSV_SUMMARY[1]:-no}"
  if [[ "$VALID_STOCK_TRIAL" == "yes" ]]; then
    VALID_DONE=$((VALID_DONE + 1))
    echo "$VALID_DONE" > "$VALID_STATE_FILE"
    echo "[cp-off] valid stock-observed trial accepted ($VALID_DONE/$COUNT)"
  else
    echo "[cp-off] non-valid stock-observed trial classification=$CLASSIFICATION (not counted toward valid target)"
  fi

  if (( VALID_DONE >= COUNT )); then
    break
  fi
done

echo "[cp-off] complete: $SCENARIO $MODE valid $VALID_DONE/$COUNT (attempts=$LAST_ATTEMPT)"
