"""Emphasis family: overplotting, fake-3D, redundant coding, label sizes.

Nine figures, each making one narrow pedagogical point from the "Emphasis"
section of the data-viz lecture:
  - big scatter clouds need binning, not more dots (overplotting -> hexbin)
  - moderate overplot has three cheap fixes: raw / jitter+alpha / density
  - fake-3D bar charts distort the very magnitudes they're meant to show
  - a legend forces eye travel; direct end-of-line labels don't
  - tick/axis-label font size is a legibility choice, not a style flourish

All synthetic (fixed seeds) — no dataset ships raw flight, stock or athlete
records that fit these exact stories, so we build minimal stand-ins with the
right shape (skew, correlation, near-equal magnitudes) instead of forcing a
seaborn dataset to say something it doesn't.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (registers 3D projection)

import style

RNG = np.random.default_rng(2024)

# Single-hue sequential ramp for hex/density bins: near-invisible on the dark
# canvas at low count, up to full course-cyan at the top of the range.
SEQ_CMAP = LinearSegmentedColormap.from_list("course_seq", ["#111a26", style.ACCENT])


def _style_3d_axes(ax) -> None:
    """Dark styling for the bits of a 3D axes rcParams doesn't reach."""
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.set_facecolor((0, 0, 0, 0))
        axis.pane.set_edgecolor(style.GRID)
        axis.line.set_color(style.DIM)
        axis._axinfo["grid"]["color"] = style.GRID
        axis._axinfo["grid"]["linewidth"] = 0.5
    ax.tick_params(colors=style.DIM)


# ---------------------------------------------------------------------------
# 1-2. Overplotting at scale: raw scatter vs hex bins
# ---------------------------------------------------------------------------

def _flight_delays(n: int = 20_000):
    """Departure/arrival delay in minutes: a busy day at a busy airport.
    Most flights leave close to on time; a long right tail runs late; a late
    departure drags the arrival late with it. This is exactly the shape that
    turns a 20k-point scatter into a solid blob near the origin.
    """
    rng = np.random.default_rng(2101)  # local: paired figures must share identical data
    dep = rng.gamma(shape=1.6, scale=11.0, size=n) - 12.0
    arr = 0.92 * dep + rng.normal(0, 14, n)
    return dep, arr


def _overplot_points():
    dep, arr = _flight_delays()
    fig, ax = style.new_fig(7, 5)
    fig.set_dpi(150)  # rasterized point cloud needs real resolution
    ax.scatter(dep, arr, s=6, color=style.ACCENT, alpha=1.0, linewidths=0,
               rasterized=True)  # 20k vector <use> tags would bloat the SVG
    ax.set_xlim(-30, 150)
    ax.set_ylim(-60, 180)
    ax.set_xlabel("Departure delay (min)")
    ax.set_ylabel("Arrival delay (min)")
    ax.set_title("20,000 Flights — Raw Scatter")
    ax.annotate("solid points at this scale hide almost\nall structure — everything overlaps",
                xy=(0, 0), xycoords="data", xytext=(0.97, 0.06),
                textcoords="axes fraction", ha="right", va="bottom",
                color=style.BAD, fontsize=9.5)
    style.save(fig, "viz_overlapping_points_nycflights_points")


def _overplot_hexbin():
    dep, arr = _flight_delays()
    fig, ax = style.new_fig(7, 5)
    hb = ax.hexbin(dep, arr, gridsize=42, cmap=SEQ_CMAP, mincnt=1,
                    extent=(-30, 150, -60, 180), linewidths=0.15,
                    edgecolors=style.GRID)
    cb = fig.colorbar(hb, ax=ax, pad=0.02)
    cb.set_label("Flights per bin", color=style.FG)
    cb.ax.yaxis.set_tick_params(color=style.DIM, labelcolor=style.DIM)
    cb.outline.set_edgecolor(style.GRID)
    ax.set_xlim(-30, 150)
    ax.set_ylim(-60, 180)
    ax.set_xlabel("Departure delay (min)")
    ax.set_ylabel("Arrival delay (min)")
    ax.set_title("Same 20,000 Flights — Hex Binned")
    style.save(fig, "viz_overlapping_points_nycflights_hex_bins")


# ---------------------------------------------------------------------------
# 3. Moderate overplot: three fixes side by side (raw / jitter+alpha / density)
# ---------------------------------------------------------------------------

def _survey_grid(n: int = 3000):
    """Two 0-10 integer ratings, correlated. Discreteness alone causes heavy
    overplotting well before the point count gets large: thousands of
    respondents collapse onto ~100 grid intersections.
    """
    latent = RNG.normal(0, 1, n)
    x = np.clip(np.round(5 + 1.6 * latent + RNG.normal(0, 1.1, n)), 0, 10)
    y = np.clip(np.round(5 + 1.3 * latent + RNG.normal(0, 1.3, n)), 0, 10)
    return x, y


def _three_fixes():
    x, y = _survey_grid()
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.2))
    fig.set_dpi(150)  # rasterized scatter panels need real resolution

    ax = axes[0]
    ax.scatter(x, y, s=26, color=style.ACCENT, alpha=1.0, linewidths=0,
               rasterized=True)
    ax.set_title("Raw scatter", fontsize=13)
    ax.set_xlabel("Question A")
    ax.set_ylabel("Question B")

    ax = axes[1]
    jx = x + RNG.uniform(-0.35, 0.35, x.size)
    jy = y + RNG.uniform(-0.35, 0.35, y.size)
    ax.scatter(jx, jy, s=18, color=style.ACCENT, alpha=0.12, linewidths=0,
               rasterized=True)
    ax.set_title("Jitter + alpha", fontsize=13)
    ax.set_xlabel("Question A")

    ax = axes[2]
    hb = ax.hexbin(x, y, gridsize=14, cmap=SEQ_CMAP, mincnt=1,
                    extent=(-0.5, 10.5, -0.5, 10.5), linewidths=0.15,
                    edgecolors=style.GRID)
    ax.set_title("2-D density", fontsize=13)
    ax.set_xlabel("Question A")
    fig.colorbar(hb, ax=ax, pad=0.03, fraction=0.06).ax.yaxis.set_tick_params(
        color=style.DIM, labelcolor=style.DIM)

    for ax in axes:
        ax.set_xlim(-0.5, 10.5)
        ax.set_ylim(-0.5, 10.5)
        ax.set_xticks(range(0, 11, 2))
        ax.set_yticks(range(0, 11, 2))

    fig.suptitle("3,000 Survey Responses — Same Data, Three Views", color=style.FG, fontsize=14)
    style.save(fig, "viz_no_3d_jitter_overplot_jitter_alpha")


# ---------------------------------------------------------------------------
# 4-5. Fake 3D bars distort magnitude vs flat 2D bars
# ---------------------------------------------------------------------------

def _product_sales():
    products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
    # Deliberately near-equal: the whole point is that the true story is
    # "these are all about the same" — 3D perspective is what invents a
    # false ranking.
    values = np.array([61, 57, 63, 59, 60])
    return products, values


def _bar_3d_bad():
    products, values = _product_sales()
    # constrained_layout doesn't support 3D axes (mpl_toolkits.mplot3d) — opt
    # this one figure out explicitly rather than let it warn-and-fall-back.
    fig = plt.figure(figsize=(7.2, 4.8), layout="none")
    ax = fig.add_subplot(111, projection="3d")
    xs = np.arange(len(products))
    ys = np.zeros(len(products))
    colors = [style.CYCLE[i % len(style.CYCLE)] for i in range(len(products))]
    ax.bar3d(xs, ys, np.zeros(len(products)), 0.6, 0.6, values,
              color=colors, shade=True, edgecolor=style.GRID, linewidth=0.4)
    ax.view_init(elev=16, azim=-55)  # oblique angle: back bars read shorter
    ax.set_xticks(xs + 0.3)
    ax.set_xticklabels(products, rotation=12, ha="right")
    ax.set_yticks([])
    ax.set_zlabel("Units sold (thousands)")
    ax.set_title("Quarterly Sales by Product — 3D Bars")
    _style_3d_axes(ax)
    ax.text2D(0.02, 0.95, "perspective hides that these are\nnearly identical values",
              transform=ax.transAxes, color=style.BAD, fontsize=9.5)
    style.save(fig, "viz_no_3d_jitter_bar_3d_bad")


def _bar_2d_fixed():
    products, values = _product_sales()
    fig, ax = style.new_fig(7, 4.4)
    # One colour: the categories are already named on the axis.
    bars = ax.bar(products, values, color=style.ACCENT, width=0.6)
    for rect, v in zip(bars, values):
        ax.annotate(f"{v}", xy=(rect.get_x() + rect.get_width() / 2, v),
                    xytext=(0, 4), textcoords="offset points",
                    ha="center", color=style.FG, fontsize=10)
    ax.set_ylim(0, values.max() * 1.25)
    ax.set_ylabel("Units sold (thousands)")
    ax.set_title("Quarterly Sales by Product — Flat 2D Bars")
    ax.tick_params(axis="x", rotation=0)
    ax.xaxis.grid(False)  # category gridlines read as stray lines rising off the bars
    style.save(fig, "viz_no_3d_jitter_bar_2d_fixed")


# ---------------------------------------------------------------------------
# 6-7. Redundant coding: legend box vs direct end-of-line labels
# ---------------------------------------------------------------------------

def _tech_stocks(n_months: int = 30):
    rng = np.random.default_rng(2102)  # local: paired figures must share identical data
    names = ["Nimbus", "Vertex", "Halcyon", "Quanta"]
    drifts = [0.9, 0.5, -0.2, 1.4]
    t = np.arange(n_months)
    series = {}
    for name, drift in zip(names, drifts):
        cum = np.cumsum(rng.normal(drift, 2.6, n_months))
        series[name] = 100 + cum - cum[0]
    return t, series


def _stocks_bad_legend():
    t, series = _tech_stocks()
    fig, ax = style.new_fig(7.4, 4.4)
    for (name, y), color in zip(series.items(), style.CYCLE):
        ax.plot(t, y, color=color, label=name)
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), borderaxespad=0)
    ax.set_xlabel("Month")
    ax.set_ylabel("Index (base 100)")
    ax.set_title("Tech Stock Index — Legend Off to the Side")
    style.save(fig, "viz_redundant_coding_tech_stocks_bad_legend")


def _stocks_good_no_legend():
    t, series = _tech_stocks()
    fig, ax = style.new_fig(7.4, 4.4)
    xmax = t.max()
    for (name, y), color in zip(series.items(), style.CYCLE):
        ax.plot(t, y, color=color)
        ax.annotate(name, xy=(xmax, y[-1]), xytext=(6, 0),
                    textcoords="offset points", va="center",
                    color=color, fontsize=11, fontweight="bold")
    ax.set_xlim(t.min(), xmax + 5)
    ax.set_xlabel("Month")
    ax.set_ylabel("Index (base 100)")
    ax.set_title("Tech Stock Index — Labelled Directly")
    style.save(fig, "viz_redundant_coding_tech_stocks_good_no_legend")


# ---------------------------------------------------------------------------
# 8-9. Axis-label font size: illegible vs balanced
# ---------------------------------------------------------------------------

def _athletes():
    rng = np.random.default_rng(2103)  # local: paired figures must share identical data
    n = 90
    male_h = rng.normal(183, 7, n)
    male_w = 0.90 * male_h - 85 + rng.normal(0, 6, n)
    female_h = rng.normal(169, 6, n)
    female_w = 0.75 * female_h - 52 + rng.normal(0, 5, n)
    return male_h, male_w, female_h, female_w


def _small_labels_too_small():
    male_h, male_w, female_h, female_w = _athletes()
    with mpl.rc_context({
        "font.size": 4, "axes.labelsize": 4, "axes.titlesize": 4,
        "xtick.labelsize": 3, "ytick.labelsize": 3, "legend.fontsize": 3,
    }):
        fig, ax = style.new_fig(7, 4.4)
        ax.scatter(male_h, male_w, s=22, color=style.CYCLE[0], label="Male", alpha=0.85)
        ax.scatter(female_h, female_w, s=22, color=style.CYCLE[3], label="Female", alpha=0.85)
        ax.set_xlabel("Height (cm)")
        ax.set_ylabel("Weight (kg)")
        ax.set_title("Athlete Height vs Weight")
        ax.legend()
        style.save(fig, "viz_small_axis_labels_aus_athletes_too_small")


def _small_labels_balanced():
    male_h, male_w, female_h, female_w = _athletes()
    fig, ax = style.new_fig(7, 4.4)
    ax.scatter(male_h, male_w, s=22, color=style.CYCLE[0], label="Male", alpha=0.85)
    ax.scatter(female_h, female_w, s=22, color=style.CYCLE[3], label="Female", alpha=0.85)
    ax.set_xlabel("Height (cm)")
    ax.set_ylabel("Weight (kg)")
    ax.set_title("Athlete Height vs Weight")
    ax.legend()
    style.save(fig, "viz_small_axis_labels_aus_athletes_balanced")


FIGURES = {
    "viz_overlapping_points_nycflights_points": _overplot_points,
    "viz_overlapping_points_nycflights_hex_bins": _overplot_hexbin,
    "viz_no_3d_jitter_overplot_jitter_alpha": _three_fixes,
    "viz_no_3d_jitter_bar_3d_bad": _bar_3d_bad,
    "viz_no_3d_jitter_bar_2d_fixed": _bar_2d_fixed,
    "viz_redundant_coding_tech_stocks_bad_legend": _stocks_bad_legend,
    "viz_redundant_coding_tech_stocks_good_no_legend": _stocks_good_no_legend,
    "viz_small_axis_labels_aus_athletes_too_small": _small_labels_too_small,
    "viz_small_axis_labels_aus_athletes_balanced": _small_labels_balanced,
}
