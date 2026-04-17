"""Sync cwilke figures into the slide deck's public/figures directory.

- For every `cwilke_*.svg` referenced from a Slidev markdown file under
  `lectures/content/slides/`, ensure the corresponding SVG exists under
  `lectures/content/public/figures/` (copied from `misc/python/cwilke/figs/`).
- Optionally, with `--prune`, delete any `cwilke_*.svg` in
  `lectures/content/public/figures/` that no slide file references.

Usage (from repo root):

    # just report what the slides need vs. what's deployed
    python misc/python/cwilke/sync_slide_figures.py

    # remove deployed figures that no slide references any more
    python misc/python/cwilke/sync_slide_figures.py --prune

This keeps the committed asset set small: only figures actually used in a
slide file are kept; everything else stays regeneratable from the scripts.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]
_FIGS_ROOT = _REPO_ROOT / "misc" / "python" / "cwilke" / "figs"
_PUBLIC_FIGS = _REPO_ROOT / "lectures" / "content" / "public" / "figures"
_SLIDES_ROOT = _REPO_ROOT / "lectures" / "content" / "slides"

_REF_RE = re.compile(r"/figures/(cwilke_[a-zA-Z0-9_]+)\.svg")


def scan_slide_references() -> set[str]:
    refs: set[str] = set()
    for md in _SLIDES_ROOT.rglob("*.md"):
        for match in _REF_RE.finditer(md.read_text()):
            refs.add(match.group(1))
    return refs


def map_source_svgs() -> dict[str, Path]:
    """Map cwilke_<chapter>_<name> → source SVG under misc/python/cwilke/figs/."""
    sources: dict[str, Path] = {}
    if not _FIGS_ROOT.exists():
        return sources
    for svg in _FIGS_ROOT.rglob("*.svg"):
        chapter = svg.parent.name
        key = f"cwilke_{chapter}_{svg.stem}"
        sources[key] = svg
    return sources


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prune", action="store_true",
                        help="delete deployed SVGs no slide references")
    args = parser.parse_args()

    refs = scan_slide_references()
    sources = map_source_svgs()

    deployed = {p.stem for p in _PUBLIC_FIGS.glob("cwilke_*.svg")}

    missing_source = refs - sources.keys()
    not_deployed = refs - deployed
    unreferenced = deployed - refs

    print(f"{len(refs)} cwilke figures referenced by slides")
    print(f"{len(sources)} source SVGs available under misc/python/cwilke/figs/")
    print(f"{len(deployed)} cwilke_*.svg deployed under public/figures/")

    if missing_source:
        print("\nReferenced by slides but no source SVG:")
        for k in sorted(missing_source):
            print(f"  !! {k}")

    # Copy any referenced-but-not-deployed (and we have the source for).
    copied = 0
    for key in sorted(not_deployed):
        src = sources.get(key)
        if src is None:
            continue
        dst = _PUBLIC_FIGS / f"{key}.svg"
        dst.write_bytes(src.read_bytes())
        copied += 1
        print(f"  +  copied {key}")
    if copied:
        print(f"\ncopied {copied} missing figures into public/figures/")

    if unreferenced:
        print(f"\n{len(unreferenced)} deployed figures are NOT referenced by any slide:")
        for k in sorted(unreferenced)[:20]:
            print(f"  ?  {k}")
        if len(unreferenced) > 20:
            print(f"  ... +{len(unreferenced) - 20} more")
        if args.prune:
            removed = 0
            for key in unreferenced:
                p = _PUBLIC_FIGS / f"{key}.svg"
                if p.exists():
                    p.unlink()
                    removed += 1
            print(f"\npruned {removed} unreferenced figures.")
        else:
            print("\n(pass --prune to delete them)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
