# ESPHome Thread ED Switch Parent

ESPHome external component for asking an OpenThread End Device / Sleepy End Device to reattach to a preferred Thread parent.

This version uses the same OpenThread-extension pattern as `ESPHome-biparental-ED`:

1. The ESPHome external component declares a weak C symbol.
2. A script patches ESP-IDF's vendored OpenThread source.
3. The patched OpenThread core exports the C bridge.
4. The component calls the bridge if it is present at runtime.

## Preferred target identifiers

The component accepts either:

- `parent_extaddr`: the candidate parent's IEEE 802.15.4 Extended Address, for example `00124b0001abcdef` or `00:12:4b:00:01:ab:cd:ef`.
- `parent_rloc`: the candidate parent's RLOC16, for example `0x5800`.

Use `parent_extaddr` when possible. The selected-parent OpenThread hook can directly target an extended address. RLOC16 support is best-effort with this selected-parent approach: the component first tries to resolve the RLOC16 from OpenThread's neighbor table. If that fails, it falls back to older optional RLOC16 preferred-parent APIs when available.

## Apply the OpenThread hook

The ESPHome component alone cannot force OpenThread to choose a parent. Patch ESP-IDF's vendored OpenThread core first:

```bash
python3 scripts/apply-openthread-selected-parent-hook.py
```

Default patch target:

```text
~/.platformio/packages/framework-espidf/components/openthread/openthread/src/core
```

For Home Assistant ESPHome add-on or Docker builds, pass the actual PlatformIO cache path explicitly, for example:

```bash
python3 scripts/apply-openthread-selected-parent-hook.py \
  /data/cache/platformio/packages/framework-espidf/components/openthread/openthread/src/core
```

Then run a clean build:

```bash
esphome clean your_node.yaml
esphome compile your_node.yaml
```

The patch exports this bridge:

```cpp
extern "C" bool thread_preferred_parent_ot_request_selected_parent_attach(
    otInstance *instance,
    const otExtAddress *preferred_ext_address
);
```

The component also detects the compatible `biparental_ot_request_selected_parent_attach(...)` symbol if you already applied the `ESPHome-biparental-ED` hook.

## Example

```yaml
thread_preferred_parent:
  id: preferred_parent
  parent_extaddr: "00124b0001abcdef"
  max_attempts: 5
  retry_interval: 8s
  require_selected_parent_hook: true

button:
  - platform: template
    name: "Switch Thread Parent"
    on_press:
      - lambda: |-
          id(preferred_parent).request_switch();
```

Runtime Home Assistant control is shown in `examples/thread_preferred_parent_example.yaml`.

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
3. If not found, it tries the older optional RLOC16 preferred-parent API names.
4. If neither route exists, it reports `rloc16 not resolved to extaddr` or `selected-parent OpenThread hook missing`.

## Notes

RLOC16 values are topology-derived and may change. Extended address is the better long-lived identifier for parent targeting.
