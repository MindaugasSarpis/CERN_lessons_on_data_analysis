"""Associations family: scatter, bubbles, slopes, correlations, trends, panels.
Ten figures for lecture 10's "Associations" / "Multi-panel" / "Trends" sections.
Real bundled datasets (seaborn penguins, mpg) where they fit the pedagogical
point; synthetic (fixed-seed RNG) Keeling-curve / price / gapminder-style
series where no bundled dataset applies.
"""
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
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
        ax.scatter(sub["bill_length_mm"], sub["bill_depth_mm"], s=30,
                   color=colors[sp], alpha=0.75, edgecolor="none")
    # Direct labels beside each cluster (offsets keep them off the points).
    offsets = {"Adelie": (-6.5, 1.6), "Chinstrap": (3.2, 1.7), "Gentoo": (2.6, -1.7)}
    for sp in species:
        sub = df[df["species"] == sp]
        cx, cy = sub["bill_length_mm"].mean(), sub["bill_depth_mm"].mean()
        dx, dy = offsets[sp]
        ax.text(cx + dx, cy + dy, sp, color=colors[sp], fontsize=12,
                fontweight="bold", ha="center", va="center")
    ax.set_xlabel("Bill length (mm)")
    ax.set_ylabel("Bill depth (mm)")
    ax.set_title("Bill Length vs. Bill Depth — colour = species")
    style.save(fig, "viz_associations_blue_jays_scatter")


def _blue_jays_bubble():
    df = sns.load_dataset("penguins").dropna(
        subset=["bill_length_mm", "bill_depth_mm", "body_mass_g"])
    scale = 420 / df["body_mass_g"].max()  # marker AREA proportional to mass
    fig, ax = style.new_fig(6.8, 4.6)
    ax.scatter(df["bill_length_mm"], df["bill_depth_mm"], s=df["body_mass_g"] * scale,
               color=style.ACCENT, alpha=0.5, edgecolor=style.FG, linewidth=0.3)
    for mass in (3000, 4500, 6000):
        ax.scatter([], [], s=mass * scale, color=style.ACCENT, alpha=0.5,
                   edgecolor=style.FG, linewidth=0.3, label=f"{mass:,} g")
    ax.set_xlabel("Bill length (mm)")
    ax.set_ylabel("Bill depth (mm)")
    ax.set_title("+ Body Mass as Bubble Size")
    ax.legend(title="Body mass", loc="upper right", labelspacing=1.6, borderpad=1.1,
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

    min_gap = 0.045 * (max(v2000.max(), v2020.max()) - min(v2000.min(), v2020.min()))
    label_y0 = _declutter(v2000, min_gap)
    label_y1 = _declutter(v2020, min_gap)

    fig, ax = style.new_fig(7.6, 5.6)
    order = np.argsort(-v2000)
    for i in order:
        name = entities[i]
        y0, y1 = v2000[i], v2020[i]
        hi = name in highlight_color
        color = highlight_color.get(name, style.DIM)
        ax.plot([0, 1], [y0, y1], color=color, lw=2.4 if hi else 1.2,
                alpha=1.0 if hi else 0.55, zorder=3 if hi else 2,
                marker="o", ms=5.5 if hi else 4)
        label_color = color if hi else style.DIM
        ax.annotate(f"{name}  {y0:.1f}", xy=(0, y0), xytext=(-0.06, label_y0[i]),
                    ha="right", va="center", fontsize=9, color=label_color)
        ax.annotate(f"{y1:.1f}  {name}", xy=(1, y1), xytext=(1.06, label_y1[i]),
                    ha="left", va="center", fontsize=9, color=label_color)
    ax.set_xlim(-0.95, 1.95)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["2000", "2020"])
    ax.set_yticks([])
    for side in ("left", "right", "top"):
        ax.spines[side].set_visible(False)
    ax.grid(False)
    ax.set_title("Per-capita CO$_2$ emissions [t / person] — 2000 vs. 2020 (approx.)")
    style.save(fig, "viz_associations_co2_slopegraph")


# --------------------------------------------------------------------------
# associations_mtcars_corr_heatmap — mpg dataset numeric cols, diverging cmap
# --------------------------------------------------------------------------

def _mtcars_corr_heatmap():
    cols = ["mpg", "cylinders", "displacement", "horsepower", "weight",
            "acceleration", "model_year"]
    short = {"mpg": "mpg", "cylinders": "cyl", "displacement": "disp",
             "horsepower": "hp", "weight": "weight", "acceleration": "accel",
             "model_year": "year"}
    df = sns.load_dataset("mpg").dropna(subset=cols)
    corr = df[cols].corr()

    cmap = mcolors.LinearSegmentedColormap.from_list(
        "diverging", [style.BAD, "#333b4a", style.ACCENT])
    norm = mcolors.Normalize(vmin=-1, vmax=1)

    fig, ax = style.new_fig(6.6, 5.8)
    im = ax.imshow(corr.values, cmap=cmap, norm=norm)
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels([short[c] for c in cols], rotation=40, ha="right")
    ax.set_yticks(range(len(cols)))
    ax.set_yticklabels([short[c] for c in cols])
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for i in range(len(cols)):
        for j in range(len(cols)):
            v = corr.values[i, j]
            r, g, b, _ = cmap(norm(v))
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            txt_color = "#0b0f14" if lum > 0.55 else style.FG
            ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                    fontsize=8.5, color=txt_color)
    cbar = fig.colorbar(im, ax=ax, shrink=0.85, pad=0.03)
    cbar.outline.set_visible(False)
    cbar.ax.tick_params(colors=style.DIM, labelsize=8)
    ax.set_title("Correlation Matrix — mpg Dataset")
    style.save(fig, "viz_associations_mtcars_corr_heatmap")


# --------------------------------------------------------------------------
# multi_panel_correlogram — 3x3 pair plot, penguins, 3 vars
# --------------------------------------------------------------------------

def _correlogram():
    varz = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
    labels = ["Bill length\n(mm)", "Bill depth\n(mm)", "Flipper length\n(mm)"]
    df = sns.load_dataset("penguins").dropna(subset=varz)
    n = len(varz)
    fig, axes = plt.subplots(n, n, figsize=(7.2, 6.8))
    for i in range(n):
        for j in range(n):
            ax = axes[i, j]
            if i == j:
                ax.hist(df[varz[i]], bins=16, color=style.ACCENT, alpha=0.85)
            else:
                ax.scatter(df[varz[j]], df[varz[i]], s=10, color=style.ACCENT,
                           alpha=0.5, edgecolor="none")
            ax.tick_params(labelsize=7)
            if i == n - 1:
                ax.set_xlabel(labels[j], fontsize=9)
            else:
                ax.set_xticklabels([])
            if j == 0:
                ax.set_ylabel(labels[i], fontsize=9)
            else:
                ax.set_yticklabels([])
    fig.suptitle("Pair Plot — Three Penguin Measurements", y=1.02)
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
        ax.plot(years, curves[name], color=style.ACCENT, lw=2.0)
        ax.set_title(name, fontsize=10, loc="left")
        ax.set_ylim(0, ymax)
    for ax in axes[-1, :]:
        ax.set_xlabel("Year", fontsize=9)
    for ax in axes[:, 0]:
        ax.set_ylabel("GDP / capita\n(synthetic $)", fontsize=9)
    fig.suptitle("Small Multiples — Same Scale, Six Panels", y=1.02)
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
    ax.set_ylabel("CO$_2$ (ppm, synthetic)")
    ax.set_title("Keeling-style CO$_2$ Curve, 1958–2024")
    style.save(fig, "viz_trends_keeling_curve")


def _keeling_decomposition():
    years, observed, trend, seasonal, noise = _keeling_series()
    seasonal_resid = seasonal + noise
    fig, axes = plt.subplots(3, 1, figsize=(7.6, 6.6), sharex=True)
    axes[0].plot(years, observed, color=style.ACCENT, lw=1.1)
    axes[0].set_ylabel("Observed")
    axes[0].set_title("Decomposing the Keeling Curve")
    axes[1].plot(years, trend, color=style.CYCLE[1], lw=1.8)
    axes[1].set_ylabel("Trend")
    axes[2].plot(years, seasonal_resid, color=style.CYCLE[2], lw=0.9)
    axes[2].axhline(0, color=style.DIM, lw=0.8, ls="--")
    axes[2].set_ylabel("Seasonal + residual")
    axes[2].set_xlabel("Year")
    style.save(fig, "viz_trends_keeling_decomposition")


# --------------------------------------------------------------------------
# trends_lincoln_temps_raw_smooth — noisy daily series + rolling-mean smooth
# --------------------------------------------------------------------------

def _lincoln_temps_raw_smooth():
    rng = np.random.default_rng(68508)
    days = np.arange(730)  # two years, daily
    doy = days % 365
    seasonal = 12 + 14 * np.sin(2 * np.pi * (doy - 80) / 365)
    noise = rng.normal(0, 4.0, days.size)
    temp = seasonal + noise
    smooth = pd.Series(temp).rolling(21, center=True, min_periods=1).mean().to_numpy()

    fig, ax = style.new_fig(7.6, 4.4)
    ax.plot(days, temp, color=style.DIM, lw=0.8, alpha=0.7, label="Daily mean (raw)")
    ax.plot(days, smooth, color=style.ACCENT, lw=2.4, label="21-day rolling mean")
    ax.set_xlabel("Day")
    ax.set_ylabel("Temperature (°C, synthetic)")
    ax.set_title("Raw Series + Smoothed Trend")
    ax.legend(loc="upper right")
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
