#!/usr/bin/env python3
"""Write the hill station's file of Seminar 12 into the course repository.

The weather project's station stands in a valley. A second station stands on
a hill 4 km away and 180 m higher. Its logger exported 2025 the way its
software does, and Seminar 12 cleans that export with pandas and compares it
with the valley station day by day.

  ../../../../misc/weather_repo/files/s12/data/raw/hill_station.csv

The hill's temperature is the valley's (`weather.csv`, next to this script)
minus 0.8 °C in January to 1.6 °C in July, plus slow noise. The export then
has the faults the seminar finds, each placed at fixed hours:

  - `;` between the values, a decimal comma, times as `DD.MM.YYYY HH:MM`
  - local clock time, Europe/Vilnius: 30 March has no 03:00, 26 October has
    03:00 twice (the valley's `weather.csv` keeps winter time all year)
  - 44 hours missing, 11 Feb 14:00 to 13 Feb 09:00 (the logger was off)
  - temp = -999 for 18 hours, 14 Apr 06:00 to 23:00 (the reading failed)
  - temp empty in 9 single hours, humidity empty for 30 hours in September
  - 72 hours in °F, 8 Jul 10:00 to 11 Jul 09:00, marked `F` in `unit`
  - the 24 rows of 20 November exported twice, one copy after the other

The random numbers are seeded, so the file is the same on every run.

Usage:  python3 weather_s12_files.py
"""
import math
import random
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[3] / "misc" / "weather_repo" / "files" / "s12" / "data" / "raw"
YEAR = 2025
# Summer time in Vilnius, as hours of winter time (UTC+2), the valley's clock:
# from 30 March 03:00 to 26 October 03:00 the local clock is one hour ahead.
DST = (datetime(2025, 3, 30, 3), datetime(2025, 10, 26, 3))
GAP = (datetime(2025, 2, 11, 14), datetime(2025, 2, 13, 10))
FAILED = (datetime(2025, 4, 14, 6), datetime(2025, 4, 15, 0))
FAHRENHEIT = (datetime(2025, 7, 8, 10), datetime(2025, 7, 11, 10))
NO_HUMIDITY = (datetime(2025, 9, 2, 12), datetime(2025, 9, 3, 18))
TWICE = datetime(2025, 11, 20)


def comma(value):
    text = f"{value:.1f}"
    if text == "-0.0":
        text = "0.0"
    return text.replace(".", ",")


def valley_2025():
    """{time: (temp_c, humidity_pct)} of the valley station, 2025."""
    rows = {}
    with open(HERE / "weather.csv", encoding="utf-8") as handle:
        next(handle)
        for line in handle:
            if line.startswith(f"{YEAR}-"):
                time, temp, rh, _ = line.rstrip("\n").split(",")
                rows[datetime.fromisoformat(time)] = (float(temp), int(rh))
    return rows


def main():
    rng = random.Random(1225)
    valley = valley_2025()
    rows = []
    noise = 0.0
    for winter_time, (temp, rh) in valley.items():
        local = winter_time + timedelta(hours=1) if DST[0] <= winter_time < DST[1] else winter_time
        angle = 2 * math.pi * (winter_time.timetuple().tm_yday - 18) / 365.25
        noise = 0.9 * noise + rng.gauss(0, 0.15)
        hill = temp - 1.2 + 0.4 * math.cos(angle) + noise
        humidity = min(100, rh + 5 + round(rng.gauss(0, 2)))
        rows.append([local, round(hill, 1), "C", str(humidity)])

    out = []
    special = (GAP, FAILED, FAHRENHEIT)
    plain = [i for i, row in enumerate(rows)
             if not any(a <= row[0] < b for a, b in special) and row[0].date() != TWICE.date()]
    empty_temp = set(rng.sample(plain, 9))
    for i, (local, hill, unit, humidity) in enumerate(rows):
        if GAP[0] <= local < GAP[1]:
            continue
        temp = comma(hill)
        if FAILED[0] <= local < FAILED[1]:
            temp = "-999"
        elif FAHRENHEIT[0] <= local < FAHRENHEIT[1]:
            temp, unit = comma(hill * 9 / 5 + 32), "F"
        elif i in empty_temp:
            temp = ""
        if NO_HUMIDITY[0] <= local < NO_HUMIDITY[1]:
            humidity = ""
        out.append((local, f"{local:%d.%m.%Y %H:%M};{temp};{unit};{humidity}"))

    lines = ["time;temp;unit;humidity"]
    day = [line for local, line in out if local.date() == TWICE.date()]
    for local, line in out:
        lines.append(line)
        if local == TWICE + timedelta(hours=23):
            lines.extend(day)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "hill_station.csv").write_bytes(("\n".join(lines) + "\n").encode())
    print(f"{len(lines) - 1} rows written to {OUT / 'hill_station.csv'}")


if __name__ == "__main__":
    main()
