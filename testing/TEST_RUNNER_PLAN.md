# Parent-Switch Benchmark Runner Plan

## Goal
Compare parent-switch timing for:
- Variant A (stock OpenThread)
- Variant B multicast (external component)
- Variant B unicast (external component)

while keeping the topology and dataset identical.

## Topology (fixed)
- Child ED: `CHILD_PORT`
- Router R1 (initial parent): `ROUTER_PRIMARY_PORT`
- Router R2 (alternate/target): `ROUTER_SECONDARY_PORT`

All values are defined in `testing/benchmark_profile.env`.

## Fairness tweak (applied)
Run both network conditions for Variant B as suggested:
1. **steady**: R1 stays online
2. **forced-failover**: R1 is powered off/disconnected shortly after switch trigger

For consistency, run the same two conditions for Variant A as well.

## Scenario matrix
1. `stock` + `steady`
2. `stock` + `forced-failover`
3. `variant-mcast` + `steady`
4. `variant-mcast` + `forced-failover`
5. `variant-ucast` + `steady`
6. `variant-ucast` + `forced-failover`

## Current steady variant runner defaults
For `variant-mcast` and `variant-ucast` steady runs, the child now defaults to the gated precondition path instead of the old immediate button press:
- `batch_precondition_gate: true`
- `batch_precondition_release_delay_ms: 75000ms`
- auto-trigger remains disabled by the batch runner during steady variant captures

The batch runner also now:
- refreshes the target router ExtAddr from live router control before flash/capture when available
- passes the refreshed `target_parent_extaddr` into the child config
- records the runtime target ExtAddr in log metadata as `# variant-target-parent-extaddr ...`

This is intended to prevent the child from pressing the switch button before the target-router suppression / restore window has completed.

## Per-run command
```bash
testing/tools/run_one_capture.sh <scenario> <mode> <duration_sec>
```

Examples:
```bash
testing/tools/run_one_capture.sh stock steady 120
testing/tools/run_one_capture.sh stock forced-failover 120
testing/tools/run_one_capture.sh variant-mcast steady 120
testing/tools/run_one_capture.sh variant-mcast forced-failover 120
testing/tools/run_one_capture.sh variant-ucast steady 120
testing/tools/run_one_capture.sh variant-ucast forced-failover 120
```

## Timing outputs
Each run writes:
- raw log: `testing/logs/<scenario>-<mode>-<timestamp>.log`
- extracted timing CSV: `testing/logs/<scenario>-<mode>-<timestamp>.csv`

CSV checkpoints:
- `T0_request`
- `T1_discovery_start`
- `T2_target_observed`
- `T3_attach_start`
- `T4_child_id_req`
- `T5_attach_done`
- `T6_parent_match`

## Operator notes for forced-failover mode
- Ensure child is attached to R1 before triggering.
- Trigger switch.
- Turn off/disconnect R1 shortly after trigger.
- Keep R2 online throughout.

## Immediate next validation
After the gated-default fix, rerun:
- `testing/tools/run_trials_batch.sh variant-mcast 10 80 steady`
- `testing/tools/run_trials_batch.sh variant-ucast 10 80 steady`

Success criteria for the rerun:
- the child log should show the precondition wait before button press
- `T3 selected-parent attach start` should appear reliably enough to publish `T6-T3`
- result summaries should be regenerated from the new CSV/log set
