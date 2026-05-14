# Results: Parent-Switch Act Timing (current)

## Scope
This report separates **switch-act** and **end-to-end** metrics for:
1. stock-observed current-parent-off
2. variant-mcast steady
3. variant-ucast steady

Primary metrics:
- stock switch act: `SO4_parent_changed - disruption_time`
- stock target reach: `SO5_target_parent_reached - disruption_time`
- variant switch act: `T6_parent_match - T3_attach_start`
- variant end-to-end: `T6_parent_match - T0_request`

## Table 1 — Stock current-parent-off

| scenario | mode | trials | valid trials | SO4 successes | SO5 successes | median SO4-disruption_time (ms) | median SO5-disruption_time (ms) | disruption method | notes |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| stock-observed | current-parent-off | 10 | 4 | 1 | 4 | 7478 | 5906 | serial-reset | from latest balanced stock rerun; serial-reset is weak fallback (not equivalent to hard power cut) |

## Table 2 — Variant switch-act

| scenario | mode | trials | T3 present | T6 present | valid T6-T3 trials | median T6-T3 (ms) | median T6-T0 (ms) | notes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| variant-mcast | steady | 10 | 0 | 10 | 0 | N/A | 33 | latest rerun; requests often completed with immediate parent-match path, so no attach-start marker emitted |
| variant-ucast | steady | 10 | 0 | 10 | 0 | N/A | 33 | same behavior as mcast in latest rerun |

## Table 3 — Interpretation

- Stock is not target-steered.
- `SO4` measures **any** parent change.
- `SO5` measures reaching the **configured target** parent.
- Variant `T6` measures reaching the configured target parent.
- Therefore: `SO5 vs T6` is the strict target comparison; `SO4 vs T6` is broader “any successful parent switch” comparison.

## Current status vs publishability criteria

- ✅ Variant reruns executed (`variant-mcast` 10, `variant-ucast` 10).
- ✅ `T6` detected in 10/10 for both variant batches.
- ❌ `T3` detection target not met in the latest committed balanced reruns (0/10, 0/10).
- ❌ Variant switch-act medians (`T6-T3`) are not yet publishable from those committed batches.

## Post-rerun runner/doc update (2026-05-13)

The child variant configs and steady batch runner were updated after the committed balanced reruns to stop the child from pressing the switch button too early during target-router suppression / restore preconditioning.

Updated defaults / runner behavior:
- `testing/configs/child_variant_multicast.yaml`
  - `batch_precondition_gate: true`
  - `batch_precondition_release_delay_ms: 75000ms`
- `testing/configs/child_variant_unicast.yaml`
  - `batch_precondition_gate: true`
  - `batch_precondition_release_delay_ms: 75000ms`
- `testing/tools/run_trials_batch.sh`
  - computes release delay from USB-off + post-restore settle windows
  - refreshes live target-router ExtAddr before flash/capture when router control is available
  - passes runtime `target_parent_extaddr` into the child build/log metadata

Spot-check evidence from the gated path:
- `testing/logs/variant-ucast-steady-20260513-192708-trial1.log`
  - precondition gate waited: `AUTO precondition satisfied ... waiting 75000ms ...`
  - delayed press occurred later: `AUTO release delay elapsed: pressing Variant B unicast switch button`
  - attach marker appeared: `T3 selected-parent attach start; target=588c81fffe5fd8c4`
  - switch completed successfully: `Thread parent switch succeeded; current parent is ExtAddr 588c81fffe5fd8c4`

Interpretation:
- this spot check suggests the early child-trigger problem is fixed in the gated path
- however, the publishable variant comparison still requires fresh full reruns using these updated defaults

## Raw artifacts used

### Stock table artifacts
- `testing/logs/stock-observed-current-parent-off-20260511-205544-trial1.log` .. `trial10.log`
- `testing/logs/stock-observed-current-parent-off-20260511-205544-trial1.csv` .. `trial10.csv`

### Variant table artifacts (latest reruns)
- mcast logs/csv:
  - `testing/logs/variant-mcast-steady-20260511-215258-trial1.log` .. `trial10.log`
  - `testing/logs/variant-mcast-steady-20260511-215258-trial1.csv` .. `trial10.csv`
- ucast logs/csv:
  - `testing/logs/variant-ucast-steady-20260511-220642-trial1.log` .. `trial10.log`
  - `testing/logs/variant-ucast-steady-20260511-220642-trial1.csv` .. `trial10.csv`

## Code changes in this update

- Added explicit attach trigger marker in component code:
  - `components/thread_preferred_parent/thread_preferred_parent.cpp`
  - log line: `T3 selected-parent attach start; target=%s`
- Updated extractor to use explicit T3 marker:
  - `testing/tools/extract_switch_timings.py`
  - `"T3_attach_start": re.compile(r"T3 selected-parent attach start(?:; target=.*)?")`

## Direct answer (current data)

With current data, stock switch-act (SO4-disruption) is on the order of seconds (median ~7.5s in latest current-parent-off stock run), while variant end-to-end (`T6-T0`) is ~33 ms in latest steady reruns. However, the **variant switch-act metric** (`T6-T3`) is still unavailable in these latest variant reruns because `T3` did not appear, so a defensible stock-vs-variant **switch-trigger-to-parent-match** comparison is not yet publishable.
