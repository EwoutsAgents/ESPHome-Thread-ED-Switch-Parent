# Phase 4 selected-parent core port

## Status

**Complete.** The native core compiles, its inactive path is validated, and the
Phase 5 deferred controller completed the active multicast attach gate.

## Implemented unit

The hardware functional patch was replayed against a clean Track A worktree at:

```text
a12ff0d0f54fd41954b45047fcdd08f302731c5f
```

The resulting native patch is
[selected-parent-core.patch](otns/selected-parent-core.patch). It applies
directly to that clean commit and changes six files:

- adds `include/openthread/selected_parent.h`;
- adds `src/core/thread/selected_parent.hpp`;
- changes `src/core/api/thread_api.cpp`;
- changes `src/core/thread/mle.cpp`;
- changes `src/core/thread/mle.hpp`;
- changes `src/core/thread/mle_ftd.cpp`.

The patch contains 688 insertions and 25 deletions. Its SHA-256 is:

```text
9ac91535050180910552e12e4e0e13c35705108405d2ca2de9fd103ae13cf0e2
```

## Native corrections

### Declared bridge API

The hardware component previously called C symbols that were defined inside
OpenThread but declared separately by ESPHome-side code. The native port adds a
public header declaring callback registration, target selection, multicast and
unicast discovery, direct continuation, reset, active-state query, and operation
generation.

An internal header contains the notification and state declarations used by
MLE. This removes duplicated hand-written declarations from `mle.cpp`.

### Candidate snapshot defect

The hardware-generated source declared the snapshot fields but did not
initialize or populate them. The native port:

1. initializes both candidate objects with the OpenThread instance;
2. clears both candidates in the constructor;
3. initializes all added boolean state;
4. snapshots `mParentCandidate` only after the target Parent Response has
   passed normal protocol validation and fully populated the candidate;
5. clears the snapshot on ordinary attach and role-change cancellation.

This corrects the undefined multicast validity bit rather than reproducing it.

### Native C linkage

The hardware patch used initialized declarations of the form:

```cpp
extern "C" bool state = false;
```

GCC 13 rejects these under OpenThread's warning-as-error configuration. The
native port defines the variables inside an `extern "C"` block instead. No
warning suppression was added.

### Operation observability

The bridge now exposes:

- explicit operation reset;
- whether discovery is active;
- a monotonically increasing operation generation number.

The controller can use the generation to discard stale deferred callback
events from an earlier operation.

## Build validation

The current OTNS RFSIM build system compiled both executable families with PPS
disabled and warnings treated as errors:

```text
ot-cli-mtd SHA-256: 8135b041a700df332e61d2adfcfb5d8880e8bd0b63aef7c1c27c06a19f41ce9d
ot-cli-ftd SHA-256: 8e0d70ac4427962aa46ab6d813d601adfef17d67b2a545f13ccf939449163741
```

The symbols for reset, active query, generation query, multicast discovery,
unicast discovery, and selected-parent continuation are present in the linked
MTD executable.

These are development-build fingerprints. Phase 8 will create the canonical
binary manifests.

## Inactive-path regression

The patched MTD and FTD binaries were run in the OTNS-MAPS static two-router
parent-removal scenario without invoking a selected-parent operation, using
OTNS seed `2404`.

Observed result:

- initial parent: Router A;
- removed node: Router A;
- final parent: Router B;
- final MED state: `child`;
- post-removal recovery: 237 simulated seconds;
- final packet delivery ratio: 1.0;
- classification: `switch_observed`.

This matches the Phase 3 stock result and shows that merely using the patched
binary does not alter ordinary attachment behavior.

## Active multicast validation

The Phase 5 controller exposed the bridge through the native CLI and deferred
continuation until after OpenThread tasklets and platform drivers returned to
the application mainloop.

A deterministic two-router test using OTNS seed `2405` observed:

- initial parent Router A;
- selected target Router B by extended address;
- multicast command accepted at generation 2;
- Router A deleted immediately after acceptance;
- Parent Request started;
- target Parent Response accepted from Router B;
- Child ID Request started using the captured target candidate;
- selected-parent success with Router B as the reported parent;
- the MED in `child` state;
- core active state zero after success;
- attachment observed within the first one-second polling interval.

A separate timeout run used an unreachable target. It emitted
`reason=timeout`, returned core activity to zero, accepted a fresh generation,
and then cleared successfully. Together with the constructor, ordinary-attach,
role-change, success, timeout, and explicit-reset cleanup paths, this meets the
Phase 4 terminal-state requirement.
