# Phase 10 comparable OTNS timing

## Result

Phase 10 is complete. The native selected-parent implementation now timestamps
the four attach protocol boundaries at their OpenThread callback sites, and
OTNS-MAPS derives the same interval sequence as the hardware PCAP analyzer.

The ESPHome hardware firmware was not changed.

## Native event instrumentation

The RFSIM platform enables `otPlatAlarmMicroGetNow()` with one-microsecond
resolution. The native controller captures its 32-bit node-local simulated
clock at:

- successful Parent Request `SendTo()` acceptance;
- validated target Parent Response reception;
- successful Child ID Request submission;
- accepted Child ID Response after child state installation.

Events include:

```text
time_us=<uint32>
timing_source=otns_openthread_event
resolution_us=1
```

The Child ID Request and Response hooks were added to the selected-parent bridge
so callback processing does not substitute the runner's one-second observation
time for protocol timing.

Patch fingerprints:

```text
selected-parent-core.patch             2a27b586474028dc7f6984563d3c7e9e0ebc67f4a558a6ef3f1da201e7c9bae4
preferred-parent-cli-controller.patch  b91b240999bc0377a5cc1ce4d18bd8af6aa80e32b3ebda2c5facb7831204832d
fast-unicast-parent-response.patch      783990f9ba10968ff5bbd12eb71465409af8f435873e5ec6168748cb3cda8a29
```

## OTNS-MAPS output

The directed runner now writes `preferred_parent_events_<timestamp>.csv` and
adds these summary fields:

- `protocol_event_timestamps`;
- `protocol_timing_ms`;
- `protocol_timing_complete`;
- `protocol_timing_source`;
- `protocol_timing_resolution_us`;
- `parent_deletion_to_target_observed_ms`;
- explicit deletion and parent-poll timing metadata.

The derived protocol intervals are:

- Parent Request to Parent Response;
- Parent Response to Child ID Request;
- Child ID Request to Child ID Response;
- Parent Request to Child ID Response (full attach).

The microsecond event clock is local to the child node. Parent deletion uses
global OTNS simulator time. The runner therefore derives protocol intervals
only within the node clock and never subtracts a node-local timestamp from the
global deletion timestamp.

Target-parent confirmation remains a one-second poll and is labeled
`otns_parent_poll` rather than `otns_openthread_event`.

## Rebuilt binary fingerprints

```text
stock-mtd-pps-off        bfb2ef7b9400ff0899769a5e5658f20f0812b57ca7ece335ecb9b1266c3040a5
preferred-parent-mtd     dd6d97f5418bd7f35b1674f32687faa6116afc65d198436070e2cca8bdba3627
stock-ftd                6c21e593fb01bd3cc984a138cbde863285c5842fe55dfd0b52a839fefe98064a
fastpr-ftd               7bc3917e1d80d8f57258b9eb20ce5049351b772dd4da84058cd8391bd0e6c260
```

## Real two-router validation

All values below are milliseconds and use native OTNS event timing:

| Variant | Parent Request → Response | Response → Child ID Request | Child ID Request → Response | Full attach |
| --- | ---: | ---: | ---: | ---: |
| multicast | 20.992 | 0.000 | 10.768 | 31.760 |
| unicast | 115.696 | 0.000 | 12.048 | 127.744 |
| unicast fast-response | 8.752 | 0.000 | 12.368 | 21.120 |

All three commands were acknowledged, emitted complete timestamped event sets,
and ended attached to the selected target.

The zero response-to-request interval means RFSIM advanced no simulated time
between response processing and Child ID Request submission. It is not a claim
about physical CPU execution time.

These two-router values are validation measurements, not a direct performance
comparison with the earlier four-router hardware runs. Phase 11 performs the
matched validation matrix and repeated comparisons.
