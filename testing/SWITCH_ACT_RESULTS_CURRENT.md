# SWITCH_ACT_RESULTS_CURRENT

## Interpretation rule
- **Stock switch-act:** `SO4_parent_changed - disruption_time`
- **Variant switch-act:** `T6_parent_match - T3_attach_start`
- **Variant end-to-end (separate):** `T6_parent_match - T0_request`

Immediate parent-match trials are **no-op successes**, not switch-act samples.

## A) Stock current-parent-off switch-act

| scenario | mode | total trials | valid trials | SO4 successes | SO5 successes | median SO4-disruption ms | median SO5-disruption ms | disruption method |
|---|---|---:|---:|---:|---:|---:|---:|---|
| stock-observed | current-parent-off | 10 | 4 | 1 | 4 | 7478 | 5906 | serial-reset |

Source artifacts (latest balanced stock run):
- `testing/logs/stock-observed-current-parent-off-20260511-205544-trial1.log` .. `trial10.log`
- `testing/logs/stock-observed-current-parent-off-20260511-205544-trial1.csv` .. `trial10.csv`

## B) Variant valid switch-act trials

| scenario | mode | total trials | valid switch-act trials | immediate no-switch trials | T3 present | T6 present | median T6-T3 ms | median T6-T0 ms |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| variant-mcast | steady | 4 | 0 | 4 | 0 | 4 | N/A | 44 |
| variant-ucast | steady | 4 | 0 | 4 | 0 | 4 | N/A | 33 |

## C) Variant immediate-parent-match/no-switch trials

Classification criteria implemented:
- `immediate_parent_match_no_switch` when:
  - `V_immediate_parent_match` present
  - `T6_parent_match` present
  - `T3_attach_start` missing

Observed in smoke reruns:
- mcast: 4/4
- ucast: 4/4

## D) Variant end-to-end timings

- mcast smoke median `T6-T0`: **44 ms**
- ucast smoke median `T6-T0`: **33 ms**

These are useful end-to-end timings, but **not** switch-act timings.

## Implementation changes in this update

1. Immediate-success marker in variant component:
   - `components/thread_preferred_parent/thread_preferred_parent.cpp`
   - Added:
     - `T_success_immediate_parent_match; target=...`
     - `V_initial_parent_extaddr=...` before switch start

2. Extractor updates:
   - `testing/tools/extract_switch_timings.py`
   - Added checkpoint pattern:
     - `V_immediate_parent_match`
   - Added classification logic:
     - `success_switch_act`
     - `immediate_parent_match_no_switch`
     - `invalid_initial_parent_is_target`
     - `timeout_or_failure`
     - `unclassified`
   - Added CSV field:
     - `delta_ms_from_attach_start`

3. Variant batch runner behavior:
   - `testing/tools/run_trials_batch.sh`
   - Variant runs now count only `success_switch_act` trials toward valid target and keep classifying non-switch-act trials separately.

4. Variant steady preconditioning in batch runner:
   - `testing/tools/run_trials_batch.sh`
   - For `variant-* steady`, the runner now maps `TARGET_PARENT_EXTADDR` through `testing/router_identity.env`, resets the target router just before child boot, and then starts the normal capture.
   - Goal: bias initial attach toward the non-target parent without changing stock paths or `forced-failover` behavior.

## Status vs acceptance

- ✅ Immediate parent-match path explicitly logged and classified.
- ✅ Variant CSV contains `classification` and `delta_ms_from_attach_start`.
- ✅ Immediate parent-match/no-switch excluded from `T6-T3` medians.
- ✅ Batch runner now preconditions `variant-* steady` by resetting the target router before child boot.
- ❌ Variant steady batches have not yet been rerun after that preconditioning change, so current tables still reflect the older smoke runs (0 valid switch-act trials so far).
- ❌ `T3`/`T6` >= 90% of valid switch-act trials not yet reached because post-change valid switch-act sample count is still uncollected.

## Raw artifacts used for latest smoke check

- mcast:
  - `testing/logs/variant-mcast-steady-20260511-224858-trial1.log`
  - `testing/logs/variant-mcast-steady-20260511-225018-trial2.log`
  - `testing/logs/variant-mcast-steady-20260511-225138-trial3.log`
  - `testing/logs/variant-mcast-steady-20260511-225258-trial4.log`
  - matching `.csv` files
- ucast:
  - `testing/logs/variant-ucast-steady-20260511-225443-trial1.log`
  - `testing/logs/variant-ucast-steady-20260511-225603-trial2.log`
  - `testing/logs/variant-ucast-steady-20260511-225723-trial3.log`
  - `testing/logs/variant-ucast-steady-20260511-225844-trial4.log`
  - matching `.csv` files
