# Stock testing methods

The method for testing stock performance is as follows. Each variation follows the same setup until `stock_router_2` is flashed. After that point, the protocol differs only in how many extra routers are added after `stock_router_2`. The extra routers are flashed in order, starting at `stock_router_3.yaml`. The current maximum is four routers total.

1. Erase firmware and non-volatile storage on all connected ESP32-C6 boards, including unused boards, using `esptool.py --chip esp32c6 --port <port> erase_flash`.
2. Put all ESP32-C6 boards, including unused ones, in a predictable state by flashing `empty.yaml` to them.
3. Start the `IEEE 802.15.4` sniffer recording.
4. Wait 5 seconds.
5. Flash the first ESP32-C6 with `stock_router_1.yaml`.
6. Wait 5 seconds.
7. Flash the second ESP32-C6 with `stock_child.yaml`.
8. Wait 10 seconds.
9. Flash the third ESP32-C6 with `stock_router_2.yaml`.
10. Depending on the variation of the run, flash one or more additional ESP32-C6 boards as routers using `stock_router_<n>.yaml`, where `<n>` starts at `3` and increases sequentially until the requested maximum router number is reached.
11. Wait 90 seconds so `stock_router_2` and all additional routers have time to become router-capable before removing `stock_router_1`.
12. Flash the first ESP32-C6 with `empty.yaml`.
13. Wait 180 seconds.
14. Stop the `IEEE 802.15.4` sniffer recording.
15. Copy the resulting sniffer `.pcapng` into the current run folder under `testing/logs/stock/<timestamp>/` as `stock_sniffer_<timestamp>.pcapng`.

# Ucast/mcast testing

The method for parent-switch performance testing is as follows. This protocol applies to both the unicast and multicast variants. Each variation follows the same setup until `stock_router_2` is flashed. After that point, the protocol differs only in how many extra routers are added after `stock_router_2`. The extra routers are flashed in order, starting at `stock_router_3.yaml`. The current maximum is four routers total.

Use the following child firmware and log directory for each variant:

| Variant   | Child firmware      | Log directory                         |
| --------- | ------------------- | ------------------------------------- |
| Unicast   | `ucast_child.yaml`  | `testing/logs/ucast/<timestamp>/`     |
| Multicast | `mcast_child.yaml`  | `testing/logs/mcast/<timestamp>/`     |

1. Erase firmware and non-volatile storage on all connected ESP32-C6 boards, including unused boards, using `esptool.py --chip esp32c6 --port <port> erase_flash`.
2. Put all ESP32-C6 boards, including unused ones, in a predictable state by flashing `empty.yaml` to them.
3. Start the `IEEE 802.15.4` sniffer recording.
4. Wait 5 seconds.
5. Flash the first ESP32-C6 with `stock_router_1.yaml`.
6. Wait 5 seconds.
7. Flash the second ESP32-C6 with the child firmware for the selected variant.
8. Wait 10 seconds.
9. Flash the third ESP32-C6 with `stock_router_2.yaml`.
10. Depending on the variation of the run, flash one or more additional ESP32-C6 boards as routers using `stock_router_<n>.yaml`, where `<n>` starts at `3` and increases sequentially until the requested maximum router number is reached.
11. Wait 90 seconds so `stock_router_2` and all additional routers have time to become router-capable before removing `stock_router_1`.
12. Read the extended address of `stock_router_2` from the `stock_router_2.yaml` logs.
13. Flash the first ESP32-C6 with `empty.yaml` to remove the old parent before the child is instructed to switch.
14. Wait 5 seconds so `stock_router_1` can no longer respond to the child’s parent request.
15. Instruct the child to change its parent to `stock-router-2` using the extended address observed from `stock_router_2.yaml` logs.
16. Wait 180 seconds.
17. Stop the `IEEE 802.15.4` sniffer recording.
18. Copy the resulting sniffer `.pcapng` into the current run folder for the selected variant as `<variant>_sniffer_<timestamp>.pcapng`.

Configuration note:

* `mcast_child.yaml` is based on the unicast variant but explicitly sets `parent_request_unicast: false`.

Implemented automation:

* For the unicast variant, copy `ucast_test_devices.example.toml` to `ucast_test_devices.toml` and fill in the serial ports.
* For the multicast variant, copy `mcast_test_devices.example.toml` to `mcast_test_devices.toml` and fill in the serial ports.
* Configure the requested maximum router number for the run. Extra routers are flashed in order, starting at `stock_router_3.yaml`.
* The runner reads router2's observed ExtAddr from `stock_router_2.yaml` logs, removes `stock_router_1`, and then sends that ExtAddr to the child automatically.
* Run `./run_ucast_test.sh --config ucast_test_devices.toml` for the unicast variant.
* Run `./run_mcast_test.sh --config mcast_test_devices.toml` for the multicast variant.
* Or use `make ucast-test` or `make mcast-test`.


# Log analysis

Use `scripts/analyze_test_logs.py` for post-run child-log analysis across `stock`, `ucast`, and `mcast` runs. It is variant-agnostic and discovers the matching `*_test_manifest_*.json` file from each run directory.

Timing policy:
- Reported attach timings are derived from sniffer pcap data only for all three variants.
- Child-log timestamps are retained as reference metadata in the report, but are not used as fallback timing values.
- If a run does not have a usable manifest, pcap, network key, or complete matched attach sequence in the pcap, the timing fields remain unavailable.

Examples:

```bash
python3 scripts/analyze_test_logs.py --logs-dir logs/stock --markdown
python3 scripts/analyze_test_logs.py --logs-dir logs/ucast --markdown
python3 scripts/analyze_test_logs.py --logs-dir logs/mcast --markdown
python3 scripts/analyze_test_logs.py --run-dir logs/stock/<timestamp> --markdown
python3 scripts/analyze_test_logs.py --run-dir logs/ucast/<timestamp> --markdown
python3 scripts/analyze_test_logs.py --run-dir logs/mcast/<timestamp> --markdown
```

To write the Markdown report to disk:

```bash
python3 scripts/analyze_test_logs.py \
  --logs-dir logs/mcast \
  --write-markdown

python3 scripts/analyze_test_logs.py \
  --run-dir logs/mcast/<timestamp> \
  --write-markdown
```

With `--logs-dir logs/<variant>`, `--write-markdown` defaults to a variant-wide report:

```text
logs/<variant>/<generated-at>-<variant>-analysis-report.md
```

With a single `--run-dir`, `--write-markdown` defaults to a scoped single-run report at the same variant root:

```text
logs/<variant>/<run-timestamp>-<variant>-analysis-report.md
```
