# Stock Test Summary - 2026-06-01

Runs covered:

- `20260601-115057`
- `20260601-121212`
- `20260601-121953`
- `20260601-122733`
- `20260601-123513`

## Aggregate

- All 5 runs completed with child log, sniffer log, pcap, and manifest present.
- Attach 1 total time was tightly grouped: average `765.0 ms`, range `762-768 ms`.
- Attach 2 total time was also tightly grouped: average `762.6 ms`, range `762-764 ms`.
- Attach 1 phase averages:
  - parent request -> response: `255.6 ms`
  - parent response -> child ID request: `495.4 ms`
  - child ID request -> response: `14.0 ms`
- Attach 2 phase averages:
  - parent request -> response: `238.0 ms`
  - parent response -> child ID request: `511.2 ms`
  - child ID request -> response: `13.4 ms`
- Each run showed exactly `64` failed TX attempts.
- In every run, the failed TX attempts were concentrated into 4 consecutive sequence numbers with `16` failures each.
- The dominant failed destination was always the first parent, with `48-53` failed attempts against that parent.

## Per Run

### `20260601-115057`

- Attach 1: parent `767d521b8f1ba668` (`0x5400`) in `765 ms`
  - `419 ms` + `332 ms` + `14 ms`
- Attach 2: parent `1284af330ed03bb3` (`0xac00`) in `762 ms`
  - `66 ms` + `683 ms` + `13 ms`
- Failed TX: `64` total
  - seqnums: `10`, `11`, `12`, `13`
  - dominant dst: `767d521b8f1ba668` (`53`)

### `20260601-121212`

- Attach 1: parent `da903c040ae68c9c` (`0xe000`) in `767 ms`
  - `319 ms` + `433 ms` + `15 ms`
- Attach 2: parent `960c79571efb5f08` (`0x3c00`) in `762 ms`
  - `92 ms` + `657 ms` + `13 ms`
- Failed TX: `64` total
  - seqnums: `152`, `153`, `154`, `155`
  - dominant dst: `da903c040ae68c9c` (`52`)

### `20260601-121953`

- Attach 1: parent `1ab1863b65df33ed` (`0x7c00`) in `768 ms`
  - `25 ms` + `729 ms` + `14 ms`
- Attach 2: parent `c682d39f01310b69` (`0x4c00`) in `763 ms`
  - `297 ms` + `452 ms` + `14 ms`
- Failed TX: `64` total
  - seqnums: `153`, `154`, `155`, `156`
  - dominant dst: `1ab1863b65df33ed` (`53`)

### `20260601-122733`

- Attach 1: parent `e61cac857cc82d78` (`0x4800`) in `762 ms`
  - `423 ms` + `326 ms` + `13 ms`
- Attach 2: parent `3a08e1d359972937` (`0xf800`) in `764 ms`
  - `317 ms` + `433 ms` + `14 ms`
- Failed TX: `64` total
  - seqnums: `121`, `122`, `123`, `124`
  - dominant dst: `e61cac857cc82d78` (`52`)

### `20260601-123513`

- Attach 1: parent `a605ee962ad7a308` (`0x7800`) in `763 ms`
  - `92 ms` + `657 ms` + `14 ms`
- Attach 2: parent `b28ac9bd69f86000` (`0xc800`) in `762 ms`
  - `418 ms` + `331 ms` + `13 ms`
- Failed TX: `64` total
  - seqnums: `220`, `221`, `222`, `223`
  - dominant dst: `a605ee962ad7a308` (`48`)

## Takeaways

- The parent switch behavior is highly repeatable. Total reattach time stayed within `2 ms` across all five runs.
- The main variability is not the total attach time. It moves between:
  - a slower parent request -> response phase, or
  - a slower parent response -> child ID request phase.
- The final child ID request -> response phase is effectively constant at `13-15 ms`.
- The repeated `64` failed TX attempts look structural rather than random because the total, the retry ceiling, and the 4-seqnum pattern repeated in every run.
