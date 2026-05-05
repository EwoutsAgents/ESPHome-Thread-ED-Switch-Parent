# ESPHome Thread Preferred Parent External Component

This is a starter external component for forcing an OpenThread End Device / Sleepy End Device to search for and attach to a specific Thread parent.

The component supports two target identifiers:

- `parent_rloc`: the candidate parent's RLOC16, for example `0x5800`.
- `parent_extaddr`: the candidate parent's IEEE 802.15.4 Extended Address, for example `00124b0001abcdef` or `00:12:4b:00:01:ab:cd:ef`.

Configure at most one of them statically. At runtime, Home Assistant can set either one through template entities or lambdas. Setting a RLOC16 target replaces any previous extended-address target. Setting an extended-address target replaces any previous RLOC16 target.

## Important implementation note

An ESPHome external component cannot force OpenThread's parent-selection decision by itself. OpenThread must be patched so the MLE attach path accepts only Parent Responses matching the selected identifier.

The included `patches/openthread-preferred-parent-api.patch` is an implementation guide for the OpenThread copy vendored by ESP-IDF. You will likely need to adapt the context lines to the exact OpenThread revision used by your ESPHome build.

## Example

```yaml
thread_preferred_parent:
  id: preferred_parent
  # Choose one, or set dynamically from Home Assistant.
  # parent_rloc: 0x5800
  # parent_extaddr: "00124b0001abcdef"
  max_attempts: 5
  retry_interval: 8s

button:
  - platform: template
    name: "Switch Thread Parent"
    on_press:
      - lambda: |-
          id(preferred_parent).request_switch();

number:
  - platform: template
    name: "Thread Preferred Parent RLOC16"
    min_value: 0
    max_value: 65534
    step: 1
    optimistic: true
    set_action:
      - lambda: |-
          id(preferred_parent).set_parent_rloc16(static_cast<uint16_t>(x));

text:
  - platform: template
    name: "Thread Preferred Parent ExtAddr"
    optimistic: true
    min_length: 0
    max_length: 23
    mode: text
    set_action:
      - lambda: |-
          id(preferred_parent).set_parent_extaddr(x);
```

## Behavior

1. The component checks that the node is currently attached as a Thread child.
2. It calls the patched OpenThread preferred-parent search API.
3. OpenThread sends MLE Parent Requests.
4. The patched OpenThread MLE attach logic ignores all Parent Responses except the one matching the configured RLOC16 or extended address.
5. If the target parent is not selected, the component retries until `max_attempts` is reached.

## Identifier choice

Use `parent_rloc` when you are testing a specific current topology. Use `parent_extaddr` when you want a more stable identifier across router ID / RLOC16 changes.
