# Thread Parent-Switch Benchmark Results (2026-05-11)

`stock-observed` is **stock behavior with observe-only instrumentation**.

## Audit status (updated after instrumentation fix)

- Instrumentation fix commit: `76c75eb`
- Rerun batch window: `20260511-171511` .. `20260511-172711` (10 trials)
- Build/flash evidence preserved: `testing/logs/stock-observed-steady-flash.log`
- Patch script execution confirmed in flash log:
  - `[thread_stock_observer] thread_api: already`
  - `[thread_stock_observer] mle_decl: already`
  - `[thread_stock_observer] mle_call: already`
- Runtime hook status during rerun: `Parent Response hook registered: YES` in all 10 trial logs.

## Batch validity

- Valid instrumentation trials: 10/10
- Invalid instrumentation trials: 0/10 (`invalid_instrumentation`)

## Stock-observed trial outcomes (steady)

Per-trial checkpoints (ms from SO0/C0 request):

- trial1 (`stock-observed-steady-20260511-171511-trial1.log`)
  - SO2: 2800
  - SO3: 3154
  - SO4: missing
  - SO5: missing
  - SO6: 15994
- trial2 (`stock-observed-steady-20260511-171631-trial2.log`)
  - SO2: 5932
  - SO3: 5973
  - SO4: missing
  - SO5: missing
  - SO6: 16003
- trial3 (`stock-observed-steady-20260511-171751-trial3.log`)
  - SO2: 413
  - SO3: 469
  - SO4: missing
  - SO5: missing
  - SO6: 15991
- trial4 (`stock-observed-steady-20260511-171911-trial4.log`)
  - SO2: 2759
  - SO3: 2782
  - SO4: missing
  - SO5: missing
  - SO6: 15992
- trial5 (`stock-observed-steady-20260511-172031-trial5.log`)
  - SO2: 2836
  - SO3: 2944
  - SO4: missing
  - SO5: missing
  - SO6: 15999
- trial6 (`stock-observed-steady-20260511-172151-trial6.log`)
  - SO2: 2086
  - SO3: 2102
  - SO4: missing
  - SO5: missing
  - SO6: 15991
- trial7 (`stock-observed-steady-20260511-172311-trial7.log`)
  - SO2: 4837
  - SO3: 4859
  - SO4: missing
  - SO5: missing
  - SO6: 15999
- trial8 (`stock-observed-steady-20260511-172431-trial8.log`)
  - SO2: 3003
  - SO3: 3200
  - SO4: missing
  - SO5: missing
  - SO6: 15997
- trial9 (`stock-observed-steady-20260511-172551-trial9.log`)
  - SO2: 6170
  - SO3: 6414
  - SO4: missing
  - SO5: missing
  - SO6: 15996
- trial10 (`stock-observed-steady-20260511-172711-trial10.log`)
  - SO2: 2711
  - SO3: 2728
  - SO4: missing
  - SO5: missing
  - SO6: 15997

## Aggregate interpretation (this valid batch only)

- SO2 observed: 10/10
- SO3 observed: 10/10
- SO4 observed: 0/10
- SO5 observed: 0/10
- SO6 timeout/failure: 10/10

Conclusion: this batch is valid for stock-observed interpretation (instrumentation available). The target parent consistently responded (SO3), but parent change/target reach did not occur before timeout in these 10 trials.

## Stock-observed current-parent-off trials

In `current-parent-off` mode, the child’s actual current parent was identified from `otThreadGetParentInfo()` and the runner attempted to disable the mapped current-parent router before `otThreadSearchForBetterParent()` was called. This differs from the steady-state stock-observed batch, where the current parent remained available.

Batch: `stock-observed-current-parent-off`, latest 10 trials (`20260511-182931` .. `20260511-184132`)

- trial count: 10
- valid trials: 4
- invalid trials: 6
- disable method: `serial-reset` (weak fallback, not hard power-off)

Per-trial current parent / disabled router / classification:
- trial1: `b27d8460213d29da` -> `router1` (`current_parent_shutdown_failed`)
- trial2: `b27d8460213d29da` -> `router1` (`timeout_target_not_reached`) [valid]
- trial3: `b27d8460213d29da` -> `router1` (`timeout_target_not_reached`) [valid]
- trial4: `b27d8460213d29da` -> `router1` (`current_parent_shutdown_failed`)
- trial5: `b27d8460213d29da` -> `router1` (`timeout_target_not_reached`) [valid]
- trial6: `b27d8460213d29da` -> `router1` (`current_parent_shutdown_failed`)
- trial7: `b27d8460213d29da` -> `router1` (`current_parent_shutdown_failed`)
- trial8: `b27d8460213d29da` -> `router1` (`current_parent_shutdown_failed`)
- trial9: `2657edfb2fbc394b` -> `unknown` (`invalid_parent_mapping`)
- trial10: `b27d8460213d29da` -> `router1` (`timeout_target_not_reached`) [valid]

Checkpoint counts (all 10 trials):
- SO2 observed: 10/10
- SO3 observed: 10/10
- SO4 parent changed: 3/10
- SO5 target reached: 0/10
- SO6 timeout/failure: 10/10

Switch-act timing basis:
- `disruption_time = disable_start`
- primary stock switch-act metric: `SO4 - disruption_time`
- strict stock target switch metric: `SO5 - disruption_time`

Measured medians from committed current-parent-off CSVs:
- median `SO4 - disruption_time`: **7968.5 ms** (2 observed SO4 events)
- median `SO5 - disruption_time`: **N/A** (0 observed SO5 events)

Interpretation split:
- Steady-state stock-observed tests whether stock OpenThread voluntarily moves to a responding target while the current parent remains available.
- Current-parent-off tests whether stock OpenThread reaches the configured target when the actual current parent is disrupted immediately before the better-parent search.
- Stock is not target-steered: SO4 (any parent change) and SO5 (configured target reached) answer different questions.

## Switch-act vs end-to-end summary table

| Scenario | Mode | Trials | Trigger | Success criterion | Successes | Median switch-act time (ms) | Notes |
|---|---|---:|---|---|---:|---:|---|
| stock-observed | current-parent-off | 10 | disruption_time (`disable_start`) | SO4 parent changed | 3/10 | 7968.5 | stock not target-steered |
| stock-observed | current-parent-off | 10 | disruption_time (`disable_start`) | SO5 target reached | 0/10 | N/A | stricter target criterion |
| variant-mcast | steady | 10 | T3 attach start | T6 target parent confirmed | 10/10 | 3846* | selected-parent attach |
| variant-ucast | steady | 0 | T3 attach start | T6 target parent confirmed | 0/0 | N/A | not rerun in this batch |

\* `T6-T3` currently available in 1/10 extracted variant-mcast trials due sparse `T3` marker logging in raw logs; `T6-T0` end-to-end median for the same batch is 33.5 ms.

## Balanced rerun (latest)

Balanced batches were rerun with 10 trials each:
- `stock-observed` `current-parent-off`: 10/10
- `variant-mcast` `steady`: 10/10
- `variant-ucast` `steady`: 10/10

Latest switch-act related outcomes from committed CSVs:
- stock current-parent-off:
  - SO2 observed: 7/10
  - SO3 observed: 7/10
  - SO4 parent changed: 1/10
  - SO5 target reached: 4/10
  - SO6 timeout/failure: 6/10
  - median `SO4 - disruption_time`: 7478 ms (n=1)
  - median `SO5 - disruption_time`: 5906 ms (n=4)
- variant-mcast steady:
  - T6 reached: 10/10
  - T3 attach-start detected: 1/10
  - median `T6-T3`: 3305 ms (n=1)
  - median end-to-end `T6-T0`: 34 ms
- variant-ucast steady:
  - T6 reached: 10/10
  - T3 attach-start detected: 0/10
  - median `T6-T3`: N/A
  - median end-to-end `T6-T0`: 33 ms

Note: `T3` sparsity in variant logs still limits strong `T6-T3` comparison quality; this needs explicit variant-side logging improvements for a publishable switch-act comparison.

## Commands used

- Build/flash + verification:
  - `testing/tools/build_stock_observed_with_verification.sh`
- Steady batch run:
  - `testing/tools/run_trials_batch.sh stock-observed 10 80 steady`
- Current-parent-off batch run:
  - `testing/tools/run_current_parent_off_trials.sh stock-observed 10 80`
- Extractor:
  - `python3 testing/tools/extract_switch_timings.py --in <log> --label child --scenario stock-observed --mode <steady|current-parent-off> --out <csv>`
- Integrity check:
  - `python3 testing/tools/check_stock_observed_integrity.py`
