"""Advanced plots of many variables: the section For the Curious of Lecture 7,
after its Recap.

- `viz_advanced_contours`: four variables on one plane. The ten-year mean
  temperature of each day of the year (x) and hour of the day (y) as colour,
  the mean humidity of the same cells as contour lines.
- `viz_advanced_slices`: four variables in 3D. Every measured hour of the ten
  years, one plane per year stacked upwards: day across, hour in depth,
  temperature as colour.
- `viz_advanced_multiples`: the same 87 552 hours as ten flat panels, one per
  year, on one colour scale: the same four variables, nothing hidden.
- `viz_advanced_parallel`: five variables of each day as parallel
  coordinates: daily mean temperature, daily range, humidity, wind, and the
  month as colour.
- `viz_advanced_corner`: the four columns of the LHCb file `D0_KPi.csv` as a
  corner plot: every pair as a 2D histogram, every column alone on the
  diagonal.

The weather figures read `weather.csv` with the functions of beyond.py (the
lecture's `weather.py` with the column as a parameter); the 120 hours of
22-26 July 2019 with temperature -999 are left out.

    python figures/src/advanced.py

prints every number the slides state.
"""
import calendar
from datetime import date

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import BoundaryNorm, LogNorm, Normalize

import style
from beyond import (BG, CRISP, D0, HUMIDITY, MONTHS, PATH, TEMP, WIND, PlaneCells,
                    _dark_3d, _month_starts, _season_cmap, _temp_norm, as_cells,
                    daily_means, day_hour_grid, finish, group, mean, vector_colorbar)

SIZE = (9.4, 3.3)
YEARS = list(range(2016, 2026))
HOURS = ["00:00", "06:00", "12:00", "18:00"]

# Humidity contours: the cell means (10 hours each) are noisy, so each hour's
# row is smoothed with a running mean of SMOOTH days that wraps from December
# to January.
SMOOTH = 15
HUM_LEVELS = [70, 80, 90]

# The 3D slices: view, box aspect, zoom, Axes rect and colorbar x, as in
# beyond.py (a 3D Axes is placed by hand and saved on its full canvas).
SLICE_SIZE = (9.4, 3.9)
VIEW_SL, BOX_SL, ZOOM_SL = (22, -64), (3.6, 1.2, 1.9), 1.2
AX_SL, CBAR_SL = [-0.03, 0.07, 0.88, 0.98], 0.8

# The corner plot: each column, its label, the transform drawn and the range.
# TAU is in ns in the file; 49 rows carry -100, a missing value, and are left
# out of the panels that use TAU. IPCHI2 spans eight decades: log10.
CORNER = [
    ("M", r"$M$ (MeV/$c^2$)", lambda v: v, (1810, 1920)),
    ("PT", r"$p_\mathrm{T}$ (GeV/$c$)", lambda v: v / 1000, (2.5, 9)),
    ("TAU", r"$\tau$ (ps)", lambda v: v * 1000, (0, 3)),
    ("IPCHI2", r"$\log_{10}\chi^2_\mathrm{IP}$", np.log10, (-1.5, 4.5)),
]
CORNER_BINS = 55
SIGNAL = (1845, 1885)                      # MeV/c^2, about +-20 around 1865
SIDEBANDS = ((1810, 1830), (1900, 1920))   # 40 MeV/c^2 of background


# ---------------------------------------------------------------------------
# The data
# ---------------------------------------------------------------------------

def humidity_grid(days):
    """Mean humidity per (hour, day of year), on the days of day_hour_grid."""
    cells = group(PATH, 5, 13, HUMIDITY)
    grid = np.full((24, len(days)), np.nan)
    for col, day in enumerate(days):
        for hour in range(24):
            key = f"{day}T{hour:02d}"
            if key in cells:
                grid[hour, col] = mean(cells[key])
    return grid


def smooth_days(grid, width=SMOOTH):
    """Running mean along the days, wrapping around the year."""
    half = width // 2
    padded = np.concatenate([grid[:, -half:], grid, grid[:, :half]], axis=1)
    kernel = np.ones(width) / width
    return np.array([np.convolve(row, kernel, mode="valid") for row in padded])


def year_grids():
    """Every measured hour: {year: 24 x (365 or 366) array}, NaN where no hour.

    Column i is day i of that year, 1 January = 0, so a leap year has one
    column more and its days after 28 February sit one column later.
    """
    grids = {y: np.full((24, 366 if calendar.isleap(y) else 365), np.nan) for y in YEARS}
    for line in open(PATH).read().splitlines()[1:]:
        t = float(line.split(",")[TEMP])
        if t == -999.0:
            continue
        day = date(int(line[0:4]), int(line[5:7]), int(line[8:10])).timetuple().tm_yday - 1
        grids[int(line[0:4])][int(line[11:13]), day] = t
    return grids


# 1 January = day 0 in a year of 365 days.
MONTH_DAYS = [date(2017, m, 1).timetuple().tm_yday - 1 for m in range(1, 13)]


def daily_ranges():
    """Daily mean temperature, max - min, humidity, wind and month.

    Only days with all 24 hours measured, so the range covers a whole day."""
    temp = group(PATH, 0, 10, TEMP)
    hum = group(PATH, 0, 10, HUMIDITY)
    wind = group(PATH, 0, 10, WIND)
    days = [d for d in temp if len(temp[d]) == 24]
    return (days,
            np.array([mean(temp[d]) for d in days]),
            np.array([max(temp[d]) - min(temp[d]) for d in days]),
            np.array([mean(hum[d]) for d in days]),
            np.array([mean(wind[d]) for d in days]),
            np.array([int(d[5:7]) for d in days]))


def d0_table():
    return np.loadtxt(D0, delimiter=",", skiprows=1)


# ---------------------------------------------------------------------------
# 1. Temperature as colour, humidity as contour lines
# ---------------------------------------------------------------------------

def _contours():
    days, temp = day_hour_grid()
    hum = smooth_days(humidity_grid(days))
    fig, ax = plt.subplots(figsize=SIZE)
    im = ax.imshow(temp, aspect="auto", origin="lower", cmap="RdBu_r",
                   norm=_temp_norm(temp), interpolation="none")
    as_cells(im, "temperature")
    cs = ax.contour(np.arange(len(days)), np.arange(24), hum, levels=HUM_LEVELS,
                    colors=BG, linewidths=1.4)
    ax.clabel(cs, fmt="%d %%", fontsize=11, inline_spacing=6)
    vector_colorbar(fig.colorbar(im, ax=ax, label="mean temperature (°C)", pad=0.015))
    ax.set_xticks(_month_starts(days), MONTHS)
    ax.set_yticks([0, 6, 12, 18], HOURS)
    ax.set(xlabel="day of the year", ylabel="hour of the day")
    ax.grid(False)
    style.save(fig, "viz_advanced_contours")
    finish("viz_advanced_contours")


# ---------------------------------------------------------------------------
# 2. Ten years stacked in 3D
# ---------------------------------------------------------------------------

def _slices():
    grids = year_grids()
    norm = Normalize(-30, 30)
    cmap = plt.get_cmap("RdBu_r")
    fig = plt.figure(figsize=SLICE_SIZE, layout="none")
    ax = fig.add_axes(AX_SL, projection="3d")
    below = []
    for year in YEARS:
        g = grids[year]
        colours = cmap(norm(g), bytes=True)
        colours[np.isnan(g)] = 0                  # an hour not measured: a hole
        x, y = np.meshgrid(np.arange(g.shape[1] + 1), np.arange(25))
        had_data = ax.has_data()
        # each year a plane of vector cells: its outline smooth, its cells
        # crisp; the cells hidden under the plane above are left out
        plane = [PlaneCells(x[0], y[:, 0], year, colours, outline=True, clip_on=False),
                 PlaneCells(x[0], y[:, 0], year, colours, clip_on=False, gid=CRISP + str(year))]
        for p in plane:
            ax.add_collection(p, autolim=False)
        for p in below:
            p.above = plane[1]
        below = plane
        ax.auto_scale_xyz(x, y, np.full(x.shape, year), had_data)   # as plot_surface does
    sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    vector_colorbar(fig.colorbar(sm, cax=fig.add_axes([CBAR_SL, 0.2, 0.012, 0.6]),
                                 label="temperature (°C)"))
    ax.view_init(elev=VIEW_SL[0], azim=VIEW_SL[1])
    ax.set_box_aspect(BOX_SL, zoom=ZOOM_SL)
    ax.set_xticks(MONTH_DAYS[::3], MONTHS[::3])
    ax.set_yticks([0, 12, 24], ["00:00", "12:00", "24:00"])
    ax.set_zticks(YEARS[::3])
    ax.set_zlim(YEARS[0], YEARS[-1])
    ax.set_xlabel("day of the year", labelpad=8)
    ax.set_ylabel("hour", labelpad=2)
    ax.set_zlabel("year", labelpad=8)
    _dark_3d(ax)
    style.save(fig, "viz_advanced_slices", tight=False)
    finish("viz_advanced_slices")


# ---------------------------------------------------------------------------
# 3. The same hours as ten panels
# ---------------------------------------------------------------------------

def _multiples():
    grids = year_grids()
    norm = Normalize(-30, 30)
    fig, axs = plt.subplots(2, 5, figsize=SIZE, sharex=True, sharey=True)
    for ax, year in zip(axs.flat, YEARS):
        g = grids[year]
        im = ax.imshow(g, aspect="auto", origin="lower", cmap="RdBu_r", norm=norm,
                       interpolation="none", extent=(0, g.shape[1], 0, 24))
        as_cells(im, str(year))
        ax.set_title(str(year), fontsize=11, pad=3)
        ax.grid(False)
    for ax in axs[1]:
        ax.set_xticks(MONTH_DAYS[::3], MONTHS[::3])
    for ax in axs[:, 0]:
        ax.set_yticks([0, 12], ["00:00", "12:00"])
    vector_colorbar(fig.colorbar(im, ax=axs, label="temperature (°C)", pad=0.015, aspect=25))
    style.save(fig, "viz_advanced_multiples")
    finish("viz_advanced_multiples")


# ---------------------------------------------------------------------------
# 4. Parallel coordinates: five variables of each day
# ---------------------------------------------------------------------------

PARALLEL = [  # (label, index into daily_ranges, ticks)
    ("daily range (°C)", 2, [0, 5, 10, 15]),
    ("mean temperature (°C)", 1, [-15, -5, 5, 15, 25]),
    ("humidity (%)", 3, [40, 60, 80, 100]),
    ("wind (m/s)", 4, [0, 2, 4, 6, 8]),
]


def _parallel():
    data = daily_ranges()
    month = data[5]
    cols = [data[i] for _, i, _ in PARALLEL]
    lims = [(min(t[0], c.min()), max(t[-1], c.max())) for (_, _, t), c in zip(PARALLEL, cols)]
    scaled = np.column_stack([(c - lo) / (hi - lo) for c, (lo, hi) in zip(cols, lims)])
    xs = np.arange(len(PARALLEL))
    order = np.random.default_rng(7).permutation(len(month))   # no month on top
    segs = [np.column_stack([xs, scaled[k]]) for k in order]
    month = month[order]
    cmap = _season_cmap()
    norm = BoundaryNorm(np.arange(0.5, 13), cmap.N)

    fig, ax = plt.subplots(figsize=SIZE)
    lc = LineCollection(segs, cmap=cmap, norm=norm, linewidths=0.35, alpha=0.3)
    lc.set_array(month)
    ax.add_collection(lc)
    for x, ((label, _, ticks), (lo, hi)) in enumerate(zip(PARALLEL, lims)):
        ax.plot([x, x], [0, 1], color=style.FG, linewidth=1.2, zorder=3)
        for t in ticks:
            yv = (t - lo) / (hi - lo)
            ax.plot([x - 0.025, x], [yv, yv], color=style.FG, linewidth=1.2, zorder=3)
            ax.text(x - 0.04, yv, f"{t}".replace("-", "−"), ha="right",
                    va="center", fontsize=10, color=style.FG, zorder=4,
                    bbox=dict(boxstyle="round,pad=0.15", fc=BG, ec="none", alpha=0.85))
        ax.text(x, 1.05, label, ha="center", va="bottom", fontsize=12, color=style.FG)
    ax.set(xlim=(-0.3, len(PARALLEL) - 0.8), ylim=(-0.03, 1.13))
    ax.axis("off")
    bar = fig.colorbar(lc, ax=ax, label="month", pad=0.01)
    bar.set_ticks(range(1, 13), labels=MONTHS)
    bar.ax.tick_params(labelsize=9)
    bar.solids.set_alpha(1)
    vector_colorbar(bar)
    style.save(fig, "viz_advanced_parallel")
    finish("viz_advanced_parallel")


# ---------------------------------------------------------------------------
# 5. The corner plot of the LHCb file
# ---------------------------------------------------------------------------

def _corner_columns():
    d = d0_table()
    keep = d[:, 2] != -100
    return [f(d[keep, i]) for i, (_, _, f, _) in enumerate(CORNER)]


def _corner():
    cols = _corner_columns()
    n = len(CORNER)
    size = style.SIZES.get("viz_advanced_corner", (6.2, 4.3))
    fig, axs = plt.subplots(n, n, figsize=size)
    for i in range(n):
        for j in range(n):
            ax = axs[i, j]
            if j > i:
                ax.set_visible(False)
                continue
            ax.grid(False)
            if i == j:
                ax.hist(cols[i], bins=CORNER_BINS, range=CORNER[i][3],
                        histtype="stepfilled", color=style.ACCENT)
                ax.set_yticks([])
                ax.spines["left"].set_visible(False)
            else:
                *_, im = ax.hist2d(cols[j], cols[i], bins=CORNER_BINS,
                                   range=[CORNER[j][3], CORNER[i][3]],
                                   cmap="viridis", norm=LogNorm(vmin=1, vmax=1000))
                as_cells(im, f"{i}{j}")
            ax.set_xlim(CORNER[j][3])
            if i == n - 1:
                ax.set_xlabel(CORNER[j][1], fontsize=10)
            else:
                ax.tick_params(labelbottom=False)
            if j == 0 and i > 0:
                ax.set_ylabel(CORNER[i][1], fontsize=10)
            elif i != j:
                ax.tick_params(labelleft=False)
            ax.tick_params(labelsize=8)
    axs[0, 2].set_visible(True)
    axs[0, 2].axis("off")
    cax = axs[0, 2].inset_axes([0.25, 0.35, 1.7, 0.14])
    vector_colorbar(fig.colorbar(im, cax=cax, orientation="horizontal",
                                 label="candidates per bin"))
    style.save(fig, "viz_advanced_corner")
    finish("viz_advanced_corner")


# ---------------------------------------------------------------------------
# 6. The four-variable scatter, turning
# ---------------------------------------------------------------------------

FIGURES = {
    "viz_advanced_contours": _contours,
    "viz_advanced_slices": _slices,
    "viz_advanced_multiples": _multiples,
    "viz_advanced_parallel": _parallel,
    "viz_advanced_corner": _corner,
}


# ---------------------------------------------------------------------------
# Every number a slide might state
# ---------------------------------------------------------------------------

def _report():
    days, temp = day_hour_grid()
    raw = humidity_grid(days)
    hum = smooth_days(raw)
    print("1. contours: humidity cells (raw)", f"{np.nanmin(raw):.1f} to {np.nanmax(raw):.1f} %;",
          f"smoothed over {SMOOTH} days {np.nanmin(hum):.1f} to {np.nanmax(hum):.1f} %")
    lo = np.unravel_index(np.nanargmin(hum), hum.shape)
    hi = np.unravel_index(np.nanargmax(hum), hum.shape)
    print(f"  driest smoothed cell {days[lo[1]]} {lo[0]:02d}:00 {hum[lo]:.1f} % "
          f"(temperature {temp[lo]:.1f} °C); wettest {days[hi[1]]} {hi[0]:02d}:00 {hum[hi]:.1f} %")
    for mm in ("01", "07"):
        c = [i for i, d in enumerate(days) if d.startswith(mm)]
        prof = np.nanmean(raw[:, c], axis=1)
        print(f"  month {mm}: humidity {prof.min():.1f} % at {prof.argmin():02d}:00, "
              f"{prof.max():.1f} % at {prof.argmax():02d}:00")
    ok = ~np.isnan(temp) & ~np.isnan(raw)
    print(f"  r(cell temperature, cell humidity) = {np.corrcoef(temp[ok], raw[ok])[0, 1]:.2f}")

    grids = year_grids()
    days = [date.fromordinal(date(2017, 1, 1).toordinal() + i).strftime("%m-%d") for i in range(366)]
    cells = sum(int((~np.isnan(g)).sum()) for g in grids.values())
    print("2-3. slices / multiples:", sum(g.size for g in grids.values()),
          "hours in ten years,", cells, "measured (day labels: non-leap calendar)")
    for y in YEARS:
        g = grids[y]
        i = np.unravel_index(np.nanargmin(g), g.shape)
        j = np.unravel_index(np.nanargmax(g), g.shape)
        print(f"  {y}: {int((~np.isnan(g)).sum())} h, min {g[i]:.1f} on {days[i[1]]} {i[0]:02d}:00, "
              f"max {g[j]:.1f} on {days[j[1]]} {j[0]:02d}:00, mean {np.nanmean(g):.2f}")

    d, t, rng, h, w, m = daily_ranges()
    print("4. parallel:", len(d), "days with 24 measured hours")
    print(f"  range {rng.min():.1f} to {rng.max():.1f}; temp {t.min():.1f} to {t.max():.1f}; "
          f"humidity {h.min():.1f} to {h.max():.1f}; wind {w.min():.2f} to {w.max():.2f}")
    names = ["range", "temp", "humidity", "wind"]
    vals = [rng, t, h, w]
    for a in range(4):
        for b in range(a + 1, 4):
            print(f"  r({names[a]}, {names[b]}) = {np.corrcoef(vals[a], vals[b])[0, 1]:.2f}")
    for label, sel in (("calm, wind < 2 m/s", w < 2), ("windy, wind > 5 m/s", w > 5)):
        print(f"  {label}: {sel.sum()} days, mean range {rng[sel].mean():.1f} °C, "
              f"humidity {h[sel].mean():.1f} %")
    for mm in (1, 7):
        sel = m == mm
        print(f"  {calendar.month_name[mm]}: mean range {rng[sel].mean():.1f} °C, "
              f"humidity {h[sel].mean():.1f} %, wind {w[sel].mean():.2f}")

    tab = d0_table()
    print("5. corner:", len(tab), "candidates;", int((tab[:, 2] == -100).sum()), "with TAU = -100 left out")
    cols = _corner_columns()
    M, PT, TAU, LIP = cols
    for (name, _, _, r), c in zip(CORNER, cols):
        print(f"  {name}: in range {((c >= r[0]) & (c <= r[1])).sum()} of {len(c)}")
    sig = (M >= SIGNAL[0]) & (M < SIGNAL[1])
    side = ((M >= SIDEBANDS[0][0]) & (M < SIDEBANDS[0][1])) | ((M >= SIDEBANDS[1][0]) & (M < SIDEBANDS[1][1]))
    bkg_in_sig = side.sum() * (SIGNAL[1] - SIGNAL[0]) / 40
    print(f"  signal window {SIGNAL}: {sig.sum()}; sidebands (40 MeV): {side.sum()}, "
          f"so about {bkg_in_sig:.0f} background in the window, {sig.sum() - bkg_in_sig:.0f} D0")
    for label, sel in (("window", sig), ("sidebands", side)):
        print(f"  {label}: median tau {np.median(TAU[sel]):.3f} ps, mean tau (0-3 ps) "
              f"{TAU[sel & (TAU > 0) & (TAU < 3)].mean():.3f} ps, median log10 IPCHI2 "
              f"{np.median(LIP[sel]):.2f}, median PT {np.median(PT[sel]):.2f} GeV/c, "
              f"share with log10 IPCHI2 > 2: {(LIP[sel] > 2).mean():.2f}")
    allp = ["M", "PT", "TAU", "IPCHI2"]
    for a in range(4):
        for b in range(a + 1, 4):
            print(f"  r({allp[a]}, {allp[b]}) = {np.corrcoef(cols[a], cols[b])[0, 1]:.2f}")


if __name__ == "__main__":
    _report()
