# Testing
For an overview of the testing sequence, refer to `README_STOCK_TESTING.md` or `README_MCAST_UCAST_TESTING.md`. 

# Log analysis

Use `scripts/analyze_test_logs.py` for post-run child-log analysis across `stock`, `ucast`, and `mcast` runs. It is variant-agnostic and discovers the matching `*_test_manifest_*.json` file from each run directory.

Timing policy:
- Reported attach timings are derived from sniffer pcap data only for all three variants.
- Child-log timestamps are retained as reference metadata in the report, but are not used as fallback timing values.
- If a run does not have a usable manifest, pcap, network key, or complete matched attach sequence in the pcap, the timing fields remain unavailable.

Examples:

```bash
python3 scripts/analyze_test_logs.py --logs-dir logs/stock --markdown
python3 scripts/analyze_test_logs.py --logs-dir logs/ucast --markdown
python3 scripts/analyze_test_logs.py --logs-dir logs/mcast --markdown
python3 scripts/analyze_test_logs.py --run-dir logs/stock/<timestamp> --markdown
python3 scripts/analyze_test_logs.py --run-dir logs/ucast/<timestamp> --markdown
python3 scripts/analyze_test_logs.py --run-dir logs/mcast/<timestamp> --markdown
```

To write the Markdown report to disk:

```bash
python3 scripts/analyze_test_logs.py \
  --logs-dir logs/mcast \
  --write-markdown

python3 scripts/analyze_test_logs.py \
  --run-dir logs/mcast/<timestamp> \
  --write-markdown
```

With `--logs-dir logs/<variant>`, `--write-markdown` defaults to a variant-wide report:

```text
logs/<variant>/<generated-at>-<variant>-analysis-report.md
```

With a single `--run-dir`, `--write-markdown` defaults to a scoped single-run report at the same variant root:

```text
logs/<variant>/<run-timestamp>-<variant>-analysis-report.md
```
