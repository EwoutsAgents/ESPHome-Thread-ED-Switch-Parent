#!/usr/bin/env python3
"""Patch ESP-IDF's vendored OpenThread core with a selected-parent attach hook.

This follows the same strategy as ESPHome-biparental-ED:

1. Add Mle::AttachToSelectedParent(const Mac::ExtAddress &).
2. Reuse OpenThread's internal kSelectedParent attach mode.
3. For MTD builds, send the selected-parent Parent Request directly to the
   target parent's link-local address derived from its extended address.
4. Export a small C bridge that ESPHome can call through a weak symbol:

       thread_preferred_parent_ot_request_selected_parent_attach(...)

Default target root:

    ~/.platformio/packages/framework-espidf/components/openthread/openthread/src/core

Pass a different root as the first argument if your ESPHome/PlatformIO cache is
elsewhere, for example:

    python3 scripts/apply-openthread-selected-parent-hook.py \
      /data/cache/platformio/packages/framework-espidf/components/openthread/openthread/src/core

Run a clean ESPHome build after applying the patch.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

DEFAULT_ROOT = Path.home() / ".platformio/packages/framework-espidf/components/openthread/openthread/src/core"
MARKER = "THREAD_PREFERRED_PARENT_SELECTED_PARENT_HOOK"


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n")


def patch_once(path: Path, old: str, new: str, *, dry_run: bool = False) -> str:
    text = normalize_newlines(path.read_text())
    old = normalize_newlines(old)
    new = normalize_newlines(new)

    if new in text:
        return "already"
    if old not in text:
        return "missing"

    if not dry_run:
        backup = path.with_suffix(path.suffix + ".thread-preferred-parent.bak")
        if not backup.exists():
            shutil.copy2(path, backup)
        path.write_text(text.replace(old, new, 1))
    return "patched"


def build_patches(root: Path):
    return [
        (
            root / "thread/mle.hpp",
            "    Error SearchForBetterParent(void);\n",
            """    Error SearchForBetterParent(void);\n\n    /**\n     * Starts targeted attach flow to a selected parent by extended address.\n     *\n     * This is an ESPHome Thread preferred-parent extension. It reuses\n     * OpenThread's internal selected-parent attach mode.\n     *\n     * @param[in] aExtAddress Extended address of the selected parent candidate.\n     *\n     * @retval kErrorNone Successfully started selected-parent attach flow.\n     * @retval kErrorInvalidState Thread is not attached as a child.\n     * @retval kErrorBusy An attach process is already in progress.\n     */\n    Error AttachToSelectedParent(const Mac::ExtAddress &aExtAddress);\n""",
        ),
        (
            root / "thread/mle.cpp",
            """Error Mle::SearchForBetterParent(void)\n{\n    Error error = kErrorNone;\n\n    VerifyOrExit(IsChild(), error = kErrorInvalidState);\n\n    mAttacher.Attach(kBetterParent);\n\nexit:\n    return error;\n}\n\n""",
            """Error Mle::SearchForBetterParent(void)\n{\n    Error error = kErrorNone;\n\n    VerifyOrExit(IsChild(), error = kErrorInvalidState);\n\n    mAttacher.Attach(kBetterParent);\n\nexit:\n    return error;\n}\n\nError Mle::AttachToSelectedParent(const Mac::ExtAddress &aExtAddress)\n{\n    Error error = kErrorNone;\n\n    VerifyOrExit(IsChild(), error = kErrorInvalidState);\n    VerifyOrExit(!IsAttaching(), error = kErrorBusy);\n\n    mAttacher.Attach(kSelectedParent);\n    mAttacher.GetParentCandidate().SetExtAddress(aExtAddress);\n\nexit:\n    return error;\n}\n\n""",
        ),
        (
            root / "thread/mle.cpp",
            """#if OPENTHREAD_FTD && OPENTHREAD_CONFIG_PARENT_SEARCH_ENABLE\n    if (aType == kToSelectedRouter)\n    {\n        TxMessage *messageToCurParent = static_cast<TxMessage *>(message->Clone());\n        VerifyOrExit(messageToCurParent != nullptr, error = kErrorNoBufs);\n\n        destination.SetToLinkLocalAddress(Get<Mle>().mParent.GetExtAddress());\n        error = messageToCurParent->SendTo(destination);\n        if (error != kErrorNone)\n        {\n            messageToCurParent->Free();\n            ExitNow();\n        }\n        Log(kMessageSend, kTypeParentRequestToRouters, destination);\n\n        destination.SetToLinkLocalAddress(Get<Mle>().mParentSearch.GetSelectedParent().GetExtAddress());\n    }\n    else\n#endif\n    {\n        destination.SetToLinkLocalAllRoutersMulticast();\n    }\n""",
            """    if (aType == kToSelectedRouter)\n    {\n#if OPENTHREAD_FTD && OPENTHREAD_CONFIG_PARENT_SEARCH_ENABLE\n        TxMessage *messageToCurParent = static_cast<TxMessage *>(message->Clone());\n        VerifyOrExit(messageToCurParent != nullptr, error = kErrorNoBufs);\n\n        destination.SetToLinkLocalAddress(Get<Mle>().mParent.GetExtAddress());\n        error = messageToCurParent->SendTo(destination);\n        if (error != kErrorNone)\n        {\n            messageToCurParent->Free();\n            ExitNow();\n        }\n        Log(kMessageSend, kTypeParentRequestToRouters, destination);\n\n        destination.SetToLinkLocalAddress(Get<Mle>().mParentSearch.GetSelectedParent().GetExtAddress());\n#else\n        // THREAD_PREFERRED_PARENT_SELECTED_PARENT_HOOK\n        // MTD builds do not have ParentSearch, but selected-parent attach still\n        // has a parent candidate. Unicast the Parent Request directly to it.\n        destination.SetToLinkLocalAddress(mParentCandidate.GetExtAddress());\n#endif\n    }\n    else\n    {\n        destination.SetToLinkLocalAllRoutersMulticast();\n    }\n""",
        ),
        (
            root / "thread/mle.cpp",
            """    case kAnyPartition:\n    case kSamePartition:\n    case kDowngradeToReed:\n    case kBetterParent:\n    case kSelectedParent:\n\n        // Ensure that a Parent Response was received from the\n        // current parent to which the device is attached, so\n        // that the new parent candidate can be compared with the\n        // current parent and confirmed to be preferred.\n        VerifyOrExit(mReceivedResponseFromParent);\n        break;\n""",
            """    case kAnyPartition:\n    case kSamePartition:\n    case kDowngradeToReed:\n    case kBetterParent:\n\n        // Ensure that a Parent Response was received from the\n        // current parent to which the device is attached, so\n        // that the new parent candidate can be compared with the\n        // current parent and confirmed to be preferred.\n        VerifyOrExit(mReceivedResponseFromParent);\n        break;\n\n    case kSelectedParent:\n        // THREAD_PREFERRED_PARENT_SELECTED_PARENT_HOOK\n        // The attach flow is already constrained to the explicitly requested\n        // candidate, so do not require a comparison response from the current\n        // parent before sending the Child ID Request.\n        break;\n""",
        ),
        (
            root / "api/thread_api.cpp",
            """otError otThreadSearchForBetterParent(otInstance *aInstance)\n{\n    return AsCoreType(aInstance).Get<Mle::Mle>().SearchForBetterParent();\n}\n\n""",
            """otError otThreadSearchForBetterParent(otInstance *aInstance)\n{\n    return AsCoreType(aInstance).Get<Mle::Mle>().SearchForBetterParent();\n}\n\nextern \"C\" bool thread_preferred_parent_ot_request_selected_parent_attach(otInstance *aInstance,\n                                                                             const otExtAddress *aPreferredExtAddress)\n{\n    // THREAD_PREFERRED_PARENT_SELECTED_PARENT_HOOK\n    if ((aInstance == nullptr) || (aPreferredExtAddress == nullptr))\n    {\n        return false;\n    }\n\n    return AsCoreType(aInstance).Get<Mle::Mle>().AttachToSelectedParent(AsCoreType(aPreferredExtAddress)) == kErrorNone;\n}\n\n""",
        ),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=DEFAULT_ROOT,
        help="OpenThread src/core root to patch",
    )
    parser.add_argument("--dry-run", action="store_true", help="Report what would be patched without writing files")
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    if not root.exists():
        print(f"[missing-root] {root}")
        return 1

    rc = 0
    for path, old, new in build_patches(root):
        if not path.exists():
            print(f"[missing-file] {path}")
            rc = 1
            continue
        state = patch_once(path, old, new, dry_run=args.dry_run)
        print(f"[{state}] {path}")
        if state == "missing":
            rc = 1

    if rc == 0:
        print("Done. Run a clean ESPHome build so OpenThread is rebuilt.")
    else:
        print("One or more patches did not match your OpenThread revision. Inspect the backup files and patch manually.")

    return rc


if __name__ == "__main__":
    raise SystemExit(main())
