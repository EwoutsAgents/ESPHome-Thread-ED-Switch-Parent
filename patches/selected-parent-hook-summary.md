# Selected-parent OpenThread hook summary

The authoritative patch mechanism for this version is:

```bash
scripts/apply-openthread-selected-parent-hook.py
```

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
