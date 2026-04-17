"""Dow Jones Industrial Average, 2009 (Wilke fig 14.1)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.dow_jones_2009()

    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    ax.plot(df["date"], df["close"], color="#333333", linewidth=0.9)
    ax.set_ylabel("Dow Jones Industrial Average")
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    grid(ax)
    fig.autofmt_xdate()
    save(fig, "trends", "dow_jones")


if __name__ == "__main__":
    render()
