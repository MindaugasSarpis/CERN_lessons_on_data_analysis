#!/usr/bin/env python3
"""Put the QA screenshots of one deck on contact sheets, four slides per PNG.

Reading 100 screenshots one by one is slow; a sheet of four, each at half
size, is enough to judge layout, crowding and overflow at a glance.

Usage:
    python3 scripts/contact-sheets.py 07-data-visualisation
    python3 scripts/contact-sheets.py 07-data-visualisation --from 60 --to 76

Reads .qa-shots/<slug>/slide-NNN.png (made by `pnpm qa:shots`) and writes
.qa-shots/<slug>/sheets/sheet-NNN-MMM.png. Needs Pillow (in the `figures`
and `outreach_talks` environments).
"""
import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
TILE = (640, 360)          # half of the 1280x720 screenshots
PER_SHEET = 4              # a 2 x 2 grid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--from", dest="first", type=int, default=1)
    ap.add_argument("--to", dest="last", type=int, default=10_000)
    args = ap.parse_args()

    shots = ROOT / ".qa-shots" / args.slug
    numbered = []
    for png in sorted(shots.glob("slide-*.png")):
        n = int(re.search(r"(\d+)", png.stem).group(1))
        if args.first <= n <= args.last:
            numbered.append((n, png))
    if not numbered:
        raise SystemExit(f"no screenshots in {shots} for slides {args.first}-{args.last}")

    out = shots / "sheets"
    out.mkdir(exist_ok=True)
    for start in range(0, len(numbered), PER_SHEET):
        group = numbered[start:start + PER_SHEET]
        sheet = Image.new("RGB", (TILE[0] * 2, TILE[1] * 2), "black")
        draw = ImageDraw.Draw(sheet)
        for i, (n, png) in enumerate(group):
            x, y = (i % 2) * TILE[0], (i // 2) * TILE[1]
            sheet.paste(Image.open(png).convert("RGB").resize(TILE), (x, y))
            draw.text((x + 8, y + TILE[1] - 18), f"slide {n}", fill="white")
        name = out / f"sheet-{group[0][0]:03d}-{group[-1][0]:03d}.png"
        sheet.save(name)
        print(name.relative_to(ROOT))


if __name__ == "__main__":
    main()
