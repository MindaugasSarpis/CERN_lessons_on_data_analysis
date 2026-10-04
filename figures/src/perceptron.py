"""Figures of Lecture 11: The Perceptron.

Every figure is computed from the same numbers as the slides:

  * the two-class dataset of the deck's training-loop slide
    (np.random.default_rng(11), 100 points around (0, 0) and 100 around
    (2, 2), unit spread);
  * Rosenblatt's rule on the AND gate from zero weights, points in the order
    (0,0), (0,1), (1,0), (1,1), learning rate 1: ten updates;
  * the logistic neuron trained by gradient descent with learning rate 0.5
    for 1000 epochs.

Run:  python figures/src/build.py --only perceptron
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

import style

C0 = style.CYCLE[1]      # class 0: orange circles
C1 = style.ACCENT        # class 1: cyan triangles
LINE = style.FG
GREEN = style.CYCLE[2]
PINK = style.CYCLE[3]
VIOLET = style.CYCLE[4]


# ------------------------------------------------------------------ numbers
def _data():
    """The dataset of the slide 'The Training Loop', exactly as typed there."""
    rng = np.random.default_rng(11)
    X = np.vstack([rng.normal((0, 0), 1, (100, 2)),
                   rng.normal((2, 2), 1, (100, 2))])
    y = np.repeat([0, 1], 100)
    return X, y


def _sig(z):
    return 1 / (1 + np.exp(-z))


def _loss(X, y, w, b):
    """Cross-entropy in the form ln(1 + e^z) - y z, which cannot overflow."""
    z = X @ w + b
    return float(np.mean(np.logaddexp(0, z) - y * z))


def _train(X, y, eta, epochs, w=None, b=0.0):
    """Gradient descent as on the slide. Entry k is the state after k updates."""
    w = np.zeros(X.shape[1]) if w is None else np.array(w, dtype=float)
    hist = []
    with np.errstate(over="ignore"):
        for _ in range(epochs + 1):
            p = _sig(X @ w + b)
            hist.append((_loss(X, y, w, b), float(np.mean((p > 0.5) == y)),
                         w.copy(), float(b)))
            w = w - eta * X.T @ (p - y) / len(y)
            b = b - eta * np.mean(p - y)
    return hist


GATE = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
AND = np.array([0, 0, 0, 1])
OR = np.array([0, 1, 1, 1])
XOR = np.array([0, 1, 1, 0])


def _rosenblatt(X, y, epochs, eta=1.0):
    """Rosenblatt's rule from zero weights. Returns the list of updates:
    (index of the point, w after, b after)."""
    w = np.zeros(X.shape[1])
    b = 0.0
    updates = []
    for _ in range(epochs):
        for i, (x, t) in enumerate(zip(X, y)):
            e = t - int(w @ x + b > 0)
            if e != 0:
                w = w + eta * e * x
                b = b + eta * e
                updates.append((i, w.copy(), b))
    return updates


# ------------------------------------------------------------------ helpers
def _scatter(ax, X, y, ms=5.0, alpha=0.9, labels=True):
    ax.plot(X[y == 0, 0], X[y == 0, 1], "o", ms=ms, color=C0, alpha=alpha,
            mec="none", label="class 0" if labels else None)
    ax.plot(X[y == 1, 0], X[y == 1, 1], "^", ms=ms + 0.5, color=C1, alpha=alpha,
            mec="none", label="class 1" if labels else None)


def _boundary(ax, w, b, xlim, **kw):
    """Draw the line w1 x1 + w2 x2 + b = 0 across xlim."""
    x1 = np.array(xlim, dtype=float)
    if abs(w[1]) > 1e-12:
        ax.plot(x1, -(w[0] * x1 + b) / w[1], **kw)
    else:
        ax.axvline(-b / w[0], **kw)


def _frame(ax, xlim, ylim, equal=True):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if equal:
        ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")


def _gate_points(ax, y, ms=11):
    for (a, b_), t in zip(GATE, y):
        ax.plot(a, b_, "^" if t else "o", ms=ms + (1 if t else 0),
                color=C1 if t else C0, mec="none", zorder=5)


def _shade(ax, w, b, xlim, ylim, color=C1, alpha=0.10):
    """Shade the side of the line where z > 0."""
    g1, g2 = np.meshgrid(np.linspace(*xlim, 200), np.linspace(*ylim, 200))
    z = w[0] * g1 + w[1] * g2 + b
    ax.contourf(g1, g2, z, levels=[0, 1e9], colors=[color], alpha=alpha)


def _arrow(ax, p, q, color=LINE, lw=2.0, ms=14, zorder=6):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=ms,
                                 lw=lw, color=color, zorder=zorder,
                                 shrinkA=0, shrinkB=0))


def _epoch_axis(ax, last=1000):
    """Epochs on a logarithmic axis that still shows epoch 0."""
    ax.set_xscale("symlog", linthresh=1)
    ticks = [0, 1, 10, 100, 1000] + ([5000] if last > 1000 else [])
    ax.set_xticks(ticks)
    ax.set_xticklabels([str(t) for t in ticks])
    ax.set_xlim(0, last)
    ax.set_xlabel("epoch (logarithmic from 1)")
    ax.minorticks_off()


def _loss_axis(ax, ticks):
    ax.set_yscale("log")
    ax.set_yticks(ticks)
    ax.set_yticklabels([f"{t:g}" for t in ticks])
    ax.minorticks_off()
    ax.set_ylabel("cross-entropy loss (logarithmic)")


# ------------------------------------------------------------- 1. the data
def _points():
    X, y = _data()
    fig, ax = style.new_fig(5.6, 4.6)
    _scatter(ax, X, y)
    _frame(ax, (-3, 5.5), (-2.6, 6.2))
    ax.legend(loc="upper left")
    ax.set_title("200 points, two inputs, one label")
    style.save(fig, "viz_perceptron_points")


def _threshold_vs_line():
    X, y = _data()
    h = _train(X, y, 0.5, 1000)
    _, acc, w, b = h[-1]
    ts = np.sort(X[:, 0])
    accs = [np.mean((X[:, 0] > t) == y) for t in ts]
    t_best = ts[int(np.argmax(accs))]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    ax = axes[0]
    _scatter(ax, X, y)
    ax.axvline(t_best, color=LINE, lw=2.2)
    ax.axvspan(t_best, 5.5, color=C1, alpha=0.08, lw=0)
    _frame(ax, (-3, 5.5), (-2.6, 6.2))
    ax.set_title(f"One input: class 1 if $x_1$ > {t_best:.2f}")
    ax.text(0.03, 0.95, f"{100 * max(accs):.1f} % correct", transform=ax.transAxes,
            va="top", fontsize=12, color=LINE)
    ax = axes[1]
    _scatter(ax, X, y)
    _shade(ax, w, b, (-3, 5.5), (-2.6, 6.2))
    _boundary(ax, w, b, (-3, 5.5), color=LINE, lw=2.2)
    _frame(ax, (-3, 5.5), (-2.6, 6.2))
    ax.set_title("Two inputs: class 1 above a line")
    ax.text(0.03, 0.95, f"{100 * acc:.1f} % correct", transform=ax.transAxes,
            va="top", fontsize=12, color=LINE)
    ax.legend(loc="lower left", fontsize=9)
    style.save(fig, "viz_perceptron_threshold_vs_line")


# ------------------------------------------------------------ 2. the neuron
def _unit(name, box_label, out_note):
    fig, ax = plt.subplots(figsize=(9.2, 3.3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.6)
    ax.axis("off")
    ax.grid(False)
    ins = [(1.0, 3.0, "$x_1$", "$w_1$", C1), (1.0, 1.8, "$x_2$", "$w_2$", C1),
           (1.0, 0.6, "1", "$b$", style.DIM)]
    for x, yy, lab, wl, col in ins:
        ax.add_patch(Circle((x, yy), 0.36, fc="none", ec=col, lw=2))
        ax.text(x, yy, lab, ha="center", va="center", fontsize=15, color=LINE)
        _arrow(ax, (x + 0.4, yy), (4.02, 1.8 + (yy - 1.8) * 0.32), color=style.DIM, lw=1.6)
        ax.text(2.25, yy + (0.08 if yy > 1.8 else 0.26 if yy == 1.8 else 0.52),
                wl, ha="center", va="bottom", fontsize=14, color=C0)
    ax.add_patch(Circle((4.6, 1.8), 0.62, fc="none", ec=LINE, lw=2.2))
    ax.text(4.6, 1.8, r"$\Sigma$", ha="center", va="center", fontsize=22, color=LINE)
    ax.text(4.6, 0.72, r"$z = \mathbf{w} \cdot \mathbf{x} + b$", ha="center", va="center",
            fontsize=13, color=LINE)
    _arrow(ax, (5.25, 1.8), (6.35, 1.8), color=style.DIM, lw=1.6)
    ax.text(5.8, 1.98, "$z$", ha="center", va="bottom", fontsize=14, color=LINE)
    ax.add_patch(FancyBboxPatch((6.4, 1.25), 1.5, 1.1, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc="none", ec=GREEN, lw=2.2))
    ax.text(7.15, 1.8, box_label, ha="center", va="center", fontsize=15, color=LINE)
    _arrow(ax, (7.95, 1.8), (9.0, 1.8), color=style.DIM, lw=1.6)
    ax.text(9.4, 1.8, r"$\hat{y}$", ha="center", va="center", fontsize=20, color=LINE)
    ax.text(7.15, 0.72, out_note, ha="center", va="center", fontsize=12, color=style.DIM)
    style.save(fig, name)


def _unit_step():
    _unit("viz_perceptron_unit_step", "step", r"$\hat{y}$ = 1 if $z$ > 0, else 0")


def _gates():
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 3.4))
    lim = (-0.6, 1.8)
    for ax, y, b, name in [(axes[0], AND, -1.5, "AND"), (axes[1], OR, -0.5, "OR")]:
        w = np.array([1.0, 1.0])
        _shade(ax, w, b, lim, lim)
        _boundary(ax, w, b, lim, color=LINE, lw=2.2)
        _gate_points(ax, y)
        _frame(ax, lim, lim)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_title(f"{name}:  $x_1 + x_2 {b:+.1f} = 0$".replace("-", "−"), fontsize=12)
    style.save(fig, "viz_perceptron_gates")


def _line():
    """w = (3, 4), b = -10: boundary, normal vector, distance of a point."""
    w = np.array([3.0, 4.0])
    b = -10.0
    n = w / np.linalg.norm(w)
    xlim, ylim = (-1.0, 6.2), (-1.2, 4.2)
    fig, ax = style.new_fig(6.0, 4.4)
    _shade(ax, w, b, xlim, ylim)
    _boundary(ax, w, b, xlim, color=LINE, lw=2.4)
    # the weight vector, drawn from the point of the line nearest the origin
    foot0 = -b / (w @ w) * w                       # (1.2, 1.6)
    _arrow(ax, foot0, foot0 + 1.5 * n, color=C0, lw=2.6, ms=18)
    ax.text(*(foot0 + 1.5 * n + np.array([0.12, 0.05])), r"$\mathbf{w}$ = (3, 4)", color=C0,
            fontsize=13, va="bottom")
    # distance of the origin
    ax.plot([0, foot0[0]], [0, foot0[1]], ls=":", color=style.DIM, lw=1.6)
    ax.text(-0.12, -0.3, "origin", color=style.DIM, fontsize=10, ha="right")
    ax.plot(0, 0, "o", color=style.DIM, ms=6)
    ax.text(0.36, 1.02, r"$|b|/\|\mathbf{w}\|$ = 2", color=style.DIM, fontsize=11,
            rotation=53, ha="center", va="center")
    # the point x = (4, 2) and its foot
    x = np.array([4.0, 2.0])
    d = (w @ x + b) / np.linalg.norm(w)
    foot = x - d * n
    ax.plot([foot[0], x[0]], [foot[1], x[1]], color=GREEN, lw=2.4)
    ax.plot(*x, "^", color=C1, ms=11, zorder=6)
    ax.plot(*foot, "o", color=LINE, ms=5, zorder=6)
    ax.text(x[0] + 0.15, x[1] + 0.1, r"$\mathbf{x}$ = (4, 2)" + "\n$z$ = 10", color=LINE, fontsize=11.5,
            va="bottom")
    ax.text(*(0.5 * (x + foot) + np.array([0.12, -0.3])), "$d$ = 2", color=GREEN, fontsize=13)
    # a point on the other side
    x2 = np.array([1.0, 0.5])
    ax.plot(*x2, "o", color=C0, ms=10, zorder=6)
    ax.text(x2[0] + 0.15, x2[1] - 0.1, "(1, 0.5)\n$z$ = −5", color=LINE, fontsize=11.5,
            va="top")
    ax.text(4.9, 3.7, "$z$ > 0", color=C1, fontsize=13)
    ax.text(-0.8, -0.95, "$z$ < 0", color=C0, fontsize=13)
    ax.text(3.9, -0.62, "$3x_1 + 4x_2 - 10 = 0$", color=LINE, fontsize=12, rotation=-36.9,
            ha="center", va="center")
    _frame(ax, xlim, ylim)
    style.save(fig, "viz_perceptron_line")


def _wb():
    lim = (-0.5, 4.5)
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.9))
    # (a) turn w
    ax = axes[0]
    p0 = np.array([2.0, 2.0])
    for w, col in [((1.0, 1.0), LINE), ((1.0, 0.25), C1), ((0.25, 1.0), C0)]:
        w = np.array(w)
        b = -w @ p0
        _boundary(ax, w, b, lim, color=col, lw=2)
        _arrow(ax, p0, p0 + 1.1 * w / np.linalg.norm(w), color=col, lw=2, ms=13)
    ax.plot(*p0, "o", color=style.DIM, ms=5, zorder=7)
    ax.set_title(r"Turn $\mathbf{w}$: the line turns", fontsize=13)
    # (b) change b
    ax = axes[1]
    for b, col in [(-2.0, C1), (-4.0, LINE), (-6.0, C0)]:
        _boundary(ax, np.array([1.0, 1.0]), b, lim, color=col, lw=2)
        c = -b
        ax.text(c / 2 + 0.75, c / 2 - 0.45, f"$b$ = {b:.0f}".replace("-", "−"), color=col,
                fontsize=11, rotation=-45, ha="center", va="center")
    ax.set_title("Change $b$: the line shifts", fontsize=13)
    # (c) scale both
    ax = axes[2]
    _boundary(ax, np.array([1.0, 1.0]), -4.0, lim, color=LINE, lw=2)
    _arrow(ax, (2.0, 2.0), (2.5, 2.5), color=C1, lw=2.4, ms=13)
    _arrow(ax, (1.2, 2.8), (2.2, 3.8), color=C0, lw=2.4, ms=13)
    ax.text(2.6, 2.2, r"$\mathbf{w}$ = (1, 1), $b$ = −4", color=C1, fontsize=10.5)
    ax.text(0.2, 4.05, r"$\mathbf{w}$ = (2, 2), $b$ = −8", color=C0, fontsize=10.5)
    ax.set_title(r"Scale $\mathbf{w}$ and $b$: the same line", fontsize=13)
    for ax in axes:
        _frame(ax, lim, lim)
        ax.set_xticks([0, 2, 4])
        ax.set_yticks([0, 2, 4])
    style.save(fig, "viz_perceptron_wb")


# -------------------------------------------------- 3. Rosenblatt's rule
def _and_run():
    ups = _rosenblatt(GATE, AND, 6)
    assert len(ups) == 10, len(ups)
    lim = (-1.6, 2.6)
    fig, axes = plt.subplots(2, 5, figsize=(11.5, 4.9))
    for k, (ax, (i, w, b)) in enumerate(zip(axes.ravel(), ups), start=1):
        if np.any(w != 0):
            _shade(ax, w, b, lim, lim)
            _boundary(ax, w, b, lim, color=LINE, lw=1.8)
        _gate_points(ax, AND, ms=7)
        ax.plot(*GATE[i], "o", ms=15, mfc="none", mec=style.BAD, mew=1.8, zorder=6)
        ax.set_xlim(*lim)
        ax.set_ylim(*lim)
        ax.set_aspect("equal")
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.tick_params(labelsize=8)
        ax.set_title(f"{k}:  $\\mathbf{{w}}$ = ({w[0]:.0f}, {w[1]:.0f}),  $b$ = {b:.0f}".replace("-", "−"),
                     fontsize=10.5, fontweight="normal")
    style.save(fig, "viz_perceptron_and_run")


def _separable():
    rng = np.random.default_rng(3)
    A = rng.normal((0, 0), 0.7, (25, 2))
    B = rng.normal((3.2, 3.2), 0.7, (25, 2))
    Xs = np.vstack([A, B])
    ys = np.repeat([0, 1], 25)
    w = np.array([1.0, 1.0])
    # the line x1 + x2 = c half-way between the closest points of the classes
    s = Xs @ w
    c = 0.5 * (s[ys == 0].max() + s[ys == 1].min())
    gap = (s[ys == 1].min() - s[ys == 0].max()) / np.linalg.norm(w)
    lim = (-2.4, 5.4)
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.6))
    ax = axes[0]
    _scatter(ax, Xs, ys, ms=6)
    _boundary(ax, w, -c, lim, color=LINE, lw=2.2)
    for off in (-1, 1):
        _boundary(ax, w, -(c + off * 0.5 * gap * np.linalg.norm(w)), lim,
                  color=style.DIM, lw=1.2, ls="--")
    _frame(ax, lim, lim)
    ax.set_title("Linearly separable")
    ax.text(0.04, 0.05, f"margin $\\gamma$ = {gap / 2:.2f}", transform=ax.transAxes,
            fontsize=12, color=LINE)
    ax = axes[1]
    X, y = _data()
    _scatter(ax, X, y, ms=5)
    h = _train(X, y, 0.5, 1000)
    _boundary(ax, h[-1][2], h[-1][3], (-3, 5.5), color=LINE, lw=2.2)
    _frame(ax, (-3, 5.5), (-2.6, 6.2))
    wrong = int(np.sum((X @ h[-1][2] + h[-1][3] > 0) != y))
    ax.set_title("Not linearly separable")
    ax.text(0.04, 0.95, f"{wrong} of 200 on the wrong side", transform=ax.transAxes,
            fontsize=12, color=LINE, va="top")
    style.save(fig, "viz_perceptron_separable")


def _proof():
    """The two inequalities of the convergence proof, on the AND run."""
    Xa = np.hstack([np.ones((4, 1)), GATE])            # (1, x1, x2)
    w_star = np.array([-3.0, 2.0, 2.0]) / np.sqrt(17)
    gamma = 1 / np.sqrt(17)
    R = np.sqrt(3.0)
    ups = _rosenblatt(GATE, AND, 6)
    wt = np.array([[b, w[0], w[1]] for _, w, b in ups])
    k = np.arange(1, len(ups) + 1)
    proj = wt @ w_star
    norm = np.linalg.norm(wt, axis=1)
    assert np.all(proj >= k * gamma - 1e-12) and np.all(norm <= np.sqrt(k) * R + 1e-12)
    kk = np.linspace(0, 60, 400)
    fig, ax = style.new_fig(5.8, 4.4)
    ax.plot(kk, np.sqrt(kk) * R, color=C0, lw=2.2, label=r"upper bound  $\sqrt{k}\,R$")
    ax.plot(kk, kk * gamma, color=C1, lw=2.2, label=r"lower bound  $k\,\gamma$")
    ax.plot(k, norm, "s", color=C0, ms=6, label=r"length  $\|\tilde{\mathbf{w}}_k\|$ in the run")
    ax.plot(k, proj, "o", color=C1, ms=6, label=r"$\tilde{\mathbf{w}}^* \cdot \tilde{\mathbf{w}}_k$ in the run")
    kmax = (R / gamma) ** 2
    ax.axvline(kmax, color=LINE, lw=1.4, ls="--")
    ax.text(kmax - 0.8, 3.6, f"the bounds cross at\n$k = R^2/\\gamma^2$ = {kmax:.0f}",
            ha="right", color=LINE, fontsize=10.5)
    ax.axvline(10, color=style.DIM, lw=1.2, ls=":")
    ax.text(11.0, 0.3, "the run stops\nafter 10 updates", color=style.DIM, fontsize=10,
            va="bottom")
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 14.5)
    ax.set_xlabel("number of updates $k$")
    ax.legend(loc="upper left", fontsize=9.5, bbox_to_anchor=(0.215, 1.02))
    style.save(fig, "viz_perceptron_proof")


def _rule_overlap():
    """Rosenblatt's rule on the overlapping dataset: it never stops."""
    X, y = _data()
    order = np.random.default_rng(0).permutation(len(y))
    w = np.zeros(2)
    b = 0.0
    wrong, lines = [], {}
    for epoch in range(1, 101):
        for i in order:
            e = y[i] - int(w @ X[i] + b > 0)
            if e != 0:
                w = w + e * X[i]
                b = b + e
        wrong.append(int(np.sum((X @ w + b > 0) != y)))
        if epoch in (98, 99, 100):
            lines[epoch] = (w.copy(), b)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), gridspec_kw={"width_ratios": [1.25, 1]})
    ax = axes[0]
    ax.plot(range(1, 101), wrong, "-", color=C1, lw=1.6)
    ax.plot(range(1, 101), wrong, "o", color=C1, ms=3)
    ax.set_ylim(0, 30)
    ax.set_xlim(0, 101)
    ax.set_xlabel("epoch")
    ax.set_ylabel("points on the wrong side, of 200")
    ax.set_title(f"Between {min(wrong)} and {max(wrong)} wrong, never 0")
    ax = axes[1]
    _scatter(ax, X, y, ms=4, alpha=0.75, labels=False)
    for (epoch, (w_, b_)), col in zip(lines.items(), [PINK, GREEN, LINE]):
        _boundary(ax, w_, b_, (-3, 5.5), color=col, lw=2, label=f"after epoch {epoch}")
    _frame(ax, (-3, 5.5), (-2.6, 6.2), equal=False)
    ax.legend(loc="lower left", fontsize=9, ncol=3, columnspacing=1.0, handlelength=1.3,
              bbox_to_anchor=(0.0, 1.0), borderaxespad=0.2)
    ax.set_title("The line keeps moving", pad=24)
    style.save(fig, "viz_perceptron_rule_overlap")


# ------------------------------------------------- 4. step and sigmoid
def _step_loss():
    """Errors and cross-entropy along one parameter, b, with w fixed."""
    X, y = _data()
    w = np.array([2.0, 2.0])
    bs = np.linspace(-9, 1, 1001)
    errs = [int(np.sum((X @ w + b > 0) != y)) for b in bs]
    ce = [_loss(X, y, w, b) for b in bs]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.0))
    ax = axes[0]
    ax.plot(bs, errs, color=C0, lw=2, drawstyle="steps-mid")
    ax.set_xlabel(r"bias $b$   (with $\mathbf{w}$ = (2, 2) fixed)")
    ax.set_ylabel("points on the wrong side")
    ax.set_title("Number of errors: flat, then a jump")
    ax.set_ylim(0, 105)
    ax = axes[1]
    ax.plot(bs, ce, color=C1, lw=2.2)
    i = int(np.argmin(ce))
    ax.plot(bs[i], ce[i], "o", color=LINE, ms=6)
    ax.text(bs[i], ce[i] + 0.22, f"minimum at $b$ = {bs[i]:.2f}".replace("-", "−"),
            ha="center", color=LINE, fontsize=11)
    ax.set_xlabel(r"bias $b$   (with $\mathbf{w}$ = (2, 2) fixed)")
    ax.set_ylabel("cross-entropy loss")
    ax.set_title("Cross-entropy: a slope everywhere")
    ax.set_ylim(0, None)
    style.save(fig, "viz_perceptron_step_loss")


def _sigmoid():
    z = np.linspace(-7, 7, 600)
    fig, axes = plt.subplots(2, 1, figsize=(5.6, 5.3), sharex=True)
    ax = axes[0]
    ax.plot(z, (z > 0).astype(float), color=C0, lw=2, label="step")
    ax.plot(z, _sig(z), color=C1, lw=2.4, label=r"sigmoid  $\sigma(z)$")
    for zz in (-2, 0, 2):
        ax.plot(zz, _sig(zz), "o", color=LINE, ms=5)
        ax.text(zz + 0.3, _sig(zz) - 0.07, f"{_sig(zz):.3g}", color=LINE, fontsize=10.5)
    ax.set_ylabel(r"output  $\hat{y}$")
    ax.legend(loc="upper left")
    ax = axes[1]
    s = _sig(z)
    ax.plot(z, s * (1 - s), color=GREEN, lw=2.4)
    ax.plot(0, 0.25, "o", color=LINE, ms=5)
    ax.text(0.4, 0.245, "0.25 at $z$ = 0", color=LINE, fontsize=10.5, va="center")
    ax.set_xlabel("$z$")
    ax.set_ylabel(r"slope  $\sigma'(z)$")
    ax.set_ylim(0, 0.29)
    style.save(fig, "viz_perceptron_sigmoid")


def _posterior():
    """Two Gaussian classes in one dimension give a sigmoid posterior."""
    x = np.linspace(-3.5, 5.5, 600)
    g = lambda m: np.exp(-0.5 * (x - m) ** 2) / np.sqrt(2 * np.pi)
    p0, p1 = g(0.0), g(2.0)
    post = p1 / (p0 + p1)
    assert np.allclose(post, _sig(2 * x - 2))
    fig, axes = plt.subplots(2, 1, figsize=(6.2, 4.7), sharex=True)
    ax = axes[0]
    ax.fill_between(x, p0, color=C0, alpha=0.25, lw=0)
    ax.plot(x, p0, color=C0, lw=2, label="class 0, centre 0")
    ax.fill_between(x, p1, color=C1, alpha=0.25, lw=0)
    ax.plot(x, p1, color=C1, lw=2, label="class 1, centre 2")
    ax.set_ylabel("density")
    ax.set_ylim(0, 0.62)
    ax.legend(loc="upper left", fontsize=9, ncol=2)
    ax = axes[1]
    ax.plot(x, post, color=LINE, lw=2.4)
    ax.axvline(1, color=style.DIM, lw=1.2, ls=":")
    ax.plot(1, 0.5, "o", color=LINE, ms=5)
    ax.set_ylabel("P(class 1 | $x$)")
    ax.set_xlabel("$x$")
    ax.text(1.5, 0.22, r"$\sigma(2x - 2)$", color=LINE, fontsize=12)
    style.save(fig, "viz_perceptron_posterior")


def _probmap():
    X, y = _data()
    _, _, w, b = _train(X, y, 0.5, 1000)[-1]
    xlim, ylim = (-3, 5.5), (-2.6, 6.2)
    g1, g2 = np.meshgrid(np.linspace(*xlim, 300), np.linspace(*ylim, 300))
    p = _sig(w[0] * g1 + w[1] * g2 + b)
    fig, ax = style.new_fig(5.8, 4.8)
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("cls", [C0, "#1a2030", C1])
    ax.contourf(g1, g2, p, levels=np.linspace(0, 1, 21), cmap=cmap, alpha=0.30)
    cs = ax.contour(g1, g2, p, levels=[0.1, 0.5, 0.9], colors=[LINE],
                    linewidths=[1.2, 2.2, 1.2], linestyles=["--", "-", "--"])
    ax.clabel(cs, fmt={0.1: "0.1", 0.5: "0.5", 0.9: "0.9"}, fontsize=10, colors=LINE)
    ax.plot(X[y == 0, 0], X[y == 0, 1], "o", ms=4.5, color=C0, mec="#0b0e14", mew=0.5)
    ax.plot(X[y == 1, 0], X[y == 1, 1], "^", ms=5, color=C1, mec="#0b0e14", mew=0.5)
    _frame(ax, xlim, ylim)
    ax.set_title(r"$\hat{y}$ over the plane, after training")
    style.save(fig, "viz_perceptron_probmap")


# ----------------------------------------------------------- 5. the loss
def _cross_entropy():
    p = np.linspace(0.004, 0.996, 500)
    fig, ax = style.new_fig(6.2, 4.4)
    ax.plot(p, -np.log(p), color=C1, lw=2.4, label=r"$y = 1$:  $-\ln \hat{y}$")
    ax.plot(p, -np.log(1 - p), color=C0, lw=2.4, label=r"$y = 0$:  $-\ln(1 - \hat{y})$")
    for q, dy in [(0.5, 0.25), (0.9, 0.3), (0.1, 0.25)]:
        ax.plot(q, -np.log(q), "o", color=LINE, ms=5)
        ax.text(q + 0.02, -np.log(q) + dy, f"{-np.log(q):.3f}", color=LINE, fontsize=10.5)
    ax.set_xlabel(r"output  $\hat{y}$")
    ax.set_ylabel("loss of one point")
    ax.set_ylim(0, 5)
    ax.set_xlim(0, 1)
    ax.legend(loc="upper center")
    style.save(fig, "viz_perceptron_cross_entropy")


# ------------------------------------------------------- 6. the training
def _training():
    X, y = _data()
    h = _train(X, y, 0.5, 1000)
    xlim, ylim = (-3, 5.5), (-2.6, 6.2)
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.2))
    for ax, k in zip(axes, (1, 20, 1000)):
        loss, acc, w, b = h[k]
        _shade(ax, w, b, xlim, ylim)
        _scatter(ax, X, y, ms=4, alpha=0.85, labels=(k == 1))
        _boundary(ax, w, b, xlim, color=LINE, lw=2.2)
        _frame(ax, xlim, ylim)
        ax.set_title(f"after {k} update{'s' if k > 1 else ''}", fontsize=13)
        ax.text(0.04, 0.96, f"loss {loss:.4f}\n{100 * acc:.1f} % correct",
                transform=ax.transAxes, va="top", fontsize=11, color=LINE)
    axes[0].legend(loc="lower right", fontsize=9)
    style.save(fig, "viz_perceptron_training")


def _loss_curve():
    X, y = _data()
    h = _train(X, y, 0.5, 1000)
    loss = np.array([r[0] for r in h])
    acc = np.array([r[1] for r in h])
    ep = np.arange(len(h))
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.0))
    ax = axes[0]
    ax.plot(ep, loss, color=C1, lw=2.4)
    ax.axhline(np.log(2), color=style.DIM, lw=1.1, ls=":")
    ax.text(990, np.log(2) + 0.012, "ln 2 = 0.6931", color=style.DIM, ha="right", fontsize=10)
    for k, dy in [(0, 0), (10, 0.03), (100, 0.035), (1000, 0.035)]:
        ax.plot(k, loss[k], "o", color=LINE, ms=5)
        if k:
            ax.text(k + 15 if k < 1000 else k - 10, loss[k] + dy, f"{loss[k]:.4f}",
                    color=LINE, fontsize=10.5, ha="left" if k < 1000 else "right")
    ax.set_xlabel("epoch")
    ax.set_ylabel("cross-entropy loss")
    ax.set_ylim(0, 0.75)
    ax.set_title("The loss")
    ax = axes[1]
    ax.plot(ep, 100 * acc, color=GREEN, lw=2.2)
    _epoch_axis(ax)
    ax.set_ylim(45, 100)
    ax.set_ylabel("correct on the 200 points, %")
    ax.set_title("The accuracy")
    ax.text(0.97, 0.08, f"{100 * acc[1]:.1f} % after 1 update\n{100 * acc[-1]:.1f} % after 1000",
            transform=ax.transAxes, ha="right", fontsize=11, color=LINE)
    style.save(fig, "viz_perceptron_loss")


def _starts():
    X, y = _data()
    starts = [((0.0, 0.0), 0.0), ((1.0, -1.0), 0.0), ((-2.0, 3.0), 4.0)]
    fig, ax = style.new_fig(5.8, 4.3)
    for (w0, b0), col in zip(starts, [C1, C0, GREEN]):
        h = _train(X, y, 0.5, 5000, w=w0, b=b0)
        loss = [r[0] for r in h]
        lab = f"$\\mathbf{{w}}$ = ({w0[0]:.0f}, {w0[1]:.0f}), $b$ = {b0:.0f}".replace("-", "−")
        ax.plot(np.arange(len(h)), loss, color=col, lw=2.2,
                label=f"start {lab}:  loss {loss[0]:.4f}")
    ax.axhline(h[-1][0], color=style.DIM, lw=1.1, ls=":")
    ax.text(4500, h[-1][0] * 1.12, f"all three end at {h[-1][0]:.4f}", color=style.DIM,
            ha="right", fontsize=10.5)
    _epoch_axis(ax, 5000)
    _loss_axis(ax, [0.2, 0.5, 1, 2])
    ax.set_ylim(0.13, 3.2)
    ax.legend(loc="upper right", fontsize=9.5)
    style.save(fig, "viz_perceptron_starts")


# ------------------------------------------------------- 7. in practice
def _eta():
    X, y = _data()
    fig, ax = style.new_fig(5.8, 4.3)
    for eta, col in [(0.01, C0), (0.1, GREEN), (1, C1), (20, style.BAD)]:
        h = _train(X, y, eta, 1000)
        loss = [r[0] for r in h]
        ax.plot(np.arange(len(h)), loss, color=col, lw=2.0 if eta < 20 else 1.4,
                label=f"$\\eta$ = {eta:g}")
    _epoch_axis(ax)
    _loss_axis(ax, [0.2, 0.5, 1, 2])
    ax.set_ylim(0.13, 4.5)
    ax.legend(loc="upper right", fontsize=9.5)
    style.save(fig, "viz_perceptron_eta")


def _scaling():
    X, y = _data()
    Xs = X * np.array([1.0, 100.0])                  # x2 written in other units
    Z = (X - X.mean(0)) / X.std(0)
    fig, ax = style.new_fig(5.8, 4.3)
    runs = [(Xs, 0.5, style.BAD, r"$x_2 \times 100$, $\eta$ = 0.5"),
            (Xs, 0.0001, C0, r"$x_2 \times 100$, $\eta$ = 0.0001"),
            (Z, 0.5, C1, r"standardised, $\eta$ = 0.5")]
    for data, eta, col, lab in runs:
        h = _train(data, y, eta, 1000)
        loss = [r[0] for r in h]
        ax.plot(np.arange(len(h)), loss, color=col, lw=1.2 if col == style.BAD else 2.2,
                label=lab)
    _epoch_axis(ax)
    _loss_axis(ax, [0.1, 1, 10, 100, 1000])
    ax.set_ylim(0.1, 2500)
    ax.legend(loc="upper left", fontsize=10, bbox_to_anchor=(0.17, 0.62))
    style.save(fig, "viz_perceptron_scaling")


def _split():
    X, y = _data()
    perm = np.random.default_rng(11).permutation(200)
    tr, te = perm[:150], perm[150:]
    m, s = X[tr].mean(0), X[tr].std(0)
    _, _, wz, bz = _train((X[tr] - m) / s, y[tr], 0.5, 1000)[-1]
    w = wz / s                                       # back to the units of x
    b = bz - np.sum(wz * m / s)
    acc_tr = np.mean((X[tr] @ w + b > 0) == y[tr])
    acc_te = np.mean((X[te] @ w + b > 0) == y[te])
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1, 1.1]})
    ax = axes[0]
    ax.plot(X[tr][y[tr] == 0, 0], X[tr][y[tr] == 0, 1], "o", ms=4, color=C0, alpha=0.35, mec="none")
    ax.plot(X[tr][y[tr] == 1, 0], X[tr][y[tr] == 1, 1], "^", ms=4.5, color=C1, alpha=0.35, mec="none")
    ax.plot(X[te][y[te] == 0, 0], X[te][y[te] == 0, 1], "o", ms=6.5, color=C0, mec=LINE, mew=0.9,
            label="test, class 0")
    ax.plot(X[te][y[te] == 1, 0], X[te][y[te] == 1, 1], "^", ms=7, color=C1, mec=LINE, mew=0.9,
            label="test, class 1")
    _boundary(ax, w, b, (-3, 5.5), color=LINE, lw=2.2)
    _frame(ax, (-3, 5.5), (-2.6, 6.2))
    ax.legend(loc="upper left", fontsize=9)
    ax.set_title(f"train {100 * acc_tr:.1f} %,  test {100 * acc_te:.1f} %", fontsize=13)
    # the same for 20 other splits
    accs = []
    for seed in range(20):
        perm = np.random.default_rng(seed).permutation(200)
        tr, te = perm[:150], perm[150:]
        m, s = X[tr].mean(0), X[tr].std(0)
        _, _, wz, bz = _train((X[tr] - m) / s, y[tr], 0.5, 1000)[-1]
        accs.append(np.mean((((X[te] - m) / s) @ wz + bz > 0) == y[te]))
    accs = 100 * np.array(accs)
    ax = axes[1]
    mean = accs.mean()
    sd = 100 * np.sqrt(mean / 100 * (1 - mean / 100) / 50)
    ax.axhspan(mean - sd, mean + sd, color=C1, alpha=0.15, lw=0)
    ax.axhline(mean, color=C1, lw=1.6)
    ax.plot(range(20), accs, "o", color=LINE, ms=6)
    ax.set_xticks(range(0, 20, 2))
    ax.set_ylim(80, 100)
    ax.set_xlabel("seed of the split")
    ax.set_ylabel("test accuracy, %")
    ax.set_title(f"20 splits: mean {mean:.1f} %, band ±{sd:.1f} %", fontsize=13)
    style.save(fig, "viz_perceptron_split")


# ------------------------------------------------------------- 8. XOR
def _xor_frame(ax, lim):
    _gate_points(ax, XOR, ms=13)
    _frame(ax, lim, lim)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])


def _xor_lines():
    lim = (-0.7, 1.7)
    fig, ax = style.new_fig(4.7, 4.6)
    tries = [((1.0, 1.0), -0.5, PINK), ((1.0, -1.0), -0.5, GREEN), ((1.0, 0.0), -0.5, VIOLET)]
    for w, b, col in tries:
        w = np.array(w)
        wrong = int(np.sum((GATE @ w + b > 0) != XOR))
        _boundary(ax, w, b, lim, color=col, lw=2, label=f"{wrong} wrong")
    _xor_frame(ax, lim)
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title("Three lines tried", fontsize=13)
    style.save(fig, "viz_perceptron_xor_lines")


def _xor_strip():
    lim = (-0.7, 1.7)
    fig, ax = style.new_fig(4.7, 4.6)
    g1, g2 = np.meshgrid(np.linspace(*lim, 200), np.linspace(*lim, 200))
    ax.contourf(g1, g2, g1 + g2, levels=[0.5, 1.5], colors=[C1], alpha=0.12)
    _boundary(ax, np.array([1.0, 1.0]), -0.5, lim, color=PINK, lw=2.2, label="$x_1 + x_2 = 0.5$")
    _boundary(ax, np.array([1.0, 1.0]), -1.5, lim, color=GREEN, lw=2.2, label="$x_1 + x_2 = 1.5$")
    _xor_frame(ax, lim)
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title("Class 1 between two lines", fontsize=13)
    style.save(fig, "viz_perceptron_xor_strip")


def _xor_hidden():
    lim = (-0.7, 1.7)
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.5))
    ax = axes[0]
    _gate_points(ax, XOR)
    for (a, b_) in GATE:
        ax.text(a + 0.09, b_ + 0.09, f"({a}, {b_})", color=LINE, fontsize=10.5)
    _frame(ax, lim, lim)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_title("The inputs $(x_1, x_2)$")
    ax = axes[1]
    H = (GATE @ np.array([[1, 1], [1, 1]]).T + np.array([-0.5, -1.5]) > 0).astype(int)
    w, b = np.array([1.0, -1.0]), -0.5
    _shade(ax, w, b, lim, lim)
    _boundary(ax, w, b, lim, color=LINE, lw=2.2)
    seen = {}
    for (h1, h2), t, x in zip(H, XOR, GATE):
        seen.setdefault((h1, h2, t), []).append(f"({x[0]}, {x[1]})")
    for (h1, h2, t), names in seen.items():
        ax.plot(h1, h2, "^" if t else "o", ms=12 if t else 11, color=C1 if t else C0,
                mec="none", zorder=5)
        below = (h1, h2) == (1, 0)          # keep this label clear of the line
        ax.text(h1 if h1 == 0 else 1.05, h2 - 0.2 if below else h2 + 0.15,
                "from " + " and ".join(names), color=LINE, fontsize=10, ha="center",
                va="top" if below else "baseline")
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_aspect("equal")
    ax.set_xlabel("$h_1$")
    ax.set_ylabel("$h_2$")
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.text(0.2, -0.47, "$h_1 - h_2 = 0.5$", color=LINE, fontsize=11, rotation=45,
            ha="center", va="center")
    ax.set_title("The hidden outputs $(h_1, h_2)$")
    style.save(fig, "viz_perceptron_xor_hidden")


def _network():
    fig, ax = plt.subplots(figsize=(9.4, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.4, 4)
    ax.axis("off")
    ax.grid(False)
    xin = [(1.2, 3.0, "$x_1$"), (1.2, 1.0, "$x_2$")]
    hid = [(4.6, 3.0, "$h_1$", "$b$ = −0.5", PINK), (4.6, 1.0, "$h_2$", "$b$ = −1.5", GREEN)]
    out = (8.0, 2.0)
    for x, yy, lab in xin:
        ax.add_patch(Circle((x, yy), 0.42, fc="none", ec=C1, lw=2))
        ax.text(x, yy, lab, ha="center", va="center", fontsize=15, color=LINE)
    for x, yy, lab, bl, col in hid:
        ax.add_patch(Circle((x, yy), 0.5, fc="none", ec=col, lw=2.2))
        ax.text(x, yy, lab, ha="center", va="center", fontsize=15, color=LINE)
        ax.text(x, yy + (0.72 if yy > 2 else -0.72), bl, ha="center", va="center",
                fontsize=12, color=col)
    ax.add_patch(Circle(out, 0.5, fc="none", ec=LINE, lw=2.2))
    ax.text(*out, r"$\hat{y}$", ha="center", va="center", fontsize=17, color=LINE)
    ax.text(out[0], out[1] - 0.76, "$b$ = −0.5", ha="center", va="center", fontsize=12,
            color=LINE)
    # arrows input -> hidden, each with its weight written beside it
    labels = {(3.0, 3.0): (2.4, 3.12), (3.0, 1.0): (2.05, 2.66),
              (1.0, 3.0): (2.05, 1.12), (1.0, 1.0): (2.4, 0.62)}
    for x, yy, _ in xin:
        for hx, hy, _, _, col in hid:
            p = np.array([x + 0.44, yy + (0.0 if hy == yy else (0.12 if hy > yy else -0.12))])
            q = np.array([hx - 0.53, hy + (0.0 if hy == yy else (-0.16 if hy > yy else 0.16))])
            _arrow(ax, p, q, color=style.DIM, lw=1.5, ms=12)
            ax.text(*labels[(yy, hy)], "1", color=C0, fontsize=13, ha="center")
    for hx, hy, _, _, col in hid:
        p = np.array([hx + 0.53, hy + (-0.12 if hy > 2 else 0.12)])
        q = np.array([out[0] - 0.5, out[1] + (0.2 if hy > 2 else -0.2)])
        _arrow(ax, p, q, color=style.DIM, lw=1.5, ms=12)
        mid = 0.5 * (p + q)
        ax.text(mid[0], mid[1] + (0.2 if hy > 2 else -0.42), "1" if hy > 2 else "−1",
                color=C0, fontsize=13, ha="center")
    ax.text(1.2, 3.75, "inputs", ha="center", color=style.DIM, fontsize=11.5)
    ax.text(4.6, -0.3, "hidden layer: two step neurons", ha="center", color=style.DIM,
            fontsize=11.5)
    ax.text(8.0, 3.02, "output: one step neuron", ha="center", color=style.DIM, fontsize=11.5)
    style.save(fig, "viz_perceptron_network")


FIGURES = {
    "viz_perceptron_points": _points,
    "viz_perceptron_threshold_vs_line": _threshold_vs_line,
    "viz_perceptron_unit_step": _unit_step,
    "viz_perceptron_gates": _gates,
    "viz_perceptron_line": _line,
    "viz_perceptron_wb": _wb,
    "viz_perceptron_and_run": _and_run,
    "viz_perceptron_separable": _separable,
    "viz_perceptron_proof": _proof,
    "viz_perceptron_rule_overlap": _rule_overlap,
    "viz_perceptron_step_loss": _step_loss,
    "viz_perceptron_sigmoid": _sigmoid,
    "viz_perceptron_posterior": _posterior,
    "viz_perceptron_probmap": _probmap,
    "viz_perceptron_cross_entropy": _cross_entropy,
    "viz_perceptron_training": _training,
    "viz_perceptron_loss": _loss_curve,
    "viz_perceptron_starts": _starts,
    "viz_perceptron_eta": _eta,
    "viz_perceptron_scaling": _scaling,
    "viz_perceptron_split": _split,
    "viz_perceptron_xor_lines": _xor_lines,
    "viz_perceptron_xor_strip": _xor_strip,
    "viz_perceptron_xor_hidden": _xor_hidden,
    "viz_perceptron_network": _network,
}
