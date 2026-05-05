# ESPHome Thread ED Switch Parent

ESPHome external component for testing controlled Thread end-device parent switching.

This version uses a safer two-phase flow:

1. **Discovery/preflight**: send a multicast MLE Parent Request while staying attached to the current parent.
2. Log every MLE Parent Response received.
3. If the configured target parent is observed, start the disruptive selected-parent attach.
4. If the target is not observed, retry discovery without dropping the current Thread/API connection.

The target can be specified as either:

```yaml
thread_preferred_parent:
  id: preferred_parent
  parent_extaddr: "00124b0001abcdef"
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

The patch adds three hooks to ESP-IDF's vendored OpenThread source:

- `thread_preferred_parent_ot_register_parent_response_callback(...)`
- `thread_preferred_parent_ot_start_parent_discovery(...)`
- `thread_preferred_parent_ot_request_selected_parent_attach(...)`

The discovery hook starts `SearchForBetterParent()` but patches the MLE attacher so the discovery cycle is cancelled before Child ID Request. This lets the component collect candidate Parent Responses without detaching from the current parent.

## Expected logs

For a missing target:

```text
Parent discovery attempt 1/5 for ExtAddr 32a4d516437f9abb
Starting non-disruptive multicast Parent Request discovery ...
Parent Response live #1: ExtAddr ... RLOC16 ... target_match=NO
Preferred parent ExtAddr 32a4d516437f9abb was not observed during discovery attempt 1/5
```

For a visible target:

```text
Parent Response live #2: ExtAddr e2f3ec457a4c6d17 RLOC16 0x4400 ... target_match=YES
Preferred parent ExtAddr e2f3ec457a4c6d17 was observed; starting selected-parent attach
Starting selected-parent attach to ExtAddr e2f3ec457a4c6d17
Selected-parent attach hook returned YES
```

During the selected-parent attach, the ESPHome API may temporarily disconnect if the node is connected over Thread. Use USB serial logs for uninterrupted MLE diagnostics.


### v10 behavior

The selected-parent attach phase now filters MLE Parent Responses: after preflight discovery observes the requested ExtAddr/RLOC16, OpenThread ignores non-target Parent Responses during the disruptive selected-parent attach. This prevents the normal parent-selection heuristic from falling back to the old or strongest parent.
