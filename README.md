# ESPHome Thread ED Switch Parent

ESPHome external component for experimenting with controlled parent switching on Thread end devices.

This component lets an ESPHome Thread end device attempt to connect to a specific Thread parent, identified either by the parent router's IEEE 802.15.4 extended address or by its RLOC16. It is mainly intended for testing, diagnostics, and controlled experiments with Thread parent selection behavior.

The component uses a two-phase flow:

1. **Discovery / preflight**: send an MLE Parent Request (multicast *or* unicast) while keeping the device attached to its current parent. During this phase, the component collects Parent Responses, logs candidates, checks whether the configured target parent appears, and retries discovery if the target is not visible.
2. **Selected-parent attach**: when the target parent is observed, invoke the patched OpenThread hook to start an attach attempt toward that selected parent. This bypasses the normal parent-selection step and directs the attach attempt toward the observed target parent.

> [!WARNING]
> This is an experimental component. It patches ESP-IDF's vendored OpenThread source during the PlatformIO build. Use it for testing and diagnostics, not as a general-purpose production Thread parent-selection mechanism.

## Features

- Select a preferred Thread parent by `parent_extaddr` or `parent_rloc`.
  - `parent_extaddr` is advised (especially in combination with a unicast parent request).
- Perform non-disruptive preflight discovery before attempting a selected-parent attach.
- Send Parent Request as multicast *or* unicast.
  - OpenThread exclusively uses multicast for Parent Requests, whereas this external component also permits unicast Parent Requests. This approach reduces the number of potential Parent Responses.
- Start selected-parent attach shortly after the target responds with `early_attach_on_target: true`. 
  - This feature is still a work in progress, but preliminary tests have been stable when using `early_attach_delay: 500ms`.
- Retry discovery when the target parent is not visible.
- Expose runtime controls through ESPHome lambdas, buttons, and text entities.
- Log Parent Response diagnostics for debugging Thread parent selection.
- Automatically registers the OpenThread patch script as a PlatformIO pre-build script.
- Provides safeguards such as attach timeouts and a busy guard for repeated switch requests.

## Requirements

- ESPHome with ESP-IDF framework support.
- An ESP32 Thread-capable target, such as an ESP32-H2 or ESP32-C6 board.
  - Note: testing has exclusively been done on ESP32-C6.
- ESPHome `openthread:` enabled in the device configuration.
- USB serial logging is recommended while testing, because the ESPHome API can temporarily disconnect during a selected-parent attach.

## Example configuration

```yaml
esphome:
  name: thread-preferred-parent-test
  friendly_name: Thread Preferred Parent Test

esp32:
  board: esp32c6  # Change to your Thread-capable ESP32 board
  framework:
    type: esp-idf

logger:
  level: VERY_VERBOSE  # Optional, VERY_VERBOSE should not be used production: https://esphome.io/components/logger/

api:

ota:
  - platform: esphome

openthread:
  device_type: MTD  # Necessary (as FTDs do not have a parent), but BE CAREFUL, requires a full wipe of the non-violatile storage to go back to FTD: https://esphome.io/components/openthread/
  tlv: "<PUT_YOUR_TLV HERE>"


external_components:
  - source:
      type: git
      url: https://github.com/EwoutBergsma/ESPHome-Thread-ED-Switch-Parent
      ref: main
    components: [thread_preferred_parent]
    refresh: 0s

thread_preferred_parent:
  id: preferred_parent

  # Preferred: target the parent by IEEE 802.15.4 extended address.
  parent_extaddr: "00124b0001abcdef"

  # Alternative: target the parent by RLOC16 instead.
  # Do not configure parent_extaddr and parent_rloc at the same time.
  # parent_rloc: 0x5800

  max_attempts: 3
  retry_interval: 8s
  selected_attach_timeout: 16s

  # Optional: send the preflight Parent Request directly to the target ExtAddr
  # instead of the all-routers multicast address.
  parent_request_unicast: false

  # Optional: start selected-parent attach shortly after the target responds,
  # instead of waiting for the full retry_interval discovery window.
  early_attach_on_target: true
  early_attach_delay: 500ms

  require_selected_parent_hook: true
  log_parent_responses: true

button:
  - platform: template
    name: "Switch Thread Parent"
    on_press:
      - lambda: |-
          id(preferred_parent).request_switch();

text:
  - platform: template
    id: preferred_parent_extaddr
    name: "Thread Preferred Parent ExtAddr"
    optimistic: true
    min_length: 0
    max_length: 23
    mode: text
    set_action:
      - lambda: |-
          id(preferred_parent).set_parent_extaddr(x);

  - platform: template
    id: preferred_parent_rloc16_text
    name: "Thread Preferred Parent RLOC16"
    optimistic: true
    min_length: 0
    max_length: 6
    mode: text
    set_action:
      - lambda: |-
          id(preferred_parent).set_parent_rloc16(x);
```

## Configuration options

| Option | Default | Description |
| --- | --- | --- |
| `id` | Required | ESPHome component ID. Use this ID from lambdas, template buttons, text entities, or other ESPHome actions, for example `id(preferred_parent).request_switch();`. |
| `parent_extaddr` | Optional | Target parent IEEE 802.15.4 extended address. This is the recommended way to identify a parent router because the extended address is stable across Thread topology changes. Configure either `parent_extaddr` or `parent_rloc`, not both. |
| `parent_rloc` | Optional | Target parent RLOC16, for example `0x5800`. This can be convenient while debugging because RLOC16 values appear in OpenThread diagnostics, but they can change when the Thread topology changes. Prefer `parent_extaddr` for repeated tests or long-lived configurations. Configure either `parent_rloc` or `parent_extaddr`, not both. |
| `max_attempts` | `5` | Maximum number of discovery cycles before the component gives up. Each attempt starts with a Parent Request discovery phase. If the target is observed, the component proceeds to selected-parent attach; if attach times out, the component returns to discovery and consumes another attempt. |
| `retry_interval` | `8s` | Length of the discovery/preflight window and the delay before retrying discovery. During this window, the component listens for Parent Responses and checks whether the configured target parent is visible. If `early_attach_on_target` is disabled, the component waits for this full interval before starting attach. |
| `selected_attach_timeout` | `16s` | Maximum time to wait after starting selected-parent attach for the device to become attached to the requested parent. If the current parent does not match the target before this timeout expires, the attach attempt is treated as timed out and the component returns to discovery, subject to `max_attempts`. |
| `parent_request_unicast` | `false` | When `false`, the preflight Parent Request is sent using normal multicast discovery. When `true`, the component tries to send the Parent Request directly to the target extended address. This is most useful together with `parent_extaddr`; when only an RLOC16 is configured, the component must first resolve it to an extended address. |
| `early_attach_on_target` | `true` | When enabled, the component starts selected-parent attach shortly after the target parent is first observed during discovery. This avoids waiting for the entire `retry_interval` when the desired parent has already responded. When disabled, attach starts only after the discovery window completes. |
| `early_attach_delay` | `250ms` | Delay between observing the target Parent Response and starting selected-parent attach when `early_attach_on_target` is enabled. This acts as a debounce period and gives additional Parent Responses time to arrive before the discovery-to-attach handoff. Higher values, such as `500ms`, may be useful while testing. |
| `require_selected_parent_hook` | `true` | Require the patched OpenThread selected-parent attach hook to be available. Keeping this enabled makes failures explicit if the patch was not applied or is incompatible with the ESP-IDF/OpenThread version. If disabled, the component may try fallback OpenThread APIs where available, but behaviour is less controlled. |
| `log_parent_responses` | `true` | Enable buffered Parent Response diagnostics. With `logger.level: INFO` or `DEBUG`, the component reports lifecycle events, summaries, and relevant buffered responses on success or failure. With `logger.level: VERY_VERBOSE`, it also logs live Parent Response rows as they arrive. |


`parent_extaddr` accepts these formats:

```yaml
parent_extaddr: "00124b0001abcdef"
parent_extaddr: "00:12:4b:00:01:ab:cd:ef"
parent_extaddr: "00-12-4b-00-01-ab-cd-ef"
parent_extaddr: "0x00124b0001abcdef"
```

`parent_rloc` accepts integer or hexadecimal-style values:

```yaml
parent_rloc: 0x5800
parent_rloc: "5800"
```

## Runtime control

You can change the target parent at runtime from ESPHome lambdas, template text entities, or Home Assistant controls:

```cpp
id(preferred_parent).set_parent_extaddr(x);
id(preferred_parent).set_parent_rloc16(x);
id(preferred_parent).request_switch();
```

A common setup is to expose:

- a button that calls `request_switch()`;
- a text entity for the target extended address;
- a text entity for the target RLOC16.

## Logging

With `logger.level: INFO` or `DEBUG`, the component logs the switch lifecycle: discovery attempts, target detection, attach start, attach result, and summaries.

For detailed MLE diagnostics, enable very verbose logging:

```yaml
logger:
  level: VERY_VERBOSE
```

With `VERY_VERBOSE`, the component logs live Parent Response rows, including target matches and timing information. This is useful when checking whether the target router is visible before attempting selected-parent attach.

During the selected-parent attach phase, the ESPHome API may briefly disconnect if the node is connected over Thread. Use USB serial logs for uninterrupted diagnostics.

## OpenThread patching

The component automatically registers `apply-openthread-selected-parent-hook.py` as a PlatformIO pre-build script. You do not need to add a manual `platformio_options.extra_scripts` entry.

The patch adds OpenThread hooks used to:

- report MLE Parent Responses back to the ESPHome component;
- start a non-disruptive discovery-only Parent Request cycle;
- optionally perform unicast Parent Request discovery;
- start a selected-parent attach attempt toward the observed target parent.

## Notes and limitations

- This component is designed for experimentation with Thread parent selection.
- Prefer `parent_extaddr` when possible. RLOC16 values can be convenient for diagnostics, but extended addresses are a better stable identifier for a specific parent.
- The selected parent must be visible during discovery before the attach phase is started.
- If the OpenThread patch does not apply cleanly against the ESP-IDF/OpenThread version in your build, selected-parent switching will not work.
- Keep a serial console attached while developing or debugging, especially if the device's ESPHome API connection depends on Thread connectivity.

## Repository layout

```text
components/thread_preferred_parent/   ESPHome external component and OpenThread patch script
examples/                             Example ESPHome configuration
patches/                              OpenThread patch reference
scripts/                              Helper scripts
```

