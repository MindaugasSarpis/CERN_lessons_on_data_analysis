# Bike Counters

Two bicycle counters, one on a bridge and one on a park path, counted
every hour of 2024 and 2025. How many bicycles pass in an hour?

## Folders

- `data/raw`: files as they arrived, never edited
- `data/processed`: files that commands make from `data/raw`
- `scripts`: programs
- `results`: numbers that the programs write

## Data

`data/raw/bikes.csv`: two bicycle counters, one row per counter and
hour of 2024 and 2025, 35 088 rows, SHA-256 `2c68aad2…e3808991`.
From [Seminar 4](https://mindaugassarpis.github.io/CERN_lessons_on_data_analysis/workbook/seminars/seminar_04/)
of the course workbook.

| Column | Meaning | Unit |
|--|--|--|
| `time` | start of the hour | YYYY-MM-DDTHH:MM |
| `counter` | `bridge` or `park` | none |
| `bikes` | bicycles that passed in that hour | bicycles |

Missing value: `bikes` is `9999` in 168 rows, the park counter from
2025-03-10 to 2025-03-16, while it was broken.

## How to rebuild

In the project folder: `./scripts/rebuild.sh` in zsh on macOS,
`./scripts/rebuild.ps1` in PowerShell 7 on Windows. They make:

- `data/processed/bikes_valid.csv`: `bikes.csv` without the rows
  marked `9999`, 34 921 lines
- `results/bikes_stats.txt`: rows, smallest, largest and mean of
  `bikes` in it
