#!/usr/bin/env python3
"""Count words and estimate reading/speaking time for a text or transcript file.

Bundled helper for the /wordcount skill (Build 3). Local only, no network,
no API - so it can't break on camera.

Usage:
    python3 wordcount.py <file>
"""
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("usage: wordcount.py <file>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1]).expanduser()
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)
    text = path.read_text(errors="ignore")
    words = len(text.split())
    speaking_min = words / 150.0   # ~150 words per minute spoken
    reading_min = words / 230.0    # ~230 words per minute read
    print(f"File: {path.name}")
    print(f"Words: {words}")
    print(f"Speaking time: ~{speaking_min:.1f} min (150 wpm)")
    print(f"Reading time:  ~{reading_min:.1f} min (230 wpm)")


if __name__ == "__main__":
    main()
