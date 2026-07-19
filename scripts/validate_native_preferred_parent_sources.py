#!/usr/bin/env python3
"""Validate preferred-parent source ownership and patch composition."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
COMPONENT = ROOT / "components/thread_preferred_parent"
CORE_PATCH = ROOT / "patches/canonical/openthread-preferred-parent-controller.patch"
CLI_PATCH = ROOT / "patches/otns/preferred-parent-cli-adapter.patch"


def require(text: str, token: str, description: str) -> None:
    if token not in text:
        raise RuntimeError(f"missing {description}: {token}")


def reject(text: str, token: str, description: str) -> None:
    if token in text:
        raise RuntimeError(f"{description} remains in thin adapter: {token}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--openthread-source", type=Path)
    args = parser.parse_args()

    adapter = (COMPONENT / "thread_preferred_parent.h").read_text() + (
        COMPONENT / "thread_preferred_parent.cpp"
    ).read_text()
    for token in ("millis()", "FreeRTOS", "BufferedParentResponse", "void loop(",
                  "continue_selected_parent_attach", "start_parent_discovery"):
        reject(adapter, token, "controller implementation")
    for token in ("otThreadPreferredParentStart", "otThreadPreferredParentCancel",
                  "otThreadPreferredParentGetStatus"):
        require(adapter, token, "OpenThread API use")

    core = CORE_PATCH.read_text()
    for token in (
        "mPreferredParentCandidate.Init(aInstance)",
        "mPreferredParentCandidate.Clear()",
        "mPreferredParentCandidate      = mParentCandidate",
        "mPreferredParentCandidateValid = true",
        "OT_THREAD_PREFERRED_PARENT_STATE_WAITING_CHILD_ID_RESPONSE",
        "OPENTHREAD_CONFIG_EXPERIMENTAL_PREFERRED_PARENT_ENABLE",
    ):
        require(core, token, "core controller invariant")

    cli = CLI_PATCH.read_text()
    for command in ('strcmp(aArgs[0], "status")', 'strcmp(aArgs[0], "cancel")',
                    'strcmp(aArgs[0], "clear")', 'strcmp(aArgs[0], "switch")'):
        require(cli, command, "thin CLI command")
    reject(cli, "HandleTimer", "CLI state machine")
    reject(cli, "HandleParentResponse", "CLI candidate handling")

    if args.openthread_source:
        subprocess.run(
            ["git", "apply", "--check", str(CORE_PATCH)],
            cwd=args.openthread_source.resolve(),
            check=True,
        )

    print("preferred-parent source ownership: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
