# ESPHome Thread ED Switch Parent

**v19 build fix:** fixes the early-attach OpenThread patch so `AttachToSelectedParent()` no longer declares an initialized local variable after a `VerifyOrExit(...)` macro. This avoids the C++ compile error where `goto exit` crosses initialization of `threadPreferredParentDiscoveryActive`.

**v18 early-attach:** adds `early_attach_on_target` and `early_attach_delay`. When the requested parent responds during discovery, the component now schedules selected-parent attach after the configured debounce instead of waiting for the full `retry_interval`. The OpenThread selected-parent hook also interrupts an active discovery-only pass so early attach does not bounce with `kErrorBusy`. Discovery logs now include a timer for target-observed time and total discovery time before attach.

**v16 build fix:** repairs the `parent_request_unicast` OpenThread patcher so `mle.cpp` is not truncated, restores a previously truncated patched `mle.cpp` from the `.thread-preferred-parent.bak` backup when present, and always declares the unicast discovery bridge symbols before use.

**v15 unicast discovery option:** add `parent_request_unicast: true` to send the preflight Parent Request directly to the configured parent ExtAddr instead of the all-routers multicast address. The selected-parent attach path remains the same.

**v13 diagnostics cleanup:** live Parent Response rows now use ESPHome's normal `VERY_VERBOSE` logger level, replay output is curated, discovery windows emit compact summaries, and Parent Response timestamps are relative to the current attempt.

**v12 targeted attach update:** this package now ports the important selected-parent attach lessons from ESPHome-biparental-ED: it keeps the child attached while attempting the selected-parent Child ID exchange, pre-seeds the target ExtAddr before `Attach(kSelectedParent)`, and forces `ChildIdRequest` for selected-parent mode once the target Parent Response has populated the OpenThread parent candidate. This is intended to fix the failure mode where the target appears in Parent Responses but OpenThread never completes the selected-parent attach.

ESPHome external component for testing controlled Thread end-device parent switching.

This version uses a safer two-phase flow:

1. **Discovery/preflight**: send an MLE Parent Request while staying attached to the current parent. By default this is multicast; set `parent_request_unicast: true` to unicast the Parent Request to the configured parent ExtAddr.
2. Track every MLE Parent Response; live rows are shown only when `logger.level` is `VERY_VERBOSE`.
3. If the configured target parent is observed and `early_attach_on_target: true`, wait `early_attach_delay` and start selected-parent attach without waiting for the full `retry_interval`.
4. If early attach is disabled, wait for the full discovery window before attaching.
5. If the target is not observed, retry discovery without dropping the current Thread/API connection.

The target can be specified as either:

```yaml
thread_preferred_parent:
  id: preferred_parent
  parent_extaddr: "00124b0001abcdef"
  parent_request_unicast: false
  early_attach_on_target: true
  early_attach_delay: 250ms
```

or:

```yaml
thread_preferred_parent:
  id: preferred_parent
  parent_rloc: 0x4400
```

Runtime Home Assistant text entities can also call:

```cpp
id(preferred_parent).set_parent_extaddr(x);
id(preferred_parent).set_parent_rloc16(value);
id(preferred_parent).request_switch();
```

## OpenThread patching

The component registers `apply-openthread-selected-parent-hook.py` automatically as a PlatformIO pre-build script. No manual `platformio_options.extra_scripts` entry is required.

The patch adds four hooks to ESP-IDF's vendored OpenThread source:

- `thread_preferred_parent_ot_register_parent_response_callback(...)`
- `thread_preferred_parent_ot_start_parent_discovery(...)`
- `thread_preferred_parent_ot_start_parent_discovery_unicast(...)`
- `thread_preferred_parent_ot_request_selected_parent_attach(...)`

The discovery hook starts `SearchForBetterParent()` but patches the MLE attacher so the discovery cycle is cancelled before Child ID Request. This lets the component collect candidate Parent Responses without detaching from the current parent. With `parent_request_unicast: true`, the same discovery-only path is used, but the Parent Request destination is the configured target ExtAddr. With `early_attach_on_target: true`, the selected-parent attach hook can also interrupt an active discovery-only pass once the target has been observed.

## Expected logs

With normal `INFO` logging, discovery now produces compact lifecycle and summary rows instead of replaying every Parent Response:

```text
Parent discovery attempt 1/5 for ExtAddr 32a4d516437f9abb
Starting non-disruptive multicast Parent Request discovery ...
# or, with parent_request_unicast: true:
Starting non-disruptive unicast Parent Request discovery to ExtAddr 32a4d516437f9abb ...
Target Parent Response observed after 680 ms during discovery; early selected-parent attach scheduled in 250 ms
Discovery summary (early target debounce complete): 11 Parent Responses, 1 target match(es), best target RLOC16 0xb000 RSSI -69
Discovery result: target observed after 680 ms; starting selected-parent attach after 930 ms total discovery time (250 ms early-attach delay)
Preferred parent ExtAddr 32a4d516437f9abb was observed; starting selected-parent attach
Starting selected-parent attach to ExtAddr 32a4d516437f9abb
Selected-parent attach hook returned YES
Attach result: success after 3498 ms; ExtAddr 32a4d516437f9abb selected
Parent Response replay (success target replay): showing 2 buffered response(s)
Parent Response replay #4 attempt_t+680ms: ExtAddr 32a4d516437f9abb RLOC16 0xb000 RSSI -69 ... device_attached=YES target_match=YES
```

Set the normal ESPHome logger to `VERY_VERBOSE` when you want every live Parent Response row:

```yaml
logger:
  level: VERY_VERBOSE
```

At `VERY_VERBOSE`, live rows look like this:

```text
Parent Response live #4 attempt_t+680ms: ExtAddr cec5115b300418f0 RLOC16 0xb000 RSSI -69 ... device_attached=YES target_match=YES
```

On failure, the final replay still shows all buffered candidates at `INFO`, because that is the useful forensic case.


During the selected-parent attach, the ESPHome API may temporarily disconnect if the OpenThread stack drops/rebuilds the Thread route. v12 tries to keep the node attached during the selected-parent Child ID exchange, but USB serial logs are still recommended for uninterrupted MLE diagnostics.


### v10 behavior

The selected-parent attach phase now filters MLE Parent Responses: after preflight discovery observes the requested ExtAddr/RLOC16, OpenThread ignores non-target Parent Responses during the disruptive selected-parent attach. This prevents the normal parent-selection heuristic from falling back to the old or strongest parent.


## v12 fix

This package fixes a clean-build ordering issue where ESP-IDF/OpenThread 5.5.4 could report `mle.cpp selected-parent candidate preseed` as missing while the old force-detach block was still present. The pre-build patcher now removes the old block before applying the preseed patch and also tolerates the legacy block if encountered.
