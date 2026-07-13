# Phase 5 native preferred-parent CLI controller

## Result

Phase 5 is complete. The native OpenThread CLI now provides a deferred
preferred-parent controller with stable machine-readable events.

The patch is
[preferred-parent-cli-controller.patch](otns/preferred-parent-cli-controller.patch)
and applies after the Phase 4
[selected-parent-core.patch](otns/selected-parent-core.patch).

Controller patch SHA-256:

```text
6ef066387cbf2f37c9a91996aa4306c947e67020cbaf36c26ce656d2a8033720
```

## Commands

```text
prefparent switch <extaddr> multicast
prefparent switch <extaddr> unicast
prefparent status
prefparent clear
```

Extended addresses may be compact hexadecimal or colon/hyphen separated. The
controller rejects malformed addresses, missing arguments, unknown modes, and
a second operation while busy.

`unicast` is parsed and connected to the existing core entry point. Phase 6
will validate its addressing and on-air behavior; it is not claimed as complete
by this phase.

## Deferred processing

OpenThread callbacks do not modify the attacher or print events directly. They
only copy bounded data into pending controller fields. The CLI application's
mainloop calls `otSelectedParentCliProcess()` after `otTaskletsProcess()` and
`otSysProcessDrivers()` return.

The deferred processor:

1. emits queued Parent Request and attacher-state events;
2. matches a Parent Response to the selected extended address;
3. calls selected-parent continuation from mainloop context;
4. observes the current parent through `otThreadGetParentInfo()`;
5. emits success only when the current parent equals the target;
6. clears core operation state on success, timeout, or reset.

The 16-second controller timeout uses `otPlatAlarmMilliGetNow()`, so OTNS
simulation time—not Python or host wall time—controls it. Operation generation
numbers allow stale queued events to be identified.

## Machine-readable events

The directed run produced:

```text
PREFPARENT event=requested generation=2 target=<target> mode=multicast
PREFPARENT event=parent_request_started generation=2
PREFPARENT event=target_response generation=2 target=<target> rloc16=<rloc16> rssi=<rssi>
PREFPARENT event=child_id_request_started generation=2 target=<target>
PREFPARENT event=succeeded generation=2 parent=<target>
```

Failure and control events include:

```text
PREFPARENT event=failed generation=<n> reason=timeout error=ResponseTimeout
PREFPARENT event=cleared
PREFPARENT event=status state=<state> generation=<n> active=<0|1> mode=<mode> target=<target>
```

## CLI validation

Live OTNS tests covered:

- idle status;
- valid compact extended address;
- valid colon-separated extended address;
- invalid length and hexadecimal input;
- missing arguments;
- unknown mode;
- status during an active operation;
- second command while busy (`Busy`);
- explicit clear and idle status;
- status after success;
- timeout failure;
- fresh operation after timeout cleanup.

## Directed multicast validation

Using OTNS seed `2405`:

1. two routers settled for 300 simulated seconds;
2. the MED attached for 5 simulated seconds to Router A;
3. Router B's extended address was supplied to `prefparent switch ... multicast`;
4. Router A was deleted immediately after the command returned `Done`;
5. the deferred event sequence completed;
6. the MED reported Router B as its parent and remained in `child` state.

Target attachment was observed during the first one-second polling interval.
The final status was `succeeded`, generation 2, with core `active=0`.

## Timeout and cleanup validation

Using OTNS seed `2504`, target `ffffffffffffffff` produced no matching Parent
Response. After 16 simulated seconds the controller emitted a timeout failure
and status reported `active=0`. A valid generation 2 operation was then accepted,
reported active, and returned to idle after `prefparent clear`.

## Build fingerprints

Both binaries compiled with warnings treated as errors and PPS disabled:

```text
ot-cli-mtd SHA-256: edb8bc920eb885bbaf37df5f22438220246938d29cf35d874901725ea5057d7a
ot-cli-ftd SHA-256: 83aaa56cbd58eab147a7f5a46d099eec630671b24dda4cb0a173d8cb696337e6
```

These remain development fingerprints. Phase 8 will create canonical binary
profiles and manifests.
