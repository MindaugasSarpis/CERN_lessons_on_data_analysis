"""California: 12-month house price change and unemployment rate over
time, as two stacked line graphs (Wilke fig 13.9)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.ca_house_unemployment()

    fig, axes = plt.subplots(2, 1, figsize=(8.0, 5.4), sharex=True)
    ax1, ax2 = axes
    ax1.plot(df["date"], df["house_price_perc"] * 100,
             color=PRIMARY_BLUE, linewidth=1.6)
    ax1.set_ylim(-32, 32)
    ax1.set_ylabel("12-month change\nin house prices (%)")
    ax1.set_title("(a)", loc="left")
    grid(ax1)

    ax2.plot(df["date"], df["unemploy_perc"],
             color=PRIMARY_BLUE, linewidth=1.6)
    ax2.set_ylim(3.5, 14)
    ax2.set_ylabel("unemployment\nrate (%)")
    ax2.set_xlabel("year")
    ax2.set_title("(b)", loc="left")
    ax2.xaxis.set_major_locator(mdates.YearLocator(4))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    grid(ax2)

    fig.tight_layout()
    save(fig, "time_series", "house_price_unemploy")


if __name__ == "__main__":
    render()
