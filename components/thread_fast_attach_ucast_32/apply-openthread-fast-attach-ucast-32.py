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
MARKER = "FAST_ATTACH_UCAST_32"


def find_patch_paths() -> list[Path]:
    """Find the three ordered, dedicated patches both normally and under SCons."""
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
        patch_dir = parent / "patches/fast-attach-ucast-32"
        patches = [
            patch_dir / "openthread-preferred-parent-controller.patch",
            patch_dir / "openthread-fast-attach-pr13121.patch",
            patch_dir / "fast-attach-ucast-32-delta.patch",
        ]
        if all(patch.is_file() for patch in patches):
            return patches
    raise FileNotFoundError("Could not locate the fast-attach-ucast-32 patch set")


def apply_patch(root: Path, *, dry_run: bool = False) -> int:
    root = root.expanduser().resolve()
    patch_paths = find_patch_paths()
    marker_file = root / "src/core/thread/mle_ftd.cpp"
    digest = hashlib.sha256(b"".join(patch.read_bytes() for patch in patch_paths)).hexdigest()
    print(f"[thread_fast_attach_ucast_32] OpenThread root: {root}")
    print(f"[thread_fast_attach_ucast_32] patch_sha256={digest}")

    if not marker_file.exists():
        print(f"[thread_fast_attach_ucast_32][missing-file] {marker_file}")
        return 1
    if MARKER in marker_file.read_text(encoding="utf-8"):
        print("[thread_fast_attach_ucast_32][already] combined backport present")
        return 0

    # `root` lives below this repository's worktree, so `git apply` would walk
    # upward and resolve paths against the wrong repository root. POSIX patch
    # honors cwd and therefore targets the isolated framework package itself.
    if dry_run:
        # A sequential dry-run cannot validate dependent patches without a
        # disposable source tree; builds exercise this exact ordered path.
        print("[thread_fast_attach_ucast_32][dry-run] patch set found; ordered application deferred")
        return 0

    for patch_path in patch_paths:
        result = subprocess.run(
            ["patch", "--batch", "--forward", "-p1", "-i", str(patch_path)], cwd=root, check=False
        )
        if result.returncode != 0:
            print(f"[thread_fast_attach_ucast_32] Failed applying {patch_path.name}")
            return result.returncode
    print("[thread_fast_attach_ucast_32][patched] combined selected-parent + Fast Attach backport applied")
    return 0


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
        "$BUILD_DIR/src/esphome/components/thread_fast_attach_ucast_32/thread_fast_attach_ucast_32.cpp.o",
        "$BUILD_DIR/openthread/openthread/src/core/api/thread_api.cpp.o",
        "$BUILD_DIR/openthread/openthread/src/core/thread/mle.cpp.o",
        "$BUILD_DIR/openthread/openthread/src/core/thread/mle_ftd.cpp.o",
    ]
    for target in targets:
        env.AddPreAction(target, _patch_before_component_compile)  # type: ignore[name-defined]  # noqa: F821

if __name__ == "__main__":
    raise SystemExit(main())
