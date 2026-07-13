# Phase 1 hardware parity profile

## Purpose

This profile records the non-secret configuration values OTNS-MAPS should use
for the first matched static experiments.

Dataset credentials and physical serial-device assignments are intentionally
not repeated. OTNS should use an independently provisioned simulation dataset
while matching protocol settings that affect the experiment.

## Firmware roles

| Variant | Child configuration | Router configuration |
| --- | --- | --- |
| `stock` | `testing/configs/stock_child.yaml` | `testing/configs/stock_router_N.yaml` |
| `mcast` | `testing/configs/mcast_child.yaml` | `testing/configs/stock_router_N.yaml` |
| `ucast` | `testing/configs/ucast_child.yaml` | `testing/configs/stock_router_N.yaml` |
| `ucast_fastpr` | `testing/configs/ucast_fastpr_child.yaml` | `testing/configs/fastpr_router_N.yaml` |

All tested devices are ESP32-C6. Children are MTDs. Routers are FTDs.

## Thread and build settings

- IEEE 802.15.4 channel: 20.
- Child device type: MTD.
- Router device type: FTD.
- `CONFIG_OPENTHREAD_PARENT_SEARCH_MTD=n` for all child variants.
- ESPHome framework: ESP-IDF.
- ESP-IDF package version under audit: 5.5.4.
- Campaign child logging level: INFO.
- Detailed Parent Response logging: disabled.
- Selected-parent hook requirement: enabled.

## Preferred-parent settings

| Setting | `mcast` | `ucast` | `ucast_fastpr` |
| --- | ---: | ---: | ---: |
| `max_attempts` | 1 | 1 | 1 |
| `retry_interval` | 8 s | 8 s | 8 s |
| `selected_attach_timeout` | 16 s | 16 s | 16 s |
| `parent_request_unicast` | false | true | true |
| fast router response | false | false | true |

The internal ParentReq launch timeout is 15 seconds. The no-target callback
drain interval is 250 ms. These are not YAML options.

## Topology matrix

Run each variant with:

- two routers and one MED child;
- three routers and one MED child;
- four routers and one MED child.

The directed selected-parent scenarios share one runner. Variant TOML files
select child and router firmware profiles.

## Directed test timeline

1. Erase assigned devices and flash an empty configuration.
2. Start the IEEE 802.15.4 sniffer.
3. Wait 5 seconds of sniffer lead-in.
4. Flash and start logging all routers.
5. Wait 300 seconds for router topology settling.
6. Flash and start logging the child.
7. Wait 5 seconds for natural child attachment.
8. Parse the child's current parent extended address.
9. Map router extended addresses from router logs.
10. Select a random router other than the current parent.
11. Send `extaddr <target>` to the child.
12. Stop logging the initial parent and immediately replace its firmware with
    the empty configuration.
13. Continue capture for 360 seconds.
14. Stop capture, retrieve the PCAP, and analyze artifacts.

The runner does not wait for selected-parent success before removing the initial
parent. OTNS-MAPS must preserve that ordering.

## Target selection

- Candidates are mapped routers except the current parent.
- Without a seed, selection uses system randomness.
- With a seed, selection uses `seed + run_index`.
- Target identity is the stable extended address, not RLOC16.
- The manifest records initial parent, target router, target extended address,
  selection mode, seed, and removed device role.

## Skip and label semantics

The directed runner skips when:

- no usable current-parent evidence exists;
- the current parent cannot be mapped to a configured router;
- no eligible non-current target exists.

If the initial parent is leader, the run receives a leader-removal label but
continues. Leader removal is a valid, more disruptive experiment case.

## Timing sources

Hardware attach-phase timing comes from PCAP where possible. Serial logs and
runner timestamps provide lifecycle and orchestration evidence.

OTNS comparison must label its sources separately:

- OpenThread/OTNS event timestamp for packet stages;
- OTNS parent-state observation for final attachment;
- runner timestamp for command and node-deletion ordering.

Do not compare one-second parent polling directly with packet-level PCAP
intervals without reporting the resolution difference.
