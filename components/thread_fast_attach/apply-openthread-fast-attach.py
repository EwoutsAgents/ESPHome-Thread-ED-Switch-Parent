#!/usr/bin/env python3
"""Apply the isolated OpenThread PR #13121 backport to PlatformIO's ESP-IDF package."""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import threading
from pathlib import Path
from typing import Optional

FRAMEWORK_RELATIVE_OT = Path("framework-espidf/components/openthread/openthread")
DEFAULT_ROOT = Path.home() / ".platformio/packages" / FRAMEWORK_RELATIVE_OT
MARKER = "OPENTHREAD_CONFIG_MLE_FAST_ATTACH_ENABLE"


def find_patch_path() -> Path:
    """Find the canonical patch both as a normal script and under SCons."""
    candidates: list[Path] = []
    script_file = globals().get("__file__")
    if script_file:
        candidates.extend(Path(script_file).resolve().parents)
    try:
        Import("env")  # type: ignore[name-defined]  # noqa: F821
        candidates.extend(Path(env.subst("$PROJECT_DIR")).resolve().parents)  # type: ignore[name-defined]  # noqa: F821
    except Exception:
        candidates.extend(Path.cwd().resolve().parents)
        candidates.append(Path.cwd().resolve())
    for parent in candidates:
        patch = parent / "patches/fast-attach/openthread-fast-attach-pr13121.patch"
        if patch.is_file():
            return patch
    raise FileNotFoundError("Could not locate patches/fast-attach/openthread-fast-attach-pr13121.patch")


def apply_patch(root: Path, *, dry_run: bool = False) -> int:
    root = root.expanduser().resolve()
    patch_path = find_patch_path()
    mle_h = root / "src/core/config/mle.h"
    digest = hashlib.sha256(patch_path.read_bytes()).hexdigest()
    print(f"[thread_fast_attach] OpenThread root: {root}")
    print(f"[thread_fast_attach] patch_sha256={digest}")

    if not mle_h.exists():
        print(f"[thread_fast_attach][missing-file] {mle_h}")
        return 1
    if MARKER in mle_h.read_text(encoding="utf-8"):
        print("[thread_fast_attach][already] PR #13121 backport present")
        return 0

    # `root` lives below this repository's worktree, so `git apply` would walk
    # upward and resolve paths against the wrong repository root. POSIX patch
    # honors cwd and therefore targets the isolated framework package itself.
    check = subprocess.run(
        ["patch", "--dry-run", "--batch", "--forward", "-p1", "-i", str(patch_path)],
        cwd=root,
        check=False,
    )
    if check.returncode != 0:
        print("[thread_fast_attach] Patch does not match this OpenThread revision.")
        return check.returncode
    if dry_run:
        print("[thread_fast_attach][dry-run] patch applies")
        return 0

    result = subprocess.run(
        ["patch", "--batch", "--forward", "-p1", "-i", str(patch_path)], cwd=root, check=False
    )
    if result.returncode == 0:
        print("[thread_fast_attach][patched] OpenThread PR #13121 backport applied")
    return result.returncode


def platformio_package_root() -> Optional[Path]:
    try:
        Import("env")  # type: ignore[name-defined]  # noqa: F821
    except Exception:
        return None
    packages_dir = env.subst("$PROJECT_PACKAGES_DIR")  # type: ignore[name-defined]  # noqa: F821
    if not packages_dir or "$" in packages_dir:
        packages_dir = os.environ.get("PLATFORMIO_PACKAGES_DIR", "")
    return Path(packages_dir) if packages_dir else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    return apply_patch(args.root, dry_run=args.dry_run)


_packages = platformio_package_root()
if _packages is not None:
    _patch_lock = threading.Lock()
    _patched_for_build = False

    def _patch_before_component_compile(source, target, env):
        global _patched_for_build
        del source, target, env
        with _patch_lock:
            if _patched_for_build:
                return
            rc = apply_patch(_packages / FRAMEWORK_RELATIVE_OT)
            if rc:
                raise SystemExit(rc)
            _patched_for_build = True

    # Framework packages are resolved after extra scripts are loaded. The
    # component object is an explicit build target, so this action runs after
    # package resolution and before either the wrapper or OpenThread is built.
    targets = [
        "$BUILD_DIR/src/esphome/components/thread_fast_attach/thread_fast_attach.cpp.o",
        "$BUILD_DIR/openthread/openthread/src/core/api/thread_api.cpp.o",
        "$BUILD_DIR/openthread/openthread/src/core/thread/mle.cpp.o",
        "$BUILD_DIR/openthread/openthread/src/core/thread/mle_ftd.cpp.o",
    ]
    for target in targets:
        env.AddPreAction(target, _patch_before_component_compile)  # type: ignore[name-defined]  # noqa: F821

if __name__ == "__main__":
    raise SystemExit(main())
