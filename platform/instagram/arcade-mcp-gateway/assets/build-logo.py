"""Key the acid green out of the captured Arcade wordmark.

Their site puts a black serif wordmark on #C4F82A. Screenshotting it gives a
green block, which cannot sit on our near-white ground. This keys the green to
transparent and keeps the ink, alpha'd by darkness so the serifs stay smooth.

Source capture: arcade-logo-raw.png, taken from arcade.dev's own header with
the element scaled 4x in-page so the mark is sharp rather than upscaled.
"""
from PIL import Image
import os

HERE = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(HERE, "arcade-logo-raw.png")).convert("RGB")
W, H = im.size
px = im.load()
out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
op = out.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        green = g > 150 and b < 140 and g > b + 55 and g > r + 10
        white = r > 235 and g > 235 and b > 235
        if green or white:
            continue
        dark = 255 - min(r, g, b)
        op[x, y] = (10, 10, 10, min(255, int(dark * 1.3)))
# Crop to the wordmark. The capture also caught "PROD" from the nav and two of
# the site's decorative grid lines.
out = out.crop((0, 0, int(W * 0.77), int(H * 0.85)))

# Despeckle: the grid lines are one pixel wide, the wordmark is not. Drop any
# opaque pixel with fewer than three opaque neighbours and the lines vanish
# while the serifs survive.
src = out.load()
w2, h2 = out.size
doomed = []
for y in range(1, h2 - 1):
    for x in range(1, w2 - 1):
        if src[x, y][3] < 40:
            continue
        n = sum(1 for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                if (dx or dy) and src[x + dx, y + dy][3] > 90)
        if n < 3:
            doomed.append((x, y))
for x, y in doomed:
    src[x, y] = (0, 0, 0, 0)

out = out.crop(out.getbbox())
out.thumbnail((640, 640), Image.LANCZOS)
out.save(os.path.join(HERE, "arcade-logo.png"))
print("arcade-logo.png", out.size)
