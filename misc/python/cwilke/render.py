"""CLI to render all (or some) cwilke figures.

Usage (from repo root):

    python -m misc.python.cwilke.render              # render every figure
    python -m misc.python.cwilke.render amounts      # one chapter
    python -m misc.python.cwilke.render amounts/boxoffice_horizontal

Each script under chapters/<chapter>/<name>.py must expose a `render()`
function that draws and saves its figure via cwilke.theme.save.
"""

from __future__ import annotations

import importlib
import pkgutil
import sys
import traceback
from pathlib import Path

_PKG_ROOT = Path(__file__).resolve().parent
_CHAPTERS_ROOT = _PKG_ROOT / "chapters"


def _iter_scripts(target: str | None):
    chapters = sorted(p.name for p in _CHAPTERS_ROOT.iterdir()
                       if p.is_dir() and not p.name.startswith("_"))
    if target is None:
        for c in chapters:
            yield from _iter_chapter(c)
        return
    if "/" in target:
        chapter, name = target.split("/", 1)
        yield chapter, name
        return
    yield from _iter_chapter(target)


def _iter_chapter(chapter: str):
    chap_dir = _CHAPTERS_ROOT / chapter
    if not chap_dir.is_dir():
        raise SystemExit(f"Unknown chapter: {chapter}")
    for py in sorted(chap_dir.glob("*.py")):
        if py.name.startswith("_"):
            continue
        yield chapter, py.stem


def main() -> int:
    target = sys.argv[1] if len(sys.argv) > 1 else None
    ok, fail = 0, 0
    for chapter, name in _iter_scripts(target):
        mod = f"cwilke.chapters.{chapter}.{name}"
        try:
            m = importlib.import_module(mod)
            m.render()
            print(f"  OK  {chapter}/{name}")
            ok += 1
        except Exception as exc:  # noqa: BLE001
            print(f"  !!  {chapter}/{name}: {exc}")
            traceback.print_exc()
            fail += 1
    print(f"\n{ok} rendered, {fail} failed.")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
