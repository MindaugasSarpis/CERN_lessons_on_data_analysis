"""House Price Index, 4 states, with long-term trend lines
(Wilke fig 14.11)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.hpi_states()
    states = ["California", "Nevada", "Texas", "West Virginia"]

    fig, axes = plt.subplots(2, 2, figsize=(10.0, 6.0),
                              sharex=True, sharey=True)
    for ax, state in zip(axes.ravel(), states):
        sub = df[df["state"] == state]
        ax.plot(sub["date"], sub["hpi_trend"],
                color="#888888", linewidth=1.0)
        ax.plot(sub["date"], sub["hpi"],
                color=PRIMARY_BLUE, linewidth=1.4)
        ax.set_yscale("log")
        ax.set_title(state)
        ax.xaxis.set_major_locator(mdates.YearLocator(10))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        hgrid(ax)
    axes[0, 0].set_ylabel("House Price Index\n(Dec. 2000 = 100)")
    axes[1, 0].set_ylabel("House Price Index\n(Dec. 2000 = 100)")
    fig.tight_layout()
    save(fig, "trends", "hpi_trends")


if __name__ == "__main__":
    render()
