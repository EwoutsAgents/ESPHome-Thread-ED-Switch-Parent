# Thread Parent-Switch Benchmark Results (2026-05-07)

## Runs executed

| Scenario | Mode | Log | CSV |
|---|---|---|---|
| `stock` | `steady` | `testing/logs/stock-steady-20260507-140832.log` | `testing/logs/stock-steady-20260507-140832.csv` |
| `stock` | `forced-failover` | `testing/logs/stock-forced-failover-20260507-142852.log` | `testing/logs/stock-forced-failover-20260507-142852.csv` |
| `variant-mcast` | `steady` | `testing/logs/variant-mcast-steady-20260507-143819.log` | `testing/logs/variant-mcast-steady-20260507-143819.csv` |
| `variant-mcast` | `forced-failover` | `testing/logs/variant-mcast-forced-failover-20260507-144056.log` | `testing/logs/variant-mcast-forced-failover-20260507-144056.csv` |
| `variant-ucast` | `steady` | `testing/logs/variant-ucast-steady-20260507-144431.log` | `testing/logs/variant-ucast-steady-20260507-144431.csv` |
| `variant-ucast` | `forced-failover` | `testing/logs/variant-ucast-forced-failover-20260507-144638.log` | `testing/logs/variant-ucast-forced-failover-20260507-144638.csv` |

## Checkpoint summary

Legend: ✅ present, — missing

| Scenario | Mode | T0 | T1 | T2 | T3 | T4 | T5 | T6 |
|---|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `stock` | `steady` | ✅ | ✅ | — | — | — | — | — |
| `stock` | `forced-failover` | ✅ | ✅ | — | — | — | — | — |
| `variant-mcast` | `steady` | ✅ | ✅ | — | — | — | — | — |
| `variant-mcast` | `forced-failover` | ✅ | ✅ | — | — | — | — | — |
| `variant-ucast` | `steady` | ✅ | ✅ | — | — | — | — | — |
| `variant-ucast` | `forced-failover` | ✅ | ✅ | — | — | — | — | — |

## What happened

- All runs captured `T0_request` and `T1_discovery_start`.
- No run captured `T2_target_observed` through `T6_parent_match`, so no selected-parent attach sequence completed.
- Variant runs (`variant-mcast`, `variant-ucast`) show Parent Responses from real extaddrs, but **never** from configured target `00124b0001abcdef`.
- The component reports: preferred parent not observed after all discovery attempts, then marks attach result failed.

## Primary root cause

- Configured preferred parent extaddr appears to be a placeholder/test value (`00124b0001abcdef`) and does not match discovered parents in the test network.

## Secondary issue observed

- Forced-failover router pre-flash (`testing/configs/router_ftd_failover.yaml`) currently fails to compile due to OpenThread patch mismatch in `mle.cpp` (`Get()` call mismatch).
- Runner was updated to continue capture even when that pre-flash step fails, so automated runs still complete.

## Recommended next step

1. Replace preferred parent target with a real discovered parent extaddr (or use an RLOC target).
2. Re-run one quick validation capture to confirm T2..T6 appear.
3. Then re-run full matrix for timing comparison.

## Follow-up validation after T2..T6 fix

Target parent set to discovered ExtAddr `da97557943a05aac`.

| Scenario | Mode | T0 | T1 | T2 | T3 | T4 | T5 | T6 | Key timing |
|---|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| `stock` | `steady` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | T2@11ms, T5@40ms |
| `variant-mcast` | `steady` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | T2@1312ms, T5@3634ms |
| `variant-ucast` | `steady` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | T2@34ms, T5@34ms |

Artifacts:
- `testing/logs/variant-mcast-steady-20260507-174248.log` and `testing/logs/variant-mcast-steady-20260507-174248.csv`
- `testing/logs/variant-ucast-steady-20260507-174538.log` and `testing/logs/variant-ucast-steady-20260507-174538.csv`
- `testing/logs/stock-steady-20260507-191205.log` and `testing/logs/stock-steady-20260507-191205.csv` (stock compatibility marker validation; T0..T6 all present)

## Aggregate timing statistics by variant (delta from T0)

| Variant | Measurement | N | Average (ms) | Std. dev (ms) |
|---|---|---:|---:|---:|
| `stock` | `T1_discovery_start` | 3 | 11.0 | 0.0 |
|  | `T2_target_observed` | 3 | 11.3 | 0.6 |
|  | `T3_attach_start` | 3 | 22.7 | 0.6 |
|  | `T4_child_id_req` | 3 | 33.7 | 0.6 |
|  | `T5_attach_done` | 3 | 40.7 | 0.6 |
|  | `T6_parent_match` | 3 | 40.7 | 0.6 |
| `variant-mcast` | `T1_discovery_start` | 3 | 11.0 | 0.0 |
|  | `T2_target_observed` | 3 | 444.7 | 751.1 |
|  | `T3_attach_start` | 3 | 452.0 | 744.8 |
|  | `T4_child_id_req` | 3 | 476.3 | 767.9 |
|  | `T5_attach_done` | 3 | 1238.0 | 2075.0 |
|  | `T6_parent_match` | 3 | 1238.0 | 2075.0 |
| `variant-ucast` | `T1_discovery_start` | 3 | 11.3 | 0.6 |
|  | `T2_target_observed` | 3 | 18.7 | 13.3 |
|  | `T3_attach_start` | 3 | 26.0 | 6.9 |
|  | `T4_child_id_req` | 3 | 33.7 | 0.6 |
|  | `T5_attach_done` | 3 | 38.7 | 4.0 |
|  | `T6_parent_match` | 3 | 38.7 | 4.0 |
