# Phase 8 native binary matrix

## Result

Phase 8 is complete. Four native OTNS executables were built from three fully
independent OpenThread clones and separate CMake build trees:

```text
openthread-variants/
├── stock/
│   ├── source/
│   └── build/
├── preferred-parent/
│   ├── source/
│   └── build/
├── preferred-parent-fastpr/
│   ├── source/
│   └── build/
└── artifacts/
    ├── stock-mtd-pps-off/ot-cli-mtd
    ├── preferred-parent-mtd-pps-off/ot-cli-mtd
    ├── stock-ftd/ot-cli-ftd
    └── fastpr-ftd/ot-cli-ftd
```

The generated ELF binaries are local build artifacts and are not committed.
Their hashes, sizes, configuration, and source composition are recorded below
and in `patches/provenance/phase-8.json`.

## Reproducible build driver

`scripts/build_otns_native_variants.sh` performs the complete procedure. It:

1. refuses to reuse an existing output root;
2. creates each source profile with an independent `--no-hardlinks` clone;
3. checks out OpenThread `a12ff0d0f54fd41954b45047fcdd08f302731c5f`;
4. initializes recursive submodules at their pinned commits;
5. applies only the patch series assigned to that profile;
6. builds in a profile-specific CMake directory with warnings as errors;
7. targets only `ot-cli-mtd` and `ot-cli-ftd`;
8. publishes and fingerprints the four logical artifacts.

The output directory must be new for every invocation. This intentionally
requires an explicit cleanup or a different path after an interrupted build,
rather than silently accepting uncertain source state.

## Source composition

The `stock` clone remained clean at the pinned base revision. The other clones
used these patch sets:

- `preferred-parent`: selected-parent core plus native CLI controller;
- `preferred-parent-fastpr`: the same patches plus fast unicast Parent Response.

This retains the hardware campaign's variant-level patch composition. The fast
source profile therefore contains the preferred-parent facilities even though
its published artifact is the FTD router executable.

All profiles set `OPENTHREAD_CONFIG_PARENT_SEARCH_ENABLE=0`, which disables PPS.
Only the fast profile sets
`OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE=1`.
No profile contains the optional `ParentRank` instrumentation.

## Artifact fingerprints

| Logical profile | Bytes | SHA-256 |
| --- | ---: | --- |
| `stock-mtd-pps-off/ot-cli-mtd` | 33,447,576 | `a088b7da5647607e712f5c79fa022d6f428b327ef5de66bc218b55f88d137e85` |
| `preferred-parent-mtd-pps-off/ot-cli-mtd` | 33,512,416 | `d780450640cc79657b00811cb289842b829a2d131a1e8fef062dd047d0adfb1b` |
| `stock-ftd/ot-cli-ftd` | 46,964,400 | `a0955043e842d1c75b679d50d93a4a2870e6ed3fefafefafc8b9a5370c7832e2` |
| `fastpr-ftd/ot-cli-ftd` | 47,041,328 | `391b2837e893878d8b3e3cfbf70880c2ef3a569a675aaad19c9407e03b380f5d` |

These Debug-build hashes identify this exact build. Absolute debug paths can
make hashes differ when rebuilding in another output location, so provenance
must retain the source revision, patch hashes, flags, and tool versions rather
than treating SHA-256 equality across machines as the sole reproducibility
test.

## Toolchain and target scope

The successful builds used:

- GNU C/C++ 13.3.0;
- CMake 3.28.3;
- Ninja 1.13.1;
- x86-64 Linux;
- OTNS/RFSIM repository commit
  `099a6c26cb1d2b8749d3171d5cdd8597fc71049c`.

The RFSIM build enables its normal Debug options and
`OT_COMPILE_WARNING_AS_ERROR=ON`. The driver explicitly targets `ot-cli-mtd`
and `ot-cli-ftd`. The default all-target graph also tries to link unrelated
radio/RCP executables, which are incompatible with this older Track A
OpenThread revision's exported API. Their failure does not affect either CLI
node binary, but excluding them makes the intended build boundary explicit.

## Concurrent runtime smoke test

OTNS seed `2802` created four nodes in one simulator process, assigning an
explicit executable to each `add` command:

- Node 1: stock FTD;
- Node 2: fast-response FTD;
- Node 3: stock MTD;
- Node 4: preferred-parent MTD.

All four native node processes started and remained responsive. The two stock
nodes returned `Error 35: InvalidCommand` for `prefparent status`. Both patched
nodes returned the structured idle status event. The preferred-parent MTD and
both stock nodes reached child state; the fast-response FTD was leader when the
probe was taken.

This proves that contradictory source variants can coexist in one OTNS run and
that their process-local OpenThread globals and CLI registrations do not leak
between nodes.

## Exit assessment

The Phase 8 exit criterion is met:

- the four required logical profiles build successfully;
- every profile has isolated source and build state;
- stock artifacts come from an unmodified OpenThread checkout;
- manifest data uniquely identifies each executable and its composition;
- PPS, fast-response, and `ParentRank` settings are explicit;
- all four binaries execute concurrently with the expected capability split.

Phase 9 can consume these paths and hashes while adding deterministic directed
parent-switch scenarios to OTNS-MAPS.
