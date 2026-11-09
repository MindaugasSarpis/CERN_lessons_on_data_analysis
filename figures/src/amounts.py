"""Amounts family: bars, dots, and heatmaps for comparing quantities across
categories (deck 10, "Visualizing Amounts" + "Proportional Ink" sections).
Data are synthetic-but-plausible (seeded RNGs) or small hardcoded arrays reused
identically across "good" vs "bad" variants of the same story.
"""
import textwrap

import numpy as np
import matplotlib.pyplot as plt

import style

# ---------------------------------------------------------------------------
# Box office: 5 (fictional) films, opening-weekend gross ($M). Long titles are
# chosen deliberately so the "bad" vertical-bar variant forces label rotation.
FILMS = [
    "Guardian of the Nebula",
    "Midnight in Marrakesh",
    "The Last Cartographer",
    "Wreckage of Tomorrow",
    "Silver Hour",
]
GROSS = [82.4, 61.7, 47.9, 33.2, 21.5]  # already sorted desc


def _boxoffice_horizontal():
    fig, ax = style.new_fig(7, 4.2)
    y = np.arange(len(FILMS))
    ax.barh(y, GROSS, color=style.ACCENT, height=0.6, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(FILMS)
    ax.invert_yaxis()
    ax.set_xlim(0, max(GROSS) * 1.18)
    ax.set_xlabel("Opening weekend gross ($M)")
    ax.set_title("Opening-Weekend Box Office")
    ax.grid(axis="y", visible=False)
    for yi, v in zip(y, GROSS):
        ax.text(v + 1.5, yi, f"${v:.0f}M", va="center", color=style.DIM, fontsize=9)
    style.save(fig, "viz_amounts_boxoffice_horizontal")


def _boxoffice_rotated_bad():
    fig, ax = style.new_fig(7, 5.0)
    x = np.arange(len(FILMS))
    ax.bar(x, GROSS, color=style.ACCENT, width=0.6, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(FILMS, rotation=45, ha="right")
    for lbl in ax.get_xticklabels():
        lbl.set_color(style.BAD)  # accent the flaw: labels, not the data
    ax.set_ylabel("Opening weekend gross ($M)")
    ax.set_title("Opening-Weekend Box Office")
    ax.grid(axis="x", visible=False)
    style.save(fig, "viz_amounts_boxoffice_rotated_bad")


def _boxoffice_wide():
    """The vertical bars spread over the width of the slide: each title has
    room under its bar, level, wrapped onto two lines."""
    fig, ax = style.new_fig(9.4, 3.3)
    x = np.arange(len(FILMS))
    ax.bar(x, GROSS, color=style.ACCENT, width=0.5, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels([textwrap.fill(f, 14) for f in FILMS], fontsize=11)
    ax.set_ylim(0, max(GROSS) * 1.15)
    ax.set_ylabel("Opening weekend gross ($M)")
    ax.set_title("Opening-Weekend Box Office")
    ax.grid(axis="x", visible=False)
    for xi, v in zip(x, GROSS):
        ax.text(xi, v + 1.5, f"${v:.0f}M", ha="center", va="bottom", color=style.DIM, fontsize=9)
    style.save(fig, "viz_amounts_boxoffice_wide")


def _cleveland_dot_plot():
    fig, ax = style.new_fig(7, 4.2)
    y = np.arange(len(FILMS))
    ax.hlines(y, 0, GROSS, color=style.GRID, linewidth=1.4, zorder=1)
    ax.plot(GROSS, y, "o", ms=9, color=style.ACCENT, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(FILMS)
    ax.invert_yaxis()
    ax.set_xlim(0, max(GROSS) * 1.18)
    ax.set_xlabel("Opening weekend gross ($M)")
    ax.set_title("Same Data, Cleveland Dot Plot")
    ax.grid(axis="y", visible=False)
    style.save(fig, "viz_amounts_cleveland_dot_plot")


# ---------------------------------------------------------------------------
# Life expectancy at birth, years, rounded: approximate values for about 2019
# (WHO Global Health Observatory), so that the order of the countries is real.
LIFE_EXPECTANCY = {
    "Japan": 84, "Switzerland": 83, "Spain": 83, "Australia": 83, "Italy": 83,
    "Norway": 83, "France": 83, "Sweden": 82, "Canada": 82, "Germany": 81,
    "United Kingdom": 81, "Denmark": 81, "Chile": 81, "United States": 79,
    "Poland": 78, "China": 77, "Argentina": 77, "Mexico": 76, "Brazil": 76,
    "Russia": 73, "Egypt": 72, "India": 71, "Kenya": 66, "South Africa": 65,
    "Nigeria": 63, "Chad": 60,
}
COUNTRIES = list(LIFE_EXPECTANCY)
LIFE_TITLE = "Life expectancy at birth, 26 countries, about 2019"


def _lifeexp_data():
    return COUNTRIES, np.array([LIFE_EXPECTANCY[c] for c in COUNTRIES], dtype=float)


def _lifeexp_alpha_order_bad():
    countries, values = _lifeexp_data()
    order = np.argsort(countries)
    countries = [countries[i] for i in order]
    values = values[order]
    fig, ax = style.new_fig(7, 6.6)
    y = np.arange(len(countries))
    ax.barh(y, values, color=style.BAD, height=0.65, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(countries, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(0, 86)
    ax.set_xlabel("Life expectancy (years)")
    ax.set_title(LIFE_TITLE)
    ax.grid(axis="y", visible=False)
    style.save(fig, "viz_amounts_lifeexp_alpha_order_bad")


def _lifeexp_bars_bad():
    countries, values = _lifeexp_data()
    order = np.argsort(values)[::-1]
    countries = [countries[i] for i in order]
    values = values[order]
    fig, ax = style.new_fig(7, 6.6)
    y = np.arange(len(countries))
    ax.barh(y, values, color=style.BAD, height=0.65, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(countries, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(0, 86)
    ax.set_xlabel("Life expectancy (years)")
    ax.set_title(LIFE_TITLE)
    ax.grid(axis="y", visible=False)
    style.save(fig, "viz_amounts_lifeexp_bars_bad")


def _lifeexp_dot_plot():
    countries, values = _lifeexp_data()
    order = np.argsort(values)[::-1]
    countries = [countries[i] for i in order]
    values = values[order]
    fig, ax = style.new_fig(7, 6.6)
    y = np.arange(len(countries))
    ax.plot(values, y, "o", ms=6, color=style.ACCENT, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(countries, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(58, 86)  # honest truncation is fine for dots, not bars
    ax.set_xlabel("Life expectancy (years)")
    ax.set_title(LIFE_TITLE)
    ax.grid(axis="y", visible=False)
    style.save(fig, "viz_amounts_lifeexp_dot_plot")


# ---------------------------------------------------------------------------
# Health heatmap: a 12-country subset x 8 decades (1950s-2020s), synthetic
# improvement trend (higher-baseline countries rise slowly, lower-baseline
# countries catch up faster) — a plausible, visually clear gradient.
HEATMAP_COUNTRY_PROFILES = {
    "Norway": (68, 1.8),
    "Japan": (62, 2.6),
    "Canada": (69, 1.6),
    "Germany": (67, 1.7),
    "Spain": (64, 2.1),
    "Argentina": (61, 1.9),
    "Brazil": (50, 2.6),
    "Mexico": (49, 2.5),
    "Egypt": (42, 2.9),
    "India": (38, 3.4),
    "Kenya": (36, 3.0),
    "Chad": (33, 2.4),
}
DECADES = list(range(1950, 2021, 10))  # 1950s..2020s, 8 decades


def _health_heatmap_data():
    rng = np.random.default_rng(77)
    countries = list(HEATMAP_COUNTRY_PROFILES)
    rows = []
    for start, gain in HEATMAP_COUNTRY_PROFILES.values():
        decade_idx = np.arange(len(DECADES))
        noise = rng.normal(0, 1.0, len(DECADES))
        rows.append(np.clip(start + gain * decade_idx + noise, 30, 84))
    return countries, DECADES, np.array(rows)


def _health_heatmap():
    countries, decades, grid = _health_heatmap_data()
    fig, ax = style.new_fig(7.8, 5.4)
    mesh = ax.pcolormesh(grid, cmap="cividis", edgecolors=style.GRID, linewidth=1.0)
    ax.set_xticks(np.arange(len(decades)) + 0.5)
    ax.set_xticklabels([f"{d}s" for d in decades])
    ax.set_yticks(np.arange(len(countries)) + 0.5)
    ax.set_yticklabels(countries)
    ax.invert_yaxis()
    ax.set_title("Life Expectancy by Country and Decade")
    ax.grid(False)
    cb = fig.colorbar(mesh, ax=ax, shrink=0.85, pad=0.02)
    cb.set_label("Life expectancy (years)", color=style.DIM)
    cb.outline.set_edgecolor(style.DIM)
    cb.ax.tick_params(colors=style.DIM)
    style.save(fig, "viz_amounts_health_heatmap")


# ---------------------------------------------------------------------------
# Stacked bars: student enrolment by year x programme (part-to-whole).
YEARS = ["2021", "2022", "2023", "2024"]
ENROLMENT = {
    "Bachelor": [120, 128, 135, 142],
    "Master": [64, 70, 75, 81],
    "PhD": [18, 21, 23, 26],
}


# ---------------------------------------------------------------------------
# Median household income by age of the householder, USA 2016 (US Census
# Bureau, the example of Wilke, Fundamentals of Data Visualization, ch. 6), in
# thousand dollars, rounded. The age groups are ordinal.
AGE_GROUPS = ["15–24", "25–34", "35–44", "45–54", "55–64", "65–74", "75+"]
INCOME = [42, 61, 74, 77, 65, 49, 31]


def _income_bars(order, name, bad):
    groups = [AGE_GROUPS[i] for i in order]
    values = [INCOME[i] for i in order]
    fig, ax = style.new_fig(5.1, 3.4)
    x = np.arange(len(groups))
    ax.bar(x, values, color=style.ACCENT, width=0.65, zorder=3)
    ax.set_xticks(x, groups)
    if bad:
        for lbl in ax.get_xticklabels():
            lbl.set_color(style.BAD)   # the flaw is the order of the labels
    for xi, v in zip(x, values):
        ax.text(xi, v + 1.5, f"{v}", ha="center", va="bottom", color=style.DIM, fontsize=9)
    ax.set_ylim(0, 88)
    ax.set_xlabel("age of the householder (years)")
    ax.set_ylabel("median income (thousand $)")
    ax.grid(axis="x", visible=False)
    style.save(fig, name)


def _income_by_value_bad():
    _income_bars(sorted(range(len(INCOME)), key=lambda i: -INCOME[i]),
                 "viz_amounts_income_by_value_bad", bad=True)


def _income_by_age_good():
    _income_bars(range(len(INCOME)), "viz_amounts_income_by_age_good", bad=False)


def _students_stacked_bars():
    fig, ax = style.new_fig(7, 4.4)
    x = np.arange(len(YEARS))
    bottom = np.zeros(len(YEARS))
    for programme, color in zip(ENROLMENT, style.CYCLE):
        vals = np.array(ENROLMENT[programme])
        ax.bar(x, vals, bottom=bottom, label=programme, color=color,
               width=0.55, edgecolor="#050507", linewidth=1.2, zorder=3)
        bottom += vals
    ax.set_xticks(x)
    ax.set_xticklabels(YEARS)
    ax.set_ylabel("Students enrolled")
    ax.set_title("Enrolment by Year and Programme")
    ax.grid(axis="x", visible=False)
    h, l = ax.get_legend_handles_labels()   # legend in the order of the stack
    ax.legend(h[::-1], l[::-1], loc="upper left", bbox_to_anchor=(1.01, 1.0))
    style.save(fig, "viz_amounts_students_stacked_bars")


# ---------------------------------------------------------------------------
# Proportional ink: truncated vs zero-based y-axis, same close-clustered data.
SCHOOLS = ["School A", "School B", "School C", "School D", "School E"]
PASS_RATES = [58.2, 54.7, 51.9, 50.3, 49.1]


def _truncated_bar_bad():
    fig, ax = style.new_fig(6.4, 4.2)
    x = np.arange(len(SCHOOLS))
    ax.bar(x, PASS_RATES, color=style.BAD, width=0.6, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(SCHOOLS)
    ax.set_ylim(48, 60)
    ax.set_ylabel("Exam pass rate (%)")
    ax.set_title("Pass Rate by School")
    ax.grid(axis="x", visible=False)
    style.save(fig, "viz_proportional_ink_truncated_bar_bad")


def _truncated_bar_fixed():
    fig, ax = style.new_fig(6.4, 4.2)
    x = np.arange(len(SCHOOLS))
    ax.bar(x, PASS_RATES, color=style.ACCENT, width=0.6, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(SCHOOLS)
    ax.set_ylim(0, 65)
    ax.set_ylabel("Exam pass rate (%)")
    ax.set_title("Pass Rate by School")
    ax.grid(axis="x", visible=False)
    style.save(fig, "viz_proportional_ink_truncated_bar_fixed")


# ---------------------------------------------------------------------------
# Log scale: citation counts spanning ~4 orders of magnitude, linear vs log.
PAPERS = ["Paper A", "Paper B", "Paper C", "Paper D", "Paper E"]
CITATIONS = [5, 60, 540, 4900, 46000]


def _log_scale():
    # Dots, not bars: on a log axis a bar has no meaningful base (there is
    # no zero), so length would encode nothing. Position does the work.
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.2))
    x = np.arange(len(PAPERS))
    for ax, scale, label in ((ax1, "linear", "Linear scale — small counts vanish"),
                             (ax2, "log", "Log scale — every magnitude visible")):
        ax.plot(x, CITATIONS, "o", ms=10, color=style.ACCENT, zorder=3)
        ax.set_yscale(scale)
        ax.set_xticks(x)
        ax.set_xticklabels(PAPERS)
        ax.set_xlim(-0.6, len(PAPERS) - 0.4)
        ax.set_title(label, fontsize=12)
        ax.grid(axis="x", visible=False)
        for xi, c in zip(x, CITATIONS):
            ax.annotate(f"{c:,}", xy=(xi, c), xytext=(0, 9), textcoords="offset points",
                        ha="center", color=style.FG, fontsize=9)
    ax1.set_ylim(0, 52000)
    ax1.set_ylabel("Citations")
    ax2.set_ylim(2, 120000)
    ax2.set_ylabel("Citations (log scale)")

    fig.suptitle("Same Data, Linear and Logarithmic", color=style.FG, fontweight="bold")
    style.save(fig, "viz_proportional_ink_log_scale")


FIGURES = {
    "viz_amounts_boxoffice_horizontal": _boxoffice_horizontal,
    "viz_amounts_boxoffice_rotated_bad": _boxoffice_rotated_bad,
    "viz_amounts_boxoffice_wide": _boxoffice_wide,
    "viz_amounts_cleveland_dot_plot": _cleveland_dot_plot,
    "viz_amounts_lifeexp_alpha_order_bad": _lifeexp_alpha_order_bad,
    "viz_amounts_lifeexp_bars_bad": _lifeexp_bars_bad,
    "viz_amounts_lifeexp_dot_plot": _lifeexp_dot_plot,
    "viz_amounts_health_heatmap": _health_heatmap,
    "viz_amounts_students_stacked_bars": _students_stacked_bars,
    "viz_amounts_income_by_value_bad": _income_by_value_bad,
    "viz_amounts_income_by_age_good": _income_by_age_good,
    "viz_proportional_ink_truncated_bar_bad": _truncated_bar_bad,
    "viz_proportional_ink_truncated_bar_fixed": _truncated_bar_fixed,
    "viz_proportional_ink_log_scale": _log_scale,
}
