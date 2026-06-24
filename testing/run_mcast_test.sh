#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PYTHON_BIN=""
for candidate in   "$SCRIPT_DIR/../.venv/bin/python"   "$SCRIPT_DIR/../venv/bin/python"   "$SCRIPT_DIR/.venv/bin/python"   "$SCRIPT_DIR/venv/bin/python"   "python3"; do
  if command -v "$candidate" >/dev/null 2>&1; then
    PYTHON_BIN="$candidate"
    break
  fi
done

if [[ -z "$PYTHON_BIN" ]]; then
  echo "Could not find python. Expected ../.venv/bin/python, ../venv/bin/python, or python3." >&2
  exit 1
fi

cd "$SCRIPT_DIR"
exec "$PYTHON_BIN" "$SCRIPT_DIR/scripts/run_ucast_test.py" --variant mcast --config mcast_test_devices_4routers.toml "$@"
