# Stock testing methods

The stock test is intended to measure natural OpenThread parent-switch behavior without using the preferred-parent switching mechanism. The test is fully automatic and opportunistic: rather than forcing a specific router to be the child’s initial parent, the runner observes which router the child naturally attaches to and only proceeds when the resulting topology is suitable for a clean reference measurement.

Each variation follows the same setup until the requested router set has been flashed. Variations differ only in the total number of router-capable ESP32-C6 boards included in the run. The `n_routers` setting is the total router count and does not include the child. Routers are flashed in order using `stock_router_<n>.yaml`, where `<n>` starts at `1` and increases sequentially until the requested total router count is reached. The current maximum is four routers total.

A run is considered suitable for measurement only if, after the fixed router-settling delay and the child's initial attach, the child’s current parent can be removed without also removing the network leader or a router that is required as a transit/nexthop between the remaining candidate parents. If those preconditions are not met, the run is skipped or classified separately instead of being treated as a valid stock parent-switch measurement.

1. Erase firmware and non-volatile storage on all connected ESP32-C6 boards, including unused boards, using `esptool.py --chip esp32c6 --port <port> erase_flash`.
2. Put all ESP32-C6 boards, including unused ones, in a predictable state by flashing `empty.yaml` to them.
3. Start the `IEEE 802.15.4` sniffer recording.
4. Wait `sniffer_lead_in_seconds` seconds.
5. Flash the requested total number of router-capable ESP32-C6 boards using `stock_router_<n>.yaml`, where `<n>` starts at `1` and increases sequentially until the configured `n_routers` total is reached.
6. Wait `router_settling_seconds` seconds before flashing the child. This delay gives the router-capable devices time to form a stable Thread topology before the child performs its initial stock attach. The runner does not extend this delay dynamically; instead, it validates the observed topology after the delay and skips or classifies the run separately if the topology is unsuitable.
7. Flash the child ESP32-C6 with `stock_child.yaml`.
8. Wait for the child to attach naturally to one of the available routers.
9. Determine the child’s current parent from the child log, router logs, or the captured MLE attach sequence.
10. Determine whether the child’s current parent is safe to remove. The parent is safe to remove only if:

    * it is not the current Thread leader;
    * it is not required as a transit/nexthop between the remaining routers;
    * the remaining routers are stable and available as candidate parents;
    * no router-capable device has recently sent MLE Parent Request or Child ID Request messages;
    * no recent router RLOC16, leader, or route-table changes have been observed.
11. If the child’s current parent is not safe to remove, do not remove it. Mark the run with an explicit skip or invalid classification, such as `SKIP_PARENT_IS_LEADER`, `SKIP_PARENT_IS_TRANSIT`, `SKIP_TOPOLOGY_UNSTABLE`, or `SKIP_NO_CHILD_PARENT`.
12. If the child’s current parent is safe to remove, flash that parent’s ESP32-C6 board with `empty.yaml`.
13. Wait `after_parent_removed_seconds` seconds while continuing to record packets and device logs.
14. Stop the `IEEE 802.15.4` sniffer recording.
15. Copy the resulting sniffer `.pcapng` into the current run folder under `testing/logs/stock/<timestamp>/` as `stock_sniffer_<timestamp>.pcapng`.
16. Classify the run outcome. A valid stock reference switch requires the target child to lose its current parent and complete a new MLE attach to one of the remaining stable candidate parents, without router-capable devices reattaching, downgrading, changing RLOC16, or otherwise repairing the router topology during the measurement window.
