#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

source testing/benchmark_profile.env

CONFIG="testing/configs/child_stock_observed.yaml"
BUILD_DIR="testing/configs/.esphome/build/thread-child-stock-observed"
FLASH_LOG="testing/logs/stock-observed-steady-flash.log"

mkdir -p testing/logs

# Force clean rebuild so OpenThread patch steps are re-evaluated.
rm -rf "$BUILD_DIR/.pioenvs" "$BUILD_DIR/dependencies.lock"

.venv/bin/esphome run "$CONFIG" --device "$CHILD_PORT" --no-logs 2>&1 | tee "$FLASH_LOG"

# Verify patch script executed.
grep -q "\[thread_stock_observer\]" "$FLASH_LOG"

# Verify expected symbol is present in final link map.
MAP_FILE="$BUILD_DIR/.pioenvs/thread-child-stock-observed/firmware.map"
grep -q "thread_stock_observer_ot_register_parent_response_callback" "$MAP_FILE"

echo "OK: stock-observed patch path ran and callback symbol is present"
