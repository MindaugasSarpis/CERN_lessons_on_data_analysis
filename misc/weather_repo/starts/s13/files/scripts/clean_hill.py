"""Clean the hill station's export; compare it with the valley, day by day.

Run from the project folder:  python scripts/clean_hill.py
"""
import os

import pandas as pd

HILL = "data/raw/hill_station.csv"
VALLEY = "data/raw/weather.csv"
OUT = "data/processed/hill_daily.csv"

df = pd.read_csv(HILL, sep=";", decimal=",", na_values=["-999"])
print("rows read      ", len(df))
print("temp missing   ", df["temp"].isna().sum())

f = df["unit"] == "F"
df.loc[f, "temp"] = ((df.loc[f, "temp"] - 32) * 5 / 9).round(1)
df.loc[f, "unit"] = "C"
print("rows in F      ", f.sum())

print("duplicate rows ", df.duplicated().sum())
df = df.drop_duplicates()

df["time"] = pd.to_datetime(df["time"], format="%d.%m.%Y %H:%M")
temp = df.set_index("time")["temp"]
day = temp.resample("D").agg(hill="mean", hours="count")
print("days < 20 hours", (day["hours"] < 20).sum())
day = day[day["hours"] >= 20]
os.makedirs("data/processed", exist_ok=True)
day["hill"].round(2).to_csv(OUT, date_format="%Y-%m-%d", lineterminator="\n")

v = pd.read_csv(VALLEY, na_values=["-999"], parse_dates=["time"])
valley = v.set_index("time")["temp_c"].resample("D").mean()
both = pd.merge(valley, day, on="time")
diff = both["hill"] - both["temp_c"]
print("days compared  ", len(both))
print("hill - valley  ", round(diff.mean(), 2))
