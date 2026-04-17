"""arXiv q-bio monthly submissions alone — the challenge (Wilke fig 29.1)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()

    df = D.preprints_three()
    qbio = df[df["archive"] == "arXiv q-bio"].sort_values("date")

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(qbio["date"], qbio["count"], color="#D55E00", linewidth=1.8)
    # direct label at the right
    last = qbio.iloc[-1]
    ax.text(last["date"], last["count"], f"  arXiv q-bio",
            color="#D55E00", va="center", fontsize=11, fontweight="bold")

    ax.set_yscale("log")
    ax.set_ylim(40, 400)
    ax.set_yticks([50, 100, 200, 300])
    ax.set_yticklabels(["50", "100", "200", "300"])
    ax.set_ylabel("preprints / month")
    ax.set_xlabel("year")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    grid(ax)

    fig.subplots_adjust(left=0.09, right=0.86, top=0.95, bottom=0.13)
    save(fig, "telling_a_story", "q_bio_monthly_growth")


if __name__ == "__main__":
    render()
