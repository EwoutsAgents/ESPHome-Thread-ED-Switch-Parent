# Ucast/mcast testing methods

The unicast, unicast-fastpr, and multicast tests are intended to measure directed OpenThread parent-switch behavior after the child is instructed to switch to a known target parent. Unlike the stock test, this method does not rely only on natural parent selection after parent removal. The runner creates a router topology, observes the child’s naturally selected current parent, selects a random eligible target parent from the remaining configured routers, instructs the child to switch to the selected target parent, and then immediately removes the child’s initial parent.

The protocol applies to the unicast, unicast-fastpr, and multicast variants. The child uses unicast Parent Requests in both unicast variants. The `ucast_fastpr` variant additionally flashes the routers with `fastpr_router_<n>.yaml`, enabling the router-side fast unicast Parent Response patch. The multicast variant uses `mcast_child.yaml`, the main difference being that it sends Parent Requests using multicast instead of unicast by setting `parent_request_unicast: false`.

Use the following child firmware and log directory pattern for each variant:

| Variant         | Child firmware            | Router firmware prefix | Batch log directory pattern                                             | Per-run directory pattern          |
| --------------- | ------------------------- | ---------------------- | ----------------------------------------------------------------------- | ---------------------------------- |
| Unicast         | `ucast_child.yaml`        | `stock_router_<n>`     | `testing/logs/ucast-<n_routers>router-<runs>runs-<timestamp>/`          | `<run_timestamp>-run<run_number>/` |
| Unicast fastpr  | `ucast_fastpr_child.yaml` | `fastpr_router_<n>`    | `testing/logs/ucast_fastpr-<n_routers>router-<runs>runs-<timestamp>/`   | `<run_timestamp>-run<run_number>/` |
| Multicast       | `mcast_child.yaml`        | `stock_router_<n>`     | `testing/logs/mcast-<n_routers>router-<runs>runs-<timestamp>/`          | `<run_timestamp>-run<run_number>/` |

Each variation follows the same setup until the requested router set has been flashed. Variations differ only in the total number of router-capable ESP32-C6 boards included in the run and, for `ucast_fastpr`, in the router firmware prefix. The `n_routers` setting is the total router count and does not include the child. Routers are flashed in order using the variant-appropriate router firmware prefix, where `<n>` starts at `1` and increases sequentially until the requested total router count is reached. The current maximum is four routers total. For a switch to occur, at least two routers must be present.

A run is considered suitable for the timed directed-switch phase only if, after the fixed router-settling delay and the child’s initial attach, the runner can reliably determine the child’s current parent, map that parent to one of the configured router devices, and select a random eligible target parent from the remaining configured routers. The target parent must not be the child’s current parent, and its extended address must be known so that the child can be instructed to switch to it. If the detected current parent is also the current Thread leader, the run continues but retains the explicit `SKIP_PARENT_IS_LEADER` label in the manifest and later analysis. Broader topology effects during the measurement window are handled during post-run outcome classification rather than as pre-switch gates.

1. Erase firmware and non-volatile storage on all connected ESP32-C6 boards, including unused boards, using `esptool.py --chip esp32c6 --port <port> erase_flash`.
2. Put all ESP32-C6 boards, including unused ones, in a predictable state by flashing `empty.yaml` to them.
3. Start the `IEEE 802.15.4` sniffer recording.
4. Wait `sniffer_lead_in_seconds` seconds.
5. Flash the requested total number of router-capable ESP32-C6 boards using `stock_router_<n>.yaml`, where `<n>` starts at `1` and increases sequentially until the configured `n_routers` total is reached.
6. Wait `router_settling_seconds` seconds before flashing the child. This delay gives the router-capable devices time to form a stable Thread topology before the child performs its initial attach.
7. Flash the child ESP32-C6 with the child firmware for the selected variant.
8. Wait `child_attach_seconds` seconds to allow the child to attach naturally to one of the available routers.
9. Determine the child’s current parent from the child log, router logs, or the captured MLE attach sequence.
10. Determine the extended addresses of the configured routers from their logs and randomly select the target parent from those whose extended address is known and does not match the child’s current parent.
11. Apply the pre-switch eligibility gate. The directed switch can continue only if the required parent/target evidence exists. Use the following skip classifications when it does not:

    * `SKIP_NO_CHILD_PARENT`: the runner could not detect the child’s current parent from the available evidence. This does not necessarily prove that the child had no parent; it means no current parent could be reliably determined.
    * `SKIP_PARENT_NOT_MAPPED_TO_DEVICE`: the child’s current parent was detected, but its extended address could not be mapped to one of the configured router devices in the test setup.
    * `SKIP_NO_ELIGIBLE_TARGET_PARENT`: no configured router with a known extended address remains after excluding the child’s current parent.
12. If the detected child parent is also the current Thread leader, keep the `SKIP_PARENT_IS_LEADER` label on the run, but continue the test.
13. Instruct the child to change its parent to the randomly selected target parent using the selected target router’s observed extended address.
14. Immediately after the targeted switch command has been sent, flash the child’s initial parent ESP32-C6 board with `empty.yaml`.
15. Wait `after_parent_removed_seconds` seconds while continuing to record packets and device logs.
16. Stop the `IEEE 802.15.4` sniffer recording.
17. Copy the resulting sniffer `.pcapng` into the current run folder for the selected variant as `<variant>_sniffer_<timestamp>.pcapng`.
18. Classify the run outcome. A valid directed parent-switch measurement requires the target child to lose its initial parent and complete a new MLE attach to the randomly selected target parent. Runs in which the child does not switch to the selected target parent, router-capable devices reattach, downgrade, change RLOC16, elect a new leader unexpectedly, or otherwise repair the router topology during the measurement window should be classified separately during analysis rather than treated as clean directed parent-switch measurements. Runs labeled `SKIP_PARENT_IS_LEADER` should keep that label even though they continue through the timed switch/removal phase.
