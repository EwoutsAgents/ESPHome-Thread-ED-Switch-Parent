# Fast Attach testing methods

This variant repeats the stock parent-removal experiment with the Fast Attach behavior from OpenThread PR [#13121](https://github.com/openthread/openthread/pull/13121). The behavioral source is PR head `61034b8a7e776695d1afe30338b3f36d24733127`, backported onto Espressif OpenThread `a12ff0d0f54fd41954b45047fcdd08f302731c5f` as vendored by ESP-IDF 5.5.4.

The initial attach is normal. After the runner identifies and removes the child's current parent exactly as in the stock test, the child component observes the transition from an attached role to Detached and calls `otThreadSetFastAttachEnabled(instance, true)`. The API result and resulting enabled state are logged. A hardware run without the successful `FAST_ATTACH event=arm_after_detach api_error=0 enabled=1` marker is failed as invalid.

## Isolation

All child and router firmware uses `thread_fast_attach` and the dedicated `patches/fast-attach/openthread-fast-attach-pr13121.patch`. The runner defaults to:

```text
testing/.platformio-core/fast-attach/
testing/.platformio-core/fast-attach/packages/
```

Stock and ucast package trees are not patched. Routers need the patch because they interpret the Scan Mask `F` bit and apply the PR's reduced randomized response ceiling.

## Run

```bash
cd testing
./run_fast_attach_test.sh --config fast_attach_test_devices_4routers.toml
```

Two-, three-, and four-router TOMLs are provided. The runner otherwise preserves the stock erase, capture, settle, initial attach, parent detection, skip classification, parent removal, and observation sequence.

## Backport notes

The embedded backport includes the public APIs, compile-time option, one-shot runtime state, Scan Mask `F` bit, suppression for better-parent/better-partition scans, immediate selection of the first acceptable LQ3 response, and router jitter ceiling of `min(normal maximum, active_router_count * 32 ms)`.

The upstream CLI command, API-version integer bump, and nexus-only tests are omitted because they do not participate in ESPHome firmware behavior. The child-side code and public APIs are compiled unconditionally inside this isolated patched package rather than being removed by a compile-time guard; this avoids ESP-IDF's separate component compilation dropping PlatformIO application build flags. The configuration macro remains defined as `1`, and no unpatched variant consumes this package.

Runtime re-arming is application integration: ESPHome's OpenThread component owns the sole public state-change callback, so the isolated component observes the role transition in its fast loop instead of replacing that callback. OpenThread schedules reattach with a start delay after entering Detached; the API is called while the role is Detached and before the subsequent request in the expected ESP32 execution path. Hardware packet capture must still confirm that the recovery Parent Request carries `F=1`; the current runner records the PCAP but does not yet decode encrypted MLE Scan Mask TLVs automatically.

## Validation criteria

- Build logs must show the dedicated patch SHA-256 and successful application.
- The manifest records the variant, isolated PlatformIO paths, PR head, vendored revision, patch path/hash, and compile option.
- The child log must prove successful post-detach API re-arming.
- Router logs record the selected `ParentResponseDelay` value, Scan Mask, and child ExtAddr; the runner requires at least one diagnostic with the Fast Attach `F` bit set.
- Packet inspection should confirm `F=1`, reduced randomized router response jitter, and immediate LQ3 candidate selection.
- Compare recovery timing with stock using the same hardware, router count, dataset, and timing configuration.
