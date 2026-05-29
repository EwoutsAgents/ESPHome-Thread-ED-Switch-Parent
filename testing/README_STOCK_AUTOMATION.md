# Stock parent-switching test automation

This implementation follows the stock testing sequence in `README.md`, with one measurement-critical change: **all ESPHome compilations happen before the timed test sequence starts**.

During the timed sequence, the runner only calls:

```bash
esptool.py --chip esp32c6 --port <port> erase_flash
esphome upload <yaml> --device <port>
```

It does not call `esphome run` during the timed sequence. This avoids compile-time variation affecting the waits between router/child introduction and router removal.

## Files

- `scripts/run_stock_test.py` — main automation runner.
- `run_stock_test.sh` — convenience wrapper that prefers the repository-local Python venv.
- `stock_test_devices.example.toml` — copy this to `stock_test_devices.toml` and edit serial ports.
- `configs/*.yaml` — current stock configs from the `better_testing` branch.
  - `configs/stock_child.yaml` explicitly sets `CONFIG_OPENTHREAD_PARENT_SEARCH_MTD: n` so the stock-child test does not include ESP-IDF/OpenThread's default periodic MTD parent-search behaviour.
- `logs/` — generated child logs and JSON run manifests.

## Setup

From the repository root, keep your ESPHome virtualenv as either `.venv/` or `venv/`. The wrapper and runner auto-detect both.

```bash
cd testing
cp stock_test_devices.example.toml stock_test_devices.toml
$EDITOR stock_test_devices.toml
```

Assign each physical ESP32-C6 to a stable role:

```toml
[devices]
router1 = "/dev/ttyACM0"
child = "/dev/ttyACM1"
router2 = "/dev/ttyACM2"
```

Do not swap these assignments between reruns unless you deliberately restart the experiment design.

## Full test

```bash
cd testing
./run_stock_test.sh --config stock_test_devices.toml
```

Equivalent Make target:

```bash
make stock-test
```

## Dry run

Print the exact compile, upload, log, and wait sequence without touching hardware:

```bash
./run_stock_test.sh --config stock_test_devices.toml --dry-run
```

## Precompile only

Compile all four firmware images and exit before flashing anything:

```bash
./run_stock_test.sh --config stock_test_devices.toml --precompile-only
```

## Clean build before compiling

Use this when you want to force all firmware artifacts to be rebuilt before the upload-only timed sequence:

```bash
./run_stock_test.sh --config stock_test_devices.toml --clean-before-compile
```

This is recommended after changing `sdkconfig_options`, so the generated ESP-IDF config is rebuilt from scratch.

## Actual command phases

Pre-test phase:

```bash
esphome compile configs/empty.yaml
esphome compile configs/stock_router_1.yaml
esphome compile configs/stock_child.yaml
esphome compile configs/stock_router_2.yaml
```

Timed phase:

1. `erase_flash`, then `upload empty.yaml`, for router 1, child, and router 2.
2. `upload stock_router_1.yaml` to router 1.
3. Wait 10 seconds.
4. `upload stock_child.yaml` to child and start `esphome logs` for the child.
5. Wait 30 seconds.
6. `upload stock_router_2.yaml` to router 2.
7. Wait 60 seconds.
8. `upload empty.yaml` to router 1.
9. Wait 300 seconds while child logging continues.
10. Stop child logging.

Each run writes:

- `logs/stock_child_<timestamp>.log`
- `logs/stock_test_manifest_<timestamp>.json`

The JSON manifest records every command and wait event, which makes it easier to audit whether a result included compilation in the timed section.
