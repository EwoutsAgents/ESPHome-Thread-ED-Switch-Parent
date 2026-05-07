#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

source testing/benchmark_profile.env

SCENARIO="${1:-variant-mcast}"
MODE="${2:-steady}"
DURATION="${3:-120}"
STAMP="$(date +%Y%m%d-%H%M%S)"
LOG="testing/logs/${SCENARIO}-${MODE}-${STAMP}.log"
CSV="testing/logs/${SCENARIO}-${MODE}-${STAMP}.csv"

case "$SCENARIO" in
  stock)
    CONFIG="testing/configs/child_stock.yaml"
    ;;
  variant-mcast)
    CONFIG="testing/configs/child_variant_multicast.yaml"
    ;;
  variant-ucast)
    CONFIG="testing/configs/child_variant_unicast.yaml"
    ;;
  *)
    echo "Unknown scenario: $SCENARIO (use: stock|variant-mcast|variant-ucast)" >&2
    exit 1
    ;;
esac

if [[ "$MODE" != "steady" && "$MODE" != "forced-failover" ]]; then
  echo "Unknown mode: $MODE (use: steady|forced-failover)" >&2
  exit 1
fi

echo "[run] scenario=$SCENARIO mode=$MODE duration=${DURATION}s"
echo "[run] child=$CHILD_PORT"
echo "[run] router-primary(R1)=$ROUTER_PRIMARY_PORT"
echo "[run] router-secondary(R2)=$ROUTER_SECONDARY_PORT"

if [[ "$MODE" == "forced-failover" ]]; then
  echo "[prep] flashing R1 with forced-failover router profile"
  if ! .venv/bin/esphome run testing/configs/router_ftd_failover.yaml --device "$ROUTER_PRIMARY_PORT" --no-logs; then
    echo "[warn] forced-failover router profile flash failed; continuing with current R1 firmware"
  fi
fi

CAPTURE_ARGS=(
  --config "$CONFIG"
  --duration "$DURATION"
  --out "$LOG"
  --node child="$CHILD_PORT"
  --node router1="$ROUTER_PRIMARY_PORT"
  --node router2="$ROUTER_SECONDARY_PORT"
)

if [[ "$MODE" == "forced-failover" ]]; then
  CAPTURE_ARGS+=(--reset-label child --reset-label router1)
fi

python3 testing/tools/capture_logs.py \
  "${CAPTURE_ARGS[@]}"

python3 testing/tools/extract_switch_timings.py --in "$LOG" --label child --out "$CSV"

echo "[done] log=$LOG"
echo "[done] csv=$CSV"
