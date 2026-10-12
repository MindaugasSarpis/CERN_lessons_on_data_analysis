# Bike Counters

Practice project of Seminar 4: bicycle counts, read and checked with typed
commands.

## Folders

- `data/raw`: files as they arrived, never edited
- `data/processed`: files that commands make from `data/raw`
- `scripts`: programs
- `results`: numbers and figures

## Two places

| Place | Bicycles |
|--|--|
| Antakalnis | 412 |
| Užupis | 388 |

Course pages: [the workbook](https://mindaugassarpis.github.io/CERN_lessons_on_data_analysis/workbook/)

## Data

- `data/raw/counts.csv`: the two places above, typed by hand.
- `data/raw/bikes.csv`: two bicycle counters, one row per counter and hour
  of 2024 and 2025, 35 088 rows, SHA-256 `2c68aad2…e3808991`. Generated for the
  course; the city and its counters are made up.

## Columns of `bikes.csv`

| Column | Meaning | Unit |
|--|--|--|
| `time` | start of the hour | YYYY-MM-DDTHH:MM |
| `counter` | `bridge` or `park` | none |
| `bikes` | bicycles that passed in that hour | bicycles |

Missing value: `bikes` is `9999` in 168 rows, the park counter from
2025-03-10 to 2025-03-16, while it was broken.

## How to rebuild

Run in the project folder: zsh on macOS, PowerShell 7 on Windows.

- `data/processed/bikes_valid.csv`: `bikes.csv` without the rows marked
  `9999`, 34 921 lines.
  - zsh: `grep -v ',9999$' data/raw/bikes.csv > data/processed/bikes_valid.csv`
  - PowerShell: `Select-String ',9999$' data/raw/bikes.csv -NotMatch -Raw > data/processed/bikes_valid.csv`
