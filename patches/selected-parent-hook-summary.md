# OpenThread patch summary

This component auto-patches ESP-IDF's vendored OpenThread core during the PlatformIO build.

The patch adds:

1. A parent-response callback bridge so ESPHome can log every received MLE Parent Response.
2. A discovery-only bridge that starts multicast Parent Request discovery without detaching from the current parent.
3. A selected-parent attach bridge that forces an attach to a chosen parent extended address after the target was observed.

The discovery-only path prevents the disruptive selected-parent attach from being attempted when the requested parent is not present.
