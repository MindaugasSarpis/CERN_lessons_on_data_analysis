"""Two-panel compound figure: totals over time + before/after dumbbell
(Wilke fig 21.5).

Panel (a) shows total degrees awarded per year; panel (b) shows the top
five fields' proportion changes from 1970-71 to 2014-15 as a dumbbell
plot.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, open_axes, save


def render() -> None:
    apply_base()
    df = D.ba_degrees()

    totals = df.groupby("year")["count"].sum().reset_index()

    mean_pct = df.groupby("field")["perc"].mean()
    top5 = mean_pct.sort_values(ascending=False).head(5).index.tolist()
    pairs = (df[df["field"].isin(top5)
                & df["year"].isin([1971, 2015])]
             .pivot(index="field", columns="year", values="perc")
             .reindex(top5))

    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(11.0, 4.6),
                                     gridspec_kw={"width_ratios": [1.1, 1.0]})

    # Panel (a)
    ax_a.fill_between(totals["year"], 0, totals["count"] / 1e6,
                      color=PRIMARY_BLUE, alpha=0.25, linewidth=0)
    ax_a.plot(totals["year"], totals["count"] / 1e6,
              color=PRIMARY_BLUE, linewidth=2.0)
    ax_a.set_ylabel("degrees awarded (millions)")
    ax_a.set_ylim(0, 2.05)
    ax_a.set_xlim(1970, 2016)
    hgrid(ax_a)
    ax_a.set_title("a", loc="left", fontweight="bold", color="#455a64")

    # Panel (b) — dumbbell
    y_pos = np.arange(len(top5))[::-1]
    for y, field in zip(y_pos, top5):
        p0, p1 = pairs.loc[field, 1971], pairs.loc[field, 2015]
        ax_b.plot([1971, 2015], [p0 * 100, p1 * 100], color="#b0bec5",
                  linewidth=2.5, zorder=1)
        ax_b.scatter([1971, 2015], [p0 * 100, p1 * 100],
                     s=90, color=PRIMARY_BLUE, edgecolor="white",
                     linewidth=1.5, zorder=3)
    # annotate field names on the right
    for field in top5:
        p1 = pairs.loc[field, 2015] * 100
        ax_b.text(2016, p1, field if len(field) < 28 else
                  field.split(",")[0] + "...",
                  va="center", fontsize=9, color="#2c3e50")
    ax_b.set_xticks([1971, 2015])
    ax_b.set_xticklabels(["1970-71", "2014-15"])
    ax_b.set_xlim(1966, 2035)
    ax_b.set_ylim(0, 24)
    ax_b.set_ylabel("proportion of degrees (%)")
    open_axes(ax_b)
    hgrid(ax_b)
    ax_b.set_title("b", loc="left", fontweight="bold", color="#455a64")

    fig.tight_layout()
    save(fig, "multi_panel", "ba_degrees_compound")


if __name__ == "__main__":
    render()
