# Fast Attach Unicast 32 test

`fast-attach-ucast-32` is an isolated proactive directed-handoff experiment. It combines the existing `ucast` selected-parent controller with the Fast Attach behavior backported from OpenThread PR #13121 at head `61034b8a7e776695d1afe30338b3f36d24733127`.

The child attaches normally, the runner selects a router other than the current parent, and the original parent remains online. The selected target receives an IPv6-unicast Parent Request with Scan Mask `F=1`. A Fast Attach response that was genuinely received as unicast uses an effective responder count of one, giving a maximum randomized response delay of 32 ms. Multicast Fast Attach still uses the actual active-router count, and Parent Requests without `F=1` retain normal timing.

The combined controller arms OpenThread's existing one-shot Fast Attach state internally when `otThreadPreferredParentStart()` begins. This is necessary because a proactive selected-parent operation starts while the device is still a child, whereas `otThreadSetFastAttachEnabled()` intentionally only accepts Disabled or Detached. The public API restriction is unchanged. A successful Child ID Response clears the flag through the PR #13121 one-shot path. Failed, timed-out, and cancelled selected-parent operations clear it in the controller's common unsuccessful-terminal path; retries do not clear it. The terminal cleanup emits `FAST_ATTACH_UCAST_32 terminal_state=N fast_attach_armed=0` when it disarms a pending attempt.

Receiver-side unicast detection uses the local IPv6 destination in `RxInfo::mMessageInfo.GetSockAddr()`, not selected-parent state. Routers emit:

```text
FAST_ATTACH_UCAST_32 unicast=1 active_routers=N effective_routers=1 max_delay_ms=32 delay_ms=X
```

Run a two-router test with:

```bash
cd testing
./run_fast_attach_ucast_32_test.sh --config fast_attach_ucast_32_test_devices_2routers.toml
```

Build and package isolation is rooted at `testing/.platformio-core/fast-attach-ucast-32/`. Firmware package groups (`child`, `routers`, and `utility`) are separate below that root. The manifest records both paths, the three dedicated patch hashes, PR head, vendored OpenThread revision, compile flags, target-selection decision, device logs, and PCAP path.

Protocol validation requires all of the following: the chosen target in the runner manifest; child `FAST_ATTACH_UCAST_32` requested, Parent Request, target-response, Child ID Request, and succeeded events; router diagnostic evidence with `unicast=1`, `effective_routers=1`, `max_delay_ms=32`, and `delay_ms` in `0..32`; and PCAP confirmation that the Parent Request was IPv6 unicast with Scan Mask `F=1` and was followed by the target response and Child ID exchange.

The backport targets vendored OpenThread revision `a12ff0d0f54fd41954b45047fcdd08f302731c5f`. Its Fast Attach portion retains the documented adjustments of the existing isolated `fast-attach` variant. For the directed operation, the preferred-parent controller accepts the selected target's otherwise-valid Parent Response regardless of LQ1/LQ2/LQ3 and immediately continues with Child ID Request. This combined variant adds selected-parent arming, actual-unicast effective responder selection, terminal-state cleanup, and diagnostic logging; upstream LQ3 selection remains unchanged outside the directed preferred-parent path.
