# Selected-parent OpenThread hook summary

The patch script lives inside the external component:

```text
components/thread_preferred_parent/apply-openthread-selected-parent-hook.py
```

`components/thread_preferred_parent/__init__.py` registers it automatically as a PlatformIO pre-build script using `cg.add_platformio_option("extra_scripts", ...)`.

Manual YAML `platformio_options.extra_scripts` is not needed.

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

It also adds a Parent Response reporting bridge:

```cpp
typedef void (*thread_preferred_parent_parent_response_callback_t)(
    const otThreadParentResponseInfo *aInfo,
    void *aContext
);

extern "C" void thread_preferred_parent_ot_register_parent_response_callback(
    thread_preferred_parent_parent_response_callback_t aCallback,
    void *aContext
);
```

OpenThread calls the reporting bridge from `Mle::Attacher::HandleParentResponse()` after it parses the parent response source RLOC16, ExtAddr, RSSI, priority and link-quality fields. The ESPHome component logs every reported candidate parent.
