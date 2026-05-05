# ESPHome Thread ED Switch Parent

ESPHome external component for asking an OpenThread End Device / Sleepy End Device to reattach to a preferred Thread parent.

This version uses the same OpenThread-extension pattern as `ESPHome-biparental-ED`, but the OpenThread patch script is now registered automatically by the external component.

## What changed in this ZIP

You no longer need this in your YAML:

```yaml
esphome:
  platformio_options:
    extra_scripts:
      - pre:/config/esphome/scripts/apply-openthread-selected-parent-hook.py
```

Remove that block if you added it earlier.

The component now contains:

```text
components/thread_preferred_parent/apply-openthread-selected-parent-hook.py
```

and `components/thread_preferred_parent/__init__.py` automatically registers it as a PlatformIO pre-build script.

## Preferred target identifiers

The component accepts either:

- `parent_extaddr`: the candidate parent's IEEE 802.15.4 Extended Address, for example `00124b0001abcdef` or `00:12:4b:00:01:ab:cd:ef`.
- `parent_rloc`: the candidate parent's RLOC16, for example `0x5800`.

Use `parent_extaddr` when possible. The selected-parent OpenThread hook can directly target an extended address. RLOC16 support is best-effort: the component first tries to resolve the RLOC16 from OpenThread's neighbor table. If that fails, set `parent_extaddr` instead.

## Example

```yaml
external_components:
  - source:
      type: git
      url: https://github.com/EwoutBergsma/ESPHome-Thread-ED-Switch-Parent
      ref: main
    components: [thread_preferred_parent]

openthread:

thread_preferred_parent:
  id: preferred_parent
  parent_extaddr: "00124b0001abcdef"
  max_attempts: 5
  retry_interval: 8s
  require_selected_parent_hook: true
  log_parent_responses: true

button:
  - platform: template
    name: "Switch Thread Parent"
    on_press:
      - lambda: |-
          id(preferred_parent).request_switch();
```

Runtime Home Assistant control is shown in `examples/thread_preferred_parent_example.yaml`.

## Expected build behavior

During compile, you should see lines like:

```text
[thread_preferred_parent] OpenThread src/core: .../framework-espidf/components/openthread/openthread/src/core
[thread_preferred_parent][patched] .../thread/mle.hpp
[thread_preferred_parent][patched] .../thread/mle.cpp
[thread_preferred_parent][patched] .../api/thread_api.cpp
[thread_preferred_parent] OpenThread selected-parent hook is installed.
```

On later builds, `patched` may become `already`.

If the patch does not match the OpenThread revision, the build fails loudly instead of producing firmware that only reports `OT_ERROR_NOT_IMPLEMENTED` at runtime.

## Behavior

For `parent_extaddr`:

1. The component checks that the node is currently attached as a Thread child.
2. It calls the patched selected-parent OpenThread bridge.
3. OpenThread starts internal `kSelectedParent` attach mode.
4. The patched MTD Parent Request path unicasts the Parent Request to the selected parent's link-local address derived from its extended address.
5. The component checks whether the current parent now matches the target and retries until `max_attempts` is reached.

For `parent_rloc`:

1. The component checks whether the RLOC16 is already present in OpenThread's neighbor table.
2. If found, it converts that RLOC16 to the parent's extended address and uses selected-parent attach.
3. If not found, it tries older optional RLOC16 preferred-parent API names.
4. If neither route exists, it reports `rloc16 not resolved to extaddr` or `selected-parent OpenThread hook missing`.

## Notes

RLOC16 values are topology-derived and may change. Extended address is the better long-lived identifier for parent targeting.

## v3 selected-parent diagnostics

This version also injects optional OpenThread MLE diagnostics for the selected-parent path. Look for log lines containing `SelectedParent` from the OpenThread `Mle` module. They show whether the target Parent Response is received, rejected, whether the Child ID Request is sent, times out, or succeeds.

## v4 note

This version adds two diagnostics/fixes for selected-parent attach testing:

- The OpenThread hook forces `BecomeDetached()` before starting selected-parent attach.
- The ESPHome component logs the current parent before every attempt and logs whether the selected-parent hook returned true.

## v5 Parent Response reporting

This version also reports every MLE Parent Response that OpenThread receives during attach/search. The patch adds a small C callback bridge inside OpenThread and the ESPHome component registers a callback at setup.

Expected runtime log example:

```text
Parent Response #1: ExtAddr e2f3ec457a4c6d17 RLOC16 0x4400 RSSI -54 priority 0 LQ3/LQ2/LQ1 8/1/0 attached=YES target_match=YES
```

You can disable this logging with:

```yaml
thread_preferred_parent:
  log_parent_responses: false
```
