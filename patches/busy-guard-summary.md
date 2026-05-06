# Busy guard / handoff diagnostics

This revision adds two runtime-only safety/diagnostic improvements:

- New switch requests are ignored while a parent switch is already active. This prevents a second Home Assistant button press from resetting discovery while selected-parent attach is in progress.
- A single discovery-to-attach handoff line is logged before selected-parent attach starts. It reports elapsed discovery time, buffered Parent Response count, and target-match count, and clarifies that in-flight Parent Responses may still be logged after attach begins.

No YAML options were added for this change.
