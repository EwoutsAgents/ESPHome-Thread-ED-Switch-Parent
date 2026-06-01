In this directory the parent switching performance is tested against the stock openthread switching behaviour.

# Stock testing methods
The methods for testing stock performance is as follows:

1. Erase firmware and non-volatile storage using `esptool.py --chip esp32c6 --port <port> erase_flash` for all connected ESP32-C6 boards, even the unused ESP32-C6.
2. Put all ESP32-C6 boards, including unused ones, in a predictable state by flashing `empty.yaml` to them.
3. Start `IEEE 802.15.4` sniffer recording.
4. Wait a short sniffer lead-in so recording is already active before any test node starts.
5. Flash the first ESP32-C6 with `stock_router_1.yaml`.
6. Wait 5 seconds.
7. Flash the second ESP32-C6 with `stock_child.yaml`.
8. Wait 10 seconds.
9. Flash the third ESP32-C6 with `stock_router_2.yaml`.
10. Wait 10 seconds.
11. Flash the first ESP32-C6 with `empty.yaml`.
12. Wait 180 seconds.
13. Stop the `IEEE 802.15.4` sniffer recording.
14. Copy the resulting sniffer `.pcapng` into the current run folder under `testing/logs/stock/<timestamp>/`.

Make sure that any reruns of the above use the same ESP32C6 for each yaml.

# Other testing
