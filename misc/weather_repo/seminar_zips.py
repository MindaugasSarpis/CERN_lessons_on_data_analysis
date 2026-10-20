#!/usr/bin/env python3
"""The starting folder of every seminar, as weather-sNN.zip.

Since 18 Oct 2026 every seminar is self-contained: it starts from its own
folder, downloaded from the release `seminar-files` of weather-project, and
never from what an earlier seminar left on a laptop (lecturer: "especially
if someone skips a seminar, and it's also easier for me"). Since 20 Oct 2026
Seminars 1 to 5 download nothing: the room types its data from the page, so
only Seminars 6 to 16 have a starts/sNN/ folder and a zip.

Each seminar NN has a folder starts/sNN/ with
  manifest.json   {"base": "s4" | "none", "git": false, "dirs": [...],
                   "drop": [...]}
  files/          the files of the seminar, laid over the base

  base "s4"   the weather project as Seminar 4 leaves it: the tree of the
              course repository's commit "Write the mean temperature..."
              (data/raw/weather.csv, daily_export.csv, scripts/clean_export.py,
              column_stats.py, rebuild.sh, README.md)
  base "none" nothing: files/ is the whole folder
  dirs        empty folders to create (data/processed, results, ...)
  drop        base paths to leave out
  git         true: the folder is a Git repository with one commit, by
              "Course" on the date of the seminar, so its id is the same on
              every laptop; "date" in the manifest sets that date

The zip holds one folder, weather-sNN/. Dates and modes are fixed, so every
run writes the same bytes, except for git: true, whose .git/index holds the
file times of the run (the commit id is the same every time).

Usage: python3 misc/weather_repo/seminar_zips.py [REPO] [--only 05,07]
  REPO is the repository that build.sh made (default run/weather-project;
  built when missing). Writes misc/weather_repo/release/weather-sNN.zip.
Publish: gh release upload seminar-files release/weather-s*.zip --clobber
  -R MindaugasSarpis/weather-project
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
STARTS = HERE / "starts"
OUT = HERE / "release"
S4_COMMIT = "Write the mean temperature into results and the README"
ZIP_DATE = (2026, 9, 1, 12, 0, 0)


def git(*args, cwd=None, env=None, capture=True):
    return subprocess.run(["git", *args], cwd=cwd, env=env, check=True,
                          capture_output=capture).stdout


def base_s4(repo):
    rev = git("-C", repo, "log", "--format=%H", "--fixed-strings", "--grep", S4_COMMIT,
              "main").decode().split()[0]
    tar = git("-C", repo, "archive", "--format=tar", rev)
    files = {}
    with tarfile.open(fileobj=io.BytesIO(tar)) as t:
        for m in t.getmembers():
            if m.isfile() and m.name != ".gitattributes":
                files[m.name] = (t.extractfile(m).read(), 0o755 if m.mode & 0o111 else 0o644)
    return files


def overlay(start):
    files = {}
    root = start / "files"
    for p in sorted(root.rglob("*")):
        if p.is_file():
            rel = p.relative_to(root).as_posix()
            files[rel] = (p.read_bytes(), 0o755 if os.access(p, os.X_OK) or rel.endswith(".sh") else 0o644)
    return files


def make_git(tree, date):
    """Write tree into a temporary repository with one commit; return its
    files, .git included, as {path: (bytes, mode)}."""
    tmp = Path(tempfile.mkdtemp())
    try:
        for rel, (data, mode) in tree.items():
            p = tmp / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
            p.chmod(mode)
        env = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_NOSYSTEM="1",
                   TZ="Europe/Vilnius", LC_ALL="C",
                   GIT_AUTHOR_NAME="Course", GIT_AUTHOR_EMAIL="course@example.org",
                   GIT_COMMITTER_NAME="Course", GIT_COMMITTER_EMAIL="course@example.org",
                   GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
        git("init", "-q", "-b", "main", cwd=tmp, env=env)
        git("config", "core.autocrlf", "false", cwd=tmp, env=env)
        (tmp / ".gitattributes").write_bytes(b"* -text\n")
        git("add", "-A", cwd=tmp, env=env)
        git("commit", "-q", "-m", "The starting folder of the seminar", cwd=tmp, env=env)
        git("gc", "-q", "--aggressive", "--prune=now", cwd=tmp, env=env)
        for junk in ("hooks", "logs", "COMMIT_EDITMSG", "description", "ORIG_HEAD"):
            j = tmp / ".git" / junk
            if j.is_dir():
                shutil.rmtree(j)
            elif j.exists():
                j.unlink()
        out, dirs = {}, set()
        for p in sorted(tmp.rglob("*")):
            if p.is_file():
                out[p.relative_to(tmp).as_posix()] = (p.read_bytes(), p.stat().st_mode & 0o777)
            elif p.is_dir():
                dirs.add(p.relative_to(tmp).as_posix())  # git needs refs/ even when empty
        return out, dirs
    finally:
        shutil.rmtree(tmp)


def build(nn, repo):
    start = STARTS / f"s{nn}"
    man = json.loads((start / "manifest.json").read_text())
    tree = base_s4(repo) if man.get("base") == "s4" else {}
    for d in man.get("drop", []):
        tree.pop(d, None)
    tree.update(overlay(start))
    dirs = set(man.get("dirs", []))
    if man.get("git"):
        tree, gitdirs = make_git(tree, man.get("date", "2026-09-01T12:00:00+03:00"))
        dirs |= gitdirs
    top = f"weather-s{nn}/"
    for rel in tree:
        parts = rel.split("/")[:-1]
        for i in range(1, len(parts) + 1):
            dirs.add("/".join(parts[:i]))
    OUT.mkdir(exist_ok=True)
    path = OUT / f"weather-s{nn}.zip"
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        def put(name, data=None, mode=0o644):
            info = zipfile.ZipInfo(top + name, ZIP_DATE)
            if data is None:
                info.external_attr = (0o40755 << 16) | 0x10
                z.writestr(info, b"")
            else:
                info.external_attr = mode << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, data)
        put("")
        for d in sorted(dirs):
            put(d.rstrip("/") + "/")
        for rel in sorted(tree):
            put(rel, *tree[rel])
    return path, len(tree)


def main(argv):
    only = None
    if "--only" in argv:
        i = argv.index("--only")
        only = {f"{int(x):02d}" for x in argv[i + 1].split(",")}
        argv = argv[:i] + argv[i + 2:]
    repo = argv[0] if argv else str(HERE / "run/weather-project")
    if not Path(repo, ".git").exists():
        subprocess.run(["bash", str(HERE / "build.sh"), str(Path(repo).parent)], check=True)
    for start in sorted(STARTS.glob("s[0-9][0-9]")):
        nn = start.name[1:]
        if only and nn not in only:
            continue
        path, n = build(nn, repo)
        print(f"{path.name}: {n} files, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main(sys.argv[1:])
