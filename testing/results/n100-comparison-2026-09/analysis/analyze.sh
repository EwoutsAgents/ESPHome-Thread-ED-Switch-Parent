#!/usr/bin/env bash
set -euo pipefail

BUNDLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO_DIR="$(cd "$BUNDLE_DIR/../../.." && pwd)"
ANALYZER="$REPO_DIR/testing/scripts/analyze_test_logs.py"
PYTHON="$REPO_DIR/.venv/bin/python"
NETWORK_KEY="${THREAD_NETWORK_KEY:-dfd34f0f05cad978ec4e32b0413038ff}"
OUTPUT="${1:-$BUNDLE_DIR/analysis/raw-summary.md}"

: > "$OUTPUT"
for variant in stock ucast fast-attach fast-attach-ucast-1 stock-low-power; do
  for routers in 2 3 4; do
    echo "# $variant / $routers routers" >> "$OUTPUT"
    THREAD_NETWORK_KEY="$NETWORK_KEY" "$PYTHON" "$ANALYZER" \
      --logs-dir "$BUNDLE_DIR/$variant/$routers-routers/runs" \
      --network-key "$NETWORK_KEY" \
      --subtract-parent-response-random-delay \
      --summary-only --markdown --reuse-pcap-csv >> "$OUTPUT"
    echo >> "$OUTPUT"
  done
done

echo "Wrote $OUTPUT"
