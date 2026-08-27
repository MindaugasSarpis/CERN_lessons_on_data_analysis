"""Machine-learning figures for Lecture 16.

Three deterministic, synthetic teaching figures:
  * viz_ml_polynomial_dial — degree 1/3/10 fits to the same noisy points,
    plus a train-vs-test error panel (overfitting made visible).
  * viz_ml_roc_curve — score distributions with three cuts, and the ROC
    curve those cuts trace; the SAME simulated scores as the slide's
    "Try It: a Threshold Sweep" monaco block (seed 0), so the figure is
    exactly what the students compute.
  * viz_ml_kmeans — k-means on two real blobs (found) vs on one blob
    (split anyway): the algorithm always returns k clusters.
"""
import numpy as np
import matplotlib.pyplot as plt

import style

# ---------------------------------------------------------------- polynomial
def _poly_data():
    rng = np.random.default_rng(16)
    truth = lambda x: np.sin(2 * np.pi * x)
    x_tr = np.sort(rng.uniform(0, 1, 15))
    x_te = np.sort(rng.uniform(0, 1, 15))
    y_tr = truth(x_tr) + rng.normal(0, 0.25, 15)
    y_te = truth(x_te) + rng.normal(0, 0.25, 15)
    return truth, x_tr, y_tr, x_te, y_te

def _rmse(a, b):
    return float(np.sqrt(np.mean((a - b) ** 2)))

def _polynomial_dial():
    truth, x_tr, y_tr, x_te, y_te = _poly_data()
    P = np.polynomial.Polynomial
    fig, axes = plt.subplots(1, 4, figsize=(11.5, 2.9))
    grid = np.linspace(0, 1, 300)
    panels = [(1, "Degree 1 — underfit", style.CYCLE[1]),
              (3, "Degree 3 — just right", style.CYCLE[2]),
              (10, "Degree 10 — overfit", style.BAD)]
    for ax, (deg, title, col) in zip(axes[:3], panels):
        p = P.fit(x_tr, y_tr, deg)
        ax.plot(grid, truth(grid), ls="--", lw=1.2, color=style.DIM, label="truth")
        ax.plot(grid, p(grid), color=col, lw=2.2, label=f"fit (deg {deg})")
        ax.plot(x_tr, y_tr, "o", ms=5, color=style.ACCENT, label="train")
        ax.plot(x_te, y_te, "o", ms=5, mfc="none", mec=style.FG, mew=1.2, label="test")
        ax.set_ylim(-1.9, 1.9)
        ax.set_xlim(0, 1)
        ax.set_title(title, fontsize=12)
        ax.set_xlabel("x")
        ax.text(0.03, 0.05,
                f"train {_rmse(p(x_tr), y_tr):.2f}   test {_rmse(p(x_te), y_te):.2f}",
                transform=ax.transAxes, fontsize=9.5, color=style.FG, va="bottom")
    axes[0].set_ylabel("y")
    axes[0].legend(loc="upper right", fontsize=8.5, ncol=2, handlelength=1.4,
                   columnspacing=0.8)

    degs = np.arange(1, 11)
    tr = [_rmse(P.fit(x_tr, y_tr, d)(x_tr), y_tr) for d in degs]
    te = [_rmse(P.fit(x_tr, y_tr, d)(x_te), y_te) for d in degs]
    ax = axes[3]
    ax.plot(degs, tr, "o-", color=style.ACCENT, label="train error")
    ax.plot(degs, te, "o-", color=style.BAD, label="test error")
    ax.axvline(3, color=style.CYCLE[2], lw=1.2, ls=":")
    ax.set_yscale("log")
    ax.set_xticks(degs)
    ax.set_xlabel("polynomial degree")
    ax.set_ylabel("RMSE (log)")
    ax.set_title("Train vs test error", fontsize=12)
    ax.legend(loc="upper center", fontsize=9)
    style.save(fig, "viz_ml_polynomial_dial")

# ---------------------------------------------------------------------- ROC
def _roc_scores():
    # Identical to the "Try It: a Threshold Sweep in NumPy" slide.
    rng = np.random.default_rng(0)
    bkg = rng.normal(0.35, 0.15, 2000).clip(0, 1)
    sig = rng.normal(0.65, 0.15, 200).clip(0, 1)
    return bkg, sig

def _roc_curve():
    bkg, sig = _roc_scores()
    cuts = (0.3, 0.5, 0.7)
    cut_cols = (style.CYCLE[1], style.CYCLE[2], style.CYCLE[3])
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8.8, 3.3),
                                   gridspec_kw={"width_ratios": [1.25, 1]})

    bins = np.linspace(0, 1, 41)
    ax0.hist(bkg, bins=bins, density=True, color=style.DIM, alpha=0.75,
             label="background (2000)")
    ax0.hist(sig, bins=bins, density=True, color=style.ACCENT, alpha=0.7,
             label="signal (200)")
    ax0.set_ylim(0, 4.0)
    for c, col in zip(cuts, cut_cols):
        ax0.axvline(c, color=col, lw=1.8, ls="--")
        ax0.text(c + 0.01, 0.97, f"cut {c}", color=col, fontsize=10, va="top",
                 transform=ax0.get_xaxis_transform())
    ax0.set_xlabel("classifier score")
    ax0.set_ylabel("density (each class normalised)")
    ax0.set_title("Scores overlap — where do you cut?", fontsize=12)
    ax0.legend(loc="upper right", bbox_to_anchor=(1.0, 0.9), fontsize=10,
               frameon=True, facecolor="#0b0e14", edgecolor="none", framealpha=0.85)

    thr = np.linspace(1, 0, 401)
    tpr = np.array([(sig >= t).mean() for t in thr])
    fpr = np.array([(bkg >= t).mean() for t in thr])
    auc = (sig[:, None] > bkg[None, :]).mean()
    ax1.plot([0, 1], [0, 1], ls="--", lw=1.2, color=style.DIM, label="coin flip (AUC 0.5)")
    ax1.plot(fpr, tpr, color=style.ACCENT, lw=2.2, label=f"this model (AUC {auc:.2f})")
    label_at = {0.3: (0.56, 0.72), 0.5: (0.30, 0.52), 0.7: (0.14, 0.18)}
    for c, col in zip(cuts, cut_cols):
        x, y = (bkg >= c).mean(), (sig >= c).mean()
        ax1.plot(x, y, "o", ms=8, color=col, zorder=4)
        ax1.annotate(f"cut {c}\nTPR {y:.2f}, FPR {x:.2f}", xy=(x, y),
                     xytext=label_at[c], color=col, fontsize=10,
                     arrowprops=dict(arrowstyle="-", color=col, lw=0.9))
    ax1.set_xlim(-0.02, 1.02)
    ax1.set_ylim(-0.02, 1.02)
    ax1.set_xlabel("false-positive rate (background kept)")
    ax1.set_ylabel("true-positive rate (recall)")
    ax1.set_title("ROC — every cut at once", fontsize=12)
    ax1.legend(loc="lower right", fontsize=10)
    style.save(fig, "viz_ml_roc_curve")

# ------------------------------------------------------------------ k-means
def _kmeans(X, k, rng, iters=10):
    c = X[rng.choice(len(X), k, replace=False)]
    for _ in range(iters):
        d = ((X[:, None] - c) ** 2).sum(2)
        lab = d.argmin(1)
        c = np.array([X[lab == j].mean(0) for j in range(k)])
    return lab, c

def _kmeans_fig():
    rng = np.random.default_rng(1)
    A = rng.normal([0, 0], 0.5, (150, 2))
    B = rng.normal([3, 3], 0.5, (150, 2))
    two = np.vstack([A, B])
    one = rng.normal([1.5, 1.5], 0.9, (300, 2))
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 3.2), sharex=True, sharey=True)
    cols = (style.ACCENT, style.CYCLE[1])
    for ax, X, title in zip(axes, (two, one),
                            ("Two real blobs, k = 2 — found",
                             "One blob, k = 2 — split anyway")):
        lab, c = _kmeans(X, 2, rng)
        for j in range(2):
            ax.plot(*X[lab == j].T, "o", ms=4, color=cols[j], alpha=0.8)
        ax.plot(*c.T, "X", ms=13, color=style.FG, mec="#0b0e14", mew=1.2, zorder=5,
                label="centres")
        ax.set_title(title, fontsize=12)
        ax.set_xlabel("feature 1")
        ax.set_aspect("equal")
    axes[0].set_ylabel("feature 2")
    axes[0].legend(loc="upper left", fontsize=9)
    axes[1].text(0.5, 0.03, "k-means always returns k clusters",
                 transform=axes[1].transAxes, ha="center", va="bottom",
                 fontsize=10, color=style.BAD)
    style.save(fig, "viz_ml_kmeans")

FIGURES = {
    "viz_ml_polynomial_dial": _polynomial_dial,
    "viz_ml_roc_curve": _roc_curve,
    "viz_ml_kmeans": _kmeans_fig,
}
