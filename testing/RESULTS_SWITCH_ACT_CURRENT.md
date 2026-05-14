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

| scenario | mode | attempts | valid switch-act trials | non-valid classifications | T3 present in valid trials | T6 present in valid trials | median T6-T3 (ms) | median T6-T0 (ms) | notes |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| variant-mcast | steady | 21 | 10 | 11× `immediate_parent_match_no_switch` | 10 | 10 | 4625 | 10751 | gated 2026-05-14 rerun; publishable T3/T6 coverage recovered |
| variant-ucast | steady | 13 | 10 | 3× `initial_parent_unknown` | 10 | 10 | 5963.5 | 12806.5 | gated 2026-05-14 rerun; publishable T3/T6 coverage recovered |

## Table 3 — Interpretation

- Stock is not target-steered.
- `SO4` measures **any** parent change.
- `SO5` measures reaching the **configured target** parent.
- Variant `T6` measures reaching the configured target parent.
- Therefore: `SO5 vs T6` is the strict target comparison; `SO4 vs T6` is broader “any successful parent switch” comparison.

## Table 4 — Stock vs variant strict target comparison

| comparison basis | stock-observed current-parent-off | variant-mcast steady | variant-ucast steady |
|---|---:|---:|---:|
| strict target metric | `SO5 - disruption_time` | `T6 - T3` | `T6 - T3` |
| median (ms) | 5906 | 4625 | 5963.5 |
| valid successes contributing to median | 4 | 10 | 10 |
| notes | stock target reach after current-parent disruption | gated rerun, target-steered attach | gated rerun, target-steered attach |

## Short conclusion

- On the strict target-based comparison, **variant-mcast** is the fastest result in the current dataset at **4625 ms** median.
- **variant-ucast** is slightly slower at **5963.5 ms** median, essentially in line with the stock strict-target median of **5906 ms**.
- The important outcome is not just the medians: both variant scenarios now have **10/10 publishable `T3`→`T6` measurements**, while stock strict-target evidence remains based on only **4** successes in the latest current-parent-off batch.
- So the benchmark is now in a defensible state for reporting, with **multicast variant best on median switch-act time** in the current reruns.

## Current status vs publishability criteria

- ✅ Fresh gated variant reruns completed on 2026-05-14.
- ✅ `T6` detected in 10/10 valid switch-act trials for both variant batches.
- ✅ `T3` detected in 10/10 valid switch-act trials for both variant batches.
- ✅ Variant switch-act medians (`T6-T3`) are now publishable from these reruns.

## Gated rerun update (2026-05-14)

The child variant configs and steady batch runner were updated to stop the child from pressing the switch button too early during target-router suppression / restore preconditioning. Fresh steady reruns were then executed with the gated defaults and longer 210 s captures so the delayed button press and attach path were fully observed.

Updated defaults / runner behavior used for these reruns:
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

Representative successful gated evidence:
- `testing/logs/variant-mcast-steady-20260514-113209-trial20.log`
  - delayed press after precondition wait
  - `T3 selected-parent attach start; target=588c81fffe5fd8c4`
  - successful target-parent match
- `testing/logs/variant-ucast-steady-20260514-123121-trial13.log`
  - delayed press after precondition wait
  - `T3 selected-parent attach start; target=588c81fffe5fd8c4`
  - `T6_parent_match` / success recorded in CSV

Interpretation:
- the early child-trigger problem is fixed in the gated path
- both variant steady scenarios now have publishable attach-start-to-parent-match measurements

## Raw artifacts used

### Stock table artifacts
- `testing/logs/stock-observed-current-parent-off-20260511-205544-trial1.log` .. `trial10.log`
- `testing/logs/stock-observed-current-parent-off-20260511-205544-trial1.csv` .. `trial10.csv`

### Variant table artifacts (fresh gated reruns)
- mcast logs/csv:
  - `testing/logs/variant-mcast-steady-20260514-102429-trial1.log` .. `testing/logs/variant-mcast-steady-20260514-113542-trial21.log`
  - `testing/logs/variant-mcast-steady-20260514-102429-trial1.csv` .. `testing/logs/variant-mcast-steady-20260514-113542-trial21.csv`
- ucast logs/csv:
  - `testing/logs/variant-ucast-steady-20260514-114837-trial1.log` .. `testing/logs/variant-ucast-steady-20260514-123121-trial13.log`
  - `testing/logs/variant-ucast-steady-20260514-114837-trial1.csv` .. `testing/logs/variant-ucast-steady-20260514-123121-trial13.csv`

## Code changes in this update

- Added explicit attach trigger marker in component code:
  - `components/thread_preferred_parent/thread_preferred_parent.cpp`
  - log line: `T3 selected-parent attach start; target=%s`
- Updated extractor to use explicit T3 marker:
  - `testing/tools/extract_switch_timings.py`
  - `"T3_attach_start": re.compile(r"T3 selected-parent attach start(?:; target=.*)?")`

## Direct answer (current data)

A defensible stock-vs-variant switch-trigger-to-parent-match comparison is now available:
- stock strict target median `SO5-disruption_time`: 5906 ms
- variant-mcast median `T6-T3`: 4625 ms
- variant-ucast median `T6-T3`: 5963.5 ms

In this dataset, **variant-mcast** is the best median result, **variant-ucast** is roughly on par with stock strict-target timing, and both variant paths now have publishable `T3`/`T6` coverage.
