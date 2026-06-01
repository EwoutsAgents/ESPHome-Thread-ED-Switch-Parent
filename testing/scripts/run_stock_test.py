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
import subprocess
import sys
import threading
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
}

COMPILE_ORDER = ["empty", "router1", "child", "router2"]
PCAP_PATH_RE = re.compile(r"Saving (?:test )?capture to (\S+\.pcapng)")


@dataclass
class Timing:
    sniffer_lead_in_seconds: int = 5
    after_router1_seconds: int = 5
    after_child_seconds: int = 10
    after_router2_seconds: int = 10
    after_router1_removed_seconds: int = 180


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


def now_utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def log(msg: str) -> None:
    print(f"[{now_utc_iso()}] {msg}", flush=True)


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
    run_logs_dir = logs_dir / dt.datetime.now().strftime("%Y%m%d-%H%M%S")

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
        after_router1_seconds=int(timing_raw.get("after_router1_seconds", 5)),
        after_child_seconds=int(timing_raw.get("after_child_seconds", 10)),
        after_router2_seconds=int(timing_raw.get("after_router2_seconds", 10)),
        after_router1_removed_seconds=int(timing_raw.get("after_router1_removed_seconds", 180)),
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
    check: bool = True,
) -> subprocess.CompletedProcess[str] | None:
    entry = {"time_utc": now_utc_iso(), "cmd": cmd, "cwd": str(cwd or Path.cwd()), "dry_run": dry_run}
    if manifest is not None:
        manifest.append(entry)
    log(("DRY-RUN " if dry_run else "RUN ") + quote_cmd(cmd))
    if dry_run:
        return None
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=check, text=True)


def esphome_base(settings: Settings) -> list[str]:
    return [settings.esphome_bin]


def erase_flash(settings: Settings, role: str, *, dry_run: bool, manifest: list[dict[str, Any]]) -> None:
    cmd = [settings.esptool_bin, "--chip", "esp32c6", "--port", settings.devices[role], "erase_flash"]
    run_command(cmd, dry_run=dry_run, manifest=manifest)


def precompile_all(settings: Settings, *, dry_run: bool, manifest: list[dict[str, Any]]) -> None:
    log("Precompiling firmware before timed test sequence.")
    for name in COMPILE_ORDER:
        yaml_path = config_path(settings, name)
        if settings.clean_before_compile:
            run_command(esphome_base(settings) + ["clean", str(yaml_path)], dry_run=dry_run, manifest=manifest)
        run_command(esphome_base(settings) + ["compile", str(yaml_path)], dry_run=dry_run, manifest=manifest)
    log("Precompile phase complete. No compile commands will be run in the timed sequence.")


def upload(settings: Settings, role: str, firmware_name: str, *, dry_run: bool, manifest: list[dict[str, Any]]) -> None:
    yaml_path = config_path(settings, firmware_name)
    cmd = esphome_base(settings) + ["upload", str(yaml_path), "--device", settings.devices[role]]
    if settings.upload_speed:
        cmd += ["--upload_speed", settings.upload_speed]
    run_command(cmd, dry_run=dry_run, manifest=manifest)


def sleep_step(seconds: int, reason: str, *, dry_run: bool, manifest: list[dict[str, Any]]) -> None:
    entry = {"time_utc": now_utc_iso(), "sleep_seconds": seconds, "reason": reason, "dry_run": dry_run}
    manifest.append(entry)
    log(f"WAIT {seconds}s: {reason}")
    if not dry_run:
        time.sleep(seconds)


def extra_empty_roles(settings: Settings) -> list[str]:
    return sorted(role for role in settings.devices if role not in {"router1", "child", "router2"})


def start_sniffer_capture(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
) -> tuple[subprocess.Popen[str] | None, Path | None]:
    if not settings.sniffer.enabled:
        return None, None

    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    stamp = settings.run_logs_dir.name
    log_path = settings.run_logs_dir / f"stock_sniffer_{stamp}.log"
    cmd = settings.sniffer.command
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "sniffer_log_path": str(log_path), "dry_run": dry_run})
    log(("DRY-RUN " if dry_run else "START ") + quote_cmd(cmd) + f" > {log_path}")

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
                print(line, end="")
                log_file.write(line)
                log_file.flush()
        finally:
            log_file.write(f"# Log reader stopped UTC: {now_utc_iso()}\n")
            log_file.close()

    thread = threading.Thread(target=pump, name="sniffer-log-pump", daemon=True)
    thread.start()
    return process, log_path


def stop_sniffer_capture(settings: Settings, process: subprocess.Popen[str] | None, *, dry_run: bool) -> None:
    if dry_run or process is None:
        return
    if process.poll() is not None:
        log(f"Sniffer process already exited with code {process.returncode}.")
        return
    log("Stopping sniffer capture process.")
    process.terminate()
    try:
        process.wait(timeout=settings.sniffer.stop_timeout_seconds)
    except subprocess.TimeoutExpired:
        log("Sniffer process did not stop after SIGTERM; killing it.")
        process.kill()
        process.wait(timeout=10)


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
) -> tuple[str | None, Path | None]:
    remote_pcap = find_pcap_path_in_sniffer_log(sniffer_log_path)
    if remote_pcap is None:
        return None, None

    local_pcap = settings.logs_dir / Path(remote_pcap).name
    local_pcap = settings.run_logs_dir / Path(remote_pcap).name
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
    log(("DRY-RUN " if dry_run else "FETCH ") + quote_cmd(cmd))
    if dry_run:
        return remote_pcap, local_pcap

    local_pcap.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd, check=True, text=True)
    return remote_pcap, local_pcap


def start_child_log(settings: Settings, *, dry_run: bool, manifest: list[dict[str, Any]]) -> tuple[subprocess.Popen[str] | None, Path]:
    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    stamp = settings.run_logs_dir.name
    log_path = settings.run_logs_dir / f"stock_child_{stamp}.log"
    cmd = esphome_base(settings) + ["logs", str(config_path(settings, "child")), "--device", settings.devices["child"]]
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "log_path": str(log_path), "dry_run": dry_run})
    log(("DRY-RUN " if dry_run else "START ") + quote_cmd(cmd) + f" > {log_path}")

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
                print(line, end="")
                log_file.write(line)
                log_file.flush()
        finally:
            log_file.write(f"# Log reader stopped UTC: {now_utc_iso()}\n")
            log_file.close()

    thread = threading.Thread(target=pump, name="child-log-pump", daemon=True)
    thread.start()
    return process, log_path


def stop_child_log(process: subprocess.Popen[str] | None, *, dry_run: bool) -> None:
    if dry_run or process is None:
        return
    if process.poll() is not None:
        log(f"Child log process already exited with code {process.returncode}.")
        return
    log("Stopping child log process.")
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        log("Child log process did not stop after SIGTERM; killing it.")
        process.kill()
        process.wait(timeout=10)


def run_timed_sequence(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
) -> tuple[Path | None, Path | None, str | None, Path | None]:
    log("Starting timed upload/logging sequence. Upload-only commands are used from here onward.")
    child_logger: subprocess.Popen[str] | None = None
    child_log_path: Path | None = None
    sniffer_process: subprocess.Popen[str] | None = None
    sniffer_log_path: Path | None = None
    sniffer_remote_pcap: str | None = None
    sniffer_local_pcap: Path | None = None
    try:
        for role in ["router1", "child", "router2", *extra_empty_roles(settings)]:
            erase_flash(settings, role, dry_run=dry_run, manifest=manifest)
            upload(settings, role, "empty", dry_run=dry_run, manifest=manifest)

        sniffer_process, sniffer_log_path = start_sniffer_capture(settings, dry_run=dry_run, manifest=manifest)
        if settings.sniffer.enabled:
            sleep_step(
                settings.timing.sniffer_lead_in_seconds,
                "sniffer started; wait before flashing router 1",
                dry_run=dry_run,
                manifest=manifest,
            )

        upload(settings, "router1", "router1", dry_run=dry_run, manifest=manifest)
        sleep_step(
            settings.timing.after_router1_seconds,
            "router 1 has been flashed; wait before adding child",
            dry_run=dry_run,
            manifest=manifest,
        )

        upload(settings, "child", "child", dry_run=dry_run, manifest=manifest)
        child_logger, child_log_path = start_child_log(settings, dry_run=dry_run, manifest=manifest)
        sleep_step(settings.timing.after_child_seconds, "child flashed/logging; wait before adding router 2", dry_run=dry_run, manifest=manifest)

        upload(settings, "router2", "router2", dry_run=dry_run, manifest=manifest)
        sleep_step(settings.timing.after_router2_seconds, "router 2 has joined; wait before removing router 1", dry_run=dry_run, manifest=manifest)

        upload(settings, "router1", "empty", dry_run=dry_run, manifest=manifest)
        sleep_step(settings.timing.after_router1_removed_seconds, "router 1 removed; keep recording child", dry_run=dry_run, manifest=manifest)
        stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
        sniffer_process = None
        sniffer_remote_pcap, sniffer_local_pcap = pull_sniffer_pcap(
            settings,
            sniffer_log_path=sniffer_log_path,
            dry_run=dry_run,
            manifest=manifest,
        )
        return child_log_path, sniffer_log_path, sniffer_remote_pcap, sniffer_local_pcap
    finally:
        stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
        stop_child_log(child_logger, dry_run=dry_run)


def write_manifest(
    settings: Settings,
    manifest: list[dict[str, Any]],
    *,
    dry_run: bool,
    child_log: Path | None,
    sniffer_log: Path | None,
    sniffer_remote_pcap: str | None,
    sniffer_local_pcap: Path | None,
) -> Path:
    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    stamp = settings.run_logs_dir.name
    path = settings.run_logs_dir / f"stock_test_manifest_{stamp}.json"
    payload = {
        "created_utc": now_utc_iso(),
        "dry_run": dry_run,
        "config_file": str(settings.config_file),
        "testing_dir": str(settings.testing_dir),
        "configs_dir": str(settings.configs_dir),
        "logs_dir": str(settings.logs_dir),
        "run_logs_dir": str(settings.run_logs_dir),
        "esphome_bin": settings.esphome_bin,
        "esptool_bin": settings.esptool_bin,
        "precompile": settings.precompile,
        "clean_before_compile": settings.clean_before_compile,
        "devices": settings.devices,
        "timing": settings.timing.__dict__,
        "child_log": str(child_log) if child_log else None,
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
    parser.add_argument("--dry-run", action="store_true", help="Print commands and write a manifest without executing ESPHome.")
    parser.add_argument("--precompile-only", action="store_true", help="Compile all firmware and exit before any flashing.")
    parser.add_argument("--skip-precompile", action="store_true", help="Skip precompile phase. Not recommended for measurement runs.")
    parser.add_argument("--force-precompile", action="store_true", help="Force precompile phase even if disabled in TOML.")
    parser.add_argument("--clean-before-compile", action="store_true", help="Run `esphome clean` before each compile.")
    parser.add_argument("--allow-same-port", action="store_true", help="Permit multiple roles to use the same serial port.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    settings = load_settings(args)
    manifest: list[dict[str, Any]] = []

    log(f"Using ESPHome: {settings.esphome_bin}")
    log(f"Using esptool: {settings.esptool_bin}")
    log(f"Using configs: {settings.configs_dir}")
    log(f"Using logs base: {settings.logs_dir}")
    log(f"Using run logs dir: {settings.run_logs_dir}")

    child_log: Path | None = None
    sniffer_log: Path | None = None
    sniffer_remote_pcap: str | None = None
    sniffer_local_pcap: Path | None = None
    try:
        if settings.precompile:
            precompile_all(settings, dry_run=args.dry_run, manifest=manifest)
        else:
            log("WARNING: precompile phase skipped. Uploads may fail if the most recent firmware builds do not exist.")

        if args.precompile_only:
            log("Precompile-only requested; not starting timed test sequence.")
        else:
            child_log, sniffer_log, sniffer_remote_pcap, sniffer_local_pcap = run_timed_sequence(
                settings, dry_run=args.dry_run, manifest=manifest
            )
    finally:
        manifest_path = write_manifest(
            settings,
            manifest,
            dry_run=args.dry_run,
            child_log=child_log,
            sniffer_log=sniffer_log,
            sniffer_remote_pcap=sniffer_remote_pcap,
            sniffer_local_pcap=sniffer_local_pcap,
        )
        log(f"Wrote manifest: {manifest_path}")
        if child_log:
            log(f"Child log: {child_log}")
        if sniffer_log:
            log(f"Sniffer log: {sniffer_log}")
        if sniffer_local_pcap:
            log(f"Sniffer pcap: {sniffer_local_pcap}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
