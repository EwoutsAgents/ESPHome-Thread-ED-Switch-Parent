#!/usr/bin/env python3
"""Apply the canonical OpenThread preferred-parent controller patch.

This pre-build action deliberately contains no controller implementation. It
applies the same canonical source patch used by the OTNS native build.
"""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys


PATCH_RELATIVE = Path("patches/canonical/openthread-preferred-parent-controller.patch")
MARKER_RELATIVE = Path("src/core/config/preferred_parent.h")


def find_repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def candidate_openthread_roots(project_dir: Path) -> list[Path]:
    explicit = os.environ.get("THREAD_PREFERRED_PARENT_OPENTHREAD_ROOT")
    platformio_packages = os.environ.get("PLATFORMIO_PACKAGES_DIR")
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    if platformio_packages:
        candidates.append(Path(platformio_packages))
    candidates.extend(
        [
            project_dir / ".pio" / "libdeps",
            project_dir / ".pio" / "packages",
            Path.home() / ".platformio" / "packages",
        ]
    )
    return candidates


def locate_openthread(project_dir: Path) -> Path:
    for candidate in candidate_openthread_roots(project_dir):
        if (candidate / "src/core/thread/mle.cpp").is_file():
            return candidate
        if not candidate.exists():
            continue
        for mle_cpp in candidate.rglob("src/core/thread/mle.cpp"):
            root = mle_cpp.parents[3]
            if (root / "include/openthread/thread.h").is_file():
                return root
    raise RuntimeError(
        "OpenThread source tree not found; set THREAD_PREFERRED_PARENT_OPENTHREAD_ROOT"
    )


def apply_patch(openthread_root: Path, patch_path: Path) -> None:
    marker = openthread_root / MARKER_RELATIVE
    if marker.is_file():
        print(f"preferred-parent OpenThread patch already present: {marker}")
        return

    check = subprocess.run(
        ["git", "apply", "--check", str(patch_path)],
        cwd=openthread_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if check.returncode != 0:
        raise RuntimeError(
            "canonical preferred-parent patch does not apply to this OpenThread revision:\n"
            + check.stdout
        )

    subprocess.run(
        ["git", "apply", str(patch_path)], cwd=openthread_root, check=True
    )
    print(f"applied canonical preferred-parent controller patch to {openthread_root}")


def main() -> int:
    repository_root = find_repository_root()
    patch_path = repository_root / PATCH_RELATIVE
    if not patch_path.is_file():
        raise RuntimeError(f"canonical patch is missing: {patch_path}")

    project_dir = Path(os.environ.get("PROJECT_DIR", os.getcwd())).resolve()
    apply_patch(locate_openthread(project_dir), patch_path)
    return 0


if "Import" in globals():
    Import("env")
    scons_env = globals()["env"]
    project_dir = Path(scons_env.subst("$PROJECT_DIR")).resolve()
    apply_patch(locate_openthread(project_dir), find_repository_root() / PATCH_RELATIVE)
elif __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(f"preferred-parent patch failed: {error}", file=sys.stderr)
        sys.exit(1)
