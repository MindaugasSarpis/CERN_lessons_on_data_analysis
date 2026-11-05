# Visualisation before NumPy: weeks 7 and 8 swapped

Date: 5 Nov 2026. Lecturer: "Deploy data visualisation as next lecture";
asked how, chose "swap + rework": Data Visualisation becomes Lecture and
Seminar 7, Python for Data & NumPy becomes Lecture and Seminar 8, and the
visualisation week uses no NumPy.

## The order

| # | Lecture | Block | Seminar page |
|--|--|--|--|
| 07 | Data Visualisation | B | seminar_07 |
| 08 | Python for Data & NumPy | B | seminar_08 |

Block B is renamed "Programming for Data" and holds both weeks, so the
landing page lists the decks in delivery order (it groups by block; block C
starts at 09). Files, slugs (`07-data-visualisation`,
`08-python-for-data-and-numpy`), workbook pages, nav, seminar start folders
(`misc/weather_repo/starts/s07`, `s08`) and the zips follow the numbers.

## What Lecture 7 may assume

Lecture 5 and Seminar 5: values and types, `list`, `tuple`, `dict`, `str`
slicing (`line[0:4]` the year, `line[5:7]` the month), `for`, `if`,
`continue`, `def`/`return`, a module `weather.py` and `import`, one
Matplotlib figure (`fig, ax = plt.subplots()`, `ax.plot` of two lists,
`plt.show()`), conda environments and `environment.yml`. Lecture 6: Git.
Not yet: NumPy, `range`, `zip`, comprehensions, f-strings in the lecture
(Seminar 5 used them), `datetime`.

## The shared code: `weather.py`

Lecture 5's module, and two functions more, used by the lecture and by
Seminar 7 alike:

```python
"""Read the hourly log of the weather station."""
from datetime import datetime

MISSING = -999.0

def read_lines(path):
    return open(path).read().splitlines()[1:]

def temp_of(line):
    return float(line.split(",")[1])

def temps(path):
    result = []
    for line in read_lines(path):
        temp = temp_of(line)
        if temp != MISSING:
            result.append(temp)
    return result

def mean(values):
    return sum(values) / len(values)

def hours(path):
    """The time and the temperature of every measured hour."""
    times = []
    result = []
    for line in read_lines(path):
        temp = temp_of(line)
        if temp != MISSING:
            times.append(datetime.fromisoformat(line[0:16]))
            result.append(temp)
    return times, result

def group(path, start, stop):
    """The temperatures of each line[start:stop]: 0, 4 the year,
    5, 7 the month, 11, 13 the hour of the day, 0, 10 the day."""
    groups = {}
    for line in read_lines(path):
        temp = temp_of(line)
        if temp == MISSING:
            continue
        key = line[start:stop]
        if key not in groups:
            groups[key] = []
        groups[key].append(temp)
    return groups
```

`datetime.fromisoformat` is the one new tool: Matplotlib puts years on an
axis of `datetime` objects. A bin range is given as `bins=50,
range=(-17, 33)`, so no list of edges is needed.

## The numbers (weather.csv, 87 672 rows, 87 552 measured)

- mean 7.16 °C; min −16.3 at 2025-01-07T05:00; max 32.4 at 2018-06-18T15:00
- the 120 missing hours: 2019-07-22T00:00 to 2019-07-26T23:00
- the station records tenths: 477 distinct values
- quartiles −0.2, 6.7, 14.2 °C
- `ax.hist` default: 10 bins of 4.87 °C from −16.3, counts
  337 3173 12733 17255 13892 14619 13466 8797 2948 332
- 1 °C bins, −17 to 33: two peaks, −1 to 0 °C 3848 hours and 11 to 12 °C
  3032, a dip at 7 to 8 °C, 2706: the mean lies between the seasons
- 10 °C bins, −20 to 40: 698 21654 30632 27141 7341 86, one hump
- 0.05 °C bins: every other bin empty (523 of 1000 from −17 to 33)
- monthly means: Jan −3.87 … Jul 18.53; hourly means: 03:00 3.66,
  15:00 10.66
- yearly means 2016–2025: 7.60 6.51 7.97 7.27 6.83 7.25 6.60 8.31 7.27 5.98
  (2019 lacks 120 July hours); hours below 0 °C: 2112 2419 1953 2443 2230
  2110 2314 1845 2249 2677

## Lecture 7 (the deck)

The gallery of chart families and design principles stays. Rebuilt: the
opening (the mean of 87 552 hours and the question how many hours lie near
it), the section *A First Plot* on `weather.py` (every hour as a line, the
time on x, a histogram, its range and bin width), the hands-on section
(hours below 0 °C per year as bars, yearly means against the ten-year mean,
monthly means with an annotation and a title that states the finding), the
live runner blocks without NumPy, the wrap-up and the quizzes. Notes in the
form of convention 13. The figures come from `figures/src/handson.py`.

## Seminar 7

The five figures of the former Seminar 8 (ten years day by day, the year's
cycle, the day's cycle, the yearly means, a histogram) drawn from lists with
`weather.py`; the zip `weather-s07.zip` brings `scripts/weather.py` (Lecture
5's four functions) and an environment with Python only; Part 1 adds
Matplotlib.

## Lecture 8 and Seminar 8

Renumbered only; Matplotlib is now known there. Their rework to the weather
project is still open.
