# Selection rules

All groups contain exactly 100 accepted hardware runs.

General requirements:

- Manifest status is `completed`.
- The PCAP and device logs required for the second attach are present.
- The intended variant path was exercised.
- A failed, incomplete, or non-qualifying run is replaced by a singleton top-up rather than counted twice.

Variant-specific rules:

- Stock and Ucast use the completed campaign runs selected for the final n=100 analysis.
- Fast Attach excludes captures missing the recovery attach and uses the recorded three- and four-router singleton replacements.
- Fast Attach Ucast 1 excludes the failed four-router run and uses its successful singleton replacement.
- Stock Low Power accepts only `expected_high_power_replacement`: initial parent at 0 dBm and replacement parent equal to the other 0 dBm router. Low-power replacements and unresolved recoveries are excluded and replaced by qualifying top-ups.

Known timestamp normalization:

- Fast Attach three-router run `20260914-235554-run06` crosses midnight. Its recovery attach occurs after midnight and precedes the pre-midnight attach under naive time-of-day sorting. The canonical table classifies the post-midnight sequence as recovery.
- Fast Attach three-router run `20260914-142411-run01` contains the recovery attach but not the initial attach in the PCAP. Its single complete sequence is classified as recovery using the detach/arm lifecycle evidence.

All excluded paths and reasons are listed in `exclusions.json`.
