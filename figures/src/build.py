#!/usr/bin/env python3
"""Regenerate the course's scripted figures. Usage:
    python3 figures/src/build.py [--only family[,family...]]
Families are modules in figures/src that define FIGURES: {name: callable}.
"""
import argparse
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import style

FAMILIES = ["anatomy", "amounts", "distributions", "associations",
            "coordinates", "emphasis", "color", "proportions", "story", "ml",
            "fitting",
            "handson", "beyond", "goodbad", "advanced",
            "arrays", "probability", "perceptron", "cleaning",
            "concepts", "computing", "git", "language", "lasting", "gallery",
            "lifecycle"]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated family list")
    args = ap.parse_args()
    wanted = args.only.split(",") if args.only else FAMILIES
    unknown = [w for w in wanted if w not in FAMILIES]
    if unknown:
        print(f"error: unknown families {unknown}; known: {FAMILIES}", file=sys.stderr)
        return 2
    style.use()
    total = 0
    failed = []
    refused = []
    for fam in wanted:
        try:
            mod = importlib.import_module(fam)
        except ImportError as e:
            print(f"[{fam}] SKIPPED — import failed: {e}", file=sys.stderr)
            failed.append(fam)
            continue
        print(f"[{fam}] {len(mod.FIGURES)} figure(s)")
        for name, fn in mod.FIGURES.items():
            try:
                fn()
            except style.FidelityError as e:  # nothing written: the old SVG stays
                print(f"  ! {e}", file=sys.stderr)
                refused.append(name)
                continue
            total += 1
    print(f"Done: {total} figure(s) → {style.OUT}")
    shown = []
    if refused:
        slides = "\n".join(p.read_text(encoding="utf-8") for p in
                           (style.ROOT / "lectures" / "content" / "slides").glob("*.md"))
        shown = [n for n in refused if f"/figures/{n}.svg" in slides]
        print(f"REFUSED, would embed a bitmap; their old SVGs stay: {', '.join(refused)}",
              file=sys.stderr)
        if shown:
            print(f"... and a deck shows {', '.join(shown)}: draw them as vector",
                  file=sys.stderr)
    if failed:
        print(f"FAILED families: {', '.join(failed)}", file=sys.stderr)
    return 1 if failed or shown else 0

if __name__ == "__main__":
    sys.exit(main())
