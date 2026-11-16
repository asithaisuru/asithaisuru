"""Build the original README artwork. Requires Pillow: python -m pip install Pillow.

Run from any directory: python scripts/build_profile_banner.py
The static image also serves visitors who prefer reduced motion.
"""

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
WIDTH, HEIGHT, SCALE = 1200, 360, 2
INK = "#203C55"
TEAL = "#327C75"
CORAL = "#E88968"
GOLD = "#F6C76F"
CREAM = "#FAF7EE"


def font(size, bold=False):
    candidates = (
        Path("C:/Windows/Fonts") / ("segoeuib.ttf" if bold else "segoeui.ttf"),
        Path("/usr/share/fonts/truetype/dejavu")
        / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"),
    )
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size * SCALE)
    raise FileNotFoundError("Install Segoe UI or DejaVu Sans to rebuild the banner.")


def render(phase):
    canvas = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), CREAM)
    draw = ImageDraw.Draw(canvas)

    def box(coords, fill, outline=None, radius=0, width=1):
        scaled = tuple(round(v * SCALE) for v in coords)
        if radius:
            draw.rounded_rectangle(scaled, radius * SCALE, fill, outline, width * SCALE)
        else:
            draw.rectangle(scaled, fill, outline, width * SCALE)

    def line(points, fill, width=1):
        draw.line([(round(x * SCALE), round(y * SCALE)) for x, y in points], fill, width * SCALE)

    def ellipse(coords, fill=None, outline=None, width=1):
        draw.ellipse(tuple(round(v * SCALE) for v in coords), fill, outline, width * SCALE)

    def label(x, y, text, size, fill=INK, bold=False, anchor=None):
        draw.text((x * SCALE, y * SCALE), text, font=font(size, bold), fill=fill, anchor=anchor)

    def star(x, y, radius, fill):
        points = [(x, y - radius), (x + radius * 0.28, y - radius * 0.28),
                  (x + radius, y), (x + radius * 0.28, y + radius * 0.28),
                  (x, y + radius), (x - radius * 0.28, y + radius * 0.28),
                  (x - radius, y), (x - radius * 0.28, y - radius * 0.28)]
        draw.polygon([(round(a * SCALE), round(b * SCALE)) for a, b in points], fill)

    for x in range(0, WIDTH, 32):
        line([(x, 0), (x, HEIGHT)], "#E8EADF")
    for y in range(0, HEIGHT, 32):
        line([(0, y), (WIDTH, y)], "#E8EADF")

    box((0, 0, 7, HEIGHT), CORAL)
    box((45, 31, 359, 64), "#EFF3E9", "#D8E3DA", radius=16)
    ellipse((60, 44, 68, 52), TEAL)
    label(80, 37, "ASITHA ISURU  /  THE BUILDER'S LOG", 12, TEAL, True)
    label(44, 82, "A little curiosity.", 58, INK, True)
    label(44, 151, "A lot of building.", 58, TEAL, True)
    line([(47, 230), (491, 230)], GOLD, 5)
    label(47, 251, "Full-stack development. Computer vision. Real problems.", 18)
    label(47, 306, "BASED IN SRI LANKA", 11, TEAL, True)
    label(311, 305, "ONE IDEA. ONE BRICK. ONE STEP FURTHER.", 11)

    # A small project universe, echoing the portfolio's galaxy and building bricks.
    cx, cy = 943, 173
    ellipse((766, 19, 1120, 337), "#DFEDE2")
    ellipse((806, 49, 1080, 305), "#EBF2E7")
    for step in range(0, 360, 6):
        a = math.radians(step)
        ellipse((cx + 152 * math.cos(a) - 1, cy + 126 * math.sin(a) - 1,
                 cx + 152 * math.cos(a) + 1, cy + 126 * math.sin(a) + 1), "#ADCCC1")

    # Orbiting accents move slowly; all meaningful text stays still.
    for offset, color, radius in ((0, TEAL, 7), (2.1, CORAL, 6), (4.2, GOLD, 5)):
        angle = phase * 2 * math.pi + offset
        px, py = cx + 152 * math.cos(angle), cy + 126 * math.sin(angle)
        ellipse((px - radius, py - radius, px + radius, py + radius), color)

    box((868, 109, 1034, 247), "#BFD5CC", radius=23)
    box((859, 100, 1025, 238), INK, radius=23)
    line([(876, 133), (1008, 133)], "#456074")
    for x, color in ((879, CORAL), (893, GOLD), (907, "#8EC5B4")):
        ellipse((x, 115, x + 6, 121), color)
    label(941, 177, "</>", 56, "#FAF7EE", True, "mm")
    label(942, 216, "BUILD / LEARN / REPEAT", 9, "#BBD8CF", True, "mm")

    # A wireframe crystal nods to the gemstone reconstruction project.
    box((772, 62, 826, 116), "#FFF8E8", "#D1DDD3", radius=13)
    crystal = [(799, 72), (812, 82), (809, 99), (797, 106), (785, 94), (786, 81), (799, 72)]
    line(crystal, TEAL, 2)
    line([(786, 81), (801, 85), (812, 82)], TEAL)
    line([(801, 85), (797, 106)], TEAL)
    line([(799, 72), (801, 85), (785, 94)], TEAL)

    # Offset bricks carry the friendly builder motif.
    box((1067, 238, 1141, 280), "#D87F60", radius=7)
    box((1067, 234, 1141, 268), CORAL, radius=6)
    for x in (1083, 1108):
        ellipse((x, 226, x + 17, 237), "#F1AC8E")
        line([(x, 232), (x, 237)], "#D87F60", 2)
    box((1043, 276, 1117, 314), "#D5A655", radius=6)
    box((1043, 271, 1117, 302), GOLD, radius=6)
    for x in (1057, 1083):
        ellipse((x, 264, x + 17, 275), "#FFDC97")

    star(1118, 76, 10 + 1.5 * math.sin(phase * 2 * math.pi), CORAL)
    star(826, 269, 8, TEAL)
    star(1137, 173, 6, GOLD)
    label(943, 325, "A SMALL UNIVERSE OF IDEAS", 10, TEAL, True, "mm")
    return canvas


def main():
    ASSETS.mkdir(exist_ok=True)
    render(0).save(ASSETS / "profile-banner.png", optimize=True)
    # A shared palette avoids color shimmer. A ten-second orbit keeps motion gentle.
    first = render(0).resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    palette = first.quantize(colors=128)
    frames = []
    for index in range(80):
        frame = render(index / 80).resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
        frames.append(frame.quantize(palette=palette, dither=Image.Dither.NONE))
    frames[0].save(
        ASSETS / "profile-banner.gif", save_all=True, append_images=frames[1:],
        duration=125, loop=0, optimize=True, disposal=1,
    )
    print("Created assets/profile-banner.png and assets/profile-banner.gif")


if __name__ == "__main__":
    main()
