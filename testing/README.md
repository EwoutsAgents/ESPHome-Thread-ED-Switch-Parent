In this directory the parent switching performance is tested against the stock openthread switching behaviour.

# Stock testing methods
The methods for testing stock performance is as follows:
1. Erase firmware and non-volatile storage using `esptool.py --chip esp32c6 --port <port> erase_flash` for all connected ESP32C6s.
2. Put all ESP32C6s in a predictable state by flashing `empty.yaml` to it.
3. Flash the first ESP32C6 with `stock_router_1.yaml`.
4. Wait 10 seconds.
5. Flash the second ESP32C6 with `stock_child.yaml`, record its logs in a `.log` file.
6. Wait 30 seconds.
7. Flash the third ESP32C6 with `stock_router_2.yaml`.
8. Wait 60 seconds.
9. Flash the first ESP32C6 with `empty.yaml`.
10. Wait 300 seconds.
11. Stop the recording.

Make sure that any reruns of the above use the same ESP32C6 for each yaml.

# Other testing
TBA

