#!/usr/bin/env python3
"""Build a branded social image: a real video screenshot under a header bar with the hook.
Usage: python3 build_card.py <frame.jpg> "<headline>" <out.png> [ratio: 16x9|1x1|4x5]
Reusable for the whole Claude Code Skills drip.
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

FRAME, HEAD, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
RATIO = sys.argv[4] if len(sys.argv) > 4 else "16x9"

SIZES = {"16x9": (1600, 900), "1x1": (1200, 1200), "4x5": (1080, 1350)}
W, H = SIZES[RATIO]

BG = (15, 15, 23)        # near-black
BAR = (26, 26, 46)       # brand dark #1a1a2e
ACCENT = (99, 102, 241)  # brand purple #6366f1
WHITE = (255, 255, 255)
MUTED = (170, 174, 190)

FB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FR = "/System/Library/Fonts/Supplemental/Arial.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

pad = int(W * 0.05)
# --- header text ---
hsize = 64 if RATIO != "4x5" else 58
fnt = font(FB, hsize)
max_w = W - pad * 2
lines = wrap(d, HEAD, fnt, max_w)
line_h = int(hsize * 1.18)
header_h = pad + len(lines) * line_h + int(pad * 0.5)

# accent tab
d.rectangle([pad, int(pad*0.7), pad + 70, int(pad*0.7) + 8], fill=ACCENT)
y = int(pad * 0.7) + 26
for ln in lines:
    d.text((pad, y), ln, font=fnt, fill=WHITE); y += line_h

# --- screenshot panel ---
shot = Image.open(FRAME).convert("RGB")
panel_w = W - pad * 2
panel_top = header_h
panel_h = H - panel_top - pad
# fit screenshot preserving aspect, then center-crop to panel box
shot = ImageOps.fit(shot, (panel_w, panel_h), method=Image.LANCZOS, centering=(0.5, 0.4))
# rounded corners + thin border
radius = 18
mask = Image.new("L", shot.size, 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, shot.size[0], shot.size[1]], radius=radius, fill=255)
# subtle border frame
border = Image.new("RGB", (shot.size[0] + 4, shot.size[1] + 4), (60, 62, 84))
bmask = Image.new("L", border.size, 0)
ImageDraw.Draw(bmask).rounded_rectangle([0, 0, border.size[0], border.size[1]], radius=radius+2, fill=255)
img.paste(border, (pad - 2, panel_top - 2), bmask)
img.paste(shot, (pad, panel_top), mask)

# --- handle bottom-right ---
hf = font(FR, 26)
handle = "@TylerReedAI"
tw = d.textlength(handle, font=hf)
d.text((W - pad - tw, H - int(pad*0.62)), handle, font=hf, fill=MUTED)

img.save(OUT)
print("saved", OUT, img.size)
