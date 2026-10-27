"""Lecture 06 (Git): every diagram of the deck, drawn in the course style.

Hairline panels like the deck's cards, text in Space Grotesk and Space Mono
(embedded as outlines, like every course figure), the deck's cyan for what
a step moves or adds, amber only for a second person's change or a warning.
Every id, name and number is the one on the slides, from
misc/l05_scratch_repo/build.sh.

The canvas is laid out in pixels (100 per inch, y downwards), so the sizes
below read as on a 1600-pixel-wide figure, shown at about 0.6 to 0.7 on a
slide: text of 24 px and more stays readable on a projector.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon

import style

FONTS = Path(__file__).resolve().parents[1] / "fonts" / "git"
SANS = FontProperties(fname=FONTS / "SpaceGrotesk-Medium.ttf")
BOLD = FontProperties(fname=FONTS / "SpaceGrotesk-Bold.ttf")
MONO = FontProperties(fname=FONTS / "SpaceMono-Regular.ttf")
MONOB = FontProperties(fname=FONTS / "SpaceMono-Bold.ttf")

# the deck's tokens (lectures/content/theme/styles/tokens.css)
FG, FG2, DIM = "#f2f5f9", "#c3ccd8", "#8b97a6"
ACC, WARN = "#7dd3fc", "#fbbf24"
BG = "#050507"
HAIR = (139 / 255, 151 / 255, 166 / 255, 0.26)
HAIR_SOFT = (139 / 255, 151 / 255, 166 / 255, 0.16)
LINE = (139 / 255, 151 / 255, 166 / 255, 0.55)
PANEL = (1, 1, 1, 0.02)
ACC_FILL = (125 / 255, 211 / 255, 252 / 255, 0.10)
WARN_FILL = (251 / 255, 191 / 255, 36 / 255, 0.10)
PT = 0.72  # points per canvas pixel


def _rgb(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) / 255 for i in (0, 2, 4))


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
    text(ax, x, y, " ".join(s.upper()).replace("   ", "   "),
         size=size, color=color, font=BOLD, ha=ha)


def box(ax, x, y, w, h, edge=HAIR, fill=PANEL, r=9, lw=1.3, ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fill, ec=edge, lw=lw, ls=ls))


def arrow(ax, a, b, color=ACC, lw=2.6, rad=0.0, ls="-", head=16, both=False):
    st = f"{'<|' if both else ''}-|>,head_length={head * PT:.1f},head_width={head * PT * 0.45:.1f}"
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=st, color=color, lw=lw, ls=ls,
                                 connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0,
                                 mutation_scale=1, capstyle="round", joinstyle="round"))


def cmd(ax, x, y, s, color=ACC, size=27, bg=True):
    """A command in mono; with bg, on a small dark plate centred on y, so an
    arrow through y passes behind it."""
    w = len(s) * size * 0.6 + 28
    if bg:
        box(ax, x - w / 2, y - size * 0.78, w, size * 1.56, edge=(*_rgb(color), 0.5),
            fill=(0.02, 0.02, 0.03, 0.97), r=6, lw=1.2)
    text(ax, x, y + size * 0.36, s, size=size, color=color, font=MONOB, ha="center")


def sheet(ax, x, y, w=28, h=38, color=DIM, lw=1.7):
    f = w * 0.32
    ax.add_patch(Polygon([(x, y), (x + w - f, y), (x + w, y + f), (x + w, y + h), (x, y + h)],
                         closed=True, fc="none", ec=color, lw=lw, joinstyle="round"))
    ax.plot([x + w - f, x + w - f, x + w], [y, y + f, y + f], color=color, lw=lw)


def folder(ax, x, y, w=38, h=32, color=DIM, lw=1.7):
    ax.add_patch(Polygon([(x, y + 6), (x + w * 0.38, y + 6), (x + w * 0.48, y + 12),
                          (x + w, y + 12), (x + w, y + h), (x, y + h)],
                         closed=True, fc="none", ec=color, lw=lw, joinstyle="round"))


def _fill(color):
    return {ACC: ACC_FILL, WARN: WARN_FILL}.get(color, PANEL)


def file_chip(ax, x, y, name, w=330, sub=None, new=False, kind="file", color=None):
    color = color or (ACC if new else None)
    h = 92 if sub else 66
    box(ax, x, y, w, h, edge=color or HAIR, fill=_fill(color), r=6, lw=2.2 if color else 1.3)
    ic = color or DIM
    if kind == "file":
        sheet(ax, x + 18, y + 13, color=ic)
    else:
        folder(ax, x + 16, y + 12, color=ic)
    text(ax, x + 66, y + 43, name, size=30, font=MONO)
    if sub:
        text(ax, x + 66, y + 78, sub, size=24, color=FG2)


def commit_chip(ax, x, y, cid, msg, w=330, new=False, color=None):
    color = color or (ACC if new else None)
    box(ax, x, y, w, 92, edge=color or HAIR, fill=_fill(color), r=6, lw=2.2 if color else 1.3)
    ax.add_patch(Circle((x + 30, y + 46), 11, fc="none", ec=color or FG2, lw=2.4))
    text(ax, x + 58, y + 42, cid, size=30, font=MONOB)
    text(ax, x + 58, y + 77, msg, size=24, color=FG2)


def empty(ax, x, y, s, w=330, h=66):
    box(ax, x, y, w, h, edge=HAIR_SOFT, fill="none", r=6, lw=1.3, ls=(0, (4, 4)))
    text(ax, x + w / 2, y + h / 2 + 9, s, size=24, color=DIM, ha="center", style="italic")


# ---- the four places -------------------------------------------------------------
PLACES = [("Working folder", "the files you edit"), ("Staging area", "the next commit"),
          ("Repository", "the commits, in .git"), ("GitHub", "a copy on a server")]
COLX = [0, 413, 827, 1240]
COLW = 360
CX = 15


def _cx(i):
    return COLX[i] + COLW / 2


def _heads(ax):
    for (name, sub), x in zip(PLACES, COLX):
        box(ax, x, 2, COLW, 120)
        label(ax, x + 24, 50, name)
        text(ax, x + 24, 96, sub, size=27, color=FG2)


def places():
    fig, ax = canvas(1600, 330)
    _heads(ax)
    for i, s in enumerate(["git add", "git commit", "git push"]):
        arrow(ax, (_cx(i) + 30, 192), (_cx(i + 1) - 30, 192))
        cmd(ax, (_cx(i) + _cx(i + 1)) / 2, 192, s)
    for x0, x1, s in [(COLX[0], COLX[2] + COLW, "on the laptop: only you see it"),
                      (COLX[3], COLX[3] + COLW, "on a server: shared")]:
        ax.plot([x0, x0, x1, x1], [250, 264, 264, 250], color=LINE, lw=1.4)
        text(ax, (x0 + x1) / 2, 310, s, size=27, color=FG2, ha="center")
    style.save(fig, "git_places", tight=False)


TOP = 84


def columns(ax, height=236):
    for (name, _), x in zip(PLACES, COLX):
        box(ax, x, TOP, COLW, height)
        label(ax, x + 22, TOP + 44, name)


def step_arrow(ax, i, j, s):
    """The command of the figure, on a straight arrow above the columns."""
    y = TOP - 42
    arrow(ax, (_cx(i) + 30, y), (_cx(j) - 30, y))
    cmd(ax, (_cx(i) + _cx(j)) / 2, y, s)


def _project(ax):
    file_chip(ax, COLX[0] + CX, TOP + 68, "README.md")
    file_chip(ax, COLX[0] + CX, TOP + 148, "data/ scripts/", kind="folder")


def git_add():
    fig, ax = canvas(1600, 330)
    columns(ax)
    _project(ax)
    file_chip(ax, COLX[1] + CX, TOP + 68, "README.md", sub="as saved just now", new=True)
    empty(ax, COLX[2] + CX, TOP + 68, "no commit yet")
    empty(ax, COLX[3] + CX, TOP + 68, "no remote yet")
    step_arrow(ax, 0, 1, "git add")
    style.save(fig, "git_add", tight=False)


def git_commit():
    fig, ax = canvas(1600, 330)
    columns(ax)
    _project(ax)
    empty(ax, COLX[1] + CX, TOP + 68, "same as the commit")
    commit_chip(ax, COLX[2] + CX, TOP + 68, "c08a1c7", "Add the README", new=True)
    empty(ax, COLX[3] + CX, TOP + 68, "no remote yet")
    step_arrow(ax, 1, 2, "git commit")
    style.save(fig, "git_commit", tight=False)


def git_push():
    fig, ax = canvas(1600, 330)
    columns(ax)
    _project(ax)
    file_chip(ax, COLX[1] + CX, TOP + 68, "README.md", sub="staged, not sent", color=WARN)
    for c in (2, 3):
        commit_chip(ax, COLX[c] + CX, TOP + 68, "2eb3b1c", "and 7 commits before", new=(c == 3))
    step_arrow(ax, 2, 3, "git push")
    style.save(fig, "git_push", tight=False)


def git_pull():
    fig, ax = canvas(1600, 310)
    _heads(ax)
    arrow(ax, (_cx(3) - 30, 186), (_cx(2) + 30, 186))
    cmd(ax, (_cx(2) + _cx(3)) / 2, 186, "git fetch")
    arrow(ax, (_cx(2) - 30, 186), (_cx(0) + 30, 186))
    cmd(ax, (_cx(0) + _cx(2)) / 2, 186, "git merge")
    x0, x1 = _cx(0), _cx(3)
    ax.plot([x0, x0, x1, x1], [238, 252, 252, 238], color=LINE, lw=1.4)
    text(ax, (x0 + x1) / 2, 296, "git pull: both, one after the other", size=27, color=FG2, ha="center")
    style.save(fig, "git_pull", tight=False)


def flow():
    fig, ax = canvas(1600, 640)
    for (name, sub), x in zip(PLACES, COLX):
        box(ax, x, 2, COLW, 630)
        label(ax, x + 24, 50, name)
        text(ax, x + 24, 94, sub, size=26, color=FG2)
    rows = [(0, 1, "git add", 170), (1, 2, "git commit", 170), (2, 3, "git push", 170),
            (3, 2, "git fetch", 262), (2, 0, "git merge", 354)]
    for i, j, s, y in rows:
        d = 1 if j > i else -1
        arrow(ax, (_cx(i) + 26 * d, y), (_cx(j) - 26 * d, y))
        cmd(ax, (_cx(i) + _cx(j)) / 2, y, s)
    arrow(ax, (_cx(3), 418), (_cx(0), 418), rad=-0.10)
    cmd(ax, (_cx(0) + _cx(3)) / 2, 488, "git pull")
    for i, j, s in [(0, 1, "git diff"), (1, 2, "git diff --staged")]:
        cmd(ax, (_cx(i) + _cx(j)) / 2, 560, s, color=FG2, bg=False)
        arrow(ax, (_cx(i) + 26, 598), (_cx(j) - 26, 598), color=FG2, lw=1.8, ls=(0, (5, 4)), both=True)
    style.save(fig, "git_flow", tight=False)


# ---- the opening: a file as a sequence of changes, two versions, a merge ----------
def _page(ax, x, y, lines, w=150, h=190, marks=()):
    marks = dict(marks)
    box(ax, x, y, w, h, edge=HAIR, fill=PANEL, r=6)
    for k in range(lines):
        c = marks.get(k)
        yy = y + 30 + k * 22
        ax.plot([x + 20, x + w - 20 - (30 if k % 3 == 2 else 0)], [yy, yy],
                color=c or DIM, lw=4 if c else 3, solid_capstyle="round", alpha=1 if c else 0.7)


def changes():
    fig, ax = canvas(1600, 290)
    steps = [("Smiltė · 10:25", "Add the data and the scripts", None, None),
             ("Tomas · 11:30", "Correct 1 October to 6,4", ("- 1;2025-10-01;6,3", "+ 1;2025-10-01;6,4"), WARN),
             ("Smiltė · 12:50", "Revert “Correct|1 October to 6,4”", ("- 1;2025-10-01;6,4", "+ 1;2025-10-01;6,3"), ACC)]
    xs = [0, 560, 1120]
    for (who, msg, diff, col), x in zip(steps, xs):
        box(ax, x, 2, 480, 284)
        label(ax, x + 24, 46, who, size=22)
        for k, part in enumerate(msg.split("|")):
            text(ax, x + 24, 92 + 36 * k, part, size=29)
        if diff:
            for k, line in enumerate(diff):
                text(ax, x + 24, 200 + 34 * k, line, size=26, font=MONO, color=(DIM if k == 0 else col))
            text(ax, x + 24, 266, "daily_export.csv, line 2", size=22, color=FG2)
        else:
            text(ax, x + 24, 200, "daily_export.csv", size=27, font=MONO, color=FG2)
            text(ax, x + 24, 236, "11 lines, as received", size=24, color=FG2)
        if x != xs[-1]:
            arrow(ax, (x + 492, 144), (x + 548, 144), color=FG2, lw=2.4)
    style.save(fig, "git_changes", tight=False)


def versions():
    fig, ax = canvas(760, 570)
    _page(ax, 40, 185, 6)
    label(ax, 115, 162, "start", ha="center", size=28)
    _page(ax, 520, 20, 6, marks={1: ACC, 2: ACC})
    _page(ax, 520, 330, 6, marks={4: WARN})
    text(ax, 595, 244, "Smiltė", size=32, color=ACC, ha="center")
    text(ax, 595, 554, "Tomas", size=32, color=WARN, ha="center")
    arrow(ax, (205, 260), (505, 120), color=FG2, lw=2.2)
    arrow(ax, (205, 300), (505, 420), color=FG2, lw=2.2)
    style.save(fig, "git_versions", tight=False)


def merge():
    fig, ax = canvas(760, 570)
    _page(ax, 40, 20, 6, marks={1: ACC, 2: ACC})
    _page(ax, 40, 330, 6, marks={4: WARN})
    _page(ax, 560, 185, 6, marks={1: ACC, 2: ACC, 4: WARN})
    label(ax, 635, 162, "merged", ha="center", size=28)
    arrow(ax, (205, 120), (545, 250), color=FG2, lw=2.2)
    arrow(ax, (205, 420), (545, 310), color=FG2, lw=2.2)
    style.save(fig, "git_merge", tight=False)


# ---- Tracking Changes: commit the rest; Undoing: restore ----------------------------
def commit_rest():
    fig, ax = canvas(860, 500)
    box(ax, 0, 2, 440, 494)
    label(ax, 24, 48, "Staging area", size=26)
    names = ["daily_export.csv", "weather.csv", "clean_export.py", "column_stats.py", "rebuild.sh"]
    for k, n in enumerate(names):
        file_chip(ax, 24, 76 + k * 82, n, w=392)
    commit_chip(ax, 530, 224, "a9f65a6", "one commit, 5 files", w=330, new=True)
    arrow(ax, (452, 270), (522, 270))
    cmd(ax, 695, 184, "git commit")
    style.save(fig, "git_commit_rest", tight=False)


def restore():
    fig, ax = canvas(800, 330)
    cmd(ax, 400, 30, "git restore README.md")
    for x, name in [(0, "Working folder"), (440, "Staging area")]:
        box(ax, x, 72, 360, 256)
        label(ax, x + 22, 116, name, size=24)
    file_chip(ax, 18, 144, "README.md", w=324, sub="11 lines deleted", color=WARN)
    file_chip(ax, 458, 144, "README.md", w=324, sub="as in 15505c4")
    text(ax, 460, 290, "= the last commit", size=25, color=FG2)
    arrow(ax, (452, 190), (348, 190))
    style.save(fig, "git_restore", tight=False)


# ---- Remotes -------------------------------------------------------------------------
def _repo(ax, x, y, w, h, title, sub, commits, hl=False):
    box(ax, x, y, w, h)
    label(ax, x + 22, y + 44, title, size=24)
    text(ax, x + 22, y + 84, sub, size=24, font=MONO, color=FG2)
    if not commits:
        empty(ax, x + 22, y + 110, "no commits", w=w - 44)
    for k, c in enumerate(commits):
        yy = y + 142 + 46 * k
        if c.startswith("…"):
            text(ax, x + 30, yy, c, size=27, font=MONO, color=FG2)
            continue
        ax.add_patch(Circle((x + 38, yy - 10), 9, fc="none", ec=ACC if hl else FG2, lw=2.4))
        if k:
            ax.plot([x + 38, x + 38], [yy - 46 - 1, yy - 19], color=LINE, lw=1.8)
        text(ax, x + 62, yy, c, size=27, font=MONO)


ROWS = ["2eb3b1c", "172f06a", "… 8 in all"]


def remote_empty():
    fig, ax = canvas(780, 300)
    _repo(ax, 0, 2, 350, 296, "Smiltė's laptop", "weather-project", ROWS)
    _repo(ax, 430, 2, 350, 296, "GitHub", "smilte-example/…", [])
    style.save(fig, "git_remote_empty", tight=False)


def remote_pushed():
    fig, ax = canvas(780, 300)
    _repo(ax, 0, 2, 350, 296, "Smiltė's laptop", "weather-project", ROWS)
    _repo(ax, 430, 2, 350, 296, "GitHub", "smilte-example/…", ROWS, hl=True)
    arrow(ax, (356, 150), (424, 150))
    style.save(fig, "git_remote_pushed", tight=False)


def remote_clone():
    fig, ax = canvas(1600, 290)
    for k, (title, sub, hl) in enumerate([("Smiltė's laptop", "weather-project", False),
                                          ("GitHub", "smilte-example/…", False),
                                          ("Tomas's laptop", "weather-project", True)]):
        _repo(ax, 575 * k, 2, 450, 286, title, sub, ROWS, hl=hl)
    for k, s in enumerate(["push", "clone"]):
        x0 = 450 + 575 * k
        arrow(ax, (x0 + 18, 160), (x0 + 107, 160))
        text(ax, x0 + 62, 132, s, size=24, font=MONOB, color=ACC, ha="center")
    style.save(fig, "git_remote_clone", tight=False)


# ---- Working Together -------------------------------------------------------------
def _node(ax, x, y, w, title, sub, dashed=False):
    box(ax, x, y, w, 108, ls=(0, (5, 4)) if dashed else "-")
    label(ax, x + 22, y + 44, title, size=24)
    text(ax, x + 22, y + 86, sub, size=25, font=MONO, color=FG2)


def _updown(ax, x, up, down, top=118, bottom=330):
    """Two vertical arrows: up (cyan) on the left, down (grey) on the right."""
    arrow(ax, (x - 22, bottom - 6), (x - 22, top + 6))
    arrow(ax, (x + 22, top + 6), (x + 22, bottom - 6), color=FG2)
    mid = (top + bottom) / 2 + 9
    text(ax, x - 38, mid, up, size=26, font=MONOB, color=ACC, ha="right")
    text(ax, x + 38, mid, down, size=26, font=MONOB, color=FG2)


def ways_shared():
    fig, ax = canvas(780, 450)
    _node(ax, 0, 2, 780, "GitHub", "smilte-example/weather-project")
    _node(ax, 0, 338, 350, "Smiltė", "a clone")
    _node(ax, 430, 338, 350, "Tomas", "a clone")
    _updown(ax, 175, "push", "pull", top=112, bottom=336)
    _updown(ax, 605, "push", "pull", top=112, bottom=336)
    style.save(fig, "git_ways_shared", tight=False)


def ways_fork():
    fig, ax = canvas(780, 450)
    _node(ax, 0, 2, 330, "Smiltė's", "smilte-example/…")
    _node(ax, 450, 2, 330, "Rūta's fork", "ruta-example/…", dashed=True)
    arrow(ax, (336, 40), (444, 40), color=FG2, lw=2.2)
    text(ax, 390, 82, "fork", size=24, font=MONOB, color=FG2, ha="center")
    _node(ax, 450, 338, 330, "Rūta", "a clone")
    _updown(ax, 615, "push", "clone", top=112, bottom=336)
    arrow(ax, (470, 116), (190, 116), color=WARN, rad=-0.55, ls=(0, (6, 4)))
    text(ax, 330, 262, "pull request", size=26, font=MONOB, color=WARN, ha="center")
    style.save(fig, "git_ways_fork", tight=False)


# ---- histories (old on the left, new on the right) ---------------------------------
def _dot(ax, p, color=FG2):
    ax.add_patch(Circle(p, 15, fc=BG, ec=color, lw=3, zorder=3))


def _edge(ax, a, b):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=LINE, lw=2.4, zorder=1)


def history_refused():
    fig, ax = canvas(780, 380)
    for y, name in [(2, "GitHub"), (196, "Smiltė's laptop")]:
        box(ax, 0, y, 780, 178)
        label(ax, 22, y + 42, name, size=22)
    for y, cid, who, col in [(110, "7abaa0d", "Tomas", WARN), (304, "94dccdc", "Smiltė", ACC)]:
        _edge(ax, (300, y), (520, y))
        _dot(ax, (300, y))
        text(ax, 300, y + 52, "f2546ed", size=26, font=MONOB, ha="center")
        _dot(ax, (520, y), col)
        text(ax, 505, y + 52, f"{cid}  {who}", size=26, font=MONOB, color=col)
    style.save(fig, "git_refused", tight=False)


def history_merged():
    fig, ax = canvas(780, 300)
    a, s, t, m = (40, 150), (300, 50), (300, 250), (560, 150)
    for p, q in [(a, s), (a, t), (s, m), (t, m)]:
        _edge(ax, p, q)
    _dot(ax, a)
    text(ax, a[0] - 15, a[1] + 50, "f2546ed", size=26, font=MONOB)
    _dot(ax, s, ACC)
    text(ax, s[0] + 30, s[1] + 10, "94dccdc  Smiltė", size=26, font=MONOB, color=ACC)
    _dot(ax, t, WARN)
    text(ax, t[0] + 30, t[1] + 10, "7abaa0d  Tomas", size=26, font=MONOB, color=WARN)
    _dot(ax, m, ACC)
    text(ax, m[0] + 30, m[1] + 10, "6dd93ad", size=26, font=MONOB)
    text(ax, m[0] + 30, m[1] + 44, "the merge", size=24, color=FG2)
    style.save(fig, "git_merged", tight=False)


def history_pr():
    fig, ax = canvas(1600, 250)
    a, r, m = (190, 70), (760, 190), (1330, 70)
    for p, q in [(a, m), (a, r), (r, m)]:
        _edge(ax, p, q)
    label(ax, 0, 79, "main", size=22)
    label(ax, 0, 199, "ranges", size=22)
    _dot(ax, a)
    text(ax, a[0] + 30, a[1] - 24, "6dd93ad", size=26, font=MONOB)
    _dot(ax, r, WARN)
    text(ax, r[0] + 30, r[1] + 10, "6e10712  Rūta: Give the range of each column", size=26, font=MONO, color=WARN)
    _dot(ax, m, ACC)
    text(ax, m[0] - 30, m[1] - 24, "2c8f8b0  Merge pull request #1", size=26, font=MONOB, color=ACC, ha="right")
    style.save(fig, "git_pr_merged", tight=False)


# ---- For the Curious: one commit as objects, history, a branch ----------------------
OW = 300
OH = 118


def _obj(ax, x, y, kind, oid, name=None, color=None):
    box(ax, x, y, OW, OH, edge=color or HAIR, fill=_fill(color), r=6, lw=2.2 if color else 1.3)
    label(ax, x + 18, y + 32, kind, size=19)
    text(ax, x + 18, y + 70, oid, size=26, font=MONOB)
    if name:
        text(ax, x + 18, y + 102, name, size=23, font=MONO, color=FG2)


def commit_tree():
    fig, ax = canvas(1600, 560)
    X = [0, 325, 650, 975, 1300]
    mid = OH / 2
    _obj(ax, X[0], 200, "commit", "a9f65a6", "the data …", color=ACC)
    _obj(ax, X[0], 430, "commit", "ef28e40")
    arrow(ax, (X[0] + 150, 322), (X[0] + 150, 424), color=FG2, lw=2)
    text(ax, X[0] + 166, 382, "parent", size=20, color=DIM)
    _obj(ax, X[1], 200, "tree", "b9c01664", "the project")
    arrow(ax, (X[0] + OW + 4, 200 + mid), (X[1] - 4, 200 + mid), color=FG2, lw=2)
    kids = [(0, "blob", "5b35420e", "README.md"), (140, "blob", "3febadb2", ".gitignore"),
            (290, "tree", "d87619c9", "data"), (430, "tree", "d824278b", "scripts")]
    for y, k, oid, name in kids:
        _obj(ax, X[2], y, k, oid, name)
        arrow(ax, (X[1] + OW + 4, 200 + mid), (X[2] - 4, y + mid), color=LINE, lw=1.8)
    _obj(ax, X[3], 290, "tree", "ee85972a", "raw")
    arrow(ax, (X[2] + OW + 4, 290 + mid), (X[3] - 4, 290 + mid), color=LINE, lw=1.8)
    _obj(ax, X[3], 430, "blob", "eb2b25d9", "rebuild.sh")
    arrow(ax, (X[2] + OW + 4, 430 + mid), (X[3] - 4, 430 + mid), color=LINE, lw=1.8)
    for y, oid, name, col in [(200, "f811f73d", "weather.csv", ACC), (380, "0799b86b", "daily_export.csv", None)]:
        _obj(ax, X[4], y, "blob", oid, name, color=col)
        arrow(ax, (X[3] + OW + 4, 290 + mid), (X[4] - 4, y + mid), color=LINE, lw=1.8)
    style.save(fig, "git_commit_tree", tight=False)


def history():
    fig, ax = canvas(1600, 290)
    cs = [("c08a1c7", ["Add the README"], "5793d65f"), ("e3f4e26", ["Add .gitignore"], "b04cfd3c"),
          ("ef28e40", ["Keep the committed", "bytes …"], "e3fe0a2e"),
          ("a9f65a6", ["Add the data and", "the scripts"], "b9c01664")]
    xs = [0, 410, 820, 1230]
    for k, ((cid, msg, tree), x) in enumerate(zip(cs, xs)):
        new = k == 3
        box(ax, x, 2, 370, 230, edge=ACC if new else HAIR, fill=_fill(ACC if new else None), r=6,
            lw=2.2 if new else 1.3)
        text(ax, x + 22, 52, cid, size=30, font=MONOB)
        for n, part in enumerate(msg):
            text(ax, x + 22, 96 + 32 * n, part, size=25, color=FG2)
        text(ax, x + 22, 208, f"tree {tree}", size=24, font=MONO, color=DIM)
        if k:
            arrow(ax, (x - 4, 120), (xs[k - 1] + 374, 120), color=FG2, lw=2.2, head=13)
    text(ax, 0, 280, "older", size=23, color=DIM)
    text(ax, 1600, 280, "newer", size=23, color=DIM, ha="right")
    text(ax, 800, 280, "each arrow: parent", size=23, color=DIM, ha="center")
    style.save(fig, "git_history", tight=False)


def _branch(name, ids):
    fig, ax = canvas(780, 210)
    xs = [60, 340, 620]
    for k in range(2):
        _edge(ax, (xs[k], 150), (xs[k + 1], 150))
    for k, (x, cid) in enumerate(zip(xs, ids)):
        _dot(ax, (x, 150), ACC if k == 2 else FG2)
        text(ax, x, 202, cid, size=26, font=MONOB, ha="center")
    box(ax, xs[-1] - 62, 2, 124, 52, edge=ACC, fill=ACC_FILL, r=6, lw=2)
    text(ax, xs[-1], 38, "main", size=26, font=MONOB, color=ACC, ha="center")
    arrow(ax, (xs[-1], 58), (xs[-1], 128), lw=2.2, head=12)
    style.save(fig, name, tight=False)


def branch_a():
    _branch("git_branch_a", ["e3f4e26", "ef28e40", "a9f65a6"])


def branch_b():
    _branch("git_branch_b", ["ef28e40", "a9f65a6", "15505c4"])


FIGURES = {
    "git_places": places, "git_add": git_add, "git_commit": git_commit, "git_push": git_push,
    "git_pull": git_pull, "git_flow": flow, "git_changes": changes, "git_versions": versions,
    "git_merge": merge, "git_commit_rest": commit_rest, "git_restore": restore,
    "git_remote_empty": remote_empty, "git_remote_pushed": remote_pushed,
    "git_remote_clone": remote_clone, "git_ways_shared": ways_shared, "git_ways_fork": ways_fork,
    "git_refused": history_refused, "git_merged": history_merged, "git_pr_merged": history_pr,
    "git_commit_tree": commit_tree, "git_history": history,
    "git_branch_a": branch_a, "git_branch_b": branch_b,
}

if __name__ == "__main__":
    style.use()
    for fn in FIGURES.values():
        fn()
