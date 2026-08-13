import sys
sys.path.insert(0, "/Users/tylerreed/.claude/skills/instagram-writer")
from PIL import Image, ImageDraw
import instagram_writer as w

# Lines sized to fill the card left to right. The first pass wrapped at about
# 23 characters inside a 520px card, which left a dead column down the right
# and made the block look like a narrow note rather than a file.
LINES = [
    ("---",                             "dim"),
    ("name:", "key", " skool-post"),
    ("description:", "key", " Draft a"),
    ("  ready-to-paste Skool post",     "val"),
    ("  from a video package.",         "val"),
    ("---",                             "dim"),
    ("",                                "dim"),
    ("Read the package. Pull the",      "txt"),
    ("hook and the one takeaway.",      "txt"),
    ("Write it in plain language.",     "txt"),
]

PAD_X, TOP, BOT, LH = 26, 62, 34, 33
f = w.load_mono(24)
probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))

widest = 0
for row in LINES:
    t = row[0] + (row[2] if len(row) > 2 else "")
    widest = max(widest, probe.textbbox((0, 0), t, font=f)[2])

CW = widest + PAD_X * 2
CH = TOP + LH * len(LINES) + BOT          # real bottom padding, not a guess
img = Image.new("RGB", (CW, CH), (18, 20, 26))
d = ImageDraw.Draw(img)
for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
    d.ellipse([22 + i * 26, 20, 34 + i * 26, 32], fill=c)
d.text((116, 17), w._space("SKILL.MD"), font=w.load_mono(19, bold=True), fill=(150, 158, 170))

COL = {"dim": (108, 116, 130), "key": w.ACCENT_DARK, "val": (222, 228, 238),
       "txt": (196, 202, 212)}
y = TOP
for row in LINES:
    d.text((PAD_X, y), row[0], font=f, fill=COL[row[1]])
    if len(row) > 2:
        d.text((PAD_X + d.textbbox((0, 0), row[0], font=f)[2], y), row[2],
               font=f, fill=COL["val"])
    y += LH
img.save("/Users/tylerreed/content/platform/instagram/first-claude-skill/assets/hero-skillmd.png")
print(f"hero {CW}x{CH}  (text fills to {widest}px, bottom pad {BOT}px)")
