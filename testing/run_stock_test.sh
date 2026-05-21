#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="${1:-$SCRIPT_DIR/stock_test_devices.toml}"

if [[ -x "$SCRIPT_DIR/../venv/bin/python" ]]; then
  PYTHON_BIN="$SCRIPT_DIR/../venv/bin/python"
elif [[ -x "$SCRIPT_DIR/venv/bin/python" ]]; then
  PYTHON_BIN="$SCRIPT_DIR/venv/bin/python"
else
  PYTHON_BIN="${PYTHON_BIN:-python3}"
fi

exec "$PYTHON_BIN" "$SCRIPT_DIR/scripts/run_stock_test.py" --config "$CONFIG_FILE"
