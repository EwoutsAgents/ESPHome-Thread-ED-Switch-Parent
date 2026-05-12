#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import time

import serial


def main() -> int:
    parser = argparse.ArgumentParser(description="Send Thread control commands over router serial console.")
    parser.add_argument("--port", required=True)
    parser.add_argument("action", choices=["on", "off", "status", "suspend"])
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--duration-ms", type=int, default=0)
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
        ser.reset_input_buffer()
        if args.action == "suspend":
            if args.duration_ms <= 0:
                raise SystemExit("--duration-ms must be > 0 for suspend")
            command = f"thread suspend {args.duration_ms}"
            expect = "THREAD_CTL ack result=ok command=suspend"
        elif args.action == "status":
            command = "thread status"
            expect = "THREAD_CTL status"
        else:
            command = f"thread {args.action}"
            expect = f"THREAD_CTL ack result=ok reason=command_{args.action}"

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
