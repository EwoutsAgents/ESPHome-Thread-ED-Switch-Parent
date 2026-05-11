# Thread Parent-Switch Benchmark Results (2026-05-11)

`stock-observed` is **stock behavior with observe-only instrumentation**.

## Artifact Audit Status

- Committed artifacts: none under `testing/logs/` (path is currently gitignored).
- Local-only artifacts present on this workstation:
  - `testing/logs/stock-observed-steady-20260507-215442.log`
  - `testing/logs/stock-observed-steady-20260507-215442.csv`
  - `testing/logs/variant-mcast-steady-20260507-202238.log`
  - `testing/logs/variant-mcast-steady-20260507-202238.csv`
  - `testing/logs/variant-ucast-steady-20260507-202442.log`
  - `testing/logs/variant-ucast-steady-20260507-202442.csv`
- Missing artifacts: none for the file list above.
- Rerun status: **required** after observe-only implementation changes.

The raw artifacts for this run were not committed. The numerical values below are retained as provisional historical notes only and must not be treated as auditable benchmark evidence.

## Table 1 — Variant Internal Timings (T0–T6)

| Variant | Mode | T0 | T1 | T2 | T3 | T4 | T5 | T6 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| variant-mcast | steady | 0 | 11 | 11 | 22 | 33 | 40 | 40 |
| variant-ucast | steady | 0 | 11 | 11 | 22 | 34 | 41 | 41 |

## Table 2 — Stock-Observed Timings (SO0–SO6)

| Variant | Mode | SO0 | SO1 | SO2 | SO3 | SO4 | SO5 | SO6 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| stock-observed | steady | 0 | 14 | 2946 | 2963 | — | — | 15998 |

## Table 3 — Common Comparable Metrics

| Variant | Mode | C0_request | C1_workflow_started | C2_target_reached | time_to_target (C2-C0, ms) | success_rate |
|---|---|---:|---:|---:|---:|---:|
| stock-observed | steady | 0 | 14 | — | — | 0/1 |
| variant-mcast | steady | 0 | 11 | 40 | 40 | 1/1 |
| variant-ucast | steady | 0 | 11 | 41 | 41 | 1/1 |

## Interpretation

The stock-observed run reached `SO3`, meaning the target parent emitted a real Parent Response. It did not reach `SO5`, meaning OpenThread did not report the target as the current parent before timeout. This is reported as `SO6_timeout_or_failure`, not converted into synthetic selected-parent timing events.

## Reproducibility Metadata

- Repository commit: 02a91bb114029cf872eb5b71169ce2e509825337
- ESPHome version: unknown
- ESP-IDF version: unknown
- OpenThread version or ESP-IDF OpenThread package: unknown
- Board: esp32-c6-devkitm-1
- Child device serial path: /dev/serial/by-id/usb-1a86_USB_Single_Serial_5AF7094208-if00
- Primary router serial path: /dev/serial/by-id/usb-1a86_USB_Single_Serial_5AF7094336-if00
- Secondary router serial path: /dev/serial/by-id/usb-1a86_USB_Single_Serial_5AF7094210-if00
- Thread channel: 15
- PAN ID: 0x1234
- Target parent ExtAddr: da97557943a05aac
- Scenario list: stock-observed, variant-mcast, variant-ucast, stock (sanity)
- Number of trials per scenario: 1 (historical), rerun pending (target >=10)
- Capture command: unknown
- Extraction command: `python3 testing/tools/extract_switch_timings.py --in <log> --label child --scenario <scenario> --mode steady --out <csv>`

## Regression Check

Run:

```bash
python3 testing/tools/check_stock_observed_integrity.py
```
