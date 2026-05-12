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

## B) Variant steady post-change smoke results

| scenario | mode | attempts | non-target confirmed | target still current | initial unknown | valid switch-act | median T6-T3 ms | median T6-T0 ms | preconditioning method |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| variant-mcast | steady | 4 | 0 | 4 | 0 | 0 | N/A | N/A | repeated-target-router-reset |
| variant-ucast | steady | 4 | 0 | 4 | 0 | 0 | N/A | N/A | repeated-target-router-reset |

Classification criteria implemented:
- `success_switch_act` only when:
  - `variant_precondition_result = non_target_confirmed`
  - `T3_attach_start` present
  - `T6_parent_match` present
- `precondition_failed_initial_parent_is_target` when:
  - `variant_precondition_result = target_still_current`

These latest steady smoke reruns show the child still initially attached to the target parent (`router2` / `da97557943a05aac`) in all 8 attempts, even under repeated target-router resets held through the preconditioning window. So no valid `T3→T6` switch-act samples were produced yet.

## C) Variant end-to-end timing note

`T6-T0` is **end-to-end timing**, not switch-act timing.

Because the post-change smoke reruns did not produce `T6_parent_match`, there is no new `T6-T0` median to report from these runs.

## Implementation changes in this update

1. Immediate-success marker in variant component:
   - `components/thread_preferred_parent/thread_preferred_parent.cpp`
   - Added:
     - `T_success_immediate_parent_match; target=...`
     - `V_initial_parent_extaddr=...` before switch start

2. Extractor updates:
   - `testing/tools/extract_switch_timings.py`
   - Added variant preconditioning metadata fields:
     - `variant_preconditioning_method`
     - `variant_precondition_result`
     - `variant_target_suppression_start`
     - `variant_target_suppression_end`
   - Added classification handling for:
     - `precondition_failed_initial_parent_is_target`
     - `success_switch_act`
     - `immediate_parent_match_no_switch`
     - `timeout_or_failure`
     - `unclassified`

3. Variant batch runner behavior:
   - `testing/tools/run_trials_batch.sh`
   - Variant runs count only `success_switch_act` trials toward the valid target.
   - Variant steady runs now flash with batch-gated auto-triggering disabled, start a repeated target-router reset loop, wait up to `VARIANT_PRECONDITION_TIMEOUT` seconds for `V_precondition_initial_parent_extaddr=...`, stop suppression only after a result is known, and append structured preconditioning metadata to each log.

4. Variant steady child configs:
   - `testing/configs/child_variant_multicast.yaml`
   - `testing/configs/child_variant_unicast.yaml`
   - Added batch preconditioning polling with timeout logging (`V_precondition_initial_parent_unknown=...`) so the child keeps checking until parent confirmation or timeout.

## Status vs acceptance

- ✅ No new runner mode added.
- ✅ Stock runner behavior unchanged.
- ✅ Variant steady now verifies/logs the initial parent before allowing the switch request.
- ✅ Trial logs now carry structured variant preconditioning metadata, including suppression start/end timestamps.
- ✅ The runner/YAML no longer relies on a single target-router reset; it now uses repeated target-router reset suppression during the preconditioning window.
- ✅ Trials starting on the target parent are excluded from valid switch-act counts and classified as `precondition_failed_initial_parent_is_target`.
- ❌ Latest post-change smoke reruns still produced 0 valid switch-act trials for both `variant-mcast steady` and `variant-ucast steady` because all observed initial parents were still the target parent.
- ❌ No post-change smoke run has yet demonstrated `non_target_confirmed` before switch request.
- ❌ 10 valid steady switch-act trials per variant mode have not been achieved yet.

## Raw artifacts used for latest post-change smoke check

- mcast:
  - `testing/logs/variant-mcast-steady-20260512-085940-trial1.log`
  - `testing/logs/variant-mcast-steady-20260512-090100-trial2.log`
  - `testing/logs/variant-mcast-steady-20260512-090220-trial3.log`
  - `testing/logs/variant-mcast-steady-20260512-090340-trial4.log`
  - matching `.csv` files
- ucast:
  - `testing/logs/variant-ucast-steady-20260512-090527-trial1.log`
  - `testing/logs/variant-ucast-steady-20260512-090647-trial2.log`
  - `testing/logs/variant-ucast-steady-20260512-090807-trial3.log`
  - `testing/logs/variant-ucast-steady-20260512-090927-trial4.log`
  - matching `.csv` files
