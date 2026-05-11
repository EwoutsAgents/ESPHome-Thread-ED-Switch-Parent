# Thread Parent-Switch Benchmark Results (2026-05-11)

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

## Commands used

- Build/flash + verification:
  - `testing/tools/build_stock_observed_with_verification.sh`
- Batch run:
  - `testing/tools/run_trials_batch.sh stock-observed 10 80 steady`
- Extractor:
  - `python3 testing/tools/extract_switch_timings.py --in <log> --label child --scenario stock-observed --mode steady --out <csv>`
- Integrity check:
  - `python3 testing/tools/check_stock_observed_integrity.py`
