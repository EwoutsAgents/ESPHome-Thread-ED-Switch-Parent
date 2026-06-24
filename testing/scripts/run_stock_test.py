#!/usr/bin/env python3
"""Run the stock ESPHome/OpenThread parent-switching test.

The important invariant is that all firmware is compiled before the timed test
sequence starts. During the timed sequence this script uses `esphome upload`,
which ESPHome documents as uploading the most recent firmware build.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
import threading
import traceback
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

try:  # Python 3.11+
    import tomllib  # type: ignore[attr-defined]
except ModuleNotFoundError:  # pragma: no cover - optional local dependency
    try:
        import tomli as tomllib  # type: ignore[no-redef]
    except ModuleNotFoundError:
        tomllib = None  # type: ignore[assignment]


CONFIG_NAMES = {
    "empty": "empty.yaml",
    "router1": "stock_router_1.yaml",
    "child": "stock_child.yaml",
    "router2": "stock_router_2.yaml",
    "router3": "stock_router_3.yaml",
    "router4": "stock_router_4.yaml",
}
CORE_COMPILE_ORDER = ["empty", "router1", "child", "router2"]
MAX_ROUTER_COUNT = max(
    int(name.removeprefix("router"))
    for name in CONFIG_NAMES
    if name.startswith("router")
)
PCAP_PATH_RE = re.compile(r"Saving (?:test )?capture to (\S+\.pcapng)")
TAIL_SNAPSHOT_LINES = 120
SKIP_NO_CHILD_PARENT = "SKIP_NO_CHILD_PARENT"
SKIP_PARENT_NOT_MAPPED_TO_DEVICE = "SKIP_PARENT_NOT_MAPPED_TO_DEVICE"
SKIP_PARENT_IS_LEADER = "SKIP_PARENT_IS_LEADER"

SKIP_NO_CHILD_PARENT_NOTE = (
    "No usable current-parent evidence was found within the child attach observation window. "
    "This classification does not prove that the child had no parent; it means no current "
    "parent could be reliably determined."
)
SKIP_PARENT_NOT_MAPPED_TO_DEVICE_NOTE = (
    "A child parent was detected, but its extended address could not be mapped to any "
    "configured router device in this test run."
)
SKIP_PARENT_IS_LEADER_NOTE = (
    "The detected child parent is the current Thread leader. Removing it would invalidate "
    "the stock parent-switch measurement by disrupting the leader rather than only removing "
    "the child's parent."
)


_SUPERVISOR_LOG_PATH: Path | None = None
_BATCH_LOG_PATH: Path | None = None
_CURRENT_TRACKER: "RunTracker | None" = None


@dataclass
class Timing:
    sniffer_lead_in_seconds: int = 5
    router_settling_seconds: int = 90
    child_attach_seconds: int = 30
    after_parent_removed_seconds: int = 180


@dataclass
class SnifferSettings:
    enabled: bool = False
    command: list[str] = field(default_factory=list)
    stop_timeout_seconds: int = 10


@dataclass
class Settings:
    config_file: Path
    testing_dir: Path
    configs_dir: Path
    logs_dir: Path
    run_logs_dir: Path
    esphome_bin: str
    esptool_bin: str
    upload_speed: str | None = None
    precompile: bool = True
    clean_before_compile: bool = False
    devices: dict[str, str] = field(default_factory=dict)
    timing: Timing = field(default_factory=Timing)
    sniffer: SnifferSettings = field(default_factory=SnifferSettings)
    capture_router2_log: bool = True
    max_router_number: int = 3


def now_utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def build_run_logs_dir(logs_dir: Path, *, run_index: int | None = None) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    if run_index is not None:
        stamp = f"{stamp}-run{run_index:02d}"
    return logs_dir / stamp


def allocate_batch_logs_dir(logs_root: Path, *, variant_name: str, router_count: int, total_runs: int) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    base_name = f"{variant_name}-{router_count}router-{total_runs}runs-{stamp}"
    candidate = logs_root / base_name
    counter = 2
    while candidate.exists():
        candidate = logs_root / f"{base_name}-dup{counter:02d}"
        counter += 1
    return candidate


def log(msg: str) -> None:
    formatted = f"[{now_utc_iso()}] {msg}"
    print(formatted, flush=True)
    targets: list[Path] = []
    if _BATCH_LOG_PATH is not None:
        targets.append(_BATCH_LOG_PATH)
    if _SUPERVISOR_LOG_PATH is not None and _SUPERVISOR_LOG_PATH not in targets:
        targets.append(_SUPERVISOR_LOG_PATH)
    for path in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8", errors="replace") as fh:
            fh.write(formatted + "\n")


def set_supervisor_log(path: Path | None) -> None:
    global _SUPERVISOR_LOG_PATH
    _SUPERVISOR_LOG_PATH = path


def set_batch_log(path: Path | None) -> None:
    global _BATCH_LOG_PATH
    _BATCH_LOG_PATH = path


def process_exit_details(process: subprocess.Popen[str] | None) -> dict[str, Any] | None:
    if process is None or process.returncode is None:
        return None
    details: dict[str, Any] = {"returncode": process.returncode}
    if process.returncode < 0:
        details["signal"] = -process.returncode
    return details


def safe_tail_lines(path: Path, lines: int = TAIL_SNAPSHOT_LINES) -> list[str]:
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            data = fh.readlines()
    except OSError:
        return []
    return [line.rstrip("\n") for line in data[-lines:]]


class RunTracker:
    def __init__(
        self,
        settings: Settings,
        *,
        dry_run: bool,
        run_number: int | None,
        total_runs: int,
        precompile_manifest: list[dict[str, Any]],
    ) -> None:
        self.settings = settings
        self.dry_run = dry_run
        self.run_number = run_number
        self.total_runs = total_runs
        self.precompile_manifest = precompile_manifest
        self.events: list[dict[str, Any]] = []
        self.lock = threading.Lock()
        self.status = "running"
        self.current_step = "initializing"
        self.abort_reason: str | None = None
        self.abort_traceback: str | None = None
        self.child_log: Path | None = None
        self.router1_log: Path | None = None
        self.router2_log: Path | None = None
        self.device_logs: dict[str, Path] = {}
        self.sniffer_log: Path | None = None
        self.sniffer_remote_pcap: str | None = None
        self.sniffer_local_pcap: Path | None = None
        self.processes: dict[str, dict[str, Any]] = {}
        self.manifest_path = self.settings.run_logs_dir / f"stock_test_manifest_{self.settings.run_logs_dir.name}.json"
        self.supervisor_log_path = self.settings.run_logs_dir / "runner_supervisor.log"
        self.settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
        set_supervisor_log(self.supervisor_log_path)
        self.flush_manifest()

    def snapshot_payload(self) -> dict[str, Any]:
        return {
            "created_utc": now_utc_iso(),
            "dry_run": self.dry_run,
            "config_file": str(self.settings.config_file),
            "testing_dir": str(self.settings.testing_dir),
            "configs_dir": str(self.settings.configs_dir),
            "logs_dir": str(self.settings.logs_dir),
            "run_logs_dir": str(self.settings.run_logs_dir),
            "run_number": self.run_number,
            "total_runs": self.total_runs,
            "status": self.status,
            "current_step": self.current_step,
            "abort_reason": self.abort_reason,
            "abort_traceback": self.abort_traceback,
            "esphome_bin": self.settings.esphome_bin,
            "esptool_bin": self.settings.esptool_bin,
            "precompile": self.settings.precompile,
            "clean_before_compile": self.settings.clean_before_compile,
            "devices": self.settings.devices,
            "timing": self.settings.timing.__dict__,
            "max_router_number": self.settings.max_router_number,
            "additional_router_assignments": additional_router_assignments(self.settings),
            "device_assignments": device_assignments(self.settings),
            "child_log": str(self.child_log) if self.child_log else None,
            "router1_log": str(self.router1_log) if self.router1_log else None,
            "router2_log": str(self.router2_log) if self.router2_log else None,
            "device_logs": {name: str(path) for name, path in sorted(self.device_logs.items())},
            "supervisor_log": str(self.supervisor_log_path),
            "sniffer": {
                "enabled": self.settings.sniffer.enabled,
                "command": self.settings.sniffer.command,
                "stop_timeout_seconds": self.settings.sniffer.stop_timeout_seconds,
                "log": str(self.sniffer_log) if self.sniffer_log else None,
                "remote_pcap": self.sniffer_remote_pcap,
                "local_pcap": str(self.sniffer_local_pcap) if self.sniffer_local_pcap else None,
            },
            "processes": self.processes,
            "events": self.precompile_manifest + self.events,
        }

    def flush_manifest(self) -> Path:
        with self.lock:
            payload = self.snapshot_payload()
            self.manifest_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
            return self.manifest_path

    def set_step(self, step: str, *, status: str | None = None, extra: dict[str, Any] | None = None) -> None:
        with self.lock:
            self.current_step = step
            if status is not None:
                self.status = status
            event = {"time_utc": now_utc_iso(), "type": "step", "step": step}
            if extra:
                event.update(extra)
            self.events.append(event)
        self.flush_manifest()

    def append_event(self, event: dict[str, Any]) -> None:
        with self.lock:
            self.events.append(event)
        self.flush_manifest()

    def set_logs(
        self,
        *,
        child_log: Path | None = None,
        router1_log: Path | None = None,
        router2_log: Path | None = None,
        sniffer_log: Path | None = None,
    ) -> None:
        with self.lock:
            if child_log is not None:
                self.child_log = child_log
                self.device_logs["child"] = child_log
            if router1_log is not None:
                self.router1_log = router1_log
                self.device_logs["router1"] = router1_log
            if router2_log is not None:
                self.router2_log = router2_log
                self.device_logs["router2"] = router2_log
            if sniffer_log is not None:
                self.sniffer_log = sniffer_log
        self.flush_manifest()

    def set_device_log(self, logical_name: str, log_path: Path) -> None:
        with self.lock:
            self.device_logs[logical_name] = log_path
            if logical_name == "child":
                self.child_log = log_path
            elif logical_name == "router1":
                self.router1_log = log_path
            elif logical_name == "router2":
                self.router2_log = log_path
        self.flush_manifest()

    def set_sniffer_pcap(self, remote_pcap: str | None, local_pcap: Path | None) -> None:
        with self.lock:
            self.sniffer_remote_pcap = remote_pcap
            self.sniffer_local_pcap = local_pcap
        self.flush_manifest()

    def start_process(
        self,
        name: str,
        cmd: list[str],
        log_path: Path | None,
        process: subprocess.Popen[str] | None,
        *,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        record = {
            "cmd": cmd,
            "log_path": str(log_path) if log_path else None,
            "started_utc": now_utc_iso(),
            "pid": process.pid if process is not None else None,
            "status": "running" if process is not None else "dry-run",
        }
        if metadata:
            record.update(metadata)
        with self.lock:
            self.processes[name] = record
            self.events.append({"time_utc": now_utc_iso(), "type": "process_started", "name": name, **record})
        self.flush_manifest()

    def finish_process(
        self,
        name: str,
        process: subprocess.Popen[str] | None,
        *,
        expected: bool,
        log_path: Path | None,
    ) -> None:
        details = process_exit_details(process) or {}
        with self.lock:
            record = self.processes.setdefault(name, {})
            record.update(
                {
                    "ended_utc": now_utc_iso(),
                    "status": "expected_exit" if expected else "unexpected_exit",
                    **details,
                }
            )
            event = {"time_utc": now_utc_iso(), "type": "process_exited", "name": name, "expected": expected, **details}
            if log_path is not None:
                event["log_path"] = str(log_path)
            self.events.append(event)
        self.flush_manifest()

    def capture_failure_tails(self) -> None:
        targets = {**self.device_logs, "sniffer": self.sniffer_log}
        for name, path in targets.items():
            if path is None:
                continue
            tail_path = self.settings.run_logs_dir / f"{name}_tail_on_failure.log"
            lines = safe_tail_lines(path)
            if not lines:
                continue
            tail_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def mark_completed(self) -> None:
        self.set_step("completed", status="completed")

    def mark_aborted(self, reason: str, *, exc: BaseException | None = None) -> None:
        with self.lock:
            self.status = "failed"
            self.abort_reason = reason
            if exc is not None:
                self.abort_traceback = "".join(traceback.format_exception(exc))
            self.events.append({"time_utc": now_utc_iso(), "type": "abort", "reason": reason})
        self.capture_failure_tails()
        self.flush_manifest()


def quote_cmd(cmd: Iterable[str | os.PathLike[str]]) -> str:
    return " ".join(shlex.quote(str(part)) for part in cmd)


def load_toml(path: Path) -> dict[str, Any]:
    if tomllib is None:
        raise SystemExit(
            "Unable to read TOML because neither Python tomllib nor tomli is available. "
            "Use Python 3.11+ from the local venv, or install tomli."
        )
    with path.open("rb") as fh:
        return tomllib.load(fh)


def resolve_relative(base: Path, value: str | None, default: str) -> Path:
    candidate = Path(value or default)
    if not candidate.is_absolute():
        candidate = base / candidate
    return candidate.resolve()


def candidate_esphome_bins(config_dir: Path, testing_dir: Path) -> list[Path]:
    repo_root = testing_dir.parent
    candidates = [
        repo_root / ".venv" / "bin" / "esphome",
        repo_root / "venv" / "bin" / "esphome",
        testing_dir / ".venv" / "bin" / "esphome",
        testing_dir / "venv" / "bin" / "esphome",
        config_dir / ".." / ".venv" / "bin" / "esphome",
        config_dir / ".." / "venv" / "bin" / "esphome",
    ]
    deduped: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved not in seen:
            deduped.append(resolved)
            seen.add(resolved)
    return deduped


def resolve_esphome_bin(
    *,
    cli_value: str | None,
    env_value: str | None,
    config_value: str | None,
    config_dir: Path,
    testing_dir: Path,
    dry_run: bool,
) -> str:
    explicit = cli_value or env_value
    if explicit:
        path = Path(explicit)
        if not path.is_absolute():
            path = (Path.cwd() / path).resolve()
        if dry_run or path.exists():
            return str(path)
        raise SystemExit(f"ESPHome binary not found: {path}")

    if config_value:
        path = Path(config_value)
        if not path.is_absolute():
            path = (config_dir / path).resolve()
        if path.exists():
            return str(path)
        log(f"Configured ESPHome binary does not exist, falling back to auto-detection: {path}")

    for candidate in candidate_esphome_bins(config_dir, testing_dir):
        if candidate.exists():
            return str(candidate)

    path_bin = shutil.which("esphome")
    if path_bin:
        return path_bin

    if dry_run:
        return "esphome"

    searched = "\n  - ".join(str(p) for p in candidate_esphome_bins(config_dir, testing_dir))
    raise SystemExit(
        "Could not find esphome. Set ESPHOME_BIN or [esphome].bin in the TOML config.\n"
        f"Searched:\n  - {searched}\n  - PATH"
    )


def resolve_esptool_bin(*, testing_dir: Path, dry_run: bool) -> str:
    repo_root = testing_dir.parent
    candidates = [
        repo_root / ".venv" / "bin" / "esptool.py",
        repo_root / ".venv" / "bin" / "esptool",
        repo_root / "venv" / "bin" / "esptool.py",
        repo_root / "venv" / "bin" / "esptool",
        testing_dir / ".venv" / "bin" / "esptool.py",
        testing_dir / ".venv" / "bin" / "esptool",
        testing_dir / "venv" / "bin" / "esptool.py",
        testing_dir / "venv" / "bin" / "esptool",
    ]
    for candidate in candidates:
        resolved = candidate.resolve()
        if dry_run or resolved.exists():
            if resolved.exists() or dry_run:
                return str(resolved)

    for name in ("esptool.py", "esptool"):
        path_bin = shutil.which(name)
        if path_bin:
            return path_bin

    if dry_run:
        return "esptool.py"

    searched = "\n  - ".join(str(p.resolve()) for p in candidates)
    raise SystemExit(
        "Could not find esptool.py/esptool for erase_flash reset step.\n"
        f"Searched:\n  - {searched}\n  - PATH"
    )


def load_settings(args: argparse.Namespace) -> Settings:
    config_file = Path(args.config).expanduser().resolve()
    if not config_file.exists():
        example = config_file.with_suffix(config_file.suffix + ".example")
        if not example.exists():
            example = config_file.parent / "stock_test_devices.example.toml"
        hint = f" Copy {example.name} to {config_file.name} and edit the serial ports." if example.exists() else ""
        raise SystemExit(f"Config file not found: {config_file}.{hint}")

    raw = load_toml(config_file)
    config_dir = config_file.parent
    testing_dir = resolve_relative(config_dir, raw.get("paths", {}).get("testing_dir"), ".")
    configs_dir = resolve_relative(config_dir, raw.get("paths", {}).get("configs_dir"), "configs")
    logs_dir = resolve_relative(config_dir, raw.get("paths", {}).get("logs_dir"), "logs")
    run_logs_dir = build_run_logs_dir(logs_dir)

    devices = dict(raw.get("devices", {}))
    required = {"router1", "child", "router2"}
    missing = sorted(required - devices.keys())
    if missing:
        raise SystemExit(f"Missing required [devices] entries: {', '.join(missing)}")

    if not args.allow_same_port:
        reverse: dict[str, list[str]] = {}
        for role, port in devices.items():
            reverse.setdefault(str(port), []).append(role)
        collisions = {port: roles for port, roles in reverse.items() if len(roles) > 1}
        if collisions:
            details = "; ".join(f"{port}: {', '.join(roles)}" for port, roles in collisions.items())
            raise SystemExit(f"Each test role should use a different serial port. Collisions: {details}")

    esphome_raw = raw.get("esphome", {})
    timing_raw = raw.get("timing", {})
    timing = Timing(
        sniffer_lead_in_seconds=int(timing_raw.get("sniffer_lead_in_seconds", 5)),
        router_settling_seconds=int(
            timing_raw.get(
                "router_settling_seconds",
                timing_raw.get("after_router2_seconds", 90),
            )
        ),
        child_attach_seconds=int(
            timing_raw.get(
                "child_attach_seconds",
                timing_raw.get("after_child_seconds", 30),
            )
        ),
        after_parent_removed_seconds=int(
            timing_raw.get(
                "after_parent_removed_seconds",
                timing_raw.get("after_router1_removed_seconds", 180),
            )
        ),
    )

    precompile = bool(esphome_raw.get("precompile", True))
    if args.skip_precompile:
        precompile = False
    if args.force_precompile:
        precompile = True

    clean_before_compile = bool(esphome_raw.get("clean_before_compile", False))
    if args.clean_before_compile:
        clean_before_compile = True

    sniffer_raw = raw.get("sniffer", {})
    sniffer_command = sniffer_raw.get("command", [])
    if sniffer_command and not isinstance(sniffer_command, list):
        raise SystemExit("[sniffer].command must be a TOML array of strings.")
    if any(not isinstance(part, str) for part in sniffer_command):
        raise SystemExit("[sniffer].command must contain only strings.")
    sniffer_enabled = bool(sniffer_raw.get("enabled", False))
    if sniffer_enabled and not sniffer_command:
        raise SystemExit("[sniffer].enabled is true, but [sniffer].command is empty.")

    variant_raw = raw.get("variant", {})
    router_count_raw = variant_raw.get("n_routers", 3)
    max_router_number = int(router_count_raw)
    if max_router_number < 2 or f"router{max_router_number}" not in CONFIG_NAMES:
        raise SystemExit(
            f"[variant].n_routers must reference an available stock_router_<n>.yaml variation. "
            f"Supported values are 2..{MAX_ROUTER_COUNT} total routers."
        )

    if args.runs > 1:
        logs_dir = allocate_batch_logs_dir(
            logs_dir.parent,
            variant_name="stock",
            router_count=max_router_number,
            total_runs=args.runs,
        )
        run_logs_dir = build_run_logs_dir(logs_dir)

    return Settings(
        config_file=config_file,
        testing_dir=testing_dir,
        configs_dir=configs_dir,
        logs_dir=logs_dir,
        run_logs_dir=run_logs_dir,
        esphome_bin=resolve_esphome_bin(
            cli_value=args.esphome_bin,
            env_value=os.environ.get("ESPHOME_BIN"),
            config_value=esphome_raw.get("bin"),
            config_dir=config_dir,
            testing_dir=testing_dir,
            dry_run=args.dry_run,
        ),
        esptool_bin=resolve_esptool_bin(testing_dir=testing_dir, dry_run=args.dry_run),
        upload_speed=str(esphome_raw.get("upload_speed")) if esphome_raw.get("upload_speed") else None,
        precompile=precompile,
        clean_before_compile=clean_before_compile,
        devices={key: str(value) for key, value in devices.items()},
        timing=timing,
        sniffer=SnifferSettings(
            enabled=sniffer_enabled,
            command=[str(part) for part in sniffer_command],
            stop_timeout_seconds=int(sniffer_raw.get("stop_timeout_seconds", 10)),
        ),
        capture_router2_log=bool(raw.get("diagnostics", {}).get("capture_router2_log", True)),
        max_router_number=max_router_number,
    )


def config_path(settings: Settings, name: str) -> Path:
    path = settings.configs_dir / CONFIG_NAMES[name]
    if not path.exists():
        raise SystemExit(f"Missing ESPHome config: {path}")
    return path


def run_command(
    cmd: list[str],
    *,
    dry_run: bool,
    cwd: Path | None = None,
    manifest: list[dict[str, Any]] | None = None,
    tracker: RunTracker | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str] | None:
    entry = {"time_utc": now_utc_iso(), "cmd": cmd, "cwd": str(cwd or Path.cwd()), "dry_run": dry_run}
    if manifest is not None:
        manifest.append(entry)
    if tracker is not None:
        tracker.append_event(entry)
    log(("DRY-RUN " if dry_run else "RUN ") + quote_cmd(cmd))
    if dry_run:
        return None
    try:
        completed = subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            check=check,
            text=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as exc:
        if tracker is not None:
            tracker.append_event(
                {
                    "time_utc": now_utc_iso(),
                    "type": "command_failed",
                    "cmd": cmd,
                    "returncode": exc.returncode,
                    "stdout_tail": (exc.stdout or "")[-2000:],
                    "stderr_tail": (exc.stderr or "")[-2000:],
                }
            )
        raise
    if tracker is not None:
        tracker.append_event(
            {
                "time_utc": now_utc_iso(),
                "type": "command_completed",
                "cmd": cmd,
                "returncode": completed.returncode,
            }
        )
    return completed


def esphome_base(settings: Settings) -> list[str]:
    return [settings.esphome_bin]


def erase_flash(
    settings: Settings,
    role: str,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker | None = None,
) -> None:
    cmd = [settings.esptool_bin, "--chip", "esp32c6", "--port", settings.devices[role], "erase_flash"]
    run_command(cmd, dry_run=dry_run, manifest=manifest, tracker=tracker)


def precompile_all(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker | None = None,
) -> None:
    log("Precompiling firmware before timed test sequence.")
    compile_order = [*CORE_COMPILE_ORDER, *additional_router_firmware_names(settings)]
    for name in compile_order:
        yaml_path = config_path(settings, name)
        if settings.clean_before_compile:
            run_command(
                esphome_base(settings) + ["clean", str(yaml_path)],
                dry_run=dry_run,
                manifest=manifest,
                tracker=tracker,
            )
        run_command(
            esphome_base(settings) + ["compile", str(yaml_path)],
            dry_run=dry_run,
            manifest=manifest,
            tracker=tracker,
        )
    log("Precompile phase complete. No compile commands will be run in the timed sequence.")


def upload(
    settings: Settings,
    role: str,
    firmware_name: str,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker | None = None,
) -> None:
    yaml_path = config_path(settings, firmware_name)
    cmd = esphome_base(settings) + ["upload", str(yaml_path), "--device", settings.devices[role]]
    if settings.upload_speed:
        cmd += ["--upload_speed", settings.upload_speed]
    run_command(cmd, dry_run=dry_run, manifest=manifest, tracker=tracker)


def sleep_step(
    seconds: int,
    reason: str,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker | None = None,
) -> None:
    entry = {"time_utc": now_utc_iso(), "sleep_seconds": seconds, "reason": reason, "dry_run": dry_run}
    manifest.append(entry)
    if tracker is not None:
        tracker.append_event(entry)
    log(f"WAIT {seconds}s: {reason}")
    if not dry_run:
        time.sleep(seconds)


def extra_empty_roles(settings: Settings) -> list[str]:
    return sorted(role for role in settings.devices if role not in {"router1", "child", "router2"})


def additional_router_firmware_names(settings: Settings) -> list[str]:
    return [f"router{number}" for number in range(3, settings.max_router_number + 1)]


def additional_router_device_roles(settings: Settings) -> list[str]:
    extras = extra_empty_roles(settings)
    selected_roles: list[str] = []
    remaining_roles = list(extras)
    for firmware_name in additional_router_firmware_names(settings):
        preferred_role = firmware_name
        if preferred_role in remaining_roles:
            selected_roles.append(preferred_role)
            remaining_roles.remove(preferred_role)
        elif remaining_roles:
            selected_roles.append(remaining_roles.pop(0))
    return selected_roles


def additional_router_assignments(settings: Settings) -> list[dict[str, str]]:
    roles = additional_router_device_roles(settings)
    firmwares = additional_router_firmware_names(settings)
    return [
        {"device_role": role, "firmware_name": firmware_name}
        for role, firmware_name in zip(roles, firmwares, strict=False)
    ]


def require_additional_router_assignments(settings: Settings) -> list[dict[str, str]]:
    assignments = additional_router_assignments(settings)
    required_count = len(additional_router_firmware_names(settings))
    if len(assignments) < required_count:
        raise SystemExit(
            "Stock testing requires enough ESP32-C6 boards in [devices] for the requested total router count. "
            f"n_routers={settings.max_router_number} requires {required_count} extra role(s) for router3..router{settings.max_router_number}. "
            "Add extra roles such as `unused1`, `unused2`, `router3`, or `router4`."
        )
    return assignments


def device_assignments(settings: Settings) -> list[dict[str, str]]:
    assignments = [
        {
            "logical_name": "router1",
            "config_name": "router1",
            "device_role": "router1",
            "device_port": settings.devices["router1"],
        },
        {
            "logical_name": "child",
            "config_name": "child",
            "device_role": "child",
            "device_port": settings.devices["child"],
        },
        {
            "logical_name": "router2",
            "config_name": "router2",
            "device_role": "router2",
            "device_port": settings.devices["router2"],
        },
    ]
    for assignment in additional_router_assignments(settings):
        device_role = assignment["device_role"]
        firmware_name = assignment["firmware_name"]
        assignments.append(
            {
                "logical_name": firmware_name,
                "config_name": firmware_name,
                "device_role": device_role,
                "device_port": settings.devices[device_role],
            }
        )
    return assignments


def log_process_name(logical_name: str) -> str:
    return f"{logical_name}_log"


def log_file_path(settings: Settings, logical_name: str) -> Path:
    stamp = settings.run_logs_dir.name
    return settings.run_logs_dir / f"stock_{logical_name}_{stamp}.log"


def start_sniffer_capture(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker | None = None,
) -> tuple[subprocess.Popen[str] | None, Path | None]:
    if not settings.sniffer.enabled:
        return None, None

    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    stamp = settings.run_logs_dir.name
    log_path = settings.run_logs_dir / f"stock_sniffer_{stamp}.log"
    cmd = settings.sniffer.command
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "sniffer_log_path": str(log_path), "dry_run": dry_run})
    if tracker is not None:
        tracker.set_logs(sniffer_log=log_path)
        tracker.append_event({"time_utc": now_utc_iso(), "type": "sniffer_log_allocated", "log_path": str(log_path)})

    host = sniffer_remote_host(settings)
    if host is not None:
        cleanup_cmd = [
            "ssh",
            host,
            "pkill -f 'nrf802154_sniffer.py|tshark.*802.15.4' >/dev/null 2>&1 || true; sleep 1",
        ]
        manifest.append({"time_utc": now_utc_iso(), "cmd": cleanup_cmd, "purpose": "sniffer-pre-clean", "dry_run": dry_run})
        if tracker is not None:
            tracker.append_event({"time_utc": now_utc_iso(), "type": "sniffer_pre_clean", "cmd": cleanup_cmd})
        log(("DRY-RUN " if dry_run else "RUN ") + quote_cmd(cleanup_cmd))
        if not dry_run:
            subprocess.run(cleanup_cmd, check=False, text=True)

    def start_once(attempt: int) -> tuple[subprocess.Popen[str] | None, Path | None]:
        log(("DRY-RUN " if dry_run else "START ") + quote_cmd(cmd) + f" > {log_path} (attempt {attempt})")
        if dry_run:
            return None, log_path

        mode = "a" if log_path.exists() else "w"
        log_file = log_path.open(mode, encoding="utf-8", errors="replace")
        if mode == "w":
            log_file.write(f"# Command: {quote_cmd(cmd)}\n")
        log_file.write(f"# Started UTC: {now_utc_iso()} (attempt {attempt})\n")
        log_file.flush()

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
        )

        def pump() -> None:
            try:
                assert process.stdout is not None
                for line in process.stdout:
                    log_file.write(line)
                    log_file.flush()
            finally:
                log_file.write(f"# Log reader stopped UTC: {now_utc_iso()} (attempt {attempt})\n")
                log_file.close()

        thread = threading.Thread(target=pump, name=f"sniffer-log-pump-{attempt}", daemon=True)
        thread.start()
        if tracker is not None:
            tracker.start_process("sniffer", cmd, log_path, process, metadata={"process_kind": "sniffer"})
        return process, log_path

    process, _ = start_once(1)
    if dry_run:
        return process, log_path
    assert process is not None
    time.sleep(2)
    if process.poll() is None:
        return process, log_path

    log(f"Sniffer exited quickly with code {process.returncode}; retrying once after cleanup.")
    if host is not None:
        retry_cleanup_cmd = [
            "ssh",
            host,
            "pkill -f 'nrf802154_sniffer.py|tshark.*802.15.4' >/dev/null 2>&1 || true; sleep 1",
        ]
        manifest.append({"time_utc": now_utc_iso(), "cmd": retry_cleanup_cmd, "purpose": "sniffer-retry-clean", "dry_run": dry_run})
        subprocess.run(retry_cleanup_cmd, check=False, text=True)
    process, _ = start_once(2)
    return process, log_path


def stop_sniffer_capture(settings: Settings, process: subprocess.Popen[str] | None, *, dry_run: bool) -> None:
    if dry_run or process is None:
        return
    if process.poll() is not None:
        log(f"Sniffer process already exited with code {process.returncode}.")
        if _CURRENT_TRACKER is not None:
            _CURRENT_TRACKER.finish_process("sniffer", process, expected=False, log_path=_CURRENT_TRACKER.sniffer_log)
        return
    log("Stopping sniffer capture process.")
    process.terminate()
    try:
        process.wait(timeout=settings.sniffer.stop_timeout_seconds)
    except subprocess.TimeoutExpired:
        log("Sniffer process did not stop after SIGTERM; killing it.")
        process.kill()
        process.wait(timeout=10)
    if _CURRENT_TRACKER is not None:
        _CURRENT_TRACKER.finish_process("sniffer", process, expected=True, log_path=_CURRENT_TRACKER.sniffer_log)


def find_pcap_path_in_sniffer_log(log_path: Path | None) -> str | None:
    if log_path is None or not log_path.exists():
        return None
    text = log_path.read_text(encoding="utf-8", errors="replace")
    matches = PCAP_PATH_RE.findall(text)
    return matches[-1] if matches else None


def sniffer_remote_host(settings: Settings) -> str | None:
    cmd = settings.sniffer.command
    if len(cmd) >= 2 and cmd[0] == "ssh":
        return cmd[1]
    return None


def pull_sniffer_pcap(
    settings: Settings,
    *,
    sniffer_log_path: Path | None,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker | None = None,
) -> tuple[str | None, Path | None]:
    remote_pcap = find_pcap_path_in_sniffer_log(sniffer_log_path)
    if remote_pcap is None:
        return None, None

    stamp = settings.run_logs_dir.name
    local_pcap = settings.run_logs_dir / f"stock_sniffer_{stamp}.pcapng"
    host = sniffer_remote_host(settings)
    if host:
        cmd = ["scp", f"{host}:{remote_pcap}", str(local_pcap)]
    else:
        cmd = ["cp", remote_pcap, str(local_pcap)]

    entry = {
        "time_utc": now_utc_iso(),
        "cmd": cmd,
        "remote_pcap_path": remote_pcap,
        "local_pcap_path": str(local_pcap),
        "dry_run": dry_run,
    }
    manifest.append(entry)
    if tracker is not None:
        tracker.append_event(entry)
    log(("DRY-RUN " if dry_run else "FETCH ") + quote_cmd(cmd))
    if dry_run:
        return remote_pcap, local_pcap

    local_pcap.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd, check=True, text=True)
    if tracker is not None:
        tracker.set_sniffer_pcap(remote_pcap, local_pcap)
    return remote_pcap, local_pcap


def start_child_log(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker | None = None,
) -> tuple[subprocess.Popen[str] | None, Path]:
    return start_device_log(
        settings,
        logical_name="child",
        config_name="child",
        device_role="child",
        dry_run=dry_run,
        manifest=manifest,
        tracker=tracker,
    )


def start_device_log(
    settings: Settings,
    *,
    logical_name: str,
    config_name: str,
    device_role: str,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker | None = None,
) -> tuple[subprocess.Popen[str] | None, Path]:
    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_file_path(settings, logical_name)
    cmd = esphome_base(settings) + ["logs", str(config_path(settings, config_name)), "--device", settings.devices[device_role]]
    manifest.append(
        {
            "time_utc": now_utc_iso(),
            "cmd": cmd,
            "log_path": str(log_path),
            "logical_name": logical_name,
            "config_name": config_name,
            "device_role": device_role,
            "device_port": settings.devices[device_role],
            "dry_run": dry_run,
        }
    )
    if tracker is not None:
        tracker.set_device_log(logical_name, log_path)
    log(
        ("DRY-RUN " if dry_run else "START ")
        + quote_cmd(cmd)
        + f" > {log_path}"
        + f"  [logical={logical_name} device_role={device_role}]"
    )

    if dry_run:
        return None, log_path

    log_file = log_path.open("w", encoding="utf-8", errors="replace")
    log_file.write(f"# Command: {quote_cmd(cmd)}\n")
    log_file.write(f"# Started UTC: {now_utc_iso()}\n")
    log_file.flush()

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )

    def pump() -> None:
        try:
            assert process.stdout is not None
            for line in process.stdout:
                log_file.write(line)
                log_file.flush()
        finally:
            log_file.write(f"# Log reader stopped UTC: {now_utc_iso()}\n")
            log_file.close()

    thread = threading.Thread(target=pump, name=f"{logical_name}-log-pump", daemon=True)
    thread.start()
    if tracker is not None:
        tracker.start_process(
            log_process_name(logical_name),
            cmd,
            log_path,
            process,
            metadata={
                "process_kind": "device_log",
                "logical_name": logical_name,
                "config_name": config_name,
                "device_role": device_role,
                "device_port": settings.devices[device_role],
            },
        )
    return process, log_path


def start_router1_log(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker | None = None,
) -> tuple[subprocess.Popen[str] | None, Path]:
    return start_device_log(
        settings,
        logical_name="router1",
        config_name="router1",
        device_role="router1",
        dry_run=dry_run,
        manifest=manifest,
        tracker=tracker,
    )


def start_router2_log(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker | None = None,
) -> tuple[subprocess.Popen[str] | None, Path]:
    return start_device_log(
        settings,
        logical_name="router2",
        config_name="router2",
        device_role="router2",
        dry_run=dry_run,
        manifest=manifest,
        tracker=tracker,
    )


def stop_child_log(process: subprocess.Popen[str] | None, *, dry_run: bool) -> None:
    stop_device_log(
        process,
        logical_name="child",
        dry_run=dry_run,
        tracker_log_path=_CURRENT_TRACKER.child_log if _CURRENT_TRACKER is not None else None,
    )


def stop_device_log(
    process: subprocess.Popen[str] | None,
    *,
    logical_name: str,
    dry_run: bool,
    tracker_log_path: Path | None,
) -> None:
    if dry_run or process is None:
        return
    if process.poll() is not None:
        log(f"{logical_name} log process already exited with code {process.returncode}.")
        if _CURRENT_TRACKER is not None:
            _CURRENT_TRACKER.finish_process(log_process_name(logical_name), process, expected=False, log_path=tracker_log_path)
        return
    log(f"Stopping {logical_name} log process.")
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        log(f"{logical_name} log process did not stop after SIGTERM; killing it.")
        process.kill()
        process.wait(timeout=10)
    if _CURRENT_TRACKER is not None:
        _CURRENT_TRACKER.finish_process(log_process_name(logical_name), process, expected=True, log_path=tracker_log_path)


def stop_router1_log(process: subprocess.Popen[str] | None, *, dry_run: bool) -> None:
    stop_device_log(
        process,
        logical_name="router1",
        dry_run=dry_run,
        tracker_log_path=_CURRENT_TRACKER.router1_log if _CURRENT_TRACKER is not None else None,
    )


def stop_router2_log(process: subprocess.Popen[str] | None, *, dry_run: bool) -> None:
    stop_device_log(
        process,
        logical_name="router2",
        dry_run=dry_run,
        tracker_log_path=_CURRENT_TRACKER.router2_log if _CURRENT_TRACKER is not None else None,
    )



def router_execution_plan(settings: Settings) -> list[dict[str, str]]:
    """Return routers that participate in the stock run."""
    plan = [
        {"logical_name": "router1", "config_name": "router1", "device_role": "router1"},
        {"logical_name": "router2", "config_name": "router2", "device_role": "router2"},
    ]
    for assignment in additional_router_assignments(settings):
        firmware_name = assignment["firmware_name"]
        plan.append(
            {
                "logical_name": firmware_name,
                "config_name": firmware_name,
                "device_role": assignment["device_role"],
            }
        )
    return plan


def normalize_extaddr(value: str | None) -> str | None:
    if not value:
        return None
    hexed = re.sub(r"[^0-9a-fA-F]", "", value).lower()
    if len(hexed) != 16:
        return None
    return ":".join(hexed[i : i + 2] for i in range(0, 16, 2))


def extaddr_key(value: str | None) -> str | None:
    norm = normalize_extaddr(value)
    return norm.replace(":", "") if norm else None


def iid_to_extaddr(iid_hex: str) -> str | None:
    """Convert an IPv6 link-local IID into a Thread EUI-64 extended address."""
    iid = re.sub(r"[^0-9a-fA-F]", "", iid_hex).lower()
    if len(iid) != 16:
        return None
    first = int(iid[:2], 16) ^ 0x02
    ext = f"{first:02x}" + iid[2:]
    return normalize_extaddr(ext)


def ipv6_link_local_to_extaddr(addr: str) -> str | None:
    if not addr.lower().startswith("fe80"):
        return None
    parts = addr.split("%", 1)[0].split(":")
    if "" in parts:
        empty_index = parts.index("")
        missing = 8 - (len(parts) - 1)
        parts = parts[:empty_index] + ["0"] * missing + parts[empty_index + 1 :]
    if len(parts) < 8:
        return None
    iid_hex = "".join(part.zfill(4) for part in parts[-4:])
    return iid_to_extaddr(iid_hex)


def parse_radio_extaddr(log_path: Path) -> str | None:
    if not log_path.exists():
        return None
    text = log_path.read_text(encoding="utf-8", errors="replace")
    patterns = [
        r"RadioExtAddress:\s*([0-9a-fA-F:]{16,23})",
        r"Ext(?:ended)?\s*Address:\s*([0-9a-fA-F:]{16,23})",
        r"ExtAddr:\s*([0-9a-fA-F:]{16,23})",
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        for match in reversed(matches):
            norm = normalize_extaddr(match)
            if norm:
                return norm
    return None


def parse_child_parent_extaddr(child_log: Path) -> tuple[str | None, str | None]:
    """Return (parent_extaddr, source). Conservative: skip if unclear."""
    if not child_log.exists():
        return None, None
    text = child_log.read_text(encoding="utf-8", errors="replace")

    explicit_patterns = [
        r"Saved ParentInfo.*?(?:ExtAddr|ExtAddress|Ext Address)[:= ]+([0-9a-fA-F:]{16,23})",
        r"ParentInfo.*?(?:ExtAddr|ExtAddress|Ext Address)[:= ]+([0-9a-fA-F:]{16,23})",
        r"parent.*?(?:ExtAddr|ExtAddress|Ext Address)[:= ]+([0-9a-fA-F:]{16,23})",
    ]
    for pattern in explicit_patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE | re.DOTALL)
        for match in reversed(matches):
            norm = normalize_extaddr(match)
            if norm:
                return norm, "child_log_explicit_parent_extaddr"

    link_local_patterns = [
        r"Saved ParentInfo.*?(fe80:[0-9a-fA-F:%]+)",
        r"ParentInfo.*?(fe80:[0-9a-fA-F:%]+)",
        r"parent.*?(fe80:[0-9a-fA-F:%]+)",
        r"Send Child Update Request as child\s*\((fe80:[0-9a-fA-F:%]+)\)",
    ]
    for pattern in link_local_patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        for match in reversed(matches):
            ext = ipv6_link_local_to_extaddr(match)
            if ext:
                return ext, "child_log_parent_link_local"
    return None, None


def map_router_extaddrs(device_logs: dict[str, Path]) -> dict[str, dict[str, str]]:
    mapped: dict[str, dict[str, str]] = {}
    for logical_name, log_path in device_logs.items():
        if logical_name == "child" or not logical_name.startswith("router"):
            continue
        extaddr = parse_radio_extaddr(log_path)
        key = extaddr_key(extaddr)
        if not key or not extaddr:
            continue
        mapped[key] = {"extaddr": extaddr, "logical_name": logical_name}
    return mapped


def parse_latest_thread_role(log_path: Path | None) -> tuple[str | None, str | None]:
    if log_path is None or not log_path.exists():
        return None, None
    try:
        lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None, None

    role_values = "disabled|detached|child|router|leader"
    patterns = [
        re.compile(rf"\b(?:OpenThread|Thread)\b.*\b(?:role|state)\b\s*[:=]\s*({role_values})\b", re.I),
        re.compile(rf"\b(?:role|state)\b\s*[:=]\s*({role_values})\b", re.I),
        re.compile(rf"\b(?:role|state)\b\s*(?:changed|change)?\s*(?:from\s+\w+\s*)?(?:to|->)\s*({role_values})\b", re.I),
        re.compile(rf"\b(?:become|became)\s+({role_values})\b", re.I),
    ]

    for line in reversed(lines):
        for pattern in patterns:
            match = pattern.search(line)
            if match:
                return match.group(1).lower(), line.strip()
    return None, None


def map_router_thread_roles(device_logs: dict[str, Path]) -> dict[str, dict[str, str | None]]:
    roles: dict[str, dict[str, str | None]] = {}
    for logical_name, log_path in sorted(device_logs.items()):
        if logical_name == "child" or not logical_name.startswith("router"):
            continue
        role, source = parse_latest_thread_role(log_path)
        roles[logical_name] = {
            "role": role,
            "source": source,
            "log_path": str(log_path),
        }
    return roles


def record_parent_removal_decision(
    *,
    tracker: RunTracker,
    manifest: list[dict[str, Any]],
    action: str,
    reason: str,
    details: dict[str, Any],
) -> None:
    event = {
        "time_utc": now_utc_iso(),
        "type": "parent_removal_decision",
        "action": action,
        "reason": reason,
        **details,
    }
    manifest.append(event)
    tracker.append_event(event)


def mark_skipped_run(tracker: RunTracker, reason: str, *, details: dict[str, Any] | None = None) -> None:
    with tracker.lock:
        tracker.status = "skipped"
        tracker.current_step = "skipped"
        tracker.abort_reason = reason
        tracker.events.append(
            {
                "time_utc": now_utc_iso(),
                "type": "skip",
                "reason": reason,
                **(details or {}),
            }
        )
    tracker.flush_manifest()


def run_timed_sequence(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
    tracker: RunTracker,
) -> tuple[Path | None, Path | None, Path | None, Path | None, str | None, Path | None]:
    log("Starting dynamic-parent stock upload/logging sequence. Upload-only commands are used from here onward.")

    child_log_path: Path | None = None
    router1_log_path: Path | None = None
    router2_log_path: Path | None = None
    device_loggers: dict[str, subprocess.Popen[str] | None] = {}
    device_log_paths: dict[str, Path] = {}
    sniffer_process: subprocess.Popen[str] | None = None
    sniffer_log_path: Path | None = None
    sniffer_remote_pcap: str | None = None
    sniffer_local_pcap: Path | None = None

    try:
        tracker.set_step("reset_all_devices")
        for role in ["router1", "child", "router2", *extra_empty_roles(settings)]:
            erase_flash(settings, role, dry_run=dry_run, manifest=manifest, tracker=tracker)
            upload(settings, role, "empty", dry_run=dry_run, manifest=manifest, tracker=tracker)

        require_additional_router_assignments(settings)
        router_plan = router_execution_plan(settings)

        tracker.set_step("start_sniffer")
        sniffer_process, sniffer_log_path = start_sniffer_capture(
            settings, dry_run=dry_run, manifest=manifest, tracker=tracker
        )
        if settings.sniffer.enabled:
            sleep_step(
                settings.timing.sniffer_lead_in_seconds,
                "sniffer started; wait before flashing routers",
                dry_run=dry_run,
                manifest=manifest,
                tracker=tracker,
            )

        tracker.set_step("flash_routers", extra={"router_plan": router_plan})
        for router in router_plan:
            upload(
                settings,
                router["device_role"],
                router["config_name"],
                dry_run=dry_run,
                manifest=manifest,
                tracker=tracker,
            )
            logger, log_path = start_device_log(
                settings,
                logical_name=router["logical_name"],
                config_name=router["config_name"],
                device_role=router["device_role"],
                dry_run=dry_run,
                manifest=manifest,
                tracker=tracker,
            )
            device_loggers[router["logical_name"]] = logger
            device_log_paths[router["logical_name"]] = log_path
            if router["logical_name"] == "router1":
                router1_log_path = log_path
            elif router["logical_name"] == "router2":
                router2_log_path = log_path

        sleep_step(
            settings.timing.router_settling_seconds,
            "all stock routers flashed/logging; fixed router-settling delay before flashing child",
            dry_run=dry_run,
            manifest=manifest,
            tracker=tracker,
        )

        tracker.set_step("flash_child")
        upload(settings, "child", "child", dry_run=dry_run, manifest=manifest, tracker=tracker)
        logger, log_path = start_child_log(settings, dry_run=dry_run, manifest=manifest, tracker=tracker)
        device_loggers["child"] = logger
        device_log_paths["child"] = log_path
        child_log_path = log_path

        sleep_step(
            settings.timing.child_attach_seconds,
            "child flashed/logging; wait for natural stock attach before detecting current parent",
            dry_run=dry_run,
            manifest=manifest,
            tracker=tracker,
        )

        tracker.set_step("detect_child_parent")
        parent_extaddr, parent_source = parse_child_parent_extaddr(child_log_path)
        router_extaddrs = map_router_extaddrs(device_log_paths)
        parent_key = extaddr_key(parent_extaddr)
        parent_match = router_extaddrs.get(parent_key or "")

        detection_details = {
            "detected_parent_extaddr": parent_extaddr,
            "detected_parent_source": parent_source,
            "router_extaddrs": router_extaddrs,
        }

        if not parent_extaddr:
            skip_details = {
                **detection_details,
                "classification_note": SKIP_NO_CHILD_PARENT_NOTE,
                "router_removed": None,
            }
            record_parent_removal_decision(
                tracker=tracker,
                manifest=manifest,
                action="skipped",
                reason=SKIP_NO_CHILD_PARENT,
                details=skip_details,
            )
            mark_skipped_run(tracker, SKIP_NO_CHILD_PARENT, details=skip_details)
            tracker.set_step("stop_sniffer_after_skip")
            stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
            sniffer_process = None
            sniffer_remote_pcap, sniffer_local_pcap = pull_sniffer_pcap(
                settings,
                sniffer_log_path=sniffer_log_path,
                dry_run=dry_run,
                manifest=manifest,
                tracker=tracker,
            )
            return child_log_path, router1_log_path, router2_log_path, sniffer_log_path, sniffer_remote_pcap, sniffer_local_pcap

        if not parent_match:
            skip_details = {
                **detection_details,
                "classification_note": SKIP_PARENT_NOT_MAPPED_TO_DEVICE_NOTE,
                "router_removed": None,
            }
            record_parent_removal_decision(
                tracker=tracker,
                manifest=manifest,
                action="skipped",
                reason=SKIP_PARENT_NOT_MAPPED_TO_DEVICE,
                details=skip_details,
            )
            mark_skipped_run(tracker, SKIP_PARENT_NOT_MAPPED_TO_DEVICE, details=skip_details)
            tracker.set_step("stop_sniffer_after_skip")
            stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
            sniffer_process = None
            sniffer_remote_pcap, sniffer_local_pcap = pull_sniffer_pcap(
                settings,
                sniffer_log_path=sniffer_log_path,
                dry_run=dry_run,
                manifest=manifest,
                tracker=tracker,
            )
            return child_log_path, router1_log_path, router2_log_path, sniffer_log_path, sniffer_remote_pcap, sniffer_local_pcap

        removed_parent_logical_name = parent_match["logical_name"]
        parent_plan = next(
            router for router in router_plan if router["logical_name"] == removed_parent_logical_name
        )

        removal_details = {
            **detection_details,
            "parent_logical_name": parent_plan["logical_name"],
            "parent_config_name": parent_plan["config_name"],
            "parent_device_role": parent_plan["device_role"],
            "parent_device_port": settings.devices[parent_plan["device_role"]],
        }

        router_thread_roles = map_router_thread_roles(device_log_paths)
        parent_log_path = device_log_paths.get(removed_parent_logical_name)
        parent_thread_role, parent_thread_role_source = parse_latest_thread_role(parent_log_path)
        leader_logical_names = sorted(
            logical_name
            for logical_name, evidence in router_thread_roles.items()
            if evidence.get("role") == "leader"
        )
        parent_is_leader = parent_thread_role == "leader" or removed_parent_logical_name in leader_logical_names

        removal_details.update(
            {
                "parent_log_path": str(parent_log_path) if parent_log_path else None,
                "parent_thread_role": parent_thread_role,
                "parent_thread_role_source": parent_thread_role_source,
                "router_thread_roles": router_thread_roles,
                "leader_logical_names": leader_logical_names,
                "leader_check": "parent_is_leader" if parent_is_leader else "parent_not_observed_as_leader",
            }
        )

        if parent_is_leader:
            skip_details = {
                **removal_details,
                "classification_note": SKIP_PARENT_IS_LEADER_NOTE,
                "router_removed": None,
            }
            record_parent_removal_decision(
                tracker=tracker,
                manifest=manifest,
                action="skipped",
                reason=SKIP_PARENT_IS_LEADER,
                details=skip_details,
            )
            mark_skipped_run(tracker, SKIP_PARENT_IS_LEADER, details=skip_details)
            tracker.set_step("stop_sniffer_after_skip")
            stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
            sniffer_process = None
            sniffer_remote_pcap, sniffer_local_pcap = pull_sniffer_pcap(
                settings,
                sniffer_log_path=sniffer_log_path,
                dry_run=dry_run,
                manifest=manifest,
                tracker=tracker,
            )
            return child_log_path, router1_log_path, router2_log_path, sniffer_log_path, sniffer_remote_pcap, sniffer_local_pcap

        record_parent_removal_decision(
            tracker=tracker,
            manifest=manifest,
            action="removed",
            reason="REMOVED_CHILD_CURRENT_PARENT",
            details=removal_details,
        )

        tracker.set_step("remove_child_parent", extra=removal_details)
        stop_device_log(
            device_loggers.get(removed_parent_logical_name),
            logical_name=removed_parent_logical_name,
            dry_run=dry_run,
            tracker_log_path=device_log_paths.get(removed_parent_logical_name),
        )
        device_loggers[removed_parent_logical_name] = None
        upload(
            settings,
            parent_plan["device_role"],
            "empty",
            dry_run=dry_run,
            manifest=manifest,
            tracker=tracker,
        )

        sleep_step(
            settings.timing.after_parent_removed_seconds,
            "child's detected current parent removed; keep recording child and remaining routers",
            dry_run=dry_run,
            manifest=manifest,
            tracker=tracker,
        )

        tracker.set_step("stop_sniffer")
        stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
        sniffer_process = None
        sniffer_remote_pcap, sniffer_local_pcap = pull_sniffer_pcap(
            settings,
            sniffer_log_path=sniffer_log_path,
            dry_run=dry_run,
            manifest=manifest,
            tracker=tracker,
        )
        tracker.set_step("timed_sequence_complete")
        return child_log_path, router1_log_path, router2_log_path, sniffer_log_path, sniffer_remote_pcap, sniffer_local_pcap

    finally:
        tracker.set_logs(
            child_log=child_log_path,
            router1_log=router1_log_path,
            router2_log=router2_log_path,
            sniffer_log=sniffer_log_path,
        )
        for logical_name, log_path in device_log_paths.items():
            tracker.set_device_log(logical_name, log_path)
        tracker.set_sniffer_pcap(sniffer_remote_pcap, sniffer_local_pcap)
        stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
        for logical_name, process in device_loggers.items():
            stop_device_log(
                process,
                logical_name=logical_name,
                dry_run=dry_run,
                tracker_log_path=device_log_paths.get(logical_name),
            )


def write_manifest(
    settings: Settings,
    manifest: list[dict[str, Any]],
    *,
    dry_run: bool,
    run_number: int | None,
    total_runs: int,
    child_log: Path | None,
    router1_log: Path | None,
    router2_log: Path | None,
    device_logs: dict[str, Path] | None,
    sniffer_log: Path | None,
    sniffer_remote_pcap: str | None,
    sniffer_local_pcap: Path | None,
) -> Path:
    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    stamp = settings.run_logs_dir.name
    path = settings.run_logs_dir / f"stock_test_manifest_{stamp}.json"
    if path.exists():
        return path
    payload = {
        "created_utc": now_utc_iso(),
        "dry_run": dry_run,
        "config_file": str(settings.config_file),
        "testing_dir": str(settings.testing_dir),
        "configs_dir": str(settings.configs_dir),
        "logs_dir": str(settings.logs_dir),
        "run_logs_dir": str(settings.run_logs_dir),
        "run_number": run_number,
        "total_runs": total_runs,
        "status": "completed",
        "esphome_bin": settings.esphome_bin,
        "esptool_bin": settings.esptool_bin,
        "precompile": settings.precompile,
        "clean_before_compile": settings.clean_before_compile,
        "devices": settings.devices,
        "timing": settings.timing.__dict__,
        "max_router_number": settings.max_router_number,
        "additional_router_assignments": additional_router_assignments(settings),
        "device_assignments": device_assignments(settings),
        "child_log": str(child_log) if child_log else None,
        "router1_log": str(router1_log) if router1_log else None,
        "router2_log": str(router2_log) if router2_log else None,
        "device_logs": {name: str(path) for name, path in sorted((device_logs or {}).items())},
        "sniffer": {
            "enabled": settings.sniffer.enabled,
            "command": settings.sniffer.command,
            "stop_timeout_seconds": settings.sniffer.stop_timeout_seconds,
            "log": str(sniffer_log) if sniffer_log else None,
            "remote_pcap": sniffer_remote_pcap,
            "local_pcap": str(sniffer_local_pcap) if sniffer_local_pcap else None,
        },
        "events": manifest,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run stock ESPHome/OpenThread parent-switching test.")
    parser.add_argument("--config", default="stock_test_devices.toml", help="Path to device/config TOML file.")
    parser.add_argument("--esphome-bin", help="Override ESPHome executable. Overrides ESPHOME_BIN and TOML.")
    parser.add_argument("--runs", type=int, default=1, help="Number of timed test runs to execute. Precompile still happens once.")
    parser.add_argument("--dry-run", action="store_true", help="Print commands and write a manifest without executing ESPHome.")
    parser.add_argument("--precompile-only", action="store_true", help="Compile all firmware and exit before any flashing.")
    parser.add_argument("--skip-precompile", action="store_true", help="Skip precompile phase. Not recommended for measurement runs.")
    parser.add_argument("--force-precompile", action="store_true", help="Force precompile phase even if disabled in TOML.")
    parser.add_argument("--clean-before-compile", action="store_true", help="Run `esphome clean` before each compile.")
    parser.add_argument("--allow-same-port", action="store_true", help="Permit multiple roles to use the same serial port.")
    return parser.parse_args(argv)


def install_signal_handlers() -> dict[int, Any]:
    def handler(signum: int, _frame: Any) -> None:
        reason = f"received signal {signum}"
        log(reason)
        if _CURRENT_TRACKER is not None:
            _CURRENT_TRACKER.mark_aborted(reason)
        raise SystemExit(128 + signum)

    previous: dict[int, Any] = {}
    for signum in (signal.SIGINT, signal.SIGTERM):
        previous[signum] = signal.getsignal(signum)
        signal.signal(signum, handler)
    return previous


def restore_signal_handlers(previous: dict[int, Any]) -> None:
    for signum, handler in previous.items():
        signal.signal(signum, handler)


def main(argv: list[str]) -> int:
    global _CURRENT_TRACKER
    args = parse_args(argv)
    if args.runs < 1:
        raise SystemExit("--runs must be at least 1.")
    settings = load_settings(args)
    if args.runs > 1:
        set_batch_log(settings.logs_dir / f"{settings.logs_dir.name}.log")
    else:
        set_batch_log(None)
    previous_handlers = install_signal_handlers()

    try:
        log(f"Using ESPHome: {settings.esphome_bin}")
        log(f"Using esptool: {settings.esptool_bin}")
        log(f"Using configs: {settings.configs_dir}")
        log(f"Using logs base: {settings.logs_dir}")
        log(f"Requested timed runs: {args.runs}")
        log(f"Initial run logs dir: {settings.run_logs_dir}")

        precompile_manifest: list[dict[str, Any]] = []
        if settings.precompile:
            precompile_all(settings, dry_run=args.dry_run, manifest=precompile_manifest)
        else:
            log("WARNING: precompile phase skipped. Uploads may fail if the most recent firmware builds do not exist.")

        if args.precompile_only:
            manifest_path = write_manifest(
                settings,
                precompile_manifest,
                dry_run=args.dry_run,
                run_number=None,
                total_runs=args.runs,
                child_log=None,
                router1_log=None,
                router2_log=None,
                device_logs={},
                sniffer_log=None,
                sniffer_remote_pcap=None,
                sniffer_local_pcap=None,
            )
            log("Precompile-only requested; not starting timed test sequence.")
            log(f"Wrote manifest: {manifest_path}")
            return 0

        for run_number in range(1, args.runs + 1):
            if args.runs > 1:
                settings.run_logs_dir = build_run_logs_dir(settings.logs_dir, run_index=run_number)
                log(f"Starting timed run {run_number}/{args.runs}")
                log(f"Using run logs dir: {settings.run_logs_dir}")
            else:
                log("Starting timed run 1/1")
                log(f"Using run logs dir: {settings.run_logs_dir}")

            tracker = RunTracker(
                settings,
                dry_run=args.dry_run,
                run_number=run_number,
                total_runs=args.runs,
                precompile_manifest=precompile_manifest,
            )
            _CURRENT_TRACKER = tracker
            manifest: list[dict[str, Any]] = []
            try:
                run_timed_sequence(settings, dry_run=args.dry_run, manifest=manifest, tracker=tracker)
                if tracker.status not in {"skipped", "failed"}:
                    tracker.mark_completed()
            except BaseException as exc:
                tracker.mark_aborted(f"run {run_number} aborted: {exc}", exc=exc)
                raise
            finally:
                log(f"Wrote manifest: {tracker.manifest_path}")
                if tracker.child_log:
                    log(f"Child log: {tracker.child_log}")
                if tracker.router1_log:
                    log(f"Router1 log: {tracker.router1_log}")
                if tracker.router2_log:
                    log(f"Router2 log: {tracker.router2_log}")
                for logical_name, log_path in sorted(tracker.device_logs.items()):
                    if logical_name not in {"child", "router1", "router2"}:
                        log(f"{logical_name} log: {log_path}")
                if tracker.sniffer_log:
                    log(f"Sniffer log: {tracker.sniffer_log}")
                if tracker.sniffer_local_pcap:
                    log(f"Sniffer pcap: {tracker.sniffer_local_pcap}")
                _CURRENT_TRACKER = None
                set_supervisor_log(None)

        return 0
    finally:
        restore_signal_handlers(previous_handlers)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
