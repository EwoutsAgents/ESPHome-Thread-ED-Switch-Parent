# OTNS integration scope

The native OTNS integration mirrors the two supported hardware variants:

| Variant | Child behavior | Router behavior |
| --- | --- | --- |
| `stock` | Ordinary OpenThread attachment and recovery | Ordinary OpenThread FTD |
| `ucast` | Directed selected-parent discovery using unicast | Ordinary OpenThread FTD |

No separate router-response variant is built. Both variants use normal
OpenThread Parent Response scheduling on routers.

## Native profiles

The build driver produces these isolated binaries:

```text
artifacts/stock-mtd-pps-off/ot-cli-mtd
artifacts/preferred-parent-mtd-pps-off/ot-cli-mtd
artifacts/stock-ftd/ot-cli-ftd
artifacts/stock-ftd-delay-diagnostic/ot-cli-ftd
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

OTNS-MAPS scenarios should retain matching two-, three-, and four-router stock
and ucast cases. Ucast cases must:

* identify a target router that is not the current parent;
* direct the Parent Request to that target;
* keep ordinary router Parent Response timing;
* verify the final parent by extended address;
* record Parent Request, Parent Response, Child ID Request, and Child ID
  Response timestamps from OpenThread events and packet captures.

The hardware and simulator runners should use the same outcome classifications
and timing definitions so results remain comparable.
