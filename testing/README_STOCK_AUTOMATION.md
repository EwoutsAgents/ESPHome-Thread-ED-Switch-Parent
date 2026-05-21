# Stock OpenThread parent-switching test automation

This package automates the stock testing sequence described in `testing/README.md` for three ESP32-C6 boards:

1. Flash all assigned ESP32-C6 boards with `empty.yaml`.
2. Flash the first board with `stock_router_1.yaml`.
3. Wait 10 seconds.
4. Flash the second board with `stock_child.yaml` and start recording child logs to a `.log` file.
5. Wait 30 seconds.
6. Flash the third board with `stock_router_2.yaml`.
7. Wait 60 seconds.
8. Flash the first board with `empty.yaml` to remove the original parent.
9. Continue recording child logs for 300 seconds.
10. Stop the recording.

The runner enforces a fixed role-to-port mapping for `router1`, `child`, and `router2`; keep the same physical ESP32-C6 board on the same role for repeated trials.

## Files

- `configs/empty.yaml` — minimal ESP32-C6 firmware used to wipe/reset test firmware.
- `configs/stock_router_1.yaml` — stock OpenThread FTD router 1.
- `configs/stock_router_2.yaml` — stock OpenThread FTD router 2.
- `configs/stock_child.yaml` — stock OpenThread MTD child with very verbose UART logging.
- `scripts/run_stock_test.py` — the timed runner.
- `stock_test_devices.example.toml` — role-to-port configuration template.
- `run_stock_test.sh` — convenience wrapper for Unix-like shells.
- `logs/` — output directory for child logs, command logs, and JSON manifests.

## Requirements

- A repository-local virtualenv at `venv/` that includes ESPHome. With this package in `<repo>/testing`, the default ESPHome executable is `<repo>/venv/bin/esphome`.
- Python 3.11 or newer if using the TOML config file. The `run_stock_test.sh` wrapper prefers `<repo>/venv/bin/python` when it exists.
- Three ESP32-C6 boards connected over USB serial.

ESPHome's CLI supports `run <CONFIG> --device <PORT> --no-logs` for compile/upload without opening the log view, and `logs <CONFIG> --device <PORT>` for explicit log capture. The runner uses that default flow.

The ESPHome executable is resolved in this order: `--esphome-bin`, `ESPHOME_BIN`, `[esphome].bin` in `stock_test_devices.toml`, then local `venv` auto-detection, then `esphome` on `PATH`.

## Setup

From the `testing/` directory:

```bash
cp stock_test_devices.example.toml stock_test_devices.toml
$EDITOR stock_test_devices.toml
```

Set each serial port carefully. Example:

```toml
[devices]
router1 = "/dev/ttyACM0"
child = "/dev/ttyACM1"
router2 = "/dev/ttyACM2"
```

## Dry run

```bash
python3 scripts/run_stock_test.py --config stock_test_devices.toml --dry-run
```

This prints the commands and creates dry-run metadata without flashing devices or waiting.

## Run the stock test

```bash
python3 scripts/run_stock_test.py --config stock_test_devices.toml
```

Or:

```bash
./run_stock_test.sh
```

## Outputs

Each run creates timestamped output in `logs/`:

- `stock_child_<timestamp>.log` — child serial/API log capture.
- `stock_test_<timestamp>_commands.log` — commands executed by the runner.
- `stock_test_<timestamp>_manifest.json` — run metadata, device mapping, timings, and status.

## Useful overrides

Shorten waits for a smoke test:

```bash
python3 scripts/run_stock_test.py \
  --config stock_test_devices.toml \
  --timing-after-router1 1 \
  --timing-after-child 1 \
  --timing-after-router2 1 \
  --timing-after-router1-empty 1
```

Pass ports without TOML:

```bash
python3 scripts/run_stock_test.py \
  --router1-port /dev/ttyACM0 \
  --child-port /dev/ttyACM1 \
  --router2-port /dev/ttyACM2 \
  --config-dir configs \
  --log-dir logs
```

Use already compiled firmware instead of compile+flash:

```bash
python3 scripts/run_stock_test.py --config stock_test_devices.toml --flash-command upload
```

Use a non-default ESPHome binary:

```bash
ESPHOME_BIN=/path/to/venv/bin/esphome ./run_stock_test.sh
# or
python3 scripts/run_stock_test.py --config stock_test_devices.toml --esphome-bin /path/to/venv/bin/esphome
```
