#!/usr/bin/env bash
set -e
mkdir -p data/processed results
grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
python scripts/clean_hill.py > results/hill.txt
