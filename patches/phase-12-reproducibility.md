# Phase 12 reproducibility and artifacts

## Result

Phase 12 is complete. OTNS-MAPS now exports self-describing directed
parent-switch artifacts, verifies their payload integrity, assigns explicit
per-run simulator seeds, and carries a committed reference collection.

No ESPHome hardware firmware source changed in this phase.

## Artifact contents

Every directed run bundle now contains:

- the exact scenario YAML and its SHA-256;
- sampled node-state and preferred-parent event CSVs;
- summary JSON with artifact-relative payload references;
- raw OTNS node logs;
- replay and normalized replay metadata;
- `ParentRank` CSV when events are present;
- OpenThread, OTNS, OTNS-MAPS, and firmware-patch repository provenance;
- node executable profiles, paths, and SHA-256 fingerprints;
- target-selection and OTNS simulator seeds;
- exact runner invocation and build source;
- README, manifest, and complete payload checksum inventory.

Repeated experiments add an aggregate summary and recursively verifiable run
bundles. `--otns-seed-base` assigns deterministic sequential simulator seeds.

## Verification

`OTNS-MAPS/scripts/verify_artifact.py` checks the payload inventory, file
hashes, scenario fingerprint, required files, relative references,
summary/manifest agreement, complete directed timing, nested repeated runs,
and locally available executable fingerprints.

Unit tests cover valid artifacts, payload tampering, unsafe absolute summary
references, and deterministic repeated-seed command construction.

## Reference collection

The committed OTNS-MAPS collection is:

```text
results/directed_parent_switch_phase12/20260714-002000-experiment/
```

It contains:

- one four-router multicast bundle: 441.320 ms full attach;
- one four-router unicast bundle: 441.064 ms full attach;
- one four-router fast-response bundle: 19.200 ms full attach;
- a three-run two-router fast-response experiment using OTNS seeds 3221–3223,
  with full attaches of 19.200, 25.600, and 19.520 ms.

All six runs reached their requested targets with complete native timing.

## Clean reproduction

A fresh OTNS-MAPS clone verified the complete committed collection. A new
four-router fast-response run from that checkout, using OTNS seed 3214,
reproduced the same target, classification, executable fingerprints, and full
timing decomposition as the reference:

```text
Parent Request -> Parent Response      9.072 ms
Parent Response -> Child ID Request    0.000 ms
Child ID Request -> Child ID Response 10.128 ms
Full attach                            19.200 ms
```

## Known limits

- The artifacts fingerprint binaries but do not commit the large executables.
- The OTNS checkout reports a modified OpenThread submodule; the packaged
  binaries came from the isolated Track A source and are identified by hash.
- Current binaries emitted no `ParentRank` events, so no ranking CSV appears in
  this collection.
- OTNS event timing and hardware PCAP timing remain semantically comparable,
  not cycle-accurate or radio-equivalent.

Build, execution, layout, verification, and timing policy are documented in
`OTNS-MAPS/docs/reproducible_artifacts.md`.
