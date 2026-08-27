"""Fitting figures for Lecture 12.

  * viz_fitting_covariance — the covariance matrix of the deck's own
    Gaussian + flat-background fit, pictured: left, the 4x4 correlation
    matrix of (A, mu, sigma, b); right, the delta-chi2 = 1 and 2.3 ellipses
    in the (A, sigma) plane. Uses EXACTLY the data of the "Interactive:
    Gaussian Fit" monaco block (np.random.seed(7), 40 bins on [0, 10]) so
    the picture is the fit the students just ran.
"""
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import style

PARAMS = ["A", r"$\mu$", r"$\sigma$", "b"]


def _gauss_bg(x, A, mu, sig, bg):
    return A * np.exp(-(x - mu) ** 2 / (2 * sig ** 2)) + bg


def _deck_fit():
    """Same data + call as the slide's Gaussian runner (absolute_sigma=True)."""
    np.random.seed(7)
    data = np.concatenate([np.random.normal(5, 0.8, 500),
                           np.random.uniform(0, 10, 200)])
    counts, edges = np.histogram(data, bins=40, range=(0, 10))
    x = 0.5 * (edges[:-1] + edges[1:])
    y = counts.astype(float)
    yerr = np.sqrt(np.maximum(counts, 1))
    popt, pcov = curve_fit(_gauss_bg, x, y, p0=[40, 5, 1, 5], sigma=yerr,
                           absolute_sigma=True)
    return popt, pcov


def _ellipse(center, cov2, dchi2, n=400):
    """Points of the contour chi2(theta) = chi2_min + dchi2 for a 2x2 cov."""
    L = np.linalg.cholesky(cov2)
    t = np.linspace(0, 2 * np.pi, n)
    circle = np.vstack([np.cos(t), np.sin(t)])
    return center[:, None] + np.sqrt(dchi2) * (L @ circle)


def _covariance():
    popt, pcov = _deck_fit()
    err = np.sqrt(np.diag(pcov))
    corr = pcov / np.outer(err, err)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.4),
                                   gridspec_kw={"width_ratios": [1, 1.25]})

    # --- left: correlation matrix ------------------------------------------
    cmap = mcolors.LinearSegmentedColormap.from_list(
        "diverging", [style.CYCLE[1], "#333b4a", style.ACCENT])
    norm = mcolors.Normalize(vmin=-1, vmax=1)
    im = ax1.imshow(corr, cmap=cmap, norm=norm)
    ax1.set_xticks(range(4))
    ax1.set_xticklabels(PARAMS, fontsize=12)
    ax1.set_yticks(range(4))
    ax1.set_yticklabels(PARAMS, fontsize=12)
    ax1.grid(False)
    for spine in ax1.spines.values():
        spine.set_visible(False)
    for i in range(4):
        for j in range(4):
            v = np.round(corr[i, j], 2) + 0.0   # kill "-0.00"
            r, g, b, _ = cmap(norm(v))
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            ax1.text(j, i, f"{v:+.2f}", ha="center", va="center",
                     fontsize=11, color="#0b0f14" if lum > 0.55 else style.FG)
    cbar = fig.colorbar(im, ax=ax1, shrink=0.8, pad=0.04)
    cbar.outline.set_visible(False)
    cbar.ax.tick_params(colors=style.DIM, labelsize=9)
    cbar.set_label(r"$\rho_{ij} = C_{ij} / (\sigma_i \sigma_j)$", color=style.DIM, fontsize=9)
    ax1.set_title(r"Correlation matrix  $\rho(\theta_i, \theta_j)$")

    # --- right: delta-chi2 ellipses in the (A, sigma) plane -----------------
    iA, iS = 0, 2
    center = popt[[iA, iS]]
    cov2 = pcov[np.ix_([iA, iS], [iA, iS])]
    e1 = _ellipse(center, cov2, 1.0)
    e2 = _ellipse(center, cov2, 2.30)
    ax2.fill(e2[0], e2[1], color=style.CYCLE[1], alpha=0.18, lw=0)
    ax2.plot(e2[0], e2[1], color=style.CYCLE[1], lw=2.0,
             label=r"$\Delta\chi^2 = 2.3$  (68 % joint region)")
    ax2.fill(e1[0], e1[1], color=style.ACCENT, alpha=0.28, lw=0)
    ax2.plot(e1[0], e1[1], color=style.ACCENT, lw=2.2,
             label=r"$\Delta\chi^2 = 1$  (projects to $\pm1\sigma$ per parameter)")
    # single-parameter +-1 sigma band: the projection of the delta-chi2=1 ellipse
    for v in (center[0] - err[iA], center[0] + err[iA]):
        ax2.axvline(v, color=style.ACCENT, lw=1.0, ls="--", alpha=0.8)
    for v in (center[1] - err[iS], center[1] + err[iS]):
        ax2.axhline(v, color=style.ACCENT, lw=1.0, ls="--", alpha=0.8)
    ax2.plot(*center, "o", color=style.FG, ms=6, zorder=5, label=r"best fit  $\hat\theta$")
    ax2.annotate(rf"$\rho(A, \sigma)$ = {corr[iA, iS]:+.2f}", xy=(0.03, 0.05),
                 xycoords="axes fraction", fontsize=11, color=style.FG)
    ax2.annotate("wider peak = lower amplitude\n(same yield)", xy=(0.97, 0.95),
                 xycoords="axes fraction", fontsize=9.5, color=style.DIM,
                 ha="right", va="top")
    pad = 1.25
    ax2.set_xlim(center[0] - pad * np.sqrt(2.3) * err[iA] * 1.35,
                 center[0] + pad * np.sqrt(2.3) * err[iA] * 1.35)
    ax2.set_ylim(center[1] - pad * np.sqrt(2.3) * err[iS] * 1.35,
                 center[1] + pad * np.sqrt(2.3) * err[iS] * 1.35)
    ax2.set_xlabel(rf"A  (amplitude)   best fit {popt[iA]:.1f} $\pm$ {err[iA]:.1f}")
    ax2.set_ylabel(rf"$\sigma$  (width)   best fit {popt[iS]:.2f} $\pm$ {err[iS]:.2f}")
    ax2.set_title(r"Confidence ellipses in the (A, $\sigma$) plane")
    ax2.legend(loc="lower right", fontsize=9)

    style.save(fig, "viz_fitting_covariance")


FIGURES = {
    "viz_fitting_covariance": _covariance,
}
