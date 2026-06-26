#!/usr/bin/env python3
"""Patch ESP-IDF's vendored OpenThread core for fast unicast Parent Responses.

This is a router-side OpenThread behavior patch. When this component is
enabled, the source patch itself forces the fast-path macro on in `mle_ftd.cpp`
so the OpenThread component build cannot silently miss the define.
"""

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path
from typing import Optional

DEFAULT_ROOT = Path.home() / ".platformio/packages/framework-espidf/components/openthread/openthread/src/core"
FRAMEWORK_RELATIVE_CORE = Path("framework-espidf/components/openthread/openthread/src/core")


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n")


def backup_once(path: Path) -> None:
    backup = path.with_suffix(path.suffix + ".thread-fast-unicast-parent-response.bak")
    if not backup.exists():
        shutil.copy2(path, backup)


def write_if_changed(path: Path, old: str, new: str, *, dry_run: bool = False) -> str:
    if old == new:
        return "already"
    if not dry_run:
        backup_once(path)
        path.write_text(new)
    return "patched"


def patch_unicast_parent_response_fastpath(root: Path, *, dry_run: bool = False) -> str:
    path = root / "thread/mle_ftd.cpp"
    text = normalize_newlines(path.read_text())

    macro_old = '#include "instance/instance.hpp"\n'
    macro_new = """#include "instance/instance.hpp"

#ifndef OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE
#define OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE 1
#endif
"""
    text_after_macro = text
    macro_existing = """#ifndef OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE
#define OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE 0
#endif
"""

    if macro_existing in text_after_macro:
        text_after_macro = text_after_macro.replace(macro_existing, macro_new.split('\n', 1)[1], 1)
    elif "OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE" not in text:
        if macro_old not in text:
            return "missing"
        text_after_macro = text.replace(macro_old, macro_new, 1)

    old_decl = """    DeviceMode         mode;
    uint32_t           delay;
    ParentResponseInfo info;
"""
    new_decl = """    DeviceMode         mode;
    uint32_t           delay;
    bool               isIpv6UnicastRequest;
    ParentResponseInfo info;
"""
    if "bool               isIpv6UnicastRequest;" not in text_after_macro:
        if old_decl not in text_after_macro:
            return "missing"
        text_after_macro = text_after_macro.replace(old_decl, new_decl, 1)

    old_delay = """    delay = GenerateRandomDelay(!ScanMaskTlv::IsEndDeviceFlagSet(scanMask) ? kParentResponseMaxDelayRouters
                                                                           : kParentResponseMaxDelayAll);
"""
    new_delay = """    isIpv6UnicastRequest = !aRxInfo.mMessageInfo.GetSockAddr().IsMulticast();

    delay = !ScanMaskTlv::IsEndDeviceFlagSet(scanMask) ? kParentResponseMaxDelayRouters
                                                       : kParentResponseMaxDelayAll;

#if OPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE
    if (isIpv6UnicastRequest)
    {
        // THREAD_FAST_UNICAST_PARENT_RESPONSE_COMPONENT
        // RxInfo exposes the IPv6 destination but not the original IEEE
        // 802.15.4 destination address, so this fast path is gated on the
        // IPv6 layer only.
        delay = 0;
    }
    else
    {
        delay = GenerateRandomDelay(delay);
    }
#else
    delay = GenerateRandomDelay(delay);
#endif
"""
    if old_delay in text_after_macro:
        text_after_macro = text_after_macro.replace(old_delay, new_delay, 1)
    elif "THREAD_FAST_UNICAST_PARENT_RESPONSE_COMPONENT" not in text_after_macro:
        return "missing"

    return write_if_changed(path, text, text_after_macro, dry_run=dry_run)


def apply_patches(root: Path, *, dry_run: bool = False) -> int:
    root = root.expanduser().resolve()
    print(f"[thread_fast_unicast_parent_response] OpenThread src/core: {root}")

    if not root.exists():
        print(f"[thread_fast_unicast_parent_response][missing-root] {root}")
        return 1

    path = root / "thread/mle_ftd.cpp"
    if not path.exists():
        print(f"[thread_fast_unicast_parent_response][missing-file] {path}")
        return 1

    state = patch_unicast_parent_response_fastpath(root, dry_run=dry_run)
    print(f"[thread_fast_unicast_parent_response][{state}] mle_ftd.cpp unicast Parent Response fast path: {path}")
    if state == "missing":
        print("[thread_fast_unicast_parent_response] Required patch did not match this OpenThread revision.")
        return 1

    print("[thread_fast_unicast_parent_response] Fast unicast Parent Response patch is installed.")
    return 0


def platformio_package_root() -> Optional[Path]:
    try:
        Import("env")  # type: ignore[name-defined]  # noqa: F821
    except Exception:
        return None

    packages_dir = env.subst("$PROJECT_PACKAGES_DIR")  # type: ignore[name-defined]  # noqa: F821
    if not packages_dir or "$" in packages_dir:
        packages_dir = os.environ.get("PLATFORMIO_PACKAGES_DIR", "")
    if not packages_dir:
        return None
    return Path(packages_dir)


def run_as_platformio_script() -> Optional[int]:
    packages_dir = platformio_package_root()
    if packages_dir is None:
        return None

    root = packages_dir / FRAMEWORK_RELATIVE_CORE
    rc = apply_patches(root)
    if rc != 0:
        raise SystemExit(rc)
    return rc


def main() -> int:
    parser = argparse.ArgumentParser(description="Patch ESP-IDF's vendored OpenThread core.")
    parser.add_argument("root", nargs="?", type=Path, default=DEFAULT_ROOT, help="OpenThread src/core root to patch")
    parser.add_argument("--dry-run", action="store_true", help="Report what would be patched without writing files")
    args = parser.parse_args()
    return apply_patches(args.root, dry_run=args.dry_run)


_pio_rc = run_as_platformio_script()

if __name__ == "__main__":
    if _pio_rc is not None:
        raise SystemExit(_pio_rc)
    raise SystemExit(main())
