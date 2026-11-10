# Seminar 5 · Python

**Paired lecture:** 05 Python Foundations · **Format:** a showcase, then a problem, in class

<!-- ~135 min: the length pnpm timing:check reads (week 5: 105 min of lecture, 135 of seminar) -->

**Today's question:** Is the coast milder than Vilnius in winter, and cooler in summer?

Part 1 is the room's first Python, step by step; the lecturer runs Part 2
from this page; in Part 3 the room works in pairs. Everything is typed in
VS Code: the scripts in the editor, the commands in its terminal (zsh on
macOS, Git Bash on Windows; the same lines in both). A line that starts
with `$` is typed in the terminal without the `$`, a line that starts with
`>>>` or `...` is typed at Python's prompt, and every other line is what
comes back.

**If time runs short:** leave out section 5 (the week by day); its calls are on the library card.

??? info "Before the session"
    - **Room:** VS Code and Miniforge on every laptop (Seminar 4, or the
      [Setup](../setup.md) page); a laptop without Miniforge installs it in
      section 1 while the others go on. Internet: Python for the environment,
      about 25 MB on a Mac and 37 MB on Windows; the weather service; two
      station files of 6.1 and 4.4 MB.
    - **No file is handed out.** In Part 1 the room types six hours of a
      weather station's log from this page. The scripts of Part 2 ask Open-Meteo's
      forecast service (CC BY 4.0, "Weather data by Open-Meteo.com"), and
      read the daily record of the Vilnius station; Part 3 adds the
      Klaipėda station. Both station files are from GHCN-Daily, NOAA NCEI,
      "for free and unrestricted use in research, education, and other
      non-commercial activities" (WMO Resolution 40); cite Menne et al.
      2012, *Global Historical Climatology Network - Daily (GHCN-Daily)*,
      Version 3.35, NOAA NCDC,
      [doi:10.7289/V5D21VHZ](https://doi.org/10.7289/V5D21VHZ), accessed
      10 November 2026.
    - **Open-Meteo's free service** allows one internet address 10 000
      calls a day; a room shares one address. The scripts of this page ask
      for at most seven days and make one, one and three calls a run.
    - **The numbers:** the forecasts on this page were printed on
      10 November 2026 and change by the hour; the station numbers of
      1991–2020 do not change.
    - **You:** remove the Python extension from your VS Code beforehand,
      to install it with the room in section 3. Paths are shown for a Mac
      (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`. Keys are
      written for Windows, macOS in brackets.

---

## Part 1 · Set up { #part-1 }

<!-- Part 1: 0:00 to 0:30, longer than the 15 min of later seminars: the room's first conda environment and first Python -->

### 1. A folder and the environment `s05` { #start }

<!-- 0:00 · 10 min -->

conda installs Python and packages into **environments**: a folder with one Python and the packages one project needs. Today's, `s05`, holds Python alone.

1. In VS Code, **View** > **Terminal**. Make the folder and go into it.

    ```text
    $ mkdir ~/weather-s05
    $ cd ~/weather-s05
    $ pwd
    /Users/smilte/weather-s05
    ```

2. **File** > **Open Folder...** > `weather-s05` (in your home folder) >
   **Open**, then **View** > **Terminal**. The Explorer on the left is empty.

3. Make the environment, with Python 3.14 from conda-forge. At
   `Proceed ([y]/n)?` press `Enter`.

    ```text
    $ conda create -n s05 python=3.14
    ...
      added / updated specs:
        - python=3.14
    ...
    Proceed ([y]/n)?
    ...
    #     $ conda activate s05
    ```

    `conda: command not found`: install Miniforge as in
    [Seminar 4, sections 1 and 2](seminar_04.md#installs) or on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

4. Switch it on, and ask which Python answers. Each new terminal starts in
   `(base)`: type the first line in each.

    ```text
    $ conda activate s05
    $ python --version
    Python 3.14.10
    ```

5. Write the environment into a file, then click `environment.yml` in the
   Explorer, delete its last line, `prefix: ...` (a folder on this
   laptop), and save (`Ctrl+S`, macOS `Cmd+S`).

    ```text
    $ conda env export --from-history -f environment.yml
    ```

    ```text
    name: s05
    channels:
      - conda-forge
    dependencies:
      - python=3.14
    ```

**Check:** `(s05)` at the start of the prompt, a Python `3.14` (the last number may be higher), and `environment.yml` in the Explorer.

---

### 2. Python at the prompt: numbers, a list, text { #prompt }

<!-- 0:10 · 10 min -->

At the `>>>` prompt Python runs one line and prints its value: the place to try a line.

1. Start the interpreter. The first line names the version; `>>>` waits
   for a line.

    ```text
    $ python
    Python 3.14.10 | packaged by conda-forge | ...
    >>>
    ```

2. Arithmetic. 23.6 °C in Fahrenheit; `//` and `%` give the whole part and
   the remainder; a float is stored in binary, so some decimals come out
   slightly off.

    ```pycon
    >>> 23.6 * 9 / 5 + 32
    74.48
    >>> 25 // 24, 25 % 24
    (1, 1)
    >>> 0.1 + 0.2
    0.30000000000000004
    ```

3. A **list**: six hours of a weather station's log, 21 July 2019, 20:00
   to 01:00. The temperature sensor failed at midnight, and the station
   wrote `-999` for "no reading".

    ```pycon
    >>> temps = [27.3, 25.6, 24.6, 23.6, -999, -999]
    >>> len(temps), temps[0], temps[-1]
    (6, 27.3, -999)
    >>> sum(temps) / len(temps)
    -316.15000000000003
    ```

    Python adds the two marks as temperatures and gives no warning.

4. A line of a file arrives as text, a **str**. `split(",")` cuts it into
   a list of strings; `float` makes a number of one of them.

    ```pycon
    >>> line = "2019-07-21T20:00,27.3,63,4.5"
    >>> parts = line.split(",")
    >>> parts
    ['2019-07-21T20:00', '27.3', '63', '4.5']
    >>> parts[1] + "1"
    '27.31'
    >>> float(parts[1]) + 1
    28.3
    >>> type(parts[1]), type(float(parts[1]))
    (<class 'str'>, <class 'float'>)
    >>> exit()
    ```

**Check:** `-316.15000000000003` for the six hours, and `'27.31'` next to `28.3`.

---

### 3. A first script: the list and a loop { #script }

<!-- 0:20 · 10 min -->

A script is lines in a file; `python mean.py` runs them from the first to the last, the same way every time.

1. **Extensions** (`Ctrl+Shift+X`, macOS `Cmd+Shift+X`), type `python`,
   click **Python** by Microsoft, **Install**.
2. `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), `Python: Select Interpreter`,
   pick the entry with `envs/s05` in its path. The Status Bar shows `s05`.
3. In the Explorer, right-click > **New File...**, type `mean.py`,
   `Enter`. Type the lines and save. `for` runs the indented lines once
   for each value of the list; `continue` skips to the next value.

    ```python title="mean.py"
    temps = [27.3, 25.6, 24.6, 23.6, -999, -999]   # 21 July 2019, 20:00 to 01:00

    total = 0.0
    count = 0
    for temp in temps:
        if temp == -999:          # the station's mark: no reading in this hour
            continue
        total = total + temp
        count = count + 1

    print(f"{count} hours, mean {total / count:.1f} °C")
    ```

4. Run it with the ▶ at the top right of the editor, then by hand in the
   terminal. `f"..."` puts the value of each `{...}` into the text; `:.1f`
   gives one decimal.

    ```text
    $ python mean.py
    4 hours, mean 25.3 °C
    ```

5. Select the two lines of the `if`, `Ctrl+/` (macOS `Cmd+/`) to make them
   comments, save, run. Then `Ctrl+/` again, save.

    ```text
    $ python mean.py
    6 hours, mean -316.2 °C
    ```

**Check:** `4 hours, mean 25.3 °C`, from the ▶ and from the typed line.

!!! warning "`IndentationError`, or `can't open file 'mean.py'`"
    The lines under `for` and `if` need the same indentation: VS Code adds
    four spaces after `:` and `Enter`. A file that is not found: the
    terminal is not in the folder; `cd ~/weather-s05`.

---

## Part 2 · Showcase { #part-2 }

The lecturer runs four complete scripts on real data; the room watches or
types along. For each: in the Explorer, right-click > **New File...**, the
name above the code, paste, save, and run it in the terminal.

### 4. The weather in Vilnius now: a dict inside a dict { #now }

<!-- 0:30 · 8 min -->

A web service answers in JSON, text that `json.load` turns into Python's own objects: dicts, lists, numbers and strings.

```python title="now.py"
import json
import urllib.request

URL = ("https://api.open-meteo.com/v1/forecast?latitude=54.69"
       "&longitude=25.28&current=temperature_2m,wind_speed_10m")
with urllib.request.urlopen(URL) as response:
    answer = json.load(response)        # JSON text -> Python objects

print(type(answer), len(answer), "keys")
print(list(answer))
print(answer["current"])
print(answer["current_units"])
print(f"Vilnius now: {answer['current']['temperature_2m']} °C")
```

```text
$ python now.py
<class 'dict'> 9 keys
['latitude', 'longitude', 'generationtime_ms', 'utc_offset_seconds', 'timezone', 'timezone_abbreviation', 'elevation', 'current_units', 'current']
{'time': '2026-11-10T19:15', 'interval': 900, 'temperature_2m': 3.7, 'wind_speed_10m': 8.6}
{'time': 'iso8601', 'interval': 'seconds', 'temperature_2m': '°C', 'wind_speed_10m': 'km/h'}
Vilnius now: 3.7 °C
```

Your time and numbers differ: they are today's, and the time is in UTC.

**Notice:** two keys in a row reach the temperature, `answer["current"]["temperature_2m"]`; the units are in a dict of their own, `answer["current_units"]`.

**Ask the room:** the wind is 8.6. A calm evening or a strong wind?

??? note "Answer"
    It depends on the unit, and the answer names it: km/h. 8.6 km/h is
    8.6 / 3.6 = 2.4 m/s, a light breeze. The station's log of Part 1 gives
    the wind in m/s: read as m/s, 8.6 would be a fresh breeze. A number
    from a service is read with its unit.

!!! warning "An error instead of an answer"
    - `URLError` or `getaddrinfo failed`: no internet; check the Wi-Fi.
    - `HTTP Error 429`: the service counted too many calls from the room's
      address today. Go on with section 6, which asks another server.

---

### 5. The next seven days: a loop, and a dict of days { #week }

<!-- 0:38 · 10 min -->

A dict collects the values of each group: here the key is the date, the value a list of that day's hours.

```python title="week.py"
import json
import urllib.request

URL = ("https://api.open-meteo.com/v1/forecast?latitude=54.69"
       "&longitude=25.28&hourly=temperature_2m&forecast_days=7"
       "&timezone=Europe%2FVilnius")
with urllib.request.urlopen(URL) as response:
    answer = json.load(response)
times = answer["hourly"]["time"]             # a list: '2026-11-10T00:00', ...
temps = answer["hourly"]["temperature_2m"]   # a list: one float per hour
print(len(times), "hours,", times[0], "to", times[-1])

days = {}                                    # a date -> its temperatures
for time, temp in zip(times, temps):
    date = time[:10]
    if date not in days:
        days[date] = []
    days[date].append(temp)

for date, values in days.items():
    mean = sum(values) / len(values)
    print(f"{date}: {min(values):5.1f} to {max(values):5.1f} °C, "
          f"mean {mean:5.1f}")
```

```text
$ python week.py
168 hours, 2026-11-10T00:00 to 2026-11-16T23:00
2026-11-10:   1.6 to   4.9 °C, mean   3.4
2026-11-11:   2.1 to   3.8 °C, mean   3.1
2026-11-12:   1.1 to   4.3 °C, mean   2.5
2026-11-13:   2.6 to   4.6 °C, mean   3.8
2026-11-14:   0.7 to   4.0 °C, mean   2.8
2026-11-15:  -0.5 to   5.1 °C, mean   1.8
2026-11-16:  -1.8 to   3.0 °C, mean   0.8
```

Your dates and numbers differ. `&timezone=Europe%2FVilnius` gives the
times of Vilnius, so that a day runs from midnight to midnight there.

**Notice:** 168 hours went in, 7 keys came out: `time[:10]`, the first ten characters of the time, decides the groups.

**Ask the room:** which hour of the day is the coldest, on average over the seven days? What one change in the loop finds it?

??? note "Answer"
    The key: `date = time[11:]` instead of `time[:10]` makes 24 groups,
    one per hour of the day, of seven values each. On 10 November 2026 the
    run printed the coldest hour at 08:00, mean 1.6 °C, and the warmest at
    14:00, 4.1 °C: the ground cools all night until the sun is up, at
    about 07:45 in mid-November.

---

### 6. 145 years of Vilnius in a CSV file: `csv`, and a day without a value { #csv }

<!-- 0:48 · 10 min -->

`split(",")` cuts a value that holds a comma; the `csv` module reads the quotes around it. An empty field is no number.

```python title="vilnius.py"
import csv
import urllib.request

URL = ("https://www.ncei.noaa.gov/data/"
       "global-historical-climatology-network-daily/access/LH000026730.csv")
urllib.request.urlretrieve(URL, "vilnius.csv")   # 6.1 MB, into the folder

line = open("vilnius.csv").read().splitlines()[1]
print(line)
print(line.split(",")[5:8])                      # split cuts the name in two
rows = list(csv.DictReader(open("vilnius.csv")))  # each row a dict
print(len(rows), "days at", rows[0]["NAME"], "from", rows[0]["DATE"])

missing = 0
coldest = 100.0
coldest_date = ""
for row in rows:
    if row["TAVG"] == "":                        # no daily mean that day
        missing = missing + 1
        continue
    temp = float(row["TAVG"]) / 10               # tenths of °C
    if temp < coldest:
        coldest = temp
        coldest_date = row["DATE"]
print(missing, "days without TAVG")
print(f"coldest day: {coldest_date}, {coldest} °C")
```

```text
$ python vilnius.py
"LH000026730","1881-01-01","54.6331","25.1","156.0","VILNIUS, LH","    0",",,r",,,,,,,"   12",",,r"
['"VILNIUS', ' LH"', '"    0"']
51041 days at VILNIUS, LH from 1881-01-01
227 days without TAVG
coldest day: 1940-01-16, -33.5 °C
```

The station: Vilnius, 156 m above the sea. `TAVG` is the mean temperature
of the day in tenths of °C: `"   12"` is 1.2 °C.

**Notice:** `split` makes two pieces of `"VILNIUS, LH"`; `csv.DictReader` keeps the name whole and gives every row as a dict, `row["TAVG"]`.

**Ask the room:** delete the three lines of the `if row["TAVG"] == ""`. What happens?

??? note "Answer"
    The loop stops at the first day without a mean, 19 April 1919:
    `ValueError: could not convert string to float: ''`. An empty field
    is a mark that Python refuses; the `-999` of section 2 was a mark it
    added without a word.

---

### 7. One function, three capitals: write a step once { #function }

<!-- 0:58 · 8 min -->

A function gives a step a name and parameters; called with other values, it does the same step for them.

```python title="capitals.py"
import json
import urllib.request


def week(latitude, longitude):
    """The hourly temperatures of the next 7 days at one place."""
    url = ("https://api.open-meteo.com/v1/forecast"
           f"?latitude={latitude}&longitude={longitude}"
           "&hourly=temperature_2m&forecast_days=7")
    with urllib.request.urlopen(url) as response:
        return json.load(response)["hourly"]["temperature_2m"]


def mean(values):
    """The mean of a list of numbers."""
    return sum(values) / len(values)


for name, lat, lon in [("Vilnius", 54.69, 25.28), ("Riga", 56.95, 24.11),
                       ("Tallinn", 59.44, 24.75)]:
    temps = week(lat, lon)
    print(f"{name:8} {lat}° N: mean {mean(temps):4.1f} °C, "
          f"coldest hour {min(temps):5.1f} °C")
```

```text
$ python capitals.py
Vilnius  54.69° N: mean  2.6 °C, coldest hour  -1.8 °C
Riga     56.95° N: mean  3.3 °C, coldest hour  -0.9 °C
Tallinn  59.44° N: mean  4.3 °C, coldest hour   0.3 °C
```

Your numbers differ: they are this week's.

**Notice:** the request is written once, in `week`; the loop calls it three times, with three pairs of coordinates.

**Ask the room:** Tallinn lies 530 km north of Vilnius. Why can its week be the warmer one?

??? note "Answer"
    Tallinn and Riga lie on the Baltic Sea; Vilnius lies about 290 km from
    it.
    In autumn and winter the sea is warmer than the land and warms the air
    over the coast. One week is weather, not climate: Part 3 asks the
    question of thirty years.

---

### 8. Library card: the calls of this page { #card }

<!-- 1:06 · 3 min -->

Every call of the examples and of the solution below, one line each.

| Call | What it does |
|--|--|
| `import json`, `import csv`, `import urllib.request` | modules of the standard library, in every Python |
| `with urllib.request.urlopen(url) as response:` | opens a web address; `with` closes it after the block |
| `json.load(response)` | JSON text into dicts, lists, numbers and strings |
| `urllib.request.urlretrieve(url, "file.csv")` | saves what an address answers into a file |
| `open("file.csv").read().splitlines()` | the lines of a file, a list of strings |
| `line.split(",")` | a string cut at each comma, also inside quotes |
| `csv.DictReader(open("file.csv"))` | the rows of a CSV file, each a dict keyed by the header; quotes kept whole |
| `answer["current"]["temperature_2m"]` | a value of a dict inside a dict |
| `for time, temp in zip(times, temps):` | two lists walked side by side |
| `if date not in days: days[date] = []` | a new key, with an empty list |
| `days[date].append(temp)`, `days.items()` | a value added to a list; the keys and values of a dict |
| `float("   12")`, `float("")` | a number from a text; `ValueError` for an empty text |
| `continue` | on to the next turn of the loop |
| `def week(latitude, longitude):` … `return` | a function: a step written once, with parameters |
| `f"{mean:5.1f}"` | a number in a text: five characters wide, one decimal |
| `min(values)`, `max(values)`, `sum(values) / len(values)` | the smallest, the largest, the mean |
| `curl -O URL` (in the terminal) | saves what an address answers, under the file's own name |

---

## Part 3 · The problem { #part-3 }

### 9. Is the coast milder in winter, and cooler in summer? { #problem }

<!-- 1:09 · 50 min -->

Klaipėda lies on the Baltic coast, Vilnius about 290 km inland. GHCN-Daily has
the daily record of both stations, in the form of section 6: one line per
day, the daily mean `TAVG` in tenths of °C. Download each file once into
the folder (6.1 and 4.4 MB) and read it from there. `curl -O` saves what an
address answers under the file's own name; your speeds and times differ.

```text
$ curl -O https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026730.csv
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 5976k  100 5976k    0     0  3546k      0  0:00:01  0:00:01 --:--:-- 3546k
$ curl -O https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026509.csv
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 4324k  100 4324k    0     0  2862k      0  0:00:01  0:00:01 --:--:-- 2863k
```

`LH000026730` is Vilnius, `LH000026509` Klaipėda. Source: NOAA NCEI,
GHCN-Daily (terms and citation under "Before the session"). Weather services
describe a climate by thirty years: use 1991–2020.

Work in pairs, with any tools, an LLM too: the work is the idea and the checks, not the typing. The answer comes from plain Python and its standard library.

1. **Predict**, before any code. In January, which station is warmer, and
   by about how much? In July? One reason. Write it down.
2. **Solve.** The mean `TAVG` of January and of July, 1991–2020, at each
   station.
3. **Check the machine's work.**
    - By hand: the `TAVG` of Klaipėda on 1 to 5 January 1991 (find the
      five lines in the file, `Ctrl+F` in VS Code). Work out their mean,
      and make your code print the mean of the same five days.
    - The sample size: on how many days does each of your four means rest?
      January and July have 31 × 30 = 930 days in 1991–2020.
    - The unit and the place: tenths of °C; the column `ELEVATION` gives
      each station's height in metres.
    - Set the answer against your prediction; where they differ, say which
      was wrong, and why.
4. **Hand in.** The four means, the two differences (Klaipėda minus
   Vilnius), the days each mean rests on, and two sentences in your own
   words, ready to show.

??? tip "Hint 1: one row at a time"
    `csv.DictReader` gives each day as a dict: `row["DATE"]` is
    `'1991-01-01'`, so `row["DATE"][:4]` is the year and `row["DATE"][5:7]`
    the month; `row["TAVG"]` is `'   24'` (2.4 °C) or `''` on a day without
    a mean.

??? tip "Hint 2: one function, four calls"
    Write the reading once: a function `temps(path, month)` that gives the
    list of `TAVG` values of that month in 1991–2020. Then four calls: two
    files, `"01"` and `"07"`. `len` of each list is its number of days.

??? tip "Hint 3: the five days by hand"
    The first five values of Klaipėda's January list are 1 to 5 January
    1991: print `values[:5]` and their mean.

??? note "One solution"
    ```python title="coast.py"
    import csv

    FILES = {"Vilnius": "LH000026730.csv", "Klaipėda": "LH000026509.csv"}


    def temps(path, month):
        """TAVG in °C of every day of one month in 1991-2020."""
        values = []
        for row in csv.DictReader(open(path)):
            year = int(row["DATE"][:4])
            if row["DATE"][5:7] == month and 1991 <= year <= 2020:
                if row["TAVG"] != "":            # skip days without a mean
                    values.append(float(row["TAVG"]) / 10)   # tenths of °C
        return values


    def mean(values):
        return sum(values) / len(values)


    for month in ["01", "07"]:
        for place, path in FILES.items():
            values = temps(path, month)
            print(f"{month} {place:9} {mean(values):6.2f} °C, {len(values)} days")

    first = temps(FILES["Klaipėda"], "01")[:5]
    print("Klaipėda, 1-5 January 1991:", first, f"mean {mean(first):.2f}")
    ```

    ```text
    $ python coast.py
    01 Vilnius    -3.88 °C, 929 days
    01 Klaipėda   -0.94 °C, 909 days
    07 Vilnius    18.41 °C, 930 days
    07 Klaipėda   18.30 °C, 915 days
    Klaipėda, 1-5 January 1991: [2.4, 1.1, 4.4, 3.7, 4.7] mean 3.26
    ```

    By hand: (2.4 + 1.1 + 4.4 + 3.7 + 4.7) / 5 = 16.3 / 5 = 3.26 °C.

    | 1991–2020 | Vilnius, 156 m | Klaipėda, 6 m | Klaipėda − Vilnius |
    |--|--|--|--|
    | January | −3.88 °C, 929 days | −0.94 °C, 909 days | +2.94 °C |
    | July | 18.41 °C, 930 days | 18.30 °C, 915 days | −0.11 °C |

    In January the coast is 2.9 °C milder than Vilnius, averaged over
    thirty years; Klaipėda misses 21 of the 930 days. In July the two
    stations differ by 0.1 °C: the coast is not cooler, as far as these two
    stations show.

**With your own project data:** two places, groups or instruments of your
own, in two seasons or conditions: one function that reads one group,
called for each, with the number of values each mean rests on.

---

## Part 4 · Show and discuss { #part-4 }

### 10. Three questions about the pairs' answers { #discuss }

<!-- 1:59 · 16 min -->

Two or three pairs show their numbers and read their two sentences.

**Ask the room:** the Vilnius station stands 150 m higher than the Klaipėda station. Air cools by about 0.65 °C per 100 m of height. What does that change in the July answer?

??? note "Answer"
    About 1 °C of the difference is the height: 150 × 0.65 / 100 = 0.98.
    At the height of Klaipėda, Vilnius would be about 19.4 °C in July, so
    the coast is about 1 °C cooler in summer after all, and about 2 °C
    milder in January. Two stations differ in more than one way; name the
    others before giving the difference to one.

**Ask the room:** why the same thirty years at both stations, and not every year each file has?

??? note "Answer"
    Klaipėda's daily means start in 1940, Vilnius's in 1881, and the
    climate has warmed in between. Means over different years mix that
    warming into the difference between the places.

**Ask the room:** Klaipėda's January rests on 909 days, not 930. Could the 21 missing days change the answer?

??? note "Answer"
    Not much. Even if all 21 days had been 10 °C colder than the mean, the
    mean would drop by 21 × 10 / 930 = 0.23 °C: the coast would still be
    2.7 °C milder. Missing days matter when they are many, or all of one
    kind.

A difference between two places means something when both rest on the same years and on enough days, and when the other things that differ, such as the height, are named.

---

## Optional, if the room is fast { #optional }

### 11. Kaunas, between the two { #kaunas }

<!-- — · 10 min -->

Kaunas lies 90 km west of Vilnius, on the way to the coast, at 77 m. Its
file: `LH000026629.csv`, the same address with this name (4.8 MB). Predict,
solve, check the machine's work, hand in, as in section 9: is Kaunas in
January closer to Vilnius or to Klaipėda?

??? note "One solution"
    `coast.py` with one more entry in `FILES`:

    ```python
    FILES = {"Vilnius": "LH000026730.csv", "Kaunas": "LH000026629.csv",
             "Klaipėda": "LH000026509.csv"}
    ```

    ```text
    $ curl -O https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/LH000026629.csv
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100 4695k  100 4695k    0     0  3059k      0  0:00:01  0:00:01 --:--:-- 3059k
    $ python coast.py
    01 Vilnius    -3.88 °C, 929 days
    01 Kaunas     -3.04 °C, 925 days
    01 Klaipėda   -0.94 °C, 909 days
    07 Vilnius    18.41 °C, 930 days
    07 Kaunas     18.56 °C, 927 days
    07 Klaipėda   18.30 °C, 915 days
    Klaipėda, 1-5 January 1991: [2.4, 1.1, 4.4, 3.7, 4.7] mean 3.26
    ```

    Kaunas in January is 0.8 °C milder than Vilnius and 2.1 °C colder than
    Klaipėda: closer to Vilnius. The sea's effect is strongest at the
    coast. With the function written once, the third station is one line.

---

## Aims practised

- ♻️ **Reproducibility:** `environment.yml` names the Python; every number
  of the page comes from a script that anyone can run again on the public
  files.
- 🔧 **Tool-agnostic:** the same Python at the prompt, in a script and in
  VS Code, on macOS and Windows; the data are CSV and JSON texts that any
  language reads.
- ⚙️ **Automation:** a loop does for 51 041 days what was done by hand for
  five, and one function serves every station.
