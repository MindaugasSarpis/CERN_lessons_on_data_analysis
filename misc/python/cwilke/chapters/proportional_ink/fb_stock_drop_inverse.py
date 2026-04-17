"""Honest area chart: price drop relative to the Oct 22 peak (Wilke 17.6)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke.data import fb_stock
from cwilke.theme import apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = fb_stock().copy()
    peak = df["price"].max()
    df["loss"] = df["price"] - peak

    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    ax.fill_between(df["date"], 0, df["loss"],
                    color="#555555", alpha=0.7, linewidth=0)
    ax.plot(df["date"], df["loss"], color="#222222", linewidth=1.0)
    ax.axhline(0, color="#2c3e50", linewidth=0.8)
    ax.set_ylim(-25, 5)
    ax.set_xlim(df["date"].min(), df["date"].max())
    ax.set_ylabel("price loss (USD)")
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b 1, %Y"))
    hgrid(ax)
    save(fig, "proportional_ink", "fb_stock_drop_inverse")


if __name__ == "__main__":
    render()
