# OTNS integration scope

The native OTNS integration mirrors the supported hardware variants:

| Variant | Child behavior | Router behavior |
| --- | --- | --- |
| `stock` | Ordinary OpenThread attachment and recovery | Ordinary OpenThread FTD |
| `ucast` | Directed selected-parent discovery using unicast | Ordinary OpenThread FTD |
| `fast-attach` | PR #13121 Fast Attach recovery | Fast Attach-aware FTD |
| `fast-attach-ucast-32` | Directed unicast Fast Attach | Fast Attach-aware FTD with a 32 ms response ceiling |
| `fast-attach-ucast-1` | Directed unicast Fast Attach | Fast Attach-aware FTD with a fixed 1 ms response delay |

No separate router-response variant is built. Both variants use normal
OpenThread Parent Response scheduling on routers.

## Native profiles

The build driver produces these isolated binaries:

```text
artifacts/stock-mtd-pps-off/ot-cli-mtd
artifacts/preferred-parent-mtd-pps-off/ot-cli-mtd
artifacts/stock-ftd/ot-cli-ftd
artifacts/stock-ftd-delay-diagnostic/ot-cli-ftd
artifacts/fast-attach-mtd-pps-off/ot-cli-mtd
artifacts/fast-attach-ftd/ot-cli-ftd
artifacts/fast-attach-ucast-32-mtd-pps-off/ot-cli-mtd
artifacts/fast-attach-ucast-32-ftd/ot-cli-ftd
artifacts/fast-attach-ucast-1-mtd-pps-off/ot-cli-mtd
artifacts/fast-attach-ucast-1-ftd/ot-cli-ftd
```

The preferred-parent MTD exposes only targeted unicast switching through its
CLI adapter. Stock FTDs are shared by stock and ucast scenarios. The optional
delay-diagnostic FTD changes logging only; it does not change response timing.

## Patch composition

The native selected-parent build applies:

1. `patches/canonical/openthread-preferred-parent-controller.patch`
2. `patches/otns/preferred-parent-cli-adapter.patch`

The diagnostic stock FTD applies only:

1. `patches/canonical/parent-response-delay-diagnostic.patch`

Fast Attach uses the isolated PR #13121 backport. The two combined directed
profiles use generated native patches under `patches/otns/`; these compose the
preferred-parent controller, Fast Attach backport, response-delay policy, and
native CLI adapter into one patch that applies cleanly to the pinned revision.

All patches target OpenThread commit
`a12ff0d0f54fd41954b45047fcdd08f302731c5f`.

## Build

```bash
OPENTHREAD_REPOSITORY=/path/to/full/openthread-repository \
OTNS_RFSIM_DIR=/path/to/ot-ns/ot-rfsim \
OTNS_VARIANT_ROOT=/new/path/to/openthread-variants \
./scripts/build_otns_native_variants.sh
```

The output root must not exist before the build. The script creates independent
source trees, records hashes and compiler provenance, and publishes only the
stock and ucast-compatible artifacts listed above.

## Scenario requirements

OTNS-MAPS scenarios should retain matching two-, three-, and four-router cases
for stock, ucast, Fast Attach, and the 32 ms and 1 ms combined variants. Directed
cases must:

* identify a target router that is not the current parent;
* direct the Parent Request to that target;
* keep ordinary router Parent Response timing;
* verify the final parent by extended address;
* record Parent Request, Parent Response, Child ID Request, and Child ID
  Response timestamps from OpenThread events and packet captures.

The hardware and simulator runners should use the same outcome classifications
and timing definitions so results remain comparable.
