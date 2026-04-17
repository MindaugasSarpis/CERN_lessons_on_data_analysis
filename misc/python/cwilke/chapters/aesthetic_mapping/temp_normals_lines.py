"""Daily temperature normals, 4 locations — colour encodes location (Wilke fig 2.3).

Standard small line chart; temperature mapped to y, day of year to x,
location to colour.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import OKABE_ITO, apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.ncdc_normals_4locs().sort_values(["location", "day"])

    loc_order = ["Death Valley", "Houston", "San Diego", "Chicago"]
    colors = {"Death Valley": OKABE_ITO[6],
              "Houston":      OKABE_ITO[1],
              "San Diego":    OKABE_ITO[5],
              "Chicago":      OKABE_ITO[3]}

    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    for loc in loc_order:
        sub = df[df["location"] == loc]
        ax.plot(sub["day"], sub["temperature"], color=colors[loc],
                linewidth=1.6, label=loc)

    ax.set_xlabel("month")
    ax.set_ylabel("temperature (°F)")
    ax.set_xlim(1, 366)
    ax.set_ylim(20, 110)
    ax.set_xticks([1, 91, 182, 274, 366])
    ax.set_xticklabels(["Jan", "Apr", "Jul", "Oct", "Jan"])
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    grid(ax)

    fig.tight_layout()
    save(fig, "aesthetic_mapping", "temp_normals_lines")


if __name__ == "__main__":
    render()
