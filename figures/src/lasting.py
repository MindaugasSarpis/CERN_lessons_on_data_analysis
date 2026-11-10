"""Lecture 12, Code That Lasts: the project's files, a dependency tree, the
packages of one environment, version ranges, the releases of pandas, and the
two means of Lecture 1 on single days; and every number the slides state.

Run directly to print every number of the deck:

    python figures/src/lasting.py

The numbers about packages come from conda-forge: environments solved without
installing them (`micromamba create --dry-run`, conda-forge only) for macOS on
Apple silicon (osx-arm64), Windows (win-64) and Linux (linux-64), and the
date of each release. They are kept in lasting_env.json, made again with

    python figures/src/lasting.py --fetch      (needs micromamba and the network)

so that the figures build without either. The numbers about the weather log
are computed from lectures/workbook/docs/data/weather.csv, with the lecture's
functions (`read_lines`, `temp_of`, `mean`), and the checksums by running the
two scripts handed out in Lecture 4 as `scripts/rebuild.sh` runs them.
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data"
PATH = DATA / "weather.csv"
ENV_FILE = Path(__file__).resolve().parent / "lasting_env.json"
MISSING = -999.0

# The evening of 21 July 2019, when the temperature sensor failed: the six
# hours that Seminars 1 to 5 typed, two of them marked -999.
SIX = [
    "2019-07-21T20:00,27.3,63,4.5",
    "2019-07-21T21:00,25.6,65,4.0",
    "2019-07-21T22:00,24.6,68,3.5",
    "2019-07-21T23:00,23.6,74,3.4",
    "2019-07-22T00:00,-999,76,3.2",
    "2019-07-22T01:00,-999,81,3.0",
]

# The perceptron of Lecture 10, its weights set by hand: frost at 06:00 when
# the evening at 18:00 is below 3.8 degrees (z = -1 * x1 + 0 * x2 + 3.8, x1 the
# temperature, x2 the humidity as a fraction), as Lecture 10 writes it.
W1, W2, B = -1.0, 0.0, 3.8
EVENINGS = ["2025-12-08", "2024-11-01"]

# The two days of the figure "two means": the midrange furthest below and
# furthest above the mean of the hours, over the 3648 days.
DAYS = ["2021-11-12", "2025-08-11"]


# ---------------------------------------------------------------------------
# The lecture's functions, as in weather.py
# ---------------------------------------------------------------------------

def read_lines(path):
    return open(path).read().splitlines()[1:]


def temp_of(line):
    return float(line.split(",")[1])


def temps_of_lines(lines):
    result = []
    for line in lines:
        temp = temp_of(line)
        if temp != MISSING:
            result.append(temp)
    return result


def mean(values):
    return sum(values) / len(values)


def loop_sum(values):
    """Add one value after the other: what sum() did for floats up to
    Python 3.11. From 3.12 on, sum() adds with a correction for rounding
    (compensated summation)."""
    total = 0.0
    for value in values:
        total = total + value
    return total


def by_day():
    days = defaultdict(list)
    for line in read_lines(PATH):
        temp = temp_of(line)
        if temp != MISSING:
            days[line[:10]].append((int(line[11:13]), temp))
    return days


def midrange(values):
    return (min(values) + max(values)) / 2


def evenings():
    """Every evening at 18:00 whose temperature and the temperature at 06:00
    the next morning were measured: (date, temp, humidity, next 06:00)."""
    by_time = {}
    for line in read_lines(PATH):
        parts = line.split(",")
        by_time[parts[0]] = (float(parts[1]), float(parts[2]))
    out = []
    for t, (temp, hum) in by_time.items():
        if not t.endswith("T18:00") or temp == MISSING:
            continue
        nxt = (datetime.fromisoformat(t) + timedelta(hours=12)).strftime("%Y-%m-%dT%H:%M")
        if nxt in by_time and by_time[nxt][0] != MISSING:
            out.append((t[:10], temp, hum, by_time[nxt][0]))
    return out


def predict(temp, humidity):
    z = W1 * temp + W2 * humidity / 100 + B
    return 1 if z > 0 else 0


# ---------------------------------------------------------------------------
# The rebuild of Lecture 4, run as scripts/rebuild.sh runs it
# ---------------------------------------------------------------------------

def rebuild_outputs():
    """Make the three outputs of rebuild.sh in a temporary project folder and
    return {path: bytes}; also the output of column_stats.py on the raw file
    (Tomas's change of Seminar 6)."""
    out = {}
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "data" / "processed").mkdir(parents=True)
        (root / "data" / "raw").mkdir(parents=True)
        (root / "results").mkdir()
        raw = PATH.read_bytes()
        (root / "data" / "raw" / "weather.csv").write_bytes(raw)
        (root / "data" / "raw" / "daily_export.csv").write_bytes(
            (DATA / "weather_daily_export.csv").read_bytes())
        # grep -v ',-999,' copies every other line, its bytes unchanged
        kept = b"".join(l for l in raw.splitlines(keepends=True) if b",-999," not in l)
        (root / "data" / "processed" / "weather_valid.csv").write_bytes(kept)
        subprocess.run([sys.executable, str(DATA / "cli_clean_export.py"),
                        "data/raw/daily_export.csv", "data/processed/daily.csv"],
                       cwd=root, check=True, capture_output=True)
        stats = subprocess.run([sys.executable, str(DATA / "cli_column_stats.py"),
                                "data/processed/weather_valid.csv", "temp_c"],
                               cwd=root, check=True, capture_output=True).stdout
        (root / "results" / "temp_c.txt").write_bytes(stats)
        for rel in ["data/processed/weather_valid.csv", "data/processed/daily.csv",
                    "results/temp_c.txt"]:
            out[rel] = (root / rel).read_bytes()
        out["tomas"] = subprocess.run([sys.executable, str(DATA / "cli_column_stats.py"),
                                       "data/raw/weather.csv", "temp_c"],
                                      cwd=root, check=True, capture_output=True).stdout
    return out


# ---------------------------------------------------------------------------
# conda-forge: solves and release dates (lasting_env.json)
# ---------------------------------------------------------------------------

PLATFORMS = ["osx-arm64", "win-64", "linux-64"]
SPECS = {
    "python": ["python=3.14"],
    "python+pandas": ["python=3.14", "pandas=3.1"],
    "python+matplotlib": ["python=3.14", "matplotlib-base=3.11"],
    "analysis": ["python=3.14", "matplotlib-base=3.11", "pandas=3.1"],
    "analysis+pytest": ["python=3.14", "matplotlib-base=3.11", "pandas=3.1", "pytest=9.2"],
    "python+pandas=2.3": ["python=3.14", "pandas=2.3"],
    "python3.11+pandas": ["python=3.11", "pandas=3.1"],
}
RELEASES_FROM = {"pandas": "2.0.0", "numpy": "1.25.0", "pytest": "8.0.0"}


def _vkey(v):
    return tuple(int(p) if p.isdigit() else -1 for p in v.replace("rc", ".rc.").split("."))


def fetch():
    """Solve each environment of SPECS on each platform and read the release
    dates; write lasting_env.json."""
    mm = os.environ.get("MICROMAMBA") or "micromamba"
    env = dict(os.environ, CONDA_OVERRIDE_OSX="14.0")
    env.setdefault("MAMBA_ROOT_PREFIX", tempfile.mkdtemp())
    data = {"fetched": date.today().isoformat(),
            "how": "micromamba create --dry-run -c conda-forge --override-channels",
            "counts": {}, "packages": {}, "releases": {}}
    for plat in PLATFORMS:
        data["counts"][plat] = {}
        data["packages"][plat] = {}
        for name, spec in SPECS.items():
            res = subprocess.run([mm, "create", "-n", "lasting-probe", "--dry-run", "--json",
                                  "-c", "conda-forge", "--override-channels",
                                  "--platform", plat, *spec],
                                 env=env, capture_output=True, text=True, check=True)
            links = json.loads(res.stdout)["actions"]["LINK"]
            data["counts"][plat][name] = len(links)
            if name in ("python", "python+pandas", "analysis+pytest", "python+pandas=2.3",
                        "python3.11+pandas"):
                names = {p["name"] for p in links}
                data["packages"][plat][name] = sorted(
                    [[p["name"], p["version"],
                      sorted(x for x in (p.get("depends") or []) if x.split()[0] in names)]
                     for p in links])
    for pkg, first in RELEASES_FROM.items():
        res = subprocess.run([mm, "repoquery", "search", pkg, "-c", "conda-forge",
                              "--override-channels", "--platform", "osx-arm64", "--json"],
                             env=env, capture_output=True, text=True, check=True)
        dates = {}
        for p in json.loads(res.stdout)["result"]["pkgs"]:
            v, ts = p["version"], p.get("timestamp") or 0
            if ts > 1e12:
                ts /= 1000
            if "rc" in v or "a" in v or "b" in v or _vkey(v) < _vkey(first):
                continue
            day = datetime.fromtimestamp(ts, timezone.utc).date().isoformat() if ts else None
            if v not in dates or (day and day < dates[v]):
                dates[v] = day
        data["releases"][pkg] = sorted(dates.items(), key=lambda kv: _vkey(kv[0]))
    ENV_FILE.write_text(json.dumps(data, indent=1) + "\n")
    print(f"wrote {ENV_FILE}")


def env_data():
    return json.loads(ENV_FILE.read_text())


def _names(pkgs):
    return {p[0]: p for p in pkgs}


def kinds(pkgs, asked):
    """Sort the packages of an environment into: asked for, Python packages
    (they depend on python or run on any system), the rest (compiled
    libraries, fonts, certificates, time-zone data)."""
    asked_set, py, rest = [], [], []
    for name, version, deps in pkgs:
        dep_names = {d.split()[0] for d in deps}
        if name in asked:
            asked_set.append(name)
        elif "python" in dep_names or "python_abi" in dep_names:
            py.append(name)
        else:
            rest.append(name)
    return asked_set, py, rest


# ---------------------------------------------------------------------------
# Drawing on a pixel canvas, as figures/src/git.py does
# ---------------------------------------------------------------------------

FONTS = Path(__file__).resolve().parents[1] / "fonts" / "git"
# Space Grotesk by family and weight: style.use() registers each weight under
# its own name. The static files of fonts/git/ all say "SpaceGrotesk-Light",
# so in one SVG their bold drew with the Medium outlines.
SANS = FontProperties(family=style.SANS, weight="normal")
BOLD = FontProperties(family=style.SANS, weight="bold")
MONO = FontProperties(fname=FONTS / "SpaceMono-Regular.ttf")
MONOB = FontProperties(fname=FONTS / "SpaceMono-Bold.ttf")

FG, FG2, DIM = "#f2f5f9", "#c3ccd8", "#8b97a6"
ACC, WARN = "#7dd3fc", "#fbbf24"
HAIR = (139 / 255, 151 / 255, 166 / 255, 0.26)
HAIR_SOFT = (139 / 255, 151 / 255, 166 / 255, 0.16)
PANEL = (1, 1, 1, 0.02)
ACC_FILL = (125 / 255, 211 / 255, 252 / 255, 0.10)
WARN_FILL = (251 / 255, 191 / 255, 36 / 255, 0.10)
PT = 0.72  # points per canvas pixel


def canvas(w, h):
    fig = plt.figure(figsize=(w / 100, h / 100), layout="none")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w)
    ax.set_ylim(h, 0)
    ax.axis("off")
    return fig, ax


def text(ax, x, y, s, size=26, color=FG, font=None, ha="left", va="baseline", **kw):
    ax.text(x, y, s, fontsize=size * PT, color=color, fontproperties=font or SANS,
            ha=ha, va=va, **kw)


def label(ax, x, y, s, ha="left", color=DIM, size=23):
    """An uppercase label, letter-spaced, as on the landing page."""
    text(ax, x, y, " ".join(s.upper()).replace("   ", "   "), size=size, color=color,
         font=BOLD, ha=ha)


def box(ax, x, y, w, h, edge=HAIR, fill=PANEL, r=9, lw=1.3, ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fill, ec=edge, lw=lw, ls=ls))


def arrow(ax, a, b, color=ACC, lw=2.6, rad=0.0, ls="-", head=16):
    st = f"-|>,head_length={head * PT:.1f},head_width={head * PT * 0.45:.1f}"
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=st, color=color, lw=lw, ls=ls,
                                 connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0,
                                 mutation_scale=1, capstyle="round", joinstyle="round"))


def sheet(ax, x, y, w=24, h=32, color=DIM, lw=1.6):
    f = w * 0.32
    ax.add_patch(Polygon([(x, y), (x + w - f, y), (x + w, y + f), (x + w, y + h), (x, y + h)],
                         closed=True, fc="none", ec=color, lw=lw, joinstyle="round"))
    ax.plot([x + w - f, x + w - f, x + w], [y, y + f, y + f], color=color, lw=lw)


def folder(ax, x, y, w=34, h=28, color=DIM, lw=1.6):
    ax.add_patch(Polygon([(x, y + 5), (x + w * 0.38, y + 5), (x + w * 0.48, y + 10),
                          (x + w, y + 10), (x + w, y + h), (x, y + h)],
                         closed=True, fc="none", ec=color, lw=lw, joinstyle="round"))


def row(ax, x, y, w, name, note, color=None, h=58):
    """One file: a chip with its name in mono and what it is for."""
    box(ax, x, y, w, h, edge=color or HAIR, fill=ACC_FILL if color == ACC else PANEL,
        r=6, lw=2.0 if color else 1.2)
    sheet(ax, x + 16, y + 13, color=color or DIM)
    text(ax, x + 56, y + 38, name, size=26, font=MONO)
    text(ax, x + w - 18, y + 38, note, size=23, color=FG2, ha="right")


def save_canvas(fig, name):
    """A diagram keeps its own canvas: the SVG is scaled as a whole into its
    box on the slide, so measured sizes do not apply."""
    style.SIZES.pop(name, None)
    style.save(fig, name, tight=False)


# ---------------------------------------------------------------------------
# Figures
# ---------------------------------------------------------------------------

def project():
    """What goes where: the weather project as Seminar 12 leaves it."""
    W, H = 1600, 640
    fig, ax = canvas(W, H)
    cols = [(0, 400), (490, 530), (1110, 490)]
    heads = [("As received", "never edited · in Git"),
             ("The recipe", "written by hand · in Git"),
             ("Made by rebuild.sh", "made again at will · not in Git")]
    for (x, w), (name, sub) in zip(cols, heads):
        box(ax, x, 2, w, H - 4)
        label(ax, x + 24, 48, name)
        text(ax, x + 24, 88, sub, size=24, color=FG2)

    def folder_row(x, y, name):
        folder(ax, x + 4, y - 22, color=DIM)
        text(ax, x + 50, y, name, size=25, font=MONO, color=FG2)

    def chip2(x, y, w, name, note, color=None):
        """A file on two lines: its name, then what it holds."""
        box(ax, x, y, w, 84, edge=color or HAIR, fill=PANEL, r=6, lw=1.2)
        sheet(ax, x + 16, y + 14, color=color or DIM)
        text(ax, x + 56, y + 38, name, size=26, font=MONO)
        text(ax, x + 56, y + 70, note, size=23, color=FG2)

    # as received
    x, w = cols[0]
    folder_row(x + 20, 150, "data/raw/")
    chip2(x + 20, 170, w - 40, "weather.csv", "87 672 hours")
    chip2(x + 20, 266, w - 40, "daily_export.csv", "9 daily means")
    # the recipe
    x, w = cols[1]
    folder_row(x + 20, 150, "scripts/")
    recipe = [("weather.py", "the functions", None), ("test_weather.py", "the facts", ACC),
              ("clean_export.py", "a step", None), ("column_stats.py", "a step", None),
              ("rebuild.sh", "the order", None)]
    for k, (name, note, color) in enumerate(recipe):
        row(ax, x + 20, 170 + 66 * k, w - 40, name, note, color=color)
    row(ax, x + 20, 506, w - 40, "environment.yml", "the versions")
    row(ax, x + 20, 572, w - 40, "README.md", "how to rebuild")
    # made by the one command
    x, w = cols[2]
    folder_row(x + 20, 150, "data/processed/")
    chip2(x + 20, 170, w - 40, "weather_valid.csv", "87 552 hours, no -999")
    chip2(x + 20, 266, w - 40, "daily.csv", "9 days, cleaned")
    folder_row(x + 20, 408, "results/")
    chip2(x + 20, 428, w - 40, "temp_c.txt", "mean    7.15997")
    # arrows: read, written, checked
    y = 312
    for (x0, w0), (x1, _), word in [(cols[0], cols[1], "read"), (cols[1], cols[2], "written")]:
        arrow(ax, (x0 + w0 + 10, y), (x1 - 10, y))
        text(ax, (x0 + w0 + x1) / 2, y - 16, word, size=22, color=ACC, ha="center")
    arrow(ax, (cols[2][0] + 20, 470), (cols[1][0] + cols[1][1] - 16, 233), color=FG2, lw=2.0,
          ls=(0, (5, 4)), rad=-0.3)
    text(ax, cols[2][0] + 40, 560, "read again by the tests", size=22, color=FG2)
    save_canvas(fig, "viz_lasting_project")


def tree_pandas():
    """pandas 3.1.1 and what it brings into an environment with Python 3.14,
    on macOS: the real dependencies, solved by conda-forge."""
    d = env_data()
    pk = _names(d["packages"]["osx-arm64"]["python+pandas"])
    base = _names(d["packages"]["osx-arm64"]["python"])
    added = sorted(set(pk) - set(base))
    v = {n: pk[n][1] for n in pk}
    W, H = 1600, 600
    fig, ax = canvas(W, H)

    def node(cx, y, name, version, w, kind="py", sub=None):
        color = {"asked": ACC, "py": None, "lib": None, "there": None}[kind]
        ls = (0, (4, 4)) if kind == "there" else "-"
        box(ax, cx - w / 2, y, w, 76, edge=color or (HAIR_SOFT if kind == "lib" else HAIR),
            fill=ACC_FILL if kind == "asked" else PANEL, r=7, lw=2.2 if color else 1.3, ls=ls)
        tc = FG if kind in ("asked", "py") else FG2
        text(ax, cx, y + 34, name, size=26 if kind != "lib" else 24, font=MONOB if kind == "asked" else MONO,
             color=tc, ha="center")
        text(ax, cx, y + 64, version if sub is None else sub, size=22, color=DIM, ha="center")

    def edge(a, b, txt=None, color=FG2, lw=1.8, dx=0):
        arrow(ax, a, b, color=color, lw=lw, head=13)
        if txt:
            mx, my = (a[0] + b[0]) / 2 + dx, (a[1] + b[1]) / 2
            text(ax, mx, my, txt, size=22, color=ACC, ha="center", va="center",
                 bbox=dict(boxstyle="round,pad=0.25", fc="#06070a", ec="none"))

    node(800, 10, "pandas", v["pandas"], 300, "asked")
    # level 1
    node(270, 175, "numpy", v["numpy"], 260)
    node(800, 175, "python-dateutil", v["python-dateutil"], 330)
    node(1395, 175, "python", v["python"], 330, "there", sub=f"{v['python']} · already there")
    node(1085, 175, "libcxx", v["libcxx"], 210, "lib")
    edge((720, 86), (300, 175), "≥ 2.0.2, < 3", dx=-30)
    edge((800, 86), (800, 175), "≥ 2.9.0", dx=0)
    edge((930, 86), (1360, 175), "3.14", dx=40)
    edge((870, 86), (1060, 175))
    # level 2
    node(270, 330, "libblas  libcblas  liblapack", v["libblas"], 470, "lib")
    node(800, 330, "python-tzdata", v["python-tzdata"], 300)
    edge((270, 251), (270, 330))
    edge((800, 251), (800, 330))
    # level 3, 4
    node(270, 470, "libopenblas", v["libopenblas"], 260, "lib")
    edge((270, 406), (270, 470))
    rt = ["libgfortran", "libgfortran5", "libgcc", "llvm-openmp", "_openmp_mutex"]
    assert set(rt) | {"pandas", "numpy", "python-dateutil", "python-tzdata", "libcxx",
                      "libblas", "libcblas", "liblapack", "libopenblas"} == set(added), added
    node(890, 470, "  ".join(rt[:3]), "+ " + "  ".join(rt[3:]), 620, "lib")
    edge((400, 508), (580, 508))
    save_canvas(fig, "viz_lasting_tree_pandas")


def env_waffle():
    """The packages of the environment `analysis` with pytest, on macOS: four
    asked for, the Python packages they need, and the rest."""
    d = env_data()
    pkgs = d["packages"]["osx-arm64"]["analysis+pytest"]
    asked = ["python", "matplotlib-base", "pandas", "pytest"]
    a, py, rest = kinds(pkgs, asked)
    W, H = 1600, 560
    fig, ax = canvas(W, H)
    cols, size, gap = 15, 62, 10
    order = [(n, "asked") for n in asked] + [(n, "py") for n in py] + [(n, "rest") for n in rest]
    for k, (name, kind) in enumerate(order):
        r, c = divmod(k, cols)
        x, y = c * (size + gap), 8 + r * (size + gap)
        if kind == "asked":
            box(ax, x, y, size, size, edge=ACC, fill=(125 / 255, 211 / 255, 252 / 255, 0.55), r=6, lw=2)
        elif kind == "py":
            box(ax, x, y, size, size, edge=FG2, fill=(0.76, 0.80, 0.85, 0.22), r=6, lw=1.4)
        else:
            box(ax, x, y, size, size, edge=HAIR, fill=PANEL, r=6, lw=1.2)
    x0 = cols * (size + gap) + 50
    groups = [(ACC, f"{len(a)} asked for", ", ".join(asked[:2]), ", ".join(asked[2:])),
              (FG2, f"{len(py)} Python packages", "they need: numpy, pillow,", "python-dateutil, pluggy, …"),
              (DIM, f"{len(rest)} other packages", "compiled libraries, fonts,", "certificates, time zones")]
    for k, (color, head, l1, l2) in enumerate(groups):
        y = 40 + k * 170
        box(ax, x0, y - 30, 34, 34, edge=color, fill=(125 / 255, 211 / 255, 252 / 255, 0.55) if k == 0
            else ((0.76, 0.80, 0.85, 0.22) if k == 1 else PANEL), r=5, lw=1.6)
        text(ax, x0 + 52, y - 3, head, size=30, color=FG, font=BOLD)
        text(ax, x0 + 52, y + 42, l1, size=24, color=FG2)
        text(ax, x0 + 52, y + 76, l2, size=24, color=FG2)
    save_canvas(fig, "viz_lasting_env")


def numpy_ranges():
    """The numpy releases on conda-forge since 1.25 and the range that each of
    three packages of the environment accepts; the newest release inside all
    three is the one the environment gets."""
    d = env_data()
    rel = [v for v, _ in d["releases"]["numpy"]]
    x = list(range(len(rel)))
    rows = [("matplotlib-base 3.11.2:  ≥ 1.25, < 3", lambda v: _vkey("1.25") <= _vkey(v) < _vkey("3")),
            ("contourpy 1.4.0:  ≥ 2.0", lambda v: _vkey(v) >= _vkey("2.0")),
            ("pandas 3.1.1:  ≥ 2.0.2", lambda v: _vkey(v) >= _vkey("2.0.2"))]
    fig, ax = plt.subplots(figsize=(9.4, 3.6))
    allowed_all = [all(f(v) for _, f in rows) for v in rel]
    for k, (name, f) in enumerate(rows + [("all three", None)]):
        y = len(rows) - k
        ok = allowed_all if f is None else [f(v) for v in rel]
        inside = [i for i, o in enumerate(ok) if o]
        ax.axhspan(y - 0.32, y + 0.32, xmin=0, xmax=1, color="none")
        if inside:
            ax.add_patch(Rectangle((inside[0] - 0.45, y - 0.28), inside[-1] - inside[0] + 0.9, 0.56,
                                   fc=(125 / 255, 211 / 255, 252 / 255, 0.16 if f else 0.30),
                                   ec=style.ACCENT if f is None else "none", lw=1.2))
        ax.scatter([i for i in x if ok[i]], [y] * sum(ok), s=26, color=style.ACCENT, zorder=3)
        ax.scatter([i for i in x if not ok[i]], [y] * (len(x) - sum(ok)), s=26,
                   facecolor="none", edgecolor=style.DIM, zorder=3)
        ax.text(-1.2, y, name, ha="right", va="center", fontsize=11,
                color=style.FG if f else style.ACCENT, fontweight="bold" if f is None else "normal")
    newest = max(i for i in x if allowed_all[i])
    ax.scatter([newest], [0], s=150, facecolor="none", edgecolor=style.FG, lw=1.6, zorder=4)
    ax.annotate(f"{rel[newest]}: the newest in all three", (newest, 0), xytext=(newest - 0.6, -0.95),
                ha="right", va="center", fontsize=11, color=style.FG,
                arrowprops=dict(arrowstyle="-", color=style.FG, lw=0.8))
    ticks = [i for i, v in enumerate(rel) if v.endswith(".0") and v.count(".") == 2]
    ax.set_xticks(ticks, [rel[i][:-2] for i in ticks])
    ax.set_yticks([])
    ax.set_ylim(-1.4, len(rows) + 0.6)
    ax.set_xlim(-0.8, len(rel) - 0.2)
    ax.set_xlabel(f"numpy releases on conda-forge, {rel[0]} to {rel[-1]} (in version order)")
    ax.spines["left"].set_visible(False)
    ax.grid(False)
    style.save(fig, "viz_lasting_numpy_ranges")


def pandas_versions():
    """The pandas releases on conda-forge since 2.0, by date; what three lines
    of environment.yml would give on 1 October 2025 and on 9 November 2026."""
    d = env_data()
    rel = [(v, date.fromisoformat(t)) for v, t in d["releases"]["pandas"]]
    series = sorted({tuple(v.split(".")[:2]) for v, _ in rel}, key=lambda s: (int(s[0]), int(s[1])))
    level = {s: k for k, s in enumerate(series)}

    def y_of(v):
        a, b, c = v.split(".")
        return level[(a, b)] + int(c) * 0.11

    fig, ax = plt.subplots(figsize=(9.4, 3.6))
    for v, t in rel:
        major3 = v.startswith("3.")
        ax.scatter([t], [y_of(v)], s=30, color=style.ACCENT if major3 else style.FG, zorder=3)
    lo, hi = y_of("2.3.0") - 0.12, y_of("2.3.3") + 0.12
    ax.axhspan(lo, hi, color=style.CYCLE[1], alpha=0.14, lw=0)
    ax.text(date(2023, 2, 1), (lo + hi) / 2, "pandas=2.3", va="center", fontsize=11,
            color=style.CYCLE[1], family="monospace")
    made, again = date(2025, 10, 1), date(2026, 11, 9)
    for t, txt in [(made, "made: 1 Oct 2025"), (again, "made again: 9 Nov 2026")]:
        ax.axvline(t, color=style.DIM, lw=1, ls=(0, (4, 3)))
        ax.text(t - timedelta(days=12), len(series) - 0.1, txt, ha="right", va="bottom",
                fontsize=10.5, color=style.DIM)
    newest_then = max((r for r in rel if r[1] <= made), key=lambda r: r[1])[0]
    newest_now = max((r for r in rel if r[1] <= again), key=lambda r: r[1])[0]
    for v, t, dx in [(newest_then, made, -12), (newest_now, again, -12)]:
        ax.annotate(v, (t, y_of(v)), xytext=(dx, 10), textcoords="offset points", ha="right",
                    fontsize=11, color=style.FG, fontweight="bold")
    ax.set_yticks(range(len(series)), [".".join(s) for s in series])
    ax.set_ylabel("pandas version")
    ax.set_ylim(-0.4, len(series) + 0.25)
    ax.set_xlim(date(2023, 1, 1), date(2027, 1, 15))
    ax.set_xticks([date(y, 1, 1) for y in range(2023, 2028)], [str(y) for y in range(2023, 2028)])
    ax.grid(axis="x")
    style.save(fig, "viz_lasting_pandas_versions")


def two_means():
    """Two single days: the mean of the 24 hours (Smiltė) against the midrange,
    halfway between the lowest and the highest hour (Ben)."""
    days = by_day()
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.6), sharey=False)
    for ax, day in zip(axes, DAYS):
        hours = [h for h, _ in days[day]]
        values = [t for _, t in days[day]]
        m, mid = mean(values), midrange(values)
        ax.plot(hours, values, "o-", color=style.FG, lw=1.2, ms=4, zorder=3)
        ax.axhline(m, color=style.ACCENT, lw=2)
        ax.axhline(mid, color=style.CYCLE[1], lw=2, ls=(0, (5, 3)))
        lo, hi = values.index(min(values)), values.index(max(values))
        for i in (lo, hi):
            ax.scatter([hours[i]], [values[i]], s=70, facecolor="none", edgecolor=style.CYCLE[1],
                       lw=1.6, zorder=4)
        up = 0.12 * (max(values) - min(values)) / 6
        ax.text(0.2, m + (up if m > mid else -up), f"mean {m:.2f}", color=style.ACCENT, fontsize=11,
                va="bottom" if m > mid else "top", ha="left")
        ax.text(0.2, mid + (-up if m > mid else up), f"midrange {mid:.2f}", color=style.CYCLE[1],
                fontsize=11, va="top" if m > mid else "bottom", ha="left")
        dt = date.fromisoformat(day)
        ax.set_title(f"{dt.day} {dt.strftime('%B')} {dt.year}", fontsize=13)
        ax.set_xticks([0, 6, 12, 18, 23])
        ax.set_xlabel("hour of the day")
        ax.set_xlim(-0.8, 23.8)
    axes[0].set_ylabel("temperature (°C)")
    style.save(fig, "viz_lasting_two_means")


FIGURES = {
    "viz_lasting_project": project,
    "viz_lasting_tree_pandas": tree_pandas,
    "viz_lasting_env": env_waffle,
    "viz_lasting_numpy_ranges": numpy_ranges,
    "viz_lasting_pandas_versions": pandas_versions,
    "viz_lasting_two_means": two_means,
}


# ---------------------------------------------------------------------------
# Every number of the slides
# ---------------------------------------------------------------------------

def report():
    four = temps_of_lines(SIX)
    print("== the six hours of 21 July 2019")
    print("four measured:", four)
    print("by hand: 101.1 / 4 = 25.275; with -999:", (101.1 - 1998) / 6)
    print("sum() (Python 3.12 and later):", repr(sum(four)), "mean", repr(mean(four)),
          "== 25.275:", mean(four) == 25.275)
    print("one after the other (Python 3.11):", repr(loop_sum(four)), "mean",
          repr(loop_sum(four) / 4), "== 25.275:", loop_sum(four) / 4 == 25.275)
    print("difference:", repr(mean(four) - 25.275), " |diff| < 1e-9:", abs(mean(four) - 25.275) < 1e-9)
    print("27.3 as stored:", Decimal(27.3))
    print("25.275 as stored:", Decimal(25.275))
    print("sum as stored:", Decimal(sum(four)), " exact sum of the four floats:",
          sum(Decimal(v) for v in four))
    six = [temp_of(l) for l in SIX]
    print("mean of all six (-999 left in):", repr(mean(six)), " |diff|:", abs(mean(six) - 25.275))
    print("midrange of the four:", repr(midrange(four)), " (23.6 + 27.3) / 2")
    print("the humidity of the four (column taken by mistake):",
          mean([float(l.split(",")[2]) for l in SIX[:4]]))

    print("\n== the whole log")
    lines = read_lines(PATH)
    values = temps_of_lines(lines)
    print("rows", len(lines), "measured", len(values))
    print("mean, sum() of 3.12+:", repr(mean(values)), " one after the other (3.11):",
          repr(loop_sum(values) / len(values)))
    print("sums:", repr(sum(values)), repr(loop_sum(values)))
    every = [temp_of(l) for l in lines]
    print("mean of every row, -999 included (Tomas):", mean(every))
    print("humidity column taken by mistake:", round(mean([float(l.split(",")[2]) for l in lines]), 2))
    days = by_day()
    mids = [midrange([t for _, t in v]) for v in days.values()]
    means = [mean([t for _, t in v]) for v in days.values()]
    print("days with a measured hour", len(days), " Ben, the mean of the midranges:", mean(mids))
    diffs = [a - b for a, b in zip(mids, means)]
    print("midrange - mean per day: mean", round(mean(diffs), 3), "min", round(min(diffs), 2),
          "max", round(max(diffs), 2), "days below:", sum(1 for x in diffs if x < 0))
    for day in DAYS:
        v = [t for _, t in days[day]]
        print(day, "hours", len(v), "mean", round(mean(v), 3), "midrange", midrange(v),
              "min", min(v), "max", max(v))

    print("\n== the perceptron of Lecture 10 (w1 = -1, w2 = 0, b = 3.8)")
    ev = evenings()
    frost = sum(1 for e in ev if e[3] < 0)
    right = sum(1 for e in ev if predict(e[1], e[2]) == (1 if e[3] < 0 else 0))
    print("evenings", len(ev), "frost", frost, "never frost right:", round(1 - frost / len(ev), 3),
          "below 3.8 right:", right, round(right / len(ev), 3))
    for e in ev:
        if e[0] in EVENINGS:
            z = W1 * e[1] + W2 * e[2] / 100 + B
            print(e[0], "18:00 x1", e[1], "x2", e[2] / 100, "z", round(z, 2), "predict",
                  predict(e[1], e[2]), "next 06:00", e[3])
    print("a new Perceptron(): w = [0, 0], b = 0, z = 0 for 8 Dec 2025: predict 0")
    print("model.json:", json.dumps({"w": [W1, W2], "b": B}))

    print("\n== rebuild.sh, its outputs and their checksums")
    out = rebuild_outputs()
    for rel in ["data/processed/weather_valid.csv", "data/processed/daily.csv", "results/temp_c.txt"]:
        b = out[rel]
        print(f"{hashlib.sha256(b).hexdigest()}  {rel}  {len(b)} bytes, {b.count(b'\n')} lines")
    print("temp_c.txt with CRLF, as Windows writes it:", len(out["results/temp_c.txt"].replace(b"\n", b"\r\n")),
          "bytes", hashlib.sha256(out["results/temp_c.txt"].replace(b"\n", b"\r\n")).hexdigest()[:8])
    print("results/temp_c.txt:\n" + out["results/temp_c.txt"].decode(), end="")
    print("column_stats.py on the raw file (Tomas):\n" + out["tomas"].decode(), end="")
    print("sha256 of the raw file:", hashlib.sha256(PATH.read_bytes()).hexdigest(),
          len(PATH.read_bytes()), "bytes")

    print("\n== conda-forge (fetched", env_data()["fetched"] + ")")
    d = env_data()
    for plat in PLATFORMS:
        print(plat, d["counts"][plat])
    for plat in ["osx-arm64", "win-64"]:
        pk = _names(d["packages"][plat]["python+pandas"])
        base = _names(d["packages"][plat]["python"])
        print(plat, "python=3.14 pandas=3.1 adds", sorted(set(pk) - set(base)))
        a, py, rest = kinds(d["packages"][plat]["analysis+pytest"],
                            ["python", "matplotlib-base", "pandas", "pytest"])
        print(plat, "analysis + pytest:", len(a) + len(py) + len(rest), "asked", len(a),
              "python packages", len(py), sorted(py), "other", len(rest))
        env = _names(d["packages"][plat]["analysis+pytest"])
        for n in ["python", "numpy", "pandas", "matplotlib-base", "pytest", "pluggy",
                  "python-dateutil"]:
            print("   ", n, env[n][1], [x for x in env[n][2] if x.split()[0] in
                                       ("numpy", "python-dateutil", "pluggy", "packaging")])
        for n in env:
            nums = [x for x in env[n][2] if x.split()[0] == "numpy"]
            if nums:
                print("    needs numpy:", n, env[n][1], nums)
        old = _names(d["packages"][plat]["python+pandas=2.3"])
        p311 = _names(d["packages"][plat]["python3.11+pandas"])
        print(plat, "python=3.14 pandas=2.3 ->", old["pandas"][1], "numpy", old["numpy"][1],
              "| python=3.11 pandas=3.1 -> numpy", p311["numpy"][1], "python", p311["python"][1])
        pyt = sorted(set(_names(d["packages"][plat]["analysis+pytest"])) -
                     set(_names(d["packages"][plat]["python+pandas"])) -
                     set(_names(d["packages"][plat]["python"])))
    for pkg, rel in d["releases"].items():
        print(pkg, len(rel), "releases from", rel[0], "to", rel[-1])
    rel = d["releases"]["pandas"]
    for when in ["2025-10-01", "2026-11-09"]:
        newest = max((r for r in rel if r[1] <= when), key=lambda r: r[1])
        print("newest pandas on", when, newest)
    print("pandas 2.3.x:", [r for r in rel if r[0].startswith("2.3.")])
    nrel = d["releases"]["numpy"]
    print("numpy 2.0.2 to 2.5.4 releases:", sum(1 for v, _ in nrel if _vkey("2.0.2") <= _vkey(v) < _vkey("3")))


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch()
    else:
        report()
