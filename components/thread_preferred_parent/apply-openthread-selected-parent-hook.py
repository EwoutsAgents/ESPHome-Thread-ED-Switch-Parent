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
ESP_IDF_MTD_CONFIG_RELATIVE = Path(
    "../private_include/openthread-core-esp32x-mtd-config.h"
)
ESP_IDF_CONFIG_MARKER = "THREAD_PREFERRED_PARENT_ESP_IDF_CONFIG"


def find_repository_root() -> Path:
    script_name = globals().get("__file__")
    if script_name:
        return Path(script_name).resolve().parents[2]

    scons_env = globals().get("env")
    if scons_env is not None:
        for phase in ("pre", "post"):
            for script in scons_env.GetExtraScripts(phase):
                path = Path(str(script)).resolve()
                if path.name == "apply-openthread-selected-parent-hook.py":
                    return path.parents[2]

    raise RuntimeError("cannot determine preferred-parent component repository root")


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
    else:
        git_env = os.environ.copy()
        # Vendored ESP-IDF sources can live below the user's Git checkout without
        # being a Git repository themselves. Prevent `git apply` from discovering
        # that outer repository and interpreting patch paths relative to it.
        git_env["GIT_CEILING_DIRECTORIES"] = str(openthread_root.parent.resolve())

        check = subprocess.run(
            ["git", "apply", "--check", "--unsafe-paths", str(patch_path)],
            cwd=openthread_root,
            env=git_env,
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
            ["git", "apply", "--unsafe-paths", str(patch_path)],
            cwd=openthread_root,
            env=git_env,
            check=True,
        )
        if not marker.is_file():
            raise RuntimeError("git apply succeeded but the OpenThread marker is missing")
        print(f"applied canonical preferred-parent controller patch to {openthread_root}")

    # PlatformIO build flags apply to ESPHome sources but ESP-IDF compiles its
    # OpenThread component as a separate CMake target. Enable the same option in
    # ESP-IDF's MTD project config so the API and core are built consistently.
    esp_idf_config = (openthread_root / ESP_IDF_MTD_CONFIG_RELATIVE).resolve()
    if esp_idf_config.is_file():
        contents = esp_idf_config.read_text()
        if ESP_IDF_CONFIG_MARKER not in contents:
            with esp_idf_config.open("a") as config_file:
                config_file.write(
                    "\n// THREAD_PREFERRED_PARENT_ESP_IDF_CONFIG\n"
                    "#undef OPENTHREAD_CONFIG_EXPERIMENTAL_PREFERRED_PARENT_ENABLE\n"
                    "#define OPENTHREAD_CONFIG_EXPERIMENTAL_PREFERRED_PARENT_ENABLE 1\n"
                )
            print(f"enabled preferred-parent controller in {esp_idf_config}")


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
