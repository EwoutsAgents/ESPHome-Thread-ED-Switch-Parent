# Phase 11 validation ladder

## Result

Phase 11 is complete. Validation progressed from isolated binaries and native
CLI behavior through controlled classifications, the complete topology matrix,
small repeated campaigns, and a preliminary four-router hardware comparison.

No ESPHome hardware firmware source was changed in this phase.

## Gates

1. **Build:** the four timestamped Phase 10 binaries remain executable and
   match their recorded SHA-256 fingerprints. Stock artifacts contain no
   `PREFPARENT` marker.
2. **CLI:** real native tests covered idle/active status, invalid target, invalid
   mode, valid request, busy rejection, clear, and cleared status.
3. **Core protocol:** all nine directed topology/variant smoke runs emitted a
   complete Parent Request through Child ID Response sequence and reached the
   requested target.
4. **Fast response:** Phase 7 matched-seed packet evidence remains valid; Phase
   11 repeated timing also showed the fast response path as a separate, stable
   latency population.
5. **Runner:** setup labels and every terminal directed classification now use
   deterministic pure helpers covered by unit tests.
6. **Matrix:** stock, multicast, unicast, and fast-response unicast passed for
   two, three, and four routers.
7. **Repeated:** ten two-router runs per directed variant all reached their
   target with complete timing. The repeated runner now forwards binary-profile
   declarations for directed scenarios.
8. **Hardware comparison:** one four-router run per directed variant was
   compared using identical semantic timing boundaries with separately labeled
   PCAP and RFSIM timing sources.

## Repeated two-router results

| Variant | Target reached | Mean full attach (ms) | Sample SD (ms) |
| --- | ---: | ---: | ---: |
| multicast | 10/10 | 220.316 | 176.997 |
| unicast | 10/10 | 324.680 | 130.869 |
| fast unicast | 10/10 | 20.416 | 2.833 |

## Four-router comparison

| Variant | Hardware PCAP full attach (ms) | OTNS native-event full attach (ms) |
| --- | ---: | ---: |
| multicast | 306 | 246.560 |
| unicast | 106 | 246.304 |
| fast unicast | 48 | 18.240 |

Hardware sources:

- `testing/logs/mcast/20260713-214915`;
- `testing/logs/ucast/20260713-220201`;
- `testing/logs/ucast_fastpr-4router-1runs-20260713-221414/20260713-221414-run01`.

The child logs confirm that each hardware run reached the selected extended
address. The comparison is preliminary: targets were independently selected,
there is one four-router sample per variant, and OTNS does not model ESP32-C6
execution or the physical test environment cycle-accurately.

The detailed OTNS gate evidence is in `OTNS-MAPS/docs/validation_ladder.md` on
the Phase 11 branch.

## Exit assessment

The Phase 11 gate is met. Phase 12 can now package reproducible commands,
scenario copies, manifests, source revisions, binary hashes, and representative
result artifacts. A larger four-router paired campaign remains future
experimental work rather than a prerequisite for packaging the validated
integration.
