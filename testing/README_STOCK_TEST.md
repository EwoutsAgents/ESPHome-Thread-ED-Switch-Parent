# Stock testing methods

The stock test is intended to measure natural OpenThread parent-switch behavior without using the preferred-parent switching mechanism. The test is fully automatic and opportunistic: rather than forcing a specific router to be the child’s initial parent, the runner observes which router the child naturally attaches to and only proceeds when the resulting topology is suitable for a clean reference measurement.

Each variation follows the same setup until the requested router set has been flashed. Variations differ only in the total number of router-capable ESP32-C6 boards included in the run. The `n_routers` setting is the total router count and does not include the child. Routers are flashed in order using `stock_router_<n>.yaml`, where `<n>` starts at `1` and increases sequentially until the requested total router count is reached. The current maximum is four routers total. For a switch to occur, at least 2 routers must be present.

A run is considered suitable for the timed parent-removal phase only if, after the fixed router-settling delay and the child's initial attach, the runner can reliably identify the child’s current parent and map that parent to one of the configured router devices. If either of those pre-removal checks fails, the run is skipped using an explicit classification. If the detected parent is also the current Thread leader, the run continues but retains the explicit `SKIP_PARENT_IS_LEADER` label in the manifest and later analysis. Broader topology effects, such as router reattachment, downgrading, RLOC16 changes, or other topology repair during the measurement window, are handled during post-run outcome classification rather than as pre-removal skip gates.

1. Erase firmware and non-volatile storage on all connected ESP32-C6 boards, including unused boards, using `esptool.py --chip esp32c6 --port <port> erase_flash`.
2. Put all ESP32-C6 boards, including unused ones, in a predictable state by flashing `empty.yaml` to them.
3. Start the `IEEE 802.15.4` sniffer recording.
4. Wait `sniffer_lead_in_seconds` seconds.
5. Flash the requested total number of router-capable ESP32-C6 boards using `stock_router_<n>.yaml`, where `<n>` starts at `1` and increases sequentially until the configured `n_routers` total is reached.
6. Wait `router_settling_seconds` seconds before flashing the child. This delay gives the router-capable devices time to form a stable Thread topology before the child performs its initial stock attach. The runner does not extend this delay dynamically; instead, it validates the observed topology after the delay and skips or classifies the run separately if the topology is unsuitable.
7. Flash the child ESP32-C6 with `stock_child.yaml`.
8. Wait `child_attach_seconds` seconds to allow the child to attach naturally to one of the available routers.
9. Determine the child’s current parent from the child log, router logs, or the captured MLE attach sequence.
10. Apply the pre-removal eligibility gate. The run cannot continue only if either of the following classifications applies. Classify the run explicitly using one of these skip reasons:

    * `SKIP_NO_CHILD_PARENT`: the runner could not detect the child’s current parent from the available evidence. This does not necessarily prove that the child had no parent; it means no current parent could be reliably determined.
    * `SKIP_PARENT_NOT_MAPPED_TO_DEVICE`: the child’s parent was detected, but its extended address could not be mapped to one of the configured router devices in the test setup.
11. If the detected child parent is also the current Thread leader, keep the `SKIP_PARENT_IS_LEADER` label on the run, but continue the test.
12. Flash the child’s detected current parent ESP32-C6 board with `empty.yaml`.
13. Wait `after_parent_removed_seconds` seconds while continuing to record packets and device logs.
14. Stop the `IEEE 802.15.4` sniffer recording.
15. Copy the resulting sniffer `.pcapng` into the current run folder under `testing/logs/stock/<timestamp>/` as `stock_sniffer_<timestamp>.pcapng`.
16. Classify the run outcome. A valid stock reference switch requires the target child to lose its current parent and complete a new MLE attach to one of the remaining candidate parents. Runs in which router-capable devices reattach, downgrade, change RLOC16, elect a new leader unexpectedly, or otherwise repair the router topology during the measurement window should be classified separately during analysis rather than treated as clean stock parent-switch measurements. Runs labeled `SKIP_PARENT_IS_LEADER` should keep that label even though they continue through the timed removal phase.
