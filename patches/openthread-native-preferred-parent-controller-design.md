# OpenThread-owned preferred-parent controller design

## Status and scope

This document replaces the split ESPHome/native-CLI controller architecture
with one controller owned by OpenThread. It targets OpenThread commit
`a12ff0d0f54fd41954b45047fcdd08f302731c5f`, which is both the ESP-IDF 5.5.4
vendored revision used by the hardware firmware and the selected Track A base
used by native OTNS/RFSIM builds.

The ESP-IDF and native RFSIM integrations therefore use one functional patch
without revision-specific controller forks. ESPHome and the OTNS CLI only
translate configuration/commands, call the public API, and display status or
events.

## Compile-time isolation

The preferred-parent MTD controller is guarded by:

```text
OPENTHREAD_CONFIG_EXPERIMENTAL_PREFERRED_PARENT_ENABLE
```

The default is `0`. When disabled, the API implementation and all preferred-
parent state, MLE branches, strings, and callbacks are absent from the build.

The independent router fast-response behavior remains guarded by:

```text
OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE
```

The two options are not coupled. `ParentRank` instrumentation remains a third,
separate patch and is not part of either functional change.

The isolated build profiles are:

- stock MTD: PPS disabled, preferred-parent disabled, FastPR disabled;
- preferred-parent MTD: PPS disabled, preferred-parent enabled, runtime
  multicast/unicast mode;
- stock FTD: preferred-parent disabled, FastPR disabled;
- FastPR FTD: preferred-parent disabled, FastPR enabled.

## Public experimental API

The API lives in `include/openthread/preferred_parent.h`. Its module prefix is
`otThreadPreferredParent`, matching OpenThread's `otThread` API namespace while
keeping the experimental operation distinct from ordinary parent search.

Conceptual declarations:

```c
typedef enum otThreadPreferredParentMode { ... } otThreadPreferredParentMode;
typedef enum otThreadPreferredParentState { ... } otThreadPreferredParentState;
typedef enum otThreadPreferredParentResult { ... } otThreadPreferredParentResult;
typedef enum otThreadPreferredParentEvent { ... } otThreadPreferredParentEvent;

typedef struct otThreadPreferredParentConfig {
    otExtAddress                 mExtAddress;
    otThreadPreferredParentMode mMode;
    uint8_t                      mMaxAttempts;
    uint32_t                     mRetryInterval;
    uint32_t                     mAttachTimeout;
} otThreadPreferredParentConfig;

typedef struct otThreadPreferredParentStatus { ... } otThreadPreferredParentStatus;
typedef struct otThreadPreferredParentEventInfo { ... } otThreadPreferredParentEventInfo;
typedef void (*otThreadPreferredParentCallback)(const otThreadPreferredParentEventInfo *, void *);

otError otThreadPreferredParentSetCallback(otInstance *, otThreadPreferredParentCallback, void *);
otError otThreadPreferredParentStart(otInstance *, const otThreadPreferredParentConfig *);
otError otThreadPreferredParentCancel(otInstance *);
otError otThreadPreferredParentClear(otInstance *);
void otThreadPreferredParentGetStatus(otInstance *, otThreadPreferredParentStatus *);
```

### Contract

- The feature is available only in MTD builds compiled with the option enabled.
- `Start` is allowed only while the Thread role is child.
- The target is an eight-byte `otExtAddress` in OpenThread/network display
  order. Text parsing and separators are adapter concerns.
- All-zero and all-`ff` targets, unknown modes, zero attempts, zero retry
  interval, and zero attach timeout return `OT_ERROR_INVALID_ARGS`.
- Starting while an operation is active returns `OT_ERROR_BUSY` without
  changing the existing operation.
- Starting from a non-child role returns `OT_ERROR_INVALID_STATE`.
- Timeout fields are milliseconds. Timer comparisons use OpenThread
  `TimerMilli` arithmetic.
- `Cancel` is valid only for an active operation. It stops the controller,
  restores temporary receive settings, cancels only controller-owned attach
  work, clears candidates, and enters terminal `cancelled` state.
- `Clear` is rejected with `OT_ERROR_BUSY` while active. In a terminal state it
  clears retained result/diagnostics and returns to `idle`. In `idle` it is
  idempotent.
- Terminal state and the last result remain readable until `Clear` or a new
  successful `Start` initialization.
- The callback runs synchronously from OpenThread tasklet/timer processing.
  Callers must not call `Start`, `Cancel`, or `Clear` reentrantly from it. They
  may query status and should defer mutating commands to their own main loop.
- The callback is observational. Correct controller progress never depends on
  an adapter callback or polling loop.

## State machine

Public states are:

```text
idle
starting_discovery
waiting_parent_request
waiting_target_response
continuing_selected_attach
waiting_child_id_response
succeeded
failed
timed_out
cancelled
```

The configured target is part of an accepted operation, so a separate public
`target_configured` state is unnecessary. Configuration is copied atomically
by `Start` before entering `starting_discovery`.

Transitions:

```text
idle/terminal --Start--> starting_discovery
starting_discovery --> waiting_parent_request
waiting_parent_request --Parent Request sent--> waiting_target_response
waiting_target_response --valid target Parent Response-->
    continuing_selected_attach --> waiting_child_id_response
waiting_target_response --attempt timeout with attempts left-->
    starting_discovery
waiting_target_response --attempt budget exhausted--> timed_out
waiting_child_id_response --valid target Child ID Response--> succeeded
waiting_child_id_response --attach timeout with attempts left-->
    starting_discovery
waiting_child_id_response --attempt budget exhausted--> timed_out
any active state --protocol/start/send rejection--> failed
any active state --Cancel--> cancelled
any active state --role loss/ordinary detach--> failed
terminal --Clear--> idle
```

`failed` is used for deterministic API, allocation, send, validation-state, or
role failures. `timed_out` is reserved for exhausted response/attach deadlines.
The status result includes a stable reason enum and the last `otError`.

## MLE ownership and protocol behavior

The controller is stored per `otInstance`, inside MLE/Attacher state. No
process-global operation variables are used.

On each attempt OpenThread:

1. initializes and clears the target candidate snapshot;
2. records the generation and attempt number;
3. enters the existing better-parent Parent Request machinery without
   detaching the current parent;
4. sends to `ff02::2` for multicast mode or to the target's link-local address
   for unicast mode;
5. arms the discovery deadline when the Parent Request is actually sent;
6. parses every Parent Response through the ordinary MLE/security path;
7. drops non-target responses from preferred-parent candidate selection;
8. fully populates `mParentCandidate`, then copies the complete candidate into
   an initialized snapshot and marks it valid;
9. directly restores that snapshot and sends Child ID Request without another
   Parent Request;
10. confirms success only after the normal Child ID Response path sets the
    device's parent to the requested extended address.

Challenge/Response, message security, TLV parsing, link validation, neighbor
state checks, and candidate consistency checks remain mandatory. The only
ranking override is that a fully valid explicitly requested target need not be
better than the current parent.

The Child ID Request notification is emitted only after `SendTo()` succeeds.
The success notification is emitted only after the normal Child ID Response is
accepted. The old parent remains installed until OpenThread's existing
successful child transition updates it.

## Timer and retry policy

Defaults preserve the existing experiment configuration:

- maximum attempts: 5;
- target discovery/retry interval: 8,000 ms;
- selected attach timeout: 16,000 ms.

Each attempt has one discovery deadline and, after direct continuation, one
Child ID deadline. There is no ESPHome `millis()` deadline and no CLI platform
alarm deadline. A retry reinitializes all per-attempt candidate and event state
before sending a fresh Parent Request. No retry is scheduled after cancellation,
role loss, or a terminal result.

## Initialization and cleanup invariants

The historical candidate-snapshot defect is fixed as an invariant:

- `ParentCandidate::Init()` and `Clear()` are called for both the live and
  saved candidates in the Attacher constructor;
- the saved-candidate-valid flag is initialized to false;
- the snapshot is copied only after every candidate field has been populated;
- continuation requires the valid flag, Parent Response neighbor state, and
  exact target extended-address match;
- retry, cancel, role change, ordinary attach start, success, failure, timeout,
  and clear deliberately invalidate and clear the snapshot;
- temporary RX-on state is restored exactly once on every exit path.

Ordinary attach paths clear preferred-parent mode before processing responses,
so state cannot leak into later stock attachment.

## Structured event contract

OpenThread emits typed callback events with a generation, attempt, state,
target, mode, reason/error, and event-specific data. The event sequence uses:

```text
requested
parent_request_started
target_response
child_id_request_started
succeeded
failed
timed_out
cancelled
cleared
```

`target_response` includes parent extended address, RLOC16, RSSI, priority, and
link-quality values. Adapters may add platform timestamps when rendering an
event but may not use those timestamps to drive the operation.

## Adapter responsibilities

### ESPHome

ESPHome validates YAML/text, acquires `InstanceLock`, constructs the OpenThread
config, calls `Start`/`Cancel`/`Clear`, and renders callbacks/status. It owns no
candidate, attempt, queue, retry timer, attach deadline, Parent Response
decision, or continuation call. Its `loop()` is limited to optional status/event
presentation and is not required for controller progress.

RLOC16 targeting is removed from the controller API because the operation is
defined by a stable extended address and unicast construction requires it.
The adapter may retain a compatibility setter only if it resolves the RLOC16
to an extended address before `Start`; unresolved values fail locally.

### OTNS CLI

The native CLI parses compact or colon-separated extended addresses and mode,
then calls the same API. `prefparent status`, `cancel`, and `clear` are direct
API wrappers. It renders OpenThread callback events in stable `PREFPARENT`
key/value form. It owns no controller state, pending callback mailbox, timeout,
candidate, parent polling success test, or per-cycle continuation logic.

## Source and patch maintenance

The shared functional patch is developed and tested against `a12ff0d0...` and
applied unchanged to isolated ESP-IDF and native RFSIM source instances. The
ESPHome pre-build hook becomes an idempotent patch applier for that canonical
patch, rather than a second implementation assembled by tolerant regexes.

Patch separation:

1. preferred-parent configuration/API/controller and MLE integration;
2. preferred-parent diagnostic logging, if additional logs are needed;
3. unicast Parent Response FastPR router change;
4. OTNS `ParentRank` instrumentation.

If a later ESP-IDF or OTNS base changes away from `a12ff0d0...`, it receives a
revision-specific mechanical port of the same controller source and API
semantics. No adapter-owned fallback state machine is permitted.

## Validation gates

Tests must cover API input/state behavior; initialization and cleanup on every
terminal path; non-target filtering; multicast/unicast addressing; complete
candidate snapshot population; direct continuation without a second Parent
Request; retry and timeout exhaustion; cancellation; ordinary attach after a
failed operation; and FastPR isolation/no duplicate response.

Native tests precede hardware tests. New hardware output must use a new
`openthread-controller-implementation-*` directory and must never modify
`testing/logs/hardware-baselines/esphome-controller-implementation-20260714-15`.
