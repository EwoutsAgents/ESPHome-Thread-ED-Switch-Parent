#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import time

import serial


def main() -> int:
    parser = argparse.ArgumentParser(description="Send Thread control commands over router serial console.")
    parser.add_argument("--port", required=True)
    parser.add_argument("action", choices=["on", "off", "state", "status"])
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

        if args.action == "off":
            if args.duration_s <= 0:
                raise SystemExit("--duration-s must be > 0 for off")
            command = f"thread off {args.duration_s}"
            expect = "USB_CTL thread off -> OT_ERROR_NONE"
        elif args.action in ("state", "status"):
            command = "thread state"
            expect = "USB_CTL thread state enabled="
        else:
            command = "thread on"
            expect = "USB_CTL thread on -> OT_ERROR_NONE"

        ser.write((command + "\n").encode("utf-8"))
        ser.flush()

        deadline = time.time() + args.timeout
        captured: list[str] = []
        while time.time() < deadline:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if not line:
                continue
            captured.append(line)
            print(line)
            if expect in line:
                return 0
        print(f"Timed out waiting for: {expect}", file=sys.stderr)
        if captured:
            print("Last lines:", file=sys.stderr)
            for line in captured[-10:]:
                print(line, file=sys.stderr)
        return 1
    finally:
        ser.close()


if __name__ == "__main__":
    raise SystemExit(main())
