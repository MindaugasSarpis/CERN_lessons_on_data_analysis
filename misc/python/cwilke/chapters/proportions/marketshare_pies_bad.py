"""Market-share pies across three years — Wilke's "bad" example (fig 10.4).

Pies fail as soon as several slices are nearly equal and we want to
compare across panels. Trends (A growing, E shrinking) become invisible.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, save, stamp_bad


def render() -> None:
    apply_base()
    df = D.marketshare()

    companies = ["A", "B", "C", "D", "E"]
    colors = [OKABE_ITO[i] for i in [1, 2, 3, 4, 5]]

    years = sorted(df["year"].unique())
    fig, axes = plt.subplots(1, len(years), figsize=(9.6, 3.6))

    for ax, year in zip(axes, years):
        sub = df[df["year"] == year].set_index("company").loc[companies]
        ax.pie(sub["percent"], labels=companies, colors=colors,
               startangle=90, counterclock=False,
               wedgeprops=dict(edgecolor="white", linewidth=1.2),
               textprops=dict(fontsize=11))
        ax.set_title(str(year))
        ax.set_aspect("equal")
    stamp_bad(fig)
    fig.tight_layout()
    save(fig, "proportions", "marketshare_pies_bad")


if __name__ == "__main__":
    render()
