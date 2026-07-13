# Phase 1 preferred-parent behavior contract

## Scope

This document freezes the behavior that the first OTNS implementation should
reproduce from the ESPHome hardware experiments. It separates required
experimental behavior, wrapper behavior, diagnostics, compatibility fallbacks,
and defects that must be documented but not copied.

The contract is based on the current component, patchers, isolated clean and
patched ESP-IDF 5.5.4 OpenThread trees, test configurations, and directed test
runner.

## Required experiment variants

### Stock

- MED child running stock OpenThread.
- Periodic MTD parent search disabled.
- Stock FTD routers.
- Initial parent removed without a preferred-parent command.
- OpenThread performs ordinary recovery and parent selection.

### Multicast selected parent

- MED child uses the preferred-parent component.
- Target is configured by router extended address.
- Discovery Parent Request uses all-routers multicast.
- OpenThread reports all valid parsed Parent Responses to the controller.
- Candidate processing is constrained to the target.
- Target observation continues directly to Child ID Request.
- Routers use stock randomized Parent Response delay.

### Unicast selected parent

- MED child uses the preferred-parent component.
- Target is configured by router extended address.
- Discovery Parent Request uses the target's link-local IPv6 address.
- The immediate hook enters Attacher ParentReq without the ordinary Start delay.
- Target observation continues directly to Child ID Request.
- Routers use stock randomized Parent Response delay.

### Unicast selected parent with fast response

- Child behavior is identical to the unicast variant.
- Every experiment router uses the fast-response FTD build.
- An IPv6-unicast Parent Request receives an immediate Parent Response.
- Multicast Parent Requests retain stock randomized delay.

## Target and command semantics

The hardware runner sends:

```text
extaddr <16-hex-digit-target>
```

The firmware's USB task sets the target and immediately calls
`request_switch()`. Extended addresses accept optional `0x`, colon, hyphen,
space, or underscore separators and normalize to eight bytes. Exactly 16
hexadecimal digits are required.

The general component also accepts RLOC16, but directed campaigns select by
extended address. RLOC16 is compatibility scope, not an initial OTNS experiment
requirement.

A new request is rejected while another switch is active. Invalid or missing
targets are rejected before OpenThread is called. Success is not command or
bridge acceptance: success requires `otThreadGetParentInfo()` to report the
requested parent.

## Controller lifecycle

The wrapper has three phases:

```text
IDLE -> DISCOVERING -> ATTACHING -> IDLE
                      ^          |
                      | timeout  |
                      +----------+
```

For a switch request:

1. Reject it if busy or invalid.
2. Record the current parent when available.
3. Reset counters, callback generation, target observation, and buffered data.
4. Enter `DISCOVERING` with attempt count zero.
5. Increment the attempt count and launch discovery.
6. Start the discovery deadline when OpenThread reaches ParentReq.
7. On target observation, close discovery in the component loop.
8. Request direct continuation to Child ID Request.
9. On accepted continuation, enter `ATTACHING` and arm its timeout.
10. Declare success only after the current parent matches the target.
11. On attach timeout, return to `DISCOVERING`.
12. If the attempt budget is exhausted, fail and return to `IDLE`.

The hardware profile uses one attempt. The general component default is higher.

## Callback delivery

OpenThread callbacks enqueue copied events and schedule the ESPHome loop. They
do not directly drive Attacher transitions.

Required native-controller properties:

- events carry an attempt generation;
- stale-generation events are ignored;
- state transitions happen outside receive callbacks;
- queue access is synchronized;
- overflow is observable;
- Parent Response data is copied before callback return.

The ESPHome mailbox holds 24 events and drops the oldest event on overflow.
The native implementation need not use the same container but must preserve the
non-reentrant behavior.

## Multicast discovery

The controller supplies a target hint when it has an extended address, then
calls the discovery-only bridge. The bridge:

- sets `parent_discovery_active=true`;
- sets `parent_discovery_unicast=false`;
- calls `SearchForBetterParent()`;
- clears discovery flags if startup fails.

The ordinary better-parent machinery sends multicast Parent Request. When the
component-owned discovery timer completes, the patch returns the Attacher to
idle rather than allowing an ordinary reattach. The current parent remains
until selected-parent continuation progresses.

The parity deadline is eight seconds from observed ParentReq start. If no target
is observed, the controller adds 250 ms to drain queued responses.

## Immediate unicast discovery

For an extended-address target, the component prefers the immediate-unicast
bridge. It must:

- require an attached child;
- reject startup while another attach is active;
- set target and unicast discovery state;
- clear the current candidate;
- enter `kBetterParent` / `kStateParentRequest` directly;
- force receiver-on-when-idle for discovery if necessary;
- determine the normal Parent Request type;
- send using the target's link-local destination;
- start the normal Parent Request timer;
- restore receiver state and clear state on failure or completion.

The non-immediate unicast bridge remains a fallback through
`SearchForBetterParent()`. An unresolved RLOC16 target falls back to multicast
rather than failing solely on address resolution.

## Parent Request transmission

When component-owned unicast discovery is active, `SendParentRequest()` uses the
target's link-local IPv6 address.

In ordinary selected-router mode, FTD builds may use OpenThread `ParentSearch`.
MTD builds use the extended address pre-seeded in `mParentCandidate`. All other
cases use all-routers multicast.

The ParentReq-start callback fires immediately before `message->SendTo()` in the
current patch. OTNS timing must distinguish command acceptance, ParentReq state
entry, and actual message transmission when those timestamps are available.

## Parent Response processing

OpenThread keeps ordinary parsing and validation before reporting a response,
including Version, Challenge/Response, Source Address, Leader Data, Link Margin,
Connectivity, link, and partition checks.

The reporting bridge copies:

- extended address and RLOC16;
- RSSI and parent priority;
- LQ3, LQ2, and LQ1;
- whether the node is currently attached.

Reporting occurs before selected-target filtering, so the controller sees
non-target responses even though OpenThread does not use them as candidates.

During targeted discovery:

- non-target responses are dropped from candidate processing;
- the target may bypass ordinary better-parent comparison;
- protocol and security validation remain active;
- the target response populates the live candidate.

During legacy `kSelectedParent` attach, responses not matching the pre-seeded
candidate are dropped.

## Direct continuation

The current component refuses legacy selected-parent fallback after observing a
target. It requires direct discovery continuation.

Continuation must:

1. require the node to remain a child;
2. require a matching valid candidate;
3. clear component-owned discovery flags;
4. switch Attacher mode to `kSelectedParent`;
5. enter Child ID Request state;
6. arm Child ID Response timeout before transmission;
7. send Child ID Request using the accepted candidate;
8. return a concrete error on failure;
9. stop its timer and return idle on startup failure.

No second Parent Request should occur between accepted target Parent Response
and Child ID Request. Selected-parent mode does not require a comparison response
from the current parent, and generic better-parent ranking must not veto the
explicit target.

Routers extend the provisional child-entry timeout after Parent Request by 10
seconds, keeping it alive through the eight-second preflight and Child ID Request.

## Completion and failure

Current-parent match uses RLOC16 for an RLOC16 target and extended address for an
extended-address target. An accepted attach command that never changes the
parent is a timeout.

Parity values:

- discovery/retry interval: 8 seconds;
- ParentReq launch timeout after Start: 15 seconds;
- selected attach timeout: 16 seconds;
- maximum attempts: 1;
- no-target callback drain: 250 ms.

After selected-attach timeout, the component returns to discovery. With one
attempt already consumed, it then fails without launching another request.

## Fast router response

The fast-response router patch is compile-time gated and defaults the gate to
enabled in its patched source.

`HandleParentRequest()` classifies unicast from the IPv6 local destination
(`MessageInfo::GetSockAddr()`), because the handler does not retain the original
IEEE 802.15.4 destination.

For IPv6 unicast with the fast path enabled:

- call `SendParentResponse(info)` immediately;
- exit the handler;
- do not schedule a delayed response.

For multicast or a disabled fast path:

- calculate normal maximum delay from Scan Mask;
- select a random delay;
- schedule through `mDelayedSender`.

OTNS validation must prove no delayed duplicate follows the immediate response
and multicast timing remains unchanged.

## Diagnostics-only behavior

Useful but non-normative diagnostics include callback registration, response
counters, the 16-entry replay buffer, RSSI summaries, branch/status prose,
challenge/rejection logs, Child ID exchange logs, and final-parent logging.

The native controller should replace fragile prose with stable structured
events. It need not reproduce repeated logs or the currently disabled branch
replay mechanism.

## Out-of-scope compatibility paths

The initial OTNS port does not require:

- `biparental_ot_request_selected_parent_attach()`;
- older RLOC16 preferred-parent storage APIs;
- generic better-parent fallback when required hooks are missing;
- ESPHome text entities, Home Assistant controls, USB/FreeRTOS task code, or
  replay logging.

## Known source mismatch

The patcher intends to snapshot the target into
`mPreferredDiscoveryParentCandidate`. In the audited ESP-IDF 5.5.4 source:

- the snapshot transformation reports `missing`;
- the candidate is never initialized or populated;
- its validity bit is not initialized in the Attacher constructor;
- immediate unicast explicitly sets the bit to `false`;
- ordinary multicast does not explicitly initialize it;
- continuation normally uses the validated live `mParentCandidate` fallback.

The multicast validity read is therefore undefined C++ behavior. Hardware
success does not make it safe.

The OTNS port must choose and test one explicit design:

1. initialize, populate, validate, and clear a dedicated snapshot; or
2. remove the snapshot branch and validate the live candidate while discovery
   remains active.

A snapshot is safer if deferred controller work can outlive the live candidate.
The live-candidate design is smaller if event ordering proves it remains valid.

## Phase 1 exit assessment

Every generated OpenThread modification is mapped to functional or diagnostic
behavior in this contract and the canonical patch set. The snapshot mismatch is
recorded rather than treated as intended behavior.

Phase 2 may proceed with provenance recovery. Functional porting should wait
until the snapshot-versus-live-candidate decision is made for the selected native
OpenThread revision.
