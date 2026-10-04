"""Figures and numbers for Lecture 16, Machine Learning & AI.

The lecture continues from Lecture 11 (one neuron, z = w.x + b, the sigmoid,
the cross-entropy loss, gradient descent). Notation of the network with one
hidden layer, the same on the slides and in this file:

    hidden unit j   u_j = v_j1 x_1 + v_j2 x_2 + c_j     h_j = sigma(u_j)
    output neuron   z   = w_1 h_1 + w_2 h_2 + ... + b   yhat = sigma(z)
    loss            L   = -[y ln yhat + (1 - y) ln(1 - yhat)]

Three data sets:

  * XOR             four points, set in this file.
  * ml_two_class    lectures/workbook/docs/data/ml_two_class.csv, 600 rows,
                    made by ml_two_class.py next to it (seed 16).
  * D0_KPi.csv      the LHCb file, for the leakage example.

Every number on the slides, the seminar page and the lecture page comes from
the functions in the first half of this file. Print them all with

    python figures/src/ml.py

(needs numpy; the checks against scikit-learn need scikit-learn and are
skipped without it). The second half draws public/figures/viz_ml_*.svg;
build them with

    python figures/src/build.py --only ml
"""
from functools import lru_cache

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data"

C1 = style.ACCENT        # class 1
C0 = style.CYCLE[1]      # class 0
BG = "#0b0e14"


# =============================================================================
# Numbers
# =============================================================================

def sigma(z):
    return 1 / (1 + np.exp(-z))


def loss(y, yhat):
    yhat = np.clip(yhat, 1e-12, 1 - 1e-12)
    return float(-np.mean(y * np.log(yhat) + (1 - y) * np.log(1 - yhat)))


def train(X, y, H, seed=0, eta=1.0, steps=5000, init=None, watch=None):
    """Full-batch gradient descent for a network with H hidden units.

    The loop is the one on the slide "The Training Loop in NumPy". `watch`,
    if given, is called as watch(step, V, c, w, b, yhat) before each update.
    """
    rng = np.random.default_rng(seed)
    V, c = rng.normal(0, 1, (H, X.shape[1])), np.zeros(H)
    w, b = rng.normal(0, 1, H), 0.0
    if init is not None:
        V, c, w, b = (np.array(a, float) for a in init)
        b = float(b)
    for step in range(steps):
        h = sigma(X @ V.T + c)
        yhat = sigma(h @ w + b)
        if watch is not None:
            watch(step, V, c, w, b, yhat)
        d = (yhat - y) / len(y)
        dh = np.outer(d, w) * h * (1 - h)
        w -= eta * h.T @ d
        b -= eta * d.sum()
        V -= eta * dh.T @ X
        c -= eta * dh.sum(axis=0)
    return V, c, w, b


def hidden(p, X):
    return sigma(X @ p[0].T + p[1])


def predict(p, X):
    return sigma(hidden(p, X) @ p[2] + p[3])


def train_neuron(X, y, eta=1.0, steps=5000):
    """The single sigmoid neuron of Lecture 11."""
    w, b = np.zeros(X.shape[1]), 0.0
    for _ in range(steps):
        yhat = sigma(X @ w + b)
        w -= eta * X.T @ (yhat - y) / len(y)
        b -= eta * np.mean(yhat - y)
    return w, b


def n_parameters(*sizes):
    """Weights and biases of a fully connected network, e.g. (2, 2, 1) -> 9."""
    return sum(m * n + m for n, m in zip(sizes, sizes[1:]))


# ------------------------------------------------------------ the hand example
HAND = dict(V=np.array([[0.5, -0.3], [-0.4, 0.8]]), c=np.array([0.1, 0.2]),
            w=np.array([0.7, -0.6]), b=0.1, x=np.array([1.0, 0.0]), y=1.0)


def hand_forward(V, c, w, b, x=HAND["x"], y=HAND["y"]):
    u = V @ x + c
    h = sigma(u)
    z = float(w @ h + b)
    yhat = sigma(z)
    L = -(y * np.log(yhat) + (1 - y) * np.log(1 - yhat))
    return dict(u=u, h=h, z=z, yhat=yhat, L=L)


def hand_backward(V, c, w, b, x=HAND["x"], y=HAND["y"]):
    f = hand_forward(V, c, w, b, x, y)
    delta = f["yhat"] - y                 # dL/dz
    gh = delta * w                        # dL/dh_j
    dj = gh * f["h"] * (1 - f["h"])       # dL/du_j
    return dict(f, delta=delta, gw=delta * f["h"], gb=delta, gh=gh, dj=dj,
                gV=np.outer(dj, x), gc=dj)


# ------------------------------------------------------------------------- XOR
XOR_X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
XOR_Y = np.array([0, 1, 1, 0])


@lru_cache(maxsize=None)
def xor_run(seed, H=2, steps=5000):
    """Returns (params, loss per step, outputs per step)."""
    L, out = [], []

    def watch(step, V, c, w, b, yhat):
        L.append(loss(XOR_Y, yhat))
        out.append(yhat.copy())

    p = train(XOR_X, XOR_Y, H, seed=seed, steps=steps, watch=watch)
    return p, np.array(L), np.array(out)


def xor_survey(H=2, steps=5000, seeds=range(100)):
    """Final loss of each seed, after the last update."""
    return np.array([loss(XOR_Y, predict(train(XOR_X, XOR_Y, H, seed=s, steps=steps), XOR_X))
                     for s in seeds])


# --------------------------------------------------------- the two-class file
@lru_cache(maxsize=None)
def two_class():
    """The file, the split (seed 0) and the inputs scaled with the training rows."""
    d = np.loadtxt(DATA / "ml_two_class.csv", delimiter=",", skiprows=1)
    X, y = d[:, :2], d[:, 2]
    idx = np.random.default_rng(0).permutation(len(y))
    tr, va, te = idx[:360], idx[360:480], idx[480:]
    mu, sd = X[tr].mean(axis=0), X[tr].std(axis=0)
    return dict(X=X, y=y, idx=idx, tr=tr, va=va, te=te, mu=mu, sd=sd, Z=(X - mu) / sd)


@lru_cache(maxsize=None)
def two_class_net(H, seed=0):
    t = two_class()
    return train(t["Z"][t["tr"]], t["y"][t["tr"]], H, seed=seed)


@lru_cache(maxsize=None)
def two_class_neuron():
    t = two_class()
    return train_neuron(t["Z"][t["tr"]], t["y"][t["tr"]])


def confusion(y, score, cut=0.5):
    pred = score > cut
    return (int(np.sum(pred & (y == 1))), int(np.sum(pred & (y == 0))),
            int(np.sum(~pred & (y == 1))), int(np.sum(~pred & (y == 0))))   # TP FP FN TN


def auc_pairs(y, score):
    """Share of (class 1, class 0) pairs in which the class-1 row scores higher."""
    s1, s0 = score[y == 1], score[y == 0]
    return float((s1[:, None] > s0[None, :]).mean())


def roc_points(y, score):
    cuts = np.r_[np.inf, np.sort(score)[::-1], -np.inf]
    tpr = np.array([(score[y == 1] >= t).mean() for t in cuts])
    fpr = np.array([(score[y == 0] >= t).mean() for t in cuts])
    return fpr, tpr


def cross_validation(H=4, k=5):
    """k folds over the 480 rows that are not the test set."""
    t = two_class()
    folds = np.array_split(t["idx"][:480], k)
    acc = []
    for i in range(k):
        held = folds[i]
        rest = np.concatenate([folds[j] for j in range(k) if j != i])
        mu, sd = t["X"][rest].mean(axis=0), t["X"][rest].std(axis=0)
        p = train((t["X"][rest] - mu) / sd, t["y"][rest], H)
        acc.append(np.mean((predict(p, (t["X"][held] - mu) / sd) > 0.5) == t["y"][held]))
    return np.array(acc)


@lru_cache(maxsize=None)
def overfit_run(n=60, H=20, steps=30000):
    """A large network on the first n training rows. Returns the loss curves,
    the parameters at the validation minimum and at the end."""
    t = two_class()
    small = t["tr"][:n]
    mu, sd = t["X"][small].mean(axis=0), t["X"][small].std(axis=0)
    Z = (t["X"] - mu) / sd
    Xs, ys, Xv, yv = Z[small], t["y"][small], Z[t["va"]], t["y"][t["va"]]
    curve, best = [], {}

    def watch(step, V, c, w, b, yhat):
        lv = loss(yv, predict((V, c, w, b), Xv))
        curve.append((loss(ys, yhat), lv))
        if not best or lv < best["lv"]:
            best.update(lv=lv, step=step, p=(V.copy(), c.copy(), w.copy(), float(b)))

    p = train(Xs, ys, H, steps=steps, watch=watch)
    acc = lambda q, X, y: float(np.mean((predict(q, X) > 0.5) == y))
    return dict(curve=np.array(curve), best=best, p=p, Xs=Xs, ys=ys, Xv=Xv, yv=yv,
                end=(loss(ys, predict(p, Xs)), loss(yv, predict(p, Xv)),
                     acc(p, Xs, ys), acc(p, Xv, yv)),
                at_best=(acc(best["p"], Xs, ys), acc(best["p"], Xv, yv)))


# ------------------------------------------------------- leakage, LHCb file
def leakage(steps=5000):
    """Label: M inside 1845-1885 MeV. Inputs: log PT, log TAU, log IPCHI2,
    then the same with M added. Returns accuracies on the 20 % test rows."""
    d = np.loadtxt(DATA / "D0_KPi.csv", delimiter=",", skiprows=1)
    n_all = len(d)
    d = d[d[:, 2] > 0]                      # TAU > 0: drops -100 and three more
    M, PT, TAU, IP = d.T
    y = ((M > 1845) & (M < 1885)).astype(float)
    idx = np.random.default_rng(0).permutation(len(y))
    n_tr = int(0.8 * len(y))
    tr, te = idx[:n_tr], idx[n_tr:]
    out = dict(n_all=n_all, n=len(y), n1=int(y.sum()), n_tr=len(tr), n_te=len(te),
               majority=float(max(y[te].mean(), 1 - y[te].mean())))
    logs = np.column_stack([np.log(PT), np.log(TAU), np.log(IP)])
    for name, F in (("without M", logs), ("with M", np.column_stack([logs, M]))):
        mu, sd = F[tr].mean(axis=0), F[tr].std(axis=0)
        Z = (F - mu) / sd
        w, b = train_neuron(Z[tr], y[tr], steps=2000)
        p = train(Z[tr], y[tr], 4, steps=steps)
        s = predict(p, Z[te])
        out[name] = dict(neuron_w=w, neuron_b=b,
                         neuron_acc=float(np.mean((sigma(Z[te] @ w + b) > 0.5) == y[te])),
                         net_acc=float(np.mean((s > 0.5) == y[te])),
                         Ztr=Z[tr], ytr=y[tr], Zte=Z[te], yte=y[te])
    return out


# -------------------------------------------------------------------- k-means
KM_POINTS = np.array([[1, 3], [2, 1], [3, 2], [6, 8], [5, 8], [4, 5]], float)   # A..F


def kmeans_steps(P, c, iters=3):
    """One (squared distances, labels, new centres, J) per iteration."""
    c = np.array(c, float)
    out = []
    for _ in range(iters):
        d2 = ((P[:, None, :] - c[None]) ** 2).sum(axis=2)
        lab = d2.argmin(axis=1)
        c = np.array([P[lab == k].mean(axis=0) for k in range(len(c))])
        J = float(sum(((P[lab == k] - c[k]) ** 2).sum() for k in range(len(c))))
        out.append((d2, lab, c.copy(), J))
    return out


# ------------------------------------------------- a language model by hand
LM_TEXT = """the kaon has a mass of 494 MeV .
the pion has a mass of 140 MeV .
the D0 has a mass of 1865 MeV .
the pendulum has a length of 60 cm ."""


def lm_follow():
    words = LM_TEXT.split()
    follow = {}
    for a, b in zip(words, words[1:]):
        follow.setdefault(a, []).append(b)
    return follow


def lm_generate(rng, follow):
    w, out = "the", ["the"]
    while w != ".":
        w = str(rng.choice(follow[w]))
        out.append(w)
    return " ".join(out)


def numbers():
    np.set_printoptions(precision=4, suppress=True)
    P = lambda *a: print(*a)

    P("== parameters")
    for s in ((2, 2, 1), (2, 3, 1), (2, 4, 1), (2, 20, 1), (3, 4, 1), (784, 100, 10)):
        P("  ", s, n_parameters(*s))

    P("== hand example: x = (1, 0), y = 1")
    g = hand_backward(HAND["V"], HAND["c"], HAND["w"], HAND["b"])
    for k in ("u", "h", "z", "yhat", "L", "delta", "gw", "gb", "gh", "dj", "gV", "gc"):
        P("  ", k, np.round(g[k], 4))
    P("   h(1-h)", np.round(g["h"] * (1 - g["h"]), 4))
    P("   without the sigmoid: w V =", HAND["w"] @ HAND["V"],
      " w.c + b =", round(float(HAND["w"] @ HAND["c"] + HAND["b"]), 4))
    eps = 0.001
    for name, (arr, i) in dict(v11=("V", (0, 0)), w2=("w", 1), c2=("c", 1)).items():
        up = {k: np.array(v, float) for k, v in HAND.items() if k in "Vcw"}
        dn = {k: np.array(v, float) for k, v in HAND.items() if k in "Vcw"}
        up[arr][i] += eps
        dn[arr][i] -= eps
        Lp = hand_forward(up["V"], up["c"], up["w"], HAND["b"])["L"]
        Lm = hand_forward(dn["V"], dn["c"], dn["w"], HAND["b"])["L"]
        P(f"   nudge {name}: L+ {Lp:.7f}  L- {Lm:.7f}  slope {(Lp - Lm) / (2 * eps):.5f}")
    eta = 1.0
    new = dict(V=HAND["V"] - eta * g["gV"], c=HAND["c"] - eta * g["gc"],
               w=HAND["w"] - eta * g["gw"], b=HAND["b"] - eta * g["gb"])
    f2 = hand_forward(**new)
    P("   after one step, eta = 1:", {k: np.round(v, 4) for k, v in new.items()})
    P("   yhat", round(float(f2["yhat"]), 4), "L", round(float(f2["L"]), 4))
    P("   chain rule: (3x+1)^2 at 1 and 1.001:", 16, (3 * 1.001 + 1) ** 2)

    P("== XOR, 2-2-1, eta = 1, 5000 steps")
    for s in (0, 1, 2, 4):
        p, L, out = xor_run(s)
        P(f"   seed {s}: loss at steps 0, 100, 300, 500, 1000, 4999:",
          np.round(L[[0, 100, 300, 500, 1000, 4999]], 4), " outputs", np.round(out[-1], 3))
        P("      V", np.round(p[0], 2).tolist(), "c", np.round(p[1], 2), "w", np.round(p[2], 2),
          "b", round(float(p[3]), 2))
        P("      h", np.round(hidden(p, XOR_X), 3).tolist())
    P("   seed 0: first step with loss < 0.1:", int(np.argmax(xor_run(0)[1] < 0.1)))
    for H, steps in ((2, 5000), (2, 20000), (3, 5000), (4, 5000)):
        Ls = xor_survey(H, steps)
        P(f"   2-{H}-1, {steps} steps, seeds 0-99: loss < 0.01: {(Ls < 0.01).sum()},"
          f" near 0.347: {((Ls > 0.33) & (Ls < 0.36)).sum()}, near 0.478: {((Ls > 0.46) & (Ls < 0.50)).sum()}")
        if (H, steps) == (2, 5000):
            P("      seeds 0-9 that fail:", [s for s in range(10) if Ls[s] > 0.01])
    P("   (ln 2)/2 =", round(np.log(2) / 2, 4), " [2 ln(3/2) + ln 3]/4 =",
      round((2 * np.log(1.5) + np.log(3)) / 4, 4))
    same = train(XOR_X, XOR_Y, 2, init=(np.full((2, 2), 0.5), np.zeros(2), np.full(2, 0.5), 0.0))
    P("   all weights 0.5 at the start: loss", round(loss(XOR_Y, predict(same, XOR_X)), 4),
      "outputs", np.round(predict(same, XOR_X), 3), "V", np.round(same[0], 3).tolist())
    zero = train(XOR_X, XOR_Y, 2, init=(np.zeros((2, 2)), np.zeros(2), np.zeros(2), 0.0))
    P("   all weights 0 at the start: loss", round(loss(XOR_Y, predict(zero, XOR_X)), 4),
      "outputs", np.round(predict(zero, XOR_X), 3))

    P("== two-class file")
    t = two_class()
    X, y, Z, tr, va, te = (t[k] for k in ("X", "y", "Z", "tr", "va", "te"))
    P("   rows", len(y), "class 1", int(y.sum()), " mu", np.round(t["mu"], 3), "sd", np.round(t["sd"], 3))
    P("   class 1 in train, validation, test:", int(y[tr].sum()), int(y[va].sum()), int(y[te].sum()))
    w, b = two_class_neuron()
    acc = lambda s, rows: float(np.mean((s > 0.5) == y[rows]))
    P("   neuron: w", np.round(w, 3), "b", round(float(b), 3), "loss", round(loss(y[tr], sigma(Z[tr] @ w + b)), 4),
      "accuracy train", round(acc(sigma(Z[tr] @ w + b), tr), 3), "validation", round(acc(sigma(Z[va] @ w + b), va), 3))
    for H in (1, 2, 3, 4, 8, 16):
        p = two_class_net(H)
        P(f"   H = {H:2d} ({n_parameters(2, H, 1):2d} parameters): loss train {loss(y[tr], predict(p, Z[tr])):.3f}"
          f" validation {loss(y[va], predict(p, Z[va])):.3f}   accuracy train {acc(predict(p, Z[tr]), tr):.3f}"
          f" validation {acc(predict(p, Z[va]), va):.3f}")
    raw = train(X[tr], y[tr], 4)
    P("   H = 4 without scaling: accuracy train", round(acc(predict(raw, X[tr]), tr), 3))
    p = two_class_net(4)
    s = predict(p, Z[te])
    TP, FP, FN, TN = confusion(y[te], s)
    P("   H = 4 on the test rows: TP FP FN TN", TP, FP, FN, TN, " accuracy", (TP + TN) / 120,
      "precision", round(TP / (TP + FP), 4), "recall", round(TP / (TP + FN), 4),
      "FPR", round(FP / (FP + TN), 4))
    P("   validation rows right:", int(round(acc(predict(p, Z[va]), va) * 120)),
      " binomial sigma at 0.95, N = 120:", round(np.sqrt(0.95 * 0.05 / 120), 4))
    for cut in (0.1, 0.5, 0.9):
        a, f, m, n = confusion(y[te], s, cut)
        P(f"   cut {cut}: TP {a} FP {f} FN {m} TN {n}  precision {a / (a + f):.3f} recall {a / (a + m):.3f}"
          f" FPR {f / (f + n):.3f} accuracy {(a + n) / 120:.3f}")
    n1, n0 = int(y[te].sum()), int((1 - y[te]).sum())
    P("   AUC: pairs", n1 * n0, "in order", int(round(auc_pairs(y[te], s) * n1 * n0)),
      "AUC", round(auc_pairs(y[te], s), 4))
    P("   AUC neuron", round(auc_pairs(y[te], sigma(Z[te] @ w + b)), 4),
      " H = 2", round(auc_pairs(y[te], predict(two_class_net(2), Z[te])), 4),
      " accuracy on test: neuron", round(acc(sigma(Z[te] @ w + b), te), 3),
      "H = 2", round(acc(predict(two_class_net(2), Z[te]), te), 3))
    cv = cross_validation()
    P("   5 folds of 96:", np.round(cv, 3), "mean", round(cv.mean(), 4), "std", round(cv.std(ddof=1), 4))
    o = overfit_run()
    P("   overfit, 60 rows, H = 20, 30000 steps: validation minimum", round(o["best"]["lv"], 4),
      "at step", o["best"]["step"], "accuracy train, validation there", np.round(o["at_best"], 3))
    P("      at the end: loss train, validation, accuracy train, validation", np.round(o["end"], 4))

    P("== ROC by hand")
    s1, s0 = np.array([0.9, 0.8, 0.6, 0.4]), np.array([0.7, 0.3, 0.2, 0.1])
    P("   pairs in order", int((s1[:, None] > s0[None]).sum()), "of 16")
    P("== rare class: 100 of 100 000, recall 0.90, FPR 0.01")
    P("   TP 90, FP", 0.01 * 99900, "precision", round(90 / (90 + 999), 4),
      "accuracy", (90 + 99900 - 999) / 100000, "always 0:", 99900 / 100000)
    P("== k-means by hand, centres start on A and B")
    for i, (d2, lab, c, J) in enumerate(kmeans_steps(KM_POINTS, KM_POINTS[[0, 1]]), 1):
        P(f"   iteration {i}: d2 {d2.tolist()} groups {lab.tolist()} centres {c.tolist()} J {J}")
    import itertools
    Js = [kmeans_steps(KM_POINTS, KM_POINTS[[i, j]], 10)[-1][3] for i, j in itertools.combinations(range(6), 2)]
    P("   J at the end for the 15 pairs of starting points:", sorted(Js))
    P("== language model by hand")
    follow = lm_follow()
    P("   after 'the':", follow["the"], " after 'a':", follow["a"], " after 'of':", follow["of"])
    rng = np.random.default_rng(0)
    for _ in range(5):
        P("   ", lm_generate(rng, follow))
    rng = np.random.default_rng(0)
    true = set(LM_TEXT.split("\n"))
    made = [lm_generate(rng, follow) for _ in range(10000)]
    P("   of 10 000 sentences (seed 0), in the text:", sum(m in true for m in made),
      " distinct:", len(set(made)), " expected share 10/64 =", 10 / 64)
    z = np.array([2.0, 1.0, 0.1])
    P("   softmax of", z, "=", np.round(np.exp(z) / np.exp(z).sum(), 4),
      " -ln p =", np.round(-np.log(np.exp(z) / np.exp(z).sum()), 3))

    P("== leakage, LHCb file (this takes about a minute)")
    lk = leakage()
    P("   rows", lk["n_all"], "kept", lk["n"], "label 1", lk["n1"], "train", lk["n_tr"], "test", lk["n_te"],
      "larger class in test", round(lk["majority"], 4))
    for name in ("without M", "with M"):
        r = lk[name]
        P(f"   {name}: neuron w {np.round(r['neuron_w'], 3)} b {r['neuron_b']:.3f}"
          f" accuracy {r['neuron_acc']:.4f}; network 4 hidden units accuracy {r['net_acc']:.4f}")

    try:
        import sklearn
        from sklearn.cluster import KMeans
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import (confusion_matrix, precision_score, recall_score,
                                     roc_auc_score)
        from sklearn.neural_network import MLPClassifier
    except ImportError:
        P("== scikit-learn not installed: checks skipped")
        return
    P("== checks against scikit-learn", sklearn.__version__)
    pred = (s > 0.5).astype(int)
    P("   confusion_matrix", confusion_matrix(y[te], pred).tolist(),
      "precision", round(precision_score(y[te], pred), 4), "recall", round(recall_score(y[te], pred), 4),
      "roc_auc", round(roc_auc_score(y[te], s), 4))
    r = lk["without M"]
    lr = LogisticRegression(penalty=None).fit(r["Ztr"], r["ytr"])
    P("   LogisticRegression on the LHCb inputs: w", np.round(lr.coef_[0], 3), "b", np.round(lr.intercept_, 3),
      "accuracy", round(lr.score(r["Zte"], r["yte"]), 4))
    for kw in (dict(), dict(solver="lbfgs")):
        m = MLPClassifier(hidden_layer_sizes=(4,), activation="logistic", random_state=0,
                          max_iter=5000, **kw).fit(Z[tr], y[tr])
        P("   MLPClassifier", kw or "defaults", "passes", m.n_iter_, "loss", round(float(m.loss_), 4),
          "test accuracy", round(m.score(Z[te], y[te]), 4),
          "confusion", confusion_matrix(y[te], m.predict(Z[te])).tolist())
    km = KMeans(n_clusters=2, init=KM_POINTS[[0, 1]], n_init=1).fit(KM_POINTS)
    P("   KMeans on the six points:", km.cluster_centers_.tolist(), "J", km.inertia_)


# =============================================================================
# Figures
# =============================================================================

def _points(ax, X, y, ms=3.2, alpha=0.9):
    ax.plot(*X[y == 0].T, "o", ms=ms, color=C0, alpha=alpha, mec="none", label="class 0")
    ax.plot(*X[y == 1].T, "o", ms=ms, color=C1, alpha=alpha, mec="none", label="class 1")


def _regions(ax, p, lim=2.9, n=220):
    g = np.linspace(-lim, lim, n)
    G = np.column_stack([a.ravel() for a in np.meshgrid(g, g)])
    S = predict(p, G).reshape(n, n)
    ax.contourf(g, g, S, levels=[0, 0.5, 1], colors=[C0, C1], alpha=0.16)
    ax.contour(g, g, S, levels=[0.5], colors=[style.FG], linewidths=1.4)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_box_aspect(1)
    ax.grid(False)


# -------------------------------------------------------------- the network
def _network():
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    ax.set_axis_off()
    ax.set_xlim(-0.9, 6.9)
    ax.set_ylim(-0.75, 3.1)
    pos = dict(x1=(0, 2.2), x2=(0, 0.3), h1=(2.9, 2.2), h2=(2.9, 0.3), y=(5.8, 1.25))
    col = dict(x1=style.DIM, x2=style.DIM, h1=style.CYCLE[1], h2=style.CYCLE[1], y=style.ACCENT)
    lab = dict(x1="$x_1$", x2="$x_2$", h1="$h_1$", h2="$h_2$", y=r"$\hat{y}$")
    edges = [("x1", "h1", "$v_{11}$", 0.36, 0.0, 0.19), ("x2", "h1", "$v_{12}$", 0.30, -0.33, 0.1),
             ("x1", "h2", "$v_{21}$", 0.30, -0.33, -0.1), ("x2", "h2", "$v_{22}$", 0.36, 0.0, -0.21),
             ("h1", "y", "$w_1$", 0.45, 0.0, 0.22), ("h2", "y", "$w_2$", 0.45, 0.0, -0.24)]
    for a, b, text, t, dx, dy in edges:
        (xa, ya), (xb, yb) = pos[a], pos[b]
        ax.add_patch(FancyArrowPatch((xa, ya), (xb, yb), arrowstyle="-|>", mutation_scale=13,
                                     shrinkA=19, shrinkB=19, color=style.DIM, lw=1.3))
        ax.text(xa + t * (xb - xa) + dx, ya + t * (yb - ya) + dy, text, fontsize=14, color=style.FG,
                ha="center", va="center")
    for k, (x, y) in pos.items():
        ax.add_patch(Circle((x, y), 0.36, fc=BG, ec=col[k], lw=2.2, zorder=3))
        ax.text(x, y, lab[k], fontsize=16, color=style.FG, ha="center", va="center", zorder=4)
    for k, text in (("h1", "$+\\,c_1$"), ("h2", "$+\\,c_2$"), ("y", "$+\\,b$")):
        x, y = pos[k]
        ax.text(x, y - 0.62, text, fontsize=13, color=style.FG, ha="center", va="center")
    for x, text, c in ((0, "inputs", style.DIM), (2.9, "hidden layer", style.CYCLE[1]),
                       (5.8, "output", style.ACCENT)):
        ax.text(x, 2.95, text, fontsize=12, color=c, ha="center", va="center")
    style.save(fig, "viz_ml_network")


# --------------------------------------- XOR: what the trained network holds
def _xor_learned():
    p, L, out = xor_run(0)
    V, c, w, b = p
    cols = [C1 if t else C0 for t in XOR_Y]
    unit_cols = (style.CYCLE[3], style.CYCLE[2])
    fig, (a0, a1) = plt.subplots(1, 2, figsize=(7.6, 3.5))
    g = np.linspace(-0.4, 1.4, 200)
    G = np.column_stack([m.ravel() for m in np.meshgrid(g, g)])
    a0.contourf(g, g, predict(p, G).reshape(200, 200), levels=[0.5, 1], colors=[C1], alpha=0.16)
    for j in range(2):
        a0.plot(g, -(V[j, 0] * g + c[j]) / V[j, 1], color=unit_cols[j], lw=1.8)
        s = -c[j] / V[j, 0]
        x0 = (-0.3, 0.42)[j == 0]
        a0.text(x0, s - x0 + 0.05, f"$u_{j + 1} = 0$: $x_1 + x_2 = {s:.2f}$", color=unit_cols[j],
                fontsize=10, rotation=-45, rotation_mode="anchor", ha="left", va="bottom")
    for (x1, x2), col in zip(XOR_X, cols):
        a0.plot(x1, x2, "o", ms=13, color=col, mec=BG, mew=1.5, zorder=4)
    a0.set_xlabel("$x_1$")
    a0.set_ylabel("$x_2$")
    a0.set_title("The two hidden units, as lines", fontsize=12)
    H = hidden(p, XOR_X)
    a1.plot(g, -(w[0] * g + b) / w[1], color=style.FG, lw=1.8)
    a1.text(0.0, 0.5, "$z = 0$", color=style.FG, fontsize=10.5, rotation=46.6,
            rotation_mode="anchor", ha="left", va="bottom")
    for (x1, x2), (h1, h2), col in zip(XOR_X, H, cols):
        a1.plot(h1, h2, "o", ms=13, color=col, mec=BG, mew=1.5, zorder=4)
    a1.text(H[0, 0] + 0.1, H[0, 1], "(0, 0)", fontsize=10, color=style.FG, va="center")
    a1.text(H[1, 0] + 0.1, H[1, 1] + 0.02, "(0, 1) and (1, 0)", fontsize=10, color=style.FG, va="center")
    a1.text(H[3, 0], H[3, 1] + 0.14, "(1, 1)", fontsize=10, color=style.FG, ha="center")
    a1.set_xlabel("$h_1$")
    a1.set_ylabel("$h_2$")
    a1.set_title("The four points after the hidden layer", fontsize=12)
    for ax in (a0, a1):
        ax.set_xlim(-0.4, 1.4)
        ax.set_ylim(-0.4, 1.4)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_box_aspect(1)
    a0.plot([], [], "o", color=C1, label="XOR = 1")
    a0.plot([], [], "o", color=C0, label="XOR = 0")
    a0.legend(loc="upper right", fontsize=9, handletextpad=0.2, borderaxespad=0.1)
    style.save(fig, "viz_ml_xor_learned")


# ------------------------------------------------- the backward pass, numbers
def _backprop(stage=None):
    """The chain of the hand example with its forward values (above the
    circles) and the derivatives of L (below). stage 1..4 draws the state
    after that step of the derivation; None draws the whole pass."""
    g = hand_backward(HAND["V"], HAND["c"], HAND["w"], HAND["b"])
    full = stage is None
    upto = 4 if full else stage
    fig, ax = plt.subplots(figsize=(10.4, 3.0 if full else 2.45))
    ax.set_axis_off()
    ax.set_xlim(-0.9, 10.6)
    ax.set_ylim(-1.5 if full else -1.3, 2.85 if full else 2.45)
    fwd, bwd = style.ACCENT, style.CYCLE[1]
    # name: (position, symbol, forward value, derivative of L, step that finds it)
    nodes = {
        "x": ((0, 0.65), "$x = (1,\\ 0)$", None, None, 0),
        "u1": ((2.2, 1.6), "$u_1$", f"{g['u'][0]:.3f}", f"{g['dj'][0]:+.4f}", 3),
        "u2": ((2.2, -0.3), "$u_2$", f"{g['u'][1]:.3f}", f"{g['dj'][1]:+.4f}", 3),
        "h1": ((4.4, 1.6), "$h_1$", f"{g['h'][0]:.3f}", f"{g['gh'][0]:+.3f}", 2),
        "h2": ((4.4, -0.3), "$h_2$", f"{g['h'][1]:.3f}", f"{g['gh'][1]:+.3f}", 2),
        "z": ((6.6, 0.65), "$z$", f"{g['z']:.3f}", f"{g['delta']:+.3f}", 1),
        "y": ((8.4, 0.65), "$\\hat{y}$", f"{g['yhat']:.3f}", None, 0),
        "L": ((10.0, 0.65), "$L$", f"{g['L']:.3f}", None, 0),
    }
    # from, to, parameters on the edge, offset of the label, their derivatives, step
    edges = [("x", "u1", "$v_{11}, v_{12}, c_1$", 0.34,
              f"{g['gV'][0, 0]:+.4f},  0,  {g['gc'][0]:+.4f}", 4),
             ("x", "u2", "$v_{21}, v_{22}, c_2$", -0.36,
              f"{g['gV'][1, 0]:+.4f},  0,  {g['gc'][1]:+.4f}", 4),
             ("u1", "h1", "$\\sigma$", 0.2, None, 0), ("u2", "h2", "$\\sigma$", 0.2, None, 0),
             ("h1", "z", "$w_1$", 0.3, f"{g['gw'][0]:+.3f}", 1),
             ("h2", "z", "$w_2,\\ b$", -0.34, f"{g['gw'][1]:+.3f},  {g['gb']:+.3f}", 1),
             ("z", "y", "$\\sigma$", 0.2, None, 0), ("y", "L", "", 0, None, 0)]
    for a, b, text, dy, grad, step in edges:
        (xa, ya), (xb, yb) = nodes[a][0], nodes[b][0]
        ax.add_patch(FancyArrowPatch((xa, ya), (xb, yb), arrowstyle="-|>", mutation_scale=12,
                                     shrinkA=24 if a == "x" else 17, shrinkB=17, color=style.DIM, lw=1.2))
        xm = (xa + xb) / 2 - (0.22 if a == "x" else 0)
        ax.text(xm, (ya + yb) / 2 + dy, text, fontsize=11, color=style.DIM,
                ha="center", va="center")
        if grad and not full and step <= upto:
            ax.text(xm, (ya + yb) / 2 + dy + (0.3 if dy > 0 else -0.3), grad, fontsize=10.5,
                    color=bwd, ha="center", va="center", fontweight="bold" if step == stage else None)
    for k, ((x, y), text, f, bk, step) in nodes.items():
        if k == "x":
            ax.text(x, y, text, fontsize=12.5, color=style.FG, ha="center", va="center")
            continue
        now = step == stage
        ax.add_patch(Circle((x, y), 0.33, fc=BG, ec=bwd if now else style.DIM, lw=2.2 if now else 1.6,
                            zorder=3))
        ax.text(x, y, text, fontsize=13.5, color=style.FG, ha="center", va="center", zorder=4)
        ax.text(x, y + 0.6, f, fontsize=12, color=fwd, ha="center", va="center")
        if bk and step <= upto:
            ax.text(x, y - 0.62, bk, fontsize=12, color=bwd, ha="center", va="center",
                    fontweight="bold" if now else None)
    ax.text(10.0, 0.03, "$y = 1$", fontsize=11, color=style.DIM, ha="center", va="center")
    if full:
        ax.annotate("", xy=(9.6, 2.6), xytext=(1.0, 2.6),
                    arrowprops=dict(arrowstyle="-|>", color=fwd, lw=1.6))
        ax.text(5.3, 2.6, "forward: the values", fontsize=11.5, color=fwd, ha="center", va="center",
                bbox=dict(fc=BG, ec="none", pad=3))
        ax.annotate("", xy=(1.0, -1.3), xytext=(7.4, -1.3),
                    arrowprops=dict(arrowstyle="-|>", color=bwd, lw=1.6))
        ax.text(4.2, -1.3, "backward: the derivatives of $L$", fontsize=11.5, color=bwd, ha="center",
                va="center", bbox=dict(fc=BG, ec="none", pad=3))
    style.save(fig, "viz_ml_backprop" if full else f"viz_ml_backprop_step{stage}")


# -------------------------------------------------------- XOR: one training run
def _xor_training():
    p, L, out = xor_run(0)
    n = 1500
    fig, (a0, a1) = plt.subplots(1, 2, figsize=(9.4, 3.1))
    a0.plot(np.arange(n), L[:n], color=style.ACCENT, lw=2.2)
    a0.axhline(np.log(2), color=style.DIM, lw=1, ls="--")
    a0.text(n * 0.98, np.log(2) + 0.015, "ln 2 = 0.693: every output 0.5", fontsize=9.5,
            color=style.DIM, ha="right", va="bottom")
    a0.set_xlabel("epoch")
    a0.set_ylabel("loss $L$")
    a0.set_ylim(0, 0.8)
    a0.set_xlim(0, n)
    a0.set_title("The loss, seed 0", fontsize=12)
    cols = [C0, C1, style.CYCLE[2], style.CYCLE[3]]
    for i, ((x1, x2), t) in enumerate(zip(XOR_X, XOR_Y)):
        a1.plot(np.arange(n), out[:n, i], color=cols[i], lw=2,
                ls="-" if i in (0, 1) else "--", label=f"({x1}, {x2}), $y$ = {t}")
    a1.set_xlabel("epoch")
    a1.set_ylabel(r"output $\hat{y}$")
    a1.set_ylim(-0.03, 1.03)
    a1.set_xlim(0, n)
    a1.set_title("The four outputs", fontsize=12)
    a1.legend(loc="center right", fontsize=9.5)
    style.save(fig, "viz_ml_xor_training")


# ------------------------------------------------------------ XOR: ten seeds
def _xor_seeds():
    n = 3000
    fig, ax = plt.subplots(figsize=(8.2, 3.2))
    stuck = {}
    for s in range(10):
        L = xor_run(s)[1]
        bad = L[-1] > 0.01
        ax.plot(np.arange(n), L[:n], color=style.BAD if bad else style.ACCENT,
                lw=1.9 if bad else 1.4, alpha=1 if bad else 0.75)
        if bad:
            stuck.setdefault(round(float(L[-1]), 2), []).append(s)
    for level, seeds in stuck.items():
        ax.text(n * 1.01, level, ("seeds " if len(seeds) > 1 else "seed ") + ", ".join(map(str, seeds)),
                fontsize=9.5, color=style.BAD, va="center", ha="left")
    ax.set_xlim(0, n)
    ax.set_ylim(0, 0.9)
    ax.set_xlabel("epoch")
    ax.set_ylabel("loss $L$")
    ax.plot([], [], color=style.ACCENT, label="7 seeds reach a loss below 0.01")
    ax.plot([], [], color=style.BAD, label="3 seeds stay near 0.35 or 0.48")
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title("The same network and data, seeds 0 to 9", fontsize=12)
    style.save(fig, "viz_ml_xor_seeds")


# ------------------------------------------------------ the two-class file
def _two_class_fig():
    t = two_class()
    X, y = t["X"], t["y"]
    fig, ax = plt.subplots(figsize=(4.4, 3.9))
    _points(ax, X, y, ms=3.6)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_box_aspect(1)
    ax.legend(loc="upper right", fontsize=9, handletextpad=0.1, borderaxespad=0.1,
              frameon=True, facecolor=BG, edgecolor="none", framealpha=0.8)
    ax.set_title("ml_two_class.csv, 600 rows", fontsize=12)
    style.save(fig, "viz_ml_two_class")


def _hidden_units():
    t = two_class()
    Z, y, tr, va = t["Z"], t["y"], t["tr"], t["va"]
    fig, axes = plt.subplots(1, 4, figsize=(11.6, 3.35))
    for ax, H in zip(axes, (1, 2, 3, 4)):
        p = two_class_net(H)
        _regions(ax, p)
        _points(ax, Z[tr], y[tr], ms=2.4, alpha=0.8)
        acc = np.mean((predict(p, Z[va]) > 0.5) == y[va])
        ax.set_title(f"{H} hidden unit{'s' if H > 1 else ''}", fontsize=12)
        ax.set_xlabel(f"validation: loss {loss(y[va], predict(p, Z[va])):.3f}, accuracy {acc:.3f}",
                      fontsize=9.5, color=style.FG)
        ax.set_xticks([])
        ax.set_yticks([])
    style.save(fig, "viz_ml_hidden_units")


def _overfit_network():
    o = overfit_run()
    curve = o["curve"]
    steps = np.arange(1, len(curve) + 1)
    fig, (a0, a1) = plt.subplots(1, 2, figsize=(9.6, 3.4), gridspec_kw={"width_ratios": [1.5, 1]})
    a0.plot(steps, curve[:, 0], color=style.ACCENT, lw=2.2, label="60 training rows")
    a0.plot(steps, curve[:, 1], color=style.BAD, lw=2.2, label="120 validation rows")
    b = o["best"]
    a0.plot(b["step"] + 1, b["lv"], "o", ms=8, color=style.CYCLE[2], zorder=5)
    a0.annotate(f"lowest validation loss\n{b['lv']:.2f} after {b['step']} epochs", xy=(b["step"] + 1, b["lv"]),
                xytext=(6, 0.15), fontsize=9.5, color=style.CYCLE[2],
                arrowprops=dict(arrowstyle="-", color=style.CYCLE[2], lw=0.9))
    a0.set_xscale("log")
    a0.set_xlim(1, len(curve))
    a0.set_ylim(0, 1.7)
    a0.set_xlabel("epoch (log scale)")
    a0.set_ylabel("loss $L$")
    a0.legend(loc="upper center", fontsize=10)
    a0.set_title("20 hidden units, 81 parameters", fontsize=12)
    _regions(a1, o["p"])
    g = np.linspace(-2.9, 2.9, 220)
    G = np.column_stack([a.ravel() for a in np.meshgrid(g, g)])
    a1.contour(g, g, predict(b["p"], G).reshape(220, 220), levels=[0.5], colors=[style.CYCLE[2]],
               linewidths=1.4, linestyles="--")
    _points(a1, o["Xs"], o["ys"], ms=4.5)
    a1.set_xticks([])
    a1.set_yticks([])
    a1.set_title("Boundary after 30 000 epochs", fontsize=12)
    a1.set_xlabel(f"dashed: after {b['step']} epochs", fontsize=9.5, color=style.CYCLE[2])
    style.save(fig, "viz_ml_overfit_network")


# ------------------------------------------------------------------- ROC
def _roc_by_hand():
    s1, s0 = np.array([0.9, 0.8, 0.6, 0.4]), np.array([0.7, 0.3, 0.2, 0.1])
    cuts = np.sort(np.r_[s1, s0])[::-1]
    fpr = np.r_[0, [(s0 >= c).mean() for c in cuts]]
    tpr = np.r_[0, [(s1 >= c).mean() for c in cuts]]
    fig, ax = plt.subplots(figsize=(3.7, 3.5))
    ax.fill_between(fpr, tpr, step="post", color=style.ACCENT, alpha=0.18)
    ax.plot([0, 1], [0, 1], ls="--", lw=1.1, color=style.DIM)
    ax.plot(fpr, tpr, "-", color=style.ACCENT, lw=2.2)
    off = {0.9: (0.045, 0.0), 0.8: (0.04, 0.07), 0.7: (0.035, -0.075), 0.6: (0.045, 0.0),
           0.4: (0.035, -0.075), 0.3: (-0.045, -0.075), 0.2: (-0.045, -0.075), 0.1: (-0.09, -0.075)}
    for c, x, yv in zip(cuts, fpr[1:], tpr[1:]):
        ax.plot(x, yv, "o", ms=6.5, color=C1 if c in s1 else C0, mec=BG, mew=1, zorder=4)
        dx, dy = off[float(c)]
        ax.text(x + dx, yv + dy, f"{c:.1f}", fontsize=9.5, color=style.FG, va="center", ha="left")
    ax.text(0.7, 0.3, "area\n14/16 = 0.875", fontsize=11, color=style.FG, ha="center", va="center")
    ax.set_xlim(-0.04, 1.08)
    ax.set_ylim(-0.04, 1.08)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xlabel("false-positive rate")
    ax.set_ylabel("true-positive rate")
    ax.set_box_aspect(1)
    style.save(fig, "viz_ml_roc_by_hand")


def _roc_curve():
    t = two_class()
    Z, y, te = t["Z"], t["y"], t["te"]
    yt = y[te]
    s4 = predict(two_class_net(4), Z[te])
    s2 = predict(two_class_net(2), Z[te])
    w, b = two_class_neuron()
    sn = sigma(Z[te] @ w + b)
    cuts = (0.1, 0.5, 0.9)
    cut_cols = (style.CYCLE[5], style.CYCLE[2], style.CYCLE[3])
    fig, (a0, a1) = plt.subplots(1, 2, figsize=(9.2, 3.4), gridspec_kw={"width_ratios": [1.3, 1]})
    bins = np.linspace(0, 1, 21)
    a0.hist(s4[yt == 0], bins=bins, color=C0, alpha=0.75, label="class 0 (63 rows)")
    a0.hist(s4[yt == 1], bins=bins, color=C1, alpha=0.7, label="class 1 (57 rows)")
    for c, col in zip(cuts, cut_cols):
        a0.axvline(c, color=col, lw=1.8, ls="--")
        a0.text(c + (-0.012 if c > 0.8 else 0.012), 0.97, f"cut {c}", color=col, fontsize=10, va="top",
                ha="right" if c > 0.8 else "left", transform=a0.get_xaxis_transform())
    a0.set_xlabel(r"output $\hat{y}$ of the 2-4-1 network, test rows")
    a0.set_ylabel("rows")
    a0.legend(loc="upper center", fontsize=9.5, bbox_to_anchor=(0.7, 0.86))
    a0.set_title("The scores of the two classes", fontsize=12)
    a1.plot([0, 1], [0, 1], ls="--", lw=1.1, color=style.DIM)
    for s, col, name in ((sn, style.DIM, "one neuron"), (s2, style.CYCLE[4], "2 hidden units"),
                         (s4, style.ACCENT, "4 hidden units")):
        fpr, tpr = roc_points(yt, s)
        a1.plot(fpr, tpr, color=col, lw=2.2 if col == style.ACCENT else 1.7,
                label=f"{name}: {auc_pairs(yt, s):.3f}")
    for c, col in zip(cuts, cut_cols):
        TP, FP, FN, TN = confusion(yt, s4, c)
        a1.plot(FP / (FP + TN), TP / (TP + FN), "o", ms=7.5, color=col, mec=BG, mew=1, zorder=5)
    a1.set_xlim(-0.03, 1.03)
    a1.set_ylim(-0.03, 1.03)
    a1.set_xlabel("false-positive rate")
    a1.set_ylabel("true-positive rate")
    a1.set_box_aspect(1)
    a1.legend(loc="lower right", fontsize=9.5, title="area under the curve", title_fontsize=9.5,
              frameon=True, facecolor=BG, edgecolor="none", framealpha=0.85)
    a1.set_title("ROC on the test rows", fontsize=12)
    style.save(fig, "viz_ml_roc_curve")


# ------------------------------------------------------- cross-validation
def _cross_validation():
    acc = cross_validation()
    fig, ax = plt.subplots(figsize=(7.6, 2.5))
    ax.set_axis_off()
    ax.set_xlim(-1.4, 7.2)
    ax.set_ylim(-0.5, 5.75)
    for r in range(5):
        yy = 4 - r
        for k in range(5):
            held = k == r
            ax.add_patch(FancyBboxPatch((k + 0.04, yy + 0.12), 0.92, 0.72, boxstyle="round,pad=0,rounding_size=0.08",
                                        fc=style.BAD if held else style.ACCENT, ec="none",
                                        alpha=0.9 if held else 0.28))
            if held:
                ax.text(k + 0.5, yy + 0.48, "held out", fontsize=9.5, color=BG, ha="center", va="center")
        ax.text(-0.15, yy + 0.48, f"run {r + 1}", fontsize=10.5, color=style.FG, ha="right", va="center")
        ax.text(5.25, yy + 0.48, f"accuracy {acc[r]:.3f}", fontsize=10.5, color=style.FG, ha="left",
                va="center")
    ax.text(2.5, 5.45, "480 rows in 5 folds of 96; train on four, measure on the fifth", fontsize=10.5,
            color=style.DIM, ha="center", va="center")
    ax.text(5.25, -0.25, f"mean {acc.mean():.3f}, spread {acc.std(ddof=1):.3f}", fontsize=10.5,
            color=style.ACCENT, ha="left", va="center")
    style.save(fig, "viz_ml_cross_validation")


# ------------------------------------------------------------------ k-means
def _kmeans_by_hand():
    P = KM_POINTS
    its = kmeans_steps(P, P[[0, 1]], 2)
    cols = (style.ACCENT, style.CYCLE[1])
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.5), sharex=True, sharey=True)
    start = P[[0, 1]]
    panels = [("Start: centres on A and B", None, start, None),
              (f"After iteration 1: J = {its[0][3]:.0f}", its[0][1], its[0][2], start),
              (f"After iteration 2: J = {its[1][3]:.0f}", its[1][1], its[1][2], its[0][2])]
    for ax, (title, lab, c, old) in zip(axes, panels):
        for i, (x, y) in enumerate(P):
            col = style.DIM if lab is None else cols[lab[i]]
            ax.plot(x, y, "o", ms=11, color=col, mec=BG, mew=1.2, zorder=3)
            dx, dy = (-0.62, -0.1) if i == 1 else (0.28, 0.28)
            ax.text(x + dx, y + dy, "ABCDEF"[i], fontsize=11, color=style.FG, zorder=4)
        if old is not None:
            for k in range(2):
                ax.annotate("", xy=c[k], xytext=old[k], zorder=4,
                            arrowprops=dict(arrowstyle="-|>", color=cols[k], lw=1.3, ls="--",
                                            shrinkA=4, shrinkB=7))
        for k in range(2):
            ax.plot(*c[k], "X", ms=13, color=cols[k], mec=style.FG, mew=1.3, zorder=5)
        ax.set_title(title, fontsize=12)
        ax.set_xlim(0, 7.4)
        ax.set_ylim(0, 9.4)
        ax.set_xticks(range(0, 8))
        ax.set_yticks(range(0, 10))
        ax.set_box_aspect(9.4 / 7.4)
    style.save(fig, "viz_ml_kmeans_by_hand")


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
                            ("Two groups, k = 2: found",
                             "One group, k = 2: split in two")):
        lab, c = _kmeans(X, 2, rng)
        for j in range(2):
            ax.plot(*X[lab == j].T, "o", ms=4, color=cols[j], alpha=0.8)
        ax.plot(*c.T, "X", ms=13, color=style.FG, mec=BG, mew=1.2, zorder=5,
                label="centres")
        ax.set_title(title, fontsize=12)
        ax.set_xlabel("feature 1")
        ax.set_aspect("equal")
    axes[0].set_ylabel("feature 2")
    axes[0].legend(loc="upper left", fontsize=9)
    style.save(fig, "viz_ml_kmeans")


FIGURES = {
    "viz_ml_network": _network,
    "viz_ml_xor_learned": _xor_learned,
    "viz_ml_backprop_step1": lambda: _backprop(1),
    "viz_ml_backprop_step2": lambda: _backprop(2),
    "viz_ml_backprop_step3": lambda: _backprop(3),
    "viz_ml_backprop_step4": lambda: _backprop(4),
    "viz_ml_backprop": _backprop,
    "viz_ml_xor_training": _xor_training,
    "viz_ml_xor_seeds": _xor_seeds,
    "viz_ml_two_class": _two_class_fig,
    "viz_ml_hidden_units": _hidden_units,
    "viz_ml_overfit_network": _overfit_network,
    "viz_ml_roc_by_hand": _roc_by_hand,
    "viz_ml_roc_curve": _roc_curve,
    "viz_ml_cross_validation": _cross_validation,
    "viz_ml_kmeans_by_hand": _kmeans_by_hand,
    "viz_ml_kmeans": _kmeans_fig,
}

if __name__ == "__main__":
    numbers()
