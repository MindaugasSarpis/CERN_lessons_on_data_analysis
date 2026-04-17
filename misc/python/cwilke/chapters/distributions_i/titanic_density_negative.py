"""KDE leaking into negative ages — Wilke's "wrong" example (fig 7.5).

Kernel density estimates smear probability mass outside the support of
the data. For bounded quantities (age, counts, concentrations) the
estimator will happily predict impossible values — guard against it by
clipping the support or using a bounded kernel.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save, stamp_wrong


def render() -> None:
    apply_base()
    age = D.titanic()["age"].dropna().values

    # Extend the grid into negatives — where the KDE has no business going.
    xs = np.linspace(-10, 80, 400)
    kde = gaussian_kde(age)
    y = kde(xs)

    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    ax.fill_between(xs, y, color=PRIMARY_BLUE, alpha=0.6)
    ax.plot(xs, y, color="#2c3e50", linewidth=1.3)
    ax.axvline(0, color="#b0242c", linewidth=1.1, linestyle=":")
    ax.annotate("impossible ages (< 0)",
                xy=(-5, 0.008), xytext=(-5, 0.025),
                fontsize=11, color="#b0242c",
                arrowprops=dict(arrowstyle="->", color="#b0242c"))
    ax.set_xlim(-10, 80)
    ax.set_ylim(0, 0.05)
    ax.set_xlabel("age (years)")
    ax.set_ylabel("density")
    hgrid(ax)
    stamp_wrong(fig)
    fig.tight_layout()
    save(fig, "distributions_i", "titanic_density_negative")


if __name__ == "__main__":
    render()
