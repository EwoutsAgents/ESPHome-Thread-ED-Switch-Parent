# Stock low-power testing methods

`stock-low-power` uses the stock parent-removal procedure without changing OpenThread protocol behavior. Its only radio-level difference is an explicit asymmetric router transmit-power configuration:

* `router1`: 0 dBm
* `router2`: 0 dBm
* `router3`: -15 dBm
* `router4`: -15 dBm

The child firmware and network dataset are copied from stock. Routers 1 and 2 are intended to dominate the child's parent choice. When the detected initial parent is one of those two routers, removing it leaves the other 0 dBm router as the expected replacement parent. This is an experimental expectation, not an OpenThread selection override; normal link measurements and parent-selection rules remain authoritative.

The dedicated runner records the complete power map, whether the detected initial parent was a 0 dBm router, and the identity of the expected remaining 0 dBm router. It otherwise preserves stock's erase, flash, settle, natural initial attachment, parent detection, parent removal, observation, capture, and classification procedure.

Run a two-, three-, or four-router test with:

```bash
cd testing
./run_stock_low_power_test.sh --config stock_low_power_test_devices_4routers.toml
```

Build and package isolation is rooted at `testing/.platformio-core/stock-low-power/`. Repeated results use `testing/logs/stock-low-power-<n>router-<runs>runs-<timestamp>/`.
