#!/usr/bin/env python3
"""Run the stock OpenThread parent-switching test sequence.

This script implements the sequence documented in testing/README.md:
  1. Flash all test ESP32-C6 devices with empty.yaml.
  2. Flash router 1 with stock_router_1.yaml.
  3. Wait 10 seconds.
  4. Flash the child with stock_child.yaml and record child logs.
  5. Wait 30 seconds.
  6. Flash router 2 with stock_router_2.yaml.
  7. Wait 60 seconds.
  8. Flash router 1 with empty.yaml.
  9. Continue recording child logs for 300 seconds.
 10. Stop the recording.

The default command for flashing is `esphome run <yaml> --device <port> --no-logs`,
so firmware is compiled if needed and uploaded without entering the log view.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import platform
import shlex
import shutil
import signal
import subprocess
import sys
import threading
import time
from typing import Any, Dict, Iterable, List, Optional

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover - fallback message handled at runtime
    tomllib = None  # type: ignore[assignment]

ROLE_ORDER = ("router1", "child", "router2")
CONFIG_FILES = {
    "empty": "empty.yaml",
    "router1": "stock_router_1.yaml",
    "child": "stock_child.yaml",
    "router2": "stock_router_2.yaml",
}
DEFAULT_TIMINGS = {
    "after_router1_flash": 10,
    "after_child_flash_before_router2": 30,
    "after_router2_flash_before_router1_empty": 60,
    "after_router1_empty_log_duration": 300,
}


class StockTestError(RuntimeError):
    """Raised when the stock test cannot continue safely."""


class ChildLogProcess:
    """Manage the background `esphome logs` process for the child device."""

    def __init__(
        self,
        command: List[str],
        log_path: Path,
        command_log_path: Path,
        echo: bool = True,
        dry_run: bool = False,
    ) -> None:
        self.command = command
        self.log_path = log_path
        self.command_log_path = command_log_path
        self.echo = echo
        self.dry_run = dry_run
        self.process: Optional[subprocess.Popen[str]] = None
        self._thread: Optional[threading.Thread] = None
        self._stop_requested = threading.Event()

    def start(self) -> None:
        write_command_log(self.command_log_path, "START CHILD LOG", self.command)
        print(f"\n==> Starting child log capture: {self.log_path}")
        print(format_command(self.command))
        if self.dry_run:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            self.log_path.write_text(
                "DRY RUN: child log capture would have run with command:\n"
                f"{format_command(self.command)}\n",
                encoding="utf-8",
            )
            return

        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        creationflags = 0
        if platform.system() == "Windows":  # allows CTRL_BREAK_EVENT on Windows
            creationflags = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)

        self.process = subprocess.Popen(
            self.command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            creationflags=creationflags,
        )
        self._thread = threading.Thread(target=self._read_stdout, name="child-log-reader", daemon=True)
        self._thread.start()

    def _read_stdout(self) -> None:
        assert self.process is not None
        assert self.process.stdout is not None
        with self.log_path.open("a", encoding="utf-8", buffering=1) as log_file:
            log_file.write(f"# Command: {format_command(self.command)}\n")
            log_file.write(f"# Started UTC: {utc_now_iso()}\n")
            for line in self.process.stdout:
                log_file.write(line)
                if self.echo:
                    print(f"[child] {line}", end="")
            log_file.write(f"# Reader ended UTC: {utc_now_iso()}\n")

    def stop(self, timeout: int = 15) -> Dict[str, Any]:
        result: Dict[str, Any] = {"stopped": False, "returncode": None}
        if self.dry_run:
            write_command_log(self.command_log_path, "STOP CHILD LOG", ["<dry-run>"])
            result.update({"stopped": True, "returncode": 0})
            return result
        if self.process is None:
            return result
        if self.process.poll() is not None:
            result.update({"stopped": True, "returncode": self.process.returncode})
            return result

        print("\n==> Stopping child log capture")
        try:
            if platform.system() == "Windows":
                self.process.send_signal(signal.CTRL_BREAK_EVENT)  # type: ignore[attr-defined]
            else:
                self.process.send_signal(signal.SIGINT)
            self.process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=5)

        if self._thread is not None:
            self._thread.join(timeout=5)
        result.update({"stopped": True, "returncode": self.process.returncode})
        write_command_log(self.command_log_path, "STOP CHILD LOG", ["returncode", str(self.process.returncode)])
        return result


def utc_now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def local_timestamp() -> str:
    return dt.datetime.now().strftime("%Y%m%d-%H%M%S")


def format_command(command: Iterable[str]) -> str:
    return " ".join(shlex.quote(part) for part in command)


def write_command_log(path: Path, label: str, command: Iterable[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(f"[{utc_now_iso()}] {label}: {format_command(command)}\n")


def load_toml(path: Optional[Path]) -> Dict[str, Any]:
    if path is None:
        return {}
    if tomllib is None:
        raise StockTestError(
            "TOML config files require Python 3.11+. Either use Python 3.11+ or pass ports via CLI flags."
        )
    with path.open("rb") as f:
        return tomllib.load(f)


def config_value(
    cli_value: Optional[Any],
    config: Dict[str, Any],
    section: str,
    key: str,
    default: Optional[Any] = None,
) -> Any:
    if cli_value is not None:
        return cli_value
    return config.get(section, {}).get(key, default)


def resolve_path(raw_path: str | Path, base_dir: Path) -> Path:
    path = Path(raw_path).expanduser()
    if path.is_absolute():
        return path
    return (base_dir / path).resolve()


def ensure_distinct_ports(devices: Dict[str, str], extra_reset_ports: List[str]) -> None:
    seen: Dict[str, str] = {}
    for role, port in devices.items():
        if port in seen:
            raise StockTestError(
                f"Device roles must use distinct ports. {role!r} and {seen[port]!r} both use {port!r}."
            )
        seen[port] = role
    for port in extra_reset_ports:
        if port in seen:
            raise StockTestError(
                f"Extra reset port {port!r} duplicates the {seen[port]!r} role port."
            )
        seen[port] = "extra_reset_port"


def has_path_separator(value: str) -> bool:
    return "/" in value or "\\" in value or os.path.sep in value or (os.path.altsep is not None and os.path.altsep in value)


def executable_exists(executable: str) -> bool:
    if has_path_separator(executable) or Path(executable).is_absolute():
        path = Path(executable).expanduser()
        return path.exists() and (os.access(path, os.X_OK) or platform.system() == "Windows")
    return shutil.which(executable) is not None


def local_venv_esphome_candidates(config_base: Path) -> List[Path]:
    """Return likely local-venv ESPHome executables, ordered from most to least specific."""
    script_path = Path(__file__).resolve()
    likely_roots = [
        config_base,
        config_base.parent,
        Path.cwd(),
        Path.cwd().parent,
    ]
    if len(script_path.parents) >= 3:
        # For <repo>/testing/scripts/run_stock_test.py, parents[2] is <repo>.
        likely_roots.append(script_path.parents[2])

    executable_names = (
        ("Scripts", "esphome.exe"),
        ("Scripts", "esphome"),
        ("bin", "esphome"),
    )
    candidates: List[Path] = []
    seen: set[str] = set()
    for root in likely_roots:
        root = root.expanduser().resolve()
        for directory, executable in executable_names:
            candidate = root / "venv" / directory / executable
            key = str(candidate)
            if key not in seen:
                candidates.append(candidate)
                seen.add(key)
    return candidates


def resolve_executable_path(raw_value: str, base_dir: Path) -> str:
    value = os.path.expanduser(os.path.expandvars(raw_value))
    path = Path(value)
    if path.is_absolute():
        return str(path)
    if has_path_separator(value):
        return str((base_dir / path).resolve())
    return value


def resolve_esphome_bin(cli_value: Optional[str], config: Dict[str, Any], config_base: Path) -> str:
    """Resolve the ESPHome CLI, preferring a repository-local ./venv when available."""
    config_value_raw = config.get("esphome", {}).get("bin")
    env_value = os.environ.get("ESPHOME_BIN")

    if cli_value:
        return resolve_executable_path(str(cli_value), Path.cwd())
    if env_value:
        return resolve_executable_path(env_value, Path.cwd())

    # Treat an omitted value or plain `esphome` as "use the local venv when present".
    if config_value_raw in (None, "", "esphome"):
        for candidate in local_venv_esphome_candidates(config_base):
            if candidate.exists():
                return str(candidate)
        return "esphome"

    return resolve_executable_path(str(config_value_raw), config_base)


def build_flash_command(
    esphome_bin: str,
    config_file: Path,
    device: str,
    flash_command: str,
    upload_speed: Optional[str],
) -> List[str]:
    if flash_command == "run":
        command = [esphome_bin, "run", str(config_file), "--device", device, "--no-logs"]
    elif flash_command == "upload":
        command = [esphome_bin, "upload", str(config_file), "--device", device]
    else:
        raise StockTestError(f"Unsupported flash command: {flash_command}")
    if upload_speed:
        command.extend(["--upload_speed", str(upload_speed)])
    return command


def build_log_command(esphome_bin: str, config_file: Path, device: str, no_states: bool) -> List[str]:
    command = [esphome_bin, "logs", str(config_file), "--device", device]
    if no_states:
        command.append("--no-states")
    return command


def run_checked(
    label: str,
    command: List[str],
    command_log_path: Path,
    dry_run: bool = False,
) -> Dict[str, Any]:
    started = utc_now_iso()
    print(f"\n==> {label}")
    print(format_command(command))
    write_command_log(command_log_path, f"START {label}", command)
    if dry_run:
        return {"label": label, "command": command, "started_utc": started, "ended_utc": utc_now_iso(), "returncode": 0}

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    assert process.stdout is not None
    for line in process.stdout:
        print(line, end="")
    return_code = process.wait()
    ended = utc_now_iso()
    write_command_log(command_log_path, f"END {label}", ["returncode", str(return_code)])
    if return_code != 0:
        raise StockTestError(f"Command failed during {label!r} with exit code {return_code}: {format_command(command)}")
    return {"label": label, "command": command, "started_utc": started, "ended_utc": ended, "returncode": return_code}


def sleep_with_progress(seconds: int | float, label: str, dry_run: bool = False) -> Dict[str, Any]:
    started = utc_now_iso()
    seconds = float(seconds)
    print(f"\n==> Waiting {seconds:g}s: {label}")
    if dry_run or seconds <= 0:
        return {"label": label, "seconds": seconds, "started_utc": started, "ended_utc": utc_now_iso()}

    deadline = time.monotonic() + seconds
    next_notice = time.monotonic()
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        if time.monotonic() >= next_notice:
            print(f"    {max(0, int(round(remaining)))}s remaining")
            next_notice = time.monotonic() + min(30, max(5, seconds / 5))
        time.sleep(min(1.0, remaining))
    return {"label": label, "seconds": seconds, "started_utc": started, "ended_utc": utc_now_iso()}


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the stock ESPHome/OpenThread parent-switching test sequence.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--config", type=Path, help="Optional TOML file with devices, paths, and timings.")
    parser.add_argument("--router1-port", help="Serial port for the ESP32-C6 that always runs stock_router_1.yaml.")
    parser.add_argument("--child-port", help="Serial port for the ESP32-C6 that always runs stock_child.yaml.")
    parser.add_argument("--router2-port", help="Serial port for the ESP32-C6 that always runs stock_router_2.yaml.")
    parser.add_argument(
        "--extra-reset-port",
        action="append",
        default=None,
        help="Additional connected ESP32-C6 serial port to reset with empty.yaml before the test. Repeatable.",
    )
    parser.add_argument("--config-dir", type=Path, help="Directory containing empty.yaml and stock_*.yaml files.")
    parser.add_argument("--log-dir", type=Path, help="Directory for child logs and run manifests.")
    parser.add_argument("--esphome-bin", help="ESPHome CLI executable.")
    parser.add_argument(
        "--flash-command",
        choices=("run", "upload"),
        help="Use `run --no-logs` to compile+upload, or `upload` to upload an already-built firmware.",
    )
    parser.add_argument("--upload-speed", help="Optional ESPHome --upload_speed value.")
    parser.add_argument("--child-log-file", type=Path, help="Explicit child .log path. Defaults to timestamped file in log-dir.")
    parser.add_argument("--no-child-log-echo", action="store_true", help="Do not mirror child log lines to the console.")
    parser.add_argument("--no-states", action="store_true", help="Pass --no-states to `esphome logs`.")
    parser.add_argument("--skip-initial-reset", action="store_true", help="Skip the initial empty.yaml flash of all devices.")
    parser.add_argument("--dry-run", action="store_true", help="Print the sequence and create dry-run logs without calling ESPHome or sleeping.")
    parser.add_argument("--timing-after-router1", type=float, help="Override wait after flashing router 1.")
    parser.add_argument("--timing-after-child", type=float, help="Override wait after flashing/logging child before router 2.")
    parser.add_argument("--timing-after-router2", type=float, help="Override wait after flashing router 2 before removing router 1.")
    parser.add_argument("--timing-after-router1-empty", type=float, help="Override child log duration after flashing router 1 with empty.yaml.")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    config_file = args.config.resolve() if args.config else None
    config_base = config_file.parent if config_file else Path.cwd()
    config = load_toml(config_file)

    devices = {
        "router1": config_value(args.router1_port, config, "devices", "router1"),
        "child": config_value(args.child_port, config, "devices", "child"),
        "router2": config_value(args.router2_port, config, "devices", "router2"),
    }
    missing_roles = [role for role, value in devices.items() if not value]
    if missing_roles:
        raise StockTestError(
            "Missing device port(s): " + ", ".join(missing_roles) + ". Pass them on the CLI or in the TOML config."
        )
    devices = {role: str(port) for role, port in devices.items()}
    extra_reset_ports = args.extra_reset_port
    if extra_reset_ports is None:
        extra_reset_ports = list(config.get("devices", {}).get("extra_reset_ports", []))

    ensure_distinct_ports(devices, [str(port) for port in extra_reset_ports])

    config_dir_raw = config_value(args.config_dir, config, "paths", "config_dir", "configs")
    log_dir_raw = config_value(args.log_dir, config, "paths", "log_dir", "logs")
    config_dir = resolve_path(config_dir_raw, config_base)
    log_dir = resolve_path(log_dir_raw, config_base)
    log_dir.mkdir(parents=True, exist_ok=True)

    esphome_bin = resolve_esphome_bin(args.esphome_bin, config, config_base)
    if not args.dry_run and not executable_exists(esphome_bin):
        searched = "\n".join(f"  - {path}" for path in local_venv_esphome_candidates(config_base))
        raise StockTestError(
            f"ESPHome executable not found: {esphome_bin!r}. "
            "Create/activate the local venv, set ESPHOME_BIN, or pass --esphome-bin.\n"
            f"Local venv paths checked:\n{searched}"
        )

    flash_command = str(config_value(args.flash_command, config, "esphome", "flash_command", "run"))
    upload_speed = config_value(args.upload_speed, config, "esphome", "upload_speed")

    timings = dict(DEFAULT_TIMINGS)
    timings.update(config.get("timing", {}))
    if args.timing_after_router1 is not None:
        timings["after_router1_flash"] = args.timing_after_router1
    if args.timing_after_child is not None:
        timings["after_child_flash_before_router2"] = args.timing_after_child
    if args.timing_after_router2 is not None:
        timings["after_router2_flash_before_router1_empty"] = args.timing_after_router2
    if args.timing_after_router1_empty is not None:
        timings["after_router1_empty_log_duration"] = args.timing_after_router1_empty

    config_paths = {name: config_dir / filename for name, filename in CONFIG_FILES.items()}
    for name, path in config_paths.items():
        if not path.exists():
            raise StockTestError(f"Required {name} config does not exist: {path}")

    run_id = local_timestamp()
    child_log_path = args.child_log_file or (log_dir / f"stock_child_{run_id}.log")
    if not child_log_path.is_absolute():
        child_log_path = (Path.cwd() / child_log_path).resolve()
    command_log_path = log_dir / f"stock_test_{run_id}_commands.log"
    manifest_path = log_dir / f"stock_test_{run_id}_manifest.json"

    steps: List[Dict[str, Any]] = []
    child_logger: Optional[ChildLogProcess] = None
    manifest: Dict[str, Any] = {
        "run_id": run_id,
        "started_utc": utc_now_iso(),
        "status": "running",
        "devices": devices,
        "extra_reset_ports": extra_reset_ports,
        "config_dir": str(config_dir),
        "log_dir": str(log_dir),
        "child_log_file": str(child_log_path),
        "command_log_file": str(command_log_path),
        "timing_seconds": timings,
        "esphome_bin": esphome_bin,
        "flash_command": flash_command,
        "upload_speed": upload_speed,
        "dry_run": args.dry_run,
        "steps": steps,
    }

    def flash(label: str, config_key: str, port: str) -> None:
        command = build_flash_command(esphome_bin, config_paths[config_key], port, flash_command, upload_speed)
        steps.append(run_checked(label, command, command_log_path, dry_run=args.dry_run))

    try:
        print("Stock OpenThread parent-switching test")
        print(f"Run id: {run_id}")
        print("Device assignment:")
        for role in ROLE_ORDER:
            print(f"  {role}: {devices[role]}")
        if extra_reset_ports:
            print("  extra reset ports: " + ", ".join(extra_reset_ports))
        print(f"Child log: {child_log_path}")

        if not args.skip_initial_reset:
            for role in ROLE_ORDER:
                flash(f"Initial reset: flash {role} with empty.yaml", "empty", devices[role])
            for index, port in enumerate(extra_reset_ports, start=1):
                flash(f"Initial reset: flash extra device {index} with empty.yaml", "empty", str(port))

        flash("Flash router 1 with stock_router_1.yaml", "router1", devices["router1"])
        steps.append(sleep_with_progress(timings["after_router1_flash"], "router 1 settle before child joins", args.dry_run))

        flash("Flash child with stock_child.yaml", "child", devices["child"])
        child_logger = ChildLogProcess(
            command=build_log_command(esphome_bin, config_paths["child"], devices["child"], args.no_states),
            log_path=child_log_path,
            command_log_path=command_log_path,
            echo=not args.no_child_log_echo,
            dry_run=args.dry_run,
        )
        child_logger.start()
        steps.append({"label": "Start child log capture", "command": child_logger.command, "started_utc": utc_now_iso()})

        steps.append(
            sleep_with_progress(
                timings["after_child_flash_before_router2"],
                "child attached/logging before router 2 is introduced",
                args.dry_run,
            )
        )
        flash("Flash router 2 with stock_router_2.yaml", "router2", devices["router2"])
        steps.append(
            sleep_with_progress(
                timings["after_router2_flash_before_router1_empty"],
                "router 2 present before router 1 is removed",
                args.dry_run,
            )
        )
        flash("Flash router 1 with empty.yaml to remove first parent", "empty", devices["router1"])
        steps.append(
            sleep_with_progress(
                timings["after_router1_empty_log_duration"],
                "continue child log capture after router 1 removal",
                args.dry_run,
            )
        )

        if child_logger is not None:
            steps.append({"label": "Stop child log capture", "result": child_logger.stop(), "ended_utc": utc_now_iso()})
        manifest["status"] = "completed"
        return 0
    except KeyboardInterrupt:
        manifest["status"] = "interrupted"
        print("\nInterrupted by user; stopping child logger if it is running.", file=sys.stderr)
        if child_logger is not None:
            steps.append({"label": "Stop child log capture after interrupt", "result": child_logger.stop(), "ended_utc": utc_now_iso()})
        return 130
    except Exception as exc:
        manifest["status"] = "failed"
        manifest["error"] = str(exc)
        if child_logger is not None:
            steps.append({"label": "Stop child log capture after failure", "result": child_logger.stop(), "ended_utc": utc_now_iso()})
        raise
    finally:
        manifest["ended_utc"] = utc_now_iso()
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
        print(f"\nManifest: {manifest_path}")
        print(f"Command log: {command_log_path}")
        print(f"Child log: {child_log_path}")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except StockTestError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
