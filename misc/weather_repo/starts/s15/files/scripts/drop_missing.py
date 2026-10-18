"""Write weather.csv without the rows whose temp_c is -999.

Run from the project folder:  python scripts/drop_missing.py
"""
import os

RAW = "data/raw/weather.csv"
OUT = "data/processed/weather_valid.csv"

with open(RAW, encoding="utf-8") as source:
    lines = [line for line in source if ",-999," not in line]
os.makedirs("data/processed", exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="\n") as target:
    target.writelines(lines)
print(len(lines) - 1, "rows written to", OUT)
