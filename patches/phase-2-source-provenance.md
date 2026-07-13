# Phase 2 source provenance

## Result

The hardware and simulation source lines are pinned to exact commits and
reproducible patch hashes.

The hardware builds use ESPHome 2026.4.5 with pioarduino PlatformIO release
`55.03.38-1` and pioarduino ESP-IDF `v5.5.4`. That tree vendors OpenThread:

```text
a12ff0d0f54fd41954b45047fcdd08f302731c5f
```

The simulation source is pinned to:

```text
OTNS:       099a6c26cb1d2b8749d3171d5cdd8597fc71049c
OpenThread: 7874555efb1772bad66049ab06a78a2ce0c925f3
OTNS-MAPS:  45ab9cf71891ff323cfce80f9b8c6546ef3b97af
```

The OTNS OpenThread commit descends from the ESP-IDF OpenThread commit by 830
commits. The machine-readable record is
[phase-2.json](provenance/phase-2.json).

## Hardware build chain

The generated stock-child `platformio.ini` records:

- ESPHome `2026.4.5`;
- `pioarduino/platform-espressif32` release `55.03.38-1`;
- `pioarduino/esp-idf` release `v5.5.4`.

Installed metadata reports platform package `55.03.38`, framework package
`3.50504`, and ESP-IDF `5.5.4`.

### Platform archive

```text
https://github.com/pioarduino/platform-espressif32/releases/download/55.03.38-1/platform-espressif32.zip
SHA-256: 54ca527d9920815d8fef77319b9c35679cf71c0299a3a9bf4ad8ae33a6cd95c4
```

### ESP-IDF archive

```text
https://github.com/pioarduino/esp-idf/releases/download/v5.5.4/esp-idf-v5.5.4.tar.xz
SHA-256: b27b43152577f4013e93c89b4d33cd049a47fe79b903a67add2a3d49f95a0cc8
```

The pioarduino `v5.5.4` lightweight tag points to:

```text
8de41af2dbb81bc443a8d7986ebd152f82e10bba
```

The Espressif upstream `v5.5.4` annotated tag resolves as:

```text
tag object: eebd1d67000d55fcf392711763de30bb3c8ddbcd
commit:     735507283d5b2f9fb363a1901172dbd9e847945d
```

Both ESP-IDF trees point `components/openthread/openthread` at:

```text
a12ff0d0f54fd41954b45047fcdd08f302731c5f
```

This removes ambiguity between the pioarduino distribution and Espressif
upstream for the OpenThread experiment source.

## Hardware OpenThread verification

Repository:

```text
https://github.com/espressif/openthread
```

Commit metadata:

```text
a12ff0d0f54fd41954b45047fcdd08f302731c5f
2025-12-22T13:55:41-08:00
[csl] account for accuracy drift for next CSL window (#11602)
```

A clean checkout was compared with the unpacked stock framework:

- 2,199 tracked paths examined;
- 2,168 packaged tracked blobs present and byte-identical;
- 31 paths omitted by release packaging;
- zero mismatched blobs.

Omissions are repository metadata, GitHub workflows, ignore/configuration files,
and the nested `third_party/mbedtls/repo` gitlink. No packaged tracked source
blob differed from the clean commit.

The canonical hardware patches therefore use `a12ff0d0…` as their verified
source baseline.

## Simulation source chain

### OTNS

```text
Repository: https://github.com/openthread/ot-ns
Commit:    099a6c26cb1d2b8749d3171d5cdd8597fc71049c
Date:      2026-07-03T12:30:38-07:00
```

The superproject tree records OpenThread gitlink:

```text
7874555efb1772bad66049ab06a78a2ce0c925f3
```

The OTNS superproject has no direct tracked-file changes. Its dirty status is
caused only by the modified OpenThread submodule described below.

### OTNS OpenThread

```text
Repository: https://github.com/openthread/openthread
Commit:    7874555efb1772bad66049ab06a78a2ce0c925f3
Date:      2026-06-22T17:32:35-07:00
Subject:   [mle] separate router and leader upgrade thresholds (#13227)
```

The ESP-IDF commit `a12ff0d0…` is its merge base and ancestor. Track B is
therefore a forward semantic port across 830 OpenThread commits.

### OTNS-MAPS

```text
Repository: https://github.com/EwoutsAgents/OTNS-MAPS
Commit:    45ab9cf71891ff323cfce80f9b8c6546ef3b97af
Date:      2026-07-13T15:22:30+02:00
Subject:   Add static parent removal scenarios
```

The OTNS-MAPS worktree was clean during this audit.

## ParentRank preservation

The only direct modification in the OTNS OpenThread worktree is:

```text
src/core/thread/mle.cpp | 96 insertions, 11 deletions
```

It instruments ordered parent-comparison criteria with stable `ParentRank:`
records. Early `VerifyOrExit` expressions are replaced by equivalent explicit
branches so the deciding criterion can be logged. Partition decisions are also
logged.

The independent artifact is
[otns-parent-rank.patch](canonical/otns-parent-rank.patch).

SHA-256:

```text
2c3858be0dd519877ec38e2bb48ba4c5a3ac0dbd1bf4fd2da8b83a362d73818b
```

It was applied to a clean `7874555e…` checkout. The resulting
`src/core/thread/mle.cpp` matched the working OTNS submodule byte-for-byte.

The preferred-parent port must be applied separately. Reapply `ParentRank` only
after the functional port passes, resolving overlapping `mle.cpp` hunks without
changing its comparison semantics.

## Canonical patch hashes

| Patch | Base | SHA-256 |
| --- | --- | --- |
| `preferred-parent-functional.patch` | `a12ff0d0…` | `aa59c5566bcbacad5ffeb8328d67d09bb508cd9404987b985e718306f36f27c8` |
| `preferred-parent-diagnostics.patch` | functional tree | `435a1592962d906ae94e5a4e2b984fc30afec314b11ed7aee7c45861217c290e` |
| `fast-unicast-parent-response.patch` | full preferred-parent tree | `5f371f803e77fcaf86c2e0f6971fc651ef5a08b3329fc9ab149ec38693591ea8` |
| `otns-parent-rank.patch` | `7874555e…` | `2c3858be0dd519877ec38e2bb48ba4c5a3ac0dbd1bf4fd2da8b83a362d73818b` |

## Clean-checkout recipes

### Hardware OpenThread

```bash
git clone https://github.com/espressif/openthread.git openthread-espidf-5.5.4
git -C openthread-espidf-5.5.4 checkout --detach \
  a12ff0d0f54fd41954b45047fcdd08f302731c5f
```

Apply from the directory containing `src/core`:

```bash
patch -p1 < preferred-parent-functional.patch
patch -p1 < preferred-parent-diagnostics.patch
patch -p1 < fast-unicast-parent-response.patch  # fast-response variant only
```

### OTNS

```bash
git clone https://github.com/openthread/ot-ns.git ot-ns
git -C ot-ns checkout --detach \
  099a6c26cb1d2b8749d3171d5cdd8597fc71049c
git -C ot-ns submodule update --init openthread
test "$(git -C ot-ns/openthread rev-parse HEAD)" = \
  "7874555efb1772bad66049ab06a78a2ce0c925f3"
patch -d ot-ns/openthread -p1 < otns-parent-rank.patch
```

### OTNS-MAPS

```bash
git clone https://github.com/EwoutsAgents/OTNS-MAPS.git OTNS-MAPS
git -C OTNS-MAPS checkout --detach \
  45ab9cf71891ff323cfce80f9b8c6546ef3b97af
```

## Phase 2 exit assessment

A clean checkout can reproduce the hardware OpenThread baseline, canonical
hardware deltas, OTNS and its OpenThread submodule, independent `ParentRank`
instrumentation, and OTNS-MAPS.

Phase 2 is complete. Phase 3 can test `a12ff0d0…` with RFSIM and choose the
native OpenThread base.
