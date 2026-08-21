# Testing

This directory contains the automated hardware tests for the supported
parent-switch variants:

* `stock`: natural OpenThread recovery after the current parent is removed.
* `ucast`: directed preferred-parent switching using a unicast Parent Request.
* `fast-attach`: stock-like parent removal using OpenThread PR #13121 Fast Attach during recovery.
* `fast-attach-ucast-32`: proactive selected-parent handoff using unicast Fast Attach and a 32 ms response ceiling.

The runners support two, three, or four ESP32-C6 routers plus one child. The
device-specific TOML files map those roles to serial ports and configure test
timing, logging, and sniffer integration.

## Entry points

Stock:

```bash
cd testing
./run_stock_test.sh --config stock_test_devices_4routers.toml
```

Unicast:

```bash
cd testing
./run_ucast_test.sh --config ucast_test_devices_4routers.toml
```

Fast Attach:

```bash
cd testing
./run_fast_attach_test.sh --config fast_attach_test_devices_4routers.toml
```

Fast Attach unicast 32:

```bash
cd testing
./run_fast_attach_ucast_32_test.sh --config fast_attach_ucast_32_test_devices_4routers.toml
```

Common runner options include:

```text
--runs N
--dry-run
--precompile-only
--skip-precompile
--force-precompile
--clean-before-compile
--reset-platformio-packages
--platformio-core-dir PATH
--platformio-packages-dir PATH
```

Equivalent Make targets are available:

```bash
make stock-test CONFIG=stock_test_devices_4routers.toml RUNS=5
make ucast-test UCAST_CONFIG=ucast_test_devices_4routers.toml RUNS=5
make dry-run CONFIG=stock_test_devices_4routers.toml
make ucast-dry-run UCAST_CONFIG=ucast_test_devices_4routers.toml
```

## Firmware configurations

Shared utility firmware:

* `configs/empty.yaml`

Stock firmware:

* `configs/stock_child.yaml`
* `configs/stock_router_1.yaml` through `configs/stock_router_4.yaml`

Unicast firmware:

* `configs/ucast_child.yaml`
* `configs/stock_router_1.yaml` through `configs/stock_router_4.yaml`

Fast Attach firmware:

* `configs/fast_attach_child.yaml`
* `configs/fast_attach_router_1.yaml` through `configs/fast_attach_router_4.yaml`

Fast Attach unicast 32 firmware:

* `configs/fast_attach_ucast_32_child.yaml`
* `configs/fast_attach_ucast_32_router_1.yaml` through `configs/fast_attach_ucast_32_router_4.yaml`

The preferred-parent component always uses targeted unicast discovery. Both
variants disable OpenThread's default periodic MTD parent search so it cannot
interfere with the experiment.

## Isolated build environments

Each runner uses a variant-specific PlatformIO core by default:

```text
testing/.platformio-core/stock/
testing/.platformio-core/ucast/
testing/.platformio-core/fast-attach/
testing/.platformio-core/fast-attach-ucast-32/
```

Packages are kept inside the selected core. This prevents framework state from
one variant contaminating the other. Use `--reset-platformio-packages` when a
clean framework installation is required.

## Results

Repeated runs are written under:

```text
logs/stock-<n>router-<runs>runs-<timestamp>/
logs/ucast-<n>router-<runs>runs-<timestamp>/
```

Each run records device logs, a manifest, packet CSV exports, and a sniffer
capture when enabled. Analyze a batch with:

```bash
python3 scripts/analyze_test_logs.py \
  --logs-dir logs/ucast-4router-<runs>runs-<timestamp> \
  --markdown
```

Use `scripts/pcap_to_csv.py` to regenerate packet exports from a capture.

## Methodology

* [README_STOCK_TEST.md](README_STOCK_TEST.md) defines the stock/reference
  procedure and validity criteria.
* [README_UCAST_TEST.md](README_UCAST_TEST.md) defines the directed unicast
  procedure and target-selection criteria.
* [README_FAST_ATTACH_TEST.md](README_FAST_ATTACH_TEST.md) defines the isolated
  PR #13121 backport, runtime re-arm evidence, and remaining packet checks.
