# Hardware baselines

This directory separates hardware datasets by preferred-parent implementation.

- `esphome-controller-implementation-20260714-15/` is the reference dataset
  for the original design, where ESPHome owns the selected-parent controller
  and patched OpenThread provides the protocol hooks.
- Future datasets for the design where OpenThread owns the complete mechanism
  should use a sibling directory named
  `openthread-controller-implementation-<date>/`.

Do not combine results from different implementation directories without
identifying the implementation in the comparison.
