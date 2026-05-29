In this directory the parent switching performance is tested against the stock openthread switching behaviour.

# Stock testing methods
The methods for testing stock performance is as follows:
1. Reset the setup by flashing all connected ESP32C6s with `empty.yaml` and using the `erase_flash` parameter in the flash command (`esptool.py`) to ensure no lingering firmware or configuration messes up the testing.
2. Flash the first ESP32C6 with `stock_router_1.yaml`.
3. Wait 10 seconds.
4. Flash the second ESP32C6 with `stock_child.yaml`, record its logs in a `.log` file.
5. Wait 30 seconds.
6. Flash the third ESP32C6 with `stock_router_2.yaml`.
7. Wait 60 seconds.
8. Flash the first ESP32C6 with `empty.yaml`.
9. Wait 300 seconds.
10. Stop the recording.

Make sure that any reruns of the above use the same ESP32C6 for each yaml.

# Other testing
TBA

