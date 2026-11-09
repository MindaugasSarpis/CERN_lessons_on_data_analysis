"""Beyond two variables: the closing section of Lecture 7, plots of three
and four variables.

- `viz_beyond_heatmap`: the mean temperature of ten years for each day of the
  year (x) and hour of the day (y), as colour: three variables on a plane.
- `viz_beyond_surface`: the same grid as a 3D surface, temperature as height.
- `viz_beyond_scatter4d`: one point per day, daily means of temperature,
  humidity and wind on three axes and the month as colour: four variables.
- `viz_beyond_d0_hist2d`: the physics version of the heatmap, the LHCb D0
  candidates of `D0_KPi.csv` binned in mass and transverse momentum, the count
  as colour on a log scale, with the two projections on the sides.

The weather figures read `weather.csv` with the plain functions of the
lecture's module `weather.py` (as in handson.py), here with the column as a
parameter so that humidity and wind come out the same way as temperature.
A cell or a day is the mean of its measured hours: the 120 hours of
22-26 July 2019 with temperature -999 are left out, humidity and wind of
those hours too.

    python figures/src/beyond.py

prints every number the slides state.
"""
import calendar
import re

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PathCollection
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap, ListedColormap, LogNorm, Normalize
from matplotlib.image import AxesImage
from matplotlib.path import Path
from mpl_toolkits.mplot3d import art3d, proj3d

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data"
PATH = DATA / "weather.csv"
D0 = DATA / "D0_KPi.csv"

BG = "#0b0e14"          # opaque slide background (GIF has no alpha)
SIZE = (9, 3.8)         # a wide 16:9-slide panel
MONTHS = [calendar.month_abbr[m] for m in range(1, 13)]
TEMP_LABEL = "temperature (°C)"

# Bins of the month histograms: 1 °C from -17 to 33 °C, as in handson.py.
T_BINS, T_RANGE = 50, (-17, 33)

# The D0 histogram: 1 MeV/c^2 in mass around the peak; PT from the selection
# cut of the file (no candidate of the mass window below 2500 MeV/c) to
# 9000 MeV/c, just above the 99th percentile (8599), in bins of 100 MeV/c.
M_RANGE, M_BINS = (1810, 1920), 110
PT_RANGE, PT_BINS = (2500, 9000), 65

# The 3D figures: view (elevation, azimuth), box aspect and zoom, then the 3D
# Axes and the colorbar in figure fractions. A 3D Axes draws its box in a
# square inside its rect and takes no part in constrained layout, so the rect
# is placed by hand and the zoomed surface and points are not clipped to that
# square (clip_on=False). Its tight bbox leaves out the axis labels, so these
# two are saved on their full canvas (tight=False).
VIEW_SURF, BOX_SURF, ZOOM_SURF = (32, -42), (4.5, 1.8, 1.1), 1.48
AX_SURF, CBAR_SURF = [-0.045, 0.27, 0.84, 0.72], 0.735
VIEW_SC, BOX_SC, ZOOM_SC = (18, -55), (1.9, 1.3, 1.0), 1.45
AX_SC, CBAR_SC = [-0.053, 0.22, 0.8, 0.76], 0.787


# ---------------------------------------------------------------------------
# weather.py, as the lecture writes it, with the column as a parameter
# ---------------------------------------------------------------------------

MISSING = -999.0
TEMP, HUMIDITY, WIND = 1, 2, 3     # columns of weather.csv


def read_lines(path):
    return open(path).read().splitlines()[1:]


def value_of(line, column):
    return float(line.split(",")[column])


def mean(values):
    return sum(values) / len(values)


def group(path, start, stop, column=TEMP):
    """The values of a column for each key line[start:stop], measured hours only."""
    groups = {}
    for line in read_lines(path):
        if value_of(line, TEMP) == MISSING:
            continue
        key = line[start:stop]
        if key not in groups:
            groups[key] = []
        groups[key].append(value_of(line, column))
    return groups


# ---------------------------------------------------------------------------
# The data each figure draws
# ---------------------------------------------------------------------------

def day_hour_grid():
    """Mean temperature per (hour, day of year): 24 rows x 366 columns.

    group(PATH, 5, 13) keys every hour by 'MM-DDTHH'; the days are the 366
    'MM-DD' of a leap year in calendar order, 29 February included.
    """
    cells = group(PATH, 5, 13)
    days = sorted({key[0:5] for key in cells})
    grid = np.full((24, len(days)), np.nan)
    for col, day in enumerate(days):
        for hour in range(24):
            key = f"{day}T{hour:02d}"
            if key in cells:
                grid[hour, col] = mean(cells[key])
    return days, grid


def daily_means():
    """Daily means of temperature, humidity and wind over the measured hours."""
    temp = group(PATH, 0, 10, TEMP)
    hum = group(PATH, 0, 10, HUMIDITY)
    wind = group(PATH, 0, 10, WIND)
    days = list(temp)        # days with no measured hour have no key
    return (days,
            np.array([mean(temp[d]) for d in days]),
            np.array([mean(hum[d]) for d in days]),
            np.array([mean(wind[d]) for d in days]),
            np.array([int(d[5:7]) for d in days]))


def month_temps():
    """The hourly temperatures of each month '01'..'12' over all ten years."""
    return group(PATH, 5, 7)


def d0_columns():
    m, pt = np.loadtxt(D0, delimiter=",", skiprows=1, usecols=(0, 1), unpack=True)
    return m, pt


# ---------------------------------------------------------------------------
# Shared pieces
# ---------------------------------------------------------------------------

def _month_starts(days):
    """Column index of the 1st of each month, for x ticks."""
    return [days.index(f"{m:02d}-01") for m in range(1, 13)]


def _temp_norm(grid):
    """Diverging scale centred on 0 °C, symmetric, rounded out to 5 °C."""
    lim = 5 * np.ceil(np.nanmax(np.abs(grid)) / 5)
    return Normalize(-lim, lim)


def _season_cmap():
    """A cyclic map for the month, bright everywhere on the dark slide:
    winter cyan, spring green, summer amber, autumn pink, back to cyan.
    Twilight would put a near-black month in the cycle, invisible here."""
    anchors = [style.ACCENT, style.CYCLE[2], style.CYCLE[1], style.CYCLE[3], style.ACCENT]
    smooth = LinearSegmentedColormap.from_list("seasons", anchors)
    # Jan sits at 0 (cyan), Apr at 0.25, Jul at 0.5, Oct at 0.75, Dec next to Jan.
    return ListedColormap([smooth(i / 12) for i in range(12)], name="months")


def _dark_3d(ax):
    """Transparent panes, hairline grid, light text for a 3D Axes."""
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1, 1, 1, 0.025))
        axis.pane.set_edgecolor(style.GRID)
        axis.line.set_color(style.DIM)
        axis._axinfo["grid"].update(color=style.GRID, linewidth=0.6)
        axis.label.set_color(style.FG)
    ax.tick_params(axis="both", colors=style.DIM)
    ax.tick_params(axis="z", colors=style.DIM)


# ---------------------------------------------------------------------------
# Cells as vector paths, not images
# ---------------------------------------------------------------------------
# Slidev scales a slide with a CSS transform, so a bitmap inside an SVG (an
# imshow, or a 2D histogram or 3D surface drawn with rasterized=True) turns
# grainy on the projector. The cells of every grid here are vector paths
# (lecturer, 9 Nov 2026: "everything has to be vectorized, crisp"):
# - the cells of one colour are one compound path, so ten years of hours
#   (87 672 cells) are a few thousand paths, not 87 672 elements; in a flat
#   grid a run of one colour along a row is one rectangle;
# - they are drawn without antialiasing (shape-rendering crispEdges, which
#   finish() writes), so two cells that share an edge leave no hairline seam
#   at any zoom: the pixelated look of the image they replace, sharp at
#   every size;
# - finish() writes their path data in whole hundredths of a point, each
#   step relative to the last, in a group scaled by 0.01: whole numbers add
#   up exactly in the browser's single precision, so a corner two cells
#   share stays one point (decimal steps would leave pinholes), in about a
#   third of matplotlib's bytes. The rest of the file gets two decimals.

CRISP = "crisp-"    # gid prefix of the artists finish() draws without antialiasing
_QUAD = np.array([Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO,
                  Path.CLOSEPOLY], dtype=Path.code_type)


def grid_paths(vx, vy, rgba, hidden=None, runs=True):
    """The cells of a grid of quads as one compound path per colour.

    vx, vy: the corners, (rows + 1) x (cols + 1); rgba: the colours,
    rows x cols x 4 bytes. A cell of alpha 0 is left out, and so is a cell
    where hidden is True. runs: a run of one colour along a row is one quad;
    for a flat grid only, since in a 3D projection the corners of the next
    row would not lie exactly on the run's long edge.
    Returns the paths and their colours (RGBA, 0 to 1).
    """
    rows, cols = rgba.shape[:2]
    key = np.ascontiguousarray(rgba).view(np.uint32)[..., 0]
    skip = rgba[..., 3] == 0
    if hidden is not None:
        skip = skip | hidden
    start = np.ones((rows, cols), bool)
    if runs:
        start[:, 1:] = (key[:, 1:] != key[:, :-1]) | skip[:, 1:] | skip[:, :-1]
    r, c0 = np.nonzero(start)
    c1 = np.append(c0[1:], cols)
    c1[np.append(r[1:] != r[:-1], True)] = cols      # a run stops at the end of its row
    keep = ~skip[r, c0]
    r, c0, c1, k = r[keep], c0[keep], c1[keep], key[r, c0][keep]
    order = np.argsort(k, kind="stable")
    r, c0, c1, k = r[order], c0[order], c1[order], k[order]
    paths, colours = [], []
    for s in np.split(np.arange(len(k)), np.flatnonzero(np.diff(k)) + 1):
        if not len(s):
            continue
        rr, a, b = r[s], c0[s], c1[s]
        corners = [(rr, a), (rr, b), (rr + 1, b), (rr + 1, a), (rr, a)]
        v = np.stack([np.stack([vx[i, j], vy[i, j]], -1) for i, j in corners], 1)
        paths.append(Path(v.reshape(-1, 2), np.tile(_QUAD, len(s))))
        colours.append(rgba[rr[0], a[0]] / 255)
    return paths, np.reshape(colours, (-1, 4))


def as_cells(artist, name):
    """Draw the cells of an image (imshow) or a mesh (pcolormesh, hist2d) as
    vector paths in its place, crisp, one compound path per colour. The
    artist stays in its Axes, not drawn, for the limits it set and as the
    colour scale of a colour bar. name: unique within the figure."""
    if isinstance(artist, AxesImage):
        rows, cols = artist.get_array().shape
        left, right, bottom, top = artist.get_extent()
        ys = (bottom, top) if artist.origin == "lower" else (top, bottom)
        vx, vy = np.meshgrid(np.linspace(left, right, cols + 1),
                             np.linspace(*ys, rows + 1))
    else:
        vx, vy = np.moveaxis(artist.get_coordinates(), -1, 0)
    paths, colours = grid_paths(vx, vy, artist.to_rgba(artist.get_array(), bytes=True))
    cells = PathCollection(paths, facecolors=colours, edgecolors="none",
                           linewidths=0, zorder=artist.get_zorder())
    cells.set_gid(CRISP + name)
    artist.axes.add_collection(cells, autolim=False)
    artist.set_visible(False)
    return cells


class PlaneCells(PathCollection):
    """The cells of the plane z of a 3D Axes as vector paths, one compound
    path per colour, projected when the figure is drawn (as the polygons of
    plot_surface are).

    xe, ye: the cell edges along x and y; rgba: rows x cols x 4 bytes, a cell
    of alpha 0 left out (a hole). above: the PlaneCells drawn over this one;
    the cells hidden behind it are left out, about half of a stack of planes.
    outline=True: only the cells at the border and around the holes, drawn
    with antialiasing under the crisp cells (give those the CRISP gid), so
    the plane's outline is smooth and its inside without seams.
    """

    MARGIN = 2.0    # points: a cell this close to the outline of the plane above stays

    def __init__(self, xe, ye, z, rgba, outline=False, **kwargs):
        super().__init__([], edgecolors="none", linewidths=0, **kwargs)
        vx, vy = np.meshgrid(np.asarray(xe, float), np.asarray(ye, float))
        self._xyz = np.stack([vx, vy, np.full(vx.shape, float(z))], -1)
        self._rgba = rgba
        self._holes = rgba[..., 3] == 0
        self._outline = outline
        self.above = None

    def _corners(self):
        """The corners projected, and the same in display units."""
        p = proj3d._scale_proj_transform_vectors(self._xyz, self.axes)
        d = self.axes.transData.transform(p[..., :2].reshape(-1, 2))
        return p, d.reshape(p.shape[:2] + (2,))

    def _covers(self, d):
        """The cells with display corners d that this plane hides whole."""
        _, mine = self._corners()
        quad = mine[[0, 0, -1, -1], [0, -1, -1, 0]]       # the plane's outline
        edge = np.roll(quad, -1, axis=0) - quad
        normal = np.stack([edge[:, 1], -edge[:, 0]], -1) / np.hypot(*edge.T)[:, None]
        normal *= np.sign(((quad.mean(axis=0) - quad) * normal).sum(-1))[:, None]
        margin = self.MARGIN * self.axes.figure.dpi / 72
        inside = (((d[..., None, :] - quad) * normal).sum(-1) >= margin).all(-1)
        covered = inside[:-1, :-1] & inside[1:, :-1] & inside[:-1, 1:] & inside[1:, 1:]
        if self._holes.any():    # a cell seen through a hole stays
            near = np.zeros(inside.shape, bool)
            for i in (0, 1):
                for j in (0, 1):
                    near[i:i + self._holes.shape[0], j:j + self._holes.shape[1]] |= self._holes
            lo, hi = mine[near].min(axis=0) - margin, mine[near].max(axis=0) + margin
            cells = np.stack([d[:-1, :-1], d[1:, :-1], d[:-1, 1:], d[1:, 1:]])
            covered &= ~((cells.max(axis=0) >= lo) & (cells.min(axis=0) <= hi)).all(-1)
        return covered

    def do_3d_projection(self):
        p, d = self._corners()
        hidden = (self.above._covers(d) if self.above is not None
                  else np.zeros(self._holes.shape, bool))
        if self._outline:
            keep = np.ones(self._holes.shape, bool)
            keep[1:-1, 1:-1] = False                      # the border
            h = self._holes
            keep[1:] |= h[:-1]
            keep[:-1] |= h[1:]
            keep[:, 1:] |= h[:, :-1]
            keep[:, :-1] |= h[:, 1:]                      # and the cells around a hole
            hidden = hidden | ~keep
        paths, colours = grid_paths(p[..., 0], p[..., 1], self._rgba, hidden, runs=False)
        self.set_paths(paths)
        self.set_facecolor(colours)
        return np.min(p[..., 2])


class _Under(art3d.Poly3DCollection):
    """Polygons drawn before every other collection of their 3D Axes."""

    def do_3d_projection(self):
        super().do_3d_projection()
        return np.inf


def quad_colours(z, cmap, norm):
    """The colour of each quad of plot_surface(x, y, z) with this cmap and
    norm: the mean of its four corners, in plot_surface's order. Shaped as z
    (the last row and column unused), for plot_surface(facecolors=...), which
    then edges each quad in its own colour."""
    mean = (z[:-1, :-1] + z[:-1, 1:] + z[1:, 1:] + z[1:, :-1]) / 4
    colours = np.zeros(z.shape + (4,))
    colours[:-1, :-1] = cmap(norm(mean))
    return colours


def smooth_outline(ax, x, y, z, colours, linewidth):
    """The border quads of plot_surface(x, y, z, facecolors=colours,
    linewidth=linewidth), one quad per cell, once more with antialiasing
    under the crisp surface: a smooth outline."""
    rows, cols = x.shape[0] - 1, x.shape[1] - 1
    r, c = np.nonzero(np.pad(np.zeros((rows - 2, cols - 2), bool), 1,
                             constant_values=True))
    corners = [(r, c), (r, c + 1), (r + 1, c + 1), (r + 1, c)]
    verts = np.stack([np.stack([x[i, j], y[i, j], z[i, j]], -1) for i, j in corners], 1)
    ax.add_collection(_Under(verts, facecolors=colours[r, c], edgecolors=colours[r, c],
                             linewidths=linewidth, clip_on=False), autolim=False)


def vector_colorbar(bar):
    """Matplotlib draws a colour bar of 50 colours or more as an image; keep
    its cells vector, each edged in its own colour so no seam shows."""
    bar.solids.set_rasterized(False)
    bar.solids.set_edgecolor("face")
    return bar


def _steps(d):
    """The M, L and z of matplotlib's path data, each point in whole
    hundredths of a point; None for other path data (the glyphs' curves)."""
    tokens, steps, i = d.split(), [], 0
    try:
        while i < len(tokens):
            if tokens[i] == "z":
                steps.append(("z", None))
                i += 1
            elif tokens[i] in ("M", "L"):
                x, y = (round(float(t) * 100) for t in tokens[i + 1:i + 3])
                steps.append((tokens[i], (x, y)))
                i += 3
            else:
                return None
    except ValueError:
        return None
    return steps


def _hundredths(n):
    """A whole number of hundredths as the shortest decimal: 1205 -> 12.05."""
    whole, part = divmod(abs(n), 100)
    sign = "-" if n < 0 else ""
    if not part:
        return f"{sign}{whole}"
    return f"{sign}{whole or ''}.{part:02d}".rstrip("0")


def _pair(a, b):
    return f"{a}{'' if str(b).startswith('-') else ' '}{b}"


def _short_path(d):
    """Path data absolute with two decimals, H and V for the straight steps,
    h0 for a step of length 0; other path data as it is."""
    steps = _steps(d)
    if steps is None:
        return d
    out, here, start = [], None, None
    for cmd, p in steps:
        if cmd == "z":
            out.append("z")
            here = start
            continue
        if cmd == "M":
            start = p
        if cmd == "M" or here is None:
            out.append(cmd + _pair(_hundredths(p[0]), _hundredths(p[1])))
        elif p == here:
            out.append("h0")
        elif p[1] == here[1]:
            out.append("H" + _hundredths(p[0]))
        elif p[0] == here[0]:
            out.append("V" + _hundredths(p[1]))
        else:
            out.append("L" + _pair(_hundredths(p[0]), _hundredths(p[1])))
        here = p
    return "".join(out)


def _whole_path(d):
    """Path data in whole hundredths, each step relative to the last; None
    for path data other than M, L and z."""
    steps = _steps(d)
    if steps is None:
        return None
    out, here, start = [], (0, 0), (0, 0)
    for cmd, p in steps:
        if cmd == "z":
            out.append("z")
            here = start
            continue
        dx, dy = p[0] - here[0], p[1] - here[1]
        if cmd == "M":
            out.append("m" + _pair(dx, dy))
            start = p
        elif dy == 0:
            out.append(f"h{dx}")
        elif dx == 0:
            out.append(f"v{dy}")
        else:
            out.append("l" + _pair(dx, dy))
        here = p
    return "".join(out)


def _hundredfold_stroke(match):
    """A path's style inside the group scaled by 0.01: its stroke 100 times
    as wide (matplotlib leaves out a width of 1)."""
    style_ = match.group(1)
    if "stroke:" in style_:
        if "stroke-width:" in style_:
            style_ = re.sub(r"stroke-width: ([\d.]+)",
                            lambda m: f"stroke-width: {float(m.group(1)) * 100:g}", style_)
        else:
            style_ += "; stroke-width: 100"
    return f' style="{style_}"'


def _crisp_group(match):
    """A CRISP group: no antialiasing, its paths' clip on the group and their
    data whole and relative inside a group scaled by 0.01."""
    gid, body = match.groups()
    head = f'<g id="{gid}" shape-rendering="crispEdges"'
    clips = set(re.findall(r' clip-path="([^"]*)"', body))
    paths = re.findall(r' d="([^"]*)"', body)
    whole = [_whole_path(d) for d in paths]
    if len(clips) > 1 or None in whole:
        return f"{head}>{body}</g>"
    it = iter(whole)
    body = re.sub(r' d="[^"]*"', lambda _: f' d="{next(it)}"', body)
    body = re.sub(r' clip-path="[^"]*"', "", body)
    body = re.sub(r' style="([^"]*)"', _hundredfold_stroke, body)
    clip = f' clip-path="{clips.pop()}"' if clips else ""
    return f'{head}{clip}><g transform="scale(.01)">{body}</g></g>'


def finish(name):
    """Draw the CRISP groups of the saved figure name.svg without
    antialiasing and shorten its path data (see Cells as vector paths)."""
    svg = style.OUT / f"{name}.svg"
    text = svg.read_text()
    text = re.sub(f'<g id="({CRISP}[^"]*)">(.*?)</g>', _crisp_group, text, flags=re.S)
    text = re.sub(r' d="([^"]*)"', lambda m: f' d="{_short_path(m.group(1))}"', text)
    svg.write_text(text)


# ---------------------------------------------------------------------------
# 1. Three variables on a plane: day, hour, temperature
# ---------------------------------------------------------------------------

def _heatmap():
    days, grid = day_hour_grid()
    fig, ax = plt.subplots(figsize=SIZE)
    im = ax.imshow(grid, aspect="auto", origin="lower", cmap="RdBu_r",
                   norm=_temp_norm(grid), interpolation="none")
    as_cells(im, "heatmap")
    vector_colorbar(fig.colorbar(im, ax=ax, label="mean temperature (°C)", pad=0.015))
    ax.set_xticks(_month_starts(days), MONTHS)
    ax.set_yticks([0, 6, 12, 18], ["00:00", "06:00", "12:00", "18:00"])
    ax.set(xlabel="day of the year", ylabel="hour of the day")
    ax.grid(False)
    style.save(fig, "viz_beyond_heatmap")
    finish("viz_beyond_heatmap")


# ---------------------------------------------------------------------------
# 2. The same grid as a surface
# ---------------------------------------------------------------------------

def _surface():
    days, grid = day_hour_grid()
    x, y = np.meshgrid(np.arange(len(days)), np.arange(24))
    fig = plt.figure(figsize=SIZE, layout="none")
    ax = fig.add_axes(AX_SURF, projection="3d")
    sm = plt.cm.ScalarMappable(norm=_temp_norm(grid), cmap="RdBu_r")
    colours = quad_colours(grid, sm.cmap, sm.norm)
    # vector quads, crisp, each edged in its own colour (0.3 pt): no pinhole
    # where the surface folds over in the projection; the outline smooth
    ax.plot_surface(x, y, grid, facecolors=colours, shade=False, rcount=24,
                    ccount=len(days), linewidth=0.3, antialiased=False,
                    clip_on=False, gid=CRISP + "surface")
    smooth_outline(ax, x, y, grid, colours, 0.3)
    vector_colorbar(fig.colorbar(sm, cax=fig.add_axes([CBAR_SURF, 0.2, 0.012, 0.6]),
                                 label="mean temperature (°C)"))
    ax.view_init(elev=VIEW_SURF[0], azim=VIEW_SURF[1])
    ax.set_box_aspect(BOX_SURF, zoom=ZOOM_SURF)
    starts = _month_starts(days)
    ax.set_xticks(starts[::3], MONTHS[::3])
    ax.set_yticks([0, 6, 12, 18], ["00:00", "06:00", "12:00", "18:00"])
    ax.set_zticks([-10, 0, 10, 20])
    ax.set_xlabel("day of the year", labelpad=8)
    ax.set_ylabel("hour of the day", labelpad=6)
    ax.set_zlabel("°C", labelpad=4)
    _dark_3d(ax)
    style.save(fig, "viz_beyond_surface", tight=False)
    finish("viz_beyond_surface")


# ---------------------------------------------------------------------------
# 3. Four variables: temperature, humidity, wind, month
# ---------------------------------------------------------------------------

def _scatter4d():
    days, temp, hum, wind, month = daily_means()
    cmap = _season_cmap()
    norm = BoundaryNorm(np.arange(0.5, 13), cmap.N)
    fig = plt.figure(figsize=SIZE, layout="none")
    ax = fig.add_axes(AX_SC, projection="3d")
    pts = ax.scatter(temp, hum, wind, c=month, cmap=cmap, norm=norm, s=4,
                     linewidths=0, alpha=0.85, depthshade=False, clip_on=False)
    bar = fig.colorbar(pts, cax=fig.add_axes([CBAR_SC, 0.12, 0.012, 0.76]), label="month")
    bar.set_ticks(range(1, 13), labels=MONTHS)
    bar.ax.tick_params(labelsize=9)
    bar.solids.set_alpha(1)
    vector_colorbar(bar)
    ax.view_init(elev=VIEW_SC[0], azim=VIEW_SC[1])
    ax.set_box_aspect(BOX_SC, zoom=ZOOM_SC)
    ax.set_xlabel(TEMP_LABEL, labelpad=6)
    ax.set_ylabel("humidity (%)", labelpad=6)
    ax.set_zlabel("wind (m/s)", labelpad=4)
    _dark_3d(ax)
    style.save(fig, "viz_beyond_scatter4d", tight=False)
    finish("viz_beyond_scatter4d")


# 4. Time as one more dimension: the month histograms of slide 84 are the
#    component MonthHistograms (data: interactive_l07_data.py, 9 Nov 2026).

# ---------------------------------------------------------------------------
# 5. Physics: D0 candidates in mass and transverse momentum
# ---------------------------------------------------------------------------

def _d0_hist2d():
    m, pt = d0_columns()
    fig, axd = plt.subplot_mosaic([["top", ".", "."], ["main", "right", "bar"]],
                                  width_ratios=[5, 1, 0.12], height_ratios=[1, 2.6],
                                  figsize=SIZE)
    ax, top, right = axd["main"], axd["top"], axd["right"]
    top.sharex(ax)
    right.sharey(ax)

    *_, im = ax.hist2d(m, pt, bins=[M_BINS, PT_BINS], range=[M_RANGE, PT_RANGE],
                       cmap="viridis", norm=LogNorm())
    as_cells(im, "d0")
    bar = vector_colorbar(fig.colorbar(im, cax=axd["bar"], label="candidates per bin"))
    bar.set_ticks([1, 10, 100], labels=["1", "10", "100"])
    ax.set(xlabel=r"$K^-\pi^+$ mass $M$ (MeV/$c^2$)",
           ylabel=r"$p_\mathrm{T}$ (MeV/$c$)")
    ax.grid(False)

    inside = (pt >= PT_RANGE[0]) & (pt < PT_RANGE[1])
    top.hist(m[inside], bins=M_BINS, range=M_RANGE, histtype="stepfilled",
             color=style.ACCENT)
    top.tick_params(labelbottom=False)
    top.set_ylabel("per MeV/$c^2$")
    top.xaxis.grid(False)

    in_mass = (m >= M_RANGE[0]) & (m < M_RANGE[1])
    right.hist(pt[in_mass], bins=PT_BINS, range=PT_RANGE, histtype="stepfilled",
               color=style.ACCENT, orientation="horizontal")
    right.tick_params(labelleft=False)
    right.set_xlabel("per 100 MeV/$c$")
    right.yaxis.grid(False)
    style.save(fig, "viz_beyond_d0_hist2d")
    finish("viz_beyond_d0_hist2d")


FIGURES = {
    "viz_beyond_heatmap": _heatmap,
    "viz_beyond_surface": _surface,
    "viz_beyond_scatter4d": _scatter4d,
    "viz_beyond_d0_hist2d": _d0_hist2d,
}


# ---------------------------------------------------------------------------
# Every number a slide might state
# ---------------------------------------------------------------------------

def _report():
    days, grid = day_hour_grid()
    print("1-2. heatmap / surface: 24 hours x", len(days), "days, mean of the measured hours")
    hot = np.unravel_index(np.nanargmax(grid), grid.shape)
    cold = np.unravel_index(np.nanargmin(grid), grid.shape)
    print(f"  warmest cell {days[hot[1]]} {hot[0]:02d}:00  {grid[hot]:.2f} °C")
    print(f"  coldest cell {days[cold[1]]} {cold[0]:02d}:00  {grid[cold]:.2f} °C")
    print(f"  colour scale ±{_temp_norm(grid).vmax:.0f} °C")
    cells = group(PATH, 5, 13)
    print(f"  hours per cell: min {min(len(v) for v in cells.values())}, "
          f"max {max(len(v) for v in cells.values())}")
    by_day = group(PATH, 0, 10)
    for mm, name in (("01", "January"), ("07", "July")):
        cols = [i for i, d in enumerate(days) if d.startswith(mm)]
        profile = np.nanmean(grid[:, cols], axis=1)
        swings = [max(v) - min(v) for d, v in by_day.items() if d[5:7] == mm and len(v) == 24]
        print(f"  {name}: mean daily cycle {profile.min():.2f} °C at "
              f"{profile.argmin():02d}:00 to {profile.max():.2f} °C at {profile.argmax():02d}:00, "
              f"swing {profile.max() - profile.min():.2f} °C; "
              f"mean of each day's max - min {mean(swings):.2f} °C ({len(swings)} days)")

    dnames, temp, hum, wind, month = daily_means()
    print("3. scatter4d:", len(dnames), "days with a measured temperature")
    print(f"  daily means: temp {temp.min():.1f} to {temp.max():.1f} °C, "
          f"humidity {hum.min():.1f} to {hum.max():.1f} %, wind {wind.min():.2f} to {wind.max():.2f} m/s")
    for label, sel in (("below 0 °C", temp < 0), ("0-20 °C", (temp >= 0) & (temp <= 20)),
                       ("above 20 °C", temp > 20)):
        print(f"  days {label}: {sel.sum()}, mean humidity {hum[sel].mean():.1f} %, "
              f"mean wind {wind[sel].mean():.2f} m/s")
    seasons = {"winter DJF": (12, 1, 2), "spring MAM": (3, 4, 5),
               "summer JJA": (6, 7, 8), "autumn SON": (9, 10, 11)}
    for name, ms in seasons.items():
        sel = np.isin(month, ms)
        print(f"  {name}: {sel.sum()} days, mean wind {wind[sel].mean():.2f} m/s, "
              f"mean humidity {hum[sel].mean():.1f} %, mean temp {temp[sel].mean():.2f} °C")
    print(f"  correlation temp-humidity {np.corrcoef(temp, hum)[0, 1]:.2f}, "
          f"temp-wind {np.corrcoef(temp, wind)[0, 1]:.2f}, humidity-wind {np.corrcoef(hum, wind)[0, 1]:.2f}")

    months = month_temps()
    every = [t for k in sorted(months) for t in months[k]]
    whole, edges = np.histogram(every, bins=T_BINS, range=T_RANGE)
    print("4. month histograms (1 °C bins, -17 to 33 °C):",
          len(every), "hours, all inside the range:", int(whole.sum()) == len(every))
    tops = whole.argsort()[::-1]
    print(f"  all hours: peaks at the bins {edges[tops[0]]:.0f} to {edges[tops[0]] + 1:.0f} °C "
          f"({whole[tops[0]]} h); local maxima (bin start, hours):",
          [(int(edges[i]), int(whole[i])) for i in range(1, T_BINS - 1)
           if whole[i] >= whole[i - 1] and whole[i] >= whole[i + 1] and whole[i] > 500])
    peaks = {}
    for k in sorted(months):
        counts, _ = np.histogram(months[k], bins=T_BINS, range=T_RANGE)
        i = counts.argmax()
        peaks[k] = (edges[i], counts[i])
        print(f"  {calendar.month_name[int(k)]:>9}: mean {mean(months[k]):5.1f} °C, "
              f"{len(months[k])} h, peak bin {edges[i]:.0f} to {edges[i] + 1:.0f} °C "
              f"with {counts[i]} h")
    lo = min(peaks, key=lambda k: peaks[k][0])
    hi = max(peaks, key=lambda k: peaks[k][0])
    flat = min(peaks, key=lambda k: peaks[k][1])
    tall = max(peaks, key=lambda k: peaks[k][1])
    print(f"  coldest peak {calendar.month_name[int(lo)]}, warmest peak {calendar.month_name[int(hi)]}; "
          f"lowest (widest) peak {calendar.month_name[int(flat)]} {peaks[flat][1]} h, "
          f"highest (narrowest) peak {calendar.month_name[int(tall)]} {peaks[tall][1]} h")

    m, pt = d0_columns()
    in_m = (m >= M_RANGE[0]) & (m < M_RANGE[1])
    in_pt = (pt >= PT_RANGE[0]) & (pt < PT_RANGE[1])
    counts, me, pe = np.histogram2d(m, pt, bins=[M_BINS, PT_BINS], range=[M_RANGE, PT_RANGE])
    i, j = np.unravel_index(counts.argmax(), counts.shape)
    print("5. D0 hist2d:", len(m), "candidates in the file")
    print(f"  PT {pt.min():.0f} to {pt.max():.0f} MeV/c (99th percentile {np.percentile(pt, 99):.0f}); "
          f"range used {PT_RANGE[0]} to {PT_RANGE[1]} MeV/c, {PT_BINS} bins of 100")
    print(f"  in mass range {M_RANGE}: {in_m.sum()}; in both ranges: {(in_m & in_pt).sum()} "
          f"(= {int(counts.sum())} in the 2D histogram)")
    print(f"  fullest bin: M {me[i]:.0f}-{me[i + 1]:.0f} MeV/c^2, PT {pe[j]:.0f}-{pe[j + 1]:.0f} MeV/c, "
          f"{counts[i, j]:.0f} candidates; empty bins {(counts == 0).sum()} of {counts.size}")
    mproj = counts.sum(axis=1)
    print(f"  mass projection peaks at {me[mproj.argmax()]:.0f}-{me[mproj.argmax()] + 1:.0f} MeV/c^2 "
          f"with {mproj.max():.0f} per MeV/c^2; sidebands 1820-1830: {mproj[10:20].mean():.0f}, "
          f"1900-1910: {mproj[90:100].mean():.0f} per MeV/c^2 (almost no candidate outside 1815-1915)")


if __name__ == "__main__":
    _report()
