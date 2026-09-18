# Firmware variants

- **Stock:** ordinary multicast OpenThread parent search after removal of the current parent.
- **Ucast:** proactive selected-parent handoff using an explicit unicast Parent Request; the original parent remains active.
- **Fast Attach:** stock-like parent removal with OpenThread PR #13121 semantics, including `F=1`, reduced randomized response delay, and immediate continuation on the first acceptable LQ3 Parent Response.
- **Fast Attach Ucast 1:** directed unicast `F=1` Parent Request, selected-target acceptance without the multicast LQ3 gate, and a fixed 1 ms responder delay.
- **Stock Low Power:** stock parent-removal procedure with routers 1 and 2 at 0 dBm and additional routers at -15 dBm. Only runs switching from one 0 dBm router to the other are accepted.

The discontinued/planned `fast-attach-ucast-32` variant is not included.
