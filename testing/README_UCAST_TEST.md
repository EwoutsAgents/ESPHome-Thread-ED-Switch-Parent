# Unicast testing method

The `ucast` test measures directed OpenThread parent switching. The child first
attaches naturally, then receives the extended address of a different eligible
router and starts selected-parent discovery using a unicast Parent Request.

## Firmware

| Role | Configuration |
| --- | --- |
| Child | `testing/configs/ucast_child.yaml` |
| Routers | `testing/configs/stock_router_<n>.yaml` |

The preferred-parent component sends discovery directly to the selected router.
Routers retain the ordinary randomized Parent Response behavior.

Router firmware records the selected OpenThread Parent Response delay as
`ParentResponseDelay delay_ms=N scan_mask=0xNN child=EXTADDR`. The runner stores
matching target-router diagnostics in the manifest and fails a completed run if
no delay record matches the directed child. This enables exact random-delay
subtraction during analysis.

## Procedure

1. Erase all participating ESP32-C6 boards and flash `empty.yaml`.
2. Start the IEEE 802.15.4 sniffer when configured.
3. Flash the requested routers and wait for the topology to settle.
4. Flash the child and let it attach naturally.
5. Read the router extended addresses and identify the child's current parent.
6. Select an eligible router that is not the current parent.
7. Send the selected router's extended address to the child over USB serial.
8. Keep the initial parent active while selected-parent discovery and attach run.
9. Record the final parent, protocol timing, logs, manifest, and packet capture.

A run cannot enter the directed-switch phase unless the current parent can be
mapped to a configured router and at least one different target router is
available. Topology changes and terminal outcomes remain explicit in the run
manifest for later classification.

## Running the test

```bash
cd testing
./run_ucast_test.sh \
  --config ucast_test_devices_4routers.toml \
  --runs 20
```

The default router-settling delay is 300 seconds unless overridden in the TOML
configuration. At least two routers are required; four are currently supported.
