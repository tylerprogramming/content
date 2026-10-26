#!/usr/bin/env python3
"""Generate 4 YouTube Library cover directions with GPT Image 2 (Kie.ai), in parallel."""
import subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
G = str(Path.home() / ".hermes/skills/creative/kie-gpt-image/scripts/generate.py")
ONLY = "Only the words YOUTUBE and LIBRARY appear, no other text, letters or logos anywhere."
JOBS = {
 "warm": ('A wide course cover graphic. Warm beige grid paper background with faint topographic contour lines in two corners. '
          'On the left, huge heavy bold sans-serif uppercase text "YOUTUBE" in white with a soft drop shadow, and directly below it the word '
          '"LIBRARY" in white inside a solid red rectangle highlight box. On the right, a large red rounded play button in matte 3D clay style, '
          'soft studio light from upper left, soft shadow. Clean, modern, high contrast. ' + ONLY, []),
 "white": ('A wide course cover graphic. Clean white background with a very light grey grid. On the left, huge heavy bold black sans-serif '
           'uppercase text "YOUTUBE" and directly below it "LIBRARY" in black on a bright yellow highlighter box. On the right, a neat fanned '
           'stack of three blank video cards with rounded corners, the front one showing a red play button. A hand-drawn black dashed line '
           'loops from the text to the cards. Flat, modern, high contrast. ' + ONLY, []),
 "shelf": ('A wide course cover graphic in matte 3D clay style. On the right, a small tidy wooden bookshelf where the books are replaced by '
           'rows of colourful video cassettes and tiny screens, each with a red play triangle. On the left, huge heavy bold white uppercase '
           'text "YOUTUBE" and below it "LIBRARY" on a red rectangle box. Warm cream background, soft studio lighting, soft shadows. ' + ONLY, []),
 "face": ('Edit this course cover. Keep the same man, same face, same expression and same pointing pose, the same white grid background '
          'and the same hand-drawn dashed line style. Replace the words with huge heavy bold black uppercase "YOUTUBE" and directly below it '
          '"LIBRARY" in black on a yellow highlight box. Put a large glossy red 3D play button where the dashed line ends. ' + ONLY,
          [str(HERE / "shelf/1.jpg")]),
}

def run(slug):
    prompt, imgs = JOBS[slug]
    cmd = [sys.executable, G, prompt, "--aspect-ratio", "2:1", "--resolution", "2K", "--count", "2", "--slug", f"yt-library-{slug}"]
    for i in imgs: cmd += ["--image", i]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    (HERE / f"kie/{slug}.log").write_text(r.stdout + r.stderr)
    return slug, r.returncode, (r.stdout + r.stderr).strip().splitlines()[-4:]

(HERE / "kie").mkdir(exist_ok=True)
with ThreadPoolExecutor(4) as ex:
    for slug, rc, tail in ex.map(run, JOBS):
        print(slug, rc, *tail, sep="\n  ")
