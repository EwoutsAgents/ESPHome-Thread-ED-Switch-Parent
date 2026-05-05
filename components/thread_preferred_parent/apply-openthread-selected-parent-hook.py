#!/usr/bin/env python3
"""PlatformIO/ESPHome pre-build script for Thread selected-parent OpenThread hook.

This script is placed inside the ESPHome external component and is registered
from components/thread_preferred_parent/__init__.py. It patches ESP-IDF's
vendored OpenThread core with a small C bridge:

    thread_preferred_parent_ot_request_selected_parent_attach(...)

The patcher intentionally uses tolerant regular expressions because ESPHome /
PlatformIO may install slightly different ESP-IDF/OpenThread revisions.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path
from typing import Callable, Optional

DEFAULT_ROOT = Path.home() / ".platformio/packages/framework-espidf/components/openthread/openthread/src/core"
FRAMEWORK_RELATIVE_CORE = Path("framework-espidf/components/openthread/openthread/src/core")
MARKER = "THREAD_PREFERRED_PARENT_SELECTED_PARENT_HOOK"


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n")


def backup_once(path: Path) -> None:
    backup = path.with_suffix(path.suffix + ".thread-preferred-parent.bak")
    if not backup.exists():
        shutil.copy2(path, backup)


def write_if_changed(path: Path, old: str, new: str, *, dry_run: bool = False) -> str:
    if old == new:
        return "already"
    if not dry_run:
        backup_once(path)
        path.write_text(new)
    return "patched"


def replace_literal(path: Path, old: str, new: str, *, already: str, dry_run: bool = False) -> str:
    text = normalize_newlines(path.read_text())
    old = normalize_newlines(old)
    new = normalize_newlines(new)

    if already in text or new in text:
        return "already"
    if old not in text:
        return "missing"
    return write_if_changed(path, text, text.replace(old, new, 1), dry_run=dry_run)


def replace_regex(
    path: Path,
    pattern: str,
    repl: str | Callable[[re.Match[str]], str],
    *,
    already: str,
    label: str,
    dry_run: bool = False,
) -> str:
    text = normalize_newlines(path.read_text())
    if already in text:
        return "already"

    new, count = re.subn(pattern, repl, text, count=1, flags=re.DOTALL | re.MULTILINE)
    if count == 0:
        print(f"[thread_preferred_parent][detail] no regex match for {label}")
        return "missing"
    return write_if_changed(path, text, new, dry_run=dry_run)


def patch_mle_hpp(root: Path, *, dry_run: bool = False) -> str:
    path = root / "thread/mle.hpp"
    declaration = """    /**
     * Starts targeted attach flow to a selected parent by extended address.
     *
     * This is an ESPHome Thread preferred-parent extension. It reuses
     * OpenThread's internal selected-parent attach mode.
     *
     * @param[in] aExtAddress Extended address of the selected parent candidate.
     *
     * @retval kErrorNone Successfully started selected-parent attach flow.
     * @retval kErrorInvalidState Thread is not attached as a child.
     * @retval kErrorBusy An attach process is already in progress.
     */
    Error AttachToSelectedParent(const Mac::ExtAddress &aExtAddress); // THREAD_PREFERRED_PARENT_SELECTED_PARENT_HOOK
"""
    return replace_literal(
        path,
        "    Error SearchForBetterParent(void);\n",
        "    Error SearchForBetterParent(void);\n\n" + declaration,
        already="AttachToSelectedParent(const Mac::ExtAddress &aExtAddress)",
        dry_run=dry_run,
    )


def patch_attach_method(root: Path, *, dry_run: bool = False) -> str:
    path = root / "thread/mle.cpp"
    method = """
Error Mle::AttachToSelectedParent(const Mac::ExtAddress &aExtAddress)
{
    // THREAD_PREFERRED_PARENT_SELECTED_PARENT_HOOK
    Error error = kErrorNone;

    VerifyOrExit(IsChild(), error = kErrorInvalidState);
    VerifyOrExit(!IsAttaching(), error = kErrorBusy);

    mAttacher.Attach(kSelectedParent);
    mAttacher.GetParentCandidate().SetExtAddress(aExtAddress);

exit:
    return error;
}

"""

    pattern = (
        r"(Error\s+Mle::SearchForBetterParent\s*\(\s*void\s*\)\s*\{.*?\n\}\s*\n\s*)"
        r"(?=bool\s+Mle::IsAttached\s*\()"
    )
    return replace_regex(
        path,
        pattern,
        lambda m: m.group(1).rstrip() + "\n\n" + method,
        already="Mle::AttachToSelectedParent",
        label="Mle::SearchForBetterParent insertion point",
        dry_run=dry_run,
    )


def patch_selected_parent_destination(root: Path, *, dry_run: bool = False) -> str:
    path = root / "thread/mle.cpp"

    replacement = """if (aType == kToSelectedRouter)
    {
#if OPENTHREAD_FTD && OPENTHREAD_CONFIG_PARENT_SEARCH_ENABLE
        TxMessage *messageToCurParent = static_cast<TxMessage *>(message->Clone());
        VerifyOrExit(messageToCurParent != nullptr, error = kErrorNoBufs);

        destination.SetToLinkLocalAddress(Get().mParent.GetExtAddress());
        error = messageToCurParent->SendTo(destination);
        if (error != kErrorNone)
        {
            messageToCurParent->Free();
            ExitNow();
        }
        Log(kMessageSend, kTypeParentRequestToRouters, destination);

        destination.SetToLinkLocalAddress(Get().mParentSearch.GetSelectedParent().GetExtAddress());
#else
        // THREAD_PREFERRED_PARENT_SELECTED_PARENT_HOOK
        // MTD builds do not have ParentSearch, but selected-parent attach still
        // stores the requested candidate in mParentCandidate.
        destination.SetToLinkLocalAddress(mParentCandidate.GetExtAddress());
#endif
    }
    else
    {
        destination.SetToLinkLocalAllRoutersMulticast();
    }"""

    # ESP-IDF 5.5.x / OpenThread compacted or normal formatting.
    pattern = (
        r"#if\s+OPENTHREAD_FTD\s*&&\s*OPENTHREAD_CONFIG_PARENT_SEARCH_ENABLE\s*\n\s*"
        r"if\s*\(\s*aType\s*==\s*kToSelectedRouter\s*\)\s*\{.*?"
        r"destination\.SetToLinkLocalAddress\s*\(\s*Get\s*\(\s*\)\s*\.\s*mParentSearch\s*\.\s*GetSelectedParent\s*\(\s*\)\s*\.\s*GetExtAddress\s*\(\s*\)\s*\)\s*;\s*"
        r"\}\s*else\s*#endif\s*\{\s*destination\.SetToLinkLocalAllRoutersMulticast\s*\(\s*\)\s*;\s*\}"
    )
    return replace_regex(
        path,
        pattern,
        replacement,
        already="mParentCandidate.GetExtAddress()",
        label="selected-router Parent Request destination block",
        dry_run=dry_run,
    )


def patch_accept_selected_parent_without_current_parent_response(root: Path, *, dry_run: bool = False) -> str:
    path = root / "thread/mle.cpp"

    replacement = """case kAnyPartition:
        case kSamePartition:
        case kDowngradeToReed:
        case kBetterParent:

            // Ensure that a Parent Response was received from the
            // current parent to which the device is attached, so
            // that the new parent candidate can be compared with the
            // current parent and confirmed to be preferred.
            VerifyOrExit(mReceivedResponseFromParent);
            break;

        case kSelectedParent:
            // THREAD_PREFERRED_PARENT_SELECTED_PARENT_HOOK
            // The attach flow is already constrained to the explicitly requested
            // candidate, so do not require a comparison response from the current
            // parent before sending the Child ID Request.
            break;"""

    pattern = (
        r"case\s+kAnyPartition\s*:\s*"
        r"case\s+kSamePartition\s*:\s*"
        r"case\s+kDowngradeToReed\s*:\s*"
        r"case\s+kBetterParent\s*:\s*"
        r"case\s+kSelectedParent\s*:\s*"
        r"//\s*Ensure\s+that\s+a\s+Parent\s+Response\s+was\s+received\s+from\s+the.*?"
        r"VerifyOrExit\s*\(\s*mReceivedResponseFromParent\s*\)\s*;\s*break\s*;"
    )
    return replace_regex(
        path,
        pattern,
        replacement,
        already="The attach flow is already constrained to the explicitly requested",
        label="selected-parent current-parent-response bypass",
        dry_run=dry_run,
    )


def patch_thread_api(root: Path, *, dry_run: bool = False) -> str:
    path = root / "api/thread_api.cpp"
    bridge = """
extern "C" bool thread_preferred_parent_ot_request_selected_parent_attach(otInstance *aInstance,
                                                                             const otExtAddress *aPreferredExtAddress)
{
    // THREAD_PREFERRED_PARENT_SELECTED_PARENT_HOOK
    if ((aInstance == nullptr) || (aPreferredExtAddress == nullptr))
    {
        return false;
    }

    return AsCoreType(aInstance).Get<Mle::Mle>().AttachToSelectedParent(AsCoreType(aPreferredExtAddress)) == kErrorNone;
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
        already="thread_preferred_parent_ot_request_selected_parent_attach",
        label="otThreadSearchForBetterParent bridge insertion point",
        dry_run=dry_run,
    )


def apply_patches(root: Path, *, dry_run: bool = False) -> int:
    root = root.expanduser().resolve()
    print(f"[thread_preferred_parent] OpenThread src/core: {root}")

    if not root.exists():
        print(f"[thread_preferred_parent][missing-root] {root}")
        return 1

    patches = [
        ("mle.hpp declaration", root / "thread/mle.hpp", patch_mle_hpp),
        ("mle.cpp AttachToSelectedParent", root / "thread/mle.cpp", patch_attach_method),
        ("mle.cpp selected-router destination", root / "thread/mle.cpp", patch_selected_parent_destination),
        ("mle.cpp selected-parent bypass", root / "thread/mle.cpp", patch_accept_selected_parent_without_current_parent_response),
        ("thread_api.cpp bridge", root / "api/thread_api.cpp", patch_thread_api),
    ]

    rc = 0
    for label, path, func in patches:
        if not path.exists():
            print(f"[thread_preferred_parent][missing-file] {path}")
            rc = 1
            continue
        state = func(root, dry_run=dry_run)
        print(f"[thread_preferred_parent][{state}] {label}: {path}")
        if state == "missing":
            rc = 1

    if rc == 0:
        print("[thread_preferred_parent] OpenThread selected-parent hook is installed.")
    else:
        print("[thread_preferred_parent] Patch did not match this OpenThread revision.")
    return rc


def platformio_package_root() -> Optional[Path]:
    """Return PlatformIO's package dir when running as an extra_script."""
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
