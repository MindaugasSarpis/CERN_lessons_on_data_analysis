#!/usr/bin/env python3
"""Write the helper files of Seminars 1 and 3 next to this script.

Each file is the state a step of a seminar page ends in, so a student who
lost a step, or missed the session, downloads it and goes on.

  pendulum_replaced.csv    Seminar 1, end of section 7 (Find and Replace)
  pendulum_report.txt      Seminar 1, end of section 9 (saved as report.md)
  project_README_s1.txt    README.md at the end of Seminar 1
  bytes_utf8.txt           Seminar 3, sections 3 to 5: `abcą` + LF, 6 bytes
  bytes_1257.txt           the same text saved as Windows 1257, 5 bytes
  pendulum_crlf.csv        the cleaned table with CRLF line breaks, 107 bytes
  project_README_s3.txt    README.md at the end of Seminar 3
  project_after_s1.zip     the whole project folder after Seminar 1
  project_after_s3.zip     the whole project folder after Seminar 3

The README and the report are `.txt`, because MkDocs turns every `.md` file
in `docs/` into a page. The seminar pages link them with `download="…md"`.
Reads `pendulum_raw.csv`, `pendulum.csv`, `pendulum_plot.png` and
`D0_KPi.csv`. The zips carry a fixed date, so the output is the same on
every run.

Usage:  python project_files.py
"""
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATE = (2026, 9, 29, 12, 0, 0)

README_S1 = """\
# Analysis Project

Seminar exercises for the course
*Best Research and Data Analysis Practices from CERN*.

The example data is from the [CERN Open Data Portal](https://opendata.cern.ch).

## About

- **Author:** your name
- **Started:** 2026-09-29
- **Data I would like to look at:** one sentence

## Folders

| Folder | What goes in |
|--|--|
| `README.md` | what the project is and where the data came from |
| `data/raw` | files exactly as downloaded, never edited |
| `data/processed` | cleaned versions, made later by scripts |
| `scripts` | code |
| `results` | figures and numbers that the code produces |

## Data

- **Source:** CERN Open Data Portal, record 401
- **Address:** https://opendata.cern.ch/record/401
- **DOI:** 10.7483/OPENDATA.LHCb.E7EJ.JUWR
- **Licence:** CC0
- **Fetched:** 2026-09-29
- **File:** `data/raw/D0_KPi.csv`, converted from the record's
  `MasterclassData.root` by the course's `root_to_csv.py`
- **Size:** 3 926 142 bytes, 91 583 rows, 4 columns
- **One row:** one candidate pair of a kaon and a pion from one collision

- **File:** `data/raw/pendulum.csv`, from a lab partner, 2026-09-29
- **Cleaned copy:** `data/processed/pendulum.csv`. Mean line deleted,
  `,` replaced by `.`, `;` replaced by `,`, column `nr` deleted
"""

ANATOMY = """
## File anatomy

`data/raw/D0_KPi.csv`

- **Encoding:** UTF-8, no letters outside ASCII
- **Line ending:** LF
- **Separator:** comma. **Decimal sign:** point
- **Size:** {d0_size} bytes
- **Lines:** 91 584, one header line and 91 583 rows
- **Bytes per row:** about 43 as text, 16 as float32

`data/processed/pendulum.csv`

- **Encoding:** UTF-8, no letters outside ASCII
- **Line ending:** LF
- **Separator:** comma. **Decimal sign:** point
- **Size:** {pendulum_size} bytes
- **Lines:** {pendulum_lines}, one header line and {pendulum_rows} rows
- **Bytes per row:** about {pendulum_per_row} as text, 8 as float32
"""


def spaced(n):
    """3926142 -> '3 926 142', the way the seminar pages write sizes."""
    return f"{n:,}".replace(",", " ")


def report(cleaned):
    """Section 9 of Seminar 1: the cleaned table as a Markdown report."""
    lines = cleaned.splitlines()
    rows = ["| " + line.replace(",", " | ") + " |" for line in lines]
    rows.insert(1, "|--|--|")
    return (
        "# Pendulum\n\nTime of 10 swings for nine lengths.\n\n"
        + "\n".join(rows)
        + "\n\n![Time of 10 swings against length](pendulum_plot.png)\n"
    )


def write_zip(path, files):
    """files: {path inside the project folder: bytes}; None = empty folder."""
    with zipfile.ZipFile(path, "w") as z:
        for name in sorted(files):
            info = zipfile.ZipInfo("analysis-project/" + name, DATE)
            data = files[name]
            if data is None:
                info.external_attr = (0o40755 << 16) | 0x10
                z.writestr(info, b"")
            else:
                info.external_attr = 0o644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, data)


def main():
    raw = (HERE / "pendulum_raw.csv").read_bytes()
    cleaned = (HERE / "pendulum.csv").read_text(encoding="utf-8")
    plot = (HERE / "pendulum_plot.png").read_bytes()
    d0 = (HERE / "D0_KPi.csv").read_bytes()

    # Seminar 1, section 7: mean line deleted, `,` -> `.`, then `;` -> `,`.
    replaced = "".join(
        line.replace(",", ".").replace(";", ",")
        for line in raw.decode("utf-8").splitlines(keepends=True)
        if not line.startswith(";mean")
    )
    assert "\n".join(l.split(",", 1)[1] for l in replaced.splitlines()) \
        == cleaned.rstrip("\n"), "pendulum_raw.csv and pendulum.csv disagree"

    rep = report(cleaned)
    n_lines = cleaned.count("\n")
    readme_s3 = README_S1 + ANATOMY.format(
        d0_size=spaced(len(d0)),
        pendulum_size=len(cleaned.encode()),
        pendulum_lines=n_lines,
        pendulum_rows=n_lines - 1,
        pendulum_per_row=round(len(cleaned.encode()) / n_lines),
    )

    out = {
        "pendulum_replaced.csv": replaced.encode(),
        "pendulum_report.txt": rep.encode(),
        "project_README_s1.txt": README_S1.encode(),
        "bytes_utf8.txt": "abcą\n".encode("utf-8"),
        "bytes_1257.txt": "abcą\n".encode("cp1257"),
        "pendulum_crlf.csv": cleaned.replace("\n", "\r\n").encode(),
        "project_README_s3.txt": readme_s3.encode(),
    }
    for name, data in out.items():
        (HERE / name).write_bytes(data)

    project = {
        "data/": None,
        "data/raw/": None,
        "data/processed/": None,
        "results/": None,
        "scripts/": None,
        "data/raw/D0_KPi.csv": d0,
        "data/raw/pendulum.csv": raw,
        "data/processed/pendulum.csv": cleaned.encode(),
        "results/report.md": rep.encode(),
        "results/pendulum_plot.png": plot,
    }
    write_zip(HERE / "project_after_s1.zip",
              {**project, "README.md": README_S1.encode()})
    write_zip(HERE / "project_after_s3.zip",
              {**project, "README.md": readme_s3.encode()})

    for name in [*out, "project_after_s1.zip", "project_after_s3.zip"]:
        print(f"{name:24} {(HERE / name).stat().st_size:>9} bytes")


if __name__ == "__main__":
    main()
