#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

source testing/benchmark_profile.env
source testing/router_identity.env

CONFIG="testing/configs/child_stock_observed.yaml"
BUILD_DIR="testing/configs/.esphome/build/thread-child-stock-observed"
FLASH_LOG="testing/logs/stock-observed-steady-flash.log"
THREAD_CTL=".venv/bin/python testing/tools/thread_ctl.py"
TARGET_PARENT_EXTADDR_RUNTIME="${TARGET_PARENT_EXTADDR,,}"

mkdir -p testing/logs

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

# Force clean rebuild so OpenThread patch steps are re-evaluated.
rm -rf "$BUILD_DIR/.pioenvs" "$BUILD_DIR/dependencies.lock"

if refresh_target_parent_extaddr; then
  echo "[stock-observed] refreshed live target parent extaddr: $TARGET_PARENT_EXTADDR_RUNTIME"
else
  echo "[stock-observed] WARNING: failed to refresh live target parent extaddr; using cached $TARGET_PARENT_EXTADDR_RUNTIME" >&2
fi

.venv/bin/esphome -s target_parent_extaddr "$TARGET_PARENT_EXTADDR_RUNTIME" run "$CONFIG" --device "$CHILD_PORT" --no-logs 2>&1 | tee "$FLASH_LOG"

# Verify patch script executed.
grep -q "\[thread_stock_observer\]" "$FLASH_LOG"

# Verify expected symbol is present in final link map.
MAP_FILE="$BUILD_DIR/.pioenvs/thread-child-stock-observed/firmware.map"
grep -q "thread_stock_observer_ot_register_parent_response_callback" "$MAP_FILE"

echo "OK: stock-observed patch path ran and callback symbol is present"
