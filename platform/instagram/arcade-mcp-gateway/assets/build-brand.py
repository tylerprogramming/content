"""Build the Arcade brand lockup: their app icon over their wordmark.

Two assets, two origins, and they are treated differently on purpose.

  arcade-icon-raw.jpeg  their app icon, downloaded. A neon A over a synthwave
                        gradient - the background is a scene, not a flat colour,
                        so it cannot be keyed out without destroying the glow.
                        Used as-is in a rounded tile, which is how the reference
                        style parks a mascot anyway.

  arcade-logo-raw.png   the wordmark, screenshotted from arcade.dev's header
                        with the element scaled 4x in-page. Acid green keyed to
                        transparent so it sits on our near-white ground.

Neither is drawn from memory. An approximated logo is worse than no logo.
"""
from PIL import Image, ImageDraw
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ICON = 168
PAD = 18

icon = Image.open(os.path.join(HERE, "arcade-icon-raw.jpeg")).convert("RGB")
icon = icon.resize((ICON, ICON), Image.LANCZOS)
mask = Image.new("L", (ICON, ICON), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, ICON - 1, ICON - 1], radius=38, fill=255)

word = Image.open(os.path.join(HERE, "arcade-logo.png")).convert("RGBA")
word.thumbnail((250, 86), Image.LANCZOS)

W = max(ICON, word.width)
H = ICON + PAD + word.height
out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
out.paste(icon, ((W - ICON) // 2, 0), mask)
out.paste(word, ((W - word.width) // 2, ICON + PAD), word)
out.save(os.path.join(HERE, "arcade-brand.png"))
print("arcade-brand.png", out.size)
