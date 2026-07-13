# OTNS Preferred-Parent Simulation Integration Plan

## Purpose

Reproduce the protocol-level parent-switching behavior from this repository in
the native OpenThread executables used by OTNS-MAPS.

The ESP32-C6 firmware images produced by ESPHome cannot run directly in OTNS.
They are ESP-IDF/FreeRTOS binaries for ESP32-C6 hardware, while OTNS runs native
host executables connected to its RFSIM radio model. The integration will
therefore port the relevant OpenThread changes and provide a small native
controller for OTNS.

The initial goal is source-level behavioral equivalence for the static MED
parent-removal experiments. It is not cycle-accurate ESP32 emulation and does
not attempt to reproduce ESPHome, FreeRTOS, USB, or ESP-IDF platform behavior.

## Repositories and responsibilities

### ESPHome-Thread-ED-Switch-Parent

This repository remains the reference implementation for the hardware tests.
It owns:

- the ESPHome component and its state-machine behavior;
- the patches applied to ESP-IDF's vendored OpenThread source;
- the hardware test configurations, runners, logs, and analysis definitions;
- the reference behavior and timing semantics to reproduce in simulation;
- canonical documentation of the selected-parent and fast-response changes.

### OTNS-MAPS

OTNS-MAPS will own the simulation-specific implementation. It will contain:

- the reproducible OpenThread patch series used for native RFSIM builds;
- the native preferred-parent CLI controller;
- stock, preferred-parent, and fast-response build profiles;
- directed parent-switch scenarios and runner support;
- OTNS event collection, result classification, and provenance manifests;
- comparison tooling for hardware and simulation results.

Changes should not couple either repository to local absolute paths. Cross-repo
inputs must be identified by Git commit and patch or artifact hash.

## Behavioral equivalence contract

The first implementation must support four experiment variants:

| Variant | Child behavior | Router behavior |
| --- | --- | --- |
| `stock` | Normal OpenThread recovery, PPS disabled | Stock FTD |
| `mcast` | Selected-parent discovery using multicast Parent Request | Stock FTD |
| `ucast` | Selected-parent discovery using unicast Parent Request | Stock FTD |
| `ucast_fastpr` | Selected-parent discovery using unicast Parent Request | Immediate response to unicast Parent Request |

Initial scenario scope:

- a MED child;
- static topologies with two, three, and four routers;
- routers settle for 300 simulated seconds;
- the child attaches and settles for 5 simulated seconds;
- the target is a known non-current router selected by extended address;
- the selected-parent request is issued once;
- the initial parent is removed immediately after the command is accepted;
- the child is observed for 360 simulated seconds;
- periodic parent search is disabled for parity with the hardware tests;
- deterministic target selection is available through a recorded random seed.

The simulation must preserve normal OpenThread validation of MLE messages. A
forced target may bypass ordinary better-parent ranking for the selected attach,
but it must not bypass security, Challenge/Response, address, or TLV validation.

## Target architecture

The integration has three layers.

### 1. OpenThread core changes

The native OpenThread tree will provide:

- selected-parent target state keyed by extended address;
- multicast and unicast Parent Request paths;
- target Parent Response filtering and capture;
- continuation from the captured Parent Response to Child ID Request;
- lifecycle callbacks or stable diagnostic events;
- cleanup on success, failure, timeout, cancellation, and ordinary attach;
- an optional FTD fast path for unicast Parent Responses.

These changes should be exposed through one documented internal bridge header.
Avoid duplicating undeclared weak symbols or platform-specific glue in the
controller.

### 2. Native OTNS controller

A small controller compiled into the native MTD CLI executable will replace the
ESPHome, ESP-IDF, and FreeRTOS wrapper. It will register commands with
`otCliSetUserCommands()` and drive the selected-parent operation through the
OpenThread bridge.

Proposed command surface:

```text
prefparent switch <extaddr> multicast
prefparent switch <extaddr> unicast
prefparent status
prefparent clear
```

Proposed state model:

```text
idle
target_configured
discovery_starting
waiting_parent_request
waiting_target_response
continuing_selected_attach
waiting_child_id_response
succeeded
failed
timed_out
```

Callbacks must enqueue work for later processing rather than recursively
changing MLE attacher state from inside a receive callback.

### 3. OTNS-MAPS orchestration

The OTNS-MAPS runner will:

1. create and settle the router topology;
2. add and attach the MED child;
3. identify the child's current parent;
4. choose a non-current target router and obtain its extended address;
5. send the `prefparent` command to the child;
6. delete the initial parent immediately after command acceptance;
7. observe parent, role, RLOC16, detach, recovery, and connectivity;
8. collect structured protocol events and classify the outcome;
9. write scenario, binary, patch, and source provenance to the result manifest.

## Work plan

Phase 1 is complete on this branch. Its audited outputs are:

- [`patches/phase-1-behavior-contract.md`](patches/phase-1-behavior-contract.md);
- [`patches/phase-1-hardware-profile.md`](patches/phase-1-hardware-profile.md);
- [`patches/canonical/`](patches/canonical/) with reproducible functional,
  diagnostic, and fast-response source deltas.

The audit found that the intended discovery-candidate snapshot is not populated
in the generated ESP-IDF 5.5.4 source. That mismatch is documented in the
behavior contract and must be resolved explicitly during the native port.

### Phase 1: Freeze the reference behavior

Document the exact semantics implemented by the current hardware firmware:

- selected-parent target setup and cleanup;
- multicast and unicast Parent Request construction;
- Parent Response filtering and target matching;
- cached response fields used for discovery continuation;
- the transition to Child ID Request;
- retry, busy-guard, and timeout behavior;
- fast unicast Parent Response behavior;
- machine-observable success and failure conditions.

Compare clean and patched OpenThread sources rather than treating the patching
script itself as the specification. Separate functional changes from logging
and diagnostic instrumentation.

Deliverables:

- a behavioral compatibility specification;
- canonical preferred-parent patch;
- canonical fast-response patch;
- optional diagnostics patch;
- a list of hardware configuration values used for parity.

Exit criterion: every functional source modification can be mapped to a stated
behavior or explicitly classified as diagnostics-only.

### Phase 2: Establish source provenance

Recover and record:

- the ESP-IDF 5.5.4 release used by the ESPHome builds;
- the exact OpenThread revision vendored by that ESP-IDF release;
- the OpenThread revision currently used by OTNS/RFSIM;
- the OTNS and OTNS-MAPS commits;
- the existing OTNS `ParentRank` instrumentation diff;
- hashes of the canonical patch files.

Preserve `ParentRank` as an independent patch or commit because it overlaps MLE
source files and must not be accidentally lost during the port.

Exit criterion: a clean checkout can reproduce each relevant source tree and
show exactly which patch set is applied.

### Phase 3: Select the native OpenThread base

Evaluate two tracks.

#### Track A: ESP-IDF's OpenThread revision

Point the RFSIM build at a clean copy of the OpenThread revision used by ESP-IDF.
This offers the closest source equivalence to the hardware firmware.

#### Track B: OTNS's current OpenThread revision

Semantically port the changes to the revision already used by OTNS. This is
likely easier to maintain but introduces an upstream-version difference between
hardware and simulation.

Decision procedure:

1. build unmodified `ot-cli-mtd` and `ot-cli-ftd` RFSIM executables from Track A;
2. run a stock two-router OTNS smoke test;
3. inspect compile, platform API, CLI, and runtime incompatibilities;
4. choose Track A if it works without substantial compatibility patches;
5. otherwise choose Track B and document the behavioral/version delta.

Exit criterion: the selected unmodified base passes a repeatable stock RFSIM
smoke test.

### Phase 4: Port selected-parent OpenThread behavior

Implement the port in small, reviewable units.

#### Bridge API

Provide native functions for:

- setting and clearing the target extended address;
- choosing multicast or unicast discovery;
- starting selected-parent discovery;
- observing Parent Request, Parent Response, and attacher-state events;
- continuing attach from a captured target response;
- querying whether an operation is active.

#### Targeted discovery state

Store:

- target extended address and validity;
- requested discovery mode;
- captured target candidate and validity;
- selected-parent operation generation or attempt identifier.

Clear it on all terminal and ordinary-attach paths to prevent stale state from
affecting later OpenThread behavior.

#### Unicast Parent Request

Ensure both IPv6 and MAC destinations identify the requested router. Preserve
the ordinary multicast path unchanged. Verify on-air/simulator events rather
than relying only on log text.

#### Parent Response handling

During an active selected-parent attempt:

- ignore non-target Parent Responses for target selection;
- accept the target without ordinary better-parent ranking rejecting it;
- retain normal protocol and security validation;
- capture all data required for the Child ID Request path;
- prevent a later non-target response from replacing the target candidate.

#### Discovery continuation

After accepting the target response:

- stop or close the discovery window safely;
- continue directly to Child ID Request using the captured candidate;
- do not transmit a redundant second Parent Request;
- keep the old attachment until the selected attach transition requires change;
- provide deterministic failure and rollback behavior.

#### Timing and cleanup

Initially match the hardware campaign configuration:

- one selected-parent attempt;
- 8-second discovery/retry window;
- 16-second selected-attach timeout;
- 15-second Parent Request launch timeout where applicable.

Use OpenThread/platform simulated time, never Python wall-clock time.

Exit criterion: a two-router unit scenario attaches the child to the specified
target via multicast and leaves ordinary stock attachment behavior unchanged
when no selected-parent operation is active.

### Phase 5: Add the native CLI controller

Implement command parsing, state transitions, deferred callback processing,
timeouts, reset, and status reporting.

Emit stable machine-readable events, for example:

```text
PREFPARENT event=requested target=<extaddr> mode=unicast
PREFPARENT event=parent_request_started
PREFPARENT event=target_response parent=<extaddr> rloc16=<value>
PREFPARENT event=child_id_request_started
PREFPARENT event=succeeded parent=<extaddr>
PREFPARENT event=failed reason=<reason>
```

Test valid compact and separated extended addresses, invalid input, missing or
unknown mode, reset, idle status, active status, and a second command while busy.

Exit criterion: OTNS can command, observe, and reset a selected-parent attempt
without parsing unstable human-oriented OpenThread log messages.

### Phase 6: Add unicast discovery

Enable the controller's unicast mode and verify:

- the Parent Request is addressed only to the selected router;
- a non-target router does not receive or answer the request through multicast;
- the response is matched to the target;
- the Child ID Request uses the selected candidate;
- the final parent is the requested router.

Exit criterion: deterministic two-router unicast tests pass repeatedly and the
multicast path remains unchanged.

### Phase 7: Add fast unicast Parent Responses

Implement the FTD behavior behind a compile-time option such as:

```text
OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE
```

When enabled, a router must identify an IPv6-unicast Parent Request and send its
Parent Response immediately, without scheduling the ordinary randomized delay.
Multicast requests must retain stock response timing. Ensure no delayed duplicate
response follows the immediate response.

Exit criterion: controlled tests show the expected unicast response-latency
difference between stock and fast-response FTD binaries, with no statistically
or functionally detectable change to multicast behavior.

### Phase 8: Produce the native binary matrix

Build at least:

- `stock-mtd-pps-off/ot-cli-mtd`;
- `preferred-parent-mtd-pps-off/ot-cli-mtd`;
- `stock-ftd/ot-cli-ftd`;
- `fastpr-ftd/ot-cli-ftd`.

One preferred-parent MTD binary should support multicast and unicast at runtime.
Stock binaries must be built without the selected-parent or fast-response
features, not merely with those features left unused.

#### Variant isolation and executable assignment

OpenThread variants must use isolated source and build trees. This mirrors the
separate PlatformIO package directories used by the hardware campaign and
prevents a source-mutating patch for one variant from contaminating another.
A suitable layout is:

```text
openthread-variants/
├── stock/
│   └── build/
├── preferred-parent/
│   └── build/
└── preferred-parent-fastpr/
    └── build/
```

Every OTNS node runs as a separate native process, so binaries produced from
these trees can coexist in one simulation without sharing OpenThread globals or
patch state. OTNS supports both family-wide executable selection:

```text
exe mtd "/path/preferred-parent/bin/ot-cli-mtd"
exe ftd "/path/stock/bin/ot-cli-ftd"
```

and a node-specific executable on `add`:

```text
add router id 1 exe "/path/stock/bin/ot-cli-ftd"
add router id 2 exe "/path/fastpr/bin/ot-cli-ftd"
add med id 10 exe "/path/preferred-parent/bin/ot-cli-mtd"
```

Use family-wide selection for the initial homogeneous experiment variants. Keep
node-specific selection available for mixed stock/fast-response router tests
and other variants with contradictory compile-time requirements.

The existing ESPHome isolation applies patches to a package shared by all
firmware compiled for that variant. The first OTNS builds should reproduce that
variant-level patch composition exactly. Role-specific child/router patch
composition may be introduced later as a separately labeled refinement, rather
than changing patch scope during the first hardware/simulation comparison.

Record for every binary:

- OpenThread base commit;
- patch-set commit or hashes;
- CMake and OpenThread configuration flags;
- PPS and fast-response settings;
- compiler and build-tool versions;
- binary SHA-256;
- whether `ParentRank` instrumentation is present.

Exit criterion: all four profiles build from isolated clean source trees, their
manifests uniquely identify the resulting executable, and a smoke scenario
proves that stock and patched binaries can run concurrently as separate OTNS
node processes.

### Phase 9: Extend OTNS-MAPS scenarios and runner

Add directed static scenarios for two, three, and four routers across `mcast`,
`ucast`, and `ucast_fastpr`. Retain corresponding stock baselines.

Suggested scenario configuration:

```yaml
scenario_type: directed_parent_switch

directed_switch:
  mode: unicast
  target_selection: random_non_current_parent
  remove_initial_parent: true
  random_seed: 1
  expected_router_firmware: stock
```

The runner must reject invalid binary/scenario combinations and record the
initial parent, target router, target extended address, target RLOC16, random
seed, command acknowledgement, deletion time, and final parent.

Scenario and runner configuration must support both a default MTD/FTD binary
for homogeneous runs and an optional executable override per node. The runner
should emit OTNS `add ... exe "<path>"` commands for per-node overrides and
record the resolved executable path and SHA-256 for every node in the manifest.

Retain or align hardware runner classifications where meaningful:

- no child parent;
- current parent cannot be mapped to a configured router;
- no eligible non-current target;
- current parent is the leader;
- command rejected;
- selected target reached;
- child attached to a non-target router;
- no reattachment;
- router topology changed during observation.

Leader-parent cases should be labeled but should not automatically invalidate a
run unless the scenario contract says so.

Exit criterion: one deterministic run for every two-router variant produces a
complete result and provenance manifest.

### Phase 10: Add comparable measurements

Record native simulation timestamps for:

- Parent Request transmission;
- target Parent Response reception;
- Child ID Request transmission;
- Child ID Response reception;
- initial parent deletion;
- final parent observation.

Derive:

- Parent Request to Parent Response;
- Parent Response to Child ID Request;
- Child ID Request to Child ID Response;
- Parent Request to Child ID Response;
- parent deletion to successful reattachment.

Label timing sources explicitly, for example:

```text
hardware_pcap
otns_openthread_event
otns_parent_poll
```

Do not present one-second OTNS polling and packet/event timestamps as equivalent
precision. Use protocol events for attach-phase latency and polling for coarse
state confirmation.

Exit criterion: hardware and simulation reports use the same semantic interval
definitions and disclose their timing source and resolution.

### Phase 11: Validation ladder

Run validation in increasing scope.

1. **Build validation**: all binary profiles compile and report correct feature
   markers and hashes.
2. **CLI validation**: valid, invalid, busy, status, and reset paths behave
   deterministically.
3. **Core protocol validation**: multicast/unicast addressing, response
   filtering, candidate capture, Child ID Request, cleanup, and final parent are
   correct.
4. **Fast-response validation**: unicast latency changes as intended, multicast
   behavior does not, and no duplicate response occurs.
5. **Runner validation**: every skip, failure, and success classification is
   exercised with a controlled scenario.
6. **Matrix smoke tests**: single deterministic stock, multicast, unicast, and
   fast-response runs for two, three, and four routers.
7. **Repeated campaigns**: small repeated batches before full experiment runs.
8. **Hardware comparison**: matched topology/configuration comparisons of target
   accuracy, success rate, response latency, attach time, outage, topology repair,
   and failure classification.

Each stage is a gate. Do not expand topology size or campaign count while a
lower-level deterministic test remains unexplained.

### Phase 12: Reproducibility and documentation

Each result bundle should include:

- scenario YAML;
- sampled node-state CSV;
- preferred-parent event CSV;
- summary JSON;
- OTNS node logs and replay;
- `ParentRank` data when enabled;
- source and patch revisions;
- build configuration and binary hashes;
- random seed;
- a provenance manifest and short README.

Document clean build commands, scenario commands, artifact layout, timing-source
policy, and known hardware/simulation differences.

## Decision gates

### Gate 1: OpenThread base revision

Prefer the ESP-IDF OpenThread revision if it runs under RFSIM without extensive
compatibility work. Otherwise port to OTNS's current revision and record the
version difference.

### Gate 2: Controller equivalence

Start with the small native controller. If comparisons show that ESPHome's retry,
timeout, or event-ordering behavior materially affects outcomes, extract a
platform-neutral state machine shared by the ESPHome and OTNS adapters as a later
project. Do not begin with that larger refactor.

### Gate 3: Static experiments before mobility

Do not add mobility scenarios until the static selected-parent protocol path is
deterministic and agrees with hardware at the semantic event level.

## Main risks and mitigations

- **Unknown vendored OpenThread revision:** recover it from ESP-IDF 5.5.4 before
  porting and record it explicitly.
- **Patch coupling to MLE internals:** port semantic changes in small commits and
  validate each transition rather than replaying layout-sensitive substitutions.
- **Callback reentrancy:** defer controller work through the native tasklet or
  mainloop instead of changing attacher state inside receive callbacks.
- **Stale selected-parent state:** clear target and candidate state on every
  terminal path and test ordinary attach after failure.
- **`ParentRank` overlap:** preserve instrumentation independently and reapply it
  only after the functional port passes.
- **Simulated versus RTOS time:** use OpenThread/platform simulated timers in the
  native controller and record timer semantics.
- **Router executable scope:** OTNS's FTD executable selection may affect all FTD
  family nodes; scenarios must make this explicit.
- **Fast-path regressions:** gate the behavior at build time and regression-test
  multicast response behavior.
- **Coarse parent polling:** use OpenThread events for protocol latency and polling
  only for state confirmation.
- **Radio/platform differences:** describe results as source-level protocol
  equivalence, not full firmware or hardware equivalence.

## Recommended implementation sequence

1. Freeze the hardware behavior and produce canonical diffs.
2. Recover and record OpenThread provenance.
3. Test the ESP-IDF OpenThread revision with native RFSIM.
4. Select the OpenThread base revision.
5. Preserve `ParentRank` independently.
6. Port the minimal selected-parent bridge and multicast path.
7. Add and validate the native CLI controller.
8. Add and validate unicast Parent Requests.
9. Add and validate fast unicast Parent Responses.
10. Produce and fingerprint the four binary profiles.
11. Add deterministic two-router OTNS-MAPS scenarios.
12. Add event-level timing and classification.
13. Expand to three and four routers.
14. Run repeated campaigns and matched hardware comparisons.
15. Consider shared state-machine extraction only if evidence requires it.
16. Add mobility experiments after static equivalence is established.

## Definition of done

The initial integration is complete when:

- clean builds reproducibly produce the four native binary profiles;
- selected-parent multicast and unicast operations reach the requested router in
  deterministic OTNS tests;
- fast-response routers alter only the intended unicast response path;
- stock behavior remains unchanged when experimental features are absent;
- two-, three-, and four-router scenarios run with complete provenance;
- protocol event timing uses documented, comparable interval definitions;
- failure and skip cases are classified explicitly;
- matched hardware and simulation results can be compared without implying
  cycle-accurate or radio-level equivalence.
