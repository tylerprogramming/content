#!/usr/bin/env python3
"""Convert a yt-dlp .en.vtt auto-caption file into ~/content/transcripts/transcript_<id>.txt
with [mm:ss] prefixed lines. Usage: vtt_to_transcript.py <vtt_path> <video_id>"""
import re
import sys
from pathlib import Path

vtt_path, vid = sys.argv[1], sys.argv[2]
raw = Path(vtt_path).read_text(encoding="utf-8", errors="ignore")

TS = re.compile(r"^(\d\d):(\d\d):(\d\d)\.\d{3} --> ")
TAG = re.compile(r"<[^>]+>")

blocks = []  # (seconds, text)
cur_t = None
for line in raw.splitlines():
    m = TS.match(line)
    if m:
        h, mi, s = map(int, m.groups())
        cur_t = h * 3600 + mi * 60 + s
        continue
    if cur_t is None or not line.strip() or line.startswith(("WEBVTT", "Kind:", "Language:")):
        continue
    text = TAG.sub("", line).strip()
    if not text:
        continue
    # auto captions repeat the previous cue; keep only new text
    if blocks and blocks[-1][1] == text:
        continue
    if blocks and text.startswith(blocks[-1][1]):
        blocks[-1] = (blocks[-1][0], text)
        continue
    blocks.append((cur_t, text))

# merge into ~8 second windows
out = []
win_start, buf = None, []
for t, text in blocks:
    if win_start is None:
        win_start = t
    buf.append(text)
    if t - win_start >= 8 or len(" ".join(buf)) > 180:
        out.append((win_start, " ".join(buf)))
        win_start, buf = None, []
if buf:
    out.append((win_start, " ".join(buf)))

# dedupe adjacent overlaps produced by rolling captions
lines = []
for t, text in out:
    if lines and text in lines[-1]:
        continue
    m, s = divmod(int(t), 60)
    lines.append(f"[{m:02d}:{s:02d}] {text}")

dest = Path.home() / "content" / "transcripts" / f"transcript_{vid}.txt"
dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"{dest} {len(lines)} lines")
