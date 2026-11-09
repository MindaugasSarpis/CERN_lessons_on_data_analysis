"""Data of the two gallery figures of Lecture 7 (Data Visualisation).

Reads the raw tables in figures/data/gallery/ (sources and licences in its
README.md) and writes lectures/content/public/data/, read at run time by the
components in lectures/content/components/:

- l07_gapminder.json  BubbleChart: 142 countries, 1952 to 2007 every 5 years:
                      life expectancy at birth (years, as published, to 0.001),
                      population, GDP per person (US$, inflation-adjusted, to
                      the cent), and each country's continent.
- l07_volcano.json    TurningSurface: Maunga Whau (Mt Eden), 87 x 61 heights
                      in metres on a 10 m grid (R's `volcano`), the isolines
                      every 10 m and the bands between them (contourpy, the
                      contouring code of Matplotlib), and the viridis palette
                      (Matplotlib), 64 colours.

    ~/micromamba/envs/figures/bin/python figures/src/interactive_l07_gallery_data.py

writes the files (deterministic: the same bytes on every run) and prints the
numbers a speaker note may quote.
"""
import csv
import json
from pathlib import Path

import contourpy
import matplotlib as mpl
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "figures" / "data" / "gallery"
OUT = ROOT / "lectures" / "content" / "public" / "data"

CONTINENTS = ["Africa", "Americas", "Asia", "Europe", "Oceania"]
YEARS = list(range(1952, 2008, 5))
LEVELS = list(range(100, 200, 10))     # isolines, m: 100 to 190
PALETTE_STOPS = 64

GAPMINDER_ABOUT = (
    "Gapminder excerpt: 142 countries, 1952 to 2007 every 5 years; life expectancy at birth "
    "(years), population, GDP per person (US$, inflation-adjusted). Data: Gapminder "
    "Foundation, gapminder.org, CC BY 4.0. Excerpt: the gapminder R package by Jennifer "
    "Bryan (CC0), CSV from Rdatasets "
    "(https://vincentarelbundock.github.io/Rdatasets/csv/gapminder/gapminder.csv). "
    "Written by figures/src/interactive_l07_gallery_data.py from figures/data/gallery/gapminder.csv."
)
VOLCANO_ABOUT = (
    "Maunga Whau (Mt Eden), Auckland: heights in metres on a 10 m x 10 m grid, 87 x 61 "
    "points, digitised from a topographic map by Ross Ihaka; R's datasets package "
    "(volcano), GPL-2 | GPL-3, CSV from Rdatasets "
    "(https://vincentarelbundock.github.io/Rdatasets/csv/datasets/volcano.csv). R's "
    "documentation: 'These data should not be regarded as accurate.' heights[i * cols + j]: "
    "row i (x, 10 m apart), column j (y, 10 m apart), as R's image(volcano) draws them. "
    "Isolines every 10 m and the bands between them by contourpy, in grid units; palette viridis (Matplotlib). "
    "Written by figures/src/interactive_l07_gallery_data.py from figures/data/gallery/volcano.csv."
)


def dump(name, data):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    path.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  + {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")


def num(s):
    """A number as the CSV writes it, as an int when it is whole."""
    v = float(s)
    return int(v) if v == int(v) else v


# ---------------------------------------------------------------------------
# Gapminder
# ---------------------------------------------------------------------------

def gapminder_data():
    with open(RAW / "gapminder.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 1704, len(rows)
    by = {}
    for r in rows:
        by.setdefault(r["country"], {})[int(r["year"])] = r
    names = sorted(by)
    assert len(names) == 142, len(names)
    out = {"about": GAPMINDER_ABOUT, "years": YEARS, "continents": CONTINENTS,
           "name": [], "continent": [], "life": [], "pop": [], "gdp": []}
    for name in names:
        years = by[name]
        assert sorted(years) == YEARS, name
        cont = {years[y]["continent"] for y in YEARS}
        assert len(cont) == 1, name
        out["name"].append(name)
        out["continent"].append(CONTINENTS.index(cont.pop()))
        out["life"].append([num(f"{float(years[y]['lifeExp']):.3f}") for y in YEARS])
        out["pop"].append([int(years[y]["pop"]) for y in YEARS])
        out["gdp"].append([num(f"{float(years[y]['gdpPercap']):.2f}") for y in YEARS])
    return out


def report_gapminder(d):
    print("BubbleChart: the Gapminder excerpt")
    print(f"  {len(d['name'])} countries x {len(d['years'])} years")
    life = np.array(d["life"])
    gdp = np.array(d["gdp"])
    pop = np.array(d["pop"])
    for label, a in (("life expectancy", life), ("GDP per person", gdp), ("population", pop)):
        i, j = np.unravel_index(a.argmin(), a.shape)
        k, m = np.unravel_index(a.argmax(), a.shape)
        print(f"  {label}: lowest {a[i, j]} ({d['name'][i]} {d['years'][j]}),"
              f" highest {a[k, m]} ({d['name'][k]} {d['years'][m]})")
    for name in ("China", "India", "United States", "Rwanda", "Korea, Rep.", "Japan"):
        i = d["name"].index(name)
        for j in (0, d["years"].index(1992), len(d["years"]) - 1):
            print(f"  {name} {d['years'][j]}: {d['life'][i][j]} years, ${d['gdp'][i][j]:,.0f},"
                  f" {d['pop'][i][j] / 1e6:.1f} million")
    for j in (0, len(d["years"]) - 1):
        w = pop[:, j]
        print(f"  {d['years'][j]}: population-weighted life expectancy {np.dot(w, life[:, j]) / w.sum():.1f} years,"
              f" total {w.sum() / 1e9:.2f} billion in these 142 countries")


# ---------------------------------------------------------------------------
# Maunga Whau
# ---------------------------------------------------------------------------

def volcano_data():
    with open(RAW / "volcano.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    assert rows[0][1:] == [f"V{j}" for j in range(1, 62)], rows[0][:3]
    z = np.array([[int(v) for v in r[1:]] for r in rows[1:]])
    assert z.shape == (87, 61), z.shape
    # contourpy wants z[y, x]: rows of R's matrix are x, columns are y.
    gen = contourpy.contour_generator(np.arange(87), np.arange(61), z.T.astype(float),
                                      name="serial", line_type="Separate", fill_type="OuterOffset")
    contours = []
    for level in LEVELS:
        lines = []
        for seg in gen.lines(level):
            pts = np.round(seg, 2)
            closed = bool(np.allclose(pts[0], pts[-1]))
            flat = [num(f"{v:.2f}") for v in pts.reshape(-1)]
            lines.append({"closed": closed, "xy": flat})
        lines.sort(key=lambda l: (-len(l["xy"]), l["xy"][:2]))
        contours.append({"level": level, "lines": lines})
    # The bands between the isolines: every ring of a band in one list
    # (drawn with the even-odd rule, so the holes stay open).
    bands = []
    edges = [float(z.min())] + LEVELS + [float(z.max()) + 1]
    for lo, hi in zip(edges[:-1], edges[1:]):
        rings = []
        for pts, offs in zip(*gen.filled(lo, hi)):
            for a, b in zip(offs[:-1], offs[1:]):
                ring = np.round(pts[a:b], 2)
                rings.append([num(f"{v:.2f}") for v in ring.reshape(-1)])
        rings.sort(key=lambda r: (-len(r), r[:2]))
        bands.append({"lo": num(f"{lo:g}"), "hi": num(f"{min(hi, z.max()):g}"), "rings": rings})
    cmap = mpl.colormaps["viridis"]
    palette = [mpl.colors.to_hex(cmap(k / (PALETTE_STOPS - 1))) for k in range(PALETTE_STOPS)]
    return {"about": VOLCANO_ABOUT, "spacing": 10, "rows": 87, "cols": 61,
            "min": int(z.min()), "max": int(z.max()),
            "heights": [int(v) for v in z.reshape(-1)], "levels": LEVELS,
            "contours": contours, "bands": bands, "palette": palette}


def report_volcano(d):
    z = np.array(d["heights"]).reshape(d["rows"], d["cols"])
    i, j = np.unravel_index(z.argmax(), z.shape)
    print("TurningSurface: Maunga Whau")
    print(f"  {d['rows']} x {d['cols']} = {z.size} heights, {(d['rows'] - 1) * d['spacing']} m x"
          f" {(d['cols'] - 1) * d['spacing']} m; {d['min']} to {d['max']} m;"
          f" summit at row {i}, column {j}")
    for c in d["contours"]:
        n = sum(len(l["xy"]) // 2 for l in c["lines"])
        print(f"  {c['level']} m: {len(c['lines'])} lines, {n} points")
    for b in d["bands"]:
        print(f"  band {b['lo']} to {b['hi']} m: {len(b['rings'])} rings, {sum(len(r) for r in b['rings']) // 2} points")


def main():
    gap = gapminder_data()
    vol = volcano_data()
    dump("l07_gapminder.json", gap)
    dump("l07_volcano.json", vol)
    report_gapminder(gap)
    report_volcano(vol)


if __name__ == "__main__":
    main()
