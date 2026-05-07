#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

source testing/benchmark_profile.env

SCENARIO="${1:-variant-mcast}"
DURATION="${2:-120}"
STAMP="$(date +%Y%m%d-%H%M%S)"
LOG="testing/logs/${SCENARIO}-${STAMP}.log"
CSV="testing/logs/${SCENARIO}-${STAMP}.csv"

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

echo "[run] scenario=$SCENARIO duration=${DURATION}s"
echo "[run] child=$CHILD_PORT"

python3 testing/tools/capture_logs.py \
  --config "$CONFIG" \
  --duration "$DURATION" \
  --out "$LOG" \
  --node child="$CHILD_PORT" \
  --node routerA="$ROUTER_A_PORT" \
  --node routerB="$ROUTER_B_PORT" \
  --node routerC="$ROUTER_C_PORT" \
  --node routerD="$ROUTER_D_PORT"

python3 testing/tools/extract_switch_timings.py --in "$LOG" --label child --out "$CSV"

echo "[done] log=$LOG"
echo "[done] csv=$CSV"
