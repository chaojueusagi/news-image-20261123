"""Pure PIL flat newspaper front page for make.fun news-image-20261123.

No AI-generated pixels: every shape is drawn with PIL rectangles, circles,
polygons and lines; all text uses system DejaVu fonts. Deterministic:
no randomness, no network, no current time. Output is exactly 1024x1024.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 36
CONTENT_W = W - 2 * MARGIN

PAPER = (244, 241, 234)      # cold off-white
PANEL = (236, 232, 219)      # slightly darker panel
INK = (20, 20, 20)           # near-black
RED = (192, 57, 43)          # single red accent
GREY = (90, 88, 80)          # secondary text
GLOBE = (58, 124, 165)       # flat blue globe
GLOBE_DARK = (38, 96, 135)   # darker blue for land shapes
CHAIR = (52, 52, 52)         # chair silhouettes

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_BOLD = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS_BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def text_w(draw, text, f):
    return draw.textbbox((0, 0), text, font=f)[2]


def fit_font(draw, text, max_w, start, minimum, bold=True):
    """Largest bold-sans size <= start that fits max_w."""
    size = start
    while size > minimum and text_w(draw, text, SANS_BOLD(size)) > max_w:
        size -= 1
    return SANS_BOLD(size)


def centered(draw, y, text, f, fill=INK, x0=MARGIN, x1=W - MARGIN):
    w = text_w(draw, text, f)
    draw.text(((x0 + x1 - w) / 2, y), text, font=f, fill=fill)
    return y + f.size


def draw_chair(draw, x, y, s, color=CHAIR):
    """Simple flat chair silhouette: backrest, seat, two legs."""
    bw, bh = int(34 * s), int(42 * s)   # backrest w/h
    sw, sh = int(38 * s), int(8 * s)    # seat w/h
    draw.rectangle([x, y, x + bw, y + bh], fill=color)
    draw.rectangle([x - 2 * s, y + bh, x + bw + 2 * s, y + bh + sh], fill=color)
    draw.rectangle([x + 2 * s, y + bh + sh, x + 8 * s, y + bh + sh + 26 * s], fill=color)
    draw.rectangle([x + bw - 8 * s, y + bh + sh, x + bw - 2 * s, y + bh + sh + 26 * s], fill=color)


def draw_icon(draw, x, y, size, kind, color):
    """Small flat geometric icon inside a coloured square."""
    draw.rectangle([x, y, x + size, y + size], fill=color)
    cx, cy = x + size // 2, y + size // 2
    if kind == "globe":
        r = size // 3
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=3)
        draw.line([(cx - r + 4, cy - 4), (cx - 2, cy + 2), (cx + 3, cy - 3),
                   (cx + r - 4, cy + 5)], fill=(255, 255, 255), width=3)
    elif kind == "dome":  # capitol dome
        draw.rectangle([x + 12, cy + 4, x + size - 12, cy + 14], fill=(255, 255, 255))
        draw.polygon([(cx - 12, cy + 4), (cx + 12, cy + 4), (cx, cy - 14)], fill=(255, 255, 255))
        draw.rectangle([cx - 2, cy - 20, cx + 2, cy - 14], fill=(255, 255, 255))
    elif kind == "tanker":
        draw.rectangle([x + 10, cy - 2, x + size - 10, cy + 10], fill=(255, 255, 255))
        draw.rectangle([x + size - 26, cy - 12, x + size - 16, cy - 2], fill=(255, 255, 255))
        draw.line([(x + 10, cy + 16), (x + 20, cy + 16), (x + 26, cy + 20),
                   (x + 36, cy + 20), (x + 44, cy + 16), (x + size - 10, cy + 16)],
                  fill=(255, 255, 255), width=2)
    elif kind == "factory":
        draw.rectangle([x + 12, cy - 2, x + size - 12, cy + 14], fill=(255, 255, 255))
        draw.polygon([(x + 12, cy - 2), (x + 22, cy - 12), (x + 32, cy - 2),
                      (x + 42, cy - 12), (x + size - 12, cy - 2)], fill=(255, 255, 255))
        draw.rectangle([x + size - 22, cy - 20, x + size - 16, cy - 2], fill=(255, 255, 255))
    elif kind == "document":
        draw.rectangle([x + 16, cy - 16, x + size - 16, cy + 16], fill=(255, 255, 255))
        for i, yy in enumerate((cy - 8, cy, cy + 8)):
            draw.line([(x + 21, yy), (x + size - 21, yy)], fill=color, width=2)
        draw.line([(x + 21, cy - 14), (x + 30, cy - 14)], fill=RED, width=3)


STORIES = [
    ("COP31 ENDS WITHOUT A DEAL",
     "Climate talks close with no agreement reached",
     (46, 125, 50), "globe"),
    ("DEMOCRATS WIN THE HOUSE",
     "Party gains majority in House elections",
     (21, 101, 192), "dome"),
    ("TANKERS HIT IN HORMUZ",
     "Two vessels struck near Strait of Hormuz",
     (230, 81, 0), "tanker"),
    ("FACTORY FIRE IN INDONESIA",
     "Large blaze at industrial site in Java",
     (183, 28, 28), "factory"),
    ("SEOUL MINISTER QUITS OVER AI CHEATING",
     "Resigns amid academic fraud allegations",
     (106, 27, 154), "document"),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    y = 26
    y = centered(d, y, "THE WORLD TODAY", SERIF_BOLD(62)) + 6
    y = centered(d, y, "Monday, 23 November 2026", SANS(22), fill=GREY) + 10
    d.rectangle([MARGIN, y, W - MARGIN, y + 5], fill=RED)
    y += 18
    y = centered(d, y, "O N E   D A Y ,   O N E   W O R L D", SANS_BOLD(26)) + 8

    # --- central panel: cracked globe over empty chairs ---
    panel_top, panel_bottom = y + 4, 470
    d.rectangle([MARGIN, panel_top, W - MARGIN, panel_bottom], fill=PANEL,
                outline=INK, width=2)
    # globe
    gc = (512, 300)
    r = 78
    d.ellipse([gc[0] - r, gc[1] - r, gc[0] + r, gc[1] + r], fill=GLOBE)
    d.polygon([(gc[0] - 58, gc[1] - 20), (gc[0] - 18, gc[1] - 38),
               (gc[0] - 8, gc[1] - 8), (gc[0] - 48, gc[1] + 6)], fill=GLOBE_DARK)
    d.polygon([(gc[0] + 12, gc[1] + 22), (gc[0] + 52, gc[1] + 10),
               (gc[0] + 58, gc[1] + 42), (gc[0] + 22, gc[1] + 52)], fill=GLOBE_DARK)
    # jagged cracks (white, then one black)
    d.line([(gc[0] - 42, gc[1] - 62), (gc[0] - 18, gc[1] - 30),
            (gc[0] - 34, gc[1] + 2), (gc[0] - 6, gc[1] + 28),
            (gc[0] - 22, gc[1] + 60)], fill=(255, 255, 255), width=4)
    d.line([(gc[0] + 8, gc[1] - 70), (gc[0] + 26, gc[1] - 38),
            (gc[0] + 10, gc[1] - 8), (gc[0] + 34, gc[1] + 22)], fill=(255, 255, 255), width=4)
    d.line([(gc[0] - 34, gc[1] + 2), (gc[0] - 58, gc[1] + 18)], fill=(255, 255, 255), width=3)
    d.line([(gc[0] + 52, gc[1] - 52), (gc[0] + 70, gc[1] - 30)], fill=INK, width=3)
    # stage line + row of 5 empty chairs
    d.line([MARGIN + 60, 452, W - MARGIN - 60, 452], fill=INK, width=3)
    chair_xs = [150, 300, 450, 600, 750]
    for cx in chair_xs:
        draw_chair(d, cx, 372, 1.0)
    d.text((MARGIN + 14, panel_top + 8), "COP31  •  ANTALYA",
           font=SANS_BOLD(16), fill=GREY)

    # --- timeline of 5 stories ---
    y = 492
    block_h = 96
    line_x = 58
    for i, (headline, expl, color, kind) in enumerate(STORIES):
        top = y + i * block_h
        # vertical timeline line + colour dot
        d.line([line_x, top + 8, line_x, top + block_h - 8], fill=INK, width=2)
        d.ellipse([line_x - 9, top + 34, line_x + 9, top + 52], fill=color,
                  outline=INK, width=2)
        # icon square
        draw_icon(d, 88, top + 14, 64, kind, color)
        # headline, auto-fit
        tx = 172
        max_w = W - MARGIN - tx
        hf = fit_font(d, headline, max_w, 30, 22)
        d.text((tx, top + 12), headline, font=hf, fill=INK)
        # one-line explanation
        d.text((tx, top + 52), expl, font=SANS(20), fill=GREY)
        # thin divider except after last block
        if i < len(STORIES) - 1:
            d.line([tx, top + block_h - 6, W - MARGIN, top + block_h - 6],
                   fill=(200, 196, 186), width=1)

    # --- footer ---
    fy = y + 5 * block_h + 4
    d.rectangle([MARGIN, fy, W - MARGIN, fy + 2], fill=INK)
    centered(d, fy + 8, "FIVE STORIES  •  ONE DAY  •  ONE WORLD", SANS_BOLD(14), fill=GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print("saved", out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
