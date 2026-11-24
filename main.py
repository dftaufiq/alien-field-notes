#!/usr/bin/env python3
"""Alien Field Notes entry: one alien tourist's review of Earth."""
import os
import sys

LINE = "Four stars. The locals pay to lift heavy objects, then set them gently back down where they found them."


def main():
    if not LINE.strip() or "\n" in LINE or "\r" in LINE or len(LINE) > 200:
        print("entry must be one clean line of 1-200 chars", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Revision: read-back verification — confirm what landed on disk
    # matches the intended line byte-for-byte; fail loudly otherwise.
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != LINE:
            print("entry.txt read-back mismatch", file=sys.stderr)
            return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
