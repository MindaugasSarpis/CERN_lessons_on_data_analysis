"""Reading a figure: Lecture 7's explainers of the error bar, the fitted curve
and the pulls, and four misleading figures each drawn again honestly.

The lecturer, 10 Nov 2026, after delivering Lecture 7: "a bit more textbook
content, a few more examples of misleading or bad plots and then good ones.
Also where we introduce error bars and things some people see it for the
first time. Need an explainer slide of what they are."

The explainers follow the slide "The Parts of a Figure" (anatomy.py) and use
its numbers: the mass of the first 1500 rows of D0_KPi.csv in 30 bins of
3 MeV/c^2, the fit of a Gaussian on a straight line.

  * viz_reading_repeats: what the error bar sqrt(n) of a count is. The file
    holds 61 blocks of 1500 rows, the same measurement 61 times: the count
    of the top bin (1862 to 1865 MeV/c^2) in each block, against the bar of
    the first block, 95 +- 9.7.
  * viz_reading_chi2: what the fitted curve is. The 30 distances from the
    points to the curve, each in units of its bar, squared and added: chi^2.
    The fit, and the same curve moved by 5 MeV/c^2.
  * viz_reading_pulls: what a pull is, (count - fit) / bar, for the fit and
    for the straight line alone.

The misleading figures, each with its honest version, from the weather log
(lectures/workbook/docs/data/weather.csv, read as handson.py reads it) and
from NOAA's record of CO2 at Mauna Loa:

  * viz_reading_ink: the principle of proportional ink (a value doubled: a
    bar's ink x2, a circle's radius x2 gives ink x4).
  * frost hours per year as circles whose radius follows the count, then as
    bars from zero;
  * the hours in four temperature bands as a pie in perspective, then as
    bars in the order of temperature;
  * the hours of 20 degC or more as a running total, then year by year;
  * CO2 at ten years of a table (every ten years, then every five) drawn as
    equal steps, then at their years.

Every number on the slides is printed by

    python figures/src/reading.py
"""
import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgba
from matplotlib.patches import Circle, Polygon, Rectangle

import anatomy
import style
from handson import PATH, group

SIDE = (6.16, 4.26)      # a single plot beside its caption (grid-side), until measured
WIDE = (9.41, 3.56)      # a figure of two panels under its caption, until measured
BLOCK = anatomy.N_ROWS   # 1500 rows: one repetition of the measurement
TOP_BIN = (1862.0, 1865.0)
SHIFT = 5.0              # MeV/c^2: the fitted curve moved, for comparison
WARM = 20.0              # degC: a "warm hour"
YEARS = list(range(2016, 2026))


def _paper(color, alpha=0.45):
    """A bar as a paper draws it: a light fill, a thin edge in the full colour."""
    return dict(facecolor=to_rgba(color, alpha), edgecolor=color, linewidth=0.9)


def _fig(name, size, **kw):
    return plt.subplots(figsize=style.SIZES.get(name, size), **kw)


# ---------------------------------------------------------------------------
# The numbers
# ---------------------------------------------------------------------------

def repeats():
    """The count in TOP_BIN for each block of BLOCK rows of the D0 file."""
    m = np.loadtxt(anatomy.DATA, delimiter=",", skiprows=1, usecols=0)
    nb = len(m) // BLOCK
    counts = np.array([((b >= TOP_BIN[0]) & (b < TOP_BIN[1])).sum()
                       for b in (m[i * BLOCK:(i + 1) * BLOCK] for i in range(nb))])
    first = counts[0]
    lo, hi = first - math.sqrt(first), first + math.sqrt(first)
    others = counts[1:]
    inside = int(((others >= lo) & (others <= hi)).sum())
    return dict(rows=len(m), blocks=nb, counts=counts, first=int(first), lo=lo, hi=hi,
                inside=inside, others=len(others), mean=counts.mean(),
                sd=counts.std(ddof=1))


def fit_numbers():
    d = anatomy.numbers()
    f = d["fit"]
    x, n, s = d["x"], d["n"], d["s"]
    curve = anatomy.model(x, *f["p"])
    moved = f["p"].copy()
    moved[1] += SHIFT
    curve_moved = anatomy.model(x, *moved)
    chi2_moved = float((((n - curve_moved) / s) ** 2).sum())
    # the straight line alone, by weighted least squares
    X = np.column_stack([np.ones_like(x), x - anatomy.PIVOT])
    w = 1 / s ** 2
    beta = np.linalg.solve(X.T @ (w[:, None] * X), X.T @ (w * n))
    line_only = X @ beta
    pulls_line = (n - line_only) / s
    i = int(np.argmax(n))
    return dict(x=x, n=n, s=s, f=f, p=f["p"], moved=moved, curve=curve,
                curve_moved=curve_moved, chi2=float(f["chi2"]), ndf=int(f["ndf"]),
                chi2_moved=chi2_moved, pulls=f["pulls"], line_beta=beta,
                line_only=line_only, pulls_line=pulls_line,
                chi2_line=float(pulls_line @ pulls_line), ndf_line=len(x) - 2, top=i)


def yearly_counts(test):
    by_year = group(PATH, 0, 4)
    return [sum(1 for t in by_year[str(y)] if test(t)) for y in YEARS]


def frost():
    return yearly_counts(lambda t: t < 0)


def warm():
    return yearly_counts(lambda t: t >= WARM)


BANDS = ["below 0 °C", "0 to 10 °C", "10 to 20 °C", "20 °C or more"]


def bands():
    """The measured hours in four temperature bands."""
    by_year = group(PATH, 0, 4)
    values = [t for v in by_year.values() for t in v]
    edges = [-math.inf, 0, 10, 20, math.inf]
    counts = [sum(1 for t in values if lo <= t < hi) for lo, hi in zip(edges, edges[1:])]
    return counts, len(values)


def lie_factor(shown_a, shown_b, data_a, data_b):
    """Tufte's lie factor: the size of the effect shown in the graphic over
    the size of the effect in the data, an effect being (b - a) / a."""
    return ((shown_b - shown_a) / shown_a) / ((data_b - data_a) / data_a)


# NOAA Global Monitoring Laboratory, annual mean CO2 at Mauna Loa (ppm),
# https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.csv, file of
# 9 Oct 2026, read 10 Nov 2026; public domain (US government); before 1974
# C. D. Keeling, Scripps. December 2022 to July 2023 measured at Maunakea
# (the eruption of Mauna Loa), as the file says.
CO2 = {
    1959: 315.98, 1960: 316.91, 1961: 317.64, 1962: 318.45, 1963: 318.99, 1964: 319.62,
    1965: 320.04, 1966: 321.37, 1967: 322.18, 1968: 323.05, 1969: 324.62, 1970: 325.68,
    1971: 326.32, 1972: 327.46, 1973: 329.68, 1974: 330.19, 1975: 331.13, 1976: 332.03,
    1977: 333.84, 1978: 335.41, 1979: 336.84, 1980: 338.76, 1981: 340.12, 1982: 341.48,
    1983: 343.15, 1984: 344.87, 1985: 346.35, 1986: 347.61, 1987: 349.31, 1988: 351.69,
    1989: 353.2, 1990: 354.45, 1991: 355.7, 1992: 356.54, 1993: 357.21, 1994: 358.96,
    1995: 360.97, 1996: 362.74, 1997: 363.88, 1998: 366.84, 1999: 368.54, 2000: 369.71,
    2001: 371.32, 2002: 373.45, 2003: 375.98, 2004: 377.7, 2005: 379.98, 2006: 382.09,
    2007: 384.02, 2008: 385.83, 2009: 387.64, 2010: 390.1, 2011: 391.85, 2012: 394.06,
    2013: 396.74, 2014: 398.81, 2015: 401.01, 2016: 404.41, 2017: 406.76, 2018: 408.72,
    2019: 411.65, 2020: 414.21, 2021: 416.41, 2022: 418.53, 2023: 421.08, 2024: 424.61,
    2025: 427.35,
}
TABLE = [1960, 1970, 1980, 1990, 2000, 2005, 2010, 2015, 2020, 2025]


# ---------------------------------------------------------------------------
# Explainers: the error bar, the fitted curve, the pulls
# ---------------------------------------------------------------------------

def _repeats():
    name = "viz_reading_repeats"
    r = repeats()
    c = r["counts"]
    k = np.arange(1, len(c) + 1)
    fig, ax = _fig(name, SIDE)
    ax.axhspan(r["lo"], r["hi"], color=style.ACCENT, alpha=0.16, lw=0)
    inside = (c >= r["lo"]) & (c <= r["hi"])
    ax.plot(k[1:][inside[1:]], c[1:][inside[1:]], "o", ms=4.5, color=style.FG)
    ax.plot(k[1:][~inside[1:]], c[1:][~inside[1:]], "o", ms=4.5, mfc="none",
            mec=style.DIM, mew=1.0)
    ax.errorbar([1], [r["first"]], yerr=[math.sqrt(r["first"])], fmt="o", ms=6,
                color=style.ACCENT, elinewidth=1.6, capsize=4, capthick=1.6, zorder=5)
    ax.annotate(rf"first 1500 rows: ${r['first']} \pm {math.sqrt(r['first']):.1f}$",
                xy=(1.6, r["hi"]), xytext=(4.5, 121), color=style.ACCENT,
                ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=style.ACCENT, lw=0.8))
    ax.text(len(c) + 0.5, 64, f"{r['inside']} of the other {r['others']} inside the bar",
            ha="right", va="bottom", color=style.FG)
    ax.set_xlim(-1, len(c) + 2)
    ax.set_ylim(60, 128)
    ax.set_xlabel("block of 1500 rows of the file")
    ax.set_ylabel(rf"pairs at {TOP_BIN[0]:.0f}–{TOP_BIN[1]:.0f} MeV/$c^2$")
    style.save(fig, name)


def _residual_panel(ax, x, n, s, curve_x, curve_y, at_x, chi2, colour, title):
    ax.plot(curve_x, curve_y, color=colour, lw=1.6, zorder=2)
    ax.vlines(x, n, at_x, color=style.BAD, lw=2.2, zorder=3)
    ax.errorbar(x, n, yerr=s, fmt="o", ms=3.6, color=style.FG, elinewidth=1.0,
                capsize=2, zorder=4)
    ax.set_title(title)
    ax.text(0.97, 0.94, rf"$\chi^2 = {chi2:.1f}$", transform=ax.transAxes,
            ha="right", va="top", fontsize=13, color=style.FG)
    ax.set_xlim(*anatomy.WINDOW)
    ax.set_ylim(0, 125)
    ax.set_xlabel(rf"mass of the $K^-\pi^+$ pair (MeV/$c^2$)")


def _chi2():
    name = "viz_reading_chi2"
    d = fit_numbers()
    x, n, s = d["x"], d["n"], d["s"]
    mm = np.linspace(*anatomy.WINDOW, 600)
    fig, (a, b) = _fig(name, WIDE, ncols=2, sharey=True)
    _residual_panel(a, x, n, s, mm, anatomy.model(mm, *d["p"]), d["curve"], d["chi2"],
                    style.CYCLE[1], "the fit")
    _residual_panel(b, x, n, s, mm, anatomy.model(mm, *d["moved"]), d["curve_moved"],
                    d["chi2_moved"], style.DIM, f"the same curve moved by {SHIFT:.0f} MeV/$c^2$")
    i = d["top"]
    a.annotate(rf"${n[i]:.0f} - {d['curve'][i]:.1f} = {n[i] - d['curve'][i]:.1f}$",
               xy=(x[i] - 0.6, (n[i] + d["curve"][i]) / 2), xytext=(1823, 112),
               ha="left", va="center", color=style.BAD,
               arrowprops=dict(arrowstyle="-", color=style.BAD, lw=0.8))
    a.set_ylabel(rf"pairs per {anatomy.BIN_W:.0f} MeV/$c^2$")
    style.save(fig, name)


def _pull_panel(ax, x, pulls, chi2, ndf, title):
    ax.axhspan(-2, 2, color=style.ACCENT, alpha=0.08, lw=0)
    ax.axhspan(-1, 1, color=style.ACCENT, alpha=0.16, lw=0)
    ax.axhline(0, color=style.DIM, lw=0.9)
    inside = np.abs(pulls) <= 2
    ax.plot(x[inside], pulls[inside], "o", ms=4.5, color=style.FG)
    ax.plot(x[~inside], pulls[~inside], "o", ms=4.5, color=style.BAD)
    ax.set_title(title)
    ax.text(0.03, 0.95, rf"$\chi^2/\mathrm{{ndf}} = {chi2:.1f}/{ndf} = {chi2 / ndf:.2f}$",
            transform=ax.transAxes, ha="left", va="top", color=style.FG)
    ax.set_xlim(*anatomy.WINDOW)
    ax.set_ylim(-4, 6)
    ax.set_yticks([-4, -2, -1, 0, 1, 2, 4, 6])
    ax.set_xlabel(rf"mass of the $K^-\pi^+$ pair (MeV/$c^2$)")


def _pulls():
    name = "viz_reading_pulls"
    d = fit_numbers()
    fig, (a, b) = _fig(name, WIDE, ncols=2, sharey=True)
    _pull_panel(a, d["x"], d["pulls"], d["chi2"], d["ndf"], "Gaussian + straight line")
    _pull_panel(b, d["x"], d["pulls_line"], d["chi2_line"], d["ndf_line"],
                "the straight line alone")
    a.set_ylabel("pull: (count − fit)/bar")
    style.save(fig, name)


# ---------------------------------------------------------------------------
# The principle of proportional ink
# ---------------------------------------------------------------------------

def _ink():
    name = "viz_reading_ink"
    fig, ax = _fig(name, SIDE, layout="none")
    fig.subplots_adjust(0, 0, 1, 1)
    w, h = fig.get_size_inches()
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect("equal")
    ax.axis("off")
    col = [w * 0.17, w * 0.5, w * 0.83]
    unit = min(w * 0.12, h * 0.26)       # the size that shows the value 1
    base = h * 0.5 - 1.25 * unit         # the shapes centred on the canvas
    blue, orange = style.ACCENT, style.CYCLE[1]
    heads = ["bar, from zero", "circle, radius ∝ value", "circle, area ∝ value"]
    inks = ["ink × 2", "ink × 4", "ink × 2"]
    for c, head, ink in zip(col, heads, inks):
        ax.text(c, base + 2.5 * unit + 0.3, head, ha="center", va="bottom", fontsize=12.5,
                color=style.FG)
        ax.text(c, base - 0.55, ink, ha="center", va="top", fontsize=14,
                color=style.BAD if ink == "ink × 4" else style.FG)
    # bars of 1 and 2
    bw = unit * 0.45
    for dx, v, colr in ((-0.33, 1, blue), (0.33, 2, orange)):
        ax.add_patch(Rectangle((col[0] + dx * unit * 1.6 - bw / 2, base), bw, v * unit * 1.25,
                               **_paper(colr)))
        ax.text(col[0] + dx * unit * 1.6, base - 0.12, str(v), ha="center", va="top",
                color=style.FG)
    # circles: radius doubled, then area doubled
    for c, scale in ((col[1], 2.0), (col[2], math.sqrt(2))):
        r1 = unit * 0.42
        for dx, rr, colr, v in ((-0.66, r1, blue, 1), (0.42, r1 * scale, orange, 2)):
            cx = c + dx * unit * 1.25
            ax.add_patch(Circle((cx, base + rr), rr, **_paper(colr)))
            ax.text(cx, base - 0.12, str(v), ha="center", va="top", color=style.FG)
    style.save(fig, name, tight=False)


# ---------------------------------------------------------------------------
# Frost hours: circles sized by radius, then bars
# ---------------------------------------------------------------------------

def _circles_bad():
    name = "viz_reading_circles_bad"
    counts = frost()
    fig, ax = _fig(name, SIDE, layout="none")
    fig.subplots_adjust(0, 0, 1, 1)
    w, h = fig.get_size_inches()
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect("equal")
    ax.axis("off")
    cell_w, cell_h = w / 5, (h - 0.55) / 2
    rmax = min(cell_w, cell_h - 0.55) / 2 * 0.96
    for k, (year, count) in enumerate(zip(YEARS, counts)):
        row, col = divmod(k, 5)
        cx = (col + 0.5) * cell_w
        top = h - 0.55 - row * cell_h
        r = rmax * count / max(counts)
        cy = top - 0.04 - rmax
        ax.add_patch(Circle((cx, cy), r, **_paper(style.ACCENT, 0.55)))
        ax.text(cx, cy - rmax - 0.08, f"{year}: {style.thousands(count)}", ha="center",
                va="top", fontsize=12, color=style.FG)
    ax.text(w / 2, h - 0.12, "Hours below 0 °C, 2016–2025", ha="center", va="top",
            fontsize=14, color=style.BAD)
    style.save(fig, name, tight=False)


def _frost_bars():
    name = "viz_reading_frost_bars"
    counts = frost()
    fig, ax = _fig(name, SIDE)
    ax.bar(YEARS, counts, width=0.7, **_paper(style.ACCENT))
    for y in (2023, 2025):
        v = counts[YEARS.index(y)]
        ax.text(y, v + 60, style.thousands(v), ha="center", va="bottom", color=style.FG)
    ax.set_xticks(YEARS[::3])
    ax.set_ylim(0, 3000)
    ax.set_xlabel("year")
    ax.set_ylabel("hours below 0 °C")
    style.save(fig, name)


# ---------------------------------------------------------------------------
# Four temperature bands: a pie in perspective, then bars
# ---------------------------------------------------------------------------

PIE_COLOURS = [style.ACCENT, style.CYCLE[2], style.CYCLE[1], style.CYCLE[6]]
TILT = math.radians(28)      # the camera above the plane of the pie
DIST = 3.2                   # its distance, in radii
DEPTH = 0.32                 # the thickness of the pie, in radii
FRONT = 0                    # the band whose wedge faces the camera


def _camera():
    eye = np.array([0.0, -DIST * math.cos(TILT), DIST * math.sin(TILT)])
    fwd = -eye / np.linalg.norm(eye)
    right = np.array([1.0, 0.0, 0.0])
    up = np.cross(right, fwd)
    return eye, fwd, right, up


def _project(p):
    eye, fwd, right, up = _camera()
    v = np.asarray(p) - eye
    z = v @ fwd
    return DIST * np.array([v @ right / z, v @ up / z])   # the radius about 1


def _arc(a0, a1, z=0.0, k=60):
    return [(math.cos(a), math.sin(a), z) for a in np.linspace(a0, a1, k)]


def _shoelace(pts):
    pts = np.asarray(pts)
    x, y = pts[:, 0], pts[:, 1]
    return 0.5 * abs(x @ np.roll(y, -1) - y @ np.roll(x, -1))


def pie3d():
    """The wedges of the pie in perspective: for each band its angles, the
    projected top face and the visible part of its rim, and their areas."""
    counts, total = bands()
    shares = [c / total for c in counts]
    centre = -math.pi / 2                       # the front of the pie
    a0 = centre - math.pi * shares[FRONT]       # FRONT centred on the front
    eye = _camera()[0]
    out = []
    for i, share in enumerate(shares):
        a1 = a0 + 2 * math.pi * share
        top = [_project((0, 0, 0))] + [_project(p) for p in _arc(a0, a1)]
        rim = []
        for a in np.linspace(a0, a1, 240):     # the rim where it faces the camera
            p = np.array([math.cos(a), math.sin(a), 0.0])
            if p @ (eye - p) > 0 and math.sin(a) < 0:
                rim.append(a)
        rim_poly = []
        if rim:
            upper = [_project((math.cos(a), math.sin(a), 0)) for a in rim]
            lower = [_project((math.cos(a), math.sin(a), -DEPTH)) for a in rim[::-1]]
            rim_poly = upper + lower
        out.append(dict(band=BANDS[i], count=counts[i], share=share, a0=a0, a1=a1,
                        top=top, rim=rim_poly, area_top=_shoelace(top),
                        area_rim=_shoelace(rim_poly) if rim_poly else 0.0))
        a0 = a1
    ink = sum(w["area_top"] + w["area_rim"] for w in out)
    for wdg in out:
        wdg["ink"] = (wdg["area_top"] + wdg["area_rim"]) / ink
    return out


def _pie3d_bad():
    name = "viz_reading_pie3d_bad"
    wedges = pie3d()
    fig, ax = _fig(name, SIDE, layout="none")
    fig.subplots_adjust(0.02, 0.02, 0.98, 0.9)
    ax.set_aspect("equal")
    ax.axis("off")
    for wdg, colour in zip(wedges, PIE_COLOURS):
        if wdg["rim"]:
            ax.add_patch(Polygon(wdg["rim"], closed=True, facecolor=to_rgba(colour, 0.35),
                                 edgecolor=colour, lw=0.8))
    for wdg, colour in zip(wedges, PIE_COLOURS):
        ax.add_patch(Polygon(wdg["top"], closed=True, facecolor=to_rgba(colour, 0.6),
                             edgecolor=style.BG, lw=1.2))
    for wdg in wedges:
        mid = (wdg["a0"] + wdg["a1"]) / 2
        r = 1.18 if math.sin(mid) > 0 else 1.0
        x, y = _project((r * math.cos(mid), r * math.sin(mid), 0))
        if math.sin(mid) < 0:
            y = _project((math.cos(mid), math.sin(mid), -DEPTH))[1] - 0.06
        ha = "center" if abs(math.cos(mid)) < 0.35 else ("left" if math.cos(mid) > 0 else "right")
        ax.text(x, y, wdg["band"], ha=ha, va="top" if math.sin(mid) < 0 else "bottom",
                fontsize=12, color=style.FG)
    pts = np.vstack([np.asarray(w["top"]) for w in wedges] +
                    [np.asarray(w["rim"]) for w in wedges if w["rim"]])
    ax.set_xlim(pts[:, 0].min() - 0.95, pts[:, 0].max() + 0.75)
    ax.set_ylim(pts[:, 1].min() - 0.16, pts[:, 1].max() + 0.1)
    fig.suptitle("The hours of ten years by temperature", color=style.BAD, fontsize=14)
    style.save(fig, name, tight=False)


def _bands_bars():
    name = "viz_reading_bands_bars"
    counts, total = bands()
    fig, ax = _fig(name, SIDE)
    pct = [100 * c / total for c in counts]
    xs = range(len(BANDS))
    ax.bar(xs, pct, width=0.62, **_paper(style.ACCENT))
    for x, p in zip(xs, pct):
        ax.text(x, p + 0.8, f"{p:.1f} %", ha="center", va="bottom", color=style.FG)
    ax.set_xticks(list(xs), BANDS)
    ax.set_ylim(0, 40)
    ax.set_ylabel("share of the 87 552 hours (%)")
    style.save(fig, name)


# ---------------------------------------------------------------------------
# Warm hours: a running total, then year by year
# ---------------------------------------------------------------------------

def _running_total_bad():
    name = "viz_reading_running_total_bad"
    counts = warm()
    total = np.cumsum(counts)
    fig, ax = _fig(name, SIDE)
    ax.fill_between(YEARS, 0, total, color=style.BAD, alpha=0.22, lw=0)
    ax.plot(YEARS, total, "o-", color=style.BAD)
    ax.set_xticks(YEARS[::3])
    ax.set_ylim(0, 8000)
    ax.yaxis.set_major_formatter(style.ThousandsFormatter())
    ax.set_xlabel("year")
    ax.set_ylabel("hours of 20 °C or more, since 2016")
    ax.set_title("Warm hours rise every year", color=style.BAD)
    style.save(fig, name)


def _warm_hours():
    name = "viz_reading_warm_hours"
    counts = warm()
    fig, ax = _fig(name, SIDE)
    ax.bar(YEARS, counts, width=0.7, **_paper(style.ACCENT))
    for y in (2023, 2024):
        v = counts[YEARS.index(y)]
        ax.text(y, v + 15, str(v), ha="center", va="bottom", color=style.FG)
    ax.set_xticks(YEARS[::3])
    ax.set_ylim(0, 1200)
    ax.set_xlabel("year")
    ax.set_ylabel("hours of 20 °C or more")
    style.save(fig, name)


# ---------------------------------------------------------------------------
# CO2: years as equal steps, then at their distance
# ---------------------------------------------------------------------------

def _co2_axes(ax):
    ax.set_ylim(305, 440)
    ax.set_ylabel(r"CO$_2$ at Mauna Loa (ppm)")


def _co2_steps_bad():
    name = "viz_reading_co2_steps_bad"
    fig, ax = _fig(name, SIDE)
    labels = [str(y) for y in TABLE]
    ax.plot(labels, [CO2[y] for y in TABLE], "o-", color=style.BAD)
    ax.set_xlabel("year")
    _co2_axes(ax)
    style.save(fig, name)


def _co2_years():
    name = "viz_reading_co2_years"
    fig, ax = _fig(name, SIDE)
    years = sorted(CO2)
    ax.plot(years, [CO2[y] for y in years], color=style.DIM, lw=1.0, label="every year")
    ax.plot(TABLE, [CO2[y] for y in TABLE], "o-", color=style.ACCENT, label="the ten years")
    ax.set_xlim(1955, 2030)
    ax.set_xlabel("year")
    ax.legend(loc="upper left")
    _co2_axes(ax)
    style.save(fig, name)


FIGURES = {
    "viz_reading_repeats": _repeats,
    "viz_reading_chi2": _chi2,
    "viz_reading_pulls": _pulls,
    "viz_reading_ink": _ink,
    "viz_reading_circles_bad": _circles_bad,
    "viz_reading_frost_bars": _frost_bars,
    "viz_reading_pie3d_bad": _pie3d_bad,
    "viz_reading_bands_bars": _bands_bars,
    "viz_reading_running_total_bad": _running_total_bad,
    "viz_reading_warm_hours": _warm_hours,
    "viz_reading_co2_steps_bad": _co2_steps_bad,
    "viz_reading_co2_years": _co2_years,
}


if __name__ == "__main__":
    r = repeats()
    print(f"error bar: {r['rows']} rows, {r['blocks']} blocks of {BLOCK}; top bin "
          f"{TOP_BIN[0]:.0f}-{TOP_BIN[1]:.0f}: first block {r['first']} +- "
          f"{math.sqrt(r['first']):.2f} ({r['lo']:.1f} to {r['hi']:.1f}); blocks "
          f"{r['counts'].min()} to {r['counts'].max()}, mean {r['mean']:.2f}, sd "
          f"{r['sd']:.2f}, sqrt(mean) {math.sqrt(r['mean']):.2f}; {r['inside']} of the "
          f"other {r['others']} inside ({100 * r['inside'] / r['others']:.0f} %)")
    d = fit_numbers()
    i = d["top"]
    pull = (d["n"][i] - d["curve"][i]) / d["s"][i]
    print(f"top bin {d['x'][i]}: n {d['n'][i]:.0f}, fit {d['curve'][i]:.2f}, bar "
          f"{d['s'][i]:.3f}, pull {pull:+.3f}, pull^2 {pull ** 2:.3f}")
    print(f"chi2 fit {d['chi2']:.2f} / {d['ndf']} = {d['chi2'] / d['ndf']:.3f}; moved by "
          f"{SHIFT}: {d['chi2_moved']:.2f}; line alone {d['chi2_line']:.2f} / "
          f"{d['ndf_line']} = {d['chi2_line'] / d['ndf_line']:.2f}, largest pull "
          f"{d['pulls_line'].max():+.2f} at {d['x'][np.argmax(d['pulls_line'])]}")
    p = d["pulls"]
    print(f"pulls of the fit: {(np.abs(p) < 1).sum()} of {len(p)} within 1, "
          f"{(np.abs(p) < 2).sum()} within 2, largest |pull| {np.abs(p).max():.2f}; "
          f"line alone: {(np.abs(d['pulls_line']) > 2).sum()} beyond 2")
    pr = [58.2, 49.1]
    print(f"pass rates: lie factor from 48: "
          f"{lie_factor(pr[1] - 48, pr[0] - 48, pr[1], pr[0]):.1f}; from 0: "
          f"{lie_factor(pr[1], pr[0], pr[1], pr[0]):.2f}; data effect "
          f"{(pr[0] - pr[1]) / pr[1]:.3f}, bars {(pr[0] - 48 - (pr[1] - 48)) / (pr[1] - 48):.2f}")
    fr = frost()
    print("frost hours", dict(zip(YEARS, fr)))
    a, b = fr[YEARS.index(2023)], fr[YEARS.index(2025)]
    print(f"2023 {a}, 2025 {b}: ratio {b / a:.3f}; radius ratio {b / a:.3f} -> area "
          f"{(b / a) ** 2:.3f}; lie factor {lie_factor(a ** 2, b ** 2, a, b):.2f}")
    wm = warm()
    cum = np.cumsum(wm)
    print("warm hours", dict(zip(YEARS, wm)), "running total", list(cum))
    j = YEARS.index(2024)
    print(f"2023 -> 2024: {wm[j - 1]} -> {wm[j]} ({100 * (wm[j] - wm[j - 1]) / wm[j - 1]:+.1f} %);"
          f" running total {cum[j - 1]} -> {cum[j]} ({100 * (cum[j] - cum[j - 1]) / cum[j - 1]:+.1f} %);"
          f" lie factor {lie_factor(cum[j - 1], cum[j], wm[j - 1], wm[j]):.2f}")
    counts, total = bands()
    for wdg in pie3d():
        print(f"pie: {wdg['band']:>14}: {wdg['count']} hours, {100 * wdg['share']:.1f} %, "
              f"ink {100 * wdg['ink']:.1f} % (top {wdg['area_top']:.3f}, rim {wdg['area_rim']:.3f})")
    pw = pie3d()
    front, back = pw[0], max(pw, key=lambda w: math.sin((w["a0"] + w["a1"]) / 2))
    print(f"front {front['band']} vs back {back['band']}: lie factor "
          f"{lie_factor(front['ink'], back['ink'], front['share'], back['share']):.2f}")
    print("CO2", {y: CO2[y] for y in TABLE})
    for y0, y1 in zip(TABLE, TABLE[1:]):
        print(f"  {y0}-{y1}: +{CO2[y1] - CO2[y0]:.2f} ppm, {(CO2[y1] - CO2[y0]) / (y1 - y0):.2f} ppm/yr")
    s0, s1 = CO2[2000] - CO2[1990], CO2[2005] - CO2[2000]
    r0, r1 = s0 / 10, s1 / 5
    print(f"step 1990-2000 {s0:.2f}, 2000-2005 {s1:.2f} (drawn x{s1 / s0:.3f}); rate {r0:.3f} -> "
          f"{r1:.3f} ppm/yr (x{r1 / r0:.3f}); lie factor {lie_factor(s0, s1, r0, r1):.2f}")
