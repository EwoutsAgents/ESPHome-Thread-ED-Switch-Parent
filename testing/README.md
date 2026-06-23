# Testing

This folder contains the automated test runners, device configuration files, sniffer integration, generated logs, packet captures, manifests, and post-run analysis tooling for the Thread parent-switch experiments.

The test variants are:

* `stock`: natural OpenThread parent switching without using the preferred-parent switching mechanism.
* `ucast`: preferred-parent switching using unicast control.
* `mcast`: preferred-parent switching using multicast control.

Variant-specific methodology is documented separately:

* `README_STOCK_TEST.md` — stock/reference parent-switching methodology and validity criteria.
* `README_MCAST_UCAST_TEST.md` — preferred-parent unicast and multicast methodology.

This README covers the shared automation, setup, runner usage, output layout, and analysis workflow.

## Files

Runner wrappers:

* `run_stock_test.sh`
* `run_ucast_test.sh`
* `run_mcast_test.sh`

Device configuration examples:

* `stock_test_devices.example.toml`
* `ucast_test_devices.example.toml`
* `mcast_test_devices.example.toml`

Local device configuration files:

* `stock_test_devices.toml`
* `stock_test_devices_2routers.toml`
* `stock_test_devices_3routers.toml`
* `ucast_test_devices.toml`
* `mcast_test_devices.toml`

Test methodology documents:

* `README_STOCK_TEST.md`
* `README_MCAST_UCAST_TEST.md`

Post-run analysis:

* `scripts/analyze_test_logs.py`

Generated logs, manifests, CSV exports, reports, and sniffer captures are written under the variant-specific log directories.

## Compilation policy

All ESPHome compilations should happen before a timed test sequence starts. During the timed sequence, runners should perform only erase, upload, logging, wait, control, validation, and capture operations.

The timed sequence should not call `esphome run`, because compile-time variation would affect the measured timing.

The intended timed flash/upload operations are:

```bash
esptool.py --chip esp32c6 --port <port> erase_flash
esphome upload <yaml> --device <port>
```

Runner options such as `--precompile-only` and `--clean-before-compile` are used to make the compilation phase explicit and auditable.

## Setup

From the repository root, keep the ESPHome virtual environment as either `.venv/` or `venv/`. The test wrappers auto-detect both.

Create a local device configuration file from the appropriate example:

```bash
cd testing
cp stock_test_devices.example.toml stock_test_devices.toml
cp ucast_test_devices.example.toml ucast_test_devices.toml
cp mcast_test_devices.example.toml mcast_test_devices.toml
```

Edit the relevant TOML file and assign each physical ESP32-C6 board to a stable role.

Example stock configuration shape:

```toml
[devices]
router1 = "/dev/ttyACM0"
child = "/dev/ttyACM1"
router2 = "/dev/ttyACM2"
unused1 = "/dev/ttyACM3"
unused2 = "/dev/ttyACM4"

[variant]
# Highest stock router number included in the run.
# 2 means stock_router_1 + stock_router_2.
# 3 means stock_router_1 + stock_router_2 + stock_router_3.
# 4 means stock_router_1 + stock_router_2 + stock_router_3 + stock_router_4.
n_routers = 3
```

Example sniffer and timing configuration shape:

```toml
[timing]
sniffer_lead_in_seconds = 5

[sniffer]
enabled = true
command = ["ssh", "rpi-802154-sniffer", "~/bin/nrf802154-sniff"]
```

Variant-specific timing keys are defined by the corresponding runner and TOML example. Keep the TOML keys aligned with the runner implementation.

Do not swap physical device assignments between repeated runs unless the experiment design is intentionally being changed.

## Running tests

Run commands are executed from the `testing/` directory.

### Stock

```bash
./run_stock_test.sh --config stock_test_devices.toml
```

Alternative stock configurations can be used when present:

```bash
./run_stock_test.sh --config stock_test_devices_2routers.toml
./run_stock_test.sh --config stock_test_devices_3routers.toml
```

### Unicast preferred-parent

```bash
./run_ucast_test.sh --config ucast_test_devices.toml
```

### Multicast preferred-parent

```bash
./run_mcast_test.sh --config mcast_test_devices.toml
```

## Multiple runs

Repeated runs can be executed with `--runs` where supported by the runner:

```bash
./run_stock_test.sh --config stock_test_devices.toml --runs 5
./run_ucast_test.sh --config ucast_test_devices.toml --runs 5
./run_mcast_test.sh --config mcast_test_devices.toml --runs 5
```

Each repeated timed run gets its own run folder with a `-runNN` suffix.

Example:

```text
logs/stock/20260609-030000-run03/
```

## Dry run

Use `--dry-run` to print the planned compile, upload, log, wait, control, and capture sequence without touching hardware, where supported:

```bash
./run_stock_test.sh --config stock_test_devices.toml --dry-run
./run_ucast_test.sh --config ucast_test_devices.toml --dry-run
./run_mcast_test.sh --config mcast_test_devices.toml --dry-run
```

## Precompile only

Use `--precompile-only` to compile the required firmware artifacts and exit before flashing anything, where supported:

```bash
./run_stock_test.sh --config stock_test_devices.toml --precompile-only
./run_ucast_test.sh --config ucast_test_devices.toml --precompile-only
./run_mcast_test.sh --config mcast_test_devices.toml --precompile-only
```

## Clean build before compiling

Use `--clean-before-compile` when firmware artifacts should be rebuilt from scratch before the upload-only timed sequence, where supported:

```bash
./run_stock_test.sh --config stock_test_devices.toml --clean-before-compile
./run_ucast_test.sh --config ucast_test_devices.toml --clean-before-compile
./run_mcast_test.sh --config mcast_test_devices.toml --clean-before-compile
```

This is recommended after changing `sdkconfig_options`, so the generated ESP-IDF configuration is rebuilt from scratch.

## Output files

Each run writes into its own timestamped folder under the relevant variant log directory.

Typical variant roots:

```text
logs/stock/
logs/ucast/
logs/mcast/
```

Typical generated files include:

```text
<variant>_child_<timestamp>.log
<variant>_router1_<timestamp>.log
<variant>_router2_<timestamp>.log
<variant>_sniffer_<timestamp>.log
<variant>_sniffer_<timestamp>.pcapng
<variant>_test_manifest_<timestamp>.json
```

Some variants or runs may include additional router logs, runner supervisor logs, CSV exports, analysis reports, or generated packet summaries.

The JSON manifest records the command sequence, wait events, device-role mapping, sniffer paths, copied `.pcapng` path, and other run metadata needed to audit the run.

## Sniffer capture

When `[sniffer].enabled = true`, the runner starts the configured IEEE 802.15.4 sniffer command before the timed test sequence and stops it after the measurement window.

The resulting `.pcapng` is copied into the run folder using the local naming scheme for that variant and timestamp.

Sniffer packet data is the authoritative source for attach timing in the analysis pipeline. Device logs are retained for context, state interpretation, and debugging.

## Methodology documents

Use the variant-specific methodology documents to understand what each test is intended to measure and how valid runs are classified.

### Stock

`README_STOCK_TEST.md` defines the stock/reference method.

At a high level, the stock test measures natural OpenThread parent switching without using the preferred-parent mechanism. The stock method is opportunistic: it observes which router the child naturally attaches to, checks whether that parent can be removed without destabilizing the remaining router topology, and only treats the run as a valid reference measurement if the child switches parent while the remaining candidate-parent topology stays stable.

### Unicast and multicast

`README_MCAST_UCAST_TEST.md` defines the preferred-parent unicast and multicast methods.

At a high level, these tests measure explicit preferred-parent switching behavior. The child is instructed to switch toward a selected parent using the variant-specific control mechanism, while the runner records logs and sniffer traffic for timing and protocol analysis.

## Log analysis

Use `scripts/analyze_test_logs.py` for post-run analysis across `stock`, `ucast`, and `mcast` runs. The analyzer is variant-agnostic and discovers the matching `*_test_manifest_*.json` file from each run directory.

Examples:

```bash
python3 scripts/analyze_test_logs.py --logs-dir logs/stock --markdown
python3 scripts/analyze_test_logs.py --logs-dir logs/ucast --markdown
python3 scripts/analyze_test_logs.py --logs-dir logs/mcast --markdown

python3 scripts/analyze_test_logs.py --run-dir logs/stock/<timestamp> --markdown
python3 scripts/analyze_test_logs.py --run-dir logs/ucast/<timestamp> --markdown
python3 scripts/analyze_test_logs.py --run-dir logs/mcast/<timestamp> --markdown
```

To write a Markdown report to disk:

```bash
python3 scripts/analyze_test_logs.py \
  --logs-dir logs/stock \
  --write-markdown

python3 scripts/analyze_test_logs.py \
  --logs-dir logs/ucast \
  --write-markdown

python3 scripts/analyze_test_logs.py \
  --logs-dir logs/mcast \
  --write-markdown

python3 scripts/analyze_test_logs.py \
  --run-dir logs/stock/<timestamp> \
  --write-markdown
```

With `--logs-dir logs/<variant>`, `--write-markdown` writes a variant-wide report:

```text
logs/<variant>/<generated-at>-<variant>-analysis-report.md
```

With a single `--run-dir`, `--write-markdown` writes a scoped single-run report at the same variant root:

```text
logs/<variant>/<run-timestamp>-<variant>-analysis-report.md
```

## Timing policy

Reported attach timings come from matched sniffer PCAP events only.

Log timestamps are retained as reference metadata in the report, but they are not used as fallback timing values.

If a run does not have a usable manifest, PCAP, network key, or complete matched attach sequence in the PCAP, the timing fields remain unavailable.

This policy applies to all three variants: `stock`, `ucast`, and `mcast`.

## CSV and packet exports

When packet CSV exports are generated, the all-packets CSV contains the decoded packet stream and the attach-MLE CSV contains decoded MLE attach-related packets, such as Parent Request, Parent Response, Child ID Request, and Child ID Response.

Attach CSV files may contain MLE attach traffic from multiple devices, not only the target child. Parent-switch metrics should therefore be computed against the target child identity and the matched complete attach sequence, not from global attach traffic alone.

## Recommended cleanup

`README.md` is the shared automation entry point.

Keep variant-specific methodology in:

```text
README_STOCK_TEST.md
README_MCAST_UCAST_TEST.md
```

Avoid duplicating runner usage, output layout, and analyzer instructions in the variant methodology documents unless a variant has genuinely different behavior.
