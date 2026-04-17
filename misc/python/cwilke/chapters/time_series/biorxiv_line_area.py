"""bioRxiv submissions as a filled-area line graph (Wilke fig 13.4)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.biorxiv_growth()

    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    ax.fill_between(df["date"], df["count"], 0,
                    color=PRIMARY_BLUE, alpha=0.25)
    ax.plot(df["date"], df["count"], color=PRIMARY_BLUE, linewidth=1.5)
    ax.set_ylim(0, 1600)
    ax.set_ylabel("preprints / month")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_xlabel("year")
    open_axes(ax)
    save(fig, "time_series", "biorxiv_line_area")


if __name__ == "__main__":
    render()
