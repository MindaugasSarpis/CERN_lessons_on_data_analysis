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
            "handson"]

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
    for fam in wanted:
        try:
            mod = importlib.import_module(fam)
        except ImportError as e:
            print(f"[{fam}] SKIPPED — import failed: {e}", file=sys.stderr)
            failed.append(fam)
            continue
        print(f"[{fam}] {len(mod.FIGURES)} figure(s)")
        for name, fn in mod.FIGURES.items():
            fn()
            total += 1
    print(f"Done: {total} figure(s) → {style.OUT}")
    if failed:
        print(f"FAILED families: {', '.join(failed)}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
