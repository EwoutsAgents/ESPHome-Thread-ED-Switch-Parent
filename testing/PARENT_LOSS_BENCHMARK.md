# Stock Parent-Loss Benchmark

## Goal
Measure the stock OpenThread failover path for the ED under a simple condition:

> the ED is attached to R1, R1 disappears, and the ED recovers onto R2.

This is a failover benchmark, not a targeted parent-selection benchmark.

## Topology
- child ED: `CHILD_PORT`
- R1 / initial parent: `ROUTER_PRIMARY_PORT`
- R2 / fallback target: `ROUTER_SECONDARY_PORT`

The ports and cached ExtAddrs come from:
- `testing/benchmark_profile.env`
- `testing/router_identity.env`

## Method
### Preconditioning
1. Confirm child and router serial ports exist.
2. Confirm router Thread control is responsive.
3. Read live router ExtAddrs and verify they still match `router_identity.env`.
4. Flash `testing/configs/child_stock_parent_loss.yaml` to the child.
5. Force the ED onto R1 with the existing selected-parent mechanism.
6. Wait until the child reports `PLP1 preferred parent reached`.
7. Wait the stabilization window.
8. Arm the benchmark when the child logs:
   - `PL0 measurement armed; initial_parent=<R1> target_parent=<R2>`

### Measurement
1. Start child log capture.
2. Turn off R1 with `thread_ctl.py off-verify-disabled-hold`.
3. Append `# parent-loss-r1-off <ISO_TIMESTAMP>` once R1 off is confirmed.
4. Observe natural stock recovery.
5. Extract the following canonical events when present:
   - `PL2 recovery/search started`
   - `PL3 parent changed`
   - `PL4 target parent reached`
   - `PL5 timeout`

## Timings
The extractor writes one CSV row per trial with:
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

Definitions:
- `detection_latency_ms = T1 - T0`
- `switching_time_ms = T3 - T1`
- `total_failover_ms = T3 - T0`

Where:
- `T0` = `# parent-loss-r1-off ...`
- `T1` = `PL2 recovery/search started`
- `T2` = `PL3 parent changed`
- `T3` = `PL4 target parent reached`

If `PL2` is missing but `PL4` is present, `total_failover_ms` can still be reported while detection/switching subtotals stay blank.

## Validity rules
A trial is valid only if:
- the initial parent is R1;
- the target parent is R2;
- measurement was armed after preconditioning;
- R1 off was confirmed;
- R2 was online before measurement.

## Classifications
Expected explicit labels:
- `success_failover_to_r2`
- `timeout_failover_to_r2_not_reached`
- `precondition_failed_not_on_r1`
- `precondition_failed_r2_unavailable`
- `precondition_failed_router_identity_unknown`
- `invalid_r1_off_not_confirmed`

Preconditioning failures are not counted as benchmark failures.

## Commands
Preflight only:
```bash
testing/tools/run_stock_parent_loss_trials.sh --preflight
```

Run a small batch:
```bash
testing/tools/run_stock_parent_loss_trials.sh 3 120
```

Or through the batch wrapper:
```bash
testing/tools/run_trials_batch.sh stock-parent-loss 3 120
```

## Interpretation
Use `stock-parent-loss` as the primary stock baseline.

Keep the older `stock-observed` current-parent-off runner only as a secondary / experimental targeted-search benchmark when you specifically want to inspect parent-response behavior before failover.
