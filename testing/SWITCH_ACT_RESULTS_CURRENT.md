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

## B) Variant steady USB thread-off smoke results

| scenario | mode | attempts | non-target confirmed | target still current | initial unknown | thread off failed | valid switch-act | median T6-T3 ms | median T6-T0 ms | preconditioning method |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| variant-mcast | steady | 4 | 0 | 4 | 0 | 0 | 0 | N/A | N/A | usb-thread-off |
| variant-ucast | steady | 4 | 0 | 4 | 0 | 0 | 0 | N/A | N/A | usb-thread-off |

Classification criteria implemented:
- `success_switch_act` only when:
  - `variant_precondition_result = non_target_confirmed`
  - `T3_attach_start` present
  - `T6_parent_match` present
- `precondition_failed_initial_parent_is_target` when:
  - `variant_precondition_result = target_still_current`

The earlier `thread_off_failed` smoke reruns turned out to be a tooling artifact: `testing/tools/thread_ctl.py` opened the USB serial port separately for `thread off` and `thread state`, and on this board each reopen effectively reset the router before the follow-up state check. That made the second command observe post-boot `enabled=true role=detached` instead of the real off-state.

After fixing the helper to verify `thread off` and `thread state` within a single serial session, the latest steady smoke reruns now show the intended behavior during preconditioning:

- `USB_CTL thread off -> OT_ERROR_NONE`
- `USB_CTL thread state enabled=false role=disabled`

So router2 **is** being locally disabled by the stronger off-path. Even with that confirmed, the child still initially reattaches to the target parent (`router2` / `da97557943a05aac`) in all 8 attempts, so all 8 latest trials classify as `precondition_failed_initial_parent_is_target` rather than `thread_off_failed`.

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

3. Router USB Thread control:
   - `components/thread_router_control/thread_router_control.cpp`
   - `components/thread_router_control/thread_router_control.h`
   - `components/thread_router_control/__init__.py`
   - `testing/configs/router_ftd.yaml`
   - Router now accepts newline-delimited USB serial commands:
     - `thread off <seconds>`
     - `thread on`
     - `thread state`
   - Strengthened off path now calls both:
     - `otThreadSetEnabled(instance, false)`
     - `otIp6SetEnabled(instance, false)`
   - On path remains:
     - `otIp6SetEnabled(instance, true)`
     - `otThreadSetEnabled(instance, true)`
   - Root-cause fix in `testing/tools/thread_ctl.py`:
     - off verification now sends `thread off` and `thread state` within one persistent serial session
     - this avoids false failures caused by reopening the USB serial port between commands
   - Stable log lines added:
     - `USB_CTL thread off requested timeout=60s`
     - `USB_CTL thread off -> OT_ERROR_NONE`
     - `USB_CTL thread on requested`
     - `USB_CTL thread on -> OT_ERROR_NONE`
     - `USB_CTL thread state enabled=<...> role=<...>`
     - `USB_CTL failsafe re-enable fired`

4. Variant batch runner behavior:
   - `testing/tools/run_trials_batch.sh`
   - Variant runs count only `success_switch_act` trials toward the valid target.
   - Variant steady runs now use USB Thread suppression on the target router (`thread off 60` / `thread on`) instead of repeated reset suppression.
   - After `thread off 60`, the runner immediately sends `thread state` and requires:
     - `USB_CTL thread state enabled=false role=disabled`
   - If that verification fails, the trial is classified as `thread_off_failed` and not counted.
   - Structured preconditioning metadata is still appended to each log.

5. Variant steady child configs:
   - `testing/configs/child_variant_multicast.yaml`
   - `testing/configs/child_variant_unicast.yaml`
   - Added batch preconditioning polling with timeout logging (`V_precondition_initial_parent_unknown=...`) so the child keeps checking until parent confirmation or timeout.

## Status vs acceptance

- ✅ No new runner mode added.
- ✅ Stock runner behavior unchanged.
- ✅ Variant steady now verifies/logs the initial parent before allowing the switch request.
- ✅ Trial logs now carry structured variant preconditioning metadata, including suppression start/end timestamps.
- ✅ Existing `variant-* steady` now uses USB Thread suppression rather than repeated target-router reset suppression.
- ✅ Runner now verifies `thread state` before child reset and classifies failed verification as `thread_off_failed`.
- ✅ Router firmware accepted `thread off 60`, `thread on`, and `thread state` over USB serial, with a failsafe re-enable path.
- ✅ Latest reruns prove `thread off 60` reaches `enabled=false role=disabled` before child reset.
- ❌ Even with router2 verified disabled, the child still started on the target parent in all 8 latest steady smoke attempts.
- ❌ No USB thread-off smoke run has yet demonstrated `non_target_confirmed` before switch request.
- ❌ 10 valid steady switch-act trials per variant mode have not been achieved yet.

## Raw artifacts used for latest USB thread-off smoke check

- mcast:
  - `testing/logs/variant-mcast-steady-20260512-215946-trial1.log`
  - `testing/logs/variant-mcast-steady-20260512-220108-trial2.log`
  - `testing/logs/variant-mcast-steady-20260512-220231-trial3.log`
  - `testing/logs/variant-mcast-steady-20260512-220354-trial4.log`
  - matching `.csv` and `.prep.out` files
- ucast:
  - `testing/logs/variant-ucast-steady-20260512-220542-trial1.log`
  - `testing/logs/variant-ucast-steady-20260512-220705-trial2.log`
  - `testing/logs/variant-ucast-steady-20260512-220827-trial3.log`
  - `testing/logs/variant-ucast-steady-20260512-220950-trial4.log`
  - matching `.csv` and `.prep.out` files
