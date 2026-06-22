#!/usr/bin/env python3
"""Skills vs MCP vs Plugins diagram card (16:9), brand style."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900
BG = (15, 15, 23)
CARD = (26, 26, 46)
ACCENT = (99, 102, 241)
WHITE = (255, 255, 255)
MUTED = (175, 179, 195)

FB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FR = "/System/Library/Fonts/Supplemental/Arial.ttf"
def f(p, s): return ImageFont.truetype(p, s)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
pad = 70

# title
d.rectangle([pad, 56, pad + 70, 64], fill=ACCENT)
d.text((pad, 84), "Skills vs MCP vs Plugins", font=f(FB, 62), fill=WHITE)
d.text((pad, 162), "The three things everyone mixes up", font=f(FR, 30), fill=MUTED)

cards = [
    ("SKILL", "Know-how", "How to do something,\nyour way, over and over."),
    ("MCP", "Access", "Connects Claude to your\nGmail, a database, an API."),
    ("PLUGIN", "The box", "Bundles skills so you\ninstall them in one command."),
]
gap = 40
top = 250
cw = (W - pad * 2 - gap * 2) // 3
ch = H - top - pad

def wrap_draw(x, y, text, fnt, fill, lh):
    for line in text.split("\n"):
        d.text((x, y), line, font=fnt, fill=fill); y += lh
    return y

for i, (tag, label, body) in enumerate(cards):
    x = pad + i * (cw + gap)
    d.rounded_rectangle([x, top, x + cw, top + ch], radius=22, fill=CARD)
    # accent top strip
    d.rounded_rectangle([x, top, x + cw, top + 12], radius=6, fill=ACCENT)
    ix = x + 44
    d.text((ix, top + 50), tag, font=f(FB, 50), fill=ACCENT)
    d.text((ix, top + 120), label, font=f(FB, 38), fill=WHITE)
    wrap_draw(ix, top + 185, body, f(FR, 28), MUTED, 40)

# handle
hf = f(FR, 26)
hd = "@TylerReedAI"
d.text((W - pad - d.textlength(hd, font=hf), H - 50), hd, font=hf, fill=MUTED)

img.save("hero_mon.png")
print("saved hero_mon.png", img.size)
