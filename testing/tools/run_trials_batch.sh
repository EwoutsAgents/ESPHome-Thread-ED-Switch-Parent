#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

source testing/benchmark_profile.env
source testing/router_identity.env

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

ROUTER_CONFIG="testing/configs/router_ftd.yaml"
TARGET_PARENT_EXTADDR_LC="${TARGET_PARENT_EXTADDR,,}"
VARIANT_PRECONDITION_TIMEOUT="${VARIANT_PRECONDITION_TIMEOUT:-45}"
VARIANT_USB_THREAD_OFF_TIMEOUT="${VARIANT_USB_THREAD_OFF_TIMEOUT:-60}"
THREAD_CTL=".venv/bin/python testing/tools/thread_ctl.py"
THREAD_CONTROL_READY=""
TARGET_ROUTER_LABEL=""
TARGET_ROUTER_PORT=""
NON_TARGET_PARENT_EXTADDR=""
if [[ "$TARGET_PARENT_EXTADDR_LC" == "${ROUTER_PRIMARY_EXTADDR,,}" ]]; then
  TARGET_ROUTER_LABEL="router1"
  TARGET_ROUTER_PORT="$ROUTER_PRIMARY_PORT"
  NON_TARGET_PARENT_EXTADDR="${ROUTER_SECONDARY_EXTADDR,,}"
elif [[ "$TARGET_PARENT_EXTADDR_LC" == "${ROUTER_SECONDARY_EXTADDR,,}" ]]; then
  TARGET_ROUTER_LABEL="router2"
  TARGET_ROUTER_PORT="$ROUTER_SECONDARY_PORT"
  NON_TARGET_PARENT_EXTADDR="${ROUTER_PRIMARY_EXTADDR,,}"
fi

get_variant_initial_parent() {
  local log_path="$1"
  python3 - <<'PY' "$log_path"
import re, sys
text = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
match = re.search(r'V_precondition_initial_parent_extaddr=([0-9a-fA-F]{16})', text)
print(match.group(1).lower() if match else '')
PY
}

get_variant_probe_metadata() {
  local log_path="$1"
  python3 - <<'PY' "$log_path"
import re, sys
text = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
matches = re.findall(r'V_precondition_probe_result\s+elapsed_ms=\d+\s+responses=(\d+)\s+target_matches=(\d+)', text)
if matches:
    responses, target_matches = matches[-1]
else:
    responses, target_matches = '', ''
m_non_target = re.search(r'V_precondition_initial_parent_extaddr=([0-9a-fA-F]{16})', text)
non_target = m_non_target.group(1).lower() if m_non_target else ''
print(responses)
print(target_matches)
print(non_target)
PY
}

thread_control_cmd() {
  local action="$1"
  shift || true
  $THREAD_CTL --port "$TARGET_ROUTER_PORT" "$action" "$@"
}

ensure_thread_control_ready() {
  if [[ "$THREAD_CONTROL_READY" == "yes" ]]; then
    return 0
  fi
  if [[ "$THREAD_CONTROL_READY" == "no" ]]; then
    return 1
  fi
  if thread_control_cmd state >/dev/null 2>&1; then
    THREAD_CONTROL_READY="yes"
    return 0
  fi

  echo "[batch] preparing target router control firmware on $TARGET_ROUTER_LABEL ($TARGET_ROUTER_PORT)" >&2
  if .venv/bin/esphome run "$ROUTER_CONFIG" --device "$TARGET_ROUTER_PORT" --no-logs >"testing/logs/${SCENARIO}-${MODE}-${TARGET_ROUTER_LABEL}-thread-control-flash.log" 2>&1 && thread_control_cmd state >/dev/null 2>&1; then
    THREAD_CONTROL_READY="yes"
    return 0
  fi
  THREAD_CONTROL_READY="no"
  return 1
}

wait_for_variant_initial_parent() {
  local log_path="$1"
  local timeout_seconds="$2"
  local target_parent="$3"
  local result_file="$4"
  local initial_parent_file="$5"

  python3 - <<'PY' "$log_path" "$timeout_seconds" "$target_parent" "$result_file" "$initial_parent_file"
import re, sys, time
log_path, timeout_s, target, result_path, initial_path = sys.argv[1:6]
deadline = time.time() + float(timeout_s)
last_text = ''
while time.time() < deadline:
    try:
        text = open(log_path, encoding='utf-8', errors='ignore').read()
    except FileNotFoundError:
        text = ''
    last_text = text
    m = re.search(r'V_precondition_initial_parent_extaddr=([0-9a-fA-F]{16})', text)
    if m:
        initial = m.group(1).lower()
        open(initial_path, 'w', encoding='utf-8').write(initial)
        result = 'non_target_confirmed' if initial != target.lower() else 'target_still_current'
        open(result_path, 'w', encoding='utf-8').write(result)
        raise SystemExit(0)
    if 'V_precondition_initial_parent_unknown=' in text:
        open(result_path, 'w', encoding='utf-8').write('initial_parent_unknown')
        raise SystemExit(0)
    time.sleep(0.5)
open(result_path, 'w', encoding='utf-8').write('initial_parent_unknown')
PY
}

append_variant_preconditioning_metadata() {
  local log_path="$1"
  local prep_result="$2"
  local prep_method="$3"
  local initial_parent="$4"
  local suppression_start="$5"
  local suppression_end="$6"
  local probe_responses="${7:-}"
  local probe_target_matches="${8:-}"
  local probe_non_target_parent="${9:-}"

  {
    echo "# variant-preconditioning-method $prep_method"
    echo "# variant-target-parent-extaddr $TARGET_PARENT_EXTADDR_LC"
    [[ -n "$initial_parent" ]] && echo "# variant-initial-parent-extaddr $initial_parent"
    echo "# variant-precondition-result $prep_result"
    [[ -n "$probe_responses" ]] && echo "# variant-precondition-probe-responses $probe_responses"
    [[ -n "$probe_target_matches" ]] && echo "# variant-precondition-probe-target-matches $probe_target_matches"
    [[ -n "$probe_non_target_parent" ]] && echo "# variant-precondition-probe-non-target-extaddr $probe_non_target_parent"
    [[ -n "$suppression_start" ]] && echo "# variant-target-suppression-start $suppression_start"
    [[ -n "$suppression_end" ]] && echo "# variant-target-suppression-end $suppression_end"
    case "$prep_result" in
      target_still_current)
        echo "# classification precondition_failed_initial_parent_is_target"
        ;;
      initial_parent_unknown)
        echo "# classification initial_parent_unknown"
        ;;
      thread_off_failed)
        echo "# classification thread_off_failed"
        ;;
      thread_on_failed)
        echo "# classification thread_on_failed"
        ;;
    esac
  } >> "$log_path"
}

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
if [[ "$SCENARIO" == variant-* && "$MODE" == "steady" && -n "$TARGET_ROUTER_LABEL" ]]; then
  if ensure_thread_control_ready; then
    echo "[batch] target-router USB Thread control ready on $TARGET_ROUTER_LABEL ($TARGET_ROUTER_PORT)"
  else
    echo "[batch] target-router USB Thread control unavailable on $TARGET_ROUTER_LABEL ($TARGET_ROUTER_PORT)"
  fi
fi
FLASH_CMD=(.venv/bin/esphome run "$CONFIG" --device "$CHILD_PORT" --no-logs)
if [[ "$SCENARIO" == variant-* && "$MODE" == "steady" ]]; then
  FLASH_CMD=(
    .venv/bin/esphome
    -s auto_trigger_switch false
    -s batch_precondition_gate true
    -s batch_precondition_timeout_ms "$((VARIANT_PRECONDITION_TIMEOUT * 1000))"
    run "$CONFIG"
    --device "$CHILD_PORT"
    --no-logs
  )
fi
"${FLASH_CMD[@]}" >"testing/logs/${SCENARIO}-${MODE}-flash.log" 2>&1

for ((i=DONE+1; i<=TARGET_ATTEMPTS; i++)); do
  STAMP="$(date +%Y%m%d-%H%M%S)"
  LOG="testing/logs/${SCENARIO}-${MODE}-${STAMP}-trial${i}.log"
  CSV="testing/logs/${SCENARIO}-${MODE}-${STAMP}-trial${i}.csv"

  if [[ "$SCENARIO" == variant-* ]]; then
    echo "[batch] trial $i/$TARGET_ATTEMPTS (valid $VALID_DONE/$COUNT)"
  else
    echo "[batch] trial $i/$COUNT"
  fi

  PREP_LOG="testing/logs/${SCENARIO}-${MODE}-${STAMP}-trial${i}.prep.out"
  PREP_RESULT="not_applicable"
  PREP_METHOD=""
  PREP_INITIAL_PARENT=""
  PREP_SUPPRESSION_START=""
  PREP_SUPPRESSION_END=""
  PREP_PROBE_RESPONSES=""
  PREP_PROBE_TARGET_MATCHES=""
  PREP_PROBE_NON_TARGET_PARENT=""
  PREP_METHOD_FILE="${PREP_LOG%.out}.method.tmp"
  PREP_RESULT_FILE="${PREP_LOG%.out}.result.tmp"
  PREP_INITIAL_PARENT_FILE="${PREP_LOG%.out}.initial_parent.tmp"
  PREP_SUPPRESSION_START_FILE="${PREP_LOG%.out}.suppression_start.tmp"
  PREP_SUPPRESSION_END_FILE="${PREP_LOG%.out}.suppression_end.tmp"
  PREP_SUPPRESSION_STOP_FILE="${PREP_LOG%.out}.suppression_stop.tmp"
  rm -f "$PREP_METHOD_FILE" "$PREP_RESULT_FILE" "$PREP_INITIAL_PARENT_FILE" "$PREP_SUPPRESSION_START_FILE" "$PREP_SUPPRESSION_END_FILE" "$PREP_SUPPRESSION_STOP_FILE"

  CAPTURE_ARGS=(
    --config "$CONFIG"
    --duration "$DURATION"
    --out "$LOG"
  )

  if [[ "$SCENARIO" == variant-* && "$MODE" == "steady" ]]; then
    PREP_METHOD="usb-thread-off"
    if [[ -z "$TARGET_ROUTER_LABEL" ]]; then
      echo "[batch] warning: USB thread preconditioning unavailable; TARGET_PARENT_EXTADDR=$TARGET_PARENT_EXTADDR does not map to router1/router2" | tee "$PREP_LOG"
      PREP_RESULT="thread_off_failed"
      CAPTURE_ARGS+=(
        --node child="$CHILD_PORT"
        --node router1="$ROUTER_PRIMARY_PORT"
        --node router2="$ROUTER_SECONDARY_PORT"
        --reset-label child
      )
      python3 testing/tools/capture_logs.py "${CAPTURE_ARGS[@]}" >"${LOG%.log}.capture.out" 2>&1
    else
      CAPTURE_ARGS+=(
        --node child="$CHILD_PORT"
        --node router1="$ROUTER_PRIMARY_PORT"
        --reset-label child
      )
      echo "[batch] steady variant preconditioning: hold target router $TARGET_ROUTER_LABEL ($TARGET_PARENT_EXTADDR_LC) off for ${VARIANT_USB_THREAD_OFF_TIMEOUT}s, reset child, confirm non-target parent, then allow auto-restore" | tee -a "$PREP_LOG"
      if ! ensure_thread_control_ready; then
        echo "[batch] USB Thread control unavailable on $TARGET_ROUTER_LABEL" | tee -a "$PREP_LOG"
        PREP_RESULT="thread_off_failed"
        python3 testing/tools/capture_logs.py "${CAPTURE_ARGS[@]}" >"${LOG%.log}.capture.out" 2>&1
      else
        thread_control_cmd off-hold-verify-disabled --duration-s "$VARIANT_USB_THREAD_OFF_TIMEOUT" >>"$PREP_LOG" 2>&1 &
        THREAD_HOLD_PID=$!
        sleep 1
        if ! kill -0 "$THREAD_HOLD_PID" 2>/dev/null; then
          wait "$THREAD_HOLD_PID" || true
          echo "[batch] thread state verification failed after thread off" | tee -a "$PREP_LOG"
          PREP_RESULT="thread_off_failed"
          python3 testing/tools/capture_logs.py "${CAPTURE_ARGS[@]}" >"${LOG%.log}.capture.out" 2>&1
        else
          date -u +%Y-%m-%dT%H:%M:%S.%3NZ > "$PREP_SUPPRESSION_START_FILE"
          python3 testing/tools/capture_logs.py "${CAPTURE_ARGS[@]}" >"${LOG%.log}.capture.out" 2>&1 &
          CAPTURE_PID=$!
          wait_for_variant_initial_parent "$LOG" "$VARIANT_PRECONDITION_TIMEOUT" "$TARGET_PARENT_EXTADDR_LC" "$PREP_RESULT_FILE" "$PREP_INITIAL_PARENT_FILE" || true
          if ! wait "$THREAD_HOLD_PID"; then
            PREP_RESULT="thread_on_failed"
          fi
          date -u +%Y-%m-%dT%H:%M:%S.%3NZ > "$PREP_SUPPRESSION_END_FILE"
          wait "$CAPTURE_PID" || true
        fi
      fi
      if [[ "$PREP_RESULT" != "thread_on_failed" && -f "$PREP_RESULT_FILE" ]]; then
        PREP_RESULT="$(cat "$PREP_RESULT_FILE")"
      fi
      [[ -f "$PREP_INITIAL_PARENT_FILE" ]] && PREP_INITIAL_PARENT="$(cat "$PREP_INITIAL_PARENT_FILE")"
      [[ -f "$PREP_SUPPRESSION_START_FILE" ]] && PREP_SUPPRESSION_START="$(cat "$PREP_SUPPRESSION_START_FILE")"
      [[ -f "$PREP_SUPPRESSION_END_FILE" ]] && PREP_SUPPRESSION_END="$(cat "$PREP_SUPPRESSION_END_FILE")"
    fi
  else
    CAPTURE_ARGS+=(
      --node child="$CHILD_PORT"
      --node router1="$ROUTER_PRIMARY_PORT"
      --node router2="$ROUTER_SECONDARY_PORT"
      --reset-label child
    )

    if [[ "$MODE" == "forced-failover" ]]; then
      CAPTURE_ARGS+=(--reset-label router1)
    fi

    python3 testing/tools/capture_logs.py "${CAPTURE_ARGS[@]}" >"${LOG%.log}.capture.out" 2>&1
  fi

  if [[ "$SCENARIO" == variant-* ]]; then
    if [[ -z "$PREP_INITIAL_PARENT" ]]; then
      PREP_INITIAL_PARENT="$(get_variant_initial_parent "$LOG")"
    fi
    mapfile -t PREP_PROBE_META < <(get_variant_probe_metadata "$LOG")
    PREP_PROBE_RESPONSES="${PREP_PROBE_META[0]:-}"
    PREP_PROBE_TARGET_MATCHES="${PREP_PROBE_META[1]:-}"
    PREP_PROBE_NON_TARGET_PARENT="${PREP_PROBE_META[2]:-}"
    if [[ "$PREP_RESULT" == "not_applicable" || "$PREP_RESULT" == "pending_initial_parent_check" ]]; then
      if [[ -z "$PREP_INITIAL_PARENT" ]]; then
        PREP_RESULT="initial_parent_unknown"
      elif [[ "$PREP_INITIAL_PARENT" == "$TARGET_PARENT_EXTADDR_LC" ]]; then
        PREP_RESULT="target_still_current"
      else
        PREP_RESULT="non_target_confirmed"
      fi
    fi
    append_variant_preconditioning_metadata "$LOG" "$PREP_RESULT" "$PREP_METHOD" "$PREP_INITIAL_PARENT" "$PREP_SUPPRESSION_START" "$PREP_SUPPRESSION_END" "$PREP_PROBE_RESPONSES" "$PREP_PROBE_TARGET_MATCHES" "$PREP_PROBE_NON_TARGET_PARENT"
  fi

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

LAST_ATTEMPT="$DONE"
if (( LAST_ATTEMPT < TARGET_ATTEMPTS )); then
  LAST_ATTEMPT="$((i - 1))"
fi

if [[ "$SCENARIO" == variant-* ]]; then
  echo "[batch] complete: $SCENARIO $MODE valid $VALID_DONE/$COUNT (attempts=$LAST_ATTEMPT)"
else
  echo "[batch] complete: $SCENARIO $MODE $COUNT/$COUNT"
fi
