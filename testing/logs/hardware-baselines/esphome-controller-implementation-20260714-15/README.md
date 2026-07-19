# ESPHome-controller hardware baseline

This is the canonical hardware baseline for the implementation used before the
preferred-parent controller is moved entirely into OpenThread.

In this implementation:

- ESPHome owns the preferred-parent state machine, callback queue, component
  loop processing, OpenThread lock acquisition, retries, and timeouts.
- Patched OpenThread exposes the selected-parent discovery and continuation
  hooks.
- FastPR routers additionally use the immediate unicast Parent Response patch.

Future OpenThread-controller hardware results must not overwrite or be added to
these campaigns. Store them in a sibling directory under `hardware-baselines/`.

## Experimental scope

- Hardware: ESP32-C6 devices
- Topology: four routers and one child
- Runs: 24 per variant
- Router settling: 300 seconds
- Initial child attachment: 5 seconds
- Observation after parent removal: 360 seconds
- Timing authority: IEEE 802.15.4 PCAP captured by the external sniffer

## Canonical campaigns

| Variant | Campaign directory | PCAP-complete second full attach, mean (SD) |
| --- | --- | ---: |
| Stock | `campaigns/stock-4router-24runs-20260715-173834/` | 765.58 (2.32) ms |
| Multicast | `campaigns/mcast-4router-24runs-20260714-104249/` | 277.71 (122.05) ms |
| Unicast | `campaigns/ucast-4router-24runs-20260714-055321/` | 325.25 (134.48) ms |
| Unicast FastPR | `campaigns/ucast_fastpr-4router-24runs-20260714-153221/` | 51.50 (5.23) ms |

All four hardware summaries contain 24 PCAP-complete second attaches.

Canonical analysis reports:

- `campaigns/stock-4router-24runs-20260715-173834/20260717-170408-stock-4router-24runs-20260715-173834-analysis-report.md`
- `campaigns/mcast-4router-24runs-20260714-104249/20260715-025441-mcast-4router-24runs-20260714-104249-analysis-report.md`
- `campaigns/ucast-4router-24runs-20260714-055321/20260715-025441-ucast-4router-24runs-20260714-055321-analysis-report.md`
- `campaigns/ucast_fastpr-4router-24runs-20260714-153221/20260715-025441-ucast_fastpr-4router-24runs-20260714-153221-analysis-report.md`

## Archived material

Each campaign retains its original:

- Per-run device and supervisor logs
- PCAPNG captures
- Packet and MLE CSV exports
- Test manifests
- Campaign log
- Generated Markdown analysis report

The paired Multicast/Unicast launcher log and the Stock launcher log are under
`launch-logs/`.

Files were moved without rewriting their contents. Absolute paths embedded in
the historical manifests and CSV files therefore identify their original
locations under `testing/logs/`; use paths relative to this directory when
opening the archived files now.

## Comparison rule for the future implementation

At minimum, compare these PCAP-derived second-attach intervals:

1. Parent Request to selected Parent Response
2. Selected Parent Response to Child ID Request
3. Child ID Request to Child ID Response
4. Parent Request to Child ID Response (full attach)

Also report selected-target success separately from final-parent retention.
