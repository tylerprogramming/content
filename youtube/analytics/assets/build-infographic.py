"""Infographic of the 2026-08-13 CTR pull.

Uses the instagram-writer primitives and the electric theme, so the chart
matches everything else built this week. Numbers come from
data/2026-08-13-tyler-last30-ctr.csv - nothing here is typed by hand twice.
"""
import csv, os, sys
sys.path.insert(0, os.path.expanduser("~/.claude/skills/instagram-writer"))
from PIL import Image, ImageDraw
import instagram_writer as w

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = list(csv.DictReader(open(os.path.join(HERE, "..", "data",
                                             "2026-08-13-tyler-last30-ctr.csv"))))
def secs(d):
    p = d.split(":"); return int(p[0]) * 60 + int(p[1])
LONG = [r for r in ROWS if secs(r["dur"]) > 180]
SHORT = [r for r in ROWS if secs(r["dur"]) <= 180]
def med(v): v = sorted(v); return v[len(v) // 2]

W, H = 1080, 1720
img = Image.new("RGB", (W, H), w.BG)
d = ImageDraw.Draw(img)
w.W, w.H = W, H
w.draw_grid(d)
PAD = w.PAD

# header
w.mono_rail(d, 1, 1, "TYLER AI", "CTR AUDIT")
y = 168
y = w.render_headline_centered(d, ["Nobody is", "clicking."], ["clicking."], y,
                               size=104, kicker="LAST 29 UPLOADS")
y += 8
f_a = w.load_script(38)
sub = "not one reached the channel average"
d.text(((W - w.tw(d, sub, f_a)) // 2, y), sub, font=f_a, fill=w.ACCENT)
y += 74

# the three big numbers
def stat(x, cx_w, label, value, note, big=False):
    f_v = w.load_display(96 if big else 74)
    f_l = w.load_mono(20, bold=True)
    f_n = w.load_font(24)
    d.text((x + (cx_w - w.tw(d, w._space(label), f_l)) // 2, 0 + 0), "", font=f_l)
    lx = x + (cx_w - w.tw(d, w._space(label), f_l)) // 2
    d.text((lx, y), w._space(label), font=f_l, fill=w.GRAY)
    vx = x + (cx_w - w.tw(d, value, f_v)) // 2
    d.text((vx, y + 34), value, font=f_v, fill=w.ACCENT if big else w.BLACK)
    nx = x + (cx_w - w.tw(d, note, f_n)) // 2
    d.text((nx, y + 34 + (104 if big else 84)), note, font=f_n, fill=w.GRAY)

col = (W - PAD * 2) // 3
stat(PAD, col, "channel avg", "4.8%", "365-day CTR")
stat(PAD + col, col, "long-form", f"{med([float(r['ctr']) for r in LONG]):.1f}%", "median of 14", big=True)
stat(PAD + col * 2, col, "shorts", f"{med([float(r['ctr']) for r in SHORT]):.1f}%", "median of 15")
y += 190

# the Opus 5 callout
ch = 168
w.soft_shadow(img, (PAD, y, W - PAD, y + ch), radius=18, blur=12, offset=(0, 7), opacity=44)
d = ImageDraw.Draw(img)
d.rounded_rectangle([PAD, y, W - PAD, y + ch], radius=18, fill=(18, 20, 26))
f_k = w.load_mono(20, bold=True)
d.text((PAD + 28, y + 24), w._space("THE ONE THAT PROVES IT"), font=f_k, fill=(150, 158, 170))
f_big = w.load_display(62)
d.text((PAD + 28, y + 58), "19,334 impressions", font=f_big, fill=(222, 228, 238))
d.text((PAD + 28 + w.tw(d, "19,334 impressions ", f_big), y + 58), "0.9%",
       font=f_big, fill=w.ACCENT_DARK)
f_s = w.load_font(25)
d.text((PAD + 28, y + 126), "Claude Opus 5 Cut My API Bill in Half. Most reach on the channel, worst conversion.",
       font=f_s, fill=(150, 158, 170))
y += ch + 34

# CTR bars, every upload
f_lab = w.load_mono(19, bold=True)
d.text((PAD, y), w._space("EVERY UPLOAD, BY CTR"), font=f_lab, fill=w.GRAY)
y += 34
bar_w = W - PAD * 2
scale = bar_w / 5.0
d.line([(PAD + 4.8 * scale, y - 6), (PAD + 4.8 * scale, y + len(ROWS) * 19 + 6)],
       fill=w.ACCENT, width=2)
f_t = w.load_font(15)
for r in sorted(ROWS, key=lambda r: float(r["ctr"])):
    c = float(r["ctr"])
    bw = max(2, c * scale)
    is_long = secs(r["dur"]) > 180
    col_bar = w.ACCENT if is_long else tuple(int(x * 0.45 + 255 * 0.55) for x in w.ACCENT)
    d.rounded_rectangle([PAD, y, PAD + bw, y + 12], radius=3, fill=col_bar)
    # Label goes inside the bar once the bar is long enough to hold it, so a
    # 4.7% bar does not push its own caption off the canvas.
    txt = f"{c:.1f}%  {r['title'][:40]}"
    tw_ = w.tw(d, txt, f_t)
    if PAD + bw + 10 + tw_ < W - PAD:
        d.text((PAD + bw + 10, y - 2), txt, font=f_t, fill=w.GRAY)
    else:
        d.text((PAD + 10, y - 2), txt, font=f_t, fill=w.BG)
    y += 19
y += 16
f_key = w.load_font(20)
d.rounded_rectangle([PAD, y + 4, PAD + 26, y + 16], radius=3, fill=w.ACCENT)
d.text((PAD + 36, y), "long-form", font=f_key, fill=w.GRAY)
d.rounded_rectangle([PAD + 170, y + 4, PAD + 196, y + 16], radius=3,
                    fill=tuple(int(x * 0.45 + 255 * 0.55) for x in w.ACCENT))
d.text((PAD + 206, y), "shorts", font=f_key, fill=w.GRAY)
d.text((W - PAD - w.tw(d, "channel average 4.8%", f_key), y), "channel average 4.8%",
       font=f_key, fill=w.ACCENT)

w.footer_rail(d, "@tylerreedai", ["IMPRESSIONS", "CTR", "VIEWS", "SUBS"], 1, 1, 1)
out = os.path.join(HERE, "2026-08-13-ctr-infographic.png")
img.save(out)
print("wrote", out, img.size)
