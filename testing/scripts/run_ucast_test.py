#!/usr/bin/env python3
"""Run directed unicast/multicast ESPHome/OpenThread parent-switching tests.

This runner follows the updated ucast/mcast method:
- flash all requested routers first, like the stock test;
- wait for router topology to settle;
- flash the child and let it attach naturally;
- detect the child's current parent;
- randomly select a target router that is not the current parent;
- send `extaddr <target_extaddr>` to the child;
- immediately remove the child's initial parent by flashing that board with empty.yaml;
- keep sniffer/device logs running, then write a manifest.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import random
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

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    try:
        import tomli as tomllib  # type: ignore[no-redef]
    except ModuleNotFoundError:
        tomllib = None  # type: ignore[assignment]

VARIANT_PRESETS = {
    "ucast": {
        "child_config": "ucast_child.yaml",
        "router_prefix": "stock_router",
        "logs_subdir": "ucast",
        "name_prefix": "ucast",
        "default_config": "ucast_test_devices_4routers.toml",
    },
    "ucast_fastpr": {
        "child_config": "ucast_fastpr_child.yaml",
        "router_prefix": "fastpr_router",
        "logs_subdir": "ucast_fastpr",
        "name_prefix": "ucast_fastpr",
        "default_config": "ucast_fastpr_test_devices_4routers.toml",
    },
    "mcast": {
        "child_config": "mcast_child.yaml",
        "router_prefix": "stock_router",
        "logs_subdir": "mcast",
        "name_prefix": "mcast",
        "default_config": "mcast_test_devices_4routers.toml",
    },
}

CONFIG_NAMES = {
    "empty": "empty.yaml",
    "child": "ucast_child.yaml",  # replaced by variant in config_path()
}
CORE_COMPILE_ORDER = ["empty", "router1", "child", "router2"]
MAX_ROUTER_COUNT = 4
PCAP_PATH_RE = re.compile(r"Saving (?:test )?capture to (\S+\.pcapng)")

SKIP_NO_CHILD_PARENT = "SKIP_NO_CHILD_PARENT"
SKIP_PARENT_NOT_MAPPED_TO_DEVICE = "SKIP_PARENT_NOT_MAPPED_TO_DEVICE"
SKIP_NO_ELIGIBLE_TARGET_PARENT = "SKIP_NO_ELIGIBLE_TARGET_PARENT"
SKIP_PARENT_IS_LEADER = "SKIP_PARENT_IS_LEADER"
SKIP_PARENT_IS_LEADER_NOTE = (
    "The detected child parent is the current Thread leader. The run continues, but it keeps "
    "the SKIP_PARENT_IS_LEADER label because removing the initial parent also disrupts the current leader."
)

_BATCH_LOG_PATH: Path | None = None


@dataclass
class Timing:
    sniffer_lead_in_seconds: int = 5
    router_settling_seconds: int = 300
    child_attach_seconds: int = 30
    after_parent_removed_seconds: int = 360


@dataclass
class SnifferSettings:
    enabled: bool = False
    command: list[str] = field(default_factory=list)
    stop_timeout_seconds: int = 10


@dataclass
class SelectionSettings:
    random_seed: int | None = None


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
    selection: SelectionSettings = field(default_factory=SelectionSettings)
    variant: str = "ucast"
    name_prefix: str = "ucast"
    max_router_number: int = 4


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


def load_toml(path: Path) -> dict[str, Any]:
    if tomllib is None:
        raise SystemExit("Unable to read TOML. Use Python 3.11+ or install tomli.")
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
    out: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved not in seen:
            out.append(resolved)
            seen.add(resolved)
    return out


def resolve_esphome_bin(*, cli_value: str | None, env_value: str | None, config_value: str | None, config_dir: Path, testing_dir: Path, dry_run: bool) -> str:
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
    raise SystemExit(f"Could not find esphome.\nSearched:\n  - {searched}\n  - PATH")


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
            return str(resolved)
    for name in ("esptool.py", "esptool"):
        path_bin = shutil.which(name)
        if path_bin:
            return path_bin
    if dry_run:
        return "esptool.py"
    searched = "\n  - ".join(str(p.resolve()) for p in candidates)
    raise SystemExit(f"Could not find esptool.py/esptool.\nSearched:\n  - {searched}\n  - PATH")


def load_settings(args: argparse.Namespace) -> Settings:
    config_file = Path(args.config).expanduser().resolve()
    if not config_file.exists():
        raise SystemExit(f"Config file not found: {config_file}")
    raw = load_toml(config_file)
    variant_raw = str(raw.get("variant", {}).get("name", args.variant)).strip().lower()
    if variant_raw not in VARIANT_PRESETS:
        raise SystemExit(f"Unsupported variant `{variant_raw}`. Choose one of: {', '.join(sorted(VARIANT_PRESETS))}")
    preset = VARIANT_PRESETS[variant_raw]

    config_dir = config_file.parent
    testing_dir = resolve_relative(config_dir, raw.get("paths", {}).get("testing_dir"), ".")
    configs_dir = resolve_relative(config_dir, raw.get("paths", {}).get("configs_dir"), "configs")
    logs_dir = resolve_relative(config_dir, raw.get("paths", {}).get("logs_dir"), f"logs/{preset['logs_subdir']}")
    run_logs_dir = build_run_logs_dir(logs_dir)

    devices = {key: str(value) for key, value in dict(raw.get("devices", {})).items()}
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

    timing_raw = raw.get("timing", {})
    timing = Timing(
        sniffer_lead_in_seconds=int(timing_raw.get("sniffer_lead_in_seconds", 5)),
        router_settling_seconds=int(timing_raw.get("router_settling_seconds", 300)),
        child_attach_seconds=int(timing_raw.get("child_attach_seconds", 30)),
        after_parent_removed_seconds=int(timing_raw.get("after_parent_removed_seconds", 360)),
    )

    esphome_raw = raw.get("esphome", {})
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

    max_router_number = int(raw.get("variant", {}).get("n_routers", 4))
    if max_router_number < 2 or max_router_number > MAX_ROUTER_COUNT:
        raise SystemExit(f"[variant].n_routers must be 2..{MAX_ROUTER_COUNT} total routers.")

    selection_raw = raw.get("selection", {})
    random_seed_raw = selection_raw.get("random_seed", None)
    random_seed = int(random_seed_raw) if random_seed_raw is not None else None

    if args.runs > 1:
        logs_dir = allocate_batch_logs_dir(logs_dir.parent, variant_name=variant_raw, router_count=max_router_number, total_runs=args.runs)
        run_logs_dir = build_run_logs_dir(logs_dir)

    return Settings(
        config_file=config_file,
        testing_dir=testing_dir,
        configs_dir=configs_dir,
        logs_dir=logs_dir,
        run_logs_dir=run_logs_dir,
        esphome_bin=resolve_esphome_bin(cli_value=args.esphome_bin, env_value=os.environ.get("ESPHOME_BIN"), config_value=esphome_raw.get("bin"), config_dir=config_dir, testing_dir=testing_dir, dry_run=args.dry_run),
        esptool_bin=resolve_esptool_bin(testing_dir=testing_dir, dry_run=args.dry_run),
        upload_speed=str(esphome_raw.get("upload_speed")) if esphome_raw.get("upload_speed") else None,
        precompile=precompile,
        clean_before_compile=clean_before_compile,
        devices=devices,
        timing=timing,
        sniffer=SnifferSettings(enabled=sniffer_enabled, command=[str(part) for part in sniffer_command], stop_timeout_seconds=int(sniffer_raw.get("stop_timeout_seconds", 10))),
        selection=SelectionSettings(random_seed=random_seed),
        variant=variant_raw,
        name_prefix=str(preset["name_prefix"]),
        max_router_number=max_router_number,
    )


def config_path(settings: Settings, name: str) -> Path:
    if name == "child":
        file_name = str(VARIANT_PRESETS[settings.variant]["child_config"])
    elif name.startswith("router"):
        router_index = name.removeprefix("router")
        file_name = f"{VARIANT_PRESETS[settings.variant]['router_prefix']}_{router_index}.yaml"
    else:
        file_name = CONFIG_NAMES[name]
    path = settings.configs_dir / file_name
    if not path.exists():
        raise SystemExit(f"Missing ESPHome config: {path}")
    return path


def run_command(cmd: list[str], *, dry_run: bool, manifest: list[dict[str, Any]], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str] | None:
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "cwd": str(cwd or Path.cwd()), "dry_run": dry_run})
    log(("DRY-RUN " if dry_run else "RUN ") + quote_cmd(cmd))
    if dry_run:
        return None
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=check, text=True)


def esphome_base(settings: Settings) -> list[str]:
    return [settings.esphome_bin]


def erase_flash(settings: Settings, role: str, *, dry_run: bool, manifest: list[dict[str, Any]]) -> None:
    run_command([settings.esptool_bin, "--chip", "esp32c6", "--port", settings.devices[role], "erase_flash"], dry_run=dry_run, manifest=manifest)


def upload(settings: Settings, role: str, firmware_name: str, *, dry_run: bool, manifest: list[dict[str, Any]]) -> None:
    cmd = esphome_base(settings) + ["upload", str(config_path(settings, firmware_name)), "--device", settings.devices[role]]
    if settings.upload_speed:
        cmd += ["--upload_speed", settings.upload_speed]
    run_command(cmd, dry_run=dry_run, manifest=manifest)


def sleep_step(seconds: int, reason: str, *, dry_run: bool, manifest: list[dict[str, Any]]) -> None:
    manifest.append({"time_utc": now_utc_iso(), "sleep_seconds": seconds, "reason": reason, "dry_run": dry_run})
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
        if firmware_name in remaining_roles:
            selected_roles.append(firmware_name)
            remaining_roles.remove(firmware_name)
        elif remaining_roles:
            selected_roles.append(remaining_roles.pop(0))
    return selected_roles


def additional_router_assignments(settings: Settings) -> list[dict[str, str]]:
    return [
        {"device_role": role, "firmware_name": firmware}
        for role, firmware in zip(additional_router_device_roles(settings), additional_router_firmware_names(settings))
    ]


def require_additional_router_assignments(settings: Settings) -> None:
    required_count = len(additional_router_firmware_names(settings))
    if len(additional_router_assignments(settings)) < required_count:
        raise SystemExit(
            f"n_routers={settings.max_router_number} requires {required_count} extra role(s) for router3..router{settings.max_router_number}. "
            "Add extra roles such as `unused1`, `unused2`, `router3`, or `router4`."
        )


def router_execution_plan(settings: Settings) -> list[dict[str, str]]:
    plan = [
        {"logical_name": "router1", "config_name": "router1", "device_role": "router1"},
        {"logical_name": "router2", "config_name": "router2", "device_role": "router2"},
    ]
    for assignment in additional_router_assignments(settings):
        firmware = assignment["firmware_name"]
        plan.append({"logical_name": firmware, "config_name": firmware, "device_role": assignment["device_role"]})
    return plan


def log_file_path(settings: Settings, logical_name: str) -> Path:
    return settings.run_logs_dir / f"{settings.name_prefix}_{logical_name}_{settings.run_logs_dir.name}.log"


def start_device_log(settings: Settings, *, logical_name: str, config_name: str, device_role: str, dry_run: bool, manifest: list[dict[str, Any]]) -> tuple[subprocess.Popen[str] | None, Path]:
    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_file_path(settings, logical_name)
    cmd = esphome_base(settings) + ["logs", str(config_path(settings, config_name)), "--device", settings.devices[device_role]]
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "log_path": str(log_path), "logical_name": logical_name, "config_name": config_name, "device_role": device_role, "dry_run": dry_run})
    log(("DRY-RUN " if dry_run else "START ") + quote_cmd(cmd) + f" > {log_path}")
    if dry_run:
        return None, log_path
    log_file = log_path.open("w", encoding="utf-8", errors="replace")
    log_file.write(f"# Command: {quote_cmd(cmd)}\n# Started UTC: {now_utc_iso()}\n")
    log_file.flush()
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", bufsize=1)

    def pump() -> None:
        try:
            assert process.stdout is not None
            for line in process.stdout:
                log_file.write(line)
                log_file.flush()
        finally:
            log_file.write(f"# Log reader stopped UTC: {now_utc_iso()}\n")
            log_file.close()

    threading.Thread(target=pump, name=f"{logical_name}-log-pump", daemon=True).start()
    return process, log_path


def stop_device_log(process: subprocess.Popen[str] | None, *, logical_name: str, dry_run: bool) -> None:
    if dry_run or process is None:
        return
    if process.poll() is not None:
        log(f"{logical_name} log process already exited with code {process.returncode}.")
        return
    log(f"Stopping {logical_name} log process.")
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=10)


def sniffer_remote_host(settings: Settings) -> str | None:
    cmd = settings.sniffer.command
    if len(cmd) >= 2 and cmd[0] == "ssh":
        return cmd[1]
    return None


def start_sniffer_capture(settings: Settings, *, dry_run: bool, manifest: list[dict[str, Any]]) -> tuple[subprocess.Popen[str] | None, Path | None]:
    if not settings.sniffer.enabled:
        return None, None
    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = settings.run_logs_dir / f"{settings.name_prefix}_sniffer_{settings.run_logs_dir.name}.log"
    cmd = settings.sniffer.command
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "sniffer_log_path": str(log_path), "dry_run": dry_run})
    host = sniffer_remote_host(settings)
    if host:
        cleanup_cmd = ["ssh", host, "pkill -f 'nrf802154_sniffer.py|tshark.*802.15.4' >/dev/null 2>&1 || true; sleep 1"]
        manifest.append({"time_utc": now_utc_iso(), "cmd": cleanup_cmd, "purpose": "sniffer-pre-clean", "dry_run": dry_run})
        log(("DRY-RUN " if dry_run else "RUN ") + quote_cmd(cleanup_cmd))
        if not dry_run:
            subprocess.run(cleanup_cmd, check=False, text=True)
    log(("DRY-RUN " if dry_run else "START ") + quote_cmd(cmd) + f" > {log_path}")
    if dry_run:
        return None, log_path
    log_file = log_path.open("w", encoding="utf-8", errors="replace")
    log_file.write(f"# Command: {quote_cmd(cmd)}\n# Started UTC: {now_utc_iso()}\n")
    log_file.flush()
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", bufsize=1)

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

    threading.Thread(target=pump, name="sniffer-log-pump", daemon=True).start()
    time.sleep(2)
    if process.poll() is not None:
        log(f"WARNING: sniffer exited quickly with code {process.returncode}.")
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
        process.kill()
        process.wait(timeout=10)


def find_pcap_path_in_sniffer_log(log_path: Path | None) -> str | None:
    if log_path is None or not log_path.exists():
        return None
    matches = PCAP_PATH_RE.findall(log_path.read_text(encoding="utf-8", errors="replace"))
    return matches[-1] if matches else None


def pull_sniffer_pcap(settings: Settings, *, sniffer_log_path: Path | None, dry_run: bool, manifest: list[dict[str, Any]]) -> tuple[str | None, Path | None]:
    remote_pcap = find_pcap_path_in_sniffer_log(sniffer_log_path)
    if remote_pcap is None:
        return None, None
    local_pcap = settings.run_logs_dir / f"{settings.name_prefix}_sniffer_{settings.run_logs_dir.name}.pcapng"
    host = sniffer_remote_host(settings)
    cmd = ["scp", f"{host}:{remote_pcap}", str(local_pcap)] if host else ["cp", remote_pcap, str(local_pcap)]
    manifest.append({"time_utc": now_utc_iso(), "cmd": cmd, "remote_pcap_path": remote_pcap, "local_pcap_path": str(local_pcap), "dry_run": dry_run})
    log(("DRY-RUN " if dry_run else "FETCH ") + quote_cmd(cmd))
    if not dry_run:
        local_pcap.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(cmd, check=True, text=True)
    return remote_pcap, local_pcap


def normalize_extaddr(value: str | None) -> str | None:
    if not value:
        return None
    hexed = re.sub(r"[^0-9a-fA-F]", "", value).lower()
    if len(hexed) != 16:
        return None
    return ":".join(hexed[i:i+2] for i in range(0, 16, 2))


def extaddr_key(value: str | None) -> str | None:
    norm = normalize_extaddr(value)
    return norm.replace(":", "") if norm else None


def iid_to_extaddr(iid_hex: str) -> str | None:
    iid = re.sub(r"[^0-9a-fA-F]", "", iid_hex).lower()
    if len(iid) != 16:
        return None
    return normalize_extaddr(f"{int(iid[:2], 16) ^ 0x02:02x}" + iid[2:])


def ipv6_link_local_to_extaddr(addr: str) -> str | None:
    if not addr.lower().startswith("fe80"):
        return None
    parts = addr.split("%", 1)[0].split(":")
    if "" in parts:
        empty_index = parts.index("")
        missing = 8 - (len(parts) - 1)
        parts = parts[:empty_index] + ["0"] * missing + parts[empty_index + 1:]
    if len(parts) < 8:
        return None
    return iid_to_extaddr("".join(part.zfill(4) for part in parts[-4:]))


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
        for match in reversed(re.findall(pattern, text, flags=re.IGNORECASE)):
            norm = normalize_extaddr(match)
            if norm:
                return norm
    return None


def parse_child_parent_extaddr(child_log: Path) -> tuple[str | None, str | None]:
    if not child_log.exists():
        return None, None
    text = child_log.read_text(encoding="utf-8", errors="replace")
    explicit_patterns = [
        r"Saved ParentInfo.*?(?:ExtAddr|ExtAddress|Ext Address)[:= ]+([0-9a-fA-F:]{16,23})",
        r"ParentInfo.*?(?:ExtAddr|ExtAddress|Ext Address)[:= ]+([0-9a-fA-F:]{16,23})",
        r"parent.*?(?:ExtAddr|ExtAddress|Ext Address)[:= ]+([0-9a-fA-F:]{16,23})",
    ]
    for pattern in explicit_patterns:
        for match in reversed(re.findall(pattern, text, flags=re.IGNORECASE | re.DOTALL)):
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
        for match in reversed(re.findall(pattern, text, flags=re.IGNORECASE)):
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
        if key and extaddr:
            mapped[key] = {"extaddr": extaddr, "logical_name": logical_name}
    return mapped


def parse_latest_thread_role(log_path: Path | None) -> tuple[str | None, str | None]:
    if log_path is None or not log_path.exists():
        return None, None
    lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()
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


def select_target(router_extaddrs: dict[str, dict[str, str]], parent_key: str, *, seed: int | None, run_index: int) -> dict[str, str] | None:
    candidates = [entry for key, entry in sorted(router_extaddrs.items()) if key != parent_key]
    if not candidates:
        return None
    if seed is None:
        return random.SystemRandom().choice(candidates)
    return random.Random(seed + run_index).choice(candidates)


def send_child_switch_command(settings: Settings, target_extaddr: str, *, dry_run: bool, manifest: list[dict[str, Any]]) -> None:
    command = f"extaddr {extaddr_key(target_extaddr)}\n"
    port = settings.devices["child"]
    manifest.append({"time_utc": now_utc_iso(), "event": "send_child_switch_command", "port": port, "command": command.strip(), "target_extaddr": target_extaddr, "dry_run": dry_run})
    log(f"{'DRY-RUN ' if dry_run else 'SEND '}child switch command `{command.strip()}` to {port}")
    if dry_run:
        return
    with open(port, "wb", buffering=0) as fh:
        fh.write(command.encode("ascii"))
        fh.flush()


def mark_skip(manifest: list[dict[str, Any]], reason: str, details: dict[str, Any]) -> None:
    manifest.append({"time_utc": now_utc_iso(), "type": "skip", "reason": reason, **details})
    log(f"SKIP {reason}: {details}")


def add_label(manifest: list[dict[str, Any]], reason: str, details: dict[str, Any]) -> None:
    manifest.append({"time_utc": now_utc_iso(), "type": "label", "reason": reason, **details})
    log(f"LABEL {reason}: {details}")


def run_timed_sequence(settings: Settings, *, dry_run: bool, manifest: list[dict[str, Any]], run_index: int) -> tuple[Path | None, dict[str, Path], Path | None, str | None, Path | None, str]:
    child_log_path: Path | None = None
    device_loggers: dict[str, subprocess.Popen[str] | None] = {}
    device_log_paths: dict[str, Path] = {}
    sniffer_process: subprocess.Popen[str] | None = None
    sniffer_log_path: Path | None = None
    sniffer_remote_pcap: str | None = None
    sniffer_local_pcap: Path | None = None
    status = "completed"

    try:
        manifest.append({"time_utc": now_utc_iso(), "type": "step", "step": "reset_all_devices"})
        for role in ["router1", "child", "router2", *extra_empty_roles(settings)]:
            erase_flash(settings, role, dry_run=dry_run, manifest=manifest)
            upload(settings, role, "empty", dry_run=dry_run, manifest=manifest)

        require_additional_router_assignments(settings)
        router_plan = router_execution_plan(settings)

        manifest.append({"time_utc": now_utc_iso(), "type": "step", "step": "start_sniffer"})
        sniffer_process, sniffer_log_path = start_sniffer_capture(settings, dry_run=dry_run, manifest=manifest)
        if settings.sniffer.enabled:
            sleep_step(settings.timing.sniffer_lead_in_seconds, "sniffer started; wait before flashing routers", dry_run=dry_run, manifest=manifest)

        manifest.append({"time_utc": now_utc_iso(), "type": "step", "step": "flash_routers", "router_plan": router_plan})
        for router in router_plan:
            upload(settings, router["device_role"], router["config_name"], dry_run=dry_run, manifest=manifest)
            logger, log_path = start_device_log(settings, logical_name=router["logical_name"], config_name=router["config_name"], device_role=router["device_role"], dry_run=dry_run, manifest=manifest)
            device_loggers[router["logical_name"]] = logger
            device_log_paths[router["logical_name"]] = log_path

        sleep_step(settings.timing.router_settling_seconds, "routers flashed; wait before adding child", dry_run=dry_run, manifest=manifest)

        manifest.append({"time_utc": now_utc_iso(), "type": "step", "step": "flash_child"})
        upload(settings, "child", "child", dry_run=dry_run, manifest=manifest)
        child_logger, child_log_path = start_device_log(settings, logical_name="child", config_name="child", device_role="child", dry_run=dry_run, manifest=manifest)
        device_loggers["child"] = child_logger
        device_log_paths["child"] = child_log_path

        sleep_step(settings.timing.child_attach_seconds, "child flashed; wait for natural attach", dry_run=dry_run, manifest=manifest)

        parent_extaddr, parent_source = parse_child_parent_extaddr(child_log_path)
        router_extaddrs = map_router_extaddrs(device_log_paths)
        parent_key = extaddr_key(parent_extaddr)
        parent_match = router_extaddrs.get(parent_key or "")
        details: dict[str, Any] = {
            "child_parent_extaddr": parent_extaddr,
            "child_parent_source": parent_source,
            "parent_key": parent_key,
            "parent_match": parent_match,
            "router_extaddrs": router_extaddrs,
        }

        if not parent_extaddr or not parent_key:
            status = "skipped"
            mark_skip(manifest, SKIP_NO_CHILD_PARENT, details)
        elif not parent_match:
            status = "skipped"
            mark_skip(manifest, SKIP_PARENT_NOT_MAPPED_TO_DEVICE, details)
        else:
            parent_logical = parent_match["logical_name"]
            parent_log_path = device_log_paths.get(parent_logical)
            parent_role, parent_role_source = parse_latest_thread_role(parent_log_path)
            details.update({"parent_logical_name": parent_logical, "parent_log_path": str(parent_log_path) if parent_log_path else None, "parent_thread_role": parent_role, "parent_thread_role_source": parent_role_source})
            if parent_role == "leader":
                add_label(
                    manifest,
                    SKIP_PARENT_IS_LEADER,
                    {**details, "classification_note": SKIP_PARENT_IS_LEADER_NOTE},
                )
            target = select_target(router_extaddrs, parent_key, seed=settings.selection.random_seed, run_index=run_index)
            if target is None:
                status = "skipped"
                mark_skip(manifest, SKIP_NO_ELIGIBLE_TARGET_PARENT, details)
            else:
                parent_plan = {router["logical_name"]: router for router in router_plan}[parent_logical]
                details.update({"target_parent": target, "target_parent_logical_name": target["logical_name"], "target_parent_extaddr": target["extaddr"], "target_selection": "random_non_current_parent", "random_seed": settings.selection.random_seed, "removed_parent_device_role": parent_plan["device_role"]})
                manifest.append({"time_utc": now_utc_iso(), "type": "directed_switch_decision", "action": "will_switch_then_remove", "reason": "TARGET_SELECTED", **details})
                send_child_switch_command(settings, target["extaddr"], dry_run=dry_run, manifest=manifest)
                stop_device_log(device_loggers.get(parent_logical), logical_name=parent_logical, dry_run=dry_run)
                device_loggers[parent_logical] = None
                upload(settings, parent_plan["device_role"], "empty", dry_run=dry_run, manifest=manifest)
                sleep_step(settings.timing.after_parent_removed_seconds, "targeted switch requested and initial parent removed; keep recording", dry_run=dry_run, manifest=manifest)

        stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
        sniffer_process = None
        sniffer_remote_pcap, sniffer_local_pcap = pull_sniffer_pcap(settings, sniffer_log_path=sniffer_log_path, dry_run=dry_run, manifest=manifest)
        return child_log_path, device_log_paths, sniffer_log_path, sniffer_remote_pcap, sniffer_local_pcap, status
    finally:
        stop_sniffer_capture(settings, sniffer_process, dry_run=dry_run)
        for logical_name, process in list(device_loggers.items()):
            stop_device_log(process, logical_name=logical_name, dry_run=dry_run)


def write_manifest(settings: Settings, manifest: list[dict[str, Any]], *, dry_run: bool, status: str, child_log: Path | None, device_logs: dict[str, Path], sniffer_log: Path | None, sniffer_remote_pcap: str | None, sniffer_local_pcap: Path | None) -> Path:
    settings.run_logs_dir.mkdir(parents=True, exist_ok=True)
    path = settings.run_logs_dir / f"{settings.name_prefix}_test_manifest_{settings.run_logs_dir.name}.json"
    payload = {
        "created_utc": now_utc_iso(),
        "status": status,
        "dry_run": dry_run,
        "variant": settings.variant,
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
        "selection": settings.selection.__dict__,
        "n_routers": settings.max_router_number,
        "additional_router_assignments": additional_router_assignments(settings),
        "child_log": str(child_log) if child_log else None,
        "device_logs": {name: str(path) for name, path in sorted(device_logs.items())},
        "sniffer": {"enabled": settings.sniffer.enabled, "command": settings.sniffer.command, "stop_timeout_seconds": settings.sniffer.stop_timeout_seconds, "log": str(sniffer_log) if sniffer_log else None, "remote_pcap": sniffer_remote_pcap, "local_pcap": str(sniffer_local_pcap) if sniffer_local_pcap else None},
        "events": manifest,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def precompile_all(settings: Settings, *, dry_run: bool, manifest: list[dict[str, Any]]) -> None:
    log("Precompiling firmware before timed test sequence.")
    compile_order = [*CORE_COMPILE_ORDER, *additional_router_firmware_names(settings)]
    seen: set[str] = set()
    for name in compile_order:
        if name in seen:
            continue
        seen.add(name)
        yaml_path = config_path(settings, name)
        if settings.clean_before_compile:
            run_command(esphome_base(settings) + ["clean", str(yaml_path)], dry_run=dry_run, manifest=manifest)
        run_command(esphome_base(settings) + ["compile", str(yaml_path)], dry_run=dry_run, manifest=manifest)
    log("Precompile phase complete. No compile commands will be run in the timed sequence.")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run directed ESPHome/OpenThread parent-switching test.")
    parser.add_argument("--variant", choices=sorted(VARIANT_PRESETS), default="ucast", help="Select test variant.")
    parser.add_argument("--config", default=None, help="Path to device/config TOML file.")
    parser.add_argument("--esphome-bin", help="Override ESPHome executable. Overrides ESPHOME_BIN and TOML.")
    parser.add_argument("--dry-run", action="store_true", help="Print commands and write a manifest without executing ESPHome.")
    parser.add_argument("--precompile-only", action="store_true", help="Compile all firmware and exit before any flashing.")
    parser.add_argument("--skip-precompile", action="store_true", help="Skip precompile phase. Not recommended for measurement runs.")
    parser.add_argument("--force-precompile", action="store_true", help="Force precompile phase even if disabled in TOML.")
    parser.add_argument("--clean-before-compile", action="store_true", help="Run `esphome clean` before each compile.")
    parser.add_argument("--allow-same-port", action="store_true", help="Permit multiple roles to use the same serial port.")
    parser.add_argument("--runs", type=int, default=1, help="Number of timed test runs to execute sequentially.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.runs < 1:
        raise SystemExit("--runs must be at least 1.")
    if args.config is None:
        args.config = str(VARIANT_PRESETS[args.variant]["default_config"])
    settings = load_settings(args)
    set_batch_log(settings.logs_dir / f"{settings.logs_dir.name}.log" if args.runs > 1 else None)

    log(f"Using ESPHome: {settings.esphome_bin}")
    log(f"Using esptool: {settings.esptool_bin}")
    log(f"Using configs: {settings.configs_dir}")
    log(f"Using logs base: {settings.logs_dir}")
    log(f"Variant: {settings.variant}")
    log(f"Requested routers: {settings.max_router_number}")
    log(f"Requested runs: {args.runs}")

    compile_manifest: list[dict[str, Any]] = []
    if settings.precompile:
        precompile_all(settings, dry_run=args.dry_run, manifest=compile_manifest)
    else:
        log("WARNING: precompile phase skipped. Uploads may fail if the most recent firmware builds do not exist.")
    if args.precompile_only:
        return 0

    for run_index in range(1, args.runs + 1):
        settings.run_logs_dir = build_run_logs_dir(settings.logs_dir, run_index=run_index) if args.runs > 1 else build_run_logs_dir(settings.logs_dir)
        log(f"Starting run {run_index}/{args.runs}")
        log(f"Using run logs dir: {settings.run_logs_dir}")
        manifest = list(compile_manifest)
        status = "failed"
        child_log = None
        device_logs: dict[str, Path] = {}
        sniffer_log = None
        sniffer_remote_pcap = None
        sniffer_local_pcap = None
        try:
            child_log, device_logs, sniffer_log, sniffer_remote_pcap, sniffer_local_pcap, status = run_timed_sequence(settings, dry_run=args.dry_run, manifest=manifest, run_index=run_index)
        finally:
            manifest_path = write_manifest(settings, manifest, dry_run=args.dry_run, status=status, child_log=child_log, device_logs=device_logs, sniffer_log=sniffer_log, sniffer_remote_pcap=sniffer_remote_pcap, sniffer_local_pcap=sniffer_local_pcap)
            log(f"Manifest written: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
