"""q-bio slows exactly as bioRxiv takes off — the resolution (Wilke fig 29.2)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


COLOURS = {"bioRxiv": "#0072B2", "arXiv q-bio": "#D55E00"}


def render() -> None:
    apply_base()

    df = D.preprints_three()
    df = df[df["archive"].isin(COLOURS.keys())]
    df = df[df["count"] > 0]

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    end_x = df["date"].max()
    for arch, col in COLOURS.items():
        sub = df[df["archive"] == arch].sort_values("date")
        ax.plot(sub["date"], sub["count"], color=col, linewidth=1.8)
        last = sub.iloc[-1]
        ax.text(end_x, last["count"], f"  {arch}",
                color=col, va="center", fontsize=11, fontweight="bold")

    ax.set_yscale("log")
    ax.set_ylim(29, 1600)
    ax.set_yticks([30, 100, 300, 1000])
    ax.set_yticklabels(["30", "100", "300", "1000"])
    ax.set_ylabel("preprints / month")
    ax.set_xlabel("year")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    grid(ax)

    fig.subplots_adjust(left=0.09, right=0.86, top=0.95, bottom=0.13)
    save(fig, "telling_a_story", "q_bio_biorxiv_monthly_growth")


if __name__ == "__main__":
    render()
