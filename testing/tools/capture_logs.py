#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import threading
from pathlib import Path


def stream_reader(prefix: str, proc: subprocess.Popen, out):
    assert proc.stdout is not None
    for line in proc.stdout:
        ts = dt.datetime.now(dt.UTC).isoformat(timespec='milliseconds')
        out.write(f'{ts} {prefix} {line}')
        out.flush()


def main() -> int:
    parser = argparse.ArgumentParser(description='Capture timestamped ESPHome logs from multiple nodes.')
    parser.add_argument('--duration', type=int, default=120, help='Capture duration in seconds.')
    parser.add_argument('--out', type=Path, default=Path('testing/logs/switch_test.log'))
    parser.add_argument(
        '--node',
        action='append',
        required=True,
        metavar='LABEL=PORT',
        help='Node label and serial port mapping, e.g. child=/dev/ttyACM0',
    )
    parser.add_argument('--baud', type=int, default=115200)
    parser.add_argument(
        '--config',
        type=Path,
        default=Path('testing/configs/child_variant_multicast.yaml'),
        help='ESPHome YAML used by `esphome logs`.',
    )
    parser.add_argument(
        '--reset-label',
        action='append',
        default=['child'],
        help='Node label(s) that should be reset before log streaming (default: child).',
    )
    args = parser.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)

    mappings: list[tuple[str, str]] = []
    for item in args.node:
        if '=' not in item:
            raise SystemExit(f'Invalid --node value: {item}')
        label, port = item.split('=', 1)
        mappings.append((label.strip(), port.strip()))

    reset_labels = {x.strip() for x in args.reset_label if x.strip()}

    procs: list[tuple[str, subprocess.Popen]] = []
    threads: list[threading.Thread] = []

    with args.out.open('w', encoding='utf-8') as out:
        out.write(f'# capture-start {dt.datetime.now(dt.UTC).isoformat()}\n')
        out.write(f'# duration-seconds {args.duration}\n')
        out.write(f'# baud {args.baud}\n')
        for label, port in mappings:
            out.write(f'# node {label} {port}\n')

        for label, port in mappings:
            cmd = [
                '.venv/bin/esphome',
                'logs',
                str(args.config),
                '--device',
                port,
            ]
            if label in reset_labels:
                cmd.append('--reset')
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
            procs.append((label, proc))
            t = threading.Thread(target=stream_reader, args=(f'[{label}]', proc, out), daemon=True)
            t.start()
            threads.append(t)

        try:
            threading.Event().wait(args.duration)
        finally:
            for _, proc in procs:
                proc.terminate()
            for _, proc in procs:
                proc.wait(timeout=10)

        out.write(f'# capture-end {dt.datetime.now(dt.UTC).isoformat()}\n')

    print(f'Wrote {args.out}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
