#!/usr/bin/env python3
"""Patch ESP-IDF vendored OpenThread with observe-only Parent Response bridge.

This patch is intentionally minimal for stock-observed instrumentation:
- registers a callback bridge for Parent Response notifications
- emits notifications from MLE Parent Response handling

It does NOT add selected-parent attach APIs, steering APIs, or unicast discovery hooks.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path

DEFAULT_ROOT = Path.home() / ".platformio/packages/framework-espidf/components/openthread/openthread/src/core"
FRAMEWORK_RELATIVE_CORE = Path("framework-espidf/components/openthread/openthread/src/core")


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n")


def backup_once(path: Path) -> None:
    backup = path.with_suffix(path.suffix + ".thread-stock-observer.bak")
    if not backup.exists():
        shutil.copy2(path, backup)


def write_if_changed(path: Path, old: str, new: str, *, dry_run: bool = False) -> str:
    if old == new:
        return "already"
    if not dry_run:
        backup_once(path)
        path.write_text(new)
    return "patched"


def replace_regex(path: Path, pattern: str, repl: str | callable, *, already: str, dry_run: bool = False) -> str:
    text = normalize_newlines(path.read_text())
    if already in text:
        return "already"
    new, count = re.subn(pattern, repl, text, count=1, flags=re.DOTALL | re.MULTILINE)
    if count == 0:
        return "missing"
    return write_if_changed(path, text, new, dry_run=dry_run)


def patch_thread_api(root: Path, *, dry_run: bool = False) -> str:
    path = root / "api/thread_api.cpp"
    bridge = """
using thread_stock_observer_parent_response_callback_t = void (*)(const otThreadParentResponseInfo *aInfo, void *aContext);

static thread_stock_observer_parent_response_callback_t sThreadStockObserverParentResponseCallback = nullptr;
static void *sThreadStockObserverParentResponseCallbackContext = nullptr;

extern "C" void thread_stock_observer_ot_register_parent_response_callback(
    thread_stock_observer_parent_response_callback_t aCallback,
    void *aContext)
{
    // THREAD_STOCK_OBSERVER_PARENT_RESPONSE_REPORTING_HOOK
    sThreadStockObserverParentResponseCallback = aCallback;
    sThreadStockObserverParentResponseCallbackContext = aContext;
}

extern "C" void thread_stock_observer_ot_notify_parent_response(const otThreadParentResponseInfo *aInfo)
{
    // THREAD_STOCK_OBSERVER_PARENT_RESPONSE_REPORTING_HOOK
    if ((sThreadStockObserverParentResponseCallback != nullptr) && (aInfo != nullptr))
    {
        sThreadStockObserverParentResponseCallback(aInfo, sThreadStockObserverParentResponseCallbackContext);
    }
}

"""
    pattern = (
        r"(otError\s+otThreadSearchForBetterParent\s*\(\s*otInstance\s*\*\s*aInstance\s*\)\s*"
        r"\{\s*return\s+AsCoreType\s*\(\s*aInstance\s*\)\s*\.\s*Get\s*<\s*Mle::Mle\s*>\s*\(\s*\)\s*\.\s*SearchForBetterParent\s*\(\s*\)\s*;\s*\}\s*)"
    )
    return replace_regex(
        path,
        pattern,
        lambda m: m.group(1).rstrip() + "\n\n" + bridge,
        already="thread_stock_observer_ot_register_parent_response_callback",
        dry_run=dry_run,
    )


def patch_mle_declaration(root: Path, *, dry_run: bool = False) -> str:
    path = root / "thread/mle.cpp"
    text = normalize_newlines(path.read_text())
    if 'thread_stock_observer_ot_notify_parent_response' in text:
        return "already"

    include_old = '#include "utils/static_counter.hpp"\n'
    include_new = (
        '#include "utils/static_counter.hpp"\n\n'
        '#include <openthread/thread.h>\n\n'
        'extern "C" void thread_stock_observer_ot_notify_parent_response(const otThreadParentResponseInfo *aInfo);\n'
        '// THREAD_STOCK_OBSERVER_PARENT_RESPONSE_REPORTING_HOOK\n'
    )

    if include_old not in text:
        return "missing"

    return write_if_changed(path, text, text.replace(include_old, include_new, 1), dry_run=dry_run)


def patch_mle_notify_call(root: Path, *, dry_run: bool = False) -> str:
    path = root / "thread/mle.cpp"
    text = normalize_newlines(path.read_text())
    if "thread_stock_observer_ot_notify_parent_response(&parentinfo)" in text:
        return "already"

    call_block = """
    {
        otThreadParentResponseInfo parentinfo;
        parentinfo.mExtAddr = extAddress;
        parentinfo.mRloc16 = sourceAddress;
        parentinfo.mRssi = rss;
        parentinfo.mPriority = connectivityTlv.GetParentPriority();
        parentinfo.mLinkQuality3 = connectivityTlv.GetLinkQuality3();
        parentinfo.mLinkQuality2 = connectivityTlv.GetLinkQuality2();
        parentinfo.mLinkQuality1 = connectivityTlv.GetLinkQuality1();
        parentinfo.mIsAttached = Get<Mle>().IsAttached();
        thread_stock_observer_ot_notify_parent_response(&parentinfo);
    }
"""

    pattern = (
        r"(#if\s+OPENTHREAD_CONFIG_MLE_PARENT_RESPONSE_CALLBACK_API_ENABLE\s*\n"
        r"\s*if\s*\(\s*mParentResponseCallback\.IsSet\s*\(\s*\)\s*\)\s*\{.*?"
        r"mParentResponseCallback\.Invoke\s*\(\s*&parentinfo\s*\)\s*;\s*\}\s*\n"
        r"#endif\s*)"
    )

    result = replace_regex(
        path,
        pattern,
        lambda m: m.group(1).rstrip() + "\n" + call_block,
        already="thread_stock_observer_ot_notify_parent_response(&parentinfo)",
        dry_run=dry_run,
    )
    if result != "missing":
        return result

    return replace_regex(
        path,
        r"(aRxInfo\.mClass\s*=\s*RxInfo::kAuthoritativeMessage\s*;)",
        lambda m: call_block + "\n    " + m.group(1),
        already="thread_stock_observer_ot_notify_parent_response(&parentinfo)",
        dry_run=dry_run,
    )


def detect_root(explicit_root: str | None) -> Path:
    candidates = []
    if explicit_root:
        candidates.append(Path(explicit_root).expanduser())

    project_dir = Path(__file__).resolve().parents[2]
    candidates.append(project_dir / FRAMEWORK_RELATIVE_CORE)
    candidates.append(DEFAULT_ROOT)

    env_core = os.environ.get("PROJECT_PACKAGES_DIR")
    if env_core:
        candidates.append(Path(env_core) / FRAMEWORK_RELATIVE_CORE)

    for candidate in candidates:
        if (candidate / "api/thread_api.cpp").exists() and (candidate / "thread/mle.cpp").exists():
            return candidate

    raise FileNotFoundError("Could not locate OpenThread src/core root")


def main() -> int:
    parser = argparse.ArgumentParser(description="Patch OpenThread for stock-observed parent-response reporting")
    parser.add_argument("--root", help="OpenThread src/core root")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = detect_root(args.root)

    steps = {
        "thread_api": patch_thread_api(root, dry_run=args.dry_run),
        "mle_decl": patch_mle_declaration(root, dry_run=args.dry_run),
        "mle_call": patch_mle_notify_call(root, dry_run=args.dry_run),
    }

    for name, state in steps.items():
        print(f"[thread_stock_observer] {name}: {state}")

    if any(state == "missing" for state in steps.values()):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
