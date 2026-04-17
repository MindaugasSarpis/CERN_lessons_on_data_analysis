"""PCA of forensic-glass composition — points coloured by type
(Wilke fig 12.12)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.forensic_glass()
    cols = ["Mg", "Ca", "Fe", "K", "Na", "Al", "Ba"]
    X = df[cols].values
    X = (X - X.mean(axis=0)) / X.std(axis=0, ddof=0)
    # SVD for PCA
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    scores = U * S
    pc1 = scores[:, 0]
    pc2 = scores[:, 1]

    fig, ax = plt.subplots(figsize=(6.6, 5.0))
    palette = {"window": "#E69F00",
               "container": "#009E73",
               "tableware": "#0072B2",
               "headlamp":  "#D55E00"}
    markers = {"window": "o", "container": "s",
               "tableware": "^", "headlamp": "D"}
    for t in ["headlamp", "tableware", "container", "window"]:
        mask = df["type"].values == t
        ax.scatter(pc1[mask], pc2[mask],
                   marker=markers[t], s=38,
                   facecolors=palette[t] + "AA",
                   edgecolors=palette[t], linewidths=1.0,
                   label=t)
    ax.set_xlabel("PC 1")
    ax.set_ylabel("PC 2")
    ax.legend(title="fragment type", loc="upper right", frameon=False)
    grid(ax)
    save(fig, "associations", "forensic_glass_pca")


if __name__ == "__main__":
    render()
