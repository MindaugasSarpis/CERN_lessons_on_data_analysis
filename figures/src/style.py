"""Course figure style — the ONLY styling entry point for figure code.

v3 (10 Nov 2026), after the lecturer on Lecture 7: "This one looks
cartoonish, need a scientific one". Dark-transparent SVG figures for the dark
slide theme, drawn as a physics paper or a good scientific talk draws them:

- Type: STIX General, the Times-like face of the journals, bundled with
  Matplotlib (regular, italic, bold, bold italic), and maths in STIX too
  (mathtext "stix"), so a label and its formula are one type. STIX has no
  thin space and no subscript digits: use() registers a copy that adds them
  (U+2009, U+202F, U+2080-2089, made from its own space and digits), so
  87 552 and d₀ come out in STIX. There is no fallback face: a glyph STIX
  lacks makes Matplotlib warn "Glyph ... missing", a bug to fix in the
  module. Space Mono stays for code-like labels (family=MONO), the slides'
  code face.
- Colours: the background, text, dim and accent are read from the slides'
  tokens (lectures/content/theme/styles/tokens.css), never copied.
- The frame of a paper: all four spines, 0.8 pt, in the text colour; ticks
  pointing in on all four sides, major 5 pt and minor 2.5 pt, minor ticks
  shown; no grid; a frameless legend; titles in regular weight. save()
  drops minor ticks on an axis of categories (bar names, fixed ticks),
  where they mean nothing, and the tick marks of a side whose spine a
  module hides (a deliberate "no box" figure keeps no stray ticks); a grid
  a module draws goes behind the marks, the ticks otherwise over them.
- Marks: lines 1.5 pt, markers 5 pt, error-bar caps 2 pt.
- Sizes for a projector: an inch of figure is 90 px of the 980 px slide
  canvas (scripts/measure-figures.mjs), so an 11 pt tick label reads at the
  size of a slide caption, axis labels 12.5 pt. Automatic ticks are counted
  as for 9.75 pt labels, and save() steps the labels of a crowded axis back
  towards 10 pt, so the type neither drops ticks nor makes them collide.
- The categorical cycle: Okabe-Ito brightened for near-black, the course cyan
  first. Each slot keeps its hue (the slides say "the orange line", "the pink
  line"); the steps are set so that neighbours stay apart for protan and
  deutan readers, and the last is no longer darker than the rest. Dataviz
  validate_palette.js, dark, surface #050507: adjacent CVD dE >= 8.8, normal
  >= 16.1; the first three (three-group scatters) pass all pairs too. Its
  lightness band (0.48-0.67, for dashboards) fails by design: the course
  cyan is L 0.83 and every slot sits in 0.68-0.90, bright on near-black.
- save() refuses a bitmap: an imshow, a rasterized artist or a filter embeds
  a PNG in the SVG, which blurs when the slide scales.
"""
import hashlib
import json
import os
import re
import tempfile
from collections import Counter
from pathlib import Path

import matplotlib as mpl
import matplotlib.axis as maxis
import matplotlib.category as mcategory
import matplotlib.font_manager as fm
import matplotlib.image as mimage
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.container import BarContainer

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "lectures" / "content" / "public" / "figures"
FONTS = Path(__file__).resolve().parents[1] / "fonts"
TOKENS_FILE = ROOT / "lectures" / "content" / "theme" / "styles" / "tokens.css"

# The size in inches of each figure that fills the rest of its slide (the
# slide has `class: fill`): its box on the slide, measured by
# scripts/measure-figures.mjs. save() draws a listed figure at that size, so
# it fills its box; constrained layout re-flows it. Unlisted figures keep the
# figsize their module gives them.
SIZES_FILE = Path(__file__).resolve().parent / "sizes.json"
SIZES = json.loads(SIZES_FILE.read_text()) if SIZES_FILE.exists() else {}


def _tokens(path: Path) -> dict:
    """The custom properties of tokens.css, {'bg': '#050507', ...}."""
    css = re.sub(r"/\*.*?\*/", "", path.read_text(), flags=re.S)
    return {m[1]: m[2].strip() for m in re.finditer(r"--([\w-]+)\s*:\s*([^;]+);", css)}


def _over(rgba: str, bg: str) -> str:
    """An rgba() token as the solid hex it shows on the background bg."""
    *rgb, a = (float(v) for v in re.findall(r"[\d.]+", rgba))
    base = (int(bg[i:i + 2], 16) for i in (1, 3, 5))
    return "#" + "".join(f"{round(a * c + (1 - a) * b):02x}" for c, b in zip(rgb, base))


_T = _tokens(TOKENS_FILE)
BG = _T["bg"]          # the slide background: the canvas of an opaque figure
FG = _T["fg"]          # text, the frame and its ticks
FG2 = _T["fg-2"]       # secondary text that must still read on a projector
DIM = _T["dim"]        # captions, de-emphasised marks
ACCENT = _T["accent"]  # course cyan, the first series colour
GRID = _over(_T["hair-strong"], BG)  # hairline grid: the slides' strong hairline
BAD = "#f47069"        # 'wrong' highlight (What's Wrong panels)
CYCLE = [ACCENT, "#f8b64f", "#6edb98", "#e88bc0", "#8a9cfc", "#f1e075", "#e67502"]

TICK_PT = 11           # tick labels; save() steps a crowded axis down to TICK_MIN_PT
TICK_MIN_PT = 10       # the old size: no figure gets smaller ticks than before
TICK_COUNT_PT = 9.75   # automatic ticks are counted as for labels this size
SERIF = "STIXGeneral"  # the figures' text face, Times-like as in a journal
SANS = SERIF           # v2's name for the text face, kept for the modules that use it
MONO = "Space Mono"    # code-like labels: family=style.MONO, or family="monospace"
THIN = " "        # thin space (the STIX copy of use() adds it)
MINUS = "−"       # the true minus sign

STIX = Path(mpl.get_data_path()) / "fonts" / "ttf"
STIX_FILES = ("STIXGeneral.ttf", "STIXGeneralItalic.ttf",
              "STIXGeneralBol.ttf", "STIXGeneralBolIta.ttf")
SPACES = {0x2009: 1 / 6, 0x202F: 1 / 6, 0x2006: 1 / 6, 0x200A: 1 / 10}  # em


def _save_font(font, out: Path) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(f"{out.name}.{os.getpid()}.tmp")
    font.save(tmp)
    tmp.replace(out)
    return out


def _stix_completed(src: Path, upright: Path | None = None) -> Path:
    """A copy of the STIX face src with the thin spaces of SPACES and the
    subscript digits U+2080-2089 (its own digits at 0.6, dropped 0.14 em),
    cached in the temp dir. An italic face also takes every symbol it lacks
    (the italics have no arrows, no ≈ ≤ ≥ √) from its upright face, upright
    as a typesetter sets them. Same family and PostScript names: the glyphs
    it shares with the bundled file are the same outlines."""
    data = src.read_bytes() + (upright.read_bytes() if upright else b"")
    key = hashlib.sha1(data).hexdigest()[:10]
    out = Path(tempfile.gettempdir()) / "cern-course-fonts" / f"{src.stem}-{key}-v2.ttf"
    if out.exists():
        return out
    from fontTools.pens.recordingPen import DecomposingRecordingPen
    from fontTools.pens.transformPen import TransformPen
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    from fontTools.ttLib import TTFont
    from fontTools.ttLib.tables._g_l_y_f import Glyph
    font = TTFont(src)
    upm = font["head"].unitsPerEm
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    glyf, hmtx = font["glyf"], font["hmtx"]
    order = list(font.getGlyphOrder())
    added = {}
    if upright:
        donor = TTFont(upright)
        dglyphs = donor.getGlyphSet()
        for cp, dname in donor.getBestCmap().items():
            if cp in cmap or not 0x2000 <= cp <= 0xFFFF:
                continue
            rec = DecomposingRecordingPen(dglyphs)
            dglyphs[dname].draw(rec)
            pen = TTGlyphPen(None)
            rec.replay(pen)
            name = f"up{cp:04X}"
            glyf[name] = glyph = pen.glyph()
            glyph.recalcBounds(glyf)
            hmtx[name] = (dglyphs[dname].width, getattr(glyph, "xMin", 0))
            added[cp] = name
        cmap = {**cmap, **added}
    for cp, em in SPACES.items():
        if cp not in cmap:
            name = f"space{cp:04X}"
            glyf[name] = Glyph()
            hmtx[name] = (round(em * upm), 0)
            added[cp] = name
    k, drop = 0.6, -0.14 * upm
    for i in range(10):
        cp = 0x2080 + i
        if cp in cmap or ord(str(i)) not in cmap:
            continue
        name = f"sub{i}"
        digit = cmap[ord(str(i))]
        rec = DecomposingRecordingPen(glyphs)
        glyphs[digit].draw(rec)
        pen = TTGlyphPen(None)
        rec.replay(TransformPen(pen, (k, 0, 0, k, 0, drop)))
        glyf[name] = glyph = pen.glyph()
        glyph.recalcBounds(glyf)
        hmtx[name] = (round(glyphs[digit].width * k), getattr(glyph, "xMin", 0))
        added[cp] = name
    order.extend(added.values())
    font.setGlyphOrder(order)
    for table in font["cmap"].tables:
        if table.isUnicode():
            table.cmap.update(added)
    return _save_font(font, out)


if not hasattr(maxis.Axis, "_mpl_tick_label_size"):  # once, even if style is reloaded
    maxis.Axis._mpl_tick_label_size = maxis.Axis._get_tick_label_size


def _density_size(axis, axis_name):
    """Matplotlib counts automatic ticks by the label size, so 11 pt labels
    alone dropped ticks (a log colour bar lost two of its four decades).
    Counted as at TICK_COUNT_PT, 283 of the 284 figures (10 Nov 2026) keep
    exactly the ticks they had with 10 pt labels on their slightly longer
    axes; one gains intermediate ticks, none loses one."""
    return min(axis._mpl_tick_label_size(axis_name), TICK_COUNT_PT)


_registered = False


def _register_fonts() -> None:
    """The completed STIX faces, put first so that "STIXGeneral" (text and
    mathtext alike) finds them before the bundled files, and Space Mono."""
    global _registered
    if _registered:
        return
    regular, italic, bold, bolditalic = (STIX / name for name in STIX_FILES)
    for src, upright in ((regular, None), (italic, regular), (bold, None), (bolditalic, bold)):
        path = str(_stix_completed(src, upright))
        fm.fontManager.addfont(path)
        entry = next(e for e in fm.fontManager.ttflist if e.fname == path)
        fm.fontManager.ttflist.remove(entry)
        fm.fontManager.ttflist.insert(0, entry)
    for path in (FONTS / "git" / "SpaceMono-Regular.ttf", FONTS / "git" / "SpaceMono-Bold.ttf"):
        fm.fontManager.addfont(str(path))
    fm.fontManager._findfont_cached.cache_clear()
    _registered = True


def use() -> None:
    _register_fonts()
    maxis.Axis._get_tick_label_size = _density_size
    mpl.rcParams.update({
        "figure.facecolor": "none", "axes.facecolor": "none",
        "savefig.facecolor": "none", "savefig.transparent": True,
        # Type: STIX for text and maths, no fallback face (see the docstring).
        "font.family": [SERIF],
        "font.monospace": [MONO, "DejaVu Sans Mono"],
        "font.size": 11,
        "mathtext.fontset": "stix",
        "axes.unicode_minus": True,
        "text.color": FG, "axes.labelcolor": FG, "axes.titlecolor": FG,
        "axes.edgecolor": FG, "xtick.color": FG, "ytick.color": FG,
        # Sizes for a projector; titles in regular weight, as in a paper.
        "axes.titlesize": 14, "axes.titleweight": "normal", "axes.titlepad": 7,
        "figure.titlesize": 14, "figure.titleweight": "normal",
        "axes.labelsize": 12.5, "axes.labelpad": 4,
        "xtick.labelsize": TICK_PT, "ytick.labelsize": TICK_PT,
        "legend.fontsize": 11, "legend.title_fontsize": 11,
        # The frame of a paper: four spines, ticks in on every side, minor
        # ticks shown, no grid.
        "axes.linewidth": 0.8,
        "axes.spines.top": True, "axes.spines.right": True,
        "xtick.direction": "in", "ytick.direction": "in",
        "xtick.top": True, "ytick.right": True,
        "xtick.minor.visible": True, "ytick.minor.visible": True,
        "xtick.major.size": 5, "ytick.major.size": 5,
        "xtick.minor.size": 2.5, "ytick.minor.size": 2.5,
        "xtick.major.width": 0.8, "ytick.major.width": 0.8,
        "xtick.minor.width": 0.7, "ytick.minor.width": 0.7,
        "xtick.major.pad": 5, "ytick.major.pad": 5,
        "xtick.minor.pad": 5, "ytick.minor.pad": 5,
        "axes.grid": False, "grid.color": GRID, "grid.linewidth": 0.6,
        "axes.axisbelow": "line",   # ticks over a filled bar, as the frame is
        # Marks: thin lines, small markers, short caps.
        "axes.prop_cycle": mpl.cycler(color=CYCLE),
        "lines.linewidth": 1.5, "lines.markersize": 5,
        "lines.markeredgewidth": 0.8,
        "lines.solid_capstyle": "butt",
        "errorbar.capsize": 2,
        "patch.linewidth": 0.8,
        "hatch.linewidth": 0.6,
        "boxplot.flierprops.markersize": 4,
        "legend.frameon": False, "legend.handlelength": 1.8,
        "legend.borderaxespad": 0.6,
        # "path": embed text as vector outlines. SVGs load via <img>, which
        # cannot see the page's webfonts, and the outlines carry true STIX.
        "svg.fonttype": "path",
        "svg.hashsalt": "cern-course",  # deterministic element ids across runs
        "figure.constrained_layout.use": True,
    })


def new_fig(w: float = 7, h: float = 4.2):
    fig, ax = plt.subplots(figsize=(w, h))
    return fig, ax


def thousands(x: float, decimals: int = 0, *, group4: bool = False) -> str:
    """A number as the slides write it: 87 552 with a thin space, a true
    minus, four digits whole (3646) unless group4. thousands(-0.5, 1) is
    '−0.5'."""
    s = f"{abs(x):.{decimals}f}"
    whole, _, frac = s.partition(".")
    if len(whole) > (3 if group4 else 4):
        whole = f"{int(whole):,}".replace(",", THIN)
    sign = MINUS if x < 0 and float(s) != 0 else ""
    return sign + whole + ("." + frac if frac else "")


class ThousandsFormatter(mticker.Formatter):
    """Tick labels written with thousands(); an axis that reaches 10 000
    groups its four-digit ticks too, so one axis has one style.
        ax.yaxis.set_major_formatter(style.ThousandsFormatter())"""

    def __init__(self, decimals: int = 0):
        self.decimals = decimals

    def __call__(self, x, pos=None):
        group4 = any(abs(v) >= 1e4 for v in self.locs)
        return thousands(x, self.decimals, group4=group4)


class FidelityError(RuntimeError):
    """A figure would put a bitmap on a slide."""


def _bitmaps(fig) -> list:
    """What in fig the SVG backend would embed as a PNG. An artist that is
    not drawn (hidden, or in a hidden Axes) does not count: beyond.as_cells
    keeps an image hidden as the scale of its colour bar."""
    found = Counter()
    for a in fig.findobj():
        ax = getattr(a, "axes", None)  # a figure's .axes is a list
        if not a.get_visible() or (hasattr(ax, "get_visible") and not ax.get_visible()):
            continue
        kind = type(a).__name__
        if isinstance(a, (mimage.AxesImage, mimage.FigureImage, mimage.BboxImage)):
            found[f"an image ({kind}: imshow, figimage or OffsetImage)"] += 1
        elif a.get_rasterized():
            found[f"rasterized=True on {kind}"] += 1
        elif a.get_agg_filter() is not None:
            found[f"an agg_filter on {kind}"] += 1
    for ax in fig.axes:
        if ax.get_rasterization_zorder() is not None:
            found["Axes.set_rasterization_zorder"] += 1
    return [f"{n} x {what}" for what, n in found.items()]


def _bar_axes(ax) -> set:
    """The category axes of ax's bar charts: 'x' under vertical bars that
    stand apart (a histogram's bars touch, and its axis is a scale)."""
    found = set()
    for c in ax.containers:
        if not isinstance(c, BarContainer) or len(c.patches) < 2:
            continue
        horiz = c.orientation == "horizontal"
        boxes = [p.get_bbox() for p in c.patches]
        mids = sorted({round((b.y0 + b.y1 if horiz else b.x0 + b.x1) / 2, 9) for b in boxes})
        width = max(abs(b.height if horiz else b.width) for b in boxes)
        steps = [b - a for a, b in zip(mids, mids[1:]) if b > a]
        if steps and width < 0.95 * min(steps):
            found.add("y" if horiz else "x")
    return found


def _ticks_on_frame(fig) -> None:
    """Minor ticks belong to a numeric scale: none on an axis of categories
    (bar names, fixed tick positions) or on a polar axes, where the default
    minor locator would only cut the space between two names. And no tick
    mark where a module took the spine away: a tick stands on its frame."""
    for ax in fig.axes:
        if ax.name == "3d":
            continue
        bars = _bar_axes(ax) if ax.name == "rectilinear" else set()
        for axis in (ax.xaxis, ax.yaxis):
            if not isinstance(axis.get_minor_locator(), mticker.AutoMinorLocator):
                continue
            major = axis.get_major_locator()
            if ax.name != "rectilinear" or axis.axis_name in bars or isinstance(
                    major, (mticker.FixedLocator, mticker.IndexLocator, mcategory.StrCategoryLocator)):
                axis.set_minor_locator(mticker.NullLocator())
        if ax.name != "rectilinear" or "outline" in ax.spines:
            continue  # a colour bar hides its four spines behind its outline
        # The ticks stand over a filled bar (axes.axisbelow "line"), but a
        # grid a module asks for goes behind every mark.
        if any(line.get_visible() for axis in (ax.xaxis, ax.yaxis)
               for line in axis.get_gridlines()):
            ax.set_axisbelow(True)
        for side, axis in (("top", "x"), ("bottom", "x"), ("left", "y"), ("right", "y")):
            spine = ax.spines.get(side)
            if spine is not None and not spine.get_visible():
                ax.tick_params(axis=axis, which="both", **{side: False})


def _crowded(axis, renderer) -> bool:
    """Do neighbouring drawn tick labels of axis overlap, or (along x) stand
    closer than 0.15 of their size? Rotated labels are not judged."""
    lo, hi = sorted(axis.get_view_interval())
    tol = (hi - lo) * 1e-9
    ticks = [t for t in axis.get_major_ticks() if lo - tol <= t.get_loc() <= hi + tol]
    horiz = axis.axis_name == "x"
    for row in ([t.label1 for t in ticks], [t.label2 for t in ticks]):
        row = [t for t in row if t.get_visible() and t.get_text().strip()]
        if len(row) < 2 or any(t.get_rotation() % 180 for t in row):
            continue
        boxes = sorted((t.get_window_extent(renderer) for t in row),
                       key=lambda b: b.x0 if horiz else b.y0)
        gap = 0.15 * row[0].get_size() * axis.get_figure(root=True).dpi / 72
        for a, b in zip(boxes, boxes[1:]):
            if (b.x0 - a.x1 < gap) if horiz else (b.y0 < a.y1):
                return True
    return False


def _fit_ticks(fig, name: str) -> None:
    """Step the tick labels of a crowded axis down by half a point, to
    TICK_MIN_PT, so the bigger type never makes neighbours collide."""
    start = {}
    for _ in range(int((TICK_PT - TICK_MIN_PT) * 2)):
        fig.draw_without_rendering()
        renderer = fig._get_renderer()
        shrunk = False
        for ax in fig.axes:
            if ax.name == "3d":
                continue
            for axis in (ax.xaxis, ax.yaxis):
                size = axis.get_majorticklabels()[0].get_size() if axis.get_majorticklabels() else 0
                if size - 0.5 >= TICK_MIN_PT and _crowded(axis, renderer):
                    start.setdefault(axis, size)
                    axis.set_tick_params(labelsize=size - 0.5)
                    shrunk = True
        if not shrunk:
            break
    for axis, size in start.items():
        print(f"  ~ {name}: crowded {axis.axis_name} tick labels "
              f"{size:g} -> {axis.get_majorticklabels()[0].get_size():g} pt")


def save(fig, name: str, *, opaque: bool = False, tight: bool = True) -> None:
    """opaque: solid slide-background canvas (for v-click layer stacks that
    must cover the layer below). tight=False: keep the full fixed canvas (for
    stage sets that must align pixel-perfectly when stacked).

    Raises FidelityError, and writes nothing, if the figure holds a bitmap:
    every figure reaches its slide as vector. Draw a grid with pcolormesh,
    hexbin or contourf, drop rasterized=True, and give a colour bar
    cb.solids.set_rasterized(False) (Matplotlib rasterizes one of 50+ colours)."""
    bitmaps = _bitmaps(fig)
    if bitmaps:
        plt.close(fig)
        raise FidelityError(f"{name}: would embed a bitmap in its SVG: " + "; ".join(bitmaps))
    OUT.mkdir(parents=True, exist_ok=True)
    if name in SIZES:
        fig.set_size_inches(*SIZES[name])
    _ticks_on_frame(fig)
    _fit_ticks(fig, name)
    kw = {"format": "svg", "metadata": {"Date": None}}
    if tight:
        kw["bbox_inches"] = "tight"
        # The tight box counts an axis label by its middle only, so a label
        # wider than its axes (a narrow panel at the edge) was cut off. The
        # list replaces Matplotlib's default one, so it starts from it.
        # A 3D Axes (axison False, _axis3don True) counts its labels
        # too, z included: its z label was cut to a sliver.
        kw["bbox_extra_artists"] = fig.get_default_bbox_extra_artists() + [
            axis.label for ax in fig.axes
            if ax.get_visible() and (ax.axison or getattr(ax, "_axis3don", False))
            for axis in (ax.xaxis, ax.yaxis, getattr(ax, "zaxis", None))
            if axis is not None and axis.get_visible() and axis.label.get_visible()
            and axis.label.get_text().strip()]
    if opaque:
        kw["transparent"] = False
        kw["facecolor"] = BG
        fig.patch.set_facecolor(BG)
    # metadata Date=None: drop the embedded timestamp so repeated builds are
    # byte-identical (otherwise every run dirties all 80+ committed SVGs).
    fig.savefig(OUT / f"{name}.svg", **kw)
    plt.close(fig)
    print(f"  + {name}.svg")
