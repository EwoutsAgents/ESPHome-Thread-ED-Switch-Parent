# Thread Parent-Switch Benchmark Results (2026-05-07)

This report separates:
- selected-parent variant internals (`T*`)
- stock-observed internals (`SO*`)
- cross-variant comparable outcomes (`C*`)

`stock-observed` is **stock behavior with observe-only instrumentation**.

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

## Artifacts

- `testing/logs/stock-observed-steady-20260507-215442.log`
- `testing/logs/stock-observed-steady-20260507-215442.csv`
- `testing/logs/variant-mcast-steady-20260507-202238.log`
- `testing/logs/variant-mcast-steady-20260507-202238.csv`
- `testing/logs/variant-ucast-steady-20260507-202442.log`
- `testing/logs/variant-ucast-steady-20260507-202442.csv`

## Notes

- `stock` remains a public-API sanity scenario only and no longer emits synthetic compatibility markers.
- `SO*` values are separate from `T*` and are not aggregated into variant-internal timing tables.
- This stock-observed run reached `SO3` (target Parent Response observed) but not `SO5` (target parent reached), so outcome is correctly reported as timeout (`SO6`).
