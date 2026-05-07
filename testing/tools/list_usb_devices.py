#!/usr/bin/env python3
from __future__ import annotations

import glob
from pathlib import Path


def main() -> int:
    by_id = sorted(Path('/dev/serial/by-id').glob('*'))
    if by_id:
        print('Detected USB serial devices (stable names):')
        for p in by_id:
            try:
                target = p.resolve()
            except FileNotFoundError:
                target = Path('<missing>')
            print(f'- {p} -> {target}')
    else:
        print('No /dev/serial/by-id entries found.')

    tty_nodes = sorted(glob.glob('/dev/ttyACM*') + glob.glob('/dev/ttyUSB*'))
    print('\nDetected tty nodes:')
    for n in tty_nodes:
        print(f'- {n}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
