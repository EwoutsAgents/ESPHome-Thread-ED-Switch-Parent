#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
import time

import serial


def read_until(ser: serial.Serial, expect: str, timeout: float) -> tuple[bool, list[str]]:
    deadline = time.time() + timeout
    captured: list[str] = []
    while time.time() < deadline:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if not line:
            continue
        captured.append(line)
        print(line, flush=True)
        if expect in line:
            return True, captured
    return False, captured


def contains_any(lines: list[str], needles: tuple[str, ...]) -> bool:
    return any(any(needle in line for needle in needles) for line in lines)


def stream_lines_for(ser: serial.Serial, duration_s: float) -> list[str]:
    deadline = time.time() + duration_s
    captured: list[str] = []
    while time.time() < deadline:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if not line:
            continue
        captured.append(line)
        print(line, flush=True)
    return captured


def verify_stays_disabled(ser: serial.Serial, duration_s: float, poll_interval_s: float = 1.0) -> bool:
    deadline = time.time() + duration_s
    while time.time() < deadline:
        ser.write(b"thread state\n")
        ser.flush()
        ok, captured = read_until(ser, "USB_CTL thread state enabled=", poll_interval_s + 2.0)
        if not ok:
            print("Timed out waiting for periodic thread state during hold", file=sys.stderr)
            return False
        if contains_any(captured, ("USB_CTL thread state enabled=true",)):
            print("Router re-enabled during off-hold window", file=sys.stderr)
            return False
        remaining = deadline - time.time()
        if remaining > 0:
            time.sleep(min(poll_interval_s, remaining))
    return True


def extract_extaddr(lines: list[str]) -> str:
    for line in reversed(lines):
        m = re.search(r"extaddr=([0-9a-fA-F]{16})", line)
        if m:
            return m.group(1).lower()
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Send Thread control commands over router serial console.")
    parser.add_argument("--port", required=True)
    parser.add_argument("action", choices=["on", "off", "state", "status", "extaddr", "off-verify-disabled", "off-hold-verify-disabled", "off-verify-disabled-hold"])
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--timeout", type=float, default=8.0)
    parser.add_argument("--duration-s", type=int, default=60)
    args = parser.parse_args()

    ser = serial.Serial()
    ser.port = args.port
    ser.baudrate = args.baud
    ser.timeout = 0.1
    ser.write_timeout = 2
    ser.rtscts = False
    ser.dsrdtr = False
    ser.exclusive = True
    ser.dtr = False
    ser.rts = False
    ser.open()

    try:
        settle_deadline = time.time() + 2.5
        while time.time() < settle_deadline:
            ser.read(4096)

        ser.reset_input_buffer()

        if args.action in ("off", "off-verify-disabled", "off-hold-verify-disabled", "off-verify-disabled-hold"):
            if args.duration_s <= 0:
                raise SystemExit("--duration-s must be > 0 for off")
            ser.write((f"thread off {args.duration_s}\n").encode("utf-8"))
            ser.flush()
            ok, captured = read_until(ser, "USB_CTL thread off -> OT_ERROR_NONE", args.timeout)
            if not ok:
                print("Timed out waiting for: USB_CTL thread off -> OT_ERROR_NONE", file=sys.stderr)
                if captured:
                    print("Last lines:", file=sys.stderr)
                    for line in captured[-10:]:
                        print(line, file=sys.stderr, flush=True)
                return 1
            if args.action == "off":
                return 0

            ser.write(b"thread state\n")
            ser.flush()
            ok, captured = read_until(ser, "USB_CTL thread state enabled=false role=disabled", args.timeout)
            if ok and args.action == "off-verify-disabled":
                return 0
            if ok and args.action in ("off-hold-verify-disabled", "off-verify-disabled-hold"):
                if args.action == "off-verify-disabled-hold":
                    print("USB_CTL_READY_DISABLED", flush=True)
                if not verify_stays_disabled(ser, args.duration_s):
                    return 1
                return 0
            print("Timed out waiting for: USB_CTL thread state enabled=false role=disabled", file=sys.stderr)
            if captured:
                print("Last lines:", file=sys.stderr)
                for line in captured[-10:]:
                    print(line, file=sys.stderr, flush=True)
            return 1

        if args.action in ("state", "status", "extaddr"):
            command = "thread state"
            expect = "USB_CTL thread state enabled="
        else:
            command = "thread on"
            expect = "USB_CTL thread on -> OT_ERROR_NONE"

        ser.write((command + "\n").encode("utf-8"))
        ser.flush()

        ok, captured = read_until(ser, expect, args.timeout)
        if not ok and args.action == "on":
            ok = contains_any(captured, (
                "USB_CTL thread on -> InvalidState (treated as success; stack already enabled:",
            ))
        if ok and args.action == "extaddr":
            extaddr = extract_extaddr(captured)
            if not extaddr:
                print("Failed to parse extaddr from thread state", file=sys.stderr)
                return 1
            print(extaddr, flush=True)
            return 0
        if ok:
            return 0
        print(f"Timed out waiting for: {expect}", file=sys.stderr)
        if captured:
            print("Last lines:", file=sys.stderr)
            for line in captured[-10:]:
                print(line, file=sys.stderr, flush=True)
        return 1
    finally:
        ser.close()


if __name__ == "__main__":
    raise SystemExit(main())
