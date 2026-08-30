#!/usr/bin/env python3
"""Lesson 01 - the first hour. One diagram.

The lesson's real argument is a shape, not a list: nothing much happens for ten
minutes, so people quit at the flat part and never see the turn. Draw the curve,
mark where they quit, mark where it clicks. The three rules ride underneath as a
base rail because they are what keeps you on the curve.

Electric palette from ~/social-studio/themes/electric.json.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / "the-first-hour-electric.png"
W, H = 2560, 1440
S = 2  # supersample, then downsample for clean edges

BG = (0xF7, 0xF8, 0xFA)
INK = (0x0A, 0x0A, 0x0A)
ACCENT = (0x24, 0x54, 0xF0)
MUTED = (0x76, 0x7C, 0x88)
FLAT = (0xA8, 0xAE, 0xBB)
RULE = (0xDF, 0xE2, 0xE9)
HALO = (0xD5, 0xDF, 0xFC)

BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
HELV = "/System/Library/Fonts/HelveticaNeue.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"

_cache = {}


def f(kind, size):
    key = (kind, size)
    if key not in _cache:
        if kind == "head":
            fo = ImageFont.truetype(BLACK, size * S)
        elif kind == "bold":
            fo = ImageFont.truetype(HELV, size * S, index=1)
        elif kind == "mono":
            fo = ImageFont.truetype(MENLO, size * S, index=1)
        else:
            fo = ImageFont.truetype(HELV, size * S, index=0)
        _cache[key] = fo
    return _cache[key]


def text(d, xy, s, kind, size, color, anchor="la", track=0):
    x, y = xy[0] * S, xy[1] * S
    fo = f(kind, size)
    if not track:
        d.text((x, y), s, font=fo, fill=color, anchor=anchor)
        return
    step = track * S
    width = sum(d.textlength(c, font=fo) + step for c in s) - step
    if anchor[0] == "m":
        x -= width / 2
    elif anchor[0] == "r":
        x -= width
    for c in s:
        d.text((x, y), c, font=fo, fill=color, anchor="l" + anchor[1])
        x += d.textlength(c, font=fo) + step


def rect(d, x0, y0, x1, y1, color):
    d.rectangle([x0 * S, y0 * S, x1 * S, y1 * S], fill=color)


def dashed(d, x0, x1, y, color, dash=16, gap=14, width=3):
    x = x0
    while x < x1:
        d.line([(x * S, y * S), (min(x + dash, x1) * S, y * S)], fill=color,
               width=width * S)
        x += dash + gap


def dot(d, cx, cy, r, fill, outline=None, ow=0):
    d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
              fill=fill, outline=outline, width=ow * S)


# --- the curve -------------------------------------------------------------
X0, X1 = 300, 2200          # curve runs left to right
Y_LOW, Y_HIGH = 940, 600    # flat floor, and where it lands
T_TURN = 0.38               # where the flat part ends
AXIS = 1035


def smoothstep(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def curve_y(t):
    return Y_LOW - (Y_LOW - Y_HIGH) * smoothstep((t - T_TURN) / 0.55)


def curve_x(t):
    return X0 + t * (X1 - X0)


def build():
    im = Image.new("RGB", (W * S, H * S), BG)
    d = ImageDraw.Draw(im)

    # --- title block
    text(d, (300, 150), "LESSON 01  ·  WHAT TO EXPECT", "mono", 24, ACCENT,
         track=5)
    rect(d, 300, 208, 372, 214, ACCENT)

    text(d, (300, 262), "The first ", "head", 84, INK)
    w = d.textlength("The first ", font=f("head", 84)) / S
    text(d, (300 + w, 262), "hour.", "head", 84, ACCENT)

    text(d, (300, 412), "Ten minutes in it feels unremarkable. That is the "
                        "flat part, not the whole curve.", "body", 34, MUTED)

    # --- the flat expectation, drawn as the thing you would wrongly assume
    dashed(d, curve_x(T_TURN), X1 + 60, Y_LOW, RULE)
    text(d, (1760, Y_LOW - 40), "STOP HERE AND IT STAYS FLAT", "mono", 19,
         FLAT, anchor="ms", track=3.5)

    # --- axis
    rect(d, X0, AXIS, 2260, AXIS + 2, RULE)

    # --- the curve itself: grey while nothing is happening, blue once it turns
    steps = 900
    pts = [(curve_x(i / steps), curve_y(i / steps)) for i in range(steps + 1)]
    flat = [(x * S, y * S) for x, y in pts if x <= curve_x(T_TURN)]
    rise = [(x * S, y * S) for x, y in pts if x >= curve_x(T_TURN)]
    d.line(flat, fill=FLAT, width=8 * S, joint="curve")
    d.line(rise, fill=ACCENT, width=11 * S, joint="curve")

    # arrowhead: it keeps going
    ax, ay = curve_x(1.0), curve_y(1.0)
    d.polygon([((ax + 34) * S, ay * S), ((ax - 8) * S, (ay - 20) * S),
               ((ax - 8) * S, (ay + 20) * S)], fill=ACCENT)

    # --- the two moments
    t10, t60 = T_TURN, 0.90
    x10, y10 = curve_x(t10), curve_y(t10)
    x60, y60 = curve_x(t60), curve_y(t60)

    for x in (x10, x60):
        dashed(d, 0, 0, 0, BG)  # no-op keeps the helper honest
    for x, top in ((x10, y10), (x60, y60)):
        y = top + 24
        while y < AXIS:
            d.line([(x * S, y * S), (x * S, min(y + 12, AXIS) * S)], fill=RULE,
                   width=3 * S)
            y += 22

    dot(d, x10, y10, 15, BG, FLAT, 6)
    dot(d, x60, y60, 34, HALO)
    dot(d, x60, y60, 18, ACCENT)

    text(d, (x60, y60 - 78), "IT CLICKS", "mono", 22, ACCENT, anchor="ms",
         track=5)

    # --- what happens at each moment, read under the axis
    text(d, (X0, AXIS + 46), "START", "mono", 21, MUTED, track=4)
    text(d, (X0, AXIS + 100), "you open the terminal", "body", 28, MUTED)

    text(d, (x10, AXIS + 46), "MINUTE 10", "mono", 21, MUTED, track=4)
    text(d, (x10, AXIS + 100), "Feels unremarkable.", "bold", 28, INK)
    text(d, (x10, AXIS + 146), "Most people quit here.", "body", 28, MUTED)

    text(d, (2260, AXIS + 46), "HOUR 1", "mono", 21, ACCENT, anchor="rs",
         track=4)
    text(d, (2260, AXIS + 100), "It catches an error you missed", "bold", 28,
         INK, anchor="ra")
    text(d, (2260, AXIS + 146), "and fixes it without being asked.", "body", 28,
         MUTED, anchor="ra")

    # --- the three rules, as the rail that keeps you on the curve
    rect(d, 300, 1268, 2260, 1269, RULE)
    rules = [
        ("01", "Go in order", "the lessons build on each other"),
        ("02", "Use your own project", "not a practice one"),
        ("03", "Actually do it", "watching alone leaves you nothing"),
    ]
    for i, (num, label, sub) in enumerate(rules):
        x = 300 + i * 660
        text(d, (x, 1310), num, "mono", 21, ACCENT, track=3)
        text(d, (x + 62, 1308), label, "bold", 30, INK)
        text(d, (x + 62, 1354), sub, "body", 26, MUTED)

    im.resize((W, H), Image.LANCZOS).save(OUT)
    print(f"saved {OUT}")


if __name__ == "__main__":
    build()
