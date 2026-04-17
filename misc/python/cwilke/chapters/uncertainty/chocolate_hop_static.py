"""Hypothetical outcome plot schematic (Wilke fig 16.19).

Nine panels, each showing one randomly drawn Canadian rating vs one U.S.
rating as vertical ticks on a common x-axis.  An animation would cycle
between panels; here we show all nine stacked.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import cacao_ratings
from cwilke.theme import apply_base, hgrid, save


def render() -> None:
    apply_base()
    rng = np.random.default_rng(49323)
    df = cacao_ratings()
    ca = df[df["location"] == "Canada"]["rating"].values
    us = df[df["location"] == "US"]["rating"].values

    n_panels = 9
    fig, axes = plt.subplots(3, 3, figsize=(8.4, 5.2), sharex=True, sharey=True)

    for ax in axes.flatten():
        for rank, (label, vals) in enumerate([("US", us), ("Canada", ca)]):
            val = float(rng.choice(vals))
            ax.vlines(val, rank - 0.35, rank + 0.35,
                       color="#116a4a", linewidth=2.2)
        ax.set_yticks([0, 1])
        ax.set_yticklabels(["US", "Canada"])
        ax.set_xlim(1.95, 4.1)
        hgrid(ax)

    for ax in axes[2]:
        ax.set_xlabel("chocolate flavor rating")
    fig.tight_layout()
    save(fig, "uncertainty", "chocolate_hop_static")


if __name__ == "__main__":
    render()
