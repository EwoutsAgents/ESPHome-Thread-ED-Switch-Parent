# Results: Parent-Switch Act Timing (current)

## Current rerun status note (2026-05-20)

A fresh stock `current-parent-off` rerun was started after changing the forced-switch criterion so the current-parent hold must stay active past the real stock search start (`SO1`). At stop time, the rerun had completed 4 attempts with 0 valid trials accepted. None of those completed attempts reached `SO1`; all remained stuck in the pre-search gate and therefore do not change the published switch-act comparison tables below.

## Scope
This report separates **switch-act** and **end-to-end** metrics for:
1. stock-observed current-parent-off
2. variant-mcast steady
3. variant-ucast steady

Primary metrics:
- stock switch act (legacy disruption basis): `SO4_parent_changed - disruption_time`
- stock target reach (legacy disruption basis): `SO5_target_parent_reached - disruption_time`
- stock search-phase basis: `SO4_parent_changed - SO1_search_started` and `SO5_target_parent_reached - SO1_search_started`
- variant switch act: `T6_parent_match - T3_attach_start`
- variant end-to-end: `T6_parent_match - T0_request`

## Table 1 — Stock current-parent-off

| scenario | mode | trials | valid trials | SO4 successes | SO5 successes | median SO4-disruption_time (ms) | median SO5-disruption_time (ms) | median SO4-SO1 (ms) | median SO5-SO1 (ms) | median SO6-SO1 (ms) | disruption method | notes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| stock-observed | current-parent-off | 10 | 10 | 10 | 10 | N/A | N/A | 2337.0 | 2340.0 | N/A | usb-thread-off-hold | latest 2026-05-18 rerun with variant-style stock diagnostics; 10/10 valid trials reached target; follow-up on the same day showed a 120 s current-parent hold is the reliable default for forced-switch runs |

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
| strict target metric | `SO5 - SO1_search_started` | `T6 - T3` | `T6 - T3` |
| median (ms) | 2340 | 4625 | 5963.5 |
| valid successes contributing to median | 10 | 10 | 10 |
| notes | latest 2026-05-18 valid-only rerun after variant-style stock diagnostics and gating; 10/10 valid target reaches | gated rerun, target-steered attach | gated rerun, target-steered attach |

## Short conclusion

- On the strict target-based comparison, **stock current-parent-off** now has a publishable search-phase median: **2340 ms** for `SO5 - SO1_search_started` across **10/10** valid target reaches in the latest rerun.
- **variant-mcast** remains the cleanest target-steered comparison path at **4625 ms** median `T6 - T3`.
- **variant-ucast** remains slightly slower at **5963.5 ms** median `T6 - T3`.
- So the benchmark is now in a much cleaner state for reporting: both variant and stock current-parent-off now have valid-only gated batches with explicit evidence about excluded attempts.
- A same-day hold-duration validation showed that the stock forced-switch runner needs the current parent held off past real `SO1` start; a 120 s hold produced a clean 3/3 success confirmation batch with median `SO5 - SO1 = 1022 ms` and median `SO5 - SO3 = 697 ms`, so 120 s is now the recommended/default stock current-parent-off hold.

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

## Fresh stock steady update (2026-05-16)

The stock steady runner was also upgraded to count only valid non-target-start trials, mirroring the variant gated-batch approach.

Fresh steady rerun window: `20260516-115511` .. `20260516-122728`

- attempts: 24
- valid trials: 10/24
- non-valid classification: 14× `initial_parent_already_target`
- valid-trial outcomes:
  - `success_target_reached`: 4/10
  - `timeout_target_not_reached`: 6/10
  - SO2 observed: 10/10
  - SO3 observed: 10/10
  - SO4 parent changed: 4/10
  - SO5 target reached: 4/10
  - SO6 timeout/failure: 6/10
  - median `SO4 - C0`: 6701 ms
  - median `SO5 - C0`: 6704 ms
  - median `SO4 - SO1`: 6687.5 ms
  - median `SO5 - SO1`: 6690.5 ms
  - median `SO6 - SO1` (timeouts only): 15985 ms
  - median `SO3 - SO1`: 4791.5 ms

This replaces the earlier ungated interpretation where many starts silently began already attached to the configured target.

Using `SO1` makes the stock batch easier to compare with the variant attach-phase timing, because it isolates the search/decision phase instead of mixing in the request-to-search setup gap.

## Raw artifacts used

## Repro command for the new stock summary basis

- `python3 testing/tools/summarize_stock_observed_batches.py --glob 'testing/logs/stock-observed-steady-20260516-*.csv' --stamp-min 20260516-115511 --stamp-max 20260516-122728 --field delta_ms_from_search_start`
- `python3 testing/tools/summarize_stock_observed_batches.py --glob 'testing/logs/stock-observed-current-parent-off-20260516-*.csv' --stamp-min 20260516-131043 --stamp-max 20260516-132244 --field delta_ms_from_search_start`
- `python3 testing/tools/summarize_stock_observed_batches.py --glob 'testing/logs/stock-observed-current-parent-off-20260517-*.csv' --stamp-min 20260517-225012 --stamp-max 20260517-230837 --field delta_ms_from_search_start`
- `python3 testing/tools/summarize_stock_observed_batches.py --glob 'testing/logs/stock-observed-current-parent-off-20260518-*.csv' --field delta_ms_from_search_start`


### Stock table artifacts
- latest current-parent-off rerun:
  - `testing/logs/stock-observed-current-parent-off-20260518-111656-trial1.log` .. `testing/logs/stock-observed-current-parent-off-20260518-114535-trial15.log`
  - `testing/logs/stock-observed-current-parent-off-20260518-111656-trial1.csv` .. `testing/logs/stock-observed-current-parent-off-20260518-114535-trial15.csv`
- previous current-parent-off rerun:
  - `testing/logs/stock-observed-current-parent-off-20260517-225012-trial1.log` .. `testing/logs/stock-observed-current-parent-off-20260517-230837-trial10.log`
  - `testing/logs/stock-observed-current-parent-off-20260517-225012-trial1.csv` .. `testing/logs/stock-observed-current-parent-off-20260517-230837-trial10.csv`
- earlier current-parent-off rerun:
  - `testing/logs/stock-observed-current-parent-off-20260516-131043-trial1.log` .. `testing/logs/stock-observed-current-parent-off-20260516-132244-trial10.log`
  - `testing/logs/stock-observed-current-parent-off-20260516-131043-trial1.csv` .. `testing/logs/stock-observed-current-parent-off-20260516-132244-trial10.csv`
- fresh steady gated rerun:
  - `testing/logs/stock-observed-steady-20260516-115511-trial1.log` .. `testing/logs/stock-observed-steady-20260516-122728-trial24.log`
  - `testing/logs/stock-observed-steady-20260516-115511-trial1.csv` .. `testing/logs/stock-observed-steady-20260516-122728-trial24.csv`

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

Two defensible comparison bases are now available:
- strict target under current-parent disruption:
  - stock current-parent-off median `SO5-SO1`: 2340 ms (10/10 target reaches in the latest valid-only rerun)
  - variant-mcast median `T6-T3`: 4625 ms
  - variant-ucast median `T6-T3`: 5963.5 ms
- search-phase basis:
  - stock current-parent-off median `SO3-SO1`: 1849.0 ms and `SO5-SO1`: 2340 ms
  - stock steady median `SO5-SO1`: 6690.5 ms
  - variant-mcast median `T6-T3`: 4625 ms
  - variant-ucast median `T6-T3`: 5963.5 ms

In this dataset, **stock current-parent-off** now outperforms both variant medians on its successful `SO1`-anchored trials and now does so with a full 10/10 valid-trial batch, while **variant-mcast** still remains the cleanest target-steered reference path.
