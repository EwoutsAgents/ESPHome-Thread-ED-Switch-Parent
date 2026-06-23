#!/usr/bin/env python3
"""Run the unicast/multicast ESPHome/OpenThread parent-switching test.

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


VARIANT_PRESETS = {
    "ucast": {
        "child_config": "ucast_child.yaml",
        "logs_subdir": "ucast",
        "name_prefix": "ucast",
        "default_config": "ucast_test_devices.toml",
    },
    "mcast": {
        "child_config": "mcast_child.yaml",
        "logs_subdir": "mcast",
        "name_prefix": "mcast",
        "default_config": "mcast_test_devices.toml",
    },
}

CONFIG_NAMES = {
    "empty": "empty.yaml",
    "router1": "stock_router_1.yaml",
    "router2": "stock_router_2.yaml",
    "router3": "stock_router_3.yaml",
    "router4": "stock_router_4.yaml",
}
CORE_COMPILE_ORDER = ["empty", "router1", "child", "router2"]
MAX_ADDITIONAL_ROUTER_NUMBER = max(
    int(name.removeprefix("router"))
    for name in CONFIG_NAMES
    if name.startswith("router") and name not in {"router1", "router2"}
)
PCAP_PATH_RE = re.compile(r"Saving (?:test )?capture to (\S+\.pcapng)")
ROUTER2_RADIO_EXTADDR_RE = re.compile(r"RadioExtAddress:\s*([0-9a-f]{16})", re.IGNORECASE)
ROUTER2_NETWORKINFO_RE = re.compile(
    r"Saved NetworkInfo \{[^}]*extaddr:([0-9a-f]{16}), role:(?:router|leader)\b",
    re.IGNORECASE,
)


_BATCH_LOG_PATH: Path | None = None


@dataclass
class Timing:
    sniffer_lead_in_seconds: int = 5
    after_router1_seconds: int = 5
    after_child_seconds: int = 10
    after_router2_seconds: int = 90
    after_router1_removal_settle_seconds: int = 5
    after_router1_removed_seconds: int = 180


@dataclass
class SnifferSettings:
    enabled: bool = False
    command: list[str] = field(default_factory=list)
    stop_timeout_seconds: int = 10


@dataclass
class SwitchSettings:
    target_parent_extaddr: str = ""
    settle_seconds: int = 2


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
    switch: SwitchSettings = field(default_factory=SwitchSettings)
    variant: str = "ucast"
    name_prefix: str = "ucast"
    capture_router2_log: bool = True
    n_routers: int = 3


def allocate_run_logs_dir(logs_dir: Path, *, run_index: int | None = None) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    if run_index is not None:
        stamp = f"{stamp}-run{run_index:02d}"
    base = logs_dir / stamp
    candidate = base
    counter = 2
    while candidate.exists():
        candidate = logs_dir / f"{base.name}-run{counter:02d}"
        counter += 1
    return candidate


def allocate_batch_logs_dir(logs_root: Path, *, variant_name: str, router_count: int, total_runs: int) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    base_name = f"{variant_name}-{router_count}router-{total_runs}runs-{stamp}"
    candidate = logs_root / base_name
    counter = 2
    while candidate.exists():
        candidate = logs_root / f"{base_name}-dup{counter:02d}"
        counter += 1
    return candidate


def now_utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def log(msg: str) -> None:
    formatted = f"[{now_utc_iso()}] {msg}"
    print(formatted, flush=True)
    if _BATCH_LOG_PATH is not None:
        _BATCH_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with _BATCH_LOG_PATH.open("a", encoding="utf-8", errors="replace") as fh:
            fh.write(formatted + "\n")


def set_batch_log(path: Path | None) -> None:
    global _BATCH_LOG_PATH
    _BATCH_LOG_PATH = path


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
            example = config_file.parent / f"{VARIANT_PRESETS[args.variant]['default_config']}.example"
        hint = f" Copy {example.name} to {config_file.name} and edit the serial ports." if example.exists() else ""
        raise SystemExit(f"Config file not found: {config_file}.{hint}")

    raw = load_toml(config_file)
    variant_raw = str(raw.get("variant", {}).get("name", args.variant)).strip().lower()
    if variant_raw not in VARIANT_PRESETS:
        raise SystemExit(f"Unsupported variant `{variant_raw}`. Choose one of: {', '.join(sorted(VARIANT_PRESETS))}")
    variant_preset = VARIANT_PRESETS[variant_raw]
    config_dir = config_file.parent
    testing_dir = resolve_relative(config_dir, raw.get("paths", {}).get("testing_dir"), ".")
    configs_dir = resolve_relative(config_dir, raw.get("paths", {}).get("configs_dir"), "configs")
    logs_default = f"logs/{variant_preset['logs_subdir']}"
    logs_dir = resolve_relative(config_dir, raw.get("paths", {}).get("logs_dir"), logs_default)
    run_logs_dir = allocate_run_logs_dir(logs_dir)

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
        after_router2_seconds=int(timing_raw.get("after_router2_seconds", 90)),
        after_router1_removal_settle_seconds=int(timing_raw.get("after_router1_removal_settle_seconds", 5)),
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
    switch_raw = raw.get("switch", {})
    router_count_raw = raw.get("variant", {}).get("n_routers", 3)
    n_routers = int(router_count_raw)
    if n_routers < 3 or f"router{n_routers}" not in CONFIG_NAMES:
        raise SystemExit(
            f"[variant].n_routers must reference an available stock_router_<n>.yaml variation. "
            f"Supported values are 3..{MAX_ADDITIONAL_ROUTER_NUMBER}."
        )

    if args.runs > 1:
        logs_dir = allocate_batch_logs_dir(
            logs_dir.parent,
            variant_name=variant_raw,
            router_count=n_routers,
            total_runs=args.runs,
        )
        run_logs_dir = allocate_run_logs_dir(logs_dir, run_index=1)

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
        switch=SwitchSettings(
            settle_seconds=int(switch_raw.get("settle_seconds", 2)),
        ),
        variant=variant_raw,
        name_prefix=str(variant_preset["name_prefix"]),
        capture_router2_log=bool(raw.get("diagnostics", {}).get("capture_router2_log", True)),
        n_routers=n_routers,
    )


def config_path(settings: Settings, name: str) -> Path:
    config_names = {
        "empty": CONFIG_NAMES["empty"],
        "router1": CONFIG_NAMES["router1"],
        "child": str(VARIANT_PRESETS[settings.variant]["child_config"]),
        "router2": CONFIG_NAMES["router2"],
        "router3": CONFIG_NAMES["router3"],
        "router4": CONFIG_NAMES["router4"],
    }
    path = settings.configs_dir / config_names[name]
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
    for name in [*CORE_COMPILE_ORDER, *additional_router_firmware_names(settings)]:
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


def additional_router_firmware_names(settings: Settings) -> list[str]:
    return [f"router{number}" for number in range(3, settings.n_routers + 1)]


def additional_router_device_roles(settings: Settings) -> list[str]:
    extras = extra_empty_roles(settings)
    selected_roles: list[str] = []
    remaining_roles = list(extras)
    for firmware_name in additional_router_firmware_names(settings):
        if firmware_name in remaining_roles:
            selected_roles.append(firmware_name)
            remaining_roles.remove(firmware_name)
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
            "This testing flow requires enough extra ESP32-C6 boards in [devices] for the requested router variation. "
            f"Need {required_count} extra role(s) for router3..router{settings.n_routers}. "
            "Add extra roles such as `unused1`, `unused2`, `router3`, or `router4`."
        )
    return assignments


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
    log_path = settings.run_logs_dir / f"{settings.name_prefix}_sniffer_{stamp}.log"
    cmd = settings.sniffer.command
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "sniffer_log_path": str(log_path), "dry_run": dry_run})

    host = sniffer_remote_host(settings)
    if host is not None:
        cleanup_cmd = [
            "ssh",
            host,
            "pkill -f 'nrf802154_sniffer.py|tshark.*802.15.4' >/dev/null 2>&1 || true; sleep 1",
        ]
        manifest.append({"time_utc": now_utc_iso(), "cmd": cleanup_cmd, "purpose": "sniffer-pre-clean", "dry_run": dry_run})
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
                    print(line, end="")
                    log_file.write(line)
                    log_file.flush()
            finally:
                log_file.write(f"# Log reader stopped UTC: {now_utc_iso()} (attempt {attempt})\n")
                log_file.close()

        thread = threading.Thread(target=pump, name=f"sniffer-log-pump-{attempt}", daemon=True)
        thread.start()
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

    stamp = settings.run_logs_dir.name
    local_pcap = settings.run_logs_dir / f"{settings.name_prefix}_sniffer_{stamp}.pcapng"
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
    log_path = settings.run_logs_dir / f"{settings.name_prefix}_child_{stamp}.log"
    cmd = esphome_base(settings) + ["logs", str(config_path(settings, "child")), "--device", settings.devices["child"]]
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "log_path": str(log_path), "dry_run": dry_run})
    log(("DRY-RUN " if dry_run else "START ") + quote_cmd(cmd) + f" > {log_path}")

    if dry_run:
        return None, log_path

    is_new = not log_path.exists()
    log_file = log_path.open("a", encoding="utf-8", errors="replace")
    if is_new:
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


def start_router1_log(settings: Settings, *, dry_run: bool, manifest: list[dict[str, Any]]) -> tuple[subprocess.Popen[str] | None, Path]:
    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    stamp = settings.run_logs_dir.name
    log_path = settings.run_logs_dir / f"{settings.name_prefix}_router1_{stamp}.log"
    cmd = esphome_base(settings) + ["logs", str(config_path(settings, "router1")), "--device", settings.devices["router1"]]
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "log_path": str(log_path), "dry_run": dry_run})
    log(("DRY-RUN " if dry_run else "START ") + quote_cmd(cmd) + f" > {log_path}")

    if dry_run:
        return None, log_path

    is_new = not log_path.exists()
    log_file = log_path.open("a", encoding="utf-8", errors="replace")
    if is_new:
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

    thread = threading.Thread(target=pump, name="router1-log-pump", daemon=True)
    thread.start()
    return process, log_path


def start_router2_log(settings: Settings, *, dry_run: bool, manifest: list[dict[str, Any]]) -> tuple[subprocess.Popen[str] | None, Path]:
    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    stamp = settings.run_logs_dir.name
    log_path = settings.run_logs_dir / f"{settings.name_prefix}_router2_{stamp}.log"
    cmd = esphome_base(settings) + ["logs", str(config_path(settings, "router2")), "--device", settings.devices["router2"]]
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "log_path": str(log_path), "dry_run": dry_run})
    log(("DRY-RUN " if dry_run else "START ") + quote_cmd(cmd) + f" > {log_path}")

    if dry_run:
        return None, log_path

    is_new = not log_path.exists()
    log_file = log_path.open("a", encoding="utf-8", errors="replace")
    if is_new:
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

    thread = threading.Thread(target=pump, name="router2-log-pump", daemon=True)
    thread.start()
    return process, log_path


def stop_router1_log(process: subprocess.Popen[str] | None, *, dry_run: bool) -> None:
    if dry_run or process is None:
        return
    if process.poll() is not None:
        log(f"Router1 log process already exited with code {process.returncode}.")
        return
    log("Stopping router1 log process.")
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        log("Router1 log process did not stop after SIGTERM; killing it.")
        process.kill()
        process.wait(timeout=10)


def stop_router2_log(process: subprocess.Popen[str] | None, *, dry_run: bool) -> None:
    if dry_run or process is None:
        return
    if process.poll() is not None:
        log(f"Router2 log process already exited with code {process.returncode}.")
        return
    log("Stopping router2 log process.")
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        log("Router2 log process did not stop after SIGTERM; killing it.")
        process.kill()
        process.wait(timeout=10)


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


def router2_extaddr_from_log(path: Path | None) -> str | None:
    if path is None or not path.exists():
        return None
    text = path.read_text(encoding="utf-8", errors="ignore")
    matches = ROUTER2_RADIO_EXTADDR_RE.findall(text)
    if matches:
        return matches[-1].lower()
    matches = ROUTER2_NETWORKINFO_RE.findall(text)
    if matches:
        return matches[-1].lower()
    return None


def verify_router2_target_parent_extaddr(
    settings: Settings,
    *,
    router2_log_path: Path | None,
    dry_run: bool,
    manifest: list[dict[str, Any]],
) -> None:
    observed = router2_extaddr_from_log(router2_log_path)
    entry = {
        "time_utc": now_utc_iso(),
        "event": "observe_router2_target_parent_extaddr",
        "observed_router2_extaddr": observed,
        "router2_log": str(router2_log_path) if router2_log_path else None,
        "dry_run": dry_run,
    }
    manifest.append(entry)

    if observed is None:
        if dry_run:
            observed = "0000000000000000"
            settings.switch.target_parent_extaddr = observed
            log(f"Dry-run: using placeholder router2 ExtAddr: {observed}")
            return
        raise SystemExit("Could not determine router2 ExtAddr from router2 log before sending switch command.")

    settings.switch.target_parent_extaddr = observed
    log(f"Observed router2 ExtAddr from router2 log: {observed}")


def send_child_switch_command(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
) -> None:
    command = f"extaddr {settings.switch.target_parent_extaddr}\n"
    port = settings.devices["child"]
    entry = {
        "time_utc": now_utc_iso(),
        "event": "send_child_switch_command",
        "port": port,
        "command": command.strip(),
        "dry_run": dry_run,
    }
    manifest.append(entry)
    log(f"{'DRY-RUN ' if dry_run else 'SEND '}child switch command `{command.strip()}` to {port}")
    if dry_run:
        return
    with open(port, "wb", buffering=0) as fh:
        fh.write(command.encode("ascii"))
        fh.flush()
    if settings.switch.settle_seconds > 0:
        sleep_step(
            settings.switch.settle_seconds,
            "allow child USB CLI to process switch command",
            dry_run=dry_run,
            manifest=manifest,
        )


def record_observed_target_parent_extaddr(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
) -> None:
    entry = {
        "time_utc": now_utc_iso(),
        "event": "use_observed_target_parent_extaddr",
        "target_parent_extaddr": settings.switch.target_parent_extaddr,
        "dry_run": dry_run,
    }
    manifest.append(entry)
    log(f"Using observed router2 ExtAddr as target parent: {settings.switch.target_parent_extaddr}")


def run_timed_sequence(
    settings: Settings,
    *,
    dry_run: bool,
    manifest: list[dict[str, Any]],
) -> tuple[Path | None, Path | None, Path | None, Path | None, str | None, Path | None]:
    log("Starting timed upload/logging sequence. Upload-only commands are used from here onward.")
    child_logger: subprocess.Popen[str] | None = None
    child_log_path: Path | None = None
    router1_logger: subprocess.Popen[str] | None = None
    router1_log_path: Path | None = None
    router2_logger: subprocess.Popen[str] | None = None
    router2_log_path: Path | None = None
    sniffer_process: subprocess.Popen[str] | None = None
    sniffer_log_path: Path | None = None
    sniffer_remote_pcap: str | None = None
    sniffer_local_pcap: Path | None = None
    try:
        for role in ["router1", "child", "router2", *extra_empty_roles(settings)]:
            erase_flash(settings, role, dry_run=dry_run, manifest=manifest)
            upload(settings, role, "empty", dry_run=dry_run, manifest=manifest)
        additional_router_plan = require_additional_router_assignments(settings)

        sniffer_process, sniffer_log_path = start_sniffer_capture(settings, dry_run=dry_run, manifest=manifest)
        if settings.sniffer.enabled:
            sleep_step(
                settings.timing.sniffer_lead_in_seconds,
                "sniffer started; wait before flashing router 1",
                dry_run=dry_run,
                manifest=manifest,
            )

        upload(settings, "router1", "router1", dry_run=dry_run, manifest=manifest)
        if settings.capture_router2_log:
            router1_logger, router1_log_path = start_router1_log(settings, dry_run=dry_run, manifest=manifest)
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
        if settings.capture_router2_log:
            router2_logger, router2_log_path = start_router2_log(settings, dry_run=dry_run, manifest=manifest)

        manifest.append(
            {
                "time_utc": now_utc_iso(),
                "event": "flash_additional_routers",
                "assignments": additional_router_plan,
                "dry_run": dry_run,
            }
        )
        for assignment in additional_router_plan:
            upload(
                settings,
                assignment["device_role"],
                assignment["firmware_name"],
                dry_run=dry_run,
                manifest=manifest,
            )
        sleep_step(
            settings.timing.after_router2_seconds,
            "router 2 and the additional routers have joined; wait before removing router 1",
            dry_run=dry_run,
            manifest=manifest,
        )
        verify_router2_target_parent_extaddr(
            settings,
            router2_log_path=router2_log_path,
            dry_run=dry_run,
            manifest=manifest,
        )
        record_observed_target_parent_extaddr(settings, dry_run=dry_run, manifest=manifest)
        stop_router1_log(router1_logger, dry_run=dry_run)
        router1_logger = None
        upload(settings, "router1", "empty", dry_run=dry_run, manifest=manifest)
        sleep_step(
            settings.timing.after_router1_removal_settle_seconds,
            "router 1 removed; wait before requesting child switch",
            dry_run=dry_run,
            manifest=manifest,
        )
        send_child_switch_command(settings, dry_run=dry_run, manifest=manifest)
        sleep_step(
            settings.timing.after_router1_removed_seconds,
            "switch requested; keep recording child",
            dry_run=dry_run,
            manifest=manifest,
        )
        stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
        sniffer_process = None
        sniffer_remote_pcap, sniffer_local_pcap = pull_sniffer_pcap(
            settings,
            sniffer_log_path=sniffer_log_path,
            dry_run=dry_run,
            manifest=manifest,
        )
        return child_log_path, router1_log_path, router2_log_path, sniffer_log_path, sniffer_remote_pcap, sniffer_local_pcap
    finally:
        stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
        stop_child_log(child_logger, dry_run=dry_run)
        stop_router1_log(router1_logger, dry_run=dry_run)
        stop_router2_log(router2_logger, dry_run=dry_run)


def write_manifest(
    settings: Settings,
    manifest: list[dict[str, Any]],
    *,
    dry_run: bool,
    child_log: Path | None,
    router1_log: Path | None,
    router2_log: Path | None,
    sniffer_log: Path | None,
    sniffer_remote_pcap: str | None,
    sniffer_local_pcap: Path | None,
) -> Path:
    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    stamp = settings.run_logs_dir.name
    path = settings.run_logs_dir / f"{settings.name_prefix}_test_manifest_{stamp}.json"
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
        "switch": settings.switch.__dict__,
        "n_routers": settings.n_routers,
        "additional_router_assignments": additional_router_assignments(settings),
        "child_log": str(child_log) if child_log else None,
        "router1_log": str(router1_log) if router1_log else None,
        "router2_log": str(router2_log) if router2_log else None,
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
    parser = argparse.ArgumentParser(description="Run ESPHome/OpenThread parent-switching test.")
    parser.add_argument("--variant", choices=sorted(VARIANT_PRESETS), default="ucast", help="Select test variant.")
    parser.add_argument("--config", default=None, help="Path to device/config TOML file.")
    parser.add_argument("--esphome-bin", help="Override ESPHome executable. Overrides ESPHOME_BIN and TOML.")
    parser.add_argument("--dry-run", action="store_true", help="Print commands and write a manifest without executing ESPHome.")
    parser.add_argument("--precompile-only", action="store_true", help="Compile all firmware and exit before any flashing.")
    parser.add_argument("--skip-precompile", action="store_true", help="Skip precompile phase. Not recommended for measurement runs.")
    parser.add_argument("--force-precompile", action="store_true", help="Force precompile phase even if disabled in TOML.")
    parser.add_argument("--clean-before-compile", action="store_true", help="Run `esphome clean` before each compile.")
    parser.add_argument("--allow-same-port", action="store_true", help="Permit multiple roles to use the same serial port.")
    parser.add_argument("--capture-router2-log", action="store_true", help="Capture router2 logs after router2 is flashed.")
    parser.add_argument("--runs", type=int, default=1, help="Number of timed test runs to execute sequentially.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.runs < 1:
        raise SystemExit("--runs must be at least 1.")
    if args.config is None:
        args.config = str(VARIANT_PRESETS[args.variant]["default_config"])
    settings = load_settings(args)
    if args.runs > 1:
        set_batch_log(settings.logs_dir / f"{settings.logs_dir.name}.log")
    else:
        set_batch_log(None)
    if args.capture_router2_log:
        settings.capture_router2_log = True

    log(f"Using ESPHome: {settings.esphome_bin}")
    log(f"Using esptool: {settings.esptool_bin}")
    log(f"Using configs: {settings.configs_dir}")
    log(f"Using logs base: {settings.logs_dir}")
    log(f"Requested runs: {args.runs}")

    compile_manifest: list[dict[str, Any]] = []
    if settings.precompile:
        precompile_all(settings, dry_run=args.dry_run, manifest=compile_manifest)
    else:
        log("WARNING: precompile phase skipped. Uploads may fail if the most recent firmware builds do not exist.")

    if args.precompile_only:
        log("Precompile-only requested; not starting timed test sequence.")
        return 0

    for run_index in range(1, args.runs + 1):
        if args.runs > 1:
            settings.run_logs_dir = allocate_run_logs_dir(settings.logs_dir, run_index=run_index)
        else:
            settings.run_logs_dir = allocate_run_logs_dir(settings.logs_dir)
        log(f"Starting run {run_index}/{args.runs}")
        log(f"Using run logs dir: {settings.run_logs_dir}")

        manifest: list[dict[str, Any]] = []
        child_log: Path | None = None
        router1_log: Path | None = None
        router2_log: Path | None = None
        sniffer_log: Path | None = None
        sniffer_remote_pcap: str | None = None
        sniffer_local_pcap: Path | None = None
        try:
            child_log, router1_log, router2_log, sniffer_log, sniffer_remote_pcap, sniffer_local_pcap = run_timed_sequence(
                settings, dry_run=args.dry_run, manifest=manifest
            )
        finally:
            manifest_path = write_manifest(
                settings,
                manifest,
                dry_run=args.dry_run,
                child_log=child_log,
                router1_log=router1_log,
                router2_log=router2_log,
                sniffer_log=sniffer_log,
                sniffer_remote_pcap=sniffer_remote_pcap,
                sniffer_local_pcap=sniffer_local_pcap,
            )
            log(f"Wrote manifest: {manifest_path}")
            if child_log:
                log(f"Child log: {child_log}")
            if router1_log:
                log(f"Router1 log: {router1_log}")
            if router2_log:
                log(f"Router2 log: {router2_log}")
            if sniffer_log:
                log(f"Sniffer log: {sniffer_log}")
            if sniffer_local_pcap:
                log(f"Sniffer pcap: {sniffer_local_pcap}")
        log(f"Completed run {run_index}/{args.runs}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
