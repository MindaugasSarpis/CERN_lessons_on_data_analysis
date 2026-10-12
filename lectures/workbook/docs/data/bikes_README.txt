# Bike Counters

Two bicycle counters of a city, one on a bridge and one on a park path:
how many bicycles passed in each hour of 2024 and 2025.

## Data

- `data/raw/bikes.csv`: one row per counter and hour, 35 088 rows.
  Generated for the course; the city and its counters are made up.
- `data/raw/monthly_export.csv`: the mean number of bicycles per day on the
  bridge, for each month of 2025, exported from a spreadsheet.

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

1. `data/processed/monthly.csv`, 189 bytes, SHA-256 `ea4ce2ce…19396ef6`:
   - zsh: `python3 scripts/clean_export.py data/raw/monthly_export.csv data/processed/monthly.csv`
   - PowerShell: `python scripts/clean_export.py data/raw/monthly_export.csv data/processed/monthly.csv`
2. `data/processed/bikes_valid.csv`, `bikes.csv` without the 168 rows marked `9999`:
   - zsh: `grep -v ',9999$' data/raw/bikes.csv > data/processed/bikes_valid.csv`
   - PowerShell: `Select-String ',9999$' data/raw/bikes.csv -NotMatch -Raw > data/processed/bikes_valid.csv`
