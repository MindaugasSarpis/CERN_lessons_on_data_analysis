"""Figures of Lecture 09: Probability & Statistics.

Every figure is computed: simulations use `np.random.default_rng(seed)` with
the seeds the slides show, and the real-data figures read the two course
files, `D0_KPi.csv` (column M) and `pendulum.csv`. No SciPy: the densities
are written out, as the lecture derives them.

  viz_probability_frequency            fraction of sixes against rolls
  viz_probability_two_dice             distribution of the sum of two dice
  viz_probability_binomial_poisson     binomial(n, 3/n) against Poisson(3)
  viz_probability_poisson_gaussian     Poisson(λ) against a Gaussian
  viz_probability_gaussian             the Gaussian density and its areas
  viz_probability_clt                  sums of N uniform numbers
  viz_probability_mass                 the mass column M as a histogram
  viz_probability_group_means          M, and means of 100 values of M
  viz_probability_correlation          four scatter plots with their r
  viz_probability_propagation          a narrow interval through g(T)
  viz_probability_likelihood_binomial  L(p) for 7 of 10
  viz_probability_likelihood_mean      ln L(μ) for five timings
  viz_probability_weighted_mean        g from nine rows, weighted mean
"""
from math import comb, factorial

import matplotlib.pyplot as plt
import numpy as np

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data"
WARM = style.CYCLE[1]     # the second series colour: curves over bars
GREEN = style.CYCLE[2]


def _gauss(x, mu, sigma):
    return np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))


def _poisson(k, lam):
    return np.array([lam ** int(i) * np.exp(-lam) / factorial(int(i)) for i in k])


def _mass():
    return np.loadtxt(DATA / "D0_KPi.csv", delimiter=",", skiprows=1, usecols=0)


def _pendulum():
    length_cm, t10 = np.loadtxt(DATA / "pendulum.csv", delimiter=",", skiprows=1).T
    return length_cm, t10


# --- probability ----------------------------------------------------------

def _frequency():
    """Same stream as the slide: default_rng(1), one million rolls."""
    rng = np.random.default_rng(1)
    rolls = rng.integers(1, 7, 1_000_000)
    n = np.unique(np.logspace(0, 6, 500).astype(int))
    frac = np.cumsum(rolls == 6)[n - 1] / n

    fig, ax = plt.subplots(figsize=(8.4, 3.3))
    ax.axhline(1 / 6, color=WARM, linewidth=1.6)
    ax.plot(n, frac, color=style.ACCENT, linewidth=1.8)
    ax.set_xscale("log")
    ax.set(xlabel="number of rolls n", ylabel="fraction of sixes",
           xlim=(1, 1e6), ylim=(0, 0.42))
    ax.text(7e5, 1 / 6 + 0.02, "1/6 = 0.1667", color=WARM, fontsize=11,
            ha="right")
    style.save(fig, "viz_probability_frequency")


def _two_dice():
    k = np.arange(2, 13)
    ways = 6 - np.abs(k - 7)

    fig, ax = plt.subplots(figsize=(5.4, 3.5))
    ax.bar(k, ways / 36, width=0.8, color=style.ACCENT)
    for ki, w in zip(k, ways):
        ax.text(ki, w / 36 + 0.004, f"{w}/36", ha="center", fontsize=8.5,
                color=style.FG)
    ax.set_xticks(k)
    ax.set(xlabel="sum of two dice", ylabel="probability", ylim=(0, 0.19))
    ax.xaxis.grid(False)
    style.save(fig, "viz_probability_two_dice")


# --- distributions --------------------------------------------------------

def _binomial_poisson():
    k = np.arange(0, 11)
    pois = _poisson(k, 3)

    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.1), sharey=True)
    for ax, n in zip(axes, [10, 100, 1000]):
        p = 3 / n
        binom = [comb(n, int(i)) * p ** int(i) * (1 - p) ** (n - int(i)) for i in k]
        ax.bar(k, binom, width=0.8, color=style.ACCENT, label="binomial")
        ax.plot(k, pois, "o", color=WARM, markersize=5, label="Poisson(3)")
        ax.set_title(f"n = {n},  p = {p:g}", fontsize=12)
        ax.set_xlabel("k")
        ax.set_xticks(k[::2])
        ax.xaxis.grid(False)
    axes[0].set_ylabel("probability")
    axes[0].legend(loc="upper right")
    style.save(fig, "viz_probability_binomial_poisson")


def _poisson_gaussian():
    fig, axes = plt.subplots(1, 4, figsize=(10.6, 2.9))
    for ax, lam in zip(axes, [1, 4, 16, 64]):
        sd = np.sqrt(lam)
        lo, hi = max(0, int(lam - 4 * sd)), int(lam + 4 * sd) + 1
        k = np.arange(lo, hi + 1)
        ax.bar(k, _poisson(k, lam), width=0.8 if lam < 10 else 1.0,
               color=style.ACCENT)
        xs = np.linspace(lo - 0.5, hi + 0.5, 300)
        ax.plot(xs, _gauss(xs, lam, sd), color=WARM, linewidth=1.8)
        ax.set_title(rf"$\lambda$ = {lam}", fontsize=12)
        ax.set_xlabel("k")
        ax.set_yticks([])
        ax.xaxis.grid(False)
    style.save(fig, "viz_probability_poisson_gaussian")


def _gaussian():
    x = np.linspace(-4, 4, 500)
    y = _gauss(x, 0, 1)

    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    for lim, alpha in [(3, 0.18), (2, 0.34), (1, 0.6)]:
        m = np.abs(x) <= lim
        ax.fill_between(x[m], y[m], color=style.ACCENT, alpha=alpha, linewidth=0)
    ax.plot(x, y, color=style.FG, linewidth=1.6)
    ax.text(0, 0.17, "68.3 %", ha="center", fontsize=12, color="#0b0e14",
            fontweight="bold")
    for lim, label, yy in [(2, "95.4 %", 0.47), (3, "99.7 %", 0.53)]:
        ax.annotate("", xy=(-lim, yy), xytext=(lim, yy),
                    arrowprops=dict(arrowstyle="<->", color=style.DIM, lw=1.1))
        ax.text(0, yy + 0.008, label, ha="center", fontsize=11, color=style.FG)
    ax.annotate("", xy=(-1, 0.415), xytext=(1, 0.415),
                arrowprops=dict(arrowstyle="<->", color=style.DIM, lw=1.1))
    ax.set_xticks(range(-3, 4))
    ax.set_xticklabels([r"$\mu - 3\sigma$", r"$\mu - 2\sigma$",
                        r"$\mu - \sigma$", r"$\mu$", r"$\mu + \sigma$",
                        r"$\mu + 2\sigma$", r"$\mu + 3\sigma$"], fontsize=9)
    ax.set_yticks([])
    ax.set(xlim=(-4, 4), ylim=(0, 0.6), ylabel="density f(x)")
    ax.grid(False)
    style.save(fig, "viz_probability_gaussian")


def _clt():
    """Same stream as the slide: default_rng(4), 100 000 sums for each N."""
    rng = np.random.default_rng(4)
    fig, axes = plt.subplots(1, 4, figsize=(10.6, 3.0))
    for ax, n in zip(axes, [1, 2, 3, 12]):
        s = rng.random((100_000, n)).sum(axis=1)
        mu, sd = n / 2, np.sqrt(n / 12)
        lo, hi = (0, n) if n <= 3 else (mu - 4 * sd, mu + 4 * sd)
        ax.hist(s, bins=50, range=(lo, hi), density=True, color=style.ACCENT)
        xs = np.linspace(lo, hi, 300)
        ax.plot(xs, _gauss(xs, mu, sd), color=WARM, linewidth=1.8)
        ax.set_title(f"N = {n}", fontsize=12)
        ax.set_xlabel("sum")
        ax.set_yticks([])
        ax.xaxis.grid(False)
    style.save(fig, "viz_probability_clt")


# --- samples ----------------------------------------------------------------

def _mass_hist():
    m = _mass()
    mean, s = m.mean(), m.std(ddof=1)

    fig, ax = plt.subplots(figsize=(8.4, 3.4))
    ax.hist(m, bins=np.arange(1810, 1922, 2), color=style.ACCENT)
    ax.axvspan(mean - s, mean + s, color=WARM, alpha=0.16, linewidth=0)
    ax.axvline(mean, color=WARM, linewidth=1.8)
    ax.text(mean - 1.5, 4000, f"mean {mean:.1f}", color=WARM, fontsize=11,
            ha="right")
    ax.text(mean + s - 1.5, 4000, f"mean ± s,  s = {s:.1f}", color=WARM,
            fontsize=11, ha="right")
    ax.set(xlabel="M (MeV/c²)", ylabel="rows per 2 MeV/c²", xlim=(1808, 1922),
           ylim=(0, 4300))
    ax.xaxis.grid(False)
    style.save(fig, "viz_probability_mass")


def _group_means():
    m = _mass()
    mean, s = m.mean(), m.std(ddof=1)
    groups = m[:91_500].reshape(915, 100).mean(axis=1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 3.3))
    ax1.hist(m, bins=np.arange(1790, 1942, 2), density=True, color=style.ACCENT)
    xs = np.linspace(1790, 1940, 300)
    ax1.plot(xs, _gauss(xs, mean, s), color=WARM, linewidth=1.8)
    ax1.set_title("91 583 single values", fontsize=12)
    ax1.set(xlabel="M (MeV/c²)", xlim=(1790, 1940))
    ax1.set_xticks([1800, 1840, 1880, 1920])

    se = s / 10
    ax2.hist(groups, bins=np.arange(1855, 1873.5, 0.5), density=True,
             color=style.ACCENT)
    xs = np.linspace(1855, 1873, 300)
    ax2.plot(xs, _gauss(xs, mean, se), color=WARM, linewidth=1.8)
    ax2.set_title("915 means of 100 values", fontsize=12)
    ax2.set(xlabel="mean of 100 values of M (MeV/c²)", xlim=(1855, 1873))
    ax2.set_xticks([1856, 1860, 1864, 1868, 1872])
    fig.get_layout_engine().set(wspace=0.08)
    for ax in (ax1, ax2):
        ax.set_yticks([])
        ax.xaxis.grid(False)
    style.save(fig, "viz_probability_group_means")


def _correlation():
    rng = np.random.default_rng(28)
    n = 150
    x = rng.normal(0, 1, n)
    noise = rng.normal(0, 1, n)
    panels = [
        x, 0.9 * x + np.sqrt(1 - 0.9 ** 2) * noise,
        x, -0.6 * x + np.sqrt(1 - 0.6 ** 2) * noise,
        x, noise,
    ]
    xq = np.linspace(-2, 2, n)
    panels += [xq, xq ** 2 - 1.3 + rng.normal(0, 0.25, n)]

    fig, axes = plt.subplots(1, 4, figsize=(10.6, 2.9))
    for i, ax in enumerate(axes):
        a, b = panels[2 * i], panels[2 * i + 1]
        r = np.round(np.corrcoef(a, b)[0, 1], 2) + 0.0     # no "-0.00"
        ax.scatter(a, b, s=9, color=style.ACCENT, alpha=0.8, linewidth=0)
        ax.set_title(f"r = {r:+.2f}".replace("-", "−"), fontsize=12)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set(xlim=(-3.2, 3.2), ylim=(-3.2, 3.2))
    style.save(fig, "viz_probability_correlation")


# --- error propagation -----------------------------------------------------

def _propagation():
    """g(T) = 4π²ℓ/T² for a length ℓ = 1 m. The interval in T is ±0.1 s, ten times
    the uncertainty of the worked example, so that it can be seen."""
    g = lambda t: 4 * np.pi ** 2 / t ** 2
    t0, st = 2.001, 0.1
    slope = -2 * g(t0) / t0
    t = np.linspace(1.6, 2.5, 300)

    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.axvspan(t0 - st, t0 + st, color=style.ACCENT, alpha=0.22, linewidth=0)
    lo, hi = g(t0) + slope * st, g(t0) - slope * st
    ax.axhspan(lo, hi, color=WARM, alpha=0.22, linewidth=0)
    ax.plot(t, g(t), color=style.FG, linewidth=2, label=r"g(T) = 4π²$\ell$ / T²")
    ax.plot(t, g(t0) + slope * (t - t0), color=WARM, linewidth=1.6,
            linestyle="--", label="tangent at T₀")
    ax.plot([t0], [g(t0)], "o", color=style.FG, markersize=5)
    ax.text(t0, 6.45, r"T₀ ± $\sigma$", color=style.ACCENT, ha="center",
            fontsize=11)
    ax.text(1.62, g(t0) - 0.12, r"g₀ ± |dg/dT| $\sigma$", color=WARM,
            va="top", fontsize=11)
    ax.set(xlabel="period T (s)", ylabel="g (m/s²)", xlim=(1.6, 2.5),
           ylim=(6.2, 15.5))
    ax.legend(loc="upper right")
    style.save(fig, "viz_probability_propagation")


# --- likelihood --------------------------------------------------------------

def _likelihood_binomial():
    p = np.linspace(0, 1, 400)
    like = comb(10, 7) * p ** 7 * (1 - p) ** 3

    fig, ax = plt.subplots(figsize=(5.4, 3.4))
    ax.plot(p, like, color=style.ACCENT, linewidth=2)
    best = comb(10, 7) * 0.7 ** 7 * 0.3 ** 3
    ax.plot([0.7, 0.7], [0, best], color=WARM, linewidth=1.4, linestyle="--")
    ax.plot([0.7], [best], "o", color=WARM, markersize=6)
    ax.text(0.7, best + 0.012, f"p = 0.7,  L = {best:.3f}", color=WARM,
            ha="center", fontsize=11)
    ax.set(xlabel="p", ylabel="L(p) for k = 7 of n = 10", xlim=(0, 1),
           ylim=(0, 0.31))
    style.save(fig, "viz_probability_likelihood_binomial")


def _likelihood_mean():
    """Five timings of 10 swings (example values), each with σ = 0.1 s."""
    t = np.array([20.01, 19.93, 20.12, 19.98, 20.06])
    sigma, n = 0.1, len(t)
    mean, se = t.mean(), sigma / np.sqrt(n)
    mu = np.linspace(19.88, 20.16, 300)
    dlnl = -n * (mu - mean) ** 2 / (2 * sigma ** 2)

    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    ax.plot(mu, dlnl, color=style.ACCENT, linewidth=2)
    ax.axhline(-0.5, color=style.DIM, linewidth=1, linestyle="--")
    ax.plot([mean - se, mean + se], [-0.5, -0.5], "o", color=WARM, markersize=6)
    ax.plot([mean - se, mean + se], [-0.5, -0.5], color=WARM, linewidth=2.2)
    ax.plot([mean], [0], "o", color=style.FG, markersize=5)
    ax.plot(t, np.full(n, -3.75), "|", color=style.FG, markersize=14,
            markeredgewidth=1.6)
    ax.text(19.885, -3.45, "the five timings", color=style.FG, fontsize=10)
    ax.text(mean, 0.17, f"maximum at {mean:.2f}", ha="center", color=style.FG,
            fontsize=11)
    ax.text(mean, -0.95, f"± {se:.3f}", ha="center", color=WARM, fontsize=11)
    ax.text(20.162, -0.42, "−1/2", ha="right", color=style.DIM, fontsize=10)
    ax.set(xlabel=r"$\mu$ (s)", ylabel=r"ln L($\mu$) − ln L(max)",
           xlim=(19.88, 20.165), ylim=(-4, 0.55))
    style.save(fig, "viz_probability_likelihood_mean")


def _weighted_mean():
    """g and its propagated uncertainty for the nine rows of pendulum.csv,
    with 0.1 cm on the length and 0.1 s on the time of 10 swings."""
    length_cm, t10 = _pendulum()
    g = 4 * np.pi ** 2 * (length_cm / 100) / (t10 / 10) ** 2
    sg = g * np.sqrt((0.1 / length_cm) ** 2 + (2 * 0.1 / t10) ** 2)
    w = 1 / sg ** 2
    best, err = (w * g).sum() / w.sum(), 1 / np.sqrt(w.sum())

    fig, ax = plt.subplots(figsize=(5.8, 3.5))
    ax.axhspan(best - err, best + err, color=WARM, alpha=0.25, linewidth=0)
    ax.axhline(best, color=WARM, linewidth=1.6)
    ax.errorbar(length_cm, g, yerr=sg, fmt="o", color=style.ACCENT,
                markersize=5, capsize=3, linewidth=1.4)
    ax.text(60, 10.11, f"weighted mean {best:.2f} ± {err:.2f} m/s²",
            color=WARM, ha="center", fontsize=11)
    ax.set(xlabel="length (cm)", ylabel="g (m/s²)", xlim=(12, 108),
           ylim=(9.4, 10.2))
    ax.set_xticks(length_cm)
    style.save(fig, "viz_probability_weighted_mean")


FIGURES = {
    "viz_probability_frequency": _frequency,
    "viz_probability_two_dice": _two_dice,
    "viz_probability_binomial_poisson": _binomial_poisson,
    "viz_probability_poisson_gaussian": _poisson_gaussian,
    "viz_probability_gaussian": _gaussian,
    "viz_probability_clt": _clt,
    "viz_probability_mass": _mass_hist,
    "viz_probability_group_means": _group_means,
    "viz_probability_correlation": _correlation,
    "viz_probability_propagation": _propagation,
    "viz_probability_likelihood_binomial": _likelihood_binomial,
    "viz_probability_likelihood_mean": _likelihood_mean,
    "viz_probability_weighted_mean": _weighted_mean,
}
