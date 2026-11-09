"""Figures and numbers for Lecture 11, From Neurons to Language Models.

Every number on the slides of Lecture 11, on its workbook page and on the page
of Seminar 11 comes from the functions in the first half of this file, in
plain Python (no NumPy). Print them all with

    python figures/src/language.py

The second half draws lectures/content/public/figures/viz_language_*.svg:

    python figures/src/build.py --only language

The numbers:

  * XOR: a 2-2-1 network of step neurons with the weights set by hand
    (h1 = OR: 1, 1, -0.5; h2 = AND: 1, 1, -1.5; output: 1, -1, -0.5), and the
    same shape with sigmoid units, trained by gradient descent from the
    weights that random.Random(0) draws.
  * The tiny network x -> h -> yhat on one evening of the weather log:
    12 April 2025, 18:00, 2.0 C, and frost at 06:00 the next morning (-3.8 C).
  * The text: one sentence per month, "in july it was warm .", the word from
    the month's mean temperature (below 0 C cold, below 10 C cool, below 15 C
    mild, else warm). Twelve sentences from the ten-year mean of each month
    (the lecture's text, data/processed/months.txt of Seminar 11); 120 from
    each month of 2016-2025 (the vectors; data/processed/months_by_year.txt).
  * Softmax of the three scores (2.0, 1.0, 0.1) at T = 0.5, 1 and 2.
  * Attention on "july it was": scores (3, 0, 0), the vectors from the text.
"""
import math
import random
from functools import lru_cache

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

import style

LOG = style.ROOT / "lectures" / "workbook" / "docs" / "data" / "weather.csv"

C1 = style.ACCENT        # class 1, the forward values
C0 = style.CYCLE[1]      # class 0, the backward values
GREEN = style.CYCLE[2]
PINK = style.CYCLE[3]
VIOLET = style.CYCLE[4]
FG = style.FG
DIM = style.DIM

NAMES = ["january", "february", "march", "april", "may", "june", "july",
         "august", "september", "october", "november", "december"]
WORDS = ["cold", "cool", "mild", "warm"]


# =============================================================================
# Numbers
# =============================================================================

def sigma(z):
    return 1 / (1 + math.exp(-z))


def step(z):
    return 1 if z > 0 else 0


# ------------------------------------------------------------------ XOR
GATE = [(0, 0), (0, 1), (1, 0), (1, 1)]
XOR = [0, 1, 1, 0]


def xor_by_hand():
    """The four inputs through the hand-set network: rows of
    (x1, x2, z1, h1, z2, h2, z, yhat)."""
    rows = []
    for x1, x2 in GATE:
        z1 = x1 + x2 - 0.5
        z2 = x1 + x2 - 1.5
        h1, h2 = step(z1), step(z2)
        z = h1 - h2 - 0.5
        rows.append((x1, x2, z1, h1, z2, h2, z, step(z)))
    return rows


def xor_linear():
    """The hand-set network without the step in the hidden layer: one line."""
    # z = 1 * (x1 + x2 - 0.5) - 1 * (x1 + x2 - 1.5) - 0.5 = 0 x1 + 0 x2 + 0.5
    w1 = 1 * 1 + (-1) * 1
    w2 = 1 * 1 + (-1) * 1
    b = 1 * (-0.5) + (-1) * (-1.5) - 0.5
    return w1, w2, b


@lru_cache(maxsize=None)
def xor_trained(seed=0, eta=2.0, steps=2000):
    """A 2-2-1 network of sigmoid units trained on the four XOR points by
    gradient descent on the mean cross-entropy, all four points per step.
    Returns (history, weights): history[k] = (mean loss, four outputs) before
    step k; weights = (V, c, w, b) at the end."""
    r = random.Random(seed)
    V = [[r.uniform(-1, 1), r.uniform(-1, 1)] for _ in range(2)]
    c = [r.uniform(-1, 1) for _ in range(2)]
    w = [r.uniform(-1, 1) for _ in range(2)]
    b = r.uniform(-1, 1)
    start = ([row[:] for row in V], c[:], w[:], b)
    history = []
    for k in range(steps + 1):
        gV = [[0.0, 0.0], [0.0, 0.0]]
        gc = [0.0, 0.0]
        gw = [0.0, 0.0]
        gb = 0.0
        L = 0.0
        outs = []
        for (x1, x2), y in zip(GATE, XOR):
            h = [sigma(V[j][0] * x1 + V[j][1] * x2 + c[j]) for j in range(2)]
            yh = sigma(w[0] * h[0] + w[1] * h[1] + b)
            outs.append(yh)
            L += -(y * math.log(yh) + (1 - y) * math.log(1 - yh))
            d = yh - y
            gb += d
            for j in range(2):
                gw[j] += d * h[j]
                dj = d * w[j] * h[j] * (1 - h[j])
                gV[j][0] += dj * x1
                gV[j][1] += dj * x2
                gc[j] += dj
        history.append((L / 4, tuple(outs)))
        if k == steps:
            break
        for j in range(2):
            w[j] -= eta * gw[j] / 4
            c[j] -= eta * gc[j] / 4
            V[j][0] -= eta * gV[j][0] / 4
            V[j][1] -= eta * gV[j][1] / 4
        b -= eta * gb / 4
    return history, start, (V, c, w, b)


def xor_starts(n=12):
    """How many of the starts random.Random(0..n-1) learn XOR in 2000 steps."""
    ok = 0
    for seed in range(n):
        outs = xor_trained(seed)[0][-1][1]
        ok += all((o > 0.5) == bool(y) for o, y in zip(outs, XOR))
    return ok, n


# ------------------------------------------------------- the tiny network
EVENING = "2025-04-12T18:00"
MORNING = "2025-04-13T06:00"
TINY = {"v": -1.0, "c": 1.0, "w": 2.0, "b": -1.0}
ETA = 1.0


@lru_cache(maxsize=None)
def _log():
    """{time: temperature} of every hour of weather.csv."""
    out = {}
    for line in _lines():
        parts = line.split(",")
        out[parts[0]] = float(parts[1])
    return out


def evening():
    x = _log()[EVENING]
    y = 1 if _log()[MORNING] < 0 else 0
    return x, y, _log()[MORNING]


def frost_counts():
    """Evenings at 18:00 with a measured temperature at 06:00 the next
    morning, and how many of them were followed by frost."""
    log = _log()
    times = sorted(t for t in log if t.endswith("T18:00"))
    n = frost = 0
    for t in times:
        day = t[:10]
        y, m, d = (int(s) for s in day.split("-"))
        nxt = _next_day(y, m, d)
        key = f"{nxt}T06:00"
        if key in log and log[t] != -999 and log[key] != -999:
            n += 1
            frost += log[key] < 0
    return n, frost


def _next_day(y, m, d):
    days = [31, 29 if y % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d += 1
    if d > days[m - 1]:
        d, m = 1, m + 1
        if m > 12:
            m, y = 1, y + 1
    return f"{y:04d}-{m:02d}-{d:02d}"


def tiny_forward(v, c, w, b, x, y):
    u = v * x + c
    h = sigma(u)
    z = w * h + b
    yh = sigma(z)
    L = -(y * math.log(yh) + (1 - y) * math.log(1 - yh))
    return {"u": u, "h": h, "z": z, "yh": yh, "L": L}


def tiny_step():
    """Forward, backward, the nudge check, one step and the forward again."""
    x, y, _ = evening()
    p = dict(TINY)
    f = tiny_forward(p["v"], p["c"], p["w"], p["b"], x, y)
    d = f["yh"] - y                     # dL/dz
    g = {"w": d * f["h"], "b": d}
    dh = d * p["w"]                     # dL/dh
    slope = f["h"] * (1 - f["h"])       # dh/du
    du = dh * slope                     # dL/du
    g["v"] = du * x
    g["c"] = du
    eps = 0.001
    lp = tiny_forward(p["v"] + eps, p["c"], p["w"], p["b"], x, y)["L"]
    lm = tiny_forward(p["v"] - eps, p["c"], p["w"], p["b"], x, y)["L"]
    new = {k: p[k] - ETA * g[k] for k in p}
    f2 = tiny_forward(new["v"], new["c"], new["w"], new["b"], x, y)
    return {"x": x, "y": y, "fwd": f, "delta": d, "dh": dh, "slope": slope,
            "du": du, "grad": g, "nudge": (lp, lm, (lp - lm) / (2 * eps)),
            "new": new, "fwd2": f2}


# ------------------------------------------------------------------ the text
def word_for(temp):
    """The word of a month's mean temperature (as scripts/sentences.py)."""
    if temp < 0:
        return "cold"
    if temp < 10:
        return "cool"
    if temp < 15:
        return "mild"
    return "warm"


@lru_cache(maxsize=None)
def _lines():
    return tuple(LOG.read_text().splitlines()[1:])


@lru_cache(maxsize=None)
def _groups(start, stop):
    """weather.group of Seminar 7: {line[start:stop]: [temperatures]}."""
    groups = {}
    for line in _lines():
        temp = float(line.split(",")[1])
        if temp == -999:
            continue
        groups.setdefault(line[start:stop], []).append(temp)
    return groups


@lru_cache(maxsize=None)
def sentences(by_year=False):
    """One sentence per month: the twelve months of the ten-year means, or
    the 120 months of 2016-2025."""
    out = []
    for key, temps in _groups(0, 7).items() if by_year else _groups(5, 7).items():
        name = NAMES[int(key[-2:]) - 1]
        out.append(f"in {name} it was {word_for(sum(temps) / len(temps))} .")
    return tuple(out)


@lru_cache(maxsize=None)
def _month_means():
    return tuple((NAMES[int(k) - 1], sum(v) / len(v)) for k, v in _groups(5, 7).items())


def month_means():
    return dict(_month_means())


def words(by_year=False):
    return " ".join(sentences(by_year)).split()


def vocabulary():
    """{word: id}, ids in the order of first appearance in the text."""
    ids = {}
    for word in words():
        if word not in ids:
            ids[word] = len(ids)
    return ids


def follow(by_year=False):
    """{word: [every word that comes right after it in the text]}, as the
    runner block and the seminar build it."""
    ws = words(by_year)
    out = {}
    for i in range(len(ws) - 1):
        if ws[i] not in out:
            out[ws[i]] = []
        out[ws[i]].append(ws[i + 1])
    return out


def next_word(word, by_year=False):
    """{next word: (count, probability)} after `word`, in order of WORDS when
    the followers are weather words."""
    after = follow(by_year)[word]
    keys = WORDS if set(after) <= set(WORDS) else sorted(set(after), key=after.index)
    return {k: (after.count(k), after.count(k) / len(after)) for k in keys}


def generate(seed, n=5):
    """The runner block "Generating Text": a month after "in", a word after
    "was"; random.seed(seed)."""
    after_was = follow()["was"]
    random.seed(seed)
    out = []
    for _ in range(n):
        month = random.choice(NAMES)
        word = random.choice(after_was)
        out.append((month, word))
    return out


def true_word(month):
    return word_for(month_means()[month])


def p_true():
    """Probability that a sentence drawn from "in" is one of the twelve."""
    probs = next_word("was")
    return sum(probs[true_word(m)][1] for m in NAMES) / 12


def draw_many(seed=1, n=10000):
    """n sentences drawn as in generate(): how many are true."""
    after_was = follow()["was"]
    rnd = random.Random(seed)
    ok = 0
    for _ in range(n):
        month = rnd.choice(NAMES)
        ok += rnd.choice(after_was) == true_word(month)
    return ok, n


def month_hits(seed=1, n=10000):
    """The draws of draw_many(), per month: {month: share of its sentences
    that were true}."""
    after_was = follow()["was"]
    rnd = random.Random(seed)
    drawn = {m: 0 for m in NAMES}
    right = {m: 0 for m in NAMES}
    for _ in range(n):
        month = rnd.choice(NAMES)
        drawn[month] += 1
        right[month] += rnd.choice(after_was) == true_word(month)
    return {m: round(right[m] / drawn[m], 3) for m in NAMES}


def contexts(vocab, n):
    return vocab ** n


# ------------------------------------------------------------- the vectors
def month_vectors():
    """For each month, how often each weather word comes with it in the 120
    sentences of 2016-2025: {month: [cold, cool, mild, warm]}."""
    out = {m: [0, 0, 0, 0] for m in NAMES}
    for s in sentences(by_year=True):
        parts = s.split()
        out[parts[1]][WORDS.index(parts[4])] += 1
    return out


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def length(a):
    return math.sqrt(dot(a, a))


def cosine(a, b):
    return dot(a, b) / (length(a) * length(b))


# ------------------------------------------------------------- softmax
SCORES = [2.0, 1.0, 0.1]
SCORE_WORDS = ["warm", "mild", "cool"]


def softmax(zs, T=1.0):
    e = [math.exp(z / T) for z in zs]
    s = sum(e)
    return [x / s for x in e], e, s


def draws(seed=1, k=10):
    """k words drawn at T = 0.5, then k at T = 2, by random.Random(seed)."""
    r = random.Random(seed)
    low = r.choices(SCORE_WORDS, weights=softmax(SCORES, 0.5)[0], k=k)
    high = r.choices(SCORE_WORDS, weights=softmax(SCORES, 2.0)[0], k=k)
    return low, high


def merges(n=8):
    """A vocabulary of pieces built by counting, on the twelve sentences: the
    words as letters, then n times the most frequent pair of neighbouring
    symbols merged into one (ties: the pair seen first). Returns the merges
    as (left, right, count) and the words in pieces at the end."""
    freq = {}
    for w in words():
        freq[w] = freq.get(w, 0) + 1
    pieces = {w: list(w) for w in freq}
    done = []
    for _ in range(n):
        pairs = {}
        for w, count in freq.items():
            s = pieces[w]
            for a, b in zip(s, s[1:]):
                pairs[(a, b)] = pairs.get((a, b), 0) + count
        (a, b), count = max(pairs.items(), key=lambda kv: kv[1])
        done.append((a, b, count))
        for w in pieces:
            s, out, i = pieces[w], [], 0
            while i < len(s):
                if i + 1 < len(s) and (s[i], s[i + 1]) == (a, b):
                    out.append(a + b)
                    i += 2
                else:
                    out.append(s[i])
                    i += 1
            pieces[w] = out
    return done, pieces


# ------------------------------------------------------------ attention
ATT_WORDS = ["july", "it", "was"]
ATT_SCORES = [3.0, 0.0, 0.0]
ATT_Q = (3.0, 0.0)
ATT_K = {"july": (1.0, 0.0), "it": (0.0, 1.0), "was": (0.0, 1.0)}


def att_vectors():
    """What each word says about the weather word that follows "was" in the
    twelve sentences: july always comes with warm; "it" and "was" stand in
    every sentence, so they carry the row of "was"."""
    row = [p for _, p in next_word("was").values()]
    jul = [0.0, 0.0, 0.0, 0.0]
    jul[WORDS.index(true_word("july"))] = 1.0
    return {"july": jul, "it": row, "was": row}


def attention():
    weights, e, s = softmax(ATT_SCORES)
    vecs = att_vectors()
    ctx = [sum(wt * vecs[word][k] for wt, word in zip(weights, ATT_WORDS)) for k in range(4)]
    return weights, e, s, ctx


def text_loss():
    """Mean -ln p of the weather word of each of the twelve sentences: the
    model that sees "was" only, and attention that puts 0.909 on the month."""
    row = next_word("was")
    weights = attention()[0]
    big, att = [], []
    for m in NAMES:
        t = true_word(m)
        big.append(-math.log(row[t][1]))
        # the month's own vector is all on its word; it and was carry the row
        att.append(-math.log(weights[0] * 1.0 + (weights[1] + weights[2]) * row[t][1]))
    return sum(big) / 12, sum(att) / 12


# ----------------------------------------------------------- the sizes
SIZES = [("the tiny network, this lecture", 4), ("XOR, this lecture", 9),
         ("GPT-2, 2019", 1.5e9), ("GPT-3, 2020", 1.75e11)]


def numbers():
    """Print every number that the slides and pages state."""
    print("== XOR by hand: x1 x2 | z1 h1 | z2 h2 | z yhat")
    for row in xor_by_hand():
        print("  ", row)
    print("   without the step in the hidden layer: w1, w2, b =", xor_linear())
    hist, start, end = xor_trained()
    print("== XOR trained, Random(0), eta 2, 2000 steps")
    V, c, w, b = start
    print("   start V", [[round(a, 3) for a in r] for r in V], "c", [round(a, 3) for a in c],
          "w", [round(a, 3) for a in w], "b", round(b, 3))
    for k in (0, 100, 300, 500, 1000, 2000):
        L, outs = hist[k]
        print(f"   step {k:5d}: loss {L:.4f}  outputs {[round(o, 3) for o in outs]}")
    first = next(k for k, (_, o) in enumerate(hist)
                 if all((p > 0.5) == bool(t) for p, t in zip(o, XOR)))
    print("   all four on the right side of 0.5 from step", first)
    V, c, w, b = end
    print("   end V", [[round(a, 2) for a in r] for r in V], "c", [round(a, 2) for a in c],
          "w", [round(a, 2) for a in w], "b", round(b, 2))
    for j in range(2):
        print(f"   trained h{j + 1} on the four inputs:",
              [round(sigma(V[j][0] * x1 + V[j][1] * x2 + c[j]), 3) for x1, x2 in GATE])
    print("   starts that learn XOR (of 12):", xor_starts())
    for seed in range(12):
        L, outs = xor_trained(seed)[0][-1]
        print(f"     start {seed:2d}: loss {L:.3f}  outputs {[round(o, 3) for o in outs]}")
    print("   sigmoid: z, sigma, slope", [(z, round(sigma(z), 3), round(sigma(z) * (1 - sigma(z)), 3))
                                       for z in (-1, 0, 2)])

    print("== frost evenings:", frost_counts())
    t = tiny_step()
    f, g = t["fwd"], t["grad"]
    print(f"== tiny network, {EVENING}: x = {t['x']}, morning {evening()[2]}, y = {t['y']}")
    print("   weights", TINY, "eta", ETA)
    print(f"   u = {f['u']:.4f}  h = {f['h']:.4f}  z = {f['z']:.4f}  yhat = {f['yh']:.4f}  L = {f['L']:.4f}")
    print(f"   delta = {t['delta']:.4f}  dL/dw = {g['w']:.4f}  dL/db = {g['b']:.4f}")
    print(f"   dL/dh = {t['dh']:.4f}  h(1-h) = {t['slope']:.4f}  dL/du = {t['du']:.4f}"
          f"  dL/dv = {g['v']:.4f}  dL/dc = {g['c']:.4f}")
    lp, lm, sl = t["nudge"]
    print(f"   nudge v: L(v+0.001) = {lp:.7f}  L(v-0.001) = {lm:.7f}  slope = {sl:.4f}")
    n, f2 = t["new"], t["fwd2"]
    print("   after one step:", {k: round(val, 4) for k, val in n.items()})
    print(f"   u = {f2['u']:.4f}  h = {f2['h']:.4f}  z = {f2['z']:.4f}  yhat = {f2['yh']:.4f}  L = {f2['L']:.4f}")
    print("== chain rule example: f = a^2, a = 3t + 1, t = 1:", 2 * 4 * 3,
          " nudge", ((3 * 1.001 + 1) ** 2 - 16) / 0.001)

    print("== the text, twelve sentences:")
    for s in sentences():
        print("  ", s)
    print("   month means:", {m: round(v, 2) for m, v in month_means().items()})
    ws = words()
    print("   words", len(ws), "vocabulary", len(vocabulary()))
    print("   ids", vocabulary())
    print("   'in july it was warm .' ->", [vocabulary()[w_] for w_ in "in july it was warm .".split()])
    for word in ("in", "it", "was", "."):
        print(f"   after {word!r}:", next_word(word))
    print("   follow['was'] =", follow()["was"])
    for seed in (3,):
        print(f"   generate(seed={seed}):", generate(seed))
        print("     true:", [w_ == true_word(m) for m, w_ in generate(seed)])
    print("   P(true sentence) =", p_true(), "=", round(p_true() * 144), "/ 144")
    print("   10 000 draws:", draw_many())
    print("   contexts: 20^2 =", contexts(20, 2), " 20^3 =", contexts(20, 3),
          " 50000^10 = %.2e" % contexts(50000, 10))

    print("== 120 sentences:", len(sentences(True)), "first", sentences(True)[:2],
          "last", sentences(True)[-1])
    print("   after 'was':", next_word("was", True))
    mv = month_vectors()
    for m in NAMES:
        print(f"   {m:10s} {mv[m]}  length {length(mv[m]):.3f}")
    for a, b_ in (("january", "february"), ("january", "december"), ("january", "march"),
                  ("january", "july"), ("march", "april"), ("may", "september"),
                  ("july", "august"), ("april", "october")):
        print(f"   {a}.{b_}: dot {dot(mv[a], mv[b_])}  cos {cosine(mv[a], mv[b_]):.3f}")

    print("== softmax of", SCORES, "for", SCORE_WORDS)
    for T in (1.0, 0.5, 2.0):
        p, e, s = softmax(SCORES, T)
        print(f"   T = {T}: z/T {[round(z / T, 2) for z in SCORES]}  e {[round(x, 3) for x in e]}"
              f"  sum {s:.3f}  p {[round(x, 3) for x in p]}")
    p2 = softmax([2.0, 0.0])[0]
    print("   two scores (2, 0):", [round(x, 4) for x in p2], " sigma(2) =", round(sigma(2.0), 4))
    low, high = draws()
    print("   ten draws at T = 0.5:", " ".join(low), f"({low.count('warm')} warm)")
    print("   ten draws at T = 2:  ", " ".join(high), f"({high.count('warm')} warm)")
    done, pieces = merges()
    print("== merges on the twelve sentences:", [(a + " + " + b, n) for a, b, n in done])
    print("   pieces:", {w: "·".join(pieces[w]) for w in
                         ("in", "it", "was", "cool", "warm", "january", "september")})
    print("== P(the right word) per month:", {m: round(next_word("was")[true_word(m)][1], 3)
                                            for m in NAMES})
    print("   in 10 000 draws, right per month:", month_hits())

    w_, e, s, ctx = attention()
    print("== attention on", ATT_WORDS, "scores", ATT_SCORES, "q", ATT_Q, "k", ATT_K)
    print("   e", [round(x, 3) for x in e], "sum", round(s, 3), "weights", [round(x, 3) for x in w_])
    print("   vectors", {k: [round(x, 3) for x in val] for k, val in att_vectors().items()})
    print("   weighted average", [round(x, 3) for x in ctx], "sum", round(sum(ctx), 6))
    big, att = text_loss()
    print(f"== loss on the weather words: one word {big:.3f}, attention {att:.3f}")
    print("   -ln 0.25 =", round(-math.log(0.25), 3), " -ln 0.932 =", round(-math.log(ctx[3]), 3))
    print("== the six hours of 21 July 2019:", repr(sum([27.3, 25.6, 24.6, 23.6]) / 4),
          " round:", round(sum([27.3, 25.6, 24.6, 23.6]) / 4, 3))
    below = sum(1 for line in _lines() if -999 < float(line.split(",")[1]) < 0)
    print("== hours below 0 C:", below, "of", sum(len(v) for v in _groups(0, 4).values()))
    print("== attention scores as dot products: q", ATT_Q,
          {k: dot(ATT_Q, kv) for k, kv in ATT_K.items()})


# =============================================================================
# Figures
# =============================================================================

def _arrow(ax, p, q, color=DIM, lw=1.8, ms=14, zorder=4, rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=ms, lw=lw,
                                 color=color, zorder=zorder, shrinkA=0, shrinkB=0,
                                 connectionstyle=f"arc3,rad={rad}"))


def _blank(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.grid(False)


def _box(ax, x, y, w, h, text, color=FG, size=13, fc="none", lw=1.8, tcolor=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                fc=fc, ec=color, lw=lw, zorder=3))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size,
            color=tcolor or FG, zorder=5)


def _points(ax, ms=13):
    for (x1, x2), t in zip(GATE, XOR):
        ax.plot(x1, x2, "^" if t else "o", ms=ms + (1 if t else 0), color=C1 if t else C0,
                mec="none", zorder=5)


def _line(ax, w1, w2, b, lim, **kw):
    """The line w1 x1 + w2 x2 + b = 0 across lim (w2 != 0)."""
    xs = [lim[0], lim[1]]
    ax.plot(xs, [-(w1 * x + b) / w2 for x in xs], **kw)




def _m(x, fmt=".3f"):
    """A number with a true minus sign, as on the slides."""
    return format(x, fmt).replace("-", "−")


def _xor_strip():
    lim = (-0.6, 1.6)
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    xs = [lim[0], lim[1]]
    ax.fill_between(xs, [0.5 - x for x in xs], [1.5 - x for x in xs], color=C1, alpha=0.10,
                    lw=0)
    _line(ax, 1, 1, -0.5, lim, color=PINK, lw=2.2, label="$h_1$, OR: $x_1 + x_2 = 0.5$")
    _line(ax, 1, 1, -1.5, lim, color=GREEN, lw=2.2, label="$h_2$, AND: $x_1 + x_2 = 1.5$")
    for (x1, x2), t in zip(GATE, XOR):
        ax.plot(x1, x2, "^" if t else "o", ms=14 if t else 13, color=C1 if t else C0,
                mec="none", zorder=5)
        ax.text(x1 + 0.07, x2 + 0.07, f"({x1}, {x2})", color=FG, fontsize=10.5)
    ax.plot([], [], "^", ms=11, color=C1, mec="none", label="XOR = 1")
    ax.plot([], [], "o", ms=10, color=C0, mec="none", label="XOR = 0")
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_aspect("equal")
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.legend(loc="center left", bbox_to_anchor=(1.03, 0.5), fontsize=10.5,
              labelspacing=1.1, handlelength=1.6)
    style.save(fig, "viz_language_xor_strip")


def _neuron(ax, x, y, r, label, color, size=15):
    ax.add_patch(Circle((x, y), r, fc="none", ec=color, lw=2.2, zorder=3))
    ax.text(x, y, label, ha="center", va="center", fontsize=size, color=FG, zorder=5)


def _xor_network():
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    _blank(ax, (0, 11.6), (-0.15, 4.65))
    xin = [(1.0, 3.1, "$x_1$"), (1.0, 1.0, "$x_2$")]
    hid = [(5.0, 3.1, "$h_1$", "OR", "−0.5", PINK),
           (5.0, 1.0, "$h_2$", "AND", "−1.5", GREEN)]
    out = (9.0, 2.05)
    for x, y, lab in xin:
        _neuron(ax, x, y, 0.42, lab, C1)
    for x, y, lab, name, bias, col in hid:
        _neuron(ax, x, y, 0.52, lab, col)
        dy = 0.8 if y > 2 else -0.8
        ax.text(x, y + dy, f"{name}, bias {bias}", ha="center", va="center", fontsize=12,
                color=col)
    _neuron(ax, *out, 0.52, r"$\hat{y}$", FG, size=17)
    ax.text(out[0], out[1] - 0.84, "bias −0.5", ha="center", va="center", fontsize=12,
            color=FG)
    for x, y, _ in xin:
        for hx, hy, *_ in hid:
            dy = 0 if hy == y else (0.14 if hy > y else -0.14)
            p = (x + 0.44, y + dy)
            q = (hx - 0.55, hy - dy)
            _arrow(ax, p, q, lw=1.5)
            t = 0.28 if hy == y else 0.24
            mx, my = p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])
            ax.text(mx, my + (0.16 if hy == y else 0.0), "1", color=C0, fontsize=13,
                    ha="center", va="bottom" if hy == y else "center",
                    bbox=dict(fc="#0b0e14", ec="none", pad=1.5) if hy != y else None)
    for hx, hy, *_ in hid:
        p = (hx + 0.55, hy + (-0.12 if hy > 2 else 0.12))
        q = (out[0] - 0.54, out[1] + (0.2 if hy > 2 else -0.2))
        _arrow(ax, p, q, lw=1.5)
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        ax.text(mx, my + (0.26 if hy > 2 else -0.3), "1" if hy > 2 else "−1", color=C0,
                fontsize=13, ha="center", va="center")
    _arrow(ax, (out[0] + 0.55, out[1]), (out[0] + 1.6, out[1]), lw=1.5)
    ax.text(out[0] + 1.75, out[1], "XOR", ha="left", va="center", fontsize=13, color=FG)
    ax.text(1.0, 4.4, "inputs", ha="center", color=DIM, fontsize=11.5)
    ax.text(5.0, 4.4, "hidden layer: two step neurons", ha="center", color=DIM, fontsize=11.5)
    ax.text(9.0, 3.0, "output: a step neuron", ha="center", color=DIM, fontsize=11.5)
    style.save(fig, "viz_language_xor_network")


def _xor_hidden():
    lim = (-0.6, 1.6)
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.6))
    ax = axes[0]
    _points(ax, ms=12)
    for x1, x2 in GATE:
        ax.text(x1 + 0.08, x2 + 0.08, f"({x1}, {x2})", color=FG, fontsize=10)
    ax.set_title("The inputs $(x_1, x_2)$: no line separates", fontsize=12.5)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax = axes[1]
    xs = [lim[0], lim[1]]
    ax.fill_between(xs, [x - 0.5 for x in xs], [lim[0]] * 2, color=C1, alpha=0.10, lw=0)
    _line(ax, 1, -1, -0.5, lim, color=FG, lw=2.0)
    seen = {}
    for row, t in zip(xor_by_hand(), XOR):
        x1, x2, _, h1, _, h2, _, _ = row
        seen.setdefault((h1, h2, t), []).append(f"({x1}, {x2})")
    for (h1, h2, t), names in seen.items():
        ax.plot(h1, h2, "^" if t else "o", ms=13 if t else 12, color=C1 if t else C0,
                mec="none", zorder=5)
        below = (h1, h2) == (1, 0)
        ax.text(h1 + (0.0 if below else 0.08), h2 - 0.2 if below else h2 + 0.08,
                "from " + " and ".join(names), color=FG, fontsize=10,
                ha="center" if below else "left", va="top" if below else "bottom")
    ax.text(1.38, 0.6, "$h_1 - h_2 = 0.5$", color=FG, fontsize=10.5, rotation=45,
            ha="center", va="center")
    ax.set_title("The hidden outputs $(h_1, h_2)$: one line does", fontsize=12.5)
    ax.set_xlabel("$h_1$")
    ax.set_ylabel("$h_2$")
    for ax in axes:
        ax.set_xlim(*lim)
        ax.set_ylim(*lim)
        ax.set_aspect("equal")
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
    style.save(fig, "viz_language_xor_hidden")


def _tiny_forward():
    t = tiny_step()
    f = t["fwd"]
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    _blank(ax, (0, 14.2), (0.6, 5.0))
    y0 = 2.5
    xs = {"x": 0.9, "h": 5.0, "yh": 9.1, "L": 12.9}
    _neuron(ax, xs["x"], y0, 0.48, "$x$", C1)
    _neuron(ax, xs["h"], y0, 0.6, "$h$", PINK)
    _neuron(ax, xs["yh"], y0, 0.6, r"$\hat{y}$", GREEN, size=17)
    _box(ax, xs["L"] - 0.7, y0 - 0.45, 1.4, 0.9, "loss", color=FG, size=14)
    _arrow(ax, (xs["x"] + 0.5, y0), (xs["h"] - 0.63, y0), lw=1.6)
    _arrow(ax, (xs["h"] + 0.63, y0), (xs["yh"] - 0.63, y0), lw=1.6)
    _arrow(ax, (xs["yh"] + 0.63, y0), (xs["L"] - 0.66, y0), lw=1.6)
    ax.text((xs["x"] + xs["h"]) / 2, y0 + 0.18, "$u = vx + c$\n$h = \\mathrm{sigmoid}(u)$",
            ha="center", va="bottom", fontsize=12, color=DIM)
    ax.text((xs["h"] + xs["yh"]) / 2, y0 + 0.18, "$z = wh + b$\n$\\hat{y} = \\mathrm{sigmoid}(z)$",
            ha="center", va="bottom", fontsize=12, color=DIM)
    ax.text((xs["yh"] + xs["L"]) / 2, y0 + 0.18, "loss $= -\\ln \\hat{y}$",
            ha="center", va="bottom", fontsize=12, color=DIM)
    ax.text((xs["x"] + xs["h"]) / 2, y0 - 0.32, "$v = -1$,  $c = 1$", ha="center",
            va="top", fontsize=12, color=PINK)
    ax.text((xs["h"] + xs["yh"]) / 2, y0 - 0.32, "$w = 2$,  $b = -1$", ha="center",
            va="top", fontsize=12, color=GREEN)
    top = 4.35
    ax.text(xs["x"], top, f"{t['x']:.1f} °C", ha="center", fontsize=14, color=C1)
    ax.text(xs["h"], top, f"$u$ = {_m(f['u'], '.1f')},  $h$ = {_m(f['h'])}", ha="center",
            fontsize=13, color=C1)
    ax.text(xs["yh"], top, f"$z$ = {_m(f['z'])},  $\\hat{{y}}$ = {_m(f['yh'])}",
            ha="center", fontsize=13, color=C1)
    ax.text(xs["L"], top, _m(f["L"]), ha="center", fontsize=14, color=C1)
    ax.text(xs["x"], 1.35, "18:00", ha="center", fontsize=11.5, color=DIM)
    ax.text(xs["yh"], 1.35, "frost by 06:00?\n$y = 1$", ha="center", va="center",
            fontsize=11.5, color=DIM, linespacing=1.5)
    style.save(fig, "viz_language_tiny_forward")


def _xor_training():
    hist, _, _ = xor_trained()
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3), gridspec_kw={"width_ratios": [1.3, 1]})
    ax = axes[0]
    ks = list(range(len(hist)))
    ax.plot(ks, [h[0] for h in hist], color=C1, lw=2)
    ax.set_xlabel("step of gradient descent")
    ax.set_ylabel("mean loss of the four points")
    ax.set_ylim(0, 0.75)
    ax.set_xlim(0, len(hist) - 1)
    ax.set_title(f"From {hist[0][0]:.3f} to {hist[-1][0]:.3f}", fontsize=13)
    ax = axes[1]
    labels = ["(0, 0)", "(0, 1)", "(1, 0)", "(1, 1)"]
    for i, k in enumerate((0, 300, 2000)):
        outs = hist[k][1]
        xs = [j + (i - 1) * 0.26 for j in range(4)]
        ax.bar(xs, outs, width=0.24, color=[DIM, VIOLET, C1][i], label=f"step {k}")
    for j, t in enumerate(XOR):
        ax.plot([j - 0.42, j + 0.42], [t, t], color=FG, lw=1.2, ls=(0, (3, 2)))
    ax.set_xticks(range(4))
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1.12)
    ax.set_ylabel(r"output $\hat{y}$")
    ax.set_title("The four outputs; dashed: XOR", fontsize=13)
    ax.legend(loc="upper center", ncol=3, fontsize=9.5, bbox_to_anchor=(0.5, -0.17))
    style.save(fig, "viz_language_xor_training")


def _xor_starts():
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    stuck = 0
    for seed in range(12):
        hist = xor_trained(seed)[0]
        ok = all((o > 0.5) == bool(t) for o, t in zip(hist[-1][1], XOR))
        stuck += not ok
        ax.plot(range(len(hist)), [h[0] for h in hist], color=C1 if ok else C0,
                lw=1.6 if ok else 2.2, alpha=0.75 if ok else 1.0, zorder=3 if ok else 4)
    ax.set_xlim(0, 2000)
    ax.set_ylim(0, 0.9)
    ax.set_xlabel("step of gradient descent")
    ax.set_ylabel("mean loss of the four points")
    ax.plot([], [], color=C1, lw=1.8, label=f"{12 - stuck} starts: XOR learned")
    ax.plot([], [], color=C0, lw=2.2, label=f"{stuck} starts: stuck on a plateau")
    ax.legend(loc="upper right", fontsize=10.5)
    style.save(fig, "viz_language_xor_starts")


def _bars(ax, labels, values, colors, fmt="{:.3f}", top=None, size=12):
    ax.bar(range(len(values)), values, color=colors, width=0.62)
    for i, v in enumerate(values):
        ax.text(i, v + (top or max(values)) * 0.025, fmt.format(v), ha="center", va="bottom",
                fontsize=size, color=FG)
    ax.set_xticks(range(len(values)))
    ax.set_xticklabels(labels)
    ax.set_ylim(0, (top or max(values)) * 1.18)


def _next_word():
    row = next_word("was")
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    vals = [p for _, p in row.values()]
    _bars(ax, [f"{k}\n{n} of 12" for k, (n, _) in row.items()], vals, [C1] * 4, top=0.4)
    ax.set_ylabel("probability of the next word")
    style.save(fig, "viz_language_next_word")


def _tree():
    """The steps of one sentence and their probabilities."""
    row = next_word("was")
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    _blank(ax, (0, 15.0), (0, 5.0))
    chain = [("in", 1.0), ("july", 3.1), ("it", 5.2), ("was", 7.3)]
    y0 = 2.5
    for word, x in chain:
        _box(ax, x - 0.75, y0 - 0.38, 1.5, 0.76, word, color=FG, size=13)
    probs = ["1/12", "1", "1"]
    for (a, xa), (b, xb), p in zip(chain, chain[1:], probs):
        _arrow(ax, (xa + 0.8, y0), (xb - 0.82, y0), lw=1.5)
        ax.text((xa + xb) / 2, y0 + 0.22, p, ha="center", va="bottom", fontsize=12, color=C1)
    ys = [4.4, 3.17, 1.83, 0.6]
    start = (8.1, y0)
    for (word, (n, p)), yy in zip(row.items(), ys):
        good = word == true_word("july")
        col = GREEN if good else FG
        end = (10.55, yy)
        _box(ax, 10.6, yy - 0.36, 1.5, 0.72, word, color=col, size=13)
        _arrow(ax, start, end, lw=1.4, color=col if good else DIM)
        f = 0.62
        ax.text(start[0] + f * (end[0] - start[0]), start[1] + f * (end[1] - start[1]) + 0.2,
                f"{n}/12", ha="center", va="bottom", fontsize=12, color=C1)
        _box(ax, 12.7, yy - 0.36, 0.8, 0.72, ".", color=DIM, size=13)
        _arrow(ax, (12.15, yy), (12.65, yy), lw=1.2)
        ax.text(13.75, yy, "true" if good else "false", ha="left", va="center",
                fontsize=11.5, color=GREEN if good else style.BAD)
    style.save(fig, "viz_language_tree")


def _similarity():
    """The cosine of every pair of month vectors, drawn as vector cells (no
    embedded raster): pcolormesh for the grid, the colorbar's cells kept as
    vectors too."""
    mv = month_vectors()
    short = [m[:3] for m in NAMES]
    grid = [[cosine(mv[a], mv[b]) for b in NAMES] for a in NAMES]
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    edges = list(range(13))
    mesh = ax.pcolormesh(edges, edges, grid, cmap="viridis", vmin=0, vmax=1,
                         edgecolors="face", linewidth=0.4, rasterized=False)
    ax.set_xlim(0, 12)
    ax.set_ylim(12, 0)                      # January at the top, as a table reads
    ax.set_aspect("equal")
    centres = [i + 0.5 for i in range(12)]
    ax.set_xticks(centres)
    ax.set_yticks(centres)
    ax.set_xticklabels(short, fontsize=9.5, rotation=90)
    ax.set_yticklabels(short, fontsize=9.5)
    ax.tick_params(length=0)
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for i in range(12):
        for j in range(12):
            v = grid[i][j]
            if 0.005 < v < 0.995:
                ax.text(j + 0.5, i + 0.5, f"{v:.2f}".lstrip("0"), ha="center", va="center",
                        fontsize=7.5, color="#0b0e14" if v > 0.6 else FG)
    cb = fig.colorbar(mesh, ax=ax, fraction=0.046, pad=0.03)
    cb.solids.set_rasterized(False)
    cb.solids.set_edgecolor("face")
    cb.set_label("cosine of the two vectors")
    cb.outline.set_visible(False)
    style.save(fig, "viz_language_similarity")


def _attention():
    weights, _, _, ctx = attention()
    row = [p for _, p in next_word("was").values()]
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3), gridspec_kw={"width_ratios": [0.8, 1]})
    ax = axes[0]
    _bars(ax, ATT_WORDS, weights, [C1, DIM, DIM], top=1.0, size=11.5)
    ax.set_ylabel("weight")
    ax.set_title("The weights of the last three words", fontsize=13)
    ax = axes[1]
    xs_ = range(4)
    ax.bar([x - 0.19 for x in xs_], row, width=0.36, color=DIM, label="“was” alone")
    ax.bar([x + 0.19 for x in xs_], ctx, width=0.36, color=C1, label="with attention")
    for x, v in zip(xs_, ctx):
        ax.text(x + 0.19, v + 0.02, f"{v:.3f}", ha="center", va="bottom", fontsize=10.5,
                color=FG)
    for x, v in zip(xs_, row):
        ax.text(x - 0.19, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=10.5,
                color=DIM)
    ax.set_xticks(list(xs_))
    ax.set_xticklabels(WORDS)
    ax.set_ylim(0, 1.18)
    ax.set_ylabel("probability of the next word")
    ax.legend(loc="upper left", fontsize=10)
    ax.set_title("After “in july it was”", fontsize=13)
    style.save(fig, "viz_language_attention")


def _llm():
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    _blank(ax, (0, 16.2), (0, 5.6))
    y = 3.1
    steps = [(0.1, 2.3, "the prompt\n“in july it was”", DIM),
             (2.9, 2.0, "tokens,\neach an id", FG),
             (5.4, 2.0, "a vector\nper token", FG),
             (7.9, 2.7, "layers:\nattention,\nneurons", PINK),
             (11.1, 2.1, "a score for\nevery token", FG),
             (13.7, 2.3, "softmax at $T$,\ndraw one", GREEN)]
    for x, w, text, col in steps:
        _box(ax, x, y - 0.95, w, 1.9, text, color=col, size=11.5)
    for (x, w, *_), (nx, *_) in zip(steps, steps[1:]):
        _arrow(ax, (x + w + 0.05, y), (nx - 0.08, y), lw=1.5)
    ax.text(9.25, y + 1.25, "× many layers", ha="center", fontsize=10.5, color=PINK)
    _arrow(ax, (14.85, y - 1.0), (14.85, 0.9), lw=1.5, color=GREEN)
    ax.text(14.85, 0.55, "“warm”", ha="center", va="center", fontsize=12.5, color=GREEN)
    ax.add_patch(FancyArrowPatch((14.0, 0.55), (1.25, y - 1.0), arrowstyle="-|>",
                                 mutation_scale=14, lw=1.5, color=GREEN,
                                 connectionstyle="angle,angleA=180,angleB=90,rad=8",
                                 shrinkA=4, shrinkB=0, zorder=4))
    ax.text(7.4, 0.25, "append the token to the text, and again, until a stop token",
            ha="center", va="center", fontsize=11, color=GREEN)
    style.save(fig, "viz_language_llm")


def _sizes():
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    names = [n for n, _ in SIZES]
    vals = [v for _, v in SIZES]
    ys = list(range(len(vals)))[::-1]
    ax.hlines(ys, 1, vals, color=style.GRID, lw=1.2)
    ax.plot(vals, ys, "o", ms=10, color=C1)
    for y_, v in zip(ys, vals):
        e = int(math.log10(v))
        text = f"{v:g}" if v < 1e3 else f"{v / 10 ** e:.3g} × 10$^{{{e}}}$"
        ax.text(v * 2.2, y_, text, va="center", fontsize=12, color=FG)
    ax.set_xscale("log")
    ax.set_xlim(1, 1e14)
    ax.set_yticks(ys)
    ax.set_yticklabels(names)
    ax.set_xlabel("parameters: weights, biases, vectors")
    ax.set_ylim(-0.6, len(vals) - 0.4)
    style.save(fig, "viz_language_sizes")


WORD_COLORS = {"cold": VIOLET, "cool": C1, "mild": GREEN, "warm": C0}


def _tiny_backward():
    """The chain of the frost evening, the forward values above, the
    derivatives of the loss below, one per link."""
    t = tiny_step()
    f, g = t["fwd"], t["grad"]
    fig, ax = plt.subplots(figsize=(9.4, 2.2))
    _blank(ax, (0, 17.4), (0.0, 3.9))
    y0 = 2.15
    xs = {"x": 0.8, "h": 6.0, "yh": 11.2, "L": 16.0}
    _neuron(ax, xs["x"], y0, 0.42, "$x$", C1)
    _neuron(ax, xs["h"], y0, 0.52, "$h$", PINK)
    _neuron(ax, xs["yh"], y0, 0.52, r"$\hat{y}$", GREEN, size=16)
    _box(ax, xs["L"] - 0.7, y0 - 0.4, 1.4, 0.8, "loss", color=FG, size=13)
    _arrow(ax, (xs["x"] + 0.45, y0), (xs["h"] - 0.55, y0), lw=1.5)
    _arrow(ax, (xs["h"] + 0.55, y0), (xs["yh"] - 0.55, y0), lw=1.5)
    _arrow(ax, (xs["yh"] + 0.55, y0), (xs["L"] - 0.75, y0), lw=1.5)
    top = 3.35
    ax.text(xs["x"], top, "2.0", ha="center", fontsize=11.5, color=C1)
    ax.text(xs["h"], top, f"$h$ = {_m(f['h'])}", ha="center", fontsize=11.5, color=C1)
    ax.text(xs["yh"], top, f"$\\hat{{y}}$ = {_m(f['yh'])}", ha="center", fontsize=11.5, color=C1)
    ax.text(xs["L"], top, _m(f["L"]), ha="center", fontsize=11.5, color=C1)
    low = 0.95
    d = "\\partial\\,\\mathrm{{loss}}/\\partial"
    kw = dict(ha="center", va="center", fontsize=11, color=C0, linespacing=1.5)
    ax.text(2.45, low, f"${d} v$ = {_m(g['v'])}\n${d} c$ = {_m(g['c'])}", **kw)
    ax.text(xs["h"] - 0.25, low, f"${d} h$ = {_m(t['dh'])}\n${d} u$ = {_m(t['du'])}", **kw)
    ax.text(9.0, low, f"${d} w$ = {_m(g['w'])}\n${d} b$ = {_m(g['b'])}", **kw)
    ax.text(xs["yh"] + 0.9, low, f"$\\delta$ = {_m(t['delta'])}", **kw)
    _arrow(ax, (15.2, 0.12), (1.6, 0.12), color=C0, lw=1.3, ms=11)
    ax.text(15.35, 0.12, "backward", ha="left", va="center", fontsize=10.5, color=C0)
    style.save(fig, "viz_language_tiny_backward")


def _nudge():
    """The loss of the frost evening as a function of v alone, the slope at
    v = -1, and where one step moves v."""
    t = tiny_step()
    x, y = t["x"], t["y"]
    vs = [-4 + 6 * i / 400 for i in range(401)]
    Ls = [tiny_forward(v, TINY["c"], TINY["w"], TINY["b"], x, y)["L"] for v in vs]
    v0 = TINY["v"]
    L0 = t["fwd"]["L"]
    slope = t["grad"]["v"]
    fig, ax = plt.subplots(figsize=(9.4, 2.6))
    ax.plot(vs, Ls, color=C1, lw=2.2, label="the loss for each $v$, the other three weights fixed")
    tx = [v0 - 1.3, v0 + 1.3]
    ax.plot(tx, [L0 + slope * (a - v0) for a in tx], color=C0, lw=1.8,
            label=f"the slope at $v = -1$: {_m(slope, '.4f')}")
    ax.plot([v0], [L0], "o", ms=8, color=C0, zorder=5)
    ax.annotate(f"$v = -1$, loss {_m(L0)}", xy=(v0, L0), xytext=(-0.55, 1.25),
                fontsize=11.5, color=FG, arrowprops={"arrowstyle": "-", "color": DIM, "lw": 1})
    ax.set_xlabel("$v$")
    ax.set_ylabel("loss")
    ax.set_xlim(-4, 2)
    ax.legend(loc="lower left", fontsize=10.5)
    style.save(fig, "viz_language_nudge")


def _true_by_month():
    row = next_word("was")
    hits = month_hits()
    fig, ax = plt.subplots(figsize=(9.4, 2.6))
    xs = list(range(12))
    vals = [row[true_word(m)][1] for m in NAMES]
    ax.bar(xs, vals, color=[WORD_COLORS[true_word(m)] for m in NAMES], width=0.62)
    ax.plot(xs, [hits[m] for m in NAMES], "o", ms=6, color=FG, zorder=5,
            label="share true in 10 000 drawn sentences")
    ax.axhline(p_true(), color=DIM, lw=1, ls=(0, (4, 3)))
    ax.text(4.5, p_true() + 0.012, f"all months: {p_true():.3f}", ha="center", va="bottom",
            fontsize=10.5, color=DIM)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"{m[:3]}\n{true_word(m)}" for m in NAMES], fontsize=9.5)
    ax.set_ylabel("P(the true word)")
    ax.set_ylim(0, 0.45)
    ax.legend(loc="upper left", fontsize=10)
    style.save(fig, "viz_language_true_by_month")


def _month_vectors():
    """The twelve month vectors of the 120 sentences as small bar charts,
    the count on every bar that is not 0."""
    mv = month_vectors()
    fig, axes = plt.subplots(2, 6, figsize=(9.4, 3.3), sharey=True)
    for ax, m in zip(axes.flat, NAMES):
        vals = mv[m]
        ax.bar(range(4), vals, color=[WORD_COLORS[w] for w in WORDS], width=0.7)
        for i, v in enumerate(vals):
            if v:
                ax.text(i, v + 0.4, str(v), ha="center", va="bottom", fontsize=10, color=FG)
        ax.set_title(m, fontsize=11.5)
        ax.set_xticks([])
        ax.set_ylim(0, 13.5)
        ax.set_yticks([0, 5, 10])
        ax.tick_params(labelsize=9)
    handles = [plt.Rectangle((0, 0), 1, 1, color=WORD_COLORS[w]) for w in WORDS]
    fig.legend(handles, WORDS, loc="outside lower center", ncol=4, fontsize=10.5,
               frameon=False)
    style.save(fig, "viz_language_month_vectors")


def _qk():
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    q = ATT_Q
    ax.add_patch(FancyArrowPatch((0, 0), q, arrowstyle="-|>", mutation_scale=18, lw=2.4,
                                 color=FG, shrinkA=0, shrinkB=0, zorder=4))
    ax.text(q[0], q[1] - 0.22, "“was” looks for $\\mathbf{q}$ = (3, 0)", ha="right", va="top",
            fontsize=11.5, color=FG)
    k = ATT_K
    ax.add_patch(FancyArrowPatch((0, 0), k["july"], arrowstyle="-|>", mutation_scale=16,
                                 lw=3.0, color=C1, shrinkA=0, shrinkB=0, zorder=5))
    ax.text(k["july"][0] + 0.05, k["july"][1] + 0.12, "“july” offers (1, 0)\nscore 3 · 1 + 0 · 0 = 3",
            ha="left", va="bottom", fontsize=11, color=C1, linespacing=1.4)
    ax.add_patch(FancyArrowPatch((0, 0), k["it"], arrowstyle="-|>", mutation_scale=16, lw=2.2,
                                 color=DIM, shrinkA=0, shrinkB=0, zorder=5))
    ax.text(k["it"][0] + 0.1, k["it"][1], "“it”, “was” offer (0, 1)\nscore 3 · 0 + 0 · 1 = 0",
            ha="left", va="center", fontsize=11, color=DIM, linespacing=1.4)
    ax.set_xlim(-0.3, 3.4)
    ax.set_ylim(-0.6, 1.6)
    ax.set_aspect("equal")
    ax.set_xticks([0, 1, 2, 3])
    ax.set_yticks([0, 1])
    ax.set_xlabel("first number")
    ax.set_ylabel("second number")
    style.save(fig, "viz_language_qk")


FIGURES = {
    "viz_language_tiny_backward": _tiny_backward,
    "viz_language_nudge": _nudge,
    "viz_language_true_by_month": _true_by_month,
    "viz_language_month_vectors": _month_vectors,
    "viz_language_qk": _qk,
    "viz_language_xor_strip": _xor_strip,
    "viz_language_xor_network": _xor_network,
    "viz_language_xor_hidden": _xor_hidden,
    "viz_language_tiny_forward": _tiny_forward,
    "viz_language_xor_training": _xor_training,
    "viz_language_xor_starts": _xor_starts,
    "viz_language_next_word": _next_word,
    "viz_language_tree": _tree,
    "viz_language_similarity": _similarity,
    "viz_language_attention": _attention,
    "viz_language_llm": _llm,
    "viz_language_sizes": _sizes,
}


if __name__ == "__main__":
    numbers()
