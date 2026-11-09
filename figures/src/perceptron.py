"""Figures of Lecture 10: Classification and the Perceptron.

The question of the lecture: will it freeze tonight? Every number the slides
state is computed here, with plain Python on lists, as the seminar computes
it, from the weather log `lectures/workbook/docs/data/weather.csv`:

  * an evening is 18:00 of a day beside 06:00 of the next day; 3652 pairs,
    six of them touch the 120 hours of July 2019 marked -999, 3646 remain
    (`evenings`, the same function as `weather.evenings` in the seminar's
    start folder);
  * the inputs are x1, the temperature at 18:00 in °C, and x2, the humidity
    at 18:00 as a fraction (85 % is 0.85); the label y is 1 when 06:00 the
    next morning is below 0 °C (frost), else 0;
  * the training years are 2016 to 2022, the test years 2023 to 2025;
  * Rosenblatt's rule starts from zero weights, learning rate 1, and takes
    the evenings in the order of the log;
  * the logistic neuron is trained by the same update with the sigmoid in
    place of the step, evening by evening, learning rate 0.01, five passes
    over the training evenings, from zero;
  * the AND gate by Rosenblatt's rule: ten updates in six epochs.

Run directly to print every number the slides state:
    python figures/src/perceptron.py
Draw the figures:
    python figures/src/build.py --only perceptron

Three figures of the old Lecture 11 (the XOR network) are kept unchanged at
the end for Lecture 11, From Neurons to Language Models.
"""
import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

import style

PATH = style.ROOT / "lectures" / "workbook" / "docs" / "data" / "weather.csv"
MISSING = -999.0

C0 = style.CYCLE[1]      # no frost, class 0: orange circles
C1 = style.ACCENT        # frost, class 1: cyan triangles
LINE = style.FG
GREEN = style.CYCLE[2]
PINK = style.CYCLE[3]
VIOLET = style.CYCLE[4]

ETA = 0.01               # learning rate of the logistic neuron
EPOCHS = 5               # its passes over the training evenings
RULE_EPOCHS = 5          # Rosenblatt's rule in the seminar's class
THRESHOLD_NEURON = ([-1.0, 0.0], 3.8)   # "frost if x1 < 3.8 °C" as a neuron
TILTED_NEURON = ([-1.0, 4.0], 0.6)      # the same with a weight on humidity
TONIGHT = "2025-12-08"                  # the running example, a test evening
FOUR = ["2025-12-06", "2025-12-07", "2025-12-08", "2025-12-09"]


# ------------------------------------------------------------------ numbers
def evenings():
    """[date, temp, humidity, frost] for each evening: 18:00 of a day and
    06:00 of the next, as weather.evenings of the seminar's start folder."""
    lines = open(PATH).read().splitlines()[1:]
    rows = []
    for i in range(18, len(lines) - 12, 24):
        evening = lines[i].split(",")
        morning = lines[i + 12].split(",")
        assert evening[0][11:] == "18:00" and morning[0][11:] == "06:00"
        temp = float(evening[1])
        humidity = float(evening[2])
        morning_temp = float(morning[1])
        if temp == MISSING or morning_temp == MISSING:
            continue
        frost = 1 if morning_temp < 0 else 0
        rows.append([evening[0][0:10], temp, humidity, frost, morning_temp])
    return rows


def inputs(row):
    return [row[1], row[2] / 100]


def xs_ys(rows):
    return [inputs(r) for r in rows], [r[3] for r in rows]


def split(rows):
    train = [r for r in rows if int(r[0][0:4]) <= 2022]
    test = [r for r in rows if int(r[0][0:4]) >= 2023]
    return train, test


def z_of(x, w, b):
    return w[0] * x[0] + w[1] * x[1] + b


def says_frost(z):
    """z > 0, decided on z rounded to 9 decimals: an evening exactly on the
    line (z = 0 in exact arithmetic, a few 1e-16 in floating point, as
    29 Mar 2021 under w = (-1, 4), b = 0.6) is "no frost", as the slides and
    PerceptronPlayground count it."""
    return round(z, 9) > 0


def predict(x, w, b):
    """The neuron with a step: 1 (frost) when z > 0, else 0."""
    return 1 if says_frost(z_of(x, w, b)) else 0


def right(xs, ys, w, b):
    """How many evenings the neuron gets right."""
    count = 0
    for i in range(len(xs)):
        if predict(xs[i], w, b) == ys[i]:
            count = count + 1
    return count


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def evening_loss(x, y, w, b):
    """-ln P(y) of one evening, in a form that cannot overflow."""
    z = z_of(x, w, b)
    return max(z, 0.0) + math.log1p(math.exp(-abs(z))) - y * z


def mean_loss(xs, ys, w, b):
    return sum(evening_loss(xs[i], ys[i], w, b) for i in range(len(xs))) / len(xs)


def rosenblatt(xs, ys, epochs, w=(0.0, 0.0), b=0.0, eta=1.0):
    """Rosenblatt's rule, evening by evening, as the seminar's loop. Returns
    the state after each epoch: (w, b, updates in the epoch)."""
    w = list(w)
    history = []
    for _ in range(epochs):
        updates = 0
        for i in range(len(xs)):
            x = xs[i]
            error = ys[i] - predict(x, w, b)
            if error != 0:
                updates = updates + 1
            w[0] = w[0] + eta * error * x[0]
            w[1] = w[1] + eta * error * x[1]
            b = b + eta * error
        history.append((list(w), b, updates))
    return history


def rosenblatt_updates(xs, ys, epochs):
    """Each update of the rule: (index of the point, z before, w after, b after)."""
    w, b = [0.0, 0.0], 0.0
    out = []
    for _ in range(epochs):
        for i in range(len(xs)):
            x = xs[i]
            z = z_of(x, w, b)
            error = ys[i] - (1 if says_frost(z) else 0)
            if error != 0:
                w = [w[0] + error * x[0], w[1] + error * x[1]]
                b = b + error
                out.append((i, z, list(w), b))
    return out


def train_logistic(xs, ys, epochs=EPOCHS, eta=ETA):
    """The same update with the sigmoid in place of the step, evening by
    evening. Returns the state after each epoch, epoch 0 = the start."""
    w, b = [0.0, 0.0], 0.0
    history = [(list(w), b)]
    for _ in range(epochs):
        for i in range(len(xs)):
            x = xs[i]
            error = ys[i] - sigmoid(z_of(x, w, b))
            w[0] = w[0] + eta * error * x[0]
            w[1] = w[1] + eta * error * x[1]
            b = b + eta * error
        history.append((list(w), b))
    return history


def train_logistic_1(xs1, ys, epochs=EPOCHS, eta=ETA):
    """The same with one input, the temperature."""
    w, b = 0.0, 0.0
    for _ in range(epochs):
        for i in range(len(xs1)):
            error = ys[i] - sigmoid(w * xs1[i] + b)
            w = w + eta * error * xs1[i]
            b = b + eta * error
    return w, b


def plus_minus(p, n):
    """The standard error of a share p of n: sqrt(p (1 - p) / n)."""
    return math.sqrt(p * (1 - p) / n)


def lowest_w1_b(xs, ys):
    """The lowest point of the loss in w1 and b, with w2 = 0: Newton's method
    on the two numbers (the loss is a bowl, so it converges from the start)."""
    w1, b = -1.0, 3.8
    for _ in range(50):
        g1 = gb = h11 = h1b = hbb = 0.0
        for x, y in zip(xs, ys):
            p = sigmoid(w1 * x[0] + b)
            g1 += (p - y) * x[0]
            gb += p - y
            s = p * (1 - p)
            h11 += s * x[0] * x[0]
            h1b += s * x[0]
            hbb += s
        det = h11 * hbb - h1b * h1b
        w1 -= (hbb * g1 - h1b * gb) / det
        b -= (h11 * gb - h1b * g1) / det
    return w1, b


def nearest_rule(train_xs, train_ys, x):
    """Frost if the training evening nearest to x (in the plane of x1, x2) had frost."""
    best_d, best_y = None, None
    for xt, yt in zip(train_xs, train_ys):
        d = (xt[0] - x[0]) ** 2 + (xt[1] - x[1]) ** 2
        if best_d is None or d < best_d:
            best_d, best_y = d, yt
    return best_y


def calendar_rule(train_rows):
    """For each date (month and day), frost if most training years had frost."""
    counts = {}
    for r in train_rows:
        c = counts.setdefault(r[0][5:], [0, 0])
        c[r[3]] += 1
    return {d: 1 if c[1] > c[0] else 0 for d, c in counts.items()}


GATE = [[0, 0], [0, 1], [1, 0], [1, 1]]
AND = [0, 0, 0, 1]
OR = [0, 1, 1, 1]
XOR = [0, 1, 1, 0]


class Perceptron:
    """The class of the slide 'A Class: Perceptron', as the seminar builds it."""

    def __init__(self):
        self.w = [0.0, 0.0]
        self.b = 0.0

    def predict(self, x):
        z = self.w[0] * x[0] + self.w[1] * x[1] + self.b
        if says_frost(z):
            return 1
        return 0

    def fit(self, xs, ys, epochs):
        for epoch in range(epochs):
            for i in range(len(xs)):
                x = xs[i]
                error = ys[i] - self.predict(x)
                self.w[0] = self.w[0] + error * x[0]
                self.w[1] = self.w[1] + error * x[1]
                self.b = self.b + error


def _fmt(v, d=2):
    return f"{v:.{d}f}".replace("-", "−")


# ------------------------------------------------------------------ report
def report():
    rows = evenings()
    xs, ys = xs_ys(rows)
    train, test = split(rows)
    xtr, ytr = xs_ys(train)
    xte, yte = xs_ys(test)
    n, nf = len(rows), sum(ys)
    print("== The evenings")
    print(f"  evenings {n}, followed by frost {nf}, not {n - nf}, share {nf / n:.3f}")
    print(f"  pairs 3652, left out {3652 - n} (they touch the -999 hours of July 2019)")
    print(f"  training 2016-2022: {len(train)} evenings, frost {sum(ytr)}; "
          f"test 2023-2025: {len(test)}, frost {sum(yte)}")
    t18 = [r[1] for r in rows]
    print(f"  temperature at 18:00 from {min(t18)} to {max(t18)} °C; humidity from "
          f"{min(r[2] for r in rows):.0f} to {max(r[2] for r in rows):.0f} %")
    cold = [r for r in rows if r[3] == 0]
    warm = [r for r in rows if r[3] == 1]
    c = min(cold, key=lambda r: r[1])
    h = max(warm, key=lambda r: r[1])
    print(f"  coldest evening without frost: {c[0]} {c[1]} °C (06:00 {c[4]}); "
          f"warmest evening with frost: {h[0]} {h[1]} °C (06:00 {h[4]})")
    mid = [r for r in rows if 0 <= r[1] < 6]
    print(f"  evenings from 0 to 6 °C: {len(mid)}, of them frost {sum(r[3] for r in mid)}")
    print("  8 December, every year:")
    for r in rows:
        if r[0][5:] == "12-08":
            print(f"    {r[0]}  {r[1]:5.1f} °C  {r[2]:3.0f} %  06:00 {r[4]:5.1f}  frost {r[3]}")
    by_month = {}
    for r in rows:
        m = r[0][5:7]
        by_month.setdefault(m, [0, 0])
        by_month[m][0] += 1
        by_month[m][1] += r[3]
    print("  share of frost by month:",
          " ".join(f"{m}:{v[1] / v[0]:.2f}" for m, v in sorted(by_month.items())))

    print("  the list: first", rows[0][:4], rows[1][:4], "last", rows[-2][:4], rows[-1][:4])
    print("  last pair: evening", rows[-1][0], "18:00 with 06:00 of the next day")

    print("== Frost by counting, per 1 °C of the temperature at 18:00 (all evenings)")
    for lo in range(-2, 9):
        sel = [r for r in rows if lo <= r[1] < lo + 1]
        k = sum(r[3] for r in sel)
        print(f"  {lo} to {lo + 1} °C: {len(sel)} evenings, {k} frost, share {k / len(sel):.2f}")

    print("== Trying every line")
    print(f"  201 values of c; 201^3 = {201 ** 3} lines; x {n} evenings = {201 ** 3 * n:.2e}; "
          f"201^10 = {201 ** 10:.1e}")

    print("== The baseline: never frost")
    print(f"  all: {n - nf} of {n} = {(n - nf) / n:.4f}")
    print(f"  test years: {len(test) - sum(yte)} of {len(test)} = "
          f"{(len(test) - sum(yte)) / len(test):.4f} ± "
          f"{plus_minus((len(test) - sum(yte)) / len(test), len(test)):.4f}")
    print(f"  always frost: {nf} of {n} = {nf / n:.4f}")

    print("== The threshold rule: frost if x1 < c")
    best = None
    for k in range(-60, 141):
        cc = k / 10
        cnt = sum(1 for r in rows if (r[1] < cc) == (r[3] == 1))
        if best is None or cnt > best[1]:
            best = (cc, cnt)
    print(f"  best on all evenings: below {best[0]} °C, {best[1]} of {n} = {best[1] / n:.4f}")
    for cc in (0.0, 2.0, 3.8, 6.0):
        cnt = sum(1 for r in rows if (r[1] < cc) == (r[3] == 1))
        print(f"    below {cc}: {cnt} = {cnt / n:.4f}")
    best_tr = None
    for k in range(-60, 141):
        cc = k / 10
        cnt = sum(1 for r in train if (r[1] < cc) == (r[3] == 1))
        if best_tr is None or cnt > best_tr[1]:
            best_tr = (cc, cnt)
    cnt_te = sum(1 for r in test if (r[1] < best_tr[0]) == (r[3] == 1))
    print(f"  best on the training years: below {best_tr[0]} °C, {best_tr[1]} of {len(train)}"
          f" = {best_tr[1] / len(train):.4f}; on the test years {cnt_te} of {len(test)}"
          f" = {cnt_te / len(test):.4f} ± {plus_minus(cnt_te / len(test), len(test)):.4f}")

    print("== The neuron with a step")
    w, b = THRESHOLD_NEURON
    tonight = next(r for r in rows if r[0] == TONIGHT)
    x = inputs(tonight)
    print(f"  tonight {TONIGHT}: x = ({x[0]}, {x[1]}), 06:00 {tonight[4]}, y = {tonight[3]}")
    print(f"  w = {w}, b = {b}: z = {w[0]}*{x[0]} + {w[1]}*{x[1]} + {b} = {z_of(x, w, b):.4f}"
          f" -> {predict(x, w, b)}")
    print(f"  right on all evenings: {right(xs, ys, w, b)} of {n}")
    for wt, bt in (THRESHOLD_NEURON, TILTED_NEURON, ([-1.0, 0.0], 2.0)):
        r_ = right(xs, ys, wt, bt)
        print(f"    w = {wt}, b = {bt}: {r_} = {r_ / n:.4f}; boundary at x2 = 0.5: "
              f"{-(bt + wt[1] * 0.5) / wt[0]:.2f} °C, at x2 = 1: {-(bt + wt[1]) / wt[0]:.2f} °C")
    print(f"  tilted neuron tonight: z = {z_of(x, *TILTED_NEURON):.4f}")

    print("== AND and OR with w = (1, 1)")
    for name, bb, target in (("AND", -1.5, AND), ("OR", -0.5, OR)):
        zs = [g[0] + g[1] + bb for g in GATE]
        outs = [1 if says_frost(z) else 0 for z in zs]
        assert outs == target
        print(f"  {name}: b = {bb}, z = {zs}, out = {outs}")

    print("== Rosenblatt's rule: one update, then AND")
    ups = rosenblatt_updates(xtr, ytr, 1)
    for k, (i, z, wn, bn) in enumerate(ups[:3], start=1):
        xi = xtr[i]
        znew = z_of(xi, wn, bn)
        print(f"  update {k}: evening {train[i][0]} x = ({xi[0]}, {xi[1]}) y = {ytr[i]}"
              f" (06:00 {train[i][4]}), z before {z:.4f} -> w = ({wn[0]:.2f}, {wn[1]:.2f}),"
              f" b = {bn}, z after {znew:.4f}; |x|^2 + 1 = {xi[0] ** 2 + xi[1] ** 2 + 1:.4f}")
    # AND, step by step
    wa, ba = [0.0, 0.0], 0.0
    step = 0
    and_updates = 0
    for epoch in range(1, 7):
        for g, t in zip(GATE, AND):
            step += 1
            z = z_of(g, wa, ba)
            out = 1 if says_frost(z) else 0
            e = t - out
            wa = [wa[0] + e * g[0], wa[1] + e * g[1]]
            ba = ba + e
            and_updates += e != 0
            if epoch <= 2:
                print(f"    step {step}: x = {g}, y = {t}, z = {z:g}, out = {out}, "
                      f"y - out = {e:+d} -> w = ({wa[0]:g}, {wa[1]:g}), b = {ba:g}")
    print(f"  AND after 6 epochs: w = {wa}, b = {ba}, updates {and_updates}")
    model = Perceptron()
    model.fit(GATE, AND, 6)
    print(f"  class Perceptron on AND, 6 epochs: w = {model.w}, b = {model.b}, "
          f"predict = {[model.predict(g) for g in GATE]}")
    hist = rosenblatt(GATE, AND, 6)
    print("  updates per epoch:", [h[2] for h in hist])
    hist = rosenblatt(GATE, OR, 6)
    print("  OR:", hist[-1][0], hist[-1][1], "updates per epoch:", [h[2] for h in hist])

    print("== Rosenblatt's rule on the training evenings (from zero, eta = 1)")
    hist = rosenblatt(xtr, ytr, 30)
    accs = [right(xtr, ytr, h[0], h[1]) / len(xtr) for h in hist]
    for e in range(5):
        print(f"  epoch {e + 1}: updates {hist[e][2]}, w = ({hist[e][0][0]:.2f}, "
              f"{hist[e][0][1]:.2f}), b = {hist[e][1]}, right {accs[e]:.4f}")
    upd = [h[2] for h in hist]
    print(f"  30 epochs: updates per epoch {min(upd)} to {max(upd)}; right from "
          f"{min(accs):.4f} to {max(accs):.4f}")
    model = Perceptron()
    model.fit(xtr, ytr, RULE_EPOCHS)
    r_tr = right(xtr, ytr, model.w, model.b)
    r_te = right(xte, yte, model.w, model.b)
    print(f"  class Perceptron, {RULE_EPOCHS} epochs: w = {model.w}, b = {model.b}; "
          f"train {r_tr} = {r_tr / len(xtr):.4f}; test {r_te} of {len(xte)} = "
          f"{r_te / len(xte):.4f} ± {plus_minus(r_te / len(xte), len(xte)):.4f}")
    print(f"    tonight: z = {z_of(x, model.w, model.b):.4f} -> {model.predict(x)}")
    bs = [k / 100 for k in range(-400, 1201)]
    ce = [mean_loss(xtr, ytr, [-1.0, 0.0], bb) for bb in bs]
    k = ce.index(min(ce))
    print(f"  with w = (-1, 0): the cross-entropy is lowest at b = {bs[k]:.2f}, "
          f"loss {ce[k]:.4f}; wrong evenings there "
          f"{len(xtr) - right(xtr, ytr, [-1.0, 0.0], bs[k])}")
    pct = [[r[1], r[2]] for r in train]
    hp = rosenblatt(pct, ytr, 10)
    print("  humidity in percent, accuracy per epoch:",
          [round(right(pct, ytr, h[0], h[1]) / len(pct), 4) for h in hp])
    print("    w after 10 epochs", hp[-1][0], hp[-1][1])

    print("== The sigmoid")
    for z in (-4, -2, -1, 0, 1, 1.2, 2, 4):
        print(f"  sigmoid({z}) = {sigmoid(z):.4f}")
    print(f"  e^-1.2 = {math.exp(-1.2):.4f}")

    print("== Four evenings, 6 to 9 December 2025, under the threshold neuron")
    w, b = THRESHOLD_NEURON
    four = [next(r for r in rows if r[0] == d) for d in FOUR]
    like = 1.0
    losses = []
    for r in four:
        xx, yy = inputs(r), r[3]
        z = z_of(xx, w, b)
        p = sigmoid(z)
        py = p if yy == 1 else 1 - p
        like *= py
        losses.append(-math.log(py))
        print(f"  {r[0]}: x = ({xx[0]}, {xx[1]}), 06:00 {r[4]}, y = {yy}, z = {z:.4f}, "
              f"yhat = {p:.4f}, P(y) = {py:.4f}, -ln P(y) = {-math.log(py):.4f}")
    print(f"  likelihood L = {like:.5f}, -ln L = {-math.log(like):.4f}, "
          f"loss = -ln L / 4 = {sum(losses) / 4:.4f}")
    for p in (0.99, 0.9, 0.5, 0.1, 0.01):
        print(f"    -ln {p} = {-math.log(p):.3f}")

    print("== The gradient of one evening: tonight, threshold neuron")
    p = sigmoid(z_of(x, w, b))
    print(f"  yhat = {p:.4f}, yhat - y = {p - 1:.4f}")
    g = [(p - 1) * x[0], (p - 1) * x[1], p - 1]
    print(f"  gradient: d/dw1 = {g[0]:.4f}, d/dw2 = {g[1]:.4f}, d/db = {g[2]:.4f}")
    l0 = evening_loss(x, 1, w, b)
    l1 = evening_loss(x, 1, [w[0] + 0.001, w[1]], b)
    print(f"  loss {l0:.6f}; with w1 + 0.001: {l1:.6f}; difference / 0.001 = "
          f"{(l1 - l0) / 0.001:.4f}")
    eta = 0.1
    wn = [w[0] - eta * g[0], w[1] - eta * g[1]]
    bn = b - eta * g[2]
    pn = sigmoid(z_of(x, wn, bn))
    print(f"  one step, eta = {eta}: w = ({wn[0]:.4f}, {wn[1]:.4f}), b = {bn:.4f}; "
          f"z = {z_of(x, wn, bn):.4f}, yhat = {pn:.4f}, loss {evening_loss(x, 1, wn, bn):.4f}")
    xf, yf = xs_ys(four)
    print(f"  the four evenings: loss before {mean_loss(xf, yf, w, b):.4f}, after the step "
          f"{mean_loss(xf, yf, wn, bn):.4f}")

    print("== The mean slope over the four evenings, threshold neuron")
    g = [0.0, 0.0, 0.0]
    for r, xx, yy in zip(four, xf, yf):
        e = sigmoid(z_of(xx, w, b)) - yy
        print(f"  {r[0]}: yhat - y = {e:.3f}, times x1 = {e * xx[0]:.3f}, times x2 = "
              f"{e * xx[1]:.3f}")
        g = [g[0] + e * xx[0] / 4, g[1] + e * xx[1] / 4, g[2] + e / 4]
    print(f"  mean: d/dw1 = {g[0]:.3f}, d/dw2 = {g[1]:.3f}, d/db = {g[2]:.3f}")
    wm = [w[0] - 0.1 * g[0], w[1] - 0.1 * g[1]]
    bm = b - 0.1 * g[2]
    print(f"  one step, eta = 0.1: w = ({wm[0]:.3f}, {wm[1]:.3f}), b = {bm:.3f}; loss of the "
          f"four {mean_loss(xf, yf, w, b):.3f} -> {mean_loss(xf, yf, wm, bm):.3f}")
    print("    new yhat:", [round(sigmoid(z_of(xx, wm, bm)), 3) for xx in xf])

    print("== The loss in w1 and b, with w2 = 0, on the training evenings")
    w1m, bm = lowest_w1_b(xtr, ytr)
    print(f"  lowest at w1 = {w1m:.3f}, b = {bm:.3f}: threshold {-bm / w1m:.2f} °C, loss "
          f"{mean_loss(xtr, ytr, [w1m, 0.0], bm):.4f}; at w1 = -1, b = 3.8: "
          f"{mean_loss(xtr, ytr, [-1.0, 0.0], 3.8):.4f}")

    print(f"== The logistic neuron: eta = {ETA}, {EPOCHS} passes over the training evenings")
    hist = train_logistic(xtr, ytr, 20)
    for e in (0, 1, 2, 5, 10, 20):
        we, be = hist[e]
        r_ = right(xtr, ytr, we, be)
        print(f"  after {e:2d} epochs: w = ({we[0]:.3f}, {we[1]:.3f}), b = {be:.3f}, "
              f"loss {mean_loss(xtr, ytr, we, be):.4f}, right {r_ / len(xtr):.4f}")
    wl, bl = hist[EPOCHS]
    r_tr = right(xtr, ytr, wl, bl)
    r_te = right(xte, yte, wl, bl)
    acc = r_te / len(xte)
    print(f"  final ({EPOCHS} epochs): w = ({wl[0]:.4f}, {wl[1]:.4f}), b = {bl:.4f}")
    print(f"    boundary at x2 = 0.5: {-(bl + wl[1] * 0.5) / wl[0]:.2f} °C, at 0.85: "
          f"{-(bl + wl[1] * 0.85) / wl[0]:.2f}, at 1: {-(bl + wl[1]) / wl[0]:.2f}")
    print(f"    train {r_tr} of {len(xtr)} = {r_tr / len(xtr):.4f}")
    print(f"    test {r_te} of {len(xte)} = {acc:.4f} ± {plus_minus(acc, len(xte)):.4f}")
    zt = z_of(x, wl, bl)
    print(f"    tonight: z = {zt:.4f}, yhat = {sigmoid(zt):.4f}")
    for t in (1.0, 3.0, 5.0):
        print(f"    {t} °C, 0.85: yhat = {sigmoid(z_of([t, 0.85], wl, bl)):.3f}")
    caught = sum(1 for i in range(len(xte)) if yte[i] == 1 and predict(xte[i], wl, bl) == 1)
    missed = sum(1 for i in range(len(xte)) if yte[i] == 1 and predict(xte[i], wl, bl) == 0)
    alarms = sum(1 for i in range(len(xte)) if yte[i] == 0 and predict(xte[i], wl, bl) == 1)
    print(f"    test errors at 0.5: caught {caught}, missed {missed}, false alarms {alarms}")
    for thr in (0.3, 0.2):
        pr = [1 if sigmoid(z_of(xte[i], wl, bl)) > thr else 0 for i in range(len(xte))]
        caught = sum(1 for i in range(len(xte)) if yte[i] == 1 and pr[i] == 1)
        missed = sum(1 for i in range(len(xte)) if yte[i] == 1 and pr[i] == 0)
        alarms = sum(1 for i in range(len(xte)) if yte[i] == 0 and pr[i] == 1)
        print(f"    at {thr}: caught {caught}, missed {missed}, false alarms {alarms}, right "
              f"{(len(xte) - missed - alarms) / len(xte):.4f}")
    w1, b1 = train_logistic_1([xx[0] for xx in xtr], ytr)
    r1 = sum(1 for i in range(len(xte)) if says_frost(w1 * xte[i][0] + b1) == (yte[i] == 1))
    print(f"  temperature alone: w = {w1:.4f}, b = {b1:.4f}, threshold {-b1 / w1:.2f} °C, "
          f"test {r1} = {r1 / len(xte):.4f}")
    rule_te = sum(1 for r in test if (r[1] < best_tr[0]) == (r[3] == 1))
    same = sum(1 for i, r in enumerate(test)
               if (r[1] < best_tr[0]) == (predict(xte[i], wl, bl) == 1))
    print(f"  the neuron and the rule below {best_tr[0]} agree on {same} of {len(test)} "
          f"test evenings; rule right {rule_te}")

    print("== Seen and unseen evenings")
    print(f"  logistic neuron, 3 numbers: train {r_tr / len(xtr):.4f}, test {acc:.4f}")
    cal = calendar_rule(train)
    c_tr = sum(1 for r in train if cal.get(r[0][5:], 0) == r[3])
    c_te = sum(1 for r in test if cal.get(r[0][5:], 0) == r[3])
    print(f"  calendar rule, {len(cal)} numbers: train {c_tr} = {c_tr / len(train):.4f}, "
          f"test {c_te} = {c_te / len(test):.4f}")
    n_tr = sum(1 for i in range(len(xtr)) if nearest_rule(xtr, ytr, xtr[i]) == ytr[i])
    n_te = sum(1 for i in range(len(xte)) if nearest_rule(xtr, ytr, xte[i]) == yte[i])
    print(f"  nearest training evening, {3 * len(xtr)} numbers: train {n_tr} = "
          f"{n_tr / len(xtr):.4f}, test {n_te} = {n_te / len(xte):.4f}")

    print("== XOR")
    print("  Rosenblatt updates per epoch:", [h[2] for h in rosenblatt(GATE, XOR, 8)])
    wq, bq = [0.3, -0.2], 0.1
    for _ in range(20000):
        grads = [0.0, 0.0, 0.0]
        for g, t in zip(GATE, XOR):
            e = sigmoid(z_of(g, wq, bq)) - t
            grads = [grads[0] + e * g[0] / 4, grads[1] + e * g[1] / 4, grads[2] + e / 4]
        wq = [wq[0] - 0.5 * grads[0], wq[1] - 0.5 * grads[1]]
        bq = bq - 0.5 * grads[2]
    print(f"  logistic, from w = (0.3, -0.2), b = 0.1, 20000 steps: w = ({wq[0]:.5f}, "
          f"{wq[1]:.5f}), b = {bq:.5f}, loss {mean_loss(GATE, XOR, wq, bq):.4f}, "
          f"ln 2 = {math.log(2):.4f}")

    print("== Convergence bound for AND (For the Curious)")
    print(f"  gamma = 1/sqrt(17) = {1 / math.sqrt(17):.3f}, R^2 = 3, bound 51, updates 10")


# ------------------------------------------------------------------ helpers
def _np(rows):
    X = np.array([inputs(r) for r in rows])
    y = np.array([r[3] for r in rows])
    return X, y


def _scatter(ax, X, y, ms=3.2, alpha=0.55, labels=True):
    """The evenings as points, as vector markers (no raster: crisp at any size)."""
    n1, n0 = int(y.sum()), int(len(y) - y.sum())
    ax.plot(X[y == 0, 0], X[y == 0, 1], "o", ms=ms, color=C0, alpha=alpha, mec="none",
            label=f"no frost at 06:00 ({n0})" if labels else None)
    ax.plot(X[y == 1, 0], X[y == 1, 1], "^", ms=ms + 0.6, color=C1, alpha=alpha, mec="none",
            label=f"frost at 06:00 ({n1})" if labels else None)


def _boundary(ax, w, b, xlim, ylim, **kw):
    """Draw the line w1 x1 + w2 x2 + b = 0 inside the frame."""
    if abs(w[1]) > 1e-12 and abs(w[0]) > 1e-12:
        x2 = np.array(ylim, dtype=float)
        ax.plot(-(b + w[1] * x2) / w[0], x2, **kw)
    elif abs(w[1]) > 1e-12:
        x1 = np.array(xlim, dtype=float)
        ax.plot(x1, -(w[0] * x1 + b) / w[1], **kw)
    else:
        ax.axvline(-b / w[0], **kw)


def _shade(ax, w, b, xlim, ylim, color=C1, alpha=0.10):
    """Shade the side of the line where z > 0."""
    g1, g2 = np.meshgrid(np.linspace(*xlim, 300), np.linspace(*ylim, 300))
    z = w[0] * g1 + w[1] * g2 + b
    ax.contourf(g1, g2, z, levels=[0, 1e9], colors=[color], alpha=alpha)


def _evening_frame(ax, xlim=(-13, 31), ylim=(0.38, 1.03)):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks([t for t in range(-15, 35, 5) if xlim[0] <= t <= xlim[1]])
    ax.set_xlabel("temperature at 18:00, $x_1$ (°C)")
    ax.set_ylabel("humidity at 18:00, $x_2$")


def _arrow(ax, p, q, color=LINE, lw=2.0, ms=14, zorder=6):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=ms,
                                 lw=lw, color=color, zorder=zorder,
                                 shrinkA=0, shrinkB=0))


def _gate_frame(ax, lim):
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")


def _gate_points(ax, y, ms=11):
    for (a, b_), t in zip(GATE, y):
        ax.plot(a, b_, "^" if t else "o", ms=ms + (1 if t else 0),
                color=C1 if t else C0, mec="none", zorder=5)


def _gate_boundary(ax, w, b, lim, **kw):
    x1 = np.array(lim, dtype=float)
    if abs(w[1]) > 1e-12:
        ax.plot(x1, -(w[0] * x1 + b) / w[1], **kw)
    else:
        ax.axvline(-b / w[0], **kw)


def _gate_shade(ax, w, b, lim, color=C1, alpha=0.10):
    g1, g2 = np.meshgrid(np.linspace(*lim, 200), np.linspace(*lim, 200))
    ax.contourf(g1, g2, w[0] * g1 + w[1] * g2 + b, levels=[0, 1e9], colors=[color], alpha=alpha)


# ------------------------------------------------------------ the evenings
def _evenings_fig():
    rows = evenings()
    X, y = _np(rows)
    fig, ax = style.new_fig(9.4, 3.4)
    _scatter(ax, X, y)
    t = inputs(next(r for r in rows if r[0] == TONIGHT))
    ax.plot(*t, "o", ms=13, mfc="none", mec=LINE, mew=1.8, zorder=6)
    ax.annotate("8 December 2025:\n2.6 °C, 0.85", xy=t, xytext=(9.5, 0.47),
                color=LINE, fontsize=11, va="center",
                arrowprops={"arrowstyle": "-", "color": LINE, "lw": 1.0})
    _evening_frame(ax)
    ax.legend(loc="upper right", markerscale=2.2)
    style.save(fig, "viz_perceptron_evenings")


def _threshold_fig():
    rows = evenings()
    X, y = _np(rows)
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3))
    ax = axes[0]
    bins = np.arange(-13, 32, 1.0)
    ax.hist(X[y == 0, 0], bins=bins, color=C0, alpha=0.55, label="no frost")
    ax.hist(X[y == 1, 0], bins=bins, color=C1, alpha=0.65, label="frost")
    ax.axvline(3.8, color=LINE, lw=1.6, ls="--")
    ax.set_xlabel("temperature at 18:00, $x_1$ (°C)")
    ax.set_ylabel("evenings per 1 °C")
    ax.legend(loc="upper right")
    ax = axes[1]
    cs = np.arange(-6, 14.01, 0.1)
    acc = [100 * np.mean((X[:, 0] < c) == (y == 1)) for c in cs]
    ax.plot(cs, acc, color=GREEN, lw=2.2)
    base = 100 * np.mean(y == 0)
    ax.axhline(base, color=style.DIM, lw=1.2, ls=":")
    ax.text(13.8, base - 1.5, f"never frost: {base:.1f} %", color=style.DIM, ha="right",
            va="top", fontsize=10.5)
    k = int(np.argmax(acc))
    ax.plot(cs[k], acc[k], "o", color=LINE, ms=6, zorder=5)
    ax.text(cs[k] + 0.6, acc[k] + 0.6, f"below {cs[k]:.1f} °C: {acc[k]:.1f} %", color=LINE,
            fontsize=11, va="bottom")
    ax.set_xlim(-6, 14)
    ax.set_xticks([-5, 0, 5, 10])
    ax.set_ylim(50, 100)
    ax.set_xlabel("threshold $c$: frost if $x_1 < c$ (°C)")
    ax.set_ylabel("evenings right (%)")
    style.save(fig, "viz_perceptron_threshold")


# ------------------------------------------------------------- the neuron
def _unit():
    fig, ax = plt.subplots(figsize=(9.2, 3.3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.6)
    ax.set_aspect("equal")   # round circles at any size of the box
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
    ax.text(0.15, 3.0, "°C", ha="center", va="center", fontsize=11, color=style.DIM)
    ax.text(0.15, 1.8, "0–1", ha="center", va="center", fontsize=11, color=style.DIM)
    ax.add_patch(Circle((4.6, 1.8), 0.62, fc="none", ec=LINE, lw=2.2))
    ax.text(4.6, 1.8, r"$\Sigma$", ha="center", va="center", fontsize=22, color=LINE)
    ax.text(4.6, 0.72, "$z = w_1 x_1 + w_2 x_2 + b$", ha="center", va="center",
            fontsize=13, color=LINE)
    _arrow(ax, (5.25, 1.8), (6.35, 1.8), color=style.DIM, lw=1.6)
    ax.text(5.8, 1.98, "$z$", ha="center", va="bottom", fontsize=14, color=LINE)
    ax.add_patch(FancyBboxPatch((6.4, 1.25), 1.5, 1.1,
                                boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc="none", ec=GREEN, lw=2.2))
    ax.text(7.15, 1.8, "step", ha="center", va="center", fontsize=15, color=LINE)
    _arrow(ax, (7.95, 1.8), (9.0, 1.8), color=style.DIM, lw=1.6)
    ax.text(9.4, 1.8, r"$\hat{y}$", ha="center", va="center", fontsize=20, color=LINE)
    ax.text(7.15, 0.72, r"$\hat{y}$ = 1 if $z$ > 0, else 0", ha="center", va="center",
            fontsize=12, color=style.DIM)
    style.save(fig, "viz_perceptron_unit")


def _gates():
    fig, axes = plt.subplots(2, 1, figsize=(5.4, 5.1))
    lim = (-0.6, 1.8)
    for ax, y, b, name in [(axes[0], AND, -1.5, "AND"), (axes[1], OR, -0.5, "OR")]:
        w = [1.0, 1.0]
        _gate_shade(ax, w, b, lim)
        _gate_boundary(ax, w, b, lim, color=LINE, lw=2.2)
        _gate_points(ax, y)
        _gate_frame(ax, lim)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_title(f"{name}:  $x_1 + x_2 {b:+.1f} = 0$".replace("-", "−"), fontsize=12)
    style.save(fig, "viz_perceptron_gates")


# ---------------------------------------------------- Rosenblatt's rule
def _and_run():
    ups = rosenblatt_updates(GATE, AND, 6)
    assert len(ups) == 10, len(ups)
    lim = (-1.6, 2.6)
    fig, axes = plt.subplots(2, 5, figsize=(11.5, 4.9))
    for k, (ax, (i, _, w, b)) in enumerate(zip(axes.ravel(), ups), start=1):
        if w[0] != 0 or w[1] != 0:
            _gate_shade(ax, w, b, lim)
            _gate_boundary(ax, w, b, lim, color=LINE, lw=1.8)
        _gate_points(ax, AND, ms=7)
        ax.plot(*GATE[i], "o", ms=15, mfc="none", mec=style.BAD, mew=1.8, zorder=6)
        ax.set_xlim(*lim)
        ax.set_ylim(*lim)
        ax.set_aspect("equal")
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.tick_params(labelsize=8)
        ax.set_title(f"{k}:  $w$ = ({w[0]:.0f}, {w[1]:.0f}),  $b$ = {b:.0f}".replace("-", "−"),
                     fontsize=10.5, fontweight="normal")
    style.save(fig, "viz_perceptron_and_run")


def _rule_evenings():
    rows = evenings()
    train, _ = split(rows)
    xtr, ytr = xs_ys(train)
    hist = rosenblatt(xtr, ytr, 30)
    accs = [100 * right(xtr, ytr, h[0], h[1]) / len(xtr) for h in hist]
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.4), gridspec_kw={"width_ratios": [1.15, 1]})
    ax = axes[0]
    ep = np.arange(1, 31)
    ax.plot(ep, accs, "-", color=C1, lw=1.4)
    ax.plot(ep, accs, "o", color=C1, ms=4.5)
    base = 100 * (1 - sum(ytr) / len(ytr))
    ax.axhline(base, color=style.DIM, lw=1.1, ls=":", label=f"never frost, {base:.1f} %")
    ax.legend(loc="lower left", fontsize=9.5)
    ax.set_xlim(0, 31)
    ax.set_ylim(20, 100)
    ax.set_xlabel("epoch: one pass over the 2551 training evenings")
    ax.set_ylabel("training evenings right (%)")
    upd = [h[2] for h in hist]
    ax.set_title(f"{min(upd)} to {max(upd)} updates in every epoch", fontsize=12.5,
                 fontweight="normal")
    ax = axes[1]
    X, y = _np(train)
    xlim, ylim = (-8, 16), (0.38, 1.03)
    _scatter(ax, X, y, ms=2.6, alpha=0.45, labels=False)
    for e, col in ((1, LINE), (3, GREEN), (4, PINK)):
        w, b, _ = hist[e - 1]
        _boundary(ax, w, b, xlim, ylim, color=col, lw=2.2,
                  label=f"after epoch {e}: {accs[e - 1]:.0f} %")
    _evening_frame(ax, xlim, ylim)
    ax.legend(loc="lower left", fontsize=9.5, bbox_to_anchor=(0.0, 1.0), ncol=3,
              borderaxespad=0.2, columnspacing=1.0, handlelength=1.3)
    style.save(fig, "viz_perceptron_rule_evenings")


# ------------------------------------------------- the step, the sigmoid
def _step_loss():
    """With w = (-1, 0), b is the threshold: the wrong evenings and the
    cross-entropy as b runs, on the training evenings."""
    rows = evenings()
    train, _ = split(rows)
    X, y = _np(train)
    bs = np.linspace(-4, 12, 1601)
    wrong = [int(np.sum((np.round(b - X[:, 0], 9) > 0) != (y == 1))) for b in bs]
    z = bs[:, None] - X[None, :, 0]
    ce = np.mean(np.logaddexp(0, z) - y[None, :] * z, axis=1)
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3))
    ax = axes[0]
    ax.plot(bs, wrong, color=C0, lw=1.8, drawstyle="steps-mid")
    ax.set_xlabel("bias $b$, with $w$ = (−1, 0)")
    ax.set_ylabel("training evenings wrong")
    ax.set_ylim(0, None)
    ax.set_title("Wrong evenings: flat steps", fontsize=12.5, fontweight="normal")
    ax.set_xlim(-4, 12)
    axin = ax.inset_axes([0.33, 0.56, 0.36, 0.38])
    sel = (bs > 2.5) & (bs < 5.0)
    axin.plot(bs[sel], np.array(wrong)[sel], color=C0, lw=1.6, drawstyle="steps-mid")
    axin.tick_params(labelsize=8)
    axin.set_title("2.5 to 5", fontsize=9, color=style.DIM)
    ax = axes[1]
    ax.plot(bs, ce, color=C1, lw=2.2)
    i = int(np.argmin(ce))
    ax.plot(bs[i], ce[i], "o", color=LINE, ms=6)
    ax.text(bs[i], ce[i] + 0.25, f"lowest at $b$ = {bs[i]:.2f}", ha="center", color=LINE,
            fontsize=11)
    ax.set_xlabel("bias $b$, with $w$ = (−1, 0)")
    ax.set_ylabel("cross-entropy loss")
    ax.set_ylim(0, None)
    ax.set_xlim(-4, 12)
    ax.set_title("Cross-entropy: a slope everywhere", fontsize=12.5, fontweight="normal")
    style.save(fig, "viz_perceptron_step_loss")


def _sigmoid():
    z = np.linspace(-7, 7, 600)
    fig, ax = style.new_fig(6.2, 4.3)
    ax.plot(z, (z > 0).astype(float), color=C0, lw=2, label="step")
    ax.plot(z, 1 / (1 + np.exp(-z)), color=C1, lw=2.4, label="sigmoid$(z)$")
    for zz, dx, dy in ((-2, 0.3, -0.06), (0, 0.35, -0.05), (2, 0.3, -0.07)):
        s = sigmoid(zz)
        ax.plot(zz, s, "o", color=LINE, ms=5)
        ax.text(zz + dx, s + dy, f"{s:.3g}", color=LINE, fontsize=10.5)
    s = sigmoid(1.2)
    ax.plot(1.2, s, "o", color=GREEN, ms=7, zorder=6)
    ax.annotate(f"8 Dec 2025: $z$ = 1.2, {s:.3f}", xy=(1.2, s), xytext=(-6.6, 0.82),
                color=GREEN, fontsize=11, va="center",
                arrowprops={"arrowstyle": "-", "color": GREEN, "lw": 1.0})
    ax.set_xlabel("$z$")
    ax.set_ylabel(r"output $\hat{y}$")
    ax.set_ylim(-0.05, 1.08)
    ax.legend(loc="lower right")
    style.save(fig, "viz_perceptron_sigmoid")


def _cross_entropy():
    rows = evenings()
    w, b = THRESHOLD_NEURON
    p = np.linspace(0.004, 0.996, 500)
    fig, ax = style.new_fig(6.2, 4.3)
    ax.plot(p, -np.log(p), color=C1, lw=2.4, label=r"frost, $y$ = 1:  $-\ln \hat{y}$")
    ax.plot(p, -np.log(1 - p), color=C0, lw=2.4,
            label=r"no frost, $y$ = 0:  $-\ln(1 - \hat{y})$")
    spots = {"2025-12-06": (0.66, 3.6), "2025-12-07": (0.45, 1.85),
             "2025-12-08": (0.5, 0.18), "2025-12-09": (0.8, 0.5)}
    for d in FOUR:
        r = next(r for r in rows if r[0] == d)
        s = sigmoid(z_of(inputs(r), w, b))
        cost = -math.log(s if r[3] else 1 - s)
        ax.plot(s, cost, "o", color=LINE, ms=6, zorder=6)
        ax.annotate(f"{int(d[8:])} Dec: {cost:.2f}", xy=(s, cost), xytext=spots[d],
                    color=LINE, fontsize=10.5, ha="center", va="center",
                    arrowprops={"arrowstyle": "-", "color": style.DIM, "lw": 0.9,
                                "shrinkA": 6, "shrinkB": 4})
    ax.set_xlabel(r"output $\hat{y}$ = P(frost)")
    ax.set_ylabel("loss of one evening")
    ax.set_ylim(0, 5)
    ax.set_xlim(0, 1)
    ax.legend(loc="upper center", fontsize=10)
    style.save(fig, "viz_perceptron_cross_entropy")


# ----------------------------------------------------------- the training
def _training():
    rows = evenings()
    train, _ = split(rows)
    xtr, ytr = xs_ys(train)
    hist = train_logistic(xtr, ytr, 20)
    loss = [mean_loss(xtr, ytr, w, b) for w, b in hist]
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.4), gridspec_kw={"width_ratios": [1, 1.15]})
    ax = axes[0]
    ep = np.arange(len(hist))
    ax.plot(ep, loss, "-", color=C1, lw=1.6)
    ax.plot(ep, loss, "o", color=C1, ms=4.5)
    ax.axhline(math.log(2), color=style.DIM, lw=1.1, ls=":")
    ax.text(20, math.log(2) - 0.03, "ln 2 = 0.693: every $\\hat{y}$ = 0.5", color=style.DIM,
            ha="right", va="top", fontsize=10)
    for e, dy in ((1, 0.06), (EPOCHS, 0.06)):
        ax.text(e + 0.3, loss[e] + dy, f"{loss[e]:.3f}", color=LINE, fontsize=10.5)
    ax.plot(EPOCHS, loss[EPOCHS], "o", color=LINE, ms=6, zorder=6)
    ax.set_xlim(-0.5, 20.5)
    ax.set_xticks([0, 5, 10, 15, 20])
    ax.set_ylim(0, 0.75)
    ax.set_xlabel("epoch")
    ax.set_ylabel("loss on the training evenings")
    ax = axes[1]
    X, y = _np(train)
    xlim, ylim = (-8, 16), (0.38, 1.03)
    _scatter(ax, X, y, ms=2.6, alpha=0.45, labels=False)
    for e, col in ((1, PINK), (EPOCHS, LINE)):
        w, b = hist[e]
        _boundary(ax, w, b, xlim, ylim, color=col, lw=2.2,
                  label=f"after epoch {e}")
    _evening_frame(ax, xlim, ylim)
    ax.legend(loc="lower left", fontsize=9.5, bbox_to_anchor=(0.0, 1.0), ncol=2,
              borderaxespad=0.2)
    style.save(fig, "viz_perceptron_training")


def _bowl():
    """The loss of the training evenings as a function of w1 and b, w2 = 0."""
    rows = evenings()
    train, _ = split(rows)
    X, y = _np(train)
    w1s = np.linspace(-2.2, -0.2, 241)
    bs = np.linspace(0.5, 7.5, 241)
    W1, B = np.meshgrid(w1s, bs)
    Z = W1[..., None] * X[:, 0] + B[..., None]
    L = np.mean(np.logaddexp(0, Z) - y * Z, axis=-1)
    xtr, ytr = xs_ys(train)
    w1m, bm = lowest_w1_b(xtr, ytr)
    fig, ax = style.new_fig(6.2, 4.3)
    levels = [0.11, 0.12, 0.14, 0.17, 0.22, 0.3, 0.45, 0.7, 1.0, 1.5]
    cs = ax.contour(W1, B, L, levels=levels, colors=[C1], linewidths=1.2, alpha=0.9)
    ax.clabel(cs, fmt=lambda v: f"{v:g}", fontsize=9, colors=[LINE])
    ax.plot(w1m, bm, "o", color=LINE, ms=7, zorder=6)
    back = {"boxstyle": "round,pad=0.25", "fc": style.BG, "ec": "none", "alpha": 0.9}
    ax.annotate(f"lowest: $w_1$ = {w1m:.2f}, $b$ = {bm:.2f}".replace("-", "−"),
                xy=(w1m, bm), xytext=(-2.1, 6.6), color=LINE, fontsize=11, bbox=back,
                arrowprops={"arrowstyle": "-", "color": LINE, "lw": 1.0})
    ax.plot(-1.0, 3.8, "s", color=GREEN, ms=7, zorder=6)
    ax.annotate("below 3.8 °C: $w_1$ = −1, $b$ = 3.8", xy=(-1.0, 3.8), xytext=(-1.55, 1.2),
                color=GREEN, fontsize=11, ha="center", bbox=back,
                arrowprops={"arrowstyle": "-", "color": GREEN, "lw": 1.0})
    ax.set_xlabel("weight of the temperature, $w_1$")
    ax.set_ylabel("bias $b$")
    style.save(fig, "viz_perceptron_bowl")


def _probability():
    """The share of test evenings followed by frost per 1 °C of x1, against the
    trained neuron's output at the humidity of tonight."""
    rows = evenings()
    train, test = split(rows)
    xtr, ytr = xs_ys(train)
    w, b = train_logistic(xtr, ytr)[EPOCHS]
    X, y = _np(test)
    fig, ax = style.new_fig(6.2, 4.3)
    edges = np.arange(-6, 13, 1.0)
    for lo in edges[:-1]:
        sel = (X[:, 0] >= lo) & (X[:, 0] < lo + 1)
        nsel = int(sel.sum())
        if nsel < 5:
            continue
        share = y[sel].mean()
        err = math.sqrt(max(share * (1 - share), 0.25 / nsel) / nsel)
        ax.errorbar(lo + 0.5, share, yerr=err, fmt="o", color=C0, ms=5, lw=1.2,
                    capsize=0)
    t = np.linspace(-6, 12, 400)
    ax.plot(t, 1 / (1 + np.exp(-(w[0] * t + w[1] * 0.85 + b))), color=C1, lw=2.4,
            label=r"neuron: $\hat{y}$ at $x_2$ = 0.85")
    ax.plot([], [], "o", color=C0, ms=5, label="test evenings: share with frost, per 1 °C")
    s = sigmoid(z_of([2.6, 0.85], w, b))
    ax.plot(2.6, s, "o", color=GREEN, ms=8, zorder=6)
    ax.annotate(f"8 Dec 2025: {s:.2f}", xy=(2.6, s), xytext=(5.0, 0.86), color=GREEN,
                fontsize=11, arrowprops={"arrowstyle": "-", "color": GREEN, "lw": 1.0})
    ax.set_xlim(-6, 12)
    ax.set_ylim(-0.04, 1.06)
    ax.set_xlabel("temperature at 18:00, $x_1$ (°C)")
    ax.set_ylabel("P(frost at 06:00)")
    ax.legend(loc="lower left", fontsize=9.5)
    style.save(fig, "viz_perceptron_probability")


def _test_fig():
    rows = evenings()
    train, test = split(rows)
    xtr, ytr = xs_ys(train)
    xte, yte = xs_ys(test)
    n = len(test)
    w, b = train_logistic(xtr, ytr)[EPOCHS]
    model = Perceptron()
    model.fit(xtr, ytr, RULE_EPOCHS)
    entries = [
        ("never frost", (n - sum(yte)) / n, style.DIM),
        (f"Rosenblatt's rule, {RULE_EPOCHS} epochs", right(xte, yte, model.w, model.b) / n, C0),
        ("frost if $x_1$ < 3.8 °C", sum(1 for r in test if (r[1] < 3.8) == (r[3] == 1)) / n,
         GREEN),
        ("logistic neuron", right(xte, yte, w, b) / n, C1),
    ]
    fig, ax = style.new_fig(9.4, 3.0)
    for k, (lab, p, col) in enumerate(entries):
        e = plus_minus(p, n)
        ax.barh(k, 100 * p, color=col, alpha=0.85, height=0.62)
        ax.errorbar(100 * p, k, xerr=100 * e, color=LINE, lw=1.4, capsize=4)
        ax.text(100 * p + 100 * e + 1.2, k, f"{100 * p:.1f} ± {100 * e:.1f} %",
                va="center", color=LINE, fontsize=11.5)
    ax.set_yticks(range(len(entries)))
    ax.set_yticklabels([e[0] for e in entries], fontsize=11.5)
    ax.set_xlim(0, 112)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_xlabel(f"test evenings right, 2023–2025, of {n} (%)")
    ax.grid(axis="y", visible=False)
    style.save(fig, "viz_perceptron_test")


# ------------------------------------------------------------------ XOR
def _xor_frame(ax, lim):
    _gate_points(ax, XOR, ms=13)
    _gate_frame(ax, lim)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])


def _xor_lines():
    lim = (-0.7, 1.7)
    fig, ax = style.new_fig(4.7, 4.6)
    tries = [([1.0, 1.0], -0.5, PINK), ([1.0, -1.0], -0.5, GREEN), ([1.0, 0.0], -0.5, VIOLET)]
    for w, b, col in tries:
        wrong = sum(1 for g, t in zip(GATE, XOR) if says_frost(z_of(g, w, b)) != (t == 1))
        _gate_boundary(ax, w, b, lim, color=col, lw=2, label=f"{wrong} wrong")
    _xor_frame(ax, lim)
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title("Three lines tried", fontsize=13)
    style.save(fig, "viz_perceptron_xor_lines")


# ------------------------------------------------------- For the Curious
def _proof():
    """The two inequalities of the convergence proof, on the AND run."""
    w_star = np.array([-3.0, 2.0, 2.0]) / np.sqrt(17)
    gamma = 1 / np.sqrt(17)
    R = np.sqrt(3.0)
    ups = rosenblatt_updates(GATE, AND, 6)
    wt = np.array([[b, w[0], w[1]] for _, _, w, b in ups])
    k = np.arange(1, len(ups) + 1)
    proj = wt @ w_star
    norm = np.linalg.norm(wt, axis=1)
    assert np.all(proj >= k * gamma - 1e-12) and np.all(norm <= np.sqrt(k) * R + 1e-12)
    kk = np.linspace(0, 60, 400)
    fig, ax = style.new_fig(5.8, 4.4)
    ax.plot(kk, np.sqrt(kk) * R, color=C0, lw=2.2, label=r"upper bound  $\sqrt{k}\,R$")
    ax.plot(kk, kk * gamma, color=C1, lw=2.2, label=r"lower bound  $k\,\gamma$")
    ax.plot(k, norm, "s", color=C0, ms=6, label=r"length  $\|\tilde{w}_k\|$ in the run")
    ax.plot(k, proj, "o", color=C1, ms=6, label=r"$\tilde{w}^* \cdot \tilde{w}_k$ in the run")
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


def _line():
    """w = (3, 4), b = -10: boundary, w at a right angle, distance of a point."""
    w = np.array([3.0, 4.0])
    b = -10.0
    nvec = w / np.linalg.norm(w)
    xlim, ylim = (-1.0, 6.2), (-1.2, 4.2)
    fig, ax = style.new_fig(6.0, 4.4)
    g1, g2 = np.meshgrid(np.linspace(*xlim, 300), np.linspace(*ylim, 300))
    ax.contourf(g1, g2, w[0] * g1 + w[1] * g2 + b, levels=[0, 1e9], colors=[C1], alpha=0.10)
    x1 = np.array(xlim)
    ax.plot(x1, -(w[0] * x1 + b) / w[1], color=LINE, lw=2.4)
    foot0 = -b / (w @ w) * w
    _arrow(ax, foot0, foot0 + 1.5 * nvec, color=C0, lw=2.6, ms=18)
    ax.text(*(foot0 + 1.5 * nvec + np.array([0.12, 0.05])), "$w$ = (3, 4)", color=C0,
            fontsize=13, va="bottom")
    ax.plot([0, foot0[0]], [0, foot0[1]], ls=":", color=style.DIM, lw=1.6)
    ax.text(-0.12, -0.3, "origin", color=style.DIM, fontsize=10, ha="right")
    ax.plot(0, 0, "o", color=style.DIM, ms=6)
    ax.text(0.36, 1.02, r"$|b|/\|w\|$ = 2", color=style.DIM, fontsize=11, rotation=53,
            ha="center", va="center")
    x = np.array([4.0, 2.0])
    d = (w @ x + b) / np.linalg.norm(w)
    foot = x - d * nvec
    ax.plot([foot[0], x[0]], [foot[1], x[1]], color=GREEN, lw=2.4)
    ax.plot(*x, "^", color=C1, ms=11, zorder=6)
    ax.plot(*foot, "o", color=LINE, ms=5, zorder=6)
    ax.text(x[0] + 0.15, x[1] + 0.1, "$x$ = (4, 2)\n$z$ = 10", color=LINE, fontsize=11.5,
            va="bottom")
    ax.text(*(0.5 * (x + foot) + np.array([0.12, -0.3])), "$d$ = 2", color=GREEN, fontsize=13)
    x2 = np.array([1.0, 0.5])
    ax.plot(*x2, "o", color=C0, ms=10, zorder=6)
    ax.text(x2[0] + 0.15, x2[1] - 0.1, "(1, 0.5)\n$z$ = −5", color=LINE, fontsize=11.5,
            va="top")
    ax.text(4.9, 3.7, "$z$ > 0", color=C1, fontsize=13)
    ax.text(-0.8, -0.95, "$z$ < 0", color=C0, fontsize=13)
    ax.text(3.9, -0.62, "$3x_1 + 4x_2 - 10 = 0$", color=LINE, fontsize=12, rotation=-36.9,
            ha="center", va="center")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    style.save(fig, "viz_perceptron_line")


def _sigmoid_slope():
    z = np.linspace(-7, 7, 600)
    s = 1 / (1 + np.exp(-z))
    fig, ax = style.new_fig(6.2, 4.3)
    ax.plot(z, s * (1 - s), color=GREEN, lw=2.4)
    for zz in (0, 2):
        v = sigmoid(zz) * (1 - sigmoid(zz))
        ax.plot(zz, v, "o", color=LINE, ms=5)
        ax.text(zz + 0.35, v, f"{v:.3f} at $z$ = {zz}", color=LINE, fontsize=10.5,
                va="center")
    ax.set_xlabel("$z$")
    ax.set_ylabel("slope of the sigmoid")
    ax.set_ylim(0, 0.29)
    style.save(fig, "viz_perceptron_sigmoid_slope")


def _posterior():
    """Two Gaussian classes in one dimension give a sigmoid posterior."""
    x = np.linspace(-3.5, 5.5, 600)

    def g(m):
        return np.exp(-0.5 * (x - m) ** 2) / np.sqrt(2 * np.pi)

    p0, p1 = g(0.0), g(2.0)
    post = p1 / (p0 + p1)
    assert np.allclose(post, 1 / (1 + np.exp(-(2 * x - 2))))
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
    ax.text(1.5, 0.22, "sigmoid$(2x - 2)$", color=LINE, fontsize=12)
    style.save(fig, "viz_perceptron_posterior")


def _wb():
    lim = (-0.5, 4.5)
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.9))
    ax = axes[0]
    p0 = np.array([2.0, 2.0])
    for w, col in [((1.0, 1.0), LINE), ((1.0, 0.25), C1), ((0.25, 1.0), C0)]:
        w = np.array(w)
        b = -w @ p0
        _gate_boundary(ax, w, b, lim, color=col, lw=2)
        _arrow(ax, p0, p0 + 1.1 * w / np.linalg.norm(w), color=col, lw=2, ms=13)
    ax.plot(*p0, "o", color=style.DIM, ms=5, zorder=7)
    ax.set_title("Turn $w$: the line turns", fontsize=13)
    ax = axes[1]
    for b, col in [(-2.0, C1), (-4.0, LINE), (-6.0, C0)]:
        _gate_boundary(ax, (1.0, 1.0), b, lim, color=col, lw=2)
        c = -b
        ax.text(c / 2 + 0.75, c / 2 - 0.45, f"$b$ = {b:.0f}".replace("-", "−"), color=col,
                fontsize=11, rotation=-45, ha="center", va="center")
    ax.set_title("Change $b$: the line shifts", fontsize=13)
    ax = axes[2]
    _gate_boundary(ax, (1.0, 1.0), -4.0, lim, color=LINE, lw=2)
    _arrow(ax, (2.0, 2.0), (2.5, 2.5), color=C1, lw=2.4, ms=13)
    _arrow(ax, (1.2, 2.8), (2.2, 3.8), color=C0, lw=2.4, ms=13)
    ax.text(2.6, 2.2, "$w$ = (1, 1), $b$ = −4", color=C1, fontsize=10.5)
    ax.text(0.2, 4.05, "$w$ = (2, 2), $b$ = −8", color=C0, fontsize=10.5)
    ax.set_title("Scale $w$ and $b$: the same line", fontsize=13)
    for ax in axes:
        _gate_frame(ax, lim)
        ax.set_xticks([0, 2, 4])
        ax.set_yticks([0, 2, 4])
    style.save(fig, "viz_perceptron_wb")


def _percent():
    """Rosenblatt's rule with the humidity in percent, against as a fraction."""
    rows = evenings()
    train, _ = split(rows)
    ytr = [r[3] for r in train]
    frac = [inputs(r) for r in train]
    pct = [[r[1], r[2]] for r in train]
    fig, ax = style.new_fig(6.2, 4.3)
    ep = np.arange(1, 11)
    for xs, col, lab in ((frac, C1, "humidity as a fraction, 0.85"),
                         (pct, C0, "humidity in percent, 85")):
        hist = rosenblatt(xs, ytr, 10)
        accs = [100 * right(xs, ytr, h[0], h[1]) / len(xs) for h in hist]
        ax.plot(ep, accs, "o-", color=col, lw=1.6, ms=5, label=lab)
    ax.set_ylim(20, 100)
    ax.set_xticks(ep)
    ax.set_xlabel("epoch")
    ax.set_ylabel("training evenings right (%)")
    ax.legend(loc="center right", fontsize=10)
    style.save(fig, "viz_perceptron_percent")


# ------------------------------------------- Lecture 11: the XOR network
def _xor_strip():
    lim = (-0.7, 1.7)
    fig, ax = style.new_fig(4.7, 4.6)
    g1, g2 = np.meshgrid(np.linspace(*lim, 200), np.linspace(*lim, 200))
    ax.contourf(g1, g2, g1 + g2, levels=[0.5, 1.5], colors=[C1], alpha=0.12)
    _gate_boundary(ax, (1.0, 1.0), -0.5, lim, color=PINK, lw=2.2, label="$x_1 + x_2 = 0.5$")
    _gate_boundary(ax, (1.0, 1.0), -1.5, lim, color=GREEN, lw=2.2, label="$x_1 + x_2 = 1.5$")
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
    _gate_frame(ax, lim)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_title("The inputs $(x_1, x_2)$")
    ax = axes[1]
    H = (np.array(GATE) @ np.array([[1, 1], [1, 1]]).T + np.array([-0.5, -1.5]) > 0).astype(int)
    w, b = (1.0, -1.0), -0.5
    _gate_shade(ax, w, b, lim)
    _gate_boundary(ax, w, b, lim, color=LINE, lw=2.2)
    seen = {}
    for (h1, h2), t, x in zip(H, XOR, GATE):
        seen.setdefault((h1, h2, t), []).append(f"({x[0]}, {x[1]})")
    for (h1, h2, t), names in seen.items():
        ax.plot(h1, h2, "^" if t else "o", ms=12 if t else 11, color=C1 if t else C0,
                mec="none", zorder=5)
        below = (h1, h2) == (1, 0)
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
    "viz_perceptron_evenings": _evenings_fig,
    "viz_perceptron_threshold": _threshold_fig,
    "viz_perceptron_unit": _unit,
    "viz_perceptron_gates": _gates,
    "viz_perceptron_and_run": _and_run,
    "viz_perceptron_rule_evenings": _rule_evenings,
    "viz_perceptron_step_loss": _step_loss,
    "viz_perceptron_sigmoid": _sigmoid,
    "viz_perceptron_cross_entropy": _cross_entropy,
    "viz_perceptron_training": _training,
    "viz_perceptron_bowl": _bowl,
    "viz_perceptron_probability": _probability,
    "viz_perceptron_test": _test_fig,
    "viz_perceptron_xor_lines": _xor_lines,
    # For the Curious
    "viz_perceptron_proof": _proof,
    "viz_perceptron_line": _line,
    "viz_perceptron_wb": _wb,
    "viz_perceptron_sigmoid_slope": _sigmoid_slope,
    "viz_perceptron_posterior": _posterior,
    "viz_perceptron_percent": _percent,
    # Lecture 11
    "viz_perceptron_xor_strip": _xor_strip,
    "viz_perceptron_xor_hidden": _xor_hidden,
    "viz_perceptron_network": _network,
}


if __name__ == "__main__":
    report()
