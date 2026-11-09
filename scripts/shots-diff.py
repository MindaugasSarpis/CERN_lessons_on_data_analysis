#!/usr/bin/env python3
"""Which QA screenshots changed between two runs, with side-by-side PNGs.

Compares every slide-NNN.png of NEW_DIR with the slide of the same number in
OLD_DIR and reports, per slide, the share of pixels that differ.

    python3 scripts/shots-diff.py OLD_DIR NEW_DIR [--threshold 0.001]
            [--out DIR] [--from N] [--to M] [--json]

A slide is changed when more than --threshold of its pixels differ (default
0.001 = 0.1 %). A new slide that matches an old slide of another number is
moved (a slide was added or taken out before it), not changed; a slide put in
is added; an old slide that matches no new slide is removed. For each changed,
added or removed slide, OUT/slide-NNN.png (default NEW_DIR/diff/, emptied
first) shows the old slide on the left and the new one on the right, with the
area that differs boxed in red.

Exit status as diff(1): 0 nothing changed, 1 something changed, 2 error.
Needs Pillow only. `pnpm review <deck> --since ...` runs it for you.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageStat

THUMB = (64, 36)       # small enough to compare every pair when looking for a moved slide
SCALE = 0.75           # each half of a side-by-side PNG, of the 1280x720 screenshot
LABEL_H = 32
GAP = 10
RED = (255, 80, 80)
try:
    FONT = ImageFont.load_default(size=18)
except TypeError:      # Pillow < 10.1: one bitmap size only
    FONT = ImageFont.load_default()


def numbered(folder):
    """{slide number: path} of the slide-NNN.png files in folder."""
    out = {}
    for png in folder.glob("slide-*.png"):
        m = re.fullmatch(r"slide-(\d+)", png.stem)
        if m:
            out[int(m.group(1))] = png
    return out


class Shot:
    """One screenshot: a hash of its pixels and a thumbnail, read once."""

    def __init__(self, path):
        self.path = path
        rgb = self.image()
        self.size = rgb.size
        self.hash = hashlib.sha1(rgb.tobytes()).hexdigest()
        self.thumb = rgb.convert("L").resize(THUMB, Image.BILINEAR)

    def image(self):
        with Image.open(self.path) as im:
            return im.convert("RGB")


def difference(a, b):
    """(share of pixels that differ in any channel, bounding box of them)."""
    if a.hash == b.hash:
        return 0.0, None
    if a.size != b.size:
        return 1.0, (0, 0) + b.size
    r, g, b_ = ImageChops.difference(a.image(), b.image()).split()
    m = ImageChops.lighter(ImageChops.lighter(r, g), b_)
    total = a.size[0] * a.size[1]
    return (total - m.histogram()[0]) / total, m.getbbox()


def matches(a, b, threshold):
    if a.hash == b.hash:
        return True
    thumbs_close = ImageStat.Stat(ImageChops.difference(a.thumb, b.thumb)).mean[0] < 2.0
    return thumbs_close and difference(a, b)[0] <= threshold


def find_match(shot, pool, near, threshold, exclude):
    """The number in pool whose slide matches shot, the nearest to `near`."""
    hits = [n for n, other in pool.items() if n not in exclude and matches(shot, other, threshold)]
    return min(hits, key=lambda n: abs(n - near)) if hits else None


def side_by_side(old, new, n, note, box, out_dir):
    w, h = int(1280 * SCALE), int(720 * SCALE)
    sheet = Image.new("RGB", (2 * w + GAP, h + LABEL_H), (0, 0, 0))
    draw = ImageDraw.Draw(sheet)
    for i, (shot, label) in enumerate(((old, "old"), (new, "new"))):
        x = i * (w + GAP)
        if shot is None:
            draw.text((x + 8, 6), f"{label}: no slide here", fill="white", font=FONT)
            continue
        im = shot.image()
        sx, sy = w / im.size[0], h / im.size[1]
        sheet.paste(im.resize((w, h)), (x, LABEL_H))
        if box:
            x0, y0, x1, y1 = box
            draw.rectangle((x + x0 * sx - 3, LABEL_H + y0 * sy - 3, x + x1 * sx + 3, LABEL_H + y1 * sy + 3),
                           outline=RED, width=3)
        draw.text((x + 8, 6), f"{label}: {shot.path.parent.name}/{shot.path.name}", fill="white", font=FONT)
    draw.text((2 * w + GAP - 8 - draw.textlength(note, font=FONT), 6), note, fill=RED, font=FONT)
    sheet.save(out_dir / f"slide-{n:03d}.png")


def runs(pairs):
    """[(new, old), ...] → '13–40 +1, 52 −2': consecutive slides moved by one offset."""
    parts, start, prev, off = [], None, None, None
    for new, old in sorted(pairs) + [(None, None)]:
        o = None if new is None else new - old
        if new is not None and prev is not None and new == prev + 1 and o == off:
            prev = new
            continue
        if start is not None:
            span = f"{start}" if start == prev else f"{start}–{prev}"
            parts.append(f"{span} {'+' if off > 0 else '−'}{abs(off)}")
        start, prev, off = new, new, o
    return ", ".join(parts)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("old_dir", type=Path)
    ap.add_argument("new_dir", type=Path)
    ap.add_argument("--threshold", type=float, default=0.001,
                    help="share of pixels that may differ before a slide counts as changed (default 0.001)")
    ap.add_argument("--out", type=Path, help="folder for the side-by-side PNGs (default NEW_DIR/diff)")
    ap.add_argument("--from", dest="first", type=int, default=1, help="first slide to report")
    ap.add_argument("--to", dest="last", type=int, default=10_000, help="last slide to report")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    args = ap.parse_args()

    for d in (args.old_dir, args.new_dir):
        if not d.is_dir():
            print(f"shots-diff: not a folder: {d}", file=sys.stderr)
            return 2
    old = {n: Shot(p) for n, p in numbered(args.old_dir).items()}
    new = {n: Shot(p) for n, p in numbered(args.new_dir).items()}
    if not old or not new:
        print(f"shots-diff: no slide-NNN.png in {args.old_dir if not old else args.new_dir}", file=sys.stderr)
        return 2
    in_range = lambda n: args.first <= n <= args.last  # noqa: E731

    unchanged, moved, edited, added = [], [], {}, []
    for n in sorted(k for k in new if in_range(k)):
        share, box = difference(old[n], new[n]) if n in old else (None, None)
        if share is not None and share <= args.threshold:
            unchanged.append(n)
            continue
        source = find_match(new[n], old, n, args.threshold, exclude={n})
        if source is not None:
            moved.append((n, source))
        elif share is None:
            added.append(n)
        else:
            edited[n] = (share, box)

    # The old slide of an "edited" number that lives on at another number was
    # not edited: a slide was put in before it, so the new one is added.
    sources = {s for _, s in moved} | set(unchanged)
    for n in [n for n in edited if n in sources]:
        del edited[n]
        added.append(n)
    added.sort()
    # An old slide whose picture is in no new slide was taken out (unless its
    # number now shows an edited slide).
    removed = [n for n in sorted(k for k in old if in_range(k))
               if n not in sources and n not in edited
               and find_match(old[n], new, n, args.threshold, exclude=set()) is None]

    out_dir = args.out or args.new_dir / "diff"
    out_dir.mkdir(parents=True, exist_ok=True)
    for stale in out_dir.glob("slide-*.png"):
        stale.unlink()
    for n, (share, box) in edited.items():
        side_by_side(old[n], new[n], n, f"slide {n}: {share:.2%} of pixels differ", box, out_dir)
    for n in added:
        side_by_side(None, new[n], n, f"slide {n}: new", None, out_dir)
    for n in removed:
        side_by_side(old[n], None, n, f"old slide {n}: taken out", None, out_dir)

    changed = sorted(edited.items())
    result = {
        "threshold": args.threshold,
        "compared": len(unchanged) + len(moved) + len(edited) + len(added),
        "unchanged": len(unchanged),
        "changed": [{"slide": n, "share": round(s, 6)} for n, (s, _) in changed],
        "added": added,
        "removed": removed,
        "moved": [{"slide": n, "from": s} for n, s in moved],
        "moved_runs": runs(moved),
        "out": str(out_dir),
    }
    if args.json:
        print(json.dumps(result, indent=1))
    else:
        print(f"{result['compared']} slides compared (threshold {args.threshold:.2%}): "
              f"{len(changed)} changed, {len(added)} added, {len(removed)} removed, "
              f"{len(moved)} moved, {len(unchanged)} unchanged")
        if changed:
            print("  changed: " + ", ".join(f"{n} ({s:.2%})" for n, (s, _) in changed))
        if added:
            print("  added:   " + ", ".join(map(str, added)))
        if removed:
            print("  removed: " + ", ".join(f"old {n}" for n in removed))
        if moved:
            print("  moved:   " + result["moved_runs"])
        if changed or added or removed:
            print(f"side by side (old | new): {out_dir}/")
    return 1 if (changed or added or removed or moved) else 0


if __name__ == "__main__":
    sys.exit(main())
