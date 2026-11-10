"""Associations family: scatter, bubbles, slopes, correlations, trends, panels.
Ten figures for lecture 10's "Associations" / "Multi-panel" / "Trends" sections.
Real bundled datasets (seaborn penguins, mpg) where they fit the pedagogical
point; synthetic (fixed-seed RNG) Keeling-curve / price / gapminder-style
series where no bundled dataset applies.
"""
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
import seaborn as sns

import style


# --------------------------------------------------------------------------
# associations_blue_jays_scatter / _bubble — penguins bill length x depth
# --------------------------------------------------------------------------

def _blue_jays_scatter():
    """Scatter with a third, categorical dimension on colour (penguin species),
    labelled directly at each cluster's centre — no legend needed."""
    df = sns.load_dataset("penguins").dropna(subset=["bill_length_mm", "bill_depth_mm"])
    species = ["Adelie", "Chinstrap", "Gentoo"]
    colors = dict(zip(species, style.CYCLE[:3]))
    fig, ax = style.new_fig(6.8, 4.6)
    for sp in species:
        sub = df[df["species"] == sp]
        ax.scatter(sub["bill_length_mm"], sub["bill_depth_mm"], s=16,
                   color=colors[sp], alpha=0.8, edgecolor="none")
    # Direct labels beside each cluster (offsets keep them off the points).
    offsets = {"Adelie": (-5.5, 1.6), "Chinstrap": (2.6, 2.7), "Gentoo": (2.6, -1.7)}
    for sp in species:
        sub = df[df["species"] == sp]
        cx, cy = sub["bill_length_mm"].mean(), sub["bill_depth_mm"].mean()
        dx, dy = offsets[sp]
        ax.text(cx + dx, cy + dy, sp, color=colors[sp], fontsize=12.5,
                ha="center", va="center")
    ax.set_xlabel("Bill length (mm)")
    ax.set_ylabel("Bill depth (mm)")
    ax.set_title("Bill Length vs. Bill Depth — colour = species")
    style.save(fig, "viz_associations_blue_jays_scatter")


def _blue_jays_bubble():
    df = sns.load_dataset("penguins").dropna(
        subset=["bill_length_mm", "bill_depth_mm", "body_mass_g"])
    scale = 420 / df["body_mass_g"].max()  # marker AREA proportional to mass
    # open circles as a paper draws bubbles: a faint fill, a thin edge in the
    # full colour, so the overlapping circles stay apart
    face = mcolors.to_rgba(style.ACCENT, 0.16)
    fig, ax = style.new_fig(6.8, 4.6)
    ax.scatter(df["bill_length_mm"], df["bill_depth_mm"], s=df["body_mass_g"] * scale,
               facecolor=face, edgecolor=style.ACCENT, linewidth=0.8)
    for mass in (3000, 4500, 6000):
        ax.scatter([], [], s=mass * scale, facecolor=face,
                   edgecolor=style.ACCENT, linewidth=0.8, label=f"{mass:,} g")
    ax.set_xlabel("Bill length (mm)")
    ax.set_ylabel("Bill depth (mm)")
    ax.set_title("+ Body Mass as Bubble Size")
    ax.legend(title="Body mass", loc="upper left", bbox_to_anchor=(1.01, 1), labelspacing=1.6, borderpad=1.1,
               handletextpad=1.4)
    style.save(fig, "viz_associations_blue_jays_bubble")


# --------------------------------------------------------------------------
# associations_co2_slopegraph — 8 entities, two time points, a few highlighted
# --------------------------------------------------------------------------

def _declutter(values: np.ndarray, min_gap: float) -> np.ndarray:
    """Nudge a copy of `values` upward, in ascending order, so no two are
    closer than `min_gap` — used to keep slopegraph end-labels legible
    without moving the lines/markers themselves."""
    order = np.argsort(values)
    out = values.astype(float).copy()
    for k in range(1, len(order)):
        i, prev_i = order[k], order[k - 1]
        if out[i] - out[prev_i] < min_gap:
            out[i] = out[prev_i] + min_gap
    return out


def _co2_slopegraph():
    # Per-capita CO2 emissions, tonnes per person, 2000 vs 2020 — rounded from
    # the Global Carbon Project / Our World in Data series (approximate).
    entities = ["China", "USA", "India", "Russia", "Germany", "Japan", "Brazil", "Nigeria"]
    v2000 = np.array([2.7, 20.5, 0.9, 10.6, 10.1, 9.6, 1.9, 0.6])
    v2020 = np.array([7.4, 14.2, 1.7, 11.2, 7.7, 8.0, 2.0, 0.6])
    highlight_color = {"China": style.CYCLE[0], "USA": style.CYCLE[1], "Germany": style.CYCLE[2]}

    min_gap = 0.052 * (max(v2000.max(), v2020.max()) - min(v2000.min(), v2020.min()))
    label_y0 = _declutter(v2000, min_gap)
    label_y1 = _declutter(v2020, min_gap)

    fig, ax = style.new_fig(7.6, 5.6)
    order = np.argsort(-v2000)
    for i in order:
        name = entities[i]
        y0, y1 = v2000[i], v2020[i]
        hi = name in highlight_color
        color = highlight_color.get(name, style.DIM)
        ax.plot([0, 1], [y0, y1], color=color, lw=1.8 if hi else 1.0,
                alpha=1.0 if hi else 0.6, zorder=3 if hi else 2,
                marker="o", ms=4.5 if hi else 3.5)
        label_color = color if hi else style.DIM
        ax.annotate(f"{name}  {y0:.1f}", xy=(0, y0), xytext=(-0.06, label_y0[i]),
                    ha="right", va="center", fontsize=10.5, color=label_color)
        ax.annotate(f"{y1:.1f}  {name}", xy=(1, y1), xytext=(1.06, label_y1[i]),
                    ha="left", va="center", fontsize=10.5, color=label_color)
    ax.set_xlim(-0.95, 1.95)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["2000", "2020"])
    ax.set_yticks([])
    ax.set_title("Per-capita CO$_2$ emissions [t / person] — 2000 vs. 2020 (approx.)")
    style.save(fig, "viz_associations_co2_slopegraph")


# --------------------------------------------------------------------------
# associations_mtcars_corr_heatmap — mpg dataset numeric cols, diverging cmap
# --------------------------------------------------------------------------

def _mtcars_corr_heatmap():
    cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
            "acceleration", "model_year"]
    short = {"mpg": "mpg", "cylinders": "cylinders", "displacement": "displacement",
             "horsepower": "horsepower", "weight": "weight",
             "acceleration": "acceleration", "model_year": "year"}
    df = sns.load_dataset("mpg").dropna(subset=cols)
    corr = df[cols].corr()

    cmap = mcolors.LinearSegmentedColormap.from_list(
        "diverging", [style.BAD, "#333b4a", style.ACCENT])
    norm = mcolors.Normalize(vmin=-1, vmax=1)

    fig, ax = style.new_fig(6.6, 5.8)
    # the cells where imshow would put them, as vector cells (an image inside
    # the SVG turns grainy on the projector), each edged in its own colour
    n = len(cols)
    im = ax.pcolormesh(np.arange(n + 1) - 0.5, np.arange(n + 1) - 0.5, corr.values,
                       cmap=cmap, norm=norm, edgecolors="face")
    ax.set(xlim=(-0.5, n - 0.5), ylim=(n - 0.5, -0.5))
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels([short[c] for c in cols], rotation=40, ha="right")
    ax.set_yticks(range(len(cols)))
    ax.set_yticklabels([short[c] for c in cols])
    # the frame stays; a named column needs no tick mark poking into its cell
    ax.tick_params(which="both", length=0)
    for i in range(len(cols)):
        for j in range(len(cols)):
            v = corr.values[i, j]
            r, g, b, _ = cmap(norm(v))
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            txt_color = "#0b0f14" if lum > 0.55 else style.FG
            ax.text(j, i, style.thousands(v, 2), ha="center", va="center",
                    fontsize=10, color=txt_color)
    cbar = fig.colorbar(im, ax=ax, shrink=0.85, pad=0.03)
    # a colour bar of many colours is an image in matplotlib's SVG; keep it vector
    cbar.solids.set_rasterized(False)
    cbar.solids.set_edgecolor("face")
    ax.set_title("Correlation Matrix — mpg Dataset")
    style.save(fig, "viz_associations_mtcars_corr_heatmap")


# --------------------------------------------------------------------------
# multi_panel_correlogram — 3x3 pair plot, penguins, 3 vars
# --------------------------------------------------------------------------

def _correlogram():
    varz = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
    labels = ["Bill length\n(mm)", "Bill depth\n(mm)", "Flipper length\n(mm)"]
    step = [10, 2, 20]   # the tick step of each measurement, mm
    df = sns.load_dataset("penguins").dropna(subset=varz)
    n = len(varz)
    fig, axes = plt.subplots(n, n, figsize=(7.2, 6.8))
    for i in range(n):
        for j in range(n):
            ax = axes[i, j]
            if i == j:
                ax.hist(df[varz[i]], bins=16, histtype="stepfilled", linewidth=0.9,
                        facecolor=mcolors.to_rgba(style.ACCENT, 0.35),
                        edgecolor=style.ACCENT)
                ax.set_yticks([])   # counts beside a label in mm would be misread
            else:
                ax.scatter(df[varz[j]], df[varz[i]], s=8, color=style.ACCENT,
                           alpha=0.55, edgecolor="none")
                ax.yaxis.set_major_locator(mticker.MultipleLocator(step[i]))
            ax.xaxis.set_major_locator(mticker.MultipleLocator(step[j]))
            ax.tick_params(labelsize=9.5)
            if i == n - 1:
                ax.set_xlabel(labels[j], fontsize=11)
            else:
                ax.set_xticklabels([])
            if j == 0:
                ax.set_ylabel(labels[i], fontsize=11)
            else:
                ax.set_yticklabels([])
    fig.suptitle("Pair Plot — Three Penguin Measurements")
    style.save(fig, "viz_multi_panel_correlogram")


# --------------------------------------------------------------------------
# multi_panel_small_multiples_gapminder — 6 panels, shared scale
# --------------------------------------------------------------------------

def _small_multiples_gapminder():
    rng = np.random.default_rng(42)
    years = np.arange(1950, 2021)
    regions = ["East Asia", "South Asia", "Europe", "N. America",
               "Sub-Saharan Africa", "Latin America"]
    base = np.array([600, 500, 5000, 9000, 400, 1800])
    rate = np.array([0.052, 0.030, 0.021, 0.018, 0.014, 0.024])
    curves = {}
    for name, b, r in zip(regions, base, rate):
        wobble = rng.normal(0, 0.02, size=years.size).cumsum() * 0.05
        curves[name] = b * np.exp(r * (years - 1950)) * (1 + wobble)
    ymax = max(c.max() for c in curves.values()) * 1.08

    fig, axes = plt.subplots(2, 3, figsize=(8.8, 5.2), sharex=True, sharey=True)
    for ax, name in zip(axes.flat, regions):
        for other in regions:
            if other != name:
                ax.plot(years, curves[other], color=style.DIM, lw=0.9, alpha=0.3)
        ax.plot(years, curves[name], color=style.ACCENT, lw=1.8)
        ax.set_title(name, fontsize=11.5, loc="left")
        ax.set_ylim(0, ymax)
        ax.yaxis.set_major_locator(mticker.MultipleLocator(10000))
        ax.yaxis.set_major_formatter(style.ThousandsFormatter())
    for ax in axes[-1, :]:
        ax.set_xlabel("Year", fontsize=11)
    for ax in axes[:, 0]:
        ax.set_ylabel("GDP / capita ($)", fontsize=10.5)
    fig.suptitle("Small Multiples — Same Scale, Six Panels")
    style.save(fig, "viz_multi_panel_small_multiples_gapminder")


# --------------------------------------------------------------------------
# trends_keeling_curve / trends_keeling_decomposition — shared synthetic series
# --------------------------------------------------------------------------

def _keeling_series():
    start_year, end_year = 1958, 2024
    n_months = (end_year - start_year + 1) * 12
    idx = np.arange(n_months)
    years = start_year + idx / 12
    x = idx / 12  # years since start
    trend = 315 + 1.1 * x + 0.0075 * x ** 2
    seasonal = 3.0 * np.sin(2 * np.pi * (idx % 12) / 12 - 1.0)
    noise = np.random.default_rng(1958).normal(0, 0.25, n_months)
    observed = trend + seasonal + noise
    return years, observed, trend, seasonal, noise


def _keeling_curve():
    years, observed, _, _, _ = _keeling_series()
    fig, ax = style.new_fig(7.6, 4.4)
    ax.plot(years, observed, color=style.ACCENT, lw=1.3)
    ax.set_xlabel("Year")
    ax.set_ylabel("CO$_2$ (ppm)")
    ax.set_title("Keeling-style CO$_2$ Curve, 1958–2024")
    style.save(fig, "viz_trends_keeling_curve")


def _keeling_decomposition():
    years, observed, trend, seasonal, noise = _keeling_series()
    seasonal_resid = seasonal + noise
    # three panels side by side: the slide shows it full width
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.6), sharex=True)
    axes[0].plot(years, observed, color=style.ACCENT, lw=1.1)
    axes[0].set_title("Observed")
    axes[0].set_ylabel("CO$_2$ (ppm)")
    axes[1].plot(years, trend, color=style.CYCLE[1], lw=1.8)
    axes[1].set_title("Trend")
    axes[2].plot(years, seasonal_resid, color=style.CYCLE[2], lw=0.9)
    axes[2].axhline(0, color=style.DIM, lw=0.8, ls="--")
    axes[2].set_title("Seasonal + residual")
    for ax in axes:
        ax.set_xlabel("Year")
    style.save(fig, "viz_trends_keeling_decomposition")


# --------------------------------------------------------------------------
# trends_lincoln_temps_raw_smooth — noisy daily series + rolling-mean smooth
# --------------------------------------------------------------------------

def _lincoln_temps_raw_smooth():
    """The daily means of 2024 and 2025 from the weather log, and their
    running mean over 21 days (centred)."""
    from datetime import datetime
    from handson import PATH, group, mean
    days = group(PATH, 0, 10)
    keys = [d for d in sorted(days) if d[:4] in ("2024", "2025")]
    dates = [datetime.fromisoformat(d) for d in keys]
    temp = np.array([mean(days[d]) for d in keys])
    smooth = pd.Series(temp).rolling(21, center=True, min_periods=1).mean().to_numpy()

    fig, ax = style.new_fig(7.6, 4.4)
    ax.plot(dates, temp, color=style.DIM, lw=0.8, alpha=0.8, label="daily mean")
    ax.plot(dates, smooth, color=style.ACCENT, lw=2.4, label="mean over 21 days")
    ax.set_ylabel("temperature (°C)")
    ax.legend(loc="upper left")
    style.save(fig, "viz_trends_lincoln_temps_raw_smooth")


# --------------------------------------------------------------------------
# trends_detrended_price — raw series (with trend overlay) vs. detrended
# --------------------------------------------------------------------------

def _detrended_price():
    rng = np.random.default_rng(1907)
    months = np.arange(180)  # 15 years, monthly
    t = months / 12
    trend = 40 + 2.6 * t + 0.15 * t ** 2
    seasonal = 5.5 * np.sin(2 * np.pi * (months % 12) / 12 + 0.6)
    noise = rng.normal(0, 1.1, months.size)
    price = trend + seasonal + noise
    detrended = price - trend

    fig, axes = plt.subplots(2, 1, figsize=(7.4, 5.8), sharex=True)
    axes[0].plot(t, price, color=style.DIM, lw=1.4, label="Raw price")
    axes[0].plot(t, trend, color=style.ACCENT, lw=1.8, ls="--", label="Trend")
    axes[0].set_ylabel("Price (raw)")
    axes[0].set_title("Raw Series — Trend Hides the Cycle")
    axes[0].legend(loc="upper left", fontsize=9)
    axes[1].plot(t, detrended, color=style.CYCLE[2], lw=1.4)
    axes[1].axhline(0, color=style.DIM, lw=0.8, ls="--")
    axes[1].set_ylabel("Detrended")
    axes[1].set_xlabel("Year")
    axes[1].set_title("Seasonality Isolated")
    style.save(fig, "viz_trends_detrended_price")


FIGURES = {
    "viz_associations_blue_jays_scatter": _blue_jays_scatter,
    "viz_associations_blue_jays_bubble": _blue_jays_bubble,
    "viz_associations_co2_slopegraph": _co2_slopegraph,
    "viz_associations_mtcars_corr_heatmap": _mtcars_corr_heatmap,
    "viz_multi_panel_correlogram": _correlogram,
    "viz_multi_panel_small_multiples_gapminder": _small_multiples_gapminder,
    "viz_trends_keeling_curve": _keeling_curve,
    "viz_trends_lincoln_temps_raw_smooth": _lincoln_temps_raw_smooth,
    "viz_trends_keeling_decomposition": _keeling_decomposition,
    "viz_trends_detrended_price": _detrended_price,
}
