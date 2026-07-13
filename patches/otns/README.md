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

## Native CLI controller

Apply after `selected-parent-core.patch`:

```bash
git -C /path/to/openthread apply \
  /path/to/patches/otns/preferred-parent-cli-controller.patch
```

The controller patch adds `prefparent` to the native CLI application and defers
callback work through the application's mainloop. Supported commands are:

```text
prefparent switch <extaddr> multicast
prefparent switch <extaddr> unicast
prefparent status
prefparent clear
```

SHA-256:

```text
6ef066387cbf2f37c9a91996aa4306c947e67020cbaf36c26ce656d2a8033720
```

Phase 5 validates the controller and multicast mode. Although the command
accepts `unicast`, its radio and protocol behavior remains a Phase 6 acceptance
gate.

## Fast unicast Parent Response

Apply after the core and controller patches:

```bash
git -C /path/to/openthread apply \
  /path/to/patches/otns/fast-unicast-parent-response.patch
```

SHA-256:

```text
783990f9ba10968ff5bbd12eb71465409af8f435873e5ec6168748cb3cda8a29
```

The patch adds this compile-time option, disabled by default:

```text
OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE
```

Set it to `1` only for the fast-response FTD build. An IPv6-unicast Parent
Request is then answered immediately and exits the handler without scheduling
the ordinary delayed response. Multicast Parent Requests retain the stock
randomized delay. Leaving the option unset produces the ordinary-response
behavior from the same patched source, which isolates the feature under test.

Phase 7 validates both settings. Phase 8 remains responsible for producing the
final isolated matrix, including a truly unpatched stock source profile.
