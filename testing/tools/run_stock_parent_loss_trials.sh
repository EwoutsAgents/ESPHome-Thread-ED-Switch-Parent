#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

source testing/benchmark_profile.env
source testing/router_identity.env

THREAD_CTL=".venv/bin/python testing/tools/thread_ctl.py"
CHILD_CONFIG="testing/configs/child_stock_parent_loss.yaml"
ROUTER_CONFIG="testing/configs/router_ftd.yaml"
SCENARIO="stock-parent-loss"
STATE_DIR="testing/logs/.batch_state"
mkdir -p "$STATE_DIR" testing/logs
STATE_FILE="$STATE_DIR/${SCENARIO}.state"
VALID_STATE_FILE="$STATE_DIR/${SCENARIO}.valid.state"
DONE=0
VALID_DONE=0
[[ -f "$STATE_FILE" ]] && DONE="$(cat "$STATE_FILE")"
[[ -f "$VALID_STATE_FILE" ]] && VALID_DONE="$(cat "$VALID_STATE_FILE")"

COUNT="${1:-10}"
DURATION="${2:-120}"
if [[ "${1:-}" == "--preflight" || "${1:-}" == "--dry-run" ]]; then
  COUNT=0
fi

STABILIZE_SECONDS="${STOCK_PARENT_LOSS_STABILIZE_SECONDS:-10}"
R1_OFF_HOLD_SECONDS="${STOCK_PARENT_LOSS_R1_OFF_HOLD_SECONDS:-120}"
ARM_TIMEOUT_SECONDS="${STOCK_PARENT_LOSS_ARM_TIMEOUT_SECONDS:-90}"
THREAD_OFF_READY_TIMEOUT="${STOCK_PARENT_LOSS_THREAD_OFF_READY_TIMEOUT:-12}"
CAPTURE_BUFFER_SECONDS="${STOCK_PARENT_LOSS_CAPTURE_BUFFER_SECONDS:-20}"
TARGET_ATTEMPTS=$(( COUNT * 4 ))
if (( TARGET_ATTEMPTS < COUNT )); then TARGET_ATTEMPTS=$COUNT; fi
EFFECTIVE_DURATION=$(( ARM_TIMEOUT_SECONDS + DURATION + CAPTURE_BUFFER_SECONDS ))
FLASH_LOG="testing/logs/${SCENARIO}-flash.log"
ROUTER_CONTROL_LOG="testing/logs/${SCENARIO}-router-thread-control-flash.log"
ROUTER_PRIMARY_EXTADDR_RUNTIME="${ROUTER_PRIMARY_EXTADDR,,}"
ROUTER_SECONDARY_EXTADDR_RUNTIME="${ROUTER_SECONDARY_EXTADDR,,}"

iso_now() {
  date -u +%Y-%m-%dT%H:%M:%S.%3NZ
}

port_exists() {
  [[ -e "$1" ]]
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
}

thread_state_enabled() {
  local port="$1"
  local output
  if ! output="$($THREAD_CTL --port "$port" state 2>/dev/null)"; then
    return 1
  fi
  grep -q 'enabled=true' <<<"$output"
}

ensure_router_thread_control_ready() {
  if thread_state_enabled "$ROUTER_PRIMARY_PORT" && thread_state_enabled "$ROUTER_SECONDARY_PORT"; then
    return 0
  fi
  echo "[parent-loss] preparing router Thread control firmware" >&2
  .venv/bin/esphome run "$ROUTER_CONFIG" --device "$ROUTER_PRIMARY_PORT" --no-logs >"$ROUTER_CONTROL_LOG" 2>&1 || true
  thread_state_enabled "$ROUTER_PRIMARY_PORT" && thread_state_enabled "$ROUTER_SECONDARY_PORT"
}

wait_for_log_pattern() {
  local log_path="$1"
  local pattern="$2"
  local timeout_seconds="$3"
  python3 - <<'PY' "$log_path" "$pattern" "$timeout_seconds"
import re, sys, time
log_path, pattern, timeout_s = sys.argv[1:4]
rx = re.compile(pattern)
deadline = time.time() + float(timeout_s)
while time.time() < deadline:
    try:
        text = open(log_path, encoding='utf-8', errors='ignore').read()
    except FileNotFoundError:
        text = ''
    if rx.search(text):
        raise SystemExit(0)
    time.sleep(0.2)
raise SystemExit(1)
PY
}

extract_final_parent_from_log() {
  local log_path="$1"
  python3 - <<'PY' "$log_path"
import re, sys
text = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
patterns = [
    r'PL4 target parent reached after .*? current=([0-9a-fA-F]{16})',
    r'PL5 timeout after .*? final_parent=([0-9a-fA-F]{16})',
    r'PL3 parent changed after .*? current=([0-9a-fA-F]{16})',
]
for pattern in patterns:
    matches = re.findall(pattern, text)
    if matches:
        print(matches[-1].lower())
        raise SystemExit(0)
print('')
PY
}

measurement_armed_in_log() {
  local log_path="$1"
  grep -q 'PL0 measurement armed; initial_parent=' "$log_path" 2>/dev/null
}

append_parent_loss_metadata() {
  local log_path="$1"
  local classification="$2"
  local r1_off_time="$3"
  local final_parent="$4"
  local measurement_state_cleared="no"
  if measurement_armed_in_log "$log_path"; then
    measurement_state_cleared="yes"
  fi
  {
    echo "# target_parent_extaddr $ROUTER_SECONDARY_EXTADDR_RUNTIME"
    echo "# measurement-state-cleared $measurement_state_cleared"
    [[ -n "$r1_off_time" ]] && echo "# parent-loss-r1-off $r1_off_time"
    [[ -n "$final_parent" ]] && echo "# final_parent_extaddr $final_parent"
    echo "# classification $classification"
  } >> "$log_path"
}

preflight() {
  local ok=1
  for path in "$CHILD_PORT" "$ROUTER_PRIMARY_PORT" "$ROUTER_SECONDARY_PORT"; do
    if port_exists "$path"; then
      echo "[parent-loss] port ok: $path"
    else
      echo "[parent-loss] missing port: $path" >&2
      ok=0
    fi
  done

  if ensure_router_thread_control_ready; then
    echo "[parent-loss] router Thread control ready"
  else
    echo "[parent-loss] router Thread control not ready" >&2
    ok=0
  fi

  if refresh_router_identity_extaddrs; then
    echo "[parent-loss] live router extaddrs: R1=$ROUTER_PRIMARY_EXTADDR_RUNTIME R2=$ROUTER_SECONDARY_EXTADDR_RUNTIME"
  else
    echo "[parent-loss] failed to read live router extaddrs" >&2
    ok=0
  fi

  if [[ "$ROUTER_PRIMARY_EXTADDR_RUNTIME" != "${ROUTER_PRIMARY_EXTADDR,,}" || "$ROUTER_SECONDARY_EXTADDR_RUNTIME" != "${ROUTER_SECONDARY_EXTADDR,,}" ]]; then
    echo "[parent-loss] router identity mismatch vs testing/router_identity.env" >&2
    ok=0
  else
    echo "[parent-loss] router identities match testing/router_identity.env"
  fi

  return $((1 - ok))
}

if [[ "${1:-}" == "--preflight" || "${1:-}" == "--dry-run" ]]; then
  preflight
  exit $?
fi

if (( VALID_DONE >= COUNT )); then
  echo "[parent-loss] already complete: valid $VALID_DONE/$COUNT (attempts=$DONE)"
  exit 0
fi

if (( DONE >= TARGET_ATTEMPTS )); then
  echo "[parent-loss] attempts exhausted: attempts=$DONE valid=$VALID_DONE target_valid=$COUNT"
  exit 0
fi

PRECONDITION_STATUS="ok"
if ! preflight; then
  PRECONDITION_STATUS="precondition_failed_router_identity_unknown"
  echo "[parent-loss] preflight warning: router identity / thread control checks failed; trials will be classified as precondition failures" >&2
else
  echo "[parent-loss] build/flash child stock parent-loss firmware"
  .venv/bin/esphome \
    -s initial_parent_extaddr "$ROUTER_PRIMARY_EXTADDR_RUNTIME" \
    -s target_parent_extaddr "$ROUTER_SECONDARY_EXTADDR_RUNTIME" \
    -s stabilize_delay "${STABILIZE_SECONDS}s" \
    -s stabilize_delay_ms "$((STABILIZE_SECONDS * 1000))" \
    -s observe_timeout "${DURATION}s" \
    run "$CHILD_CONFIG" --device "$CHILD_PORT" --no-logs >"$FLASH_LOG" 2>&1
fi

CURRENT_BATCH_CSVS=()

for ((i=DONE+1; i<=TARGET_ATTEMPTS; i++)); do
  if (( VALID_DONE >= COUNT )); then
    break
  fi

  STAMP="$(date +%Y%m%d-%H%M%S)"
  LOG="testing/logs/${SCENARIO}-${STAMP}-trial${i}.log"
  CSV="testing/logs/${SCENARIO}-${STAMP}-trial${i}.csv"
  CAPTURE_OUT="${LOG%.log}.capture.out"
  READY_FILE="/tmp/${SCENARIO}-r1-off-trial${i}.out"
  rm -f "$READY_FILE"

  echo "[parent-loss] trial $i/$TARGET_ATTEMPTS (valid $VALID_DONE/$COUNT)"

  TRIAL_CLASSIFICATION=""
  R1_OFF_TIME=""
  FINAL_PARENT=""

  if [[ "$PRECONDITION_STATUS" == "ok" ]]; then
    python3 testing/tools/capture_logs.py \
      --config "$CHILD_CONFIG" \
      --duration "$EFFECTIVE_DURATION" \
      --out "$LOG" \
      --node child="$CHILD_PORT" \
      --reset-label child >"$CAPTURE_OUT" 2>&1 &
    CAP_PID=$!

    if ! wait_for_log_pattern "$LOG" 'PL0 measurement armed; initial_parent=' "$ARM_TIMEOUT_SECONDS"; then
      TRIAL_CLASSIFICATION="precondition_failed_not_on_r1"
    elif ! thread_state_enabled "$ROUTER_SECONDARY_PORT"; then
      TRIAL_CLASSIFICATION="precondition_failed_r2_unavailable"
    else
      echo "[parent-loss] confirmed initial parent R1"
      echo "[parent-loss] R2 online"
      echo "[parent-loss] measurement armed"

      $THREAD_CTL --port "$ROUTER_PRIMARY_PORT" off-verify-disabled-hold --duration-s "$R1_OFF_HOLD_SECONDS" >"$READY_FILE" 2>&1 &
      HOLD_PID=$!
      READY_DEADLINE=$(( $(date +%s) + THREAD_OFF_READY_TIMEOUT ))
      READY_CONFIRMED="no"
      while true; do
        if grep -q 'USB_CTL_READY_DISABLED' "$READY_FILE" 2>/dev/null; then
          READY_CONFIRMED="yes"
          break
        fi
        if ! kill -0 "$HOLD_PID" 2>/dev/null; then
          break
        fi
        if (( $(date +%s) >= READY_DEADLINE )); then
          break
        fi
        sleep 0.2
      done

      if [[ "$READY_CONFIRMED" != "yes" ]]; then
        TRIAL_CLASSIFICATION="invalid_r1_off_not_confirmed"
        wait "$HOLD_PID" || true
      else
        R1_OFF_TIME="$(iso_now)"
        echo "# parent-loss-r1-off $R1_OFF_TIME" >> "$LOG"
        echo "[parent-loss] R1 off confirmed"
        if wait_for_log_pattern "$LOG" 'PL4 target parent reached; current=' "$DURATION"; then
          TRIAL_CLASSIFICATION="success_failover_to_r2"
        else
          wait_for_log_pattern "$LOG" 'PL5 timeout;|PL5 timeout after' 5 || true
          TRIAL_CLASSIFICATION="timeout_failover_to_r2_not_reached"
        fi
        wait "$HOLD_PID" || true
      fi
    fi

    if kill -0 "$CAP_PID" 2>/dev/null; then
      kill "$CAP_PID" 2>/dev/null || true
    fi

    wait "$CAP_PID" || true
  else
    : > "$LOG"
    TRIAL_CLASSIFICATION="$PRECONDITION_STATUS"
  fi

  FINAL_PARENT="$(extract_final_parent_from_log "$LOG")"
  append_parent_loss_metadata "$LOG" "$TRIAL_CLASSIFICATION" "$R1_OFF_TIME" "$FINAL_PARENT"

  python3 testing/tools/extract_switch_timings.py \
    --in "$LOG" \
    --scenario stock-parent-loss \
    --trial "$i" \
    --out "$CSV" >/dev/null
  CURRENT_BATCH_CSVS+=("$CSV")

  if [[ "$TRIAL_CLASSIFICATION" == "success_failover_to_r2" ]]; then
    TOTAL_FAILOVER_MS="$(python3 - <<'PY' "$CSV"
import csv, sys
row = next(csv.DictReader(open(sys.argv[1], newline='', encoding='utf-8')), {})
print(row.get('total_failover_ms', ''))
PY
)"
    if [[ -n "$TOTAL_FAILOVER_MS" ]]; then
      echo "[parent-loss] target R2 reached after ${TOTAL_FAILOVER_MS} ms"
    else
      echo "[parent-loss] target R2 reached"
    fi
  fi

  DONE="$i"
  echo "$DONE" > "$STATE_FILE"

  case "$TRIAL_CLASSIFICATION" in
    success_failover_to_r2)
      VALID_DONE=$((VALID_DONE + 1))
      echo "$VALID_DONE" > "$VALID_STATE_FILE"
      echo "[parent-loss] valid trial accepted $VALID_DONE/$COUNT"
      ;;
    timeout_failover_to_r2_not_reached)
      VALID_DONE=$((VALID_DONE + 1))
      echo "$VALID_DONE" > "$VALID_STATE_FILE"
      echo "[parent-loss] valid timeout accepted $VALID_DONE/$COUNT"
      ;;
    precondition_failed_*)
      echo "[parent-loss] precondition failure: $TRIAL_CLASSIFICATION"
      ;;
    *)
      echo "[parent-loss] invalid trial: $TRIAL_CLASSIFICATION"
      ;;
  esac

done

python3 - <<'PY' "${CURRENT_BATCH_CSVS[@]}"
import csv, statistics, sys
paths = [p for p in sys.argv[1:] if p]
rows = []
for path in paths:
    with open(path, newline='', encoding='utf-8') as fh:
        rows.extend(csv.DictReader(fh))
def values(field, klass):
    out = []
    for row in rows:
        if row.get('classification') != klass:
            continue
        value = row.get(field, '')
        if value:
            out.append(int(value))
    return out
valid = [r for r in rows if r.get('classification') in ('success_failover_to_r2', 'timeout_failover_to_r2_not_reached')]
print('[parent-loss] complete:')
print(f"  valid trials: {len(valid)}/{len(rows)}")
print(f"  success_failover_to_r2: {sum(1 for r in rows if r.get('classification') == 'success_failover_to_r2')}")
print(f"  timeout_failover_to_r2_not_reached: {sum(1 for r in rows if r.get('classification') == 'timeout_failover_to_r2_not_reached')}")
print(f"  precondition failures: {sum(1 for r in rows if r.get('classification', '').startswith('precondition_failed_'))}")
for field in ('total_failover_ms', 'detection_latency_ms', 'switching_time_ms'):
    nums = values(field, 'success_failover_to_r2')
    if nums:
        print(f"  median {field}: {int(statistics.median(nums))}")
PY
