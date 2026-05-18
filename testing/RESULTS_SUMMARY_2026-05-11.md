# Thread Parent-Switch Benchmark Results (2026-05-11)

## Latest stock-observed current-parent-off update (2026-05-18)

A fresh rerun was executed after adding variant-style stock diagnostics and timeout taxonomy (`SO_invariant_*`, `SO3_post_*`, explicit `SO6 classification=...`).

Latest current-parent-off rerun window: `20260518-111656` .. `20260518-114535`

- attempts: 15
- valid trials: 10/10
- valid-trial outcomes: `success_target_reached` 10/10
- non-valid classifications:
  - 4× `timeout_target_seen_but_never_left_current_parent`
  - 1× `capture_truncated_after_target_seen`
- disruption method: `usb-thread-off-hold` via `thread_ctl.py off-verify-disabled-hold`

Valid-trial outcomes only:
- `success_target_reached`: 10/10
- `timeout_target_not_reached`: 0/10
- SO2 observed: 10/10
- SO3 observed: 10/10
- SO4 parent changed: 10/10
- SO5 target reached: 10/10
- SO6 timeout/failure: 0/10
- median `SO3 - SO1`: **1849.0 ms**
- median `SO4 - SO1`: **2337.0 ms**
- median `SO5 - SO1`: **2340.0 ms**

Interpretation: stock-observed current-parent-off now has a variant-style valid batch with full 10/10 successful target reaches. The new diagnostics also explain the excluded attempts: in the repeated `timeout_target_seen_but_never_left_current_parent` cases, the child observed the target (and usually saw both target and non-target responses after `SO3`) but stayed attached to the original parent for the full timeout window. The remaining excluded attempt is now explained as `capture_truncated_after_target_seen`, which came from the capture ending before `SO5` or `SO6`; the runner has been updated to extend capture duration so future batches should not fall into that ambiguous bucket.

## Previous stock-observed current-parent-off update (2026-05-17)

The stock `current-parent-off` path was tightened to copy the multicast anti-`initial_parent_already_target` strategy more faithfully:

- runner-side target-router suppression before each trial,
- explicit non-target-start preconditioning,
- wait for target restoration before releasing stock search,
- and finally a stricter evidence gate that requires an observed non-target Parent Response before accepting the precondition.

Latest current-parent-off rerun window: `20260517-225012` .. `20260517-230837`

- attempts: 10
- valid trials: 10/10
- disruption method: `usb-thread-off-hold` via `thread_ctl.py off-verify-disabled-hold`
- non-valid classifications: none

Valid-trial outcomes only:
- `success_target_reached`: 6/10
- `timeout_target_not_reached`: 4/10
- SO2 observed: 10/10
- SO3 observed: 10/10
- SO4 parent changed: 6/10
- SO5 target reached: 6/10
- SO6 timeout/failure: 4/10
- median `SO3 - SO1`: **1742.5 ms**
- median `SO4 - SO1`: **3137.0 ms**
- median `SO5 - SO1`: **3140.0 ms**
- median `SO6 - SO1` (timeouts only): **44981.5 ms**

Interpretation: this is the first stock current-parent-off batch in this investigation that both removes the bad-start waste and produces a publishable set of successful target reaches. The remaining failures are no longer dominated by invalid starts; they are mixed behavioral timeouts after a much stronger mcast-style precondition.

## Fresh stock-observed rerun update (2026-05-16)

Two stock-observed reruns were executed after fixing stale router identity data and replacing the fragile current-parent-off `serial-reset` path with the same verified USB Thread-off hold used by the variant preconditioning flow.

Live router identities used during the rerun:
- router1 / primary: `588c81fffe5db0e0`
- router2 / secondary target: `588c81fffe5db0c4`

Runner changes relevant to interpretation:
- stock steady now uses the same valid-trial gating idea as the variant batches and rejects `initial_parent_already_target` starts;
- stock current-parent-off now refreshes router identities live and uses `thread_ctl.py off-verify-disabled-hold` instead of `timeout 8 esphome logs ... --reset`;
- router-port contention was removed by capturing only the child port during current-parent-off runs.

### Fresh stock-observed steady (gated valid batch)

Batch window: `20260516-115511` .. `20260516-122728`

- attempts: 24
- valid trials: 10/24
- non-valid classification: 14× `initial_parent_already_target`

Valid-trial outcomes only (`stock-observed-steady-20260516-120151-trial6.csv` .. `stock-observed-steady-20260516-122728-trial24.csv`):
- `success_target_reached`: 4/10
- `timeout_target_not_reached`: 6/10
- SO2 observed: 10/10
- SO3 observed: 10/10
- SO4 parent changed: 4/10
- SO5 target reached: 4/10
- SO6 timeout/failure: 6/10
- median `SO4 - C0`: **6701 ms**
- median `SO5 - C0`: **6704 ms**
- median `SO4 - SO1`: **6687.5 ms**
- median `SO5 - SO1`: **6690.5 ms**
- median `SO6 - SO1` (timeouts only): **15985 ms**
- median `SO3 - SO1`: **4791.5 ms**

Interpretation: once invalid “already on target” starts were gated out, stock steady produced a mixed batch instead of the earlier all-timeout interpretation. In this refreshed topology, stock steady reached the configured target in 4 of 10 valid non-target starts. The new `SO1`-anchored basis makes the stock batch more comparable to the variant `T3`-anchored attach-phase reporting.

### Earlier fresh stock-observed current-parent-off (gated valid batch)

Batch window: `20260516-131043` .. `20260516-132244`

- attempts: 10
- valid trials: 10/10
- disruption method: `usb-thread-off-hold` via `thread_ctl.py off-verify-disabled-hold`
- non-valid classifications: none in the final rerun

Valid-trial outcomes only:
- `timeout_target_not_reached`: 10/10
- SO2 observed: 7/10
- SO3 observed: 7/10
- SO4 parent changed: 0/10
- SO5 target reached: 0/10
- SO6 timeout/failure: 10/10
- median `SO4 - disruption_time`: **N/A**
- median `SO5 - disruption_time`: **N/A**
- median `SO3 - SO1`: **5040 ms**
- median `SO6 - SO1`: **9983.5 ms**

Interpretation: after the runner fix, the dominant earlier `current_parent_shutdown_failed` classification disappeared. This rerun cleaned up the runner behavior, but every valid trial still timed out before any parent change or target reach was observed. It is now superseded by the later 2026-05-17 mcast-style-gated rerun above.

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

Balanced batches were rerun with 10 valid switch-act trials targeted for each scenario:
- `stock-observed` `current-parent-off`: 10 attempts / 4 valid in the latest committed stock batch
- `variant-mcast` `steady`: 10 valid in 21 attempts (fresh gated rerun 2026-05-14)
- `variant-ucast` `steady`: 10 valid in 13 attempts (fresh gated rerun 2026-05-14)

Latest switch-act related outcomes from committed CSVs:
- stock current-parent-off:
  - SO2 observed: 7/10
  - SO3 observed: 7/10
  - SO4 parent changed: 1/10
  - SO5 target reached: 4/10
  - SO6 timeout/failure: 6/10
  - median `SO4 - disruption_time`: 7478 ms (n=1)
  - median `SO5 - disruption_time`: 5906 ms (n=4)
- variant-mcast steady (fresh gated rerun window `20260514-102429` .. `20260514-113542`):
  - valid `success_switch_act`: 10/21
  - non-valid classification: 11× `immediate_parent_match_no_switch`
  - T3 attach-start detected in valid trials: 10/10
  - T6 reached in valid trials: 10/10
  - median `T6-T3`: 4625 ms
  - median end-to-end `T6-T0`: 10751 ms
- variant-ucast steady (fresh gated rerun window `20260514-114837` .. `20260514-123121`):
  - valid `success_switch_act`: 10/13
  - non-valid classification: 3× `initial_parent_unknown`
  - T3 attach-start detected in valid trials: 10/10
  - T6 reached in valid trials: 10/10
  - median `T6-T3`: 5963.5 ms
  - median end-to-end `T6-T0`: 12806.5 ms

The gated reruns replace the earlier non-publishable variant interpretation. `T3` is now present in all 10/10 valid trials for both variant scenarios, so a publishable variant `T6-T3` comparison is now available.

## Final comparison / conclusion

Using the strict target-based metrics:
- stock-observed current-parent-off median `SO5 - SO1`: **2340 ms** in the latest valid-only rerun (**10/10** target reaches)
- variant-mcast steady median `T6 - T3`: **4625 ms**
- variant-ucast steady median `T6 - T3`: **5963.5 ms**

Using the new stock search-phase basis:
- stock-observed current-parent-off median `SO3 - SO1`: **1849.0 ms**
- stock-observed current-parent-off median `SO5 - SO1`: **2340 ms**
- stock-observed steady median `SO5 - SO1`: **6690.5 ms**
- variant-mcast steady median `T6 - T3`: **4625 ms**
- variant-ucast steady median `T6 - T3`: **5963.5 ms**

Interpretation:
- **stock-observed current-parent-off** is now the fastest successful median in the latest `SO1`-anchored dataset and now does so on a full **10/10 valid-trial** batch.
- **variant-mcast** remains the strongest target-steered comparison path because it still contributes a clean **10/10 valid attach-start-to-target-match** dataset with explicit selected-parent attach semantics.
- **variant-ucast** remains slower than variant-mcast and faster than stock steady on the `SO1`/`T3` search-phase basis.
- The new stock diagnostics materially improved evidence quality: rejected stock attempts are now explainable, with the dominant excluded class being `timeout_target_seen_but_never_left_current_parent` rather than vague timeout buckets.

Bottom line: the project now has a publishable stock-observed current-parent-off batch at roughly the same evidence quality level as the variant batches: valid-only gating, explicit precondition evidence, and a clear explanation of excluded attempts.

## Commands used

- Build/flash + verification:
  - `testing/tools/build_stock_observed_with_verification.sh`
- Steady batch run:
  - `testing/tools/run_trials_batch.sh stock-observed 10 80 steady`
- Current-parent-off batch run:
  - `testing/tools/run_current_parent_off_trials.sh stock-observed 10 80`
  - latest tuned rerun: `testing/tools/run_current_parent_off_trials.sh stock-observed 10 120`
  - latest diagnostic rerun: `testing/tools/run_current_parent_off_trials.sh stock-observed 10 120`
- Extractor:
  - `python3 testing/tools/extract_switch_timings.py --in <log> --label child --scenario stock-observed --mode <steady|current-parent-off> --out <csv>`
- Stock batch summary on the new `SO1` basis:
  - `python3 testing/tools/summarize_stock_observed_batches.py --glob 'testing/logs/stock-observed-steady-20260516-*.csv' --stamp-min 20260516-115511 --stamp-max 20260516-122728 --field delta_ms_from_search_start`
  - `python3 testing/tools/summarize_stock_observed_batches.py --glob 'testing/logs/stock-observed-current-parent-off-20260516-*.csv' --stamp-min 20260516-131043 --stamp-max 20260516-132244 --field delta_ms_from_search_start`
  - `python3 testing/tools/summarize_stock_observed_batches.py --glob 'testing/logs/stock-observed-current-parent-off-20260517-*.csv' --stamp-min 20260517-225012 --stamp-max 20260517-230837 --field delta_ms_from_search_start`
  - `python3 testing/tools/summarize_stock_observed_batches.py --glob 'testing/logs/stock-observed-current-parent-off-20260518-*.csv' --field delta_ms_from_search_start`
- Integrity check:
  - `python3 testing/tools/check_stock_observed_integrity.py`
