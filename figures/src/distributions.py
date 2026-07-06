"""Distributions family: histograms, densities, box/violin/strip, QQ, ECDF,
ridgeline. Eleven figures for lecture 10 ("Distributions" + "Avoid Line
Drawings" sections). Seaborn is used ONLY for load_dataset; all plotting goes
through style (matplotlib).
"""
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import gaussian_kde, norm, t as student_t

import style

# ---------------------------------------------------------------------------
# distributions_i_anscombes_quartet
# ---------------------------------------------------------------------------

def _anscombes_quartet():
    x_common = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], dtype=float)
    x4 = np.array([8, 8, 8, 8, 8, 19, 8, 8, 8, 8, 8], dtype=float)
    datasets = {
        "I": (x_common, np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])),
        "II": (x_common, np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])),
        "III": (x_common, np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])),
        "IV": (x4, np.array([6.58, 5.76, 7.71, 8.84, 8.47, 12.50, 7.04, 5.25, 5.56, 7.91, 6.89])),
    }
    fig, axes = plt.subplots(2, 2, figsize=(7.4, 6.0), sharex=True, sharey=True)
    xs_line = np.array([2, 20])
    for ax, (label, (x, y)) in zip(axes.flat, datasets.items()):
        m, b = np.polyfit(x, y, 1)
        r = np.corrcoef(x, y)[0, 1]
        ax.scatter(x, y, s=42, color=style.ACCENT, zorder=3, edgecolor="none")
        ax.plot(xs_line, m * xs_line + b, color=style.CYCLE[1], lw=1.6, zorder=2)
        ax.set_title(f"Dataset {label}")
        ax.text(0.04, 0.92, f"r = {r:.2f}   y = {b:.2f} + {m:.2f}x",
                transform=ax.transAxes, fontsize=8.5, color=style.DIM, va="top")
        ax.set_xlim(2, 20)
        ax.set_ylim(2, 14)
    for ax in axes[-1, :]:
        ax.set_xlabel("x")
    for ax in axes[:, 0]:
        ax.set_ylabel("y")
    style.save(fig, "viz_distributions_i_anscombes_quartet")


# ---------------------------------------------------------------------------
# distributions_i_titanic_density  (histogram + KDE overlay, single variable)
# ---------------------------------------------------------------------------

def _titanic_density():
    age = sns.load_dataset("titanic")["age"].dropna().to_numpy()
    fig, ax = style.new_fig(7.2, 4.4)
    ax.hist(age, bins=np.arange(0, 82, 4), density=True, color=style.ACCENT,
            alpha=0.35, edgecolor=style.ACCENT, linewidth=1.0)
    xs = np.linspace(0, 80, 300)
    ax.plot(xs, gaussian_kde(age)(xs), color=style.ACCENT, lw=2.2)
    ax.set_xlim(0, 80)
    ax.set_xlabel("Age (years)")
    ax.set_ylabel("Density")
    ax.set_title("Distribution of Passenger Age — Titanic")
    style.save(fig, "viz_distributions_i_titanic_density")


# ---------------------------------------------------------------------------
# distributions_i_titanic_hist_binwidth  (too narrow / good / too wide)
# ---------------------------------------------------------------------------

def _titanic_hist_binwidth():
    age = sns.load_dataset("titanic")["age"].dropna().to_numpy()
    panels = [
        (0.5, "binwidth = 0.5 yr — too narrow", True),
        (5.0, "binwidth = 5 yr — good", False),
        (20.0, "binwidth = 20 yr — too wide", True),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.6), sharey=False)
    for ax, (width, title, bad) in zip(axes, panels):
        edges = np.arange(0, age.max() + width, width)
        ax.hist(age, bins=edges, color=style.ACCENT, alpha=0.85, edgecolor="none")
        ax.set_title(title, fontsize=12, color=style.BAD if bad else style.FG)
        ax.set_xlabel("Age (years)")
        ax.set_xlim(0, 80)
    axes[0].set_ylabel("Count")
    style.save(fig, "viz_distributions_i_titanic_hist_binwidth")


# ---------------------------------------------------------------------------
# distributions_i_titanic_ecdf
# ---------------------------------------------------------------------------

def _titanic_ecdf():
    age = sns.load_dataset("titanic")["age"].dropna().to_numpy()
    fig, ax = style.new_fig(7.2, 4.4)
    ax.ecdf(age, color=style.ACCENT, lw=2.2)
    q1, med, q3 = np.percentile(age, [25, 50, 75])
    ax.axhline(0.5, color=style.DIM, lw=0.8, ls=":", zorder=1)
    ax.axvline(med, color=style.CYCLE[1], lw=1.2, ls="--", zorder=1)
    ax.annotate(f"median ≈ {med:.0f} yr", xy=(med, 0.5), xytext=(med + 4, 0.36),
                color=style.CYCLE[1], fontsize=10,
                arrowprops=dict(arrowstyle="->", color=style.CYCLE[1], lw=1))
    for q, lbl in [(q1, "Q1"), (q3, "Q3")]:
        y = 0.25 if q == q1 else 0.75
        ax.plot(q, y, "o", ms=6, color=style.CYCLE[1], zorder=3)
        ax.annotate(lbl, xy=(q, y), xytext=(q - 3, y + 0.06), color=style.DIM, fontsize=9, ha="right")
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 1.02)
    ax.set_xlabel("Age (years)")
    ax.set_ylabel("Fraction ≤ age")
    ax.set_title("Empirical CDF — Passenger Age")
    style.save(fig, "viz_distributions_i_titanic_ecdf")


# ---------------------------------------------------------------------------
# distributions_i_qq_plot
# ---------------------------------------------------------------------------

def _qq_plot():
    rng = np.random.default_rng(42)
    n = 200
    sample = student_t.rvs(df=30, size=n, random_state=rng)  # near-normal, slightly heavy tails
    sample.sort()
    sample_z = (sample - sample.mean()) / sample.std()
    probs = (np.arange(1, n + 1) - 0.5) / n
    theo = norm.ppf(probs)

    fig, ax = style.new_fig(5.6, 5.2)
    lo, hi = theo.min() - 0.3, theo.max() + 0.3
    ax.plot([lo, hi], [lo, hi], color=style.DIM, lw=1.4, ls="--", zorder=1)
    ax.scatter(theo, sample_z, s=22, color=style.ACCENT, alpha=0.85, zorder=2, edgecolor="none")
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("Theoretical quantiles (Normal)")
    ax.set_ylabel("Sample quantiles")
    ax.set_title("Q–Q Plot — Sample vs Normal")
    style.save(fig, "viz_distributions_i_qq_plot")


# ---------------------------------------------------------------------------
# distributions_ii_mpg_{boxplot, strip_jitter, violin}  — shared setup
# ---------------------------------------------------------------------------

CYL_ORDER = [4, 6, 8]
CYL_COLOR = dict(zip(CYL_ORDER, style.CYCLE[:3]))


def _mpg_by_cylinders():
    mpg = sns.load_dataset("mpg")
    return {c: mpg.loc[mpg["cylinders"] == c, "mpg"].to_numpy() for c in CYL_ORDER}


def _mpg_axes_common(ax):
    ax.set_xticks(range(len(CYL_ORDER)))
    ax.set_xticklabels([str(c) for c in CYL_ORDER])
    ax.set_xlabel("Cylinders")
    ax.set_ylabel("Fuel economy (mpg)")
    ax.set_ylim(5, 50)


def _mpg_boxplot():
    data = _mpg_by_cylinders()
    fig, ax = style.new_fig(4.8, 3.8)
    bx = ax.boxplot([data[c] for c in CYL_ORDER], positions=range(len(CYL_ORDER)),
                     widths=0.5, patch_artist=True,
                     medianprops=dict(color=style.FG, lw=1.6),
                     whiskerprops=dict(color=style.DIM), capprops=dict(color=style.DIM),
                     flierprops=dict(marker="o", ms=3.5, markerfacecolor=style.DIM,
                                      markeredgecolor="none", alpha=0.7))
    for c, box in zip(CYL_ORDER, bx["boxes"]):
        box.set_facecolor(CYL_COLOR[c])
        box.set_alpha(0.55)
        box.set_edgecolor(CYL_COLOR[c])
    _mpg_axes_common(ax)
    ax.set_title("Boxplot")
    style.save(fig, "viz_distributions_ii_mpg_boxplot")


def _mpg_strip_jitter():
    data = _mpg_by_cylinders()
    rng = np.random.default_rng(6)
    fig, ax = style.new_fig(4.8, 3.8)
    for i, c in enumerate(CYL_ORDER):
        y = data[c]
        x = i + rng.uniform(-0.16, 0.16, size=len(y))
        ax.scatter(x, y, s=14, color=CYL_COLOR[c], alpha=0.55, linewidths=0, zorder=2)
    _mpg_axes_common(ax)
    ax.set_title("Strip + Jitter")
    style.save(fig, "viz_distributions_ii_mpg_strip_jitter")


def _mpg_violin():
    data = _mpg_by_cylinders()
    fig, ax = style.new_fig(4.8, 3.8)
    parts = ax.violinplot([data[c] for c in CYL_ORDER], positions=range(len(CYL_ORDER)),
                           widths=0.8, showmedians=True, showextrema=True)
    for c, body in zip(CYL_ORDER, parts["bodies"]):
        body.set_facecolor(CYL_COLOR[c])
        body.set_alpha(0.55)
        body.set_edgecolor(CYL_COLOR[c])
    for key in ("cmedians", "cbars", "cmins", "cmaxes"):
        parts[key].set_color(style.DIM)
    parts["cmedians"].set_color(style.FG)
    _mpg_axes_common(ax)
    ax.set_title("Violin")
    style.save(fig, "viz_distributions_ii_mpg_violin")


# ---------------------------------------------------------------------------
# distributions_ii_ridgeline  (synthetic monthly temperatures)
# ---------------------------------------------------------------------------

def _ridgeline():
    rng = np.random.default_rng(2026)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    means = 10 + 12 * np.sin(2 * np.pi * (np.arange(12) - 3) / 12)
    std = 3.0
    xs = np.linspace(-16, 32, 300)
    densities = [gaussian_kde(rng.normal(mu, std, 500))(xs) for mu in means]
    dmax = max(d.max() for d in densities)
    step = dmax * 0.68

    cmap = mcolors.LinearSegmentedColormap.from_list("months", [style.DIM, style.ACCENT])
    colors = [cmap(t) for t in np.linspace(0.2, 1.0, 12)]

    fig, ax = style.new_fig(7.4, 5.4)
    offsets = [-(i) * step for i in range(12)]
    for i, (dens, color) in enumerate(zip(densities, colors)):
        base = offsets[i]
        ax.fill_between(xs, base, base + dens, color=color, alpha=0.92, zorder=100 - i, lw=0)
        ax.plot(xs, base + dens, color=color, lw=1.4, zorder=100 - i + 0.5)
    ax.set_yticks(offsets)
    ax.set_yticklabels(months)
    ax.set_ylim(offsets[-1] - step * 0.3, offsets[0] + dmax * 1.15)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("Temperature (°C)")
    ax.set_title("Monthly Temperature Distributions (synthetic)")
    style.save(fig, "viz_distributions_ii_ridgeline")


# ---------------------------------------------------------------------------
# avoid_line_drawings_iris_densities_{lines, filled}
# ---------------------------------------------------------------------------

def _iris_petal_kdes():
    iris = sns.load_dataset("iris")
    species = ["setosa", "versicolor", "virginica"]
    xs = np.linspace(iris["petal_length"].min() - 0.4, iris["petal_length"].max() + 0.4, 300)
    curves = {sp: gaussian_kde(iris.loc[iris["species"] == sp, "petal_length"])(xs) for sp in species}
    return species, xs, curves


def _iris_densities_lines():
    species, xs, curves = _iris_petal_kdes()
    fig, ax = style.new_fig(6.8, 4.0)
    for i, sp in enumerate(species):
        ax.plot(xs, curves[sp], color=style.CYCLE[i], lw=1.6, label=sp.capitalize())
    ax.legend(loc="upper right")
    ax.set_xlabel("Petal length (cm)")
    ax.set_ylabel("Density")
    ax.set_title("Iris Petal Length — Lines Only", color=style.BAD)
    style.save(fig, "viz_avoid_line_drawings_iris_densities_lines")


def _iris_densities_filled():
    species, xs, curves = _iris_petal_kdes()
    fig, ax = style.new_fig(6.8, 4.0)
    for i, sp in enumerate(species):
        color = style.CYCLE[i]
        dens = curves[sp]
        ax.fill_between(xs, dens, color=color, alpha=0.35, zorder=2)
        ax.plot(xs, dens, color=color, lw=1.6, zorder=3)
        peak = np.argmax(dens)
        ax.plot(xs[peak], dens[peak], "o", ms=5, color=color, zorder=4)
        ax.annotate(sp.capitalize(), xy=(xs[peak], dens[peak]),
                    xytext=(xs[peak], dens[peak] * 1.08 + 0.02),
                    color=style.FG, fontsize=10, ha="center")
    ax.set_xlabel("Petal length (cm)")
    ax.set_ylabel("Density")
    ax.set_title("Iris Petal Length — Filled")
    style.save(fig, "viz_avoid_line_drawings_iris_densities_filled")


FIGURES = {
    "viz_distributions_i_anscombes_quartet": _anscombes_quartet,
    "viz_distributions_i_titanic_density": _titanic_density,
    "viz_distributions_i_titanic_hist_binwidth": _titanic_hist_binwidth,
    "viz_distributions_i_titanic_ecdf": _titanic_ecdf,
    "viz_distributions_i_qq_plot": _qq_plot,
    "viz_distributions_ii_mpg_boxplot": _mpg_boxplot,
    "viz_distributions_ii_mpg_strip_jitter": _mpg_strip_jitter,
    "viz_distributions_ii_mpg_violin": _mpg_violin,
    "viz_distributions_ii_ridgeline": _ridgeline,
    "viz_avoid_line_drawings_iris_densities_lines": _iris_densities_lines,
    "viz_avoid_line_drawings_iris_densities_filled": _iris_densities_filled,
}
