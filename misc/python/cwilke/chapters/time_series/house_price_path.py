"""Connected scatter plot: house prices vs unemployment over time
(Wilke fig 13.10)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.ca_house_unemployment()
    t = (df["date"] - df["date"].min()).dt.days.values
    t_norm = t / t.max()

    # Plot segment-by-segment, gradually darkening colour.
    fig, ax = plt.subplots(figsize=(6.6, 4.8))
    x = df["unemploy_perc"].values
    y = df["house_price_perc"].values * 100
    # Manual segment colouring using a colormap.
    import matplotlib.collections as mc
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = mc.LineCollection(segments, cmap="Blues",
                            array=t_norm[:-1],
                            linewidths=2.0, capstyle="round")
    ax.add_collection(lc)
    ax.autoscale()

    # annotate selected dates
    labels = {
        pd.Timestamp("2005-01-01"): "Jan 2005",
        pd.Timestamp("2007-07-01"): "Jul 2007",
        pd.Timestamp("2010-01-01"): "Jan 2010",
        pd.Timestamp("2012-07-01"): "Jul 2012",
        pd.Timestamp("2015-01-01"): "Jan 2015",
    }
    for date, label in labels.items():
        if (df["date"] == date).any():
            row = df[df["date"] == date].iloc[0]
            ax.scatter([row["unemploy_perc"]],
                       [row["house_price_perc"] * 100],
                       s=28, color="black", zorder=3)
            ax.annotate(label,
                         (row["unemploy_perc"],
                          row["house_price_perc"] * 100),
                         xytext=(6, 4), textcoords="offset points",
                         fontsize=9)

    ax.set_xlim(3.5, 14.5)
    ax.set_ylim(-32, 32)
    ax.set_xlabel("unemployment rate (%)")
    ax.set_ylabel("12-month change in house prices (%)")
    grid(ax)
    save(fig, "time_series", "house_price_path")


if __name__ == "__main__":
    render()
