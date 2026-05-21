# Parent-Switch Benchmark Runner Plan

## Goal
Use a simple stock baseline plus the two targeted Variant B runners:
- `stock-parent-loss` = stock OpenThread failover after the current parent disappears
- Variant B multicast (external component)
- Variant B unicast (external component)

while keeping the topology and dataset identical.

## Topology (fixed)
- Child ED: `CHILD_PORT`
- Router R1 (initial parent): `ROUTER_PRIMARY_PORT`
- Router R2 (alternate/target): `ROUTER_SECONDARY_PORT`

All values are defined in `testing/benchmark_profile.env`.

## Stock baseline (primary)
The recommended stock benchmark is now `stock-parent-loss`.

Method:
1. force the child onto R1 as setup only;
2. wait for stabilization on R1;
3. arm measurement;
4. turn off R1 with the verified USB Thread-off hold path;
5. measure natural stock OpenThread recovery to R2.

This intentionally replaces the older stock-targeted search path as the primary baseline because it is simpler and much more defensible.

## Scenario matrix
Primary baseline:
1. `stock-parent-loss`

Targeted switch comparisons:
2. `variant-mcast` + `steady`
3. `variant-mcast` + `forced-failover`
4. `variant-ucast` + `steady`
5. `variant-ucast` + `forced-failover`

Secondary / experimental stock paths:
- `stock-observed` current-parent-off targeted search runner
- legacy `stock` steady / forced-failover captures

## Current steady variant runner defaults
For `variant-mcast` and `variant-ucast` steady runs, the child now defaults to the gated precondition path instead of the old immediate button press:
- `batch_precondition_gate: true`
- `batch_precondition_release_delay_ms: 75000ms`
- auto-trigger remains disabled by the batch runner during steady variant captures

## Stock parent-loss runner defaults
`testing/tools/run_stock_parent_loss_trials.sh` now owns the stock baseline.

Defaults:
- `count=10`
- `duration=120`
- `STOCK_PARENT_LOSS_STABILIZE_SECONDS=10`
- `STOCK_PARENT_LOSS_R1_OFF_HOLD_SECONDS=120`
- `STOCK_PARENT_LOSS_ARM_TIMEOUT_SECONDS=90`

Validity rules:
- initial parent must be R1
- target parent must be R2
- measurement state must be armed after preconditioning
- R1 off must be confirmed
- R2 must be online before measurement

Classifications are expected to stay explicit:
- `success_failover_to_r2`
- `timeout_failover_to_r2_not_reached`
- `precondition_failed_not_on_r1`
- `precondition_failed_r2_unavailable`
- `invalid_r1_off_not_confirmed`
- `precondition_failed_router_identity_unknown`

## Per-run commands
Primary stock baseline:
```bash
testing/tools/run_stock_parent_loss_trials.sh 10 120
testing/tools/run_stock_parent_loss_trials.sh --preflight
```

Variant batch runs:
```bash
testing/tools/run_trials_batch.sh variant-mcast 10 80 steady
testing/tools/run_trials_batch.sh variant-mcast 10 80 forced-failover
testing/tools/run_trials_batch.sh variant-ucast 10 80 steady
testing/tools/run_trials_batch.sh variant-ucast 10 80 forced-failover
```

## Timing outputs
Each run writes:
- raw log: `testing/logs/<scenario>-<timestamp>.log`
- extracted timing CSV: `testing/logs/<scenario>-<timestamp>.csv`

`stock-parent-loss` CSV fields:
- `initial_parent_extaddr`
- `target_parent_extaddr`
- `final_parent_extaddr`
- `r1_off_time_utc`
- `recovery_start_time_utc`
- `parent_changed_time_utc`
- `target_parent_reached_time_utc`
- `detection_latency_ms`
- `switching_time_ms`
- `total_failover_ms`

Variant CSV checkpoints remain:
- `T0_request`
- `T1_discovery_start`
- `T2_target_observed`
- `T3_attach_start`
- `T4_child_id_req`
- `T5_attach_done`
- `T6_parent_match`

## Operator notes
For `stock-parent-loss`:
- R1 is the initial parent used only for setup.
- The measured phase begins only after `PL0 measurement armed` and `# parent-loss-r1-off ...`.
- Keep R2 online throughout the measured failover window.

For Variant B forced-failover modes:
- ensure child is attached before triggering;
- trigger switch;
- turn off/disconnect R1 shortly after trigger;
- keep R2 online throughout.

## Immediate next validation
1. Run `testing/tools/run_stock_parent_loss_trials.sh --preflight`.
2. Run a small stock batch such as `testing/tools/run_stock_parent_loss_trials.sh 3 120`.
3. Confirm every CSV row lands in an explicit classification.
4. Keep the older `stock-observed` path available only for secondary / experimental comparison.
