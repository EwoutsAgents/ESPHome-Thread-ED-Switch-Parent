#!/usr/bin/env python3
"""Log the random delay selected for each OpenThread Parent Response."""

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path
from typing import Optional

DEFAULT_ROOT = Path.home() / ".platformio/packages/framework-espidf/components/openthread/openthread/src/core"
FRAMEWORK_RELATIVE_CORE = Path("framework-espidf/components/openthread/openthread/src/core")
MARKER = "THREAD_PARENT_RESPONSE_DELAY_LOG_COMPONENT"


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n")


def backup_once(path: Path) -> None:
    backup = path.with_suffix(path.suffix + ".thread-parent-response-delay-log.bak")
    if not backup.exists():
        shutil.copy2(path, backup)


def patch_parent_response_delay_log(root: Path, *, dry_run: bool = False) -> str:
    path = root / "thread/mle_ftd.cpp"
    text = normalize_newlines(path.read_text(encoding="utf-8"))

    if MARKER in text:
        return "already"

    old = """    delay = GenerateRandomDelay(!ScanMaskTlv::IsEndDeviceFlagSet(scanMask) ? kParentResponseMaxDelayRouters
                                                                           : kParentResponseMaxDelayAll);
    mDelayedSender.ScheduleParentResponse(info, delay);
"""
    new = """    delay = GenerateRandomDelay(!ScanMaskTlv::IsEndDeviceFlagSet(scanMask) ? kParentResponseMaxDelayRouters
                                                                           : kParentResponseMaxDelayAll);
    // THREAD_PARENT_RESPONSE_DELAY_LOG_COMPONENT
    LogNote("ParentResponseDelay delay_ms=%lu scan_mask=0x%02x child=%s", ToUlong(delay), scanMask,
            info.mChildExtAddress.ToString().AsCString());
    mDelayedSender.ScheduleParentResponse(info, delay);
"""

    if old not in text:
        return "missing"

    if not dry_run:
        backup_once(path)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    return "patched"


def apply_patch(root: Path, *, dry_run: bool = False) -> int:
    root = root.expanduser().resolve()
    path = root / "thread/mle_ftd.cpp"
    print(f"[thread_parent_response_delay_log] OpenThread src/core: {root}")

    if not path.exists():
        print(f"[thread_parent_response_delay_log][missing-file] {path}")
        return 1

    state = patch_parent_response_delay_log(root, dry_run=dry_run)
    print(f"[thread_parent_response_delay_log][{state}] Parent Response delay log: {path}")
    if state == "missing":
        print("[thread_parent_response_delay_log] Required patch did not match this OpenThread revision.")
        return 1

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

    rc = apply_patch(packages_dir / FRAMEWORK_RELATIVE_CORE)
    if rc != 0:
        raise SystemExit(rc)
    return rc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    return apply_patch(args.root, dry_run=args.dry_run)


_pio_rc = run_as_platformio_script()

if __name__ == "__main__":
    if _pio_rc is not None:
        raise SystemExit(_pio_rc)
    raise SystemExit(main())
