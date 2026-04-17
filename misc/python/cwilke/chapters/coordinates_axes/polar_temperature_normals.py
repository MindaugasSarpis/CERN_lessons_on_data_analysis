"""Temperature normals for four US locations in polar coordinates (Wilke fig 3.10).

Polar axis emphasises the cyclical nature of the year — Dec 31 and Jan 1
sit next to each other instead of on opposite edges.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, save


def render() -> None:
    apply_base()
    df = D.ncdc_normals_4locs()

    loc_order = ["Death Valley", "Houston", "San Diego", "Chicago"]
    colors = {"Death Valley": OKABE_ITO[6],   # vermillion
              "Houston":      OKABE_ITO[1],   # orange
              "San Diego":    OKABE_ITO[5],   # blue
              "Chicago":      OKABE_ITO[3]}   # green

    fig = plt.figure(figsize=(6.0, 6.0))
    ax = fig.add_subplot(111, projection="polar")

    for loc in loc_order:
        sub = df[df["location"] == loc].sort_values("day")
        theta = 2 * np.pi * (sub["day"].values - 1) / 366
        r = sub["temperature"].values
        ax.plot(theta, r, color=colors[loc], linewidth=1.6, label=loc)

    ax.set_theta_zero_location("S")   # Jan 1 at the bottom (6 o'clock)
    ax.set_theta_direction(-1)         # counter-clockwise
    ax.set_rlim(0, 105)
    ax.set_rticks([30, 60, 90])
    ax.set_rlabel_position(90)

    # Label months approximately
    month_ticks = np.array([1, 32, 60, 91, 121, 152,
                            182, 213, 244, 274, 305, 335])
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    ax.set_xticks(2 * np.pi * (month_ticks - 1) / 366)
    ax.set_xticklabels(month_names, fontsize=9)

    ax.legend(loc="center", bbox_to_anchor=(1.20, 0.5),
              frameon=False, fontsize=10)

    fig.tight_layout()
    save(fig, "coordinates_axes", "polar_temperature_normals")


if __name__ == "__main__":
    render()
