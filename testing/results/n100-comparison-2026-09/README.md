# Thread parent-attachment n=100 comparison bundle

This bundle contains the curated hardware measurements used for the five-variant comparison completed in September 2026. It contains exactly 100 accepted runs for every combination of variant and router count: 5 variants × 3 router counts × 100 runs = 1,500 runs.

Included variants:

- `stock`
- `ucast`
- `fast-attach`
- `fast-attach-ucast-1`
- `stock-low-power`

`fast-attach-ucast-32` is intentionally excluded because its campaign did not reach n=100.

Each accepted run directory contains the original manifest, child/router logs, packet capture, generated packet CSVs when available, runner supervisor log, and embedded build provenance. Files under `runs/` are hard links to the original `testing/logs/` artifacts, so this local bundle does not duplicate their storage. Copying or archiving the directory produces a self-contained dataset.

## Layout

- `MANIFEST.json`: accepted run index, original path, and SHA-256 values for the run manifest and PCAP.
- `MANIFEST.sha256`: checksum of `MANIFEST.json`.
- `analysis/results.md`: canonical comparison table.
- `analysis/results.csv` and `analysis/results.json`: machine-readable results.
- `analysis/raw-summary.md`: direct analyzer output against the packaged files.
- `analysis/analyze.sh`: reruns the repository analyzer against every packaged group.
- `provenance/`: firmware, hardware, selection, revision, and exclusion documentation.
- `<variant>/<n>-routers/runs.tsv`: mapping between bundle run names and original paths.
- `<variant>/<n>-routers/runs/`: the 100 accepted run directories.

## Metrics

The reported values describe the recovery/directed second attach and are mean ± sample standard deviation in milliseconds:

1. Parent Request → Parent Response
2. Adjusted Parent Request → Parent Response
3. Parent Response → Child ID Request
4. Child ID Request → Child ID Response
5. Full attach

The adjusted metric subtracts the selected replacement parent's logged Parent Response delay. For `fast-attach-ucast-1`, the protocol delay is fixed at 1 ms, so the adjusted mean is the raw mean minus 1 ms and the standard deviation is unchanged.

See `provenance/selection-rules.md` for curation details and known timestamp normalization.
