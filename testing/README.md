In this directory the parent switching performance is tested against the stock openthread switching behaviour.

# Stock testing methods
The methods for testing stock performance is as follows:
1. Erase firmware and non-volatile storage using `esptool.py --chip esp32c6 --port <port> erase_flash` for all connected ESP32C6s (even the unused ESP32C6).
2. Put all ESP32C6s (including unused) in a predictable state by flashing `empty.yaml` to it.
3. Flash the first ESP32C6 with `stock_router_1.yaml`.
4. Start `IEEE 802.15.4` sniffer recording.
5. Wait 10 seconds.
6. Flash the second ESP32C6 with `stock_child.yaml`.
7. Wait 30 seconds.
8. Flash the third ESP32C6 with `stock_router_2.yaml`.
9. Wait 60 seconds.
10. Flash the first ESP32C6 with `empty.yaml`.
11. Wait 300 seconds.
12. Stop the `IEEE 802.15.4` sniffer recording.

Make sure that any reruns of the above use the same ESP32C6 for each yaml.

# Other testing
TBA

