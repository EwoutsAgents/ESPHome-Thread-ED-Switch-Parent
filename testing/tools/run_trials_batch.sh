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
TARGET_ROUTER_LABEL=""
TARGET_ROUTER_PORT=""
if [[ "$TARGET_PARENT_EXTADDR_LC" == "${ROUTER_PRIMARY_EXTADDR,,}" ]]; then
  TARGET_ROUTER_LABEL="router1"
  TARGET_ROUTER_PORT="$ROUTER_PRIMARY_PORT"
elif [[ "$TARGET_PARENT_EXTADDR_LC" == "${ROUTER_SECONDARY_EXTADDR,,}" ]]; then
  TARGET_ROUTER_LABEL="router2"
  TARGET_ROUTER_PORT="$ROUTER_SECONDARY_PORT"
fi

append_variant_preconditioning_metadata() {
  local log_path="$1"
  local prep_result="$2"
  local prep_method="$3"

  local initial_parent=""
  initial_parent="$(python3 - <<'PY' "$log_path"
import re, sys
text = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
match = re.search(r'V_precondition_initial_parent_extaddr=([0-9a-fA-F]{16})', text)
print(match.group(1).lower() if match else '')
PY
)"

  if [[ -z "$initial_parent" ]]; then
    prep_result="initial_parent_unknown"
  elif [[ "$initial_parent" == "$TARGET_PARENT_EXTADDR_LC" ]]; then
    prep_result="target_still_current"
  else
    prep_result="non_target_confirmed"
  fi

  {
    echo "# variant-preconditioning-method $prep_method"
    echo "# variant-target-parent-extaddr $TARGET_PARENT_EXTADDR_LC"
    [[ -n "$initial_parent" ]] && echo "# variant-initial-parent-extaddr $initial_parent"
    echo "# variant-precondition-result $prep_result"
    if [[ "$prep_result" == "target_still_current" ]]; then
      echo "# classification precondition_failed_initial_parent_is_target"
    fi
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
FLASH_CMD=(.venv/bin/esphome run "$CONFIG" --device "$CHILD_PORT" --no-logs)
if [[ "$SCENARIO" == variant-* && "$MODE" == "steady" ]]; then
  FLASH_CMD=(
    .venv/bin/esphome
    -s auto_trigger_switch false
    -s batch_precondition_gate true
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
  PREP_METHOD="target-router-reset"

  CAPTURE_ARGS=(
    --config "$CONFIG"
    --duration "$DURATION"
    --out "$LOG"
  )

  if [[ "$SCENARIO" == variant-* && "$MODE" == "steady" ]]; then
    if [[ -z "$TARGET_ROUTER_LABEL" ]]; then
      echo "[batch] warning: steady variant preconditioning skipped; TARGET_PARENT_EXTADDR=$TARGET_PARENT_EXTADDR does not map to router1/router2" | tee "$PREP_LOG"
      PREP_RESULT="initial_parent_unknown"
      CAPTURE_ARGS+=(
        --node child="$CHILD_PORT"
        --node router1="$ROUTER_PRIMARY_PORT"
        --node router2="$ROUTER_SECONDARY_PORT"
        --reset-label child
      )
    else
      echo "[batch] steady variant preconditioning: reset target router $TARGET_ROUTER_LABEL ($TARGET_PARENT_EXTADDR_LC) in capture sequence before child parent check" | tee "$PREP_LOG"
      PREP_RESULT="pending_initial_parent_check"
      if [[ "$TARGET_ROUTER_LABEL" == "router1" ]]; then
        CAPTURE_ARGS+=(
          --node router1="$ROUTER_PRIMARY_PORT"
          --node child="$CHILD_PORT"
          --node router2="$ROUTER_SECONDARY_PORT"
        )
      else
        CAPTURE_ARGS+=(
          --node router2="$ROUTER_SECONDARY_PORT"
          --node child="$CHILD_PORT"
          --node router1="$ROUTER_PRIMARY_PORT"
        )
      fi
      CAPTURE_ARGS+=(--reset-label "$TARGET_ROUTER_LABEL" --reset-label child)
    fi
  else
    CAPTURE_ARGS+=(
      --node child="$CHILD_PORT"
      --node router1="$ROUTER_PRIMARY_PORT"
      --node router2="$ROUTER_SECONDARY_PORT"
      --reset-label child
    )
  fi

  if [[ "$MODE" == "forced-failover" ]]; then
    CAPTURE_ARGS+=(--reset-label router1)
  fi

  python3 testing/tools/capture_logs.py "${CAPTURE_ARGS[@]}" >"${LOG%.log}.capture.out" 2>&1

  if [[ "$SCENARIO" == variant-* ]]; then
    append_variant_preconditioning_metadata "$LOG" "$PREP_RESULT" "$PREP_METHOD"
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

if [[ "$SCENARIO" == variant-* ]]; then
  echo "[batch] complete: $SCENARIO $MODE valid $VALID_DONE/$COUNT (attempts=$i)"
else
  echo "[batch] complete: $SCENARIO $MODE $COUNT/$COUNT"
fi
