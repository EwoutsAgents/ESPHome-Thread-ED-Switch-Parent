In this directory the parent switching performance is tested against the stock openthread switching behaviour.

# Stock testing methods
The methods for testing stock performance is as follows:

1. Erase firmware and non-volatile storage using `esptool.py --chip esp32c6 --port <port> erase_flash` for all connected ESP32-C6 boards, even the unused ESP32-C6.
2. Put all ESP32-C6 boards, including unused ones, in a predictable state by flashing `empty.yaml` to them.
3. Start `IEEE 802.15.4` sniffer recording.
4. Wait 5 seconds.
5. Flash the first ESP32-C6 with `stock_router_1.yaml`.
6. Wait 5 seconds.
7. Flash the second ESP32-C6 with `stock_child.yaml`.
8. Wait 10 seconds.
9. Flash the third ESP32-C6 with `stock_router_2.yaml`.
10. Wait 90 seconds so `stock_router_2` has time to become router-capable before removing `stock_router_1`.
11. Flash the first ESP32-C6 with `empty.yaml`.
12. Wait 180 seconds.
13. Stop the `IEEE 802.15.4` sniffer recording.
14. Copy the resulting sniffer `.pcapng` into the current run folder under `testing/logs/stock/<timestamp>/`.

Make sure that any reruns of the above use the same ESP32C6 for each yaml.


# Unicast no-early-attach testing 

The methods for testing stock performance is as follows:
1. Erase firmware and non-volatile storage using `esptool.py --chip esp32c6 --port <port> erase_flash` for all connected ESP32-C6 boards, even the unused ESP32-C6.
2. Put all ESP32-C6 boards, including unused ones, in a predictable state by flashing `empty.yaml` to them.
3. Start `IEEE 802.15.4` sniffer recording.
4. Wait 5 seconds.
5. Flash the first ESP32-C6 with `stock_router_1.yaml`.
6. Wait 5 seconds.
7. Flash the second ESP32-C6 with `ucast_child_no_early_attach.yaml`.
8. Wait 10 seconds.
9. Flash the third ESP32-C6 with `stock_router_2.yaml`.
10. Wait 90 seconds so `stock_router_2` has time to become router-capable.
11. Instruct the child to change its parent to `stock-router-2` using the extended address observed from `stock_router_2.yaml` logs.
12. Wait 180 seconds.
13. Stop the `IEEE 802.15.4` sniffer recording.
14. Copy the resulting sniffer `.pcapng` into the current run folder under `testing/logs/ucast-no-early-attach/<timestamp>/`.

Implemented automation:
- Copy `ucast_no_early_attach_test_devices.example.toml` to `ucast_no_early_attach_test_devices.toml` and fill in the serial ports.
- The runner reads router2's observed ExtAddr from `stock_router_2.yaml` logs and sends that value to the child automatically.
- Run `./run_ucast_no_early_attach_test.sh --config ucast_no_early_attach_test_devices.toml`.
- Or use `make ucast-no-early-attach-test`.

# Multicast no-early-attach testing

The methods for multicast no-early-attach performance testing are as follows:
1. Erase firmware and non-volatile storage using `esptool.py --chip esp32c6 --port <port> erase_flash` for all connected ESP32-C6 boards, even the unused ESP32-C6.
2. Put all ESP32-C6 boards, including unused ones, in a predictable state by flashing `empty.yaml` to them.
3. Start `IEEE 802.15.4` sniffer recording.
4. Wait 5 seconds.
5. Flash the first ESP32-C6 with `stock_router_1.yaml`.
6. Wait 5 seconds.
7. Flash the second ESP32-C6 with `mcast_child_no_early_attach.yaml`.
8. Wait 10 seconds.
9. Flash the third ESP32-C6 with `stock_router_2.yaml`.
10. Wait 90 seconds so `stock_router_2` has time to become router-capable.
11. Instruct the child to change its parent to `stock-router-2` using the extended address observed from `stock_router_2.yaml` logs.
12. Wait 180 seconds.
13. Stop the `IEEE 802.15.4` sniffer recording.
14. Copy the resulting sniffer `.pcapng` into the current run folder under `testing/logs/mcast-no-early-attach/<timestamp>/`.

Configuration note:
- `mcast_child_no_early_attach.yaml` is based on the unicast variant but explicitly sets `parent_request_unicast: false` and `early_attach_on_target: false`.

Implemented automation:
- Copy `mcast_no_early_attach_test_devices.example.toml` to `mcast_no_early_attach_test_devices.toml` and fill in the serial ports.
- The runner reads router2's observed ExtAddr from `stock_router_2.yaml` logs and sends that value to the child automatically.
- Run `./run_mcast_no_early_attach_test.sh --config mcast_no_early_attach_test_devices.toml`.
- Or use `make mcast-no-early-attach-test`.

# Other testing

TBA

# Log analysis

Use `scripts/analyze_stock_logs.py` for post-run child-log analysis across `stock`, `ucast-no-early-attach`, and `mcast-no-early-attach` runs. Despite the filename, it is now variant-agnostic and discovers the matching `*_test_manifest_*.json` file from each run directory.

Timing policy:
- Reported attach timings are derived from sniffer pcap data only for all three variants.
- Child-log timestamps are retained as reference metadata in the report, but are not used as fallback timing values.
- If a run does not have a usable manifest, pcap, network key, or complete matched attach sequence in the pcap, the timing fields remain unavailable.

Examples:

```bash
python3 scripts/analyze_stock_logs.py --logs-dir logs/stock --markdown
python3 scripts/analyze_stock_logs.py --logs-dir logs/ucast-no-early-attach --markdown
python3 scripts/analyze_stock_logs.py --logs-dir logs/mcast-no-early-attach --markdown
python3 scripts/analyze_stock_logs.py --run-dir logs/stock/<timestamp> --markdown
python3 scripts/analyze_stock_logs.py --run-dir logs/ucast-no-early-attach/<timestamp> --markdown
python3 scripts/analyze_stock_logs.py --run-dir logs/mcast-no-early-attach/<timestamp> --markdown
```

To write the Markdown report to disk:

```bash
python3 scripts/analyze_stock_logs.py \
  --logs-dir logs/mcast-no-early-attach \
  --write-markdown

python3 scripts/analyze_stock_logs.py \
  --run-dir logs/mcast-no-early-attach/<timestamp> \
  --write-markdown
```

With `--logs-dir logs/<variant>`, `--write-markdown` defaults to a stock-style variant-wide report:

```text
logs/<variant>/<generated-at>-<variant>-analysis-report.md
```

With a single `--run-dir`, `--write-markdown` defaults to a scoped single-run report at the same variant root:

```text
logs/<variant>/<run-timestamp>-<variant>-analysis-report.md
```
