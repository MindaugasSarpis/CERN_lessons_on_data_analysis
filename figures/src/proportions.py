"""Visualising Proportions: pies, stacks, side-by-side bars, and a treemap.

Six figures for lectures/content/slides/10_Data_Visualisation.md:
  - the "three ways, one story" trio (pie_bad / stacked_bar / side_by_side_bars)
    showing ONE synthetic survey, same colours per category throughout, so the
    pie's angle-judgement problem is directly contrasted with the bars' direct
    value read;
  - the "when pies actually work" pair (bundestag_pie_good / marketshare_pies_bad)
    contrasting a single unambiguous whole with few, clearly-different slices
    against many small multiples with near-identical wedges;
  - a treemap for nested (2-level) proportions, laid out with a ~20-line inline
    squarified-treemap implementation (Bruls, Huizing & van Wijk, 1999) rather
    than pulling in the `squarify` package.

All data is synthetic/illustrative except the 1976 Bundestag seat counts,
which are the real historical result.
"""
import numpy as np
from matplotlib.patches import Patch, Rectangle

import style

BG = "#050507"     # course dark canvas — used as the stroke between fills
INK = "#12161c"    # near-black — legible text set ON TOP of light CYCLE fills

# ---------------------------------------------------------------------------
# "Three ways, one story": one synthetic survey, shared across three charts.
# ---------------------------------------------------------------------------
TRIO_LABELS = ["Python", "R", "Excel / Sheets", "MATLAB", "Julia", "Other"]


def _trio_values():
    """Six similar-sized shares (sum 100) — deliberately hard to rank by eye."""
    rng = np.random.default_rng(11)
    base = np.clip(rng.normal(100 / 6, 3.2, size=6), 10, None)
    vals = np.round(base / base.sum() * 100).astype(int)
    vals[0] += 100 - vals.sum()  # fix rounding drift, keep sum exactly 100
    return vals


TRIO_COLORS = dict(zip(TRIO_LABELS, style.CYCLE[:6]))


def _pie_bad():
    """6-slice pie, similar-sized wedges, NO value labels — forces the reader
    into angle/area judgement, which is exactly what fails."""
    vals = _trio_values()
    colors = [TRIO_COLORS[l] for l in TRIO_LABELS]
    fig, ax = style.new_fig(6.2, 4.4)
    ax.axis("off")
    wedges, _ = ax.pie(
        vals, colors=colors, startangle=90, counterclock=False,
        wedgeprops=dict(edgecolor=BG, linewidth=1.5),
    )
    ax.set_title("Preferred Analysis Tool — Survey (n=240)")
    ax.legend(wedges, TRIO_LABELS, loc="center left", bbox_to_anchor=(1.0, 0.5))
    style.save(fig, "viz_proportions_pie_bad")


def _side_by_side_bars():
    """Same survey, sorted bars — the winner is obvious at a glance."""
    vals = _trio_values()
    order = np.argsort(vals)[::-1]
    labels = [TRIO_LABELS[i] for i in order]
    sorted_vals = vals[order]
    # One colour: position on the common axis carries the value, so a
    # per-category hue would only be redundant ink.
    fig, ax = style.new_fig(7.2, 4.4)
    bars = ax.bar(labels, sorted_vals, color=style.ACCENT, width=0.62)
    ax.bar_label(bars, fmt="%d%%", padding=3, color=style.FG, fontsize=10)
    ax.set_ylabel("Share of respondents (%)")
    ax.set_ylim(0, max(sorted_vals) * 1.22)
    ax.grid(axis="x", visible=False)  # keep only the horizontal (y) gridlines
    ax.set_title("Preferred Analysis Tool — Same Data as Bars")
    style.save(fig, "viz_proportions_proportions_side_by_side_bars")


def _stacked_bar():
    """Same survey, one 100%-stacked bar — good for reading part-of-whole."""
    vals = _trio_values()
    fig, ax = style.new_fig(7.6, 2.7)
    left = 0.0
    for label, v in zip(TRIO_LABELS, vals):
        ax.barh(0, v, left=left, height=0.6, color=TRIO_COLORS[label],
                edgecolor=BG, linewidth=1.5)
        if v >= 8:  # only label segments wide enough to hold text
            ax.text(left + v / 2, 0, f"{v}%", ha="center", va="center",
                    color=INK, fontsize=10, fontweight="bold")
        left += v
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.6, 0.6)
    ax.set_yticks([])
    ax.set_xlabel("Share of respondents (%)")
    ax.grid(False)  # the single bar covers the whole axes — gridlines add nothing
    ax.set_title("Preferred Analysis Tool — One Stacked Bar")
    handles = [Patch(facecolor=TRIO_COLORS[l], label=l) for l in TRIO_LABELS]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.32),
              ncol=3)
    style.save(fig, "viz_proportions_proportions_stacked_bar")


# ---------------------------------------------------------------------------
# "When pies actually work": one unambiguous whole vs. many small multiples.
# ---------------------------------------------------------------------------
def _bundestag_pie_good():
    """1976 Bundestag: 3 clearly-different slices, one unambiguous whole —
    the SPD-FDP coalition's slim majority is the whole story."""
    labels = ["CDU/CSU", "SPD", "FDP"]
    seats = [243, 214, 39]  # real 8th Bundestag result, 496 seats total
    colors = style.CYCLE[:3]
    fig, ax = style.new_fig(5.8, 4.5)
    ax.axis("off")
    wedges, _, autotexts = ax.pie(
        seats, colors=colors, startangle=90, counterclock=False,
        autopct="%1.0f%%", pctdistance=0.72,
        wedgeprops=dict(edgecolor=BG, linewidth=1.5),
    )
    for t in autotexts:
        t.set_color(INK)
        t.set_fontweight("bold")
    ax.legend(wedges, [f"{l} ({s} seats)" for l, s in zip(labels, seats)],
              loc="center left", bbox_to_anchor=(0.98, 0.5))
    ax.set_title("1976 Bundestag — One Legislature, One Whole")
    ax.text(0, -1.32, "SPD + FDP = 51% → governing majority",
            ha="center", va="top", fontsize=10, style="italic", color=style.DIM)
    style.save(fig, "viz_proportions_bundestag_pie_good")


def _marketshare_pies_bad():
    """3 pies across years: Nimbus fades from 1st to tied-last, Solace rises
    to 1st — but split across separate wedges the trend is nearly invisible."""
    companies = ["Nimbus", "Solace", "Vertex", "Others"]
    years = {2021: [30, 24, 24, 22], 2022: [27, 27, 24, 22], 2023: [24, 30, 24, 22]}
    colors = style.CYCLE[:4]
    fig, axes = style.plt.subplots(1, 3, figsize=(9.6, 3.9))
    for ax, (year, vals) in zip(axes, years.items()):
        ax.axis("off")
        wedges = ax.pie(
            vals, colors=colors, startangle=90, counterclock=False,
            wedgeprops=dict(edgecolor=BG, linewidth=1.3),
        )[0]
        ax.set_title(str(year), fontsize=13)
    fig.legend(wedges, companies, loc="lower center", ncol=4,
               bbox_to_anchor=(0.5, -0.04))
    fig.suptitle("Market Share, 2021–2023 — Spot the Trend?", fontsize=13,
                 fontweight="bold")
    style.save(fig, "viz_proportions_marketshare_pies_bad")


# ---------------------------------------------------------------------------
# Treemap: inline squarified layout (Bruls, Huizing & van Wijk, 1999).
# ---------------------------------------------------------------------------
def _squarify(values, x, y, w, h):
    """Squarified treemap rects for `values` (any order; areas need not be
    pre-sorted by the caller for correctness, only for near-square results).
    Precondition: sum(values) == w * h. Returns [(x, y, w, h), ...] aligned
    index-for-index with `values`."""
    if not values:
        return []
    if len(values) == 1:
        return [(x, y, w, h)]
    side = min(w, h)

    def worst(row):
        s, lo, hi = sum(row), min(row), max(row)
        return max(side * side * hi / s / s, s * s / (side * side * lo))

    row = [values[0]]
    for v in values[1:]:
        if worst(row + [v]) <= worst(row):
            row.append(v)
        else:
            break
    thickness = sum(row) / side
    rects = []
    if w >= h:  # lay `row` as a column at the left, items stacked vertically
        cy = y
        for v in row:
            rh = v / thickness
            rects.append((x, cy, thickness, rh))
            cy += rh
        rects += _squarify(values[len(row):], x + thickness, y, w - thickness, h)
    else:  # lay `row` as a strip along the top, items placed left-to-right
        cx = x
        for v in row:
            rw = v / thickness
            rects.append((cx, y, rw, thickness))
            cx += rw
        rects += _squarify(values[len(row):], x, y + thickness, w, h - thickness)
    return rects


def _treemap():
    groups = {
        "Data Analysis": {"Coding": 46, "Debugging": 24, "Plotting": 15, "Cleaning": 10},
        "Writing": {"Thesis": 30, "Paper": 22, "Docs": 8},
        "Meetings": {"Group meeting": 13, "Seminar": 10, "Standup": 5},
        "Admin": {"Email": 10, "Travel": 7},
    }
    group_order = sorted(groups, key=lambda g: sum(groups[g].values()), reverse=True)
    total_all = sum(sum(v.values()) for v in groups.values())

    W, H = 20.0, 11.0
    k = (W * H) / total_all  # scale factor: value -> area, exact by construction

    group_totals = [sum(groups[g].values()) * k for g in group_order]
    group_rects = _squarify(group_totals, 0, 0, W, H)
    group_colors = dict(zip(group_order, style.CYCLE[:4]))

    fig, ax = style.new_fig(8.0, 4.7)
    ax.axis("off")
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal")

    for g, (gx, gy, gw, gh) in zip(group_order, group_rects):
        leaves = groups[g]
        leaf_labels = sorted(leaves, key=leaves.get, reverse=True)
        leaf_areas = [leaves[l] * k for l in leaf_labels]
        leaf_rects = _squarify(leaf_areas, gx, gy, gw, gh)
        n = len(leaf_labels)
        alphas = np.linspace(1.0, 0.5, n) if n > 1 else [1.0]
        for label, (lx, ly, lw, lh), a in zip(leaf_labels, leaf_rects, alphas):
            ax.add_patch(Rectangle((lx, ly), lw, lh, facecolor=group_colors[g],
                                    alpha=a, edgecolor=BG, linewidth=1.2))
            if lw > 2.2 and lh > 1.1:
                ax.text(lx + lw / 2, ly + lh / 2 + 0.18, label, ha="center",
                        va="center", fontsize=8.5, color=INK, fontweight="bold",
                        clip_on=True)
                ax.text(lx + lw / 2, ly + lh / 2 - 0.28, f"{leaves[label]} h",
                        ha="center", va="center", fontsize=7.5, color=INK,
                        clip_on=True)
        ax.add_patch(Rectangle((gx, gy), gw, gh, facecolor="none",
                                edgecolor=style.FG, linewidth=2.2))

    ax.set_title("How a Research Month Is Spent (hours)")
    handles = [Patch(facecolor=group_colors[g],
                      label=f"{g} ({sum(groups[g].values())} h)") for g in group_order]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=4)
    style.save(fig, "viz_proportions_treemap")


FIGURES = {
    "viz_proportions_pie_bad": _pie_bad,
    "viz_proportions_proportions_side_by_side_bars": _side_by_side_bars,
    "viz_proportions_proportions_stacked_bar": _stacked_bar,
    "viz_proportions_bundestag_pie_good": _bundestag_pie_good,
    "viz_proportions_marketshare_pies_bad": _marketshare_pies_bad,
    "viz_proportions_treemap": _treemap,
}
