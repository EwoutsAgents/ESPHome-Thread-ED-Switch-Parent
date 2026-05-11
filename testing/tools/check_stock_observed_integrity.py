#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FORBIDDEN_IN_STOCK_OBSERVER = [
    "request_selected_parent_attach",
    "biparental_ot_request_selected_parent_attach",
    "otThreadSetPreferredParentExtAddress",
    "otThreadSetPreferredParentRloc16",
    "otThreadSearchForPreferredParentExtAddress",
    "otThreadSearchForPreferredParentRloc16",
    "start_parent_discovery_unicast",
    "AttachToSelectedParent",
    "apply-openthread-selected-parent-hook.py",
]

FORBIDDEN_IN_CHILD_STOCK = [
    "stock compatibility marker",
    "target observed after 0 ms",
    "starting selected-parent attach",
    "SendChildIdRequest",
    "Attach result: success",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def assert_file_contains_none(path: Path, forbidden: list[str], label: str) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for needle in forbidden:
        if needle in text:
            fail(f"{label} contains forbidden string '{needle}' ({path})")


def check_so_not_mapped_to_t() -> None:
    path = ROOT / "testing/tools/extract_switch_timings.py"
    text = path.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"SO\d.*T\d|T\d.*SO\d", text):
        # very broad guard; allow co-existence but disallow explicit mapping hints
        pass
    if "SO*" in text and "mapped" in text.lower() and "T*" in text:
        fail("extractor appears to describe SO* mapped into T*")


def check_results_artifacts_exist() -> None:
    summary = ROOT / "testing/RESULTS_SUMMARY_2026-05-11.md"
    if not summary.exists():
        summary = ROOT / "testing/RESULTS_SUMMARY_2026-05-07.md"
    text = summary.read_text(encoding="utf-8", errors="ignore")
    refs = re.findall(r"`(testing/logs/[^`]+\.(?:log|csv))`", text)
    for ref in refs:
        if not (ROOT / ref).exists():
            fail(f"results summary references missing artifact: {ref}")


def main() -> int:
    child_stock = ROOT / "testing/configs/child_stock.yaml"
    stock_observer_init = ROOT / "components/thread_stock_observer/__init__.py"

    assert_file_contains_none(child_stock, FORBIDDEN_IN_CHILD_STOCK, "child_stock.yaml")

    for path in (ROOT / "components/thread_stock_observer").glob("**/*"):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".o", ".a"}:
            continue
        assert_file_contains_none(path, FORBIDDEN_IN_STOCK_OBSERVER, "thread_stock_observer")

    init_text = stock_observer_init.read_text(encoding="utf-8", errors="ignore")
    if "apply-openthread-selected-parent-hook.py" in init_text:
        fail("thread_stock_observer/__init__.py still registers full selected-parent patch")

    check_so_not_mapped_to_t()
    check_results_artifacts_exist()

    print("PASS: stock-observed integrity checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
