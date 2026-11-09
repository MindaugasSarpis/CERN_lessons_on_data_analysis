"""Course figure style — the ONLY styling entry point for figure code.

Dark-transparent SVG figures for the dark slide theme, in one palette and one
type with the slides:

- Colours: the background, text, dim and accent are read from the slides'
  tokens (lectures/content/theme/styles/tokens.css), never copied.
- Type: Space Grotesk at the slides' weights (400 text, 500 medium, 700
  bold) and in math, Space Mono for code-like labels.
  figures/fonts/SpaceGrotesk-Regular.ttf is the VARIABLE font, whose default
  instance is Light (300): registered as it is, every label came out Light.
  use() pins it at 400, 500 and 700, each under its own name.
- Sizes for a projector: an inch of figure is 90 px of the 980 px slide
  canvas (scripts/measure-figures.mjs), so an 11 pt tick label reads at the
  size of a slide caption. Automatic ticks are counted as before, and save()
  steps the labels of a crowded axis back towards the old 10 pt, so the
  bigger type neither drops ticks nor makes them collide.
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
import io
import json
import math
import os
import re
import tempfile
from collections import Counter
from pathlib import Path

import matplotlib as mpl
import matplotlib.axis as maxis
import matplotlib.font_manager as fm
import matplotlib.image as mimage
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

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
FG = _T["fg"]          # text and strokes
FG2 = _T["fg-2"]       # secondary text that must still read on a projector
DIM = _T["dim"]        # ticks, captions, de-emphasised marks
ACCENT = _T["accent"]  # course cyan, the first series colour
GRID = _over(_T["hair-strong"], BG)  # hairline grid: the slides' strong hairline
BAD = "#f47069"        # 'wrong' highlight (What's Wrong panels)
CYCLE = [ACCENT, "#f8b64f", "#6edb98", "#e88bc0", "#8a9cfc", "#f1e075", "#e67502"]

TICK_PT = 11           # tick labels; save() steps a crowded axis down to TICK_MIN_PT
TICK_MIN_PT = 10       # the old size: no figure gets smaller ticks than before
TICK_COUNT_PT = 9.75   # automatic ticks are counted as for labels this size
SANS = "Space Grotesk"
MONO = "Space Mono"    # code-like labels: family=style.MONO, or family="monospace"
THIN = "\u2009"        # thin space; Space Grotesk has no U+202F
MINUS = "\u2212"       # the true minus sign


GREEK = [*range(0x391, 0x3AA), *range(0x3B1, 0x3CA), 0x3D1, 0x3D5, 0x3D6, 0x3F1, 0x3F5]
DEJAVU = Path(mpl.get_data_path()) / "fonts" / "ttf"


def _x_height(font) -> float:
    from fontTools.pens.boundsPen import BoundsPen
    glyphs = font.getGlyphSet()
    pen = BoundsPen(glyphs)
    glyphs[font.getBestCmap()[ord("x")]].draw(pen)
    return pen.bounds[3]


def _add_greek(font, donor_file: Path) -> None:
    """Copy the Greek letters of a DejaVu face into font, scaled to its
    x-height. Space Grotesk has none; borrowed whole, DejaVu's stood 12 %
    taller than the text and the math fallback STIX Sans 12 % shorter."""
    from fontTools.pens.recordingPen import DecomposingRecordingPen
    from fontTools.pens.transformPen import TransformPen
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    from fontTools.ttLib import TTFont
    donor = TTFont(donor_file)
    dglyphs, dcmap = donor.getGlyphSet(), donor.getBestCmap()
    k = _x_height(font) / _x_height(donor)
    have, glyf, hmtx = font.getBestCmap(), font["glyf"], font["hmtx"]
    order = list(font.getGlyphOrder())
    for cp in GREEK:
        name = f"greek{cp:04X}"
        if cp in have or cp not in dcmap or name in glyf:
            continue
        rec = DecomposingRecordingPen(dglyphs)
        dglyphs[dcmap[cp]].draw(rec)
        pen = TTGlyphPen(None)
        rec.replay(TransformPen(pen, (k, 0, 0, k, 0, 0)))
        glyf[name] = glyph = pen.glyph()
        glyph.recalcBounds(glyf)
        hmtx[name] = (round(dglyphs[dcmap[cp]].width * k), getattr(glyph, "xMin", 0))
        order.append(name)
        for table in font["cmap"].tables:
            if table.isUnicode():
                table.cmap[cp] = name
    font.setGlyphOrder(order)


def _save_font(font, out: Path) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(f"{out.name}.{os.getpid()}.tmp")
    font.save(tmp)
    tmp.replace(out)
    return out


def _pinned(var: Path, wght: int) -> Path:
    """The variable font var pinned at weight wght, with Greek, cached in the
    temp dir.

    Each weight gets its own PostScript name (SpaceGrotesk-Bold, ...). The
    SVG backend names a glyph outline by the PostScript name and character,
    so weights that share a name share outlines: the static files in
    fonts/git/ are all "SpaceGrotesk-Light", and a bold title drew every
    letter already used by a 400 label at 400."""
    data = var.read_bytes()
    key = hashlib.sha1(data).hexdigest()[:10]
    out = Path(tempfile.gettempdir()) / "cern-course-fonts" / f"{var.stem}-{wght}-{key}-v3.ttf"
    if not out.exists():
        from fontTools.ttLib import TTFont
        from fontTools.varLib.instancer import instantiateVariableFont
        font = instantiateVariableFont(TTFont(io.BytesIO(data)), {"wght": wght},
                                       updateFontNames=True)
        font["OS/2"].usWeightClass = wght
        _add_greek(font, DEJAVU / ("DejaVuSans-Bold.ttf" if wght >= 600 else "DejaVuSans.ttf"))
        _save_font(font, out)
    return out


def _sheared(src: Path, skew: float = 0.25) -> Path:
    """An italic of the static font src, sheared by skew (about 14 degrees).
    Space Grotesk has no italic; a browser draws the slides' <em> in Space
    Grotesk by this same shear (Skia's synthetic italic). Math variables and
    style="italic" text use it; its Greek, from src, is sheared alike."""
    out = src.with_name(f"{src.stem}-italic.ttf")
    if not out.exists():
        from fontTools.ttLib import TTFont
        font = TTFont(src)
        glyf, hmtx = font["glyf"], font["hmtx"]
        for name in font.getGlyphOrder():
            g = glyf[name]
            if g.isComposite():
                for c in g.components:
                    c.x = round(c.x + skew * c.y)
            elif g.numberOfContours > 0:
                g.coordinates.transform(((1, 0), (skew, 1)))
                g.coordinates.toInt()
            g.recalcBounds(glyf)
            if hasattr(g, "xMin"):
                hmtx[name] = (hmtx[name][0], g.xMin)
        font["post"].italicAngle = -math.degrees(math.atan(skew))
        font["OS/2"].fsSelection = (font["OS/2"].fsSelection | 0x01) & ~0x40  # italic, not regular
        font["head"].macStyle |= 0x02
        weight = font["name"].getDebugName(6).split("-")[-1]   # Regular, Medium, Bold
        sub = "Italic" if weight == "Regular" else f"{weight} Italic"
        names = {2: "Bold Italic" if weight == "Bold" else "Italic", 17: sub,
                 4: f"Space Grotesk {sub}", 6: f"SpaceGrotesk-{sub.replace(' ', '')}"}
        for rec in font["name"].names:
            if rec.nameID in names:
                rec.string = names[rec.nameID]
        _save_font(font, out)
    return out


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
    """Space Grotesk at 400, 500 and 700, pinned from the variable font (the
    fonts/git/ statics have the same outlines but one shared name), each
    with its sheared italic, and Space Mono."""
    global _registered
    if _registered:
        return
    var = FONTS / "SpaceGrotesk-Regular.ttf"
    for wght in (400, 500, 700):
        upright = _pinned(var, wght)
        fm.fontManager.addfont(str(upright))
        fm.fontManager.addfont(str(_sheared(upright)))
    for path in (FONTS / "git" / "SpaceMono-Regular.ttf", FONTS / "git" / "SpaceMono-Bold.ttf"):
        fm.fontManager.addfont(str(path))
    _registered = True


def use() -> None:
    _register_fonts()
    maxis.Axis._get_tick_label_size = _density_size
    mpl.rcParams.update({
        "figure.facecolor": "none", "axes.facecolor": "none",
        "savefig.facecolor": "none", "savefig.transparent": True,
        # Type: the slides' faces; DejaVu fills any glyph still missing. Math
        # is set in Space Grotesk too: digits and operators as in the text,
        # variables and Greek in its sheared italic, other symbols (sqrt, ell,
        # partial) from STIX Sans. ("cm" would copy the slides' KaTeX, whose
        # hairlines thin out at figure sizes on a projector.)
        "font.family": [SANS, "DejaVu Sans"],
        "font.monospace": [MONO, "DejaVu Sans Mono"],
        "font.size": 11,
        "mathtext.fontset": "custom",
        "mathtext.rm": SANS, "mathtext.sf": SANS, "mathtext.cal": SANS,
        "mathtext.it": f"{SANS}:italic", "mathtext.bf": f"{SANS}:bold", "mathtext.tt": MONO,
        "mathtext.fallback": "stixsans",
        "axes.unicode_minus": True,
        "text.color": FG, "axes.labelcolor": FG, "axes.titlecolor": FG,
        "axes.edgecolor": DIM, "xtick.color": DIM, "ytick.color": DIM,
        # Sizes for a projector.
        "axes.titlesize": 15, "axes.titleweight": "bold", "axes.titlepad": 8,
        "figure.titlesize": 15, "figure.titleweight": "bold",
        "axes.labelsize": 12.5, "axes.labelpad": 4,
        "xtick.labelsize": TICK_PT, "ytick.labelsize": TICK_PT,
        "legend.fontsize": 11,
        # Short outward ticks, a thin frame, a hairline grid behind the data.
        "xtick.direction": "out", "ytick.direction": "out",
        "xtick.major.size": 3, "ytick.major.size": 3,
        "xtick.major.width": 0.8, "ytick.major.width": 0.8,
        "xtick.minor.size": 2, "ytick.minor.size": 2,
        "xtick.minor.width": 0.6, "ytick.minor.width": 0.6,
        "xtick.major.pad": 3.5, "ytick.major.pad": 3.5,
        "axes.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
        "axes.axisbelow": True,
        # Marks.
        "axes.prop_cycle": mpl.cycler(color=CYCLE),
        "lines.linewidth": 2.4, "lines.markersize": 7,
        "lines.solid_capstyle": "round",
        "patch.linewidth": 0.8,
        "legend.frameon": False,
        # "path": embed text as vector outlines. SVGs load via <img>, which
        # cannot see the page's webfonts — fonttype "none" silently fell back
        # to the browser default sans. Outlines carry true Space Grotesk.
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
    _fit_ticks(fig, name)
    kw = {"format": "svg", "metadata": {"Date": None}}
    if tight:
        kw["bbox_inches"] = "tight"
        # The tight box counts an axis label by its middle only, so a label
        # wider than its axes (a narrow panel at the edge) was cut off. The
        # list replaces Matplotlib's default one, so it starts from it.
        kw["bbox_extra_artists"] = fig.get_default_bbox_extra_artists() + [
            axis.label for ax in fig.axes if ax.get_visible() and ax.axison
            for axis in (ax.xaxis, ax.yaxis)
            if axis.get_visible() and axis.label.get_visible() and axis.label.get_text().strip()]
    if opaque:
        kw["transparent"] = False
        kw["facecolor"] = BG
        fig.patch.set_facecolor(BG)
    # metadata Date=None: drop the embedded timestamp so repeated builds are
    # byte-identical (otherwise every run dirties all 80+ committed SVGs).
    fig.savefig(OUT / f"{name}.svg", **kw)
    plt.close(fig)
    print(f"  + {name}.svg")
