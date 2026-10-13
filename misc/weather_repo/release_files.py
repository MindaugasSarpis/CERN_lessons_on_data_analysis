#!/usr/bin/env python3
"""The files of Seminar 5 for the release `seminar-files` of weather-project.

Seminar 5 (Python) comes before Git, so its files are downloads:

  weather-project-s4.zip  the folder `weather-project` as Seminar 4 leaves it:
                          the tree of the course repository's fifth commit
                          (the mean 7.16 in the README, rebuild.sh), plus
                          scripts/coldest_hour.py, for a student without the
                          folder of Seminar 4
  coldest_hour.py         the script with two bugs that Seminar 5 repairs

Usage: python3 misc/weather_repo/release_files.py REPO
  REPO is the repository that build.sh made (run/weather-project). The files
  are written to misc/weather_repo/release/ next to those of
  lectures/workbook/docs/data/weather_seminar_files.py. Fixed dates and
  modes: every run writes the same bytes.
"""
import io
import subprocess
import sys
import tarfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "release"
COMMIT_MESSAGE = "Write the mean temperature into results and the README"
DATE = (2026, 10, 16, 16, 10, 0)


def main(repo):
    rev = subprocess.run(
        ["git", "-C", repo, "log", "--format=%H", "--fixed-strings", "--grep", COMMIT_MESSAGE],
        capture_output=True, text=True, check=True).stdout.split()[0]
    tar = subprocess.run(["git", "-C", repo, "archive", "--format=tar", rev],
                         capture_output=True, check=True).stdout
    OUT.mkdir(exist_ok=True)
    bug = (HERE / "files/s05/scripts/coldest_hour.py").read_bytes()
    with tarfile.open(fileobj=io.BytesIO(tar)) as t, \
            zipfile.ZipFile(OUT / "weather-project-s4.zip", "w", zipfile.ZIP_DEFLATED) as z:
        def put(name, data=None, mode=0o644):
            info = zipfile.ZipInfo("weather-project/" + name, DATE)
            if data is None:
                info.external_attr = 0o40755 << 16
                z.writestr(info, b"")
            else:
                info.external_attr = mode << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, data)
        put("")
        for folder in ("data/", "data/raw/", "data/processed/", "scripts/", "results/"):
            put(folder)
        for m in sorted(t.getmembers(), key=lambda m: m.name):
            if m.isfile() and m.name != ".gitattributes":
                put(m.name, t.extractfile(m).read(), 0o755 if m.mode & 0o111 else 0o644)
        put("scripts/coldest_hour.py", bug)
    (OUT / "coldest_hour.py").write_bytes(bug)
    print(rev[:7], "->", OUT / "weather-project-s4.zip", "and coldest_hour.py")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else str(HERE / "run/weather-project"))
