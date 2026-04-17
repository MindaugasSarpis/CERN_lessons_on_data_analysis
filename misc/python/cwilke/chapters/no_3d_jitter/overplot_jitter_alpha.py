"""Three ways to tame overplotting: raw, jitter+alpha, hexbin (Wilke ch. 18)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, open_axes, save


def render() -> None:
    apply_base()

    df = D.diamonds(n=1500)
    x = df["carat"].values
    y = df["price"].values

    fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.8))

    # (a) raw overplotting
    ax = axes[0]
    ax.scatter(x, y, s=14, color=PRIMARY_BLUE, edgecolors="none")
    ax.set_title("raw")
    open_axes(ax)

    # (b) jitter + alpha
    rng = np.random.default_rng(0)
    jx = x + rng.normal(0, 0.02, size=x.size)
    jy = y + rng.normal(0, 40, size=y.size)
    ax = axes[1]
    ax.scatter(jx, jy, s=14, color=PRIMARY_BLUE, alpha=0.2,
               edgecolors="none")
    ax.set_title("jitter + alpha")
    open_axes(ax)

    # (c) 2D density / hexbin
    ax = axes[2]
    hb = ax.hexbin(x, y, gridsize=30, cmap="Blues", mincnt=1)
    ax.set_title("2D density")
    open_axes(ax)
    cb = fig.colorbar(hb, ax=ax, shrink=0.85, pad=0.02)
    cb.set_label("count")

    for ax in axes:
        ax.set_xlabel("carat")
    axes[0].set_ylabel("price (USD)")

    fig.tight_layout()
    save(fig, "no_3d_jitter", "overplot_jitter_alpha")


if __name__ == "__main__":
    render()
