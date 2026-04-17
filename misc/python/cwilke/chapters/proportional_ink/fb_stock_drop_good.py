"""FB price with a $0 baseline puts the dip in proper context (Wilke 17.4)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke.data import fb_stock
from cwilke.theme import apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = fb_stock()

    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    ax.fill_between(df["date"], 0, df["price"],
                    color="#555555", alpha=0.7, linewidth=0)
    ax.plot(df["date"], df["price"], color="#222222", linewidth=1.0)
    ax.set_ylim(0, 150)
    ax.set_xlim(df["date"].min(), df["date"].max())
    ax.set_ylabel("stock price (USD)")
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b 1, %Y"))
    hgrid(ax)
    save(fig, "proportional_ink", "fb_stock_drop_good")


if __name__ == "__main__":
    render()
