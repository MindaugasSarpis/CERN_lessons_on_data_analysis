"""Areas of Northeastern U.S. states on linear vs. sqrt y-scale (Wilke fig 3.8).

Linear scale emphasises that New York is ~6x the next state; sqrt
scale instead reflects linear extent (driving time).
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.northeast_state_areas()

    fig, (ax_lin, ax_sqrt) = plt.subplots(1, 2, figsize=(10.5, 4.2))

    # Linear
    ax_lin.bar(df["state_abr"], df["area"], color=PRIMARY_BLUE, width=0.75)
    ax_lin.set_ylabel("area (square miles)")
    ax_lin.set_xlabel("state")
    ax_lin.set_yticks([0, 10000, 20000, 30000, 40000, 50000])
    ax_lin.set_ylim(0, 55000)
    hgrid(ax_lin)
    ax_lin.set_title("a · linear scale", loc="left",
                     fontsize=11, color="#455a64", fontweight="bold")

    # Sqrt
    breaks = [0, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
    positions = np.sqrt(breaks)
    ax_sqrt.bar(df["state_abr"], np.sqrt(df["area"]),
                color=PRIMARY_BLUE, width=0.75)
    ax_sqrt.set_ylabel("area (square miles)")
    ax_sqrt.set_xlabel("state")
    ax_sqrt.set_yticks(positions)
    ax_sqrt.set_yticklabels([str(b) for b in breaks])
    ax_sqrt.set_ylim(0, np.sqrt(55000))
    hgrid(ax_sqrt)
    ax_sqrt.set_title("b · square-root scale", loc="left",
                      fontsize=11, color="#455a64", fontweight="bold")

    fig.tight_layout()
    save(fig, "coordinates_axes", "northeast_areas_linear_sqrt")


if __name__ == "__main__":
    render()
