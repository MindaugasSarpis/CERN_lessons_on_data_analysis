#!/usr/bin/env python3
"""Data of the interactive teaching figures (lectures/content/components/).

Reads the weather log, prints every number the components show, and writes
their small JSON files to lectures/content/public/data/ deterministically
(same input, byte-identical output). Standard library only, so it runs with
any Python:

    python figures/src/interactive_data.py

Components and the numbers they rely on:

  FitLine               the ten yearly means (two decimals, as the slides
                        show them) -> public/data/yearly_means.json; the
                        least-squares line, chi-square with sigma = 0.70
  PerceptronPlayground  every evening as Lecture 10 has it: x1 the
                        temperature at 18:00, x2 the humidity as a fraction,
                        frost at 06:00 the next morning; about 300 of the
                        3646 drawn -> public/data/frost_evenings.json
  MeanSpread            every measured hour, as a count per 0.1 degC value
                        (lossless: the log has one decimal)
                        -> public/data/hour_temps.json; the sample means of
                        the component's seeded draws, recomputed here with
                        the same generator (mulberry32) so the two agree to
                        the last digit
  SoftmaxTemperature    the default scores 2.0, 1.0, 0.1 at five temperatures
  FormulaSteps          the mean of the four measured hours of 21 July 2019
"""
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV = ROOT / "lectures" / "workbook" / "docs" / "data" / "weather.csv"
OUT = ROOT / "lectures" / "content" / "public" / "data"
MISSING = -999.0


def load():
    with CSV.open(newline="") as f:
        rows = list(csv.DictReader(f))
    times = [r["time"] for r in rows]
    temp = [float(r["temp_c"]) for r in rows]
    hum = [float(r["humidity_pct"]) for r in rows]
    return times, temp, hum


def write(name, obj):
    OUT.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n"
    (OUT / name).write_text(text, encoding="utf-8")
    print(f"  wrote public/data/{name} ({len(text.encode())} bytes)")


# ------------------------------------------------------------------ FitLine
def yearly_means(times, temp):
    print("\n== FitLine: the ten yearly means ==")
    years = list(range(2016, 2026))
    full, shown = [], []
    for y in years:
        vals = [t for s, t in zip(times, temp) if s.startswith(str(y)) and t != MISSING]
        m = sum(vals) / len(vals)
        full.append(m)
        shown.append(round(m, 2))
        print(f"  {y}: {len(vals)} hours, mean {m:.4f} -> {m:.2f}")
    n = len(shown)
    ybar = sum(shown) / n
    sd = math.sqrt(sum((v - ybar) ** 2 for v in shown) / (n - 1))
    print(f"  mean of the ten: {ybar:.4f}; scatter s (N-1): {sd:.4f} -> sigma = {sd:.2f}")
    print(f"  s / sqrt(10) = {sd / math.sqrt(n):.3f}")

    sigma = 0.70
    x = [y - 2016 for y in years]          # x = year - 2016, 0 ... 9
    S, Sx, Sy = n, sum(x), sum(shown)
    Sxx = sum(v * v for v in x)
    Sxy = sum(a * b for a, b in zip(x, shown))
    b = (S * Sxy - Sx * Sy) / (S * Sxx - Sx ** 2)
    a = (Sy - b * Sx) / S
    print(f"  five sums (x = year - 2016): N={S}, Sx={Sx}, Sy={Sy:.2f}, Sxx={Sxx}, Sxy={Sxy:.2f}")
    print(f"  slope b = ({S}*{Sxy:.2f} - {Sx}*{Sy:.2f}) / ({S}*{Sxx} - {Sx}^2) = {b:.5f} degC/yr"
          f" = {10 * b:.3f} degC per decade")
    print(f"  intercept a = ({Sy:.2f} - b*{Sx}) / {S} = {a:.4f} degC (the line in 2016)")
    # the same from the unrounded means
    Sy_f = sum(full)
    Sxy_f = sum(p * q for p, q in zip(x, full))
    b_f = (S * Sxy_f - Sx * Sy_f) / (S * Sxx - Sx ** 2)
    print(f"  (from the unrounded means: {10 * b_f:.3f} degC per decade)")

    def chi2(a_, b_):
        return sum((yy - a_ - b_ * xx) ** 2 for xx, yy in zip(x, shown)) / sigma ** 2

    sxx_c = Sxx - Sx ** 2 / S
    print(f"  chi2 at the best line (sigma {sigma}): {chi2(a, b):.3f}")
    print(f"  chi2 of the flat line at the mean {ybar:.2f}: {chi2(ybar, 0):.3f}")
    sb = sigma / math.sqrt(sxx_c)
    print(f"  slope uncertainty sigma/sqrt(Sxx - Sx^2/N) = {sb:.4f} /yr = {10 * sb:.2f} per decade")
    print("  terms at the best line, (y - a - b x)^2 / sigma^2:")
    for yr, xx, yy in zip(years, x, shown):
        r = yy - a - b * xx
        print(f"    {yr}: x={xx} y={yy:.2f} line={a + b * xx:.3f} r={r:+.3f} term={r * r / sigma ** 2:.3f}")
    xx, yy = 7, shown[7]
    r = yy - a - b * xx
    print(f"  one point pushed through, 2023: ({yy:.2f} - {a:.2f} - ({b:.3f})*7)^2 / {sigma:.2f}^2"
          f" = {r:.3f}^2 / {sigma ** 2:.2f} = {r * r / sigma ** 2:.3f}")
    write("yearly_means.json", {
        "about": "Yearly mean temperature (degC) of the weather log, -999 left out, two decimals as on the slides. figures/src/interactive_data.py",
        "years": years,
        "means": shown,
        "sigma": sigma,
        "best": {"a": round(a, 4), "b": round(b, 5), "x0": 2016, "chi2": round(chi2(a, b), 3)},
    })
    return shown


# -------------------------------------------------------- PerceptronPlayground
def even_picks(items, m):
    """m items spread evenly over a list: index floor((k + 1/2) n / m)."""
    n = len(items)
    return [items[(2 * k + 1) * n // (2 * m)] for k in range(m)]


# The evenings Lecture 10 names (figures/src/perceptron.py): they are always
# among the drawn ones, so the component can push the same evening through z.
NAMED_EVENINGS = ["2016-01-01", "2016-01-10", "2016-01-11",
                  "2025-12-06", "2025-12-07", "2025-12-08", "2025-12-09"]


def frost_evenings(times, temp, hum):
    """Lecture 10's evenings: x1 the temperature at 18:00 (degC), x2 the
    humidity at 18:00 as a fraction (85 % is 0.85), y = 1 if 06:00 the next
    morning is below 0 degC."""
    print("\n== PerceptronPlayground: evenings at 18:00, frost at 06:00 the next morning ==")
    days = len(temp) // 24
    ev = []
    for d in range(days - 1):
        t18, h18 = temp[24 * d + 18], hum[24 * d + 18]
        t06 = temp[24 * (d + 1) + 6]
        assert times[24 * d + 18].endswith("T18:00") and times[24 * (d + 1) + 6].endswith("T06:00")
        if t18 == MISSING or t06 == MISSING:
            continue
        ev.append({"date": times[24 * d + 18][:10], "x1": t18, "x2": round(h18 / 100, 2),
                   "m": t06, "y": int(t06 < 0)})
    n, nf = len(ev), sum(e["y"] for e in ev)
    print(f"  {days - 1} pairs, {n} evenings without -999, {nf} followed by frost")

    def acc(evs, w1, w2, b):
        # z to four decimals, as the component computes it: with its weights
        # (steps 0.01, 0.01, 0.1) that is z exactly, so z = 0 is never frost.
        right = sum(int((round(w1 * e["x1"] + w2 * e["x2"] + b, 4) > 0) == bool(e["y"])) for e in evs)
        return right, len(evs)

    # Lecture 10's neurons, on all evenings (its slides count all 3646).
    for w1, w2, b, name in ((0.0, 0.0, -1.0, "never frost"), (-1.0, 0.0, 2.0, "below 2 degC"),
                            (-1.0, 0.0, 3.8, "below 3.8 degC, the start"),
                            (-1.0, 4.0, 0.6, "the tilted neuron")):
        r, m = acc(ev, w1, w2, b)
        print(f"  w = ({w1}, {w2}), b = {b} ({name}): {r} of {m} = {100 * r / m:.1f} %")
    e = next(e for e in ev if e["date"] == "2025-12-08")
    z = round(-1.0 * e["x1"] + 0.0 * e["x2"] + 3.8, 4)
    print(f"  8 Dec 2025: x = ({e['x1']}, {e['x2']}), z = (-1)({e['x1']}) + (0)({e['x2']}) + 3.8 = {z}"
          f" -> {'frost' if z > 0 else 'no frost'}; 06:00 {e['m']} degC, y = {e['y']}")
    x1s = [e["x1"] for e in ev]
    x2s = [e["x2"] for e in ev]
    print(f"  ranges: x1 {min(x1s)} .. {max(x1s)} degC, x2 {min(x2s)} .. {max(x2s)}")
    # The component counts right and wrong over ALL evenings and draws about
    # 300 of them: 300 picked evenly through the frost evenings and through
    # the others (the frost share kept), and the evenings Lecture 10 names.
    for i, e in enumerate(ev):
        e["i"] = i
    frost = [e for e in ev if e["y"] == 1]
    clear = [e for e in ev if e["y"] == 0]
    nf_s = round(300 * nf / n)
    picked = {e["i"]: e for e in even_picks(frost, nf_s) + even_picks(clear, 300 - nf_s)}
    named = [e for e in ev if e["date"] in NAMED_EVENINGS]
    assert len(named) == len(NAMED_EVENINGS)
    for e in named:
        picked[e["i"]] = e
    sample = sorted(picked.values(), key=lambda e: e["i"])
    print(f"  drawn: {len(sample)} evenings (300 picked evenly, {nf_s} of them frost, and the {len(named)} named ones)")
    write("frost_evenings.json", {
        "about": "Every evening of the weather log with 18:00 and 06:00 the next morning measured, as in Lecture 10: x1 = temperature at 18:00 (degC), x2 = humidity at 18:00 as a fraction, y = 1 if 06:00 the next morning is below 0 degC. 'shown' = the evenings drawn (about 300, the frost share kept, and those Lecture 10 names), with their date and their 06:00 temperature 'm'. figures/src/interactive_data.py",
        "x1": x1s,
        "x2": x2s,
        "y": [e["y"] for e in ev],
        "shown": [e["i"] for e in sample],
        "date": [e["date"] for e in sample],
        "m": [e["m"] for e in sample],
    })


# ---------------------------------------------------------------- MeanSpread
def mulberry32(seed):
    """The component's generator, bit for bit (JavaScript's mulberry32)."""
    a = seed & 0xFFFFFFFF

    def rnd():
        nonlocal a
        a = (a + 0x6D2B79F5) & 0xFFFFFFFF
        t = ((a ^ (a >> 15)) * (a | 1)) & 0xFFFFFFFF
        t = ((t + (((t ^ (t >> 7)) * (t | 61)) & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296

    return rnd


def seed_of(n, draw):
    """Seed of the draw-th press of 'draw again' at N hours (0 = first view)."""
    return n * 7919 + draw * 104729 + 1


def sample_means(values, n, draw, m=1000):
    rnd = mulberry32(seed_of(n, draw))
    size = len(values)
    out = []
    for _ in range(m):
        s = 0.0
        for _ in range(n):
            s += values[math.floor(rnd() * size)]
        out.append(s / n)
    return out


def hour_temps(temp):
    print("\n== MeanSpread: every measured hour ==")
    tenths = sorted(round(t * 10) for t in temp if t != MISSING)
    lo, hi = tenths[0], tenths[-1]
    counts = [0] * (hi - lo + 1)
    for v in tenths:
        counts[v - lo] += 1
    values = [(lo + k) / 10 for k, c in enumerate(counts) for _ in range(c)]
    n = len(values)
    mean = sum(values) / n
    sd_pop = math.sqrt(sum((v - mean) ** 2 for v in values) / n)
    sd = math.sqrt(sum((v - mean) ** 2 for v in values) / (n - 1))
    print(f"  {n} hours from {lo / 10} to {hi / 10} degC, {len(counts)} values of 0.1 degC")
    print(f"  mean {mean:.4f}, s {sd:.4f} (N-1) / {sd_pop:.4f} (N)")
    print(f"  s / sqrt(N) for all of them: {sd:.2f} / sqrt({n}) = {sd / math.sqrt(n):.4f}")
    inside = sum(1 for v in values if abs(v - mean) <= sd) / n
    print(f"  share of hours within mean +- s: {inside:.3f} (a Gaussian has 0.683)")
    print("  seeded draws, 1000 sample means each (the component's first view of each N):")
    for k in (1, 4, 16, 100, 1000):
        means = sample_means(values, k, 0)
        mm = sum(means) / len(means)
        spread = math.sqrt(sum((v - mm) ** 2 for v in means) / (len(means) - 1))
        print(f"    N={k:4d}: mean of the means {mm:.3f}, spread {spread:.3f}"
              f" vs s/sqrt(N) = {sd:.2f}/sqrt({k}) = {sd / math.sqrt(k):.3f}")
    means = sample_means(values, 100, 1)
    mm = sum(means) / len(means)
    spread = math.sqrt(sum((v - mm) ** 2 for v in means) / (len(means) - 1))
    print(f"    N= 100, after one 'draw again': mean {mm:.3f}, spread {spread:.3f}")
    write("hour_temps.json", {
        "about": "Every measured hour of the weather log (-999 left out) as a count per 0.1 degC value, from 'min' upwards. figures/src/interactive_data.py",
        "hours": n,
        "min": lo / 10,
        "step": 0.1,
        "counts": counts,
    })


# --------------------------------------------------------- SoftmaxTemperature
def softmax():
    print("\n== SoftmaxTemperature: scores 2.0, 1.0, 0.1 ==")
    s = [2.0, 1.0, 0.1]
    for T in (0.1, 0.5, 0.7, 1.0, 2.0, 3.0):
        e = [math.exp(v / T) for v in s]
        tot = sum(e)
        p = [v / tot for v in e]
        print(f"  T={T}: e^(s/T) = {', '.join(f'{v:.4g}' for v in e)}; sum {tot:.4g};"
              f" p = {', '.join(f'{v:.3f}' for v in p)}")


# -------------------------------------------------------------- FormulaSteps
def formula_steps(times, temp):
    print("\n== FormulaSteps: the evening of 21 July 2019 ==")
    i = times.index("2019-07-21T20:00")
    six = temp[i:i + 6]
    ok = [t for t in six if t != MISSING]
    print(f"  20:00 to 01:00: {six}")
    print(f"  with the marks: {sum(six)} / 6 = {sum(six) / 6:.3f}")
    print(f"  without: ({' + '.join(str(t) for t in ok)}) / {len(ok)} = {sum(ok):.1f} / {len(ok)} = {sum(ok) / len(ok):.3f}")


def main():
    times, temp, hum = load()
    print(f"{CSV.relative_to(ROOT)}: {len(times)} rows, {sum(t == MISSING for t in temp)} temperatures of -999")
    yearly_means(times, temp)
    frost_evenings(times, temp, hum)
    hour_temps(temp)
    softmax()
    formula_steps(times, temp)


if __name__ == "__main__":
    main()
