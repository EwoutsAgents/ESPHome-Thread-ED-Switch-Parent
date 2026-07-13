# Native OTNS OpenThread patches

These patches target the Track A OpenThread base selected in Phase 3:

```text
a12ff0d0f54fd41954b45047fcdd08f302731c5f
```

Apply each patch to a separate clean OpenThread worktree. Do not apply them to
the hardware PlatformIO package tree or the OTNS `7874555e...` submodule.

## Selected-parent core

```bash
git -C /path/to/openthread checkout --detach \
  a12ff0d0f54fd41954b45047fcdd08f302731c5f
git -C /path/to/openthread apply \
  /path/to/patches/otns/selected-parent-core.patch
```

`selected-parent-core.patch` contains the functional preferred-parent delta
plus the native-port corrections identified during Phase 4:

- public bridge declarations in `include/openthread/selected_parent.h`;
- internal bridge declarations in `src/core/thread/selected_parent.hpp`;
- initialized target-candidate and fast-discovery state;
- a populated snapshot of the fully validated target Parent Response;
- explicit clear, active-query, and generation APIs;
- native-compatible C-linkage definitions.

SHA-256:

```text
9ac91535050180910552e12e4e0e13c35705108405d2ca2de9fd103ae13cf0e2
```

The patch includes multicast and unicast mechanisms inherited from the hardware
implementation. Phase 4 validates multicast first. Unicast remains outside its
acceptance scope until Phase 6.

The operation state is process-global. This matches OTNS's current execution
model, where each simulated node is a separate native process with one
OpenThread instance. It is not suitable for a multiple-instance OpenThread
process without further refactoring.
