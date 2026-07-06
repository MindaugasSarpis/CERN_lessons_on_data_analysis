"""Story family: annotation, titles, reference lines, context, uncertainty.

Fourteen figures for the "Telling a Story", "Balance Data & Context", and
"Visualising Uncertainty" sections of lecture 10. Datasets are synthetic
(fixed seeds) except Titanic, which is the seaborn bundled sample.
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle

import style

RNG = np.random.default_rng(2025)


# ---------------------------------------------------------------------------
# Telling a story
# ---------------------------------------------------------------------------

def _annotated_vs_plain():
    x = np.linspace(0, 10, 120)
    y = 12 + 1.2 * x + 30 / (1 + np.exp(-(x - 6.2) * 2.2))
    y += RNG.normal(0, 0.5, x.size)

    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.2))
    for ax in axes:
        ax.plot(x, y, color=style.ACCENT, lw=2.2)
        ax.set_xlabel("week"); ax.set_ylabel("active users (k)")
        ax.set_xlim(0, 10)
    axes[0].set_title("Plain")
    axes[1].set_title("Annotated")
    i = int(np.argmin(np.abs(x - 6.2)))
    axes[1].annotate(
        "feature launched here",
        xy=(x[i], y[i]), xytext=(1.0, y.max() * 0.92),
        color=style.FG, fontsize=10.5,
        arrowprops=dict(arrowstyle="->", color=style.CYCLE[1], lw=1.6),
    )
    axes[1].scatter([x[i]], [y[i]], s=45, color=style.CYCLE[1], zorder=4)
    style.save(fig, "viz_telling_a_story_annotated_vs_plain")


def _story_titles_captions():
    years = np.arange(2019, 2026)
    sales = np.array([102, 108, 112, 118, 165, 210, 245.0])

    # Manual axes placement: constrained_layout (course default) would fight
    # the fixed-fraction title/subtitle/caption zones below, so this figure
    # opts out and lays itself out by hand.
    fig = plt.figure(figsize=(7.4, 4.6), layout="none")
    ax = fig.add_axes((0.12, 0.24, 0.84, 0.50))
    ax.plot(years, sales, "o-", color=style.ACCENT, lw=2.2, ms=6)
    ax.set_xlabel("year"); ax.set_ylabel("sales ($M)")

    fig.text(0.02, 0.925, "Sales doubled after 2022", fontsize=15,
              fontweight="bold", color=style.FG, ha="left", va="center")
    fig.text(0.02, 0.825, "Annual revenue, 2019–2025, all regions", fontsize=11,
              color=style.DIM, ha="left", va="center")
    fig.text(0.02, 0.05, "Source: internal finance dashboard, synthetic figures for illustration.",
              fontsize=8.5, color=style.DIM, ha="left", va="center")

    def zone(y0, y1, label, color):
        fig.add_artist(Rectangle(
            (0.01, y0), 0.98, y1 - y0, transform=fig.transFigure, clip_on=False,
            fill=False, ls="--", lw=1.1, color=color))
        fig.text(0.99, (y0 + y1) / 2, label, fontsize=9, color=color,
                  ha="right", va="center", fontstyle="italic")

    zone(0.86, 0.99, "TITLE", style.CYCLE[1])
    zone(0.79, 0.86, "SUBTITLE", style.CYCLE[2])
    zone(0.01, 0.09, "CAPTION", style.CYCLE[2])
    style.save(fig, "viz_telling_a_story_story_titles_captions")


def _title_as_finding():
    years = np.arange(2019, 2026)
    sales = np.array([102, 108, 112, 118, 165, 210, 245.0])

    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.2))
    for ax, title in zip(axes, ["Sales 2019–2025", "Sales doubled after 2022"]):
        ax.plot(years, sales, "o-", color=style.ACCENT, lw=2.2, ms=6)
        ax.set_xlabel("year"); ax.set_ylabel("sales ($M)")
        ax.set_title(title, fontsize=13.5)
    axes[1].axvspan(2022, 2025.3, color=style.CYCLE[1], alpha=0.12, lw=0)
    style.save(fig, "viz_telling_a_story_title_as_finding")


# ---------------------------------------------------------------------------
# Balance data & context
# ---------------------------------------------------------------------------

def _gene_expression_data():
    rng = np.random.default_rng(2104)  # local: paired figures must share identical data
    n = 220
    wt = rng.lognormal(mean=3.0, sigma=0.9, size=n)
    mut = wt * rng.lognormal(mean=0.0, sigma=0.18, size=n)
    # a handful of genuinely differentially-expressed genes
    idx = rng.choice(n, 10, replace=False)
    mut[idx[:5]] *= rng.uniform(2.5, 5, 5)
    mut[idx[5:]] /= rng.uniform(2.5, 5, 5)
    return wt, mut, idx


def _gene_expression_bad():
    wt, mut, _ = _gene_expression_data()
    fig, ax = plt.subplots(figsize=(5.2, 4.6))
    ax.scatter(wt, mut, s=16, color=style.ACCENT, alpha=0.75, edgecolor="none")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("wild-type abundance (a.u.)")
    ax.set_ylabel("mutant abundance (a.u.)")
    style.save(fig, "viz_balance_data_context_gene_expression_bad")


def _gene_expression_good():
    wt, mut, idx = _gene_expression_data()
    fig, ax = plt.subplots(figsize=(5.2, 4.6))
    lims = (min(wt.min(), mut.min()) * 0.7, max(wt.max(), mut.max()) * 1.3)
    ax.plot(lims, lims, "--", color=style.DIM, lw=1.3, zorder=1)
    mask = np.zeros(wt.size, dtype=bool); mask[idx] = True
    ax.scatter(wt[~mask], mut[~mask], s=16, color=style.ACCENT, alpha=0.7, edgecolor="none", zorder=2)
    ax.scatter(wt[mask], mut[mask], s=34, color=style.BAD, edgecolor=style.FG, linewidth=0.5,
               zorder=3, label="differentially expressed")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(lims); ax.set_ylim(lims)
    ax.set_xlabel("wild-type abundance (a.u.)")
    ax.set_ylabel("mutant abundance (a.u.)")
    ax.legend(loc="upper left")
    style.save(fig, "viz_balance_data_context_gene_expression_good")


def _grid_vs_no_grid():
    x = RNG.uniform(0, 10, 90)
    y = 2.1 * x + RNG.normal(0, 3.2, 90)

    fig, (bad, good) = plt.subplots(1, 2, figsize=(9.6, 4.3))

    bad.set_facecolor("#232a36")
    bad.scatter(x, y, s=22, color=style.ACCENT, edgecolor="none")
    bad.grid(True, which="major", color="#4a5568", linewidth=1.1)
    bad.minorticks_on()
    bad.grid(True, which="minor", color="#3a4353", linewidth=0.6)
    for s in bad.spines.values():
        s.set_visible(True); s.set_color(style.DIM); s.set_linewidth(1.2)
    bad.tick_params(which="both", direction="in", top=True, right=True, color=style.DIM)
    bad.set_title("Default: heavy grid, boxed axes")
    bad.set_xlabel("x"); bad.set_ylabel("y")

    good.scatter(x, y, s=22, color=style.ACCENT, edgecolor="none")
    good.grid(True, axis="y", color=style.GRID, linewidth=0.6)
    good.spines["left"].set_visible(False)
    good.set_title("Less ink, same data")
    good.set_xlabel("x"); good.set_ylabel("y")

    style.save(fig, "viz_balance_data_context_grid_vs_no_grid")


def _price_series():
    rng = np.random.default_rng(2105)  # local: paired figures must share identical data
    days = np.arange(180)
    steps = rng.normal(0.15, 2.0, days.size)
    price = 100 + np.cumsum(steps)
    return days, price


def _price_plot_ggplot_default():
    days, price = _price_series()
    fig, ax = plt.subplots(figsize=(5.4, 3.9))
    ax.set_facecolor("#232a36")
    ax.plot(days, price, color=style.ACCENT, lw=1.8)
    ax.grid(True, which="major", color="#4a5568", linewidth=1.1)
    ax.minorticks_on()
    ax.grid(True, which="minor", color="#3a4353", linewidth=0.6)
    for s in ax.spines.values():
        s.set_visible(True); s.set_color(style.DIM); s.set_linewidth(1.2)
    ax.tick_params(which="both", direction="in", top=True, right=True, color=style.DIM)
    ax.set_xlabel("trading day"); ax.set_ylabel("price ($)")
    style.save(fig, "viz_balance_data_context_price_plot_ggplot_default")


def _price_plot_no_grid():
    days, price = _price_series()
    fig, ax = plt.subplots(figsize=(5.4, 3.9))
    ax.plot(days, price, color=style.ACCENT, lw=2.0)
    ax.grid(False)
    ax.set_xlabel("trading day"); ax.set_ylabel("price ($)")
    style.save(fig, "viz_balance_data_context_price_plot_no_grid")


def _titanic_rates():
    df = sns.load_dataset("titanic").dropna(subset=["survived", "pclass", "sex"])
    rates = df.groupby(["pclass", "sex"])["survived"].mean().unstack()
    return rates  # index 1,2,3; columns female, male


def _titanic_survival_bad():
    rates = _titanic_rates()
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.6))
    for ax, cls in zip(axes, [1, 2, 3]):
        vals = rates.loc[cls, ["female", "male"]].to_numpy()
        ax.bar(["F", "M"], vals, color=[style.ACCENT, style.CYCLE[1]], width=0.55)
        ax.set_ylim(0, vals.max() * 1.15)  # each panel autoscaled to its own max
        ax.set_title(f"Class {cls}")
        ax.set_ylabel("survival rate" if cls == 1 else "")
    style.save(fig, "viz_balance_data_context_titanic_survival_bad")


def _titanic_survival_good():
    rates = _titanic_rates()
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.6))
    for ax, cls in zip(axes, [1, 2, 3]):
        vals = rates.loc[cls, ["female", "male"]].to_numpy()
        ax.bar(["F", "M"], vals, color=[style.ACCENT, style.CYCLE[1]], width=0.55)
        ax.set_ylim(0, 1)  # shared scale across all panels
        ax.set_title(f"Class {cls}")
        ax.set_ylabel("survival rate" if cls == 1 else "")
    style.save(fig, "viz_balance_data_context_titanic_survival_good")


# ---------------------------------------------------------------------------
# Visualising uncertainty
# ---------------------------------------------------------------------------

def _error_bars():
    groups = ["A", "B", "C", "D", "E"]
    means = np.array([4.8, 6.1, 5.3, 7.4, 6.6])
    se = np.array([0.35, 0.5, 0.25, 0.6, 0.4])
    order = np.argsort(means)

    fig, ax = plt.subplots(figsize=(4.2, 3.3))
    y = np.arange(len(groups))
    ax.errorbar(means[order], y, xerr=se[order], fmt="o", ms=7,
                color=style.ACCENT, ecolor=style.DIM, elinewidth=1.6, capsize=4)
    ax.set_yticks(y, [groups[i] for i in order])
    ax.set_xlabel("mean response ± SE")
    ax.grid(True, axis="x", color=style.GRID, linewidth=0.6)
    ax.grid(False, axis="y")
    style.save(fig, "viz_uncertainty_error_bars")


def _ci_band():
    n = 60
    x = RNG.uniform(0, 10, n)
    y = 3 + 1.6 * x + RNG.normal(0, 2.6, n)
    xs = np.linspace(0, 10, 200)

    boots = np.empty((400, xs.size))
    for i in range(400):
        idx = RNG.integers(0, n, n)
        b, a = np.polyfit(x[idx], y[idx], 1)
        boots[i] = a + b * xs
    lo, hi = np.percentile(boots, [2.5, 97.5], axis=0)
    b, a = np.polyfit(x, y, 1)
    fit = a + b * xs

    fig, ax = plt.subplots(figsize=(4.2, 3.3))
    ax.scatter(x, y, s=18, color=style.DIM, alpha=0.6, edgecolor="none", zorder=2)
    ax.fill_between(xs, lo, hi, color=style.ACCENT, alpha=0.22, lw=0, zorder=1)
    ax.plot(xs, fit, color=style.ACCENT, lw=2.2, zorder=3)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    style.save(fig, "viz_uncertainty_ci_band")


def _quantile_dot():
    n_dots = 100
    q = (np.arange(n_dots) + 0.5) / n_dots
    # inverse-normal via rational approximation-free: use numpy's percent point
    # function through a standard normal sample large draw + sort (avoids scipy)
    draws = np.sort(RNG.normal(51.5, 3.2, 200_000))
    outcomes = draws[(q * (draws.size - 1)).astype(int)]

    bin_width = 1.0
    bins = np.round(outcomes / bin_width) * bin_width
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    counts = {}
    for v in np.sort(bins):
        counts[v] = counts.get(v, 0) + 1
        color = style.ACCENT if v >= 50 else style.CYCLE[1]
        ax.scatter(v, counts[v], s=42, color=color, edgecolor="none", zorder=3)
    ax.axvline(50, color=style.FG, lw=1.2, ls="--", zorder=2)
    ax.text(50.15, max(counts.values()) + 1, "50% — tossup line", color=style.FG,
            fontsize=9.5, va="bottom")
    ax.set_xlabel("candidate A vote share (%)")
    ax.set_ylabel("draws in this bin")
    ax.set_yticks([])
    for s in ["left", "top", "right"]:
        ax.spines[s].set_visible(False)
    style.save(fig, "viz_uncertainty_election_quantile_dot")


def _hop_demo():
    n = 40
    x = RNG.uniform(0, 10, n)
    y = 3 + 1.6 * x + RNG.normal(0, 2.6, n)
    xs = np.linspace(0, 10, 200)

    fig, ax = plt.subplots(figsize=(4.4, 3.4), layout="none")  # manual bottom margin for caption
    fig.subplots_adjust(bottom=0.24, left=0.14, right=0.96, top=0.95)
    for _ in range(28):
        idx = RNG.integers(0, n, n)
        b, a = np.polyfit(x[idx], y[idx], 1)
        ax.plot(xs, a + b * xs, color=style.ACCENT, lw=1.0, alpha=0.18, zorder=1)
    b, a = np.polyfit(x, y, 1)
    ax.plot(xs, a + b * xs, color=style.CYCLE[1], lw=2.6, zorder=3)
    ax.scatter(x, y, s=16, color=style.DIM, alpha=0.6, edgecolor="none", zorder=2)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    fig.text(0.5, 0.03, "one plausible world per frame", ha="center",
              fontsize=10, color=style.DIM, fontstyle="italic")
    style.save(fig, "viz_uncertainty_hop_demo")


FIGURES = {
    "viz_telling_a_story_annotated_vs_plain": _annotated_vs_plain,
    "viz_telling_a_story_story_titles_captions": _story_titles_captions,
    "viz_telling_a_story_title_as_finding": _title_as_finding,
    "viz_balance_data_context_gene_expression_bad": _gene_expression_bad,
    "viz_balance_data_context_gene_expression_good": _gene_expression_good,
    "viz_balance_data_context_grid_vs_no_grid": _grid_vs_no_grid,
    "viz_balance_data_context_price_plot_ggplot_default": _price_plot_ggplot_default,
    "viz_balance_data_context_price_plot_no_grid": _price_plot_no_grid,
    "viz_balance_data_context_titanic_survival_bad": _titanic_survival_bad,
    "viz_balance_data_context_titanic_survival_good": _titanic_survival_good,
    "viz_uncertainty_error_bars": _error_bars,
    "viz_uncertainty_ci_band": _ci_band,
    "viz_uncertainty_election_quantile_dot": _quantile_dot,
    "viz_uncertainty_hop_demo": _hop_demo,
}
