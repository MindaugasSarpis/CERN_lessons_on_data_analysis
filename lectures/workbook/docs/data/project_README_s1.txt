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
