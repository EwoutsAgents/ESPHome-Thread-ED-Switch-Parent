# Thread Parent-Switch Benchmark Results (filtered latest runs)

Older runs were removed from `testing/logs`; statistics below are computed only from the remaining runs.

## Runs included

| Scenario | Mode | Log | CSV |
|---|---|---|---|
| `variant-mcast` | `steady` | `testing/logs/variant-mcast-steady-20260507-174248.log` | `testing/logs/variant-mcast-steady-20260507-174248.csv` |
| `variant-ucast` | `steady` | `testing/logs/variant-ucast-steady-20260507-174538.log` | `testing/logs/variant-ucast-steady-20260507-174538.csv` |

## Checkpoint summary

| Scenario | T0 | T1 | T2 | T3 | T4 | T5 | T6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `variant-mcast` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `variant-ucast` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Common metrics by variant (delta from T0, same schema)

| Variant | Measurement | N | Average (ms) | Std. dev (ms) |
|---|---|---:|---:|---:|
| `variant-mcast` | `C1_workflow_start` | 1 | 11 | 0.0 |
|  | `C2_switch_success` | 1 | 3634 | 0.0 |
|  | `C3_final_parent_match` | 1 | 3634 | 0.0 |
|  | `success_rate` | 1/1 | 100.0% | — |
| `variant-ucast` | `C1_workflow_start` | 1 | 12 | 0.0 |
|  | `C2_switch_success` | 1 | 34 | 0.0 |
|  | `C3_final_parent_match` | 1 | 34 | 0.0 |
|  | `success_rate` | 1/1 | 100.0% | — |
