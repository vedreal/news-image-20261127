#!/usr/bin/env python3
"""Draw entry.png for make.fun bounty news-image-20261127.

One image summing up the world news of Friday 27 November 2026.
All drawing is done with PIL so every word renders exactly.
Stories (all first reported / announced on 27 Nov 2026):
  1. New Zealand final election count: hung parliament, 65-65.
     Sources: Reuters, AP, Elections NZ, 27 Nov 2026.
  2. Thanksgiving storm on the US East Coast: 900,000+ without power,
     400+ flights cancelled. Sources: Reuters, ANI/CNN, 27 Nov 2026.
  3. EU budget talks stall; 24 states back a 45bn euro Ukraine loan.
     Source: European Council President Costa's remarks, 27 Nov 2026.
  4. Trump says Putin "would like to make a deal" to end the war in
     Ukraine. Source: ANI / Global Journal, 27 Nov 2026.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
CREAM = (255, 246, 227)
NAVY = (27, 42, 74)
RED = (192, 57, 43)
GOLD = (212, 175, 55)
WHITE = (255, 255, 255)
INK = (40, 40, 40)
GREY = (90, 90, 90)
LIGHT_BLUE = (120, 170, 220)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONTB if bold else FONT, size)


def center(draw, y, text, fnt, fill, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)


def draw_ballot(d, cx, cy):
    """Ballot box with a checked ballot slip (New Zealand vote)."""
    # ballot slip
    d.rounded_rectangle([cx - 52, cy - 78, cx + 52, cy - 8], radius=6,
                        fill=WHITE, outline=NAVY, width=4)
    # red check mark
    d.line([(cx - 34, cy - 46), (cx - 12, cy - 24), (cx + 36, cy - 66)],
           fill=RED, width=9, joint="curve")
    # box
    d.rounded_rectangle([cx - 78, cy - 6, cx + 78, cy + 78], radius=10,
                        fill=NAVY, outline=NAVY)
    d.rectangle([cx - 78, cy - 6, cx + 78, cy + 14], fill=(52, 72, 110))
    d.rectangle([cx - 22, cy - 6, cx + 22, cy + 2], fill=CREAM)
    # stars on box
    for sx in (cx - 52, cx, cx + 52):
        d.ellipse([sx - 5, cy + 42, sx + 5, cy + 52], fill=GOLD)


def draw_storm(d, cx, cy):
    """Storm cloud, lightning bolt and rain (US Thanksgiving storm)."""
    # cloud: overlapping circles
    for ox, oy, r in [(-58, 6, 42), (-18, -18, 52), (28, -6, 46), (58, 14, 36)]:
        d.ellipse([cx + ox - r, cy + oy - r, cx + ox + r, cy + oy + r],
                  fill=(70, 80, 100))
    d.rectangle([cx - 96, cy - 6, cx + 92, cy + 34], fill=(70, 80, 100))
    # lightning bolt
    bolt = [(cx + 6, cy + 18), (cx - 22, cy + 78), (cx - 2, cy + 78),
            (cx - 14, cy + 118), (cx + 30, cy + 44), (cx + 8, cy + 44)]
    d.polygon(bolt, fill=GOLD, outline=(180, 140, 20))
    # rain
    for rx in (-84, -52, 66, 92):
        d.line([(cx + rx, cy + 52), (cx + rx - 10, cy + 92)],
               fill=LIGHT_BLUE, width=7)


def draw_eu_stars(d, cx, cy):
    """Circle of 12 gold stars on a navy disc (EU summit)."""
    import math
    d.ellipse([cx - 88, cy - 88, cx + 88, cy + 88], fill=NAVY)
    for i in range(12):
        a = math.radians(i * 30 - 90)
        sx, sy = cx + 62 * math.cos(a), cy + 62 * math.sin(a)
        r = 11
        pts = []
        for k in range(10):
            ang = math.radians(k * 36 - 90)
            rr = r if k % 2 == 0 else r * 0.45
            pts.append((sx + rr * math.cos(ang), sy + rr * math.sin(ang)))
        d.polygon(pts, fill=GOLD)


def draw_mic(d, cx, cy):
    """Microphone on a stand (Trump statement)."""
    # mic head
    d.ellipse([cx - 46, cy - 82, cx + 46, cy + 10], fill=NAVY)
    for gy in (-58, -38, -18):
        d.line([(cx - 40, cy + gy), (cx + 40, cy + gy)], fill=WHITE, width=5)
    d.line([(cx, cy - 78), (cx, cy + 6)], fill=WHITE, width=5)
    # stand
    d.line([(cx, cy + 10), (cx, cy + 78)], fill=NAVY, width=10)
    d.line([(cx - 48, cy + 84), (cx + 48, cy + 84)], fill=NAVY, width=10)
    d.ellipse([cx - 58, cy + 74, cx - 38, cy + 94], fill=RED)
    d.ellipse([cx + 38, cy + 74, cx + 58, cy + 94], fill=RED)


def card(d, x, y, w, h, icon_fn, lines, sub):
    d.rounded_rectangle([x, y, x + w, y + h], radius=18,
                        fill=WHITE, outline=NAVY, width=4)
    # red top strip
    d.rounded_rectangle([x, y, x + w, y + 14], radius=7, fill=RED)
    d.rectangle([x, y + 7, x + w, y + 14], fill=RED)
    icon_fn(d, x + w // 2, y + 108)
    ly = y + 216
    for line in lines:
        center(d, ly, line, font(40, bold=True), NAVY, x, x + w)
        ly += 48
    center(d, y + h - 48, sub, font(27), GREY, x, x + w)


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # ---- date banner ----
    d.rectangle([0, 0, W, 168], fill=NAVY)
    d.rectangle([0, 168, W, 178], fill=RED)
    center(d, 26, "27 NOVEMBER 2026", font(82, bold=True), WHITE)
    center(d, 122, "F R I D A Y  •  T H E  W O R L D  I N  O N E  D A Y",
           font(26, bold=True), GOLD)

    # ---- 2 x 2 story grid ----
    m, gap = 28, 24
    cw = (W - 2 * m - gap) // 2
    ch = 356
    y0 = 200
    card(d, m, y0, cw, ch, draw_ballot,
         ["NEW ZEALAND", "HUNG PARLIAMENT"],
         "Final count: 65–65, no majority")
    card(d, m + cw + gap, y0, cw, ch, draw_storm,
         ["THANKSGIVING", "STORM"],
         "900,000+ lose power in the US")
    card(d, m, y0 + ch + gap, cw, ch, draw_eu_stars,
         ["EU BUDGET", "TALKS STALL"],
         "24 back €45bn Ukraine loan")
    card(d, m + cw + gap, y0 + ch + gap, cw, ch, draw_mic,
         ["TRUMP: PUTIN", "WANTS A DEAL"],
         "Push to end the Ukraine war")

    # ---- footer ----
    center(d, 952, "Sources: Reuters • AP • European Council • ANI — 27 Nov 2026",
           font(23), GREY)
    center(d, 984, "All four stories first reported on 27 November 2026",
           font(23), GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print(out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
