# Phase 7 fast Parent Response validation

## Result

Phase 7 is complete. The FTD fast path is implemented behind
`OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE`, which
defaults to `0`. When enabled, an IPv6-unicast Parent Request is answered
immediately and the handler exits before scheduling the ordinary randomized
response. The multicast path is unchanged.

The native patch is incremental and must be applied after the Phase 4 core and
Phase 5 controller patches:

```text
patches/otns/fast-unicast-parent-response.patch
SHA-256: 783990f9ba10968ff5bbd12eb71465409af8f435873e5ec6168748cb3cda8a29
```

## Build profiles

Two FTD validation profiles were compiled from the same Track A source tree so
that the fast-path setting was the only behavioral difference:

- ordinary response: `OPENTHREAD_CONFIG_PARENT_SEARCH_ENABLE=0`;
- fast response: the same flag plus
  `OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE=1`.

Both builds completed with warnings treated as errors. Their validation
fingerprints were:

```text
ordinary FTD: 88afb87e3bc87ac7db55fc5056e34b19bc8fd011013f85d0c7a9f3e0dfc36d3e
fast FTD:     295b0249ec3ba7c2daa7dcf32c261bb1a1c7836b5a39ff286cf99bd6c7dd5205
```

These are Phase 7 comparison binaries, not the final Phase 8 artifact matrix.
In particular, the final stock profile must be built from an unpatched isolated
source tree.

## Matched unicast timing

Seeds `2701` through `2705` used the same two-router procedure and identities in
both profiles. Routers settled for 300 simulated seconds, the MED attached for
5 seconds, the other router was selected, and the initial parent was removed
immediately after the unicast switch command.

| Profile | Runs | Mean (ms) | Median (ms) | Minimum (ms) | Maximum (ms) |
| --- | ---: | ---: | ---: | ---: | ---: |
| ordinary response | 5 | 272.240 | 251.160 | 48.760 | 478.440 |
| fast response | 5 | 4.072 | 4.136 | 3.816 | 4.456 |

All ten runs attached to the selected target. In every capture, exactly two MLE
frames traveled from target to child during the one-second exchange window: the
correlated Parent Response and Child ID Response. No delayed duplicate Parent
Response followed the immediate response.

The encrypted MLE command byte was not decoded. Packet roles were correlated
from direction, timing, and the known selected-parent exchange order, as in
Phase 6.

## Multicast regression control

Seeds `2711`, `2712`, and `2713` repeated the switch in multicast mode with both
FTD profiles. The response delays were respectively `302.696`, `437.656`, and
`133.376` ms in both profiles. For every matched seed, the complete stock and
fast-profile PCAP files had identical SHA-256 hashes. This is stronger than a
statistical comparison: the compile-time fast path did not alter any captured
multicast behavior in these controls.

All six multicast runs attached to the selected target and showed no duplicate
target response.

## Exit assessment

The Phase 7 exit criterion is met:

- unicast Parent Response latency changes from randomized delay to immediate
  simulator/radio scheduling latency;
- every unicast and multicast switch reaches the requested target;
- the immediate path does not also schedule a delayed duplicate;
- multicast packet behavior is unchanged in matched deterministic runs;
- the feature is disabled by default and isolated by a compile-time setting.

Phase 8 can now produce the four isolated, reproducibly fingerprinted native
binary profiles.
