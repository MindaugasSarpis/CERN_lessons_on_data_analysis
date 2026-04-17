"""Density estimates at four bandwidth / kernel choices (Wilke fig 7.4).

The density-plot analogue of the classic histogram-binwidth grid.
Too narrow a bandwidth -> peaky, visually busy; too wide -> smooths
real structure away; rectangular kernels look blocky.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def _rect_kde(samples: np.ndarray, xs: np.ndarray, bw: float) -> np.ndarray:
    """Uniform (rectangular) kernel density estimate."""
    out = np.zeros_like(xs, dtype=float)
    half = bw / 2
    for s in samples:
        mask = (xs >= s - half) & (xs <= s + half)
        out[mask] += 1.0
    return out / (samples.size * bw)


def render() -> None:
    apply_base()
    age = D.titanic()["age"].dropna().values
    xs = np.linspace(0, 75, 400)

    # (label, bandwidth, kernel)
    specs = [
        ("Gaussian, bw = 0.5", 0.5, "gauss"),
        ("Gaussian, bw = 2",   2.0, "gauss"),
        ("Gaussian, bw = 5",   5.0, "gauss"),
        ("Rectangular, bw = 2", 2.0, "rect"),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(9.0, 6.0),
                              sharex=True, sharey=True)
    for ax, (label, bw, kernel) in zip(axes.ravel(), specs):
        if kernel == "gauss":
            kde = gaussian_kde(age, bw_method=bw / age.std(ddof=1))
            y = kde(xs)
        else:
            y = _rect_kde(age, xs, bw)
        ax.fill_between(xs, y, color=PRIMARY_BLUE, alpha=0.55)
        ax.plot(xs, y, color="#2c3e50", linewidth=1.1)
        ax.set_title(label)
        ax.set_xlim(0, 75)
        ax.set_xlabel("age (years)")
        ax.set_ylabel("density")
        hgrid(ax)

    fig.tight_layout()
    save(fig, "distributions_i", "titanic_density_bandwidth")


if __name__ == "__main__":
    render()
