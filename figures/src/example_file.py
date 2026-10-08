"""Example-file family: figures drawn from the real LHCb masterclass sample,
lectures/workbook/docs/data/D0_KPi.csv (CERN Open Data Portal, record 401).
No seed and no simulation: the histogram is the file's column M as it is.
The fit figure needs scipy.
"""
import numpy as np

import style

CSV = style.ROOT / "lectures" / "workbook" / "docs" / "data" / "D0_KPi.csv"


def _load():
    return np.genfromtxt(CSV, delimiter=",", names=True)


def _mass():
    m = _load()["M"]
    edges = np.arange(1790, 1942, 2)

    fig, ax = style.new_fig(6.4, 3.7)
    ax.hist(m, bins=edges, histtype="stepfilled", color=style.ACCENT,
            alpha=0.35, edgecolor=style.ACCENT, linewidth=1.2)
    ax.axvline(1864.84, color=style.CYCLE[1], linewidth=1.2, linestyle="--")
    ax.annotate("D⁰ mass\n1864.84 MeV/c²", xy=(1864.84, 3300),
                xytext=(1888, 3000), color=style.CYCLE[1], fontsize=10,
                arrowprops={"arrowstyle": "-", "color": style.CYCLE[1]})
    ax.set(xlabel="column M (MeV/c²)", ylabel="rows per 2 MeV/c²",
           xlim=(1790, 1940))
    ax.xaxis.grid(False)
    style.save(fig, "viz_example_d0_mass")


def _gauss_line(x, n, mu, sigma, a, b):
    """Counts per 2 MeV bin: a Gaussian of n rows on a straight line."""
    g = np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))
    return n * 2.0 * g + a + b * (x - 1865)


def fit_mass():
    """Fit the peak of column M. Returns (parameters, errors, chi2, ndf)."""
    from scipy.optimize import curve_fit

    m = _load()["M"]
    edges = np.arange(1816, 1914.001, 2.0)
    h, _ = np.histogram(m, bins=edges)
    x = 0.5 * (edges[1:] + edges[:-1])
    p, cov = curve_fit(_gauss_line, x, h, p0=[30000, 1865, 8, 1400, 0],
                       sigma=np.sqrt(h), absolute_sigma=True)
    chi2 = (((h - _gauss_line(x, *p)) / np.sqrt(h)) ** 2).sum()
    return p, np.sqrt(np.diag(cov)), chi2, len(x) - len(p), x, h


def _fit():
    p, e, chi2, ndf, x, h = fit_mass()
    xs = np.linspace(1816, 1914, 400)

    fig, ax = style.new_fig(6.4, 3.7)
    ax.errorbar(x, h, yerr=np.sqrt(h), fmt="o", markersize=2.5,
                color=style.FG, elinewidth=0.8, label="rows per 2 MeV/c²")
    ax.plot(xs, _gauss_line(xs, *p), color=style.ACCENT, label="fit")
    ax.plot(xs, p[3] + p[4] * (xs - 1865), color=style.CYCLE[1],
            linestyle="--", linewidth=1.2, label="background")
    ax.set(xlabel="column M (MeV/c²)", ylabel="rows per 2 MeV/c²",
           xlim=(1816, 1914), ylim=(0, None))
    ax.xaxis.grid(False)
    ax.legend(loc="upper right")
    style.save(fig, "viz_example_d0_fit")
    print(f"    mass {p[1]:.2f} +- {e[1]:.2f}, width {p[2]:.2f} +- {e[2]:.2f},"
          f" signal {p[0]:.0f} +- {e[0]:.0f}, chi2/ndf {chi2:.1f}/{ndf}")


FIGURES = {"viz_example_d0_mass": _mass, "viz_example_d0_fit": _fit}
