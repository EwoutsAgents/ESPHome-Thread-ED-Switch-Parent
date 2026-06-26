# Unicast Parent Response fast path

This patch adds an experimental router-side fast path for MLE Parent Requests
that arrive as IPv6 unicast.

Target source:

- ESP-IDF `5.5.4`
- bundled OpenThread core under
  `framework-espidf/components/openthread/openthread`
- patched file: `src/core/thread/mle_ftd.cpp`

Behavior:

- Default behavior is unchanged.
- When
  `OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE=1`,
  `Mle::HandleParentRequest()` skips the randomized Parent Response delay for
  IPv6-unicast Parent Requests and schedules the Parent Response with zero
  delay.
- Multicast Parent Requests keep the stock randomized delay path.

Why the check is IPv6-only:

- `HandleParentRequest()` receives `RxInfo`, which carries `Ip6::MessageInfo`.
- That exposes whether the IPv6 destination was multicast, but not the
  original IEEE 802.15.4 destination address.
- So this minimal patch can distinguish IPv6 unicast from IPv6 multicast
  without deeper receive-path plumbing, but it does not prove MAC-layer
  unicast inside the handler itself.

Risk notes:

- This is a non-standard optimization and should stay behind an experimental
  compile-time flag.
- It may change parent-discovery response timing and responder collision
  behavior relative to stock Thread expectations.
