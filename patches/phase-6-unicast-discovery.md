# Phase 6 unicast discovery validation

## Result

Phase 6 is complete. The unicast path implemented by the Phase 4 core patch and
exposed by the Phase 5 controller behaves as targeted unicast in OTNS/RFSIM.
No additional source patch was required.

Validation covered:

- three repeated directed two-router switches;
- one three-router unicast packet capture with a surviving non-target router;
- one matched three-router multicast control capture;
- target Parent Response matching;
- direct Child ID Request continuation;
- final-parent identity and terminal cleanup.

## Repeated two-router tests

OTNS seeds `2601`, `2602`, and `2603` used the same procedure:

1. two routers settled for 300 simulated seconds;
2. the MED attached for 5 simulated seconds;
3. the non-current router was selected by extended address;
4. `prefparent switch <target> unicast` was accepted;
5. the initial parent was removed immediately;
6. the MED was observed for up to 360 simulated seconds.

All three runs emitted target response, Child ID Request, and success events.
All ended with the requested router as parent, the MED in child state, and core
activity cleared. Target attachment was observed within the first one-second
polling interval in every run.

## Three-router packet validation

OTNS seed `2604` used three routers so that one non-target router remained after
the initial parent was removed.

Node identities:

```text
MED:                  be:5a:a2:9c:ea:b6:de:2b
selected target:      e6:e4:93:74:19:23:56:66
surviving non-target: 6a:f8:a6:c5:61:41:b0:ef
```

The selected-parent exchange began at simulation time 305 s. TShark reported:

| Frame | Time (s) | Source EUI-64 | Destination EUI-64 | IPv6 destination | Correlated event |
| ---: | ---: | --- | --- | --- | --- |
| 140 | 305.000488 | `be:5a:a2:9c:ea:b6:de:2b` | `e6:e4:93:74:19:23:56:66` | `fe80::e4e4:9374:1923:5666` | Parent Request |
| 142 | 305.490288 | `e6:e4:93:74:19:23:56:66` | `be:5a:a2:9c:ea:b6:de:2b` | MED link-local | target Parent Response |
| 144 | 305.496184 | `be:5a:a2:9c:ea:b6:de:2b` | `e6:e4:93:74:19:23:56:66` | target link-local | Child ID Request |
| 146 | 305.502240 | `e6:e4:93:74:19:23:56:66` | `be:5a:a2:9c:ea:b6:de:2b` | MED link-local | Child ID Response |

The encrypted command payload was not decoded by TShark. Frame roles are
correlated from direction, timing, and the controller's event sequence. The
address evidence itself does not depend on payload decryption.

The Parent Request's MAC destination is exactly the target EUI-64. Its IPv6
destination is the target's derived link-local address. It is neither MAC
broadcast nor an IPv6 multicast address.

No frame from the surviving non-target router appeared in the selected-parent
exchange window from frame 140 through frame 146. The controller accepted only
the selected target response and reported the same target as the final parent.

Unicast capture SHA-256:

```text
0b3b1f982a9cf538ed8db2c0f87fefe0dea37013e7eaf7f6b8b3904948caaf20
```

The scratch capture contained 165 packets and covered 305.627680 simulated
seconds. It is fingerprinted for audit but not committed; durable campaign
artifacts are produced in Phase 12.

## Multicast regression control

OTNS seed `2605` repeated the directed procedure with multicast mode and three
routers. The switch succeeded within the first one-second observation interval.

The Parent Request was frame 156 at simulation time 305.003088 s:

```text
source EUI-64: 36:9e:ac:ee:a9:5d:b7:3d
MAC destination: 0xffff
IPv6 destination: ff02::2
```

This confirms that enabling and exercising unicast mode did not replace or
alter the multicast Parent Request path.

Multicast control capture SHA-256:

```text
001ea80ff8ff95671d8dd1509f0bd62d49a6cc0a30a4deea541e06b8436cb676
```

## Exit assessment

The Phase 6 exit criterion is met:

- Parent Request is addressed only to the selected router in unicast mode;
- a surviving non-target router does not answer the exchange;
- target response is matched and captured;
- Child ID Request uses the selected candidate;
- final parent equals the requested router;
- three deterministic two-router runs pass;
- multicast remains broadcast/`ff02::2`.

Phase 7 can now compare stock delayed Parent Responses with the fast unicast
response variant.
