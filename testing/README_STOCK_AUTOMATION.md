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
- `scripts/analyze_stock_logs.py` — post-run child-log analyzer for `stock`, `ucast-no-early-attach`, and `mcast-no-early-attach`.
  - Reported attach timings are derived from sniffer pcap data only.
  - Child-log timestamps are preserved as reference metadata and are not used as fallback timing values.
- `stock_test_devices.example.toml` — copy this to `stock_test_devices.toml` and edit serial ports.
  - Optional extra device entries such as `unused` are erased and flashed with `empty.yaml` before the timed sequence starts.
  - Optional `[sniffer]` settings can start/stop an IEEE 802.15.4 capture command during the timed sequence, then pull the resulting `.pcapng` into `logs/stock/`.
- `configs/*.yaml` — current stock configs from the `better_testing` branch.
  - `configs/stock_child.yaml` explicitly sets `CONFIG_OPENTHREAD_PARENT_SEARCH_MTD: n` so the stock-child test does not include ESP-IDF/OpenThread's default periodic MTD parent-search behaviour.
- `logs/stock/` — base directory for generated run folders, stock child logs, `.pcapng` captures, and JSON manifests.

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
unused = "/dev/ttyACM3"
```

Optional sniffer integration:

```toml
[timing]
sniffer_lead_in_seconds = 5
after_router1_seconds = 5
after_child_seconds = 10
after_router2_seconds = 90
after_router1_removed_seconds = 180

[sniffer]
enabled = true
command = ["ssh", "rpi-802154-sniffer", "~/bin/nrf802154-sniff"]
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

## Multiple runs

Execute the timed stock test multiple times with one command. The precompile phase still runs only once before the repeated timed sequence starts.

```bash
./run_stock_test.sh --config stock_test_devices.toml --runs 5
```

Equivalent Make invocation:

```bash
make stock-test RUNS=5
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

1. `erase_flash`, then `upload empty.yaml`, for router 1, child, router 2, and any extra configured ESP32-C6 roles such as `unused`.
2. Start the optional sniffer capture command.
3. Wait `sniffer_lead_in_seconds` so the sniffer is already recording before any test node starts.
4. `upload stock_router_1.yaml` to router 1.
5. Wait 5 seconds.
6. `upload stock_child.yaml` to child and start `esphome logs` for the child.
7. Wait 10 seconds.
8. `upload stock_router_2.yaml` to router 2.
9. Wait 90 seconds.
10. `upload empty.yaml` to router 1.
11. Wait 180 seconds while child logging continues.
12. Stop the optional sniffer capture command.
13. Copy the resulting sniffer `.pcapng` into `logs/stock/`.
14. Stop child logging.

Each run writes into its own timestamped folder:

- `logs/stock/<timestamp>/stock_child_<timestamp>.log`
- `logs/stock/<timestamp>/stock_sniffer_<timestamp>.log` when `[sniffer].enabled = true`
- `logs/stock/<timestamp>/<sniffer-capture-basename>.pcapng` when `[sniffer].enabled = true`
- `logs/stock/<timestamp>/stock_test_manifest_<timestamp>.json`

When `--runs N` is used, each repeated timed run gets its own folder with a `-runNN` suffix, for example `logs/stock/20260609-030000-run03/`.

The JSON manifest records every command and wait event, including the remote sniffer pcap path and the pulled local pcap path, which makes it easier to audit whether a result included compilation in the timed section.

## Log analysis

The post-run analyzer is no longer stock-specific despite the filename:

```bash
python3 scripts/analyze_stock_logs.py --run-dir logs/stock/<timestamp> --markdown
python3 scripts/analyze_stock_logs.py --run-dir logs/ucast-no-early-attach/<timestamp> --markdown
python3 scripts/analyze_stock_logs.py --run-dir logs/mcast-no-early-attach/<timestamp> --markdown
```

To write a Markdown report to disk:

```bash
python3 scripts/analyze_stock_logs.py \
  --run-dir logs/mcast-no-early-attach/<timestamp> \
  --write-markdown
```

With a single `--run-dir`, `--write-markdown` defaults to:

```text
logs/<variant>/<timestamp>-<variant>-analysis-report.md
```

Timing policy for all variants:

- Reported attach timings come from matched pcap events only.
- Log timestamps are shown for reference but never substituted for missing pcap timings.
- If the analyzer cannot match a complete attach sequence in pcap, the timing fields remain unavailable.
