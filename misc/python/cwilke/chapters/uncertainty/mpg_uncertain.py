"""Nonlinear fit + confidence band vs alternative fit draws (Wilke fig 16.18).

We substitute a cubic polynomial for Wilke's cubic regression spline; the
message (uncertainty = wigglier curves) is the same.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import mtcars
from cwilke.theme import apply_base, grid, save


def _fit_and_draws():
    df = mtcars()
    x = df["disp"].values
    y = df["mpg"].values
    # design matrix for cubic fit
    X = np.column_stack([np.ones_like(x), x, x ** 2, x ** 3])
    # Normalise for numerical stability
    scale = np.array([1, x.std(), (x.std()) ** 2, (x.std()) ** 3])
    X_scaled = X / scale
    beta, *_ = np.linalg.lstsq(X_scaled, y, rcond=None)
    beta = beta / scale
    y_hat = X @ beta
    resid = y - y_hat
    sigma2 = (resid ** 2).sum() / (len(x) - X.shape[1])
    cov = sigma2 * np.linalg.inv(X.T @ X)

    x_grid = np.linspace(x.min(), x.max(), 200)
    Xg = np.column_stack([np.ones_like(x_grid), x_grid,
                           x_grid ** 2, x_grid ** 3])
    y_grid = Xg @ beta
    se = np.sqrt(np.sum(Xg @ cov * Xg, axis=1))

    rng = np.random.default_rng(8692282)
    draws = rng.multivariate_normal(beta, cov, size=10)
    return df, x_grid, y_grid, se, draws, Xg


def render() -> None:
    apply_base()
    df, x_grid, y_grid, se, draws, Xg = _fit_and_draws()
    from scipy.stats import t
    crit = t.ppf(0.975, len(df) - 4)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.0), sharey=True)
    for ax, panel_letter, label in [(ax1, "a", "best fit + CI band"),
                                     (ax2, "b", "alternative fit draws")]:
        ax.fill_between(x_grid, y_grid - crit * se, y_grid + crit * se,
                         color="#cccccc", alpha=0.5, linewidth=0)
        ax.scatter(df["disp"], df["mpg"], color="#777777", s=22)
        ax.set_xlabel("displacement (cu. in.)")
        ax.text(0.02, 0.94, panel_letter, transform=ax.transAxes,
                fontsize=13, fontweight="bold", va="top")
        grid(ax)

    ax1.plot(x_grid, y_grid, color="#0072B2", linewidth=2.0)
    for d in draws:
        ax2.plot(x_grid, Xg @ d, color="#0072B2", linewidth=0.6, alpha=0.85)

    ax1.set_ylabel("fuel efficiency (mpg)")
    ax1.set_ylim(8, 35)
    fig.tight_layout()
    save(fig, "uncertainty", "mpg_uncertain")


if __name__ == "__main__":
    render()
