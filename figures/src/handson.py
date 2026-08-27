"""Hands-on family: the rendered output of the three matplotlib snippets in
lecture 10's "Hands-on" section (minimal bar chart, scatter + fit, histogram
+ density), so each code slide shows its result beside the code. The plotting
calls mirror the slide snippets line for line (same data, seeds, colours);
only the canvas is the course dark style, and the KDE is a 12-line NumPy
stand-in for scipy.stats.gaussian_kde (Scott's rule) so the build needs no
SciPy.
"""
import matplotlib.pyplot as plt
import numpy as np

import style


def _bar_minimal():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    sales = [22, 25, 31, 28, 36]

    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.bar(days, sales, color="#56B4E9", width=0.7)
    ax.set(xlabel="weekday", ylabel="sales (M USD)", ylim=(0, 40))

    ax.yaxis.grid(True, color="#b0bec5", linewidth=0.6)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    style.save(fig, "viz_handson_bar_minimal")


def _scatter_fit():
    rng = np.random.default_rng(0)
    x = rng.uniform(0, 10, 60)
    y = 0.8 * x + rng.normal(0, 1.2, 60)

    slope, intercept = np.polyfit(x, y, 1)
    xs = np.linspace(0, 10, 100)
    ys = slope * xs + intercept

    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    ax.scatter(x, y, s=30, color="#56B4E9", alpha=0.85, edgecolor="white", linewidth=0.5)
    ax.plot(xs, ys, color="#D55E00", linewidth=2, label=f"y = {slope:.2f} x + {intercept:.2f}")
    ax.set(xlabel="x", ylabel="y")
    ax.legend(frameon=False)
    style.save(fig, "viz_handson_scatter_fit")


def _gaussian_kde(data: np.ndarray, xs: np.ndarray) -> np.ndarray:
    """scipy.stats.gaussian_kde with Scott's rule, in plain NumPy."""
    n = data.size
    bw = n ** (-1 / 5) * data.std(ddof=1)
    z = (xs[:, None] - data[None, :]) / bw
    return np.exp(-0.5 * z * z).sum(axis=1) / (n * bw * np.sqrt(2 * np.pi))


def _hist_kde():
    rng = np.random.default_rng(1)
    data = rng.normal(loc=5, scale=1.5, size=500)

    xs = np.linspace(data.min(), data.max(), 300)

    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    ax.hist(data, bins=25, density=True, color="#56B4E9", alpha=0.75, edgecolor="white")
    ax.plot(xs, _gaussian_kde(data, xs), color="#D55E00", linewidth=2, label="kde")
    ax.set(xlabel="value", ylabel="density")
    ax.legend(frameon=False)
    style.save(fig, "viz_handson_hist_kde")


FIGURES = {
    "viz_handson_bar_minimal": _bar_minimal,
    "viz_handson_scatter_fit": _scatter_fit,
    "viz_handson_hist_kde": _hist_kde,
}
