#!/usr/bin/env python3
"""Reference thumbnail mockups, drawn not generated.

These are layout references for the editor, not finished art. The point is that
the geometry is exact and checkable: word count, type size as a fraction of the
frame, split position, contrast. An AI image generator cannot hold any of those
steady, and costs money per attempt.

Every render is also emitted at 210px wide - the size a thumbnail actually
occupies in a YouTube feed. If a word is unreadable in the small version, the
design is wrong regardless of how it looks at full size.

    python3 build-thumb-refs.py            # writes ../reference/
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
OUT = Path(__file__).resolve().parent.parent / "reference"

INK = (10, 10, 12)
PAPER = (247, 248, 250)
ACCENT = (36, 84, 240)      # electric blue, matches the brand
HOT = (255, 196, 0)         # yellow, IndyDevDan's accent
RED = (222, 48, 48)
GREEN = (32, 176, 92)
DIM = (128, 132, 140)

# SFNSDisplay.ttf does NOT exist on macOS 15+ - naming it silently falls through
# to Helvetica at regular weight, which is how the first pass of these renders
# came out thin. SFNS.ttf is the real file and carries a "Black" variation.
FACES = [
    "/System/Library/Fonts/SFNS.ttf",
    "/System/Library/Fonts/Supplemental/Arial Black.ttf",
    "/System/Library/Fonts/Supplemental/Impact.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]
MONO = "/System/Library/Fonts/Menlo.ttc"


def font(size, mono=False):
    if mono:
        try:
            return ImageFont.truetype(MONO, size)
        except OSError:
            pass
    for f in FACES:
        try:
            fo = ImageFont.truetype(f, size)
        except OSError:
            continue
        try:
            fo.set_variation_by_name("Black")
        except Exception:
            pass  # static face, already heavy
        return fo
    raise RuntimeError("no display face found - renders would be silently thin")


def fit(draw, text, target_w, mono=False, cap=460):
    """Largest size at which `text` is <= target_w wide. Measured with textbbox,
    which is the drawn extent - the glyph box lies about heavy display faces."""
    lo, hi = 10, cap
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if draw.textbbox((0, 0), text, font=font(mid, mono))[2] <= target_w:
            lo = mid
        else:
            hi = mid - 1
    return font(lo, mono)


def centered(draw, text, cx, cy, fo, fill):
    b = draw.textbbox((0, 0), text, font=fo)
    draw.text((cx - (b[2] - b[0]) / 2 - b[0], cy - (b[3] - b[1]) / 2 - b[1]),
              text, font=fo, fill=fill)
    return b


def arrow(draw, x, y, size, fill):
    draw.line([(x - size, y), (x + size * 0.35, y)], fill=fill, width=max(6, size // 5))
    draw.polygon([(x + size, y), (x + size * 0.25, y - size * 0.55),
                  (x + size * 0.25, y + size * 0.55)], fill=fill)


def terminal(draw, box, lines, title, ok):
    """A small fake terminal. `ok` tints the chrome so the two panels read as
    before and after without needing a caption."""
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, 14, fill=(18, 18, 22))
    draw.rounded_rectangle((x0, y0, x1, y0 + 34), 14, fill=(38, 38, 46))
    draw.rectangle((x0, y0 + 20, x1, y0 + 34), fill=(38, 38, 46))
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        draw.ellipse((x0 + 14 + i * 20, y0 + 11, x0 + 26 + i * 20, y0 + 23), fill=c)
    f = font(21, mono=True)
    draw.text((x0 + 52, y0 + 8), title, font=f, fill=(150, 152, 160))
    for i, (t, role) in enumerate(lines):
        col = {"dim": (120, 122, 130), "ok": GREEN, "no": RED}.get(role, (228, 230, 236))
        draw.text((x0 + 20, y0 + 54 + i * 30), t, font=f, fill=col)


def split(left_label, right_label, left_lines, right_lines,
          left_title, right_title, accent_r=GREEN, accent_l=RED, dark=False):
    """The before/after split. Six of eighteen top competitor thumbnails are
    this shape; zero of ours are."""
    bg = INK if dark else PAPER
    fg = PAPER if dark else INK
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    mid = W // 2

    # words sized against the half-frame, which is what makes them huge
    fl = fit(d, left_label, mid - 90)
    fr = fit(d, right_label, mid - 90)
    size = min(fl.size, fr.size)
    fl = fr = font(size)

    centered(d, left_label, mid // 2, 118, fl, accent_l)
    centered(d, right_label, mid + mid // 2, 118, fr, accent_r)

    terminal(d, (46, 250, mid - 52, H - 150), left_lines, left_title, False)
    terminal(d, (mid + 52, 250, W - 46, H - 150), right_lines, right_title, True)

    d.rectangle((mid - 3, 232, mid + 3, H - 134), fill=fg if not dark else (66, 66, 74))
    arrow(d, mid, 118, 46, fg)
    return im


def hero_face(word, chips, dark=True):
    """Chase's OPUS 5 composition: huge type across the left two thirds, face
    reserved in the right third. Used where trust matters (a course)."""
    bg = INK if dark else PAPER
    fg = PAPER if dark else INK
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    col = int(W * 0.66)

    fo = fit(d, word, col - 60)
    centered(d, word, col // 2, 270, fo, HOT if dark else ACCENT)

    # one row of app marks - the single supporting object
    n = len(chips)
    cw, gap = 108, 20
    total = n * cw + (n - 1) * gap
    x = col // 2 - total // 2
    for label in chips:
        d.rounded_rectangle((x, 500, x + cw, 500 + cw), 24,
                            fill=(30, 30, 38) if dark else (232, 234, 240))
        cf = fit(d, label, cw - 26, cap=44)
        centered(d, label, x + cw // 2, 500 + cw // 2, cf, fg)
        x += cw + gap

    # face placeholder - the brief says large and reacting, not medium and neutral
    d.rectangle((col, 0, W, H), fill=(30, 30, 38) if dark else (226, 228, 234))
    pf = font(30)
    for i, line in enumerate(["FACE", "right third", "large +", "reacting"]):
        centered(d, line, col + (W - col) // 2, 280 + i * 42, pf, DIM)
    return im


def contact(im):
    """What it actually looks like in a feed, on the page next to the full size."""
    small = im.resize((210, 118))
    sheet = Image.new("RGB", (W, H + 150), (24, 24, 28))
    sheet.paste(im, (0, 0))
    sheet.paste(small, (30, H + 16))
    d = ImageDraw.Draw(sheet)
    d.text((260, H + 20), "^ actual feed size (210px).", font=font(26), fill=(240, 240, 245))
    d.text((260, H + 56), "If a word is unreadable here, the design is wrong",
           font=font(22), fill=(170, 172, 180))
    d.text((260, H + 84), "no matter how it reads at full size.",
           font=font(22), fill=(170, 172, 180))
    return sheet


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    made = []

    refuse = [("> read my email", "dim"), ("I can't access", "no"),
              ("your Gmail.", "no"), ("", "dim")]
    works = [("> read my email", "dim"), ("3 unread from", "ok"),
             ("Sarah, Mike, AWS", "ok"), ("drafting replies_", "ok")]

    made.append(("045-talks-does",
                 split("TALKS", "DOES", refuse, works,
                       "claude code", "claude code + arcade")))
    made.append(("045-cant-can",
                 split("CAN'T", "CAN", refuse, works,
                       "claude code", "claude code + arcade", dark=True)))
    made.append(("047-any-app-face",
                 hero_face("ANY APP", ["Gmail", "Slack", "Cal", "Notion"])))
    made.append(("047-any-app-nofa",
                 hero_face("ANY APP", ["Gmail", "Slack", "Cal", "Notion", "Drive"],
                           dark=False)))

    for name, im in made:
        im.save(OUT / f"{name}.png")
        contact(im).save(OUT / f"{name}-feedcheck.png")
        print("wrote", name)


if __name__ == "__main__":
    main()
