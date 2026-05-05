# Selected-parent OpenThread hook summary

The patch script now lives inside the external component:

```text
components/thread_preferred_parent/apply-openthread-selected-parent-hook.py
```

`components/thread_preferred_parent/__init__.py` registers it automatically as a PlatformIO pre-build script using `cg.add_platformio_option("extra_scripts", ...)`.

Manual YAML `platformio_options.extra_scripts` is no longer needed.

The script modifies ESP-IDF's vendored OpenThread core under `src/core`:

- `thread/mle.hpp`
- `thread/mle.cpp`
- `api/thread_api.cpp`

It adds `Mle::AttachToSelectedParent(const Mac::ExtAddress &)` and exports:

```cpp
extern "C" bool thread_preferred_parent_ot_request_selected_parent_attach(
    otInstance *aInstance,
    const otExtAddress *aPreferredExtAddress
);
```

The ESPHome component resolves that function as a weak symbol at runtime.
