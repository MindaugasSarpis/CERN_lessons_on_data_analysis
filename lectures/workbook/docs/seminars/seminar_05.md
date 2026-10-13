# Seminar 5 — Can You Compute 7.16 Yourself? Python on the Weather Project

**Paired lecture:** 05 Python Foundations · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student writes a Python script that reads
`weather.csv` line by line, leaves out the `-999` hours and prints the mean
temperature, 7.15997 °C; fixes a script with two bugs; records both
results in the README.

Everything is typed in VS Code: the scripts in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same
in both).

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · Python in VS Code** · 25 min | | |
| 0:00 | [1. The project, and one file from the course](#start) | `mv ~/Downloads/coldest_hour.py scripts/` | `scripts/coldest_hour.py` |
| 0:05 | [2. Python and its extension](#check) | **Python: Select Interpreter** | `Python 3.14.7` |
| 0:15 | [3. The prompt](#prompt) | `python`, then `7.16 * 9 / 5 + 32` | `44.888` |
| | **Part 2 · One line into numbers** · 30 min | | |
| 0:25 | [4. A first script](#script) | `python scripts/first_row.py` | the line printed |
| 0:35 | [5. Cut the line, convert the parts](#split) | `line.split(",")`, `float(parts[1])` | `-4.4 <class 'float'>` |
| 0:45 | [6. Read a traceback](#traceback) | `float(parts[0])` | `ValueError`, line 6 |
| | **Part 3 · The mean of the whole file** · 35 min | | |
| 0:55 | [7. Every line of the file in a list](#lines) | `open(...).read().splitlines()` | `87673` |
| 1:05 | [8. A sum in a loop](#loop) | `for line in lines[1:]:` | `5.782796103659093` |
| 1:15 | [9. Leave out `-999` with `if`](#skip) | `if temp == -999:` | `mean 7.15997 °C` |
| | **Part 4 · Fix a script, record the results** · 30 min | | |
| 1:30 | [10. A traceback in someone else's script](#nameerror) | `python scripts/coldest_hour.py` | `NameError` fixed |
| 1:35 | [11. A wrong number without a message](#wrong) | a `print` in the loop | `-16.3 °C` |
| 1:45 | [12. Record the results in the README](#readme) | `ls -1 scripts` | two lines in the README |
| 1:55 | [13. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [14. Stop at a line: the debugger](#debugger) | `F5` | the loop watched step by step |
| — | [15. Hours per year in a dict](#dict) | `hours[year] = hours.get(year, 0) + 1` | 8784 in leap years |
| — | [16. The mean in two lines](#comprehension) | `[... for line in lines[1:]]` | `7.15997` |

**If time runs short:** stop after section 12; sections 14 to 16 are optional.

??? info "Before the session"
    - **Room:** `weather-project` in the home folder as Seminar 4 left it
      (not yet a Git repository), Miniforge from Seminar 4, internet for the
      extension and one download.
    - **You:** remove the Python extension from your VS Code beforehand, to
      install it with the room in section 2.
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · Python in VS Code { #part-1 }

**0:00 to 0:25**

---

### 1. The project, and one file from the course { #start }

**0:00 · 5 min** · Today's scripts go into `scripts/` of the project of Seminar 4; one script comes from the course.

1. Open VS Code, **File** > **Open Folder...** > `weather-project`. Open
   the terminal: **View** > **Terminal**.
2. On the Releases page
   (`github.com/MindaugasSarpis/weather-project/releases`), under
   **Assets**, click `coldest_hour.py`. The browser saves it in
   **Downloads**.
3. Move it into `scripts`.

    ```text
    mv ~/Downloads/coldest_hour.py scripts/
    ```

    ```text
    ls scripts
    ```

    ```text
    clean_export.py  coldest_hour.py  column_stats.py  rebuild.sh
    ```

**Check:** `scripts/coldest_hour.py` in the Explorer.

??? warning "No `weather-project` from Seminar 4"
    On the same Releases page, click `weather-project-s4.zip` and unpack it
    into your home folder (macOS: double-click it in **Downloads**,
    `Cmd+C`, `Cmd+Shift+H`, `Cmd+V`; Windows: right-click > **Extract
    All...** > **Browse...** > `C:\Users\` and your name > **Extract**). It
    already holds `scripts/coldest_hour.py`: skip steps 2 and 3.

---

### 2. Python and its extension { #check }

**0:05 · 10 min** · The extension colours the code and adds a button that runs it; Python itself comes from Miniforge.

1. The Python of conda's `base`.

    ```text
    python --version
    ```

    ```text
    Python 3.14.7
    ```

2. **Extensions** (`Ctrl+Shift+X`, macOS `Cmd+Shift+X`), type `python`,
   select **Python** by Microsoft, **Install**. Pylance and Python
   Debugger come with it.
3. `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), type `Python: Select
   Interpreter`, `Enter`, pick the entry with `miniforge3` in its path.
4. The Status Bar, bottom right, shows `3.14.7`.

**Check:** `3.14.7` in the terminal and in the Status Bar.

!!! warning "`python: command not found`, or no `(base)` at the start of the prompt"
    conda is not on in this terminal: Seminar 4, section 2.

---

### 3. The prompt { #prompt }

**0:15 · 10 min** · At `>>>` Python works out one line at a time: the place to try a line.

1. Start Python. The prompt changes to `>>>`.

    ```text
    python
    ```

2. The mean of Lecture 1 in Fahrenheit.

    ```text
    7.16 * 9 / 5 + 32
    ```

    ```text
    44.888
    ```

3. Two types.

    ```text
    type(7.16)
    ```

    ```text
    <class 'float'>
    ```

    ```text
    type("7.16")
    ```

    ```text
    <class 'str'>
    ```

4. Text and a number do not add.

    ```text
    "7.16" + 1
    ```

    The last line of the answer:

    ```text
    TypeError: can only concatenate str (not "int") to str
    ```

5. `float` turns the text into a number.

    ```text
    float("7.16") + 1
    ```

    ```text
    8.16
    ```

6. Leave the prompt.

    ```text
    exit()
    ```

**Check:** the shell's prompt again: `%` on a Mac, `$` in Git Bash.

!!! warning "`zsh: command not found: 7.16` or `bash: 7.16: command not found`"
    The line went to the shell, not to Python. Type `python` first.

!!! question "Task: how many rows should `weather.csv` have?"
    The log is hourly from 1 January 2016 to 31 December 2025. 2016, 2020
    and 2024 are leap years. Work it out at `>>>`, then the number of days.

??? note "Answer"
    ```text
    365 * 24 * 10 + 3 * 24
    ```

    ```text
    87672
    ```

    ```text
    87672 // 24
    ```

    ```text
    3653
    ```

    `87672 / 24` gives `3653.0`: `/` always gives a `float`, `//` an `int`.
    `weather.csv` has 87 672 rows below its header, one per hour.

---

## Part 2 · One line into numbers { #part-2 }

**0:25 to 0:55** · The first row of `weather.csv`: `2016-01-01T00:00,-4.4,93,2.5`.

---

### 4. A first script { #script }

**0:25 · 10 min** · A script is the lines of the prompt in a file, run top to bottom.

1. In the Explorer, right-click `scripts` > **New File...**, type
   `first_row.py`, `Enter`.
2. Type, then save (`Ctrl+S`, macOS `Cmd+S`).

    ```python
    line = "2016-01-01T00:00,-4.4,93,2.5"
    print(line)
    print(len(line))
    ```

3. Run it with the ▶ at the top right of the editor. VS Code types a line
   with the paths of Python and the script, then the output appears.
4. Run it by hand, from the project folder.

    ```text
    python scripts/first_row.py
    ```

    ```text
    2016-01-01T00:00,-4.4,93,2.5
    28
    ```

**Check:** the line and `28`, its characters.

---

### 5. Cut the line, convert the parts { #split }

**0:35 · 10 min** · `split` cuts a string into a list; `float` makes a part a number.

1. Replace the file with these lines, save.

    ```python
    line = "2016-01-01T00:00,-4.4,93,2.5"
    parts = line.split(",")
    print(parts)
    print(parts[1], type(parts[1]))
    print(parts[1] * 2)
    temp = float(parts[1])
    print(temp, type(temp))
    print(temp * 2)
    ```

2. Run it.

    ```text
    python scripts/first_row.py
    ```

    ```text
    ['2016-01-01T00:00', '-4.4', '93', '2.5']
    -4.4 <class 'str'>
    -4.4-4.4
    -4.4 <class 'float'>
    -8.8
    ```

    A list counts from 0: `parts[1]` is the second item. A string times 2
    is the string twice; a float times 2 is a number.

**Check:** `-8.8` on the last line.

---

### 6. Read a traceback { #traceback }

**0:45 · 10 min** · An error message is read from the bottom: what went wrong, then where.

1. Replace the file with these lines, save, run.

    ```python
    line = "2016-01-01T00:00,-4.4,93,2.5"
    parts = line.split(",")
    temp = float(parts[1])
    humidity = int(parts[2])
    wind = float(parts[3])
    print(float(parts[0]))
    ```

    ```text
    python scripts/first_row.py
    ```

    ```text
    Traceback (most recent call last):
      File "/Users/smilte/weather-project/scripts/first_row.py", line 6, in <module>
        print(float(parts[0]))
              ~~~~~^^^^^^^^^^
    ValueError: could not convert string to float: '2016-01-01T00:00'
    ```

2. The last line: a time is not a number. The line above: line 6, and
   `^^^` under the part that failed.
3. `Ctrl+click` (macOS `Cmd+click`) the path: VS Code opens line 6.
4. Replace line 6 with two lines, save, run.

    ```python
    time = parts[0]
    print(f"{time}: {temp} °C, {humidity} %, {wind} m/s")
    ```

    ```text
    2016-01-01T00:00: -4.4 °C, 93 %, 2.5 m/s
    ```

    An `f` before the quotes puts the value of each `{name}` into the text.

**Check:** the sentence printed, no traceback.

!!! question "Task: the wind in km/h, the temperature in °F"
    Add one line to `first_row.py` that prints the wind in km/h (× 3.6)
    and the temperature in °F, each with one decimal.

??? note "Answer"
    `:.1f` after a value in `{}` rounds it to one decimal.

    ```python
    print(f"wind {wind * 3.6:.1f} km/h, {temp * 9 / 5 + 32:.1f} °F")
    ```

    ```text
    wind 9.0 km/h, 24.1 °F
    ```

---

## Part 3 · The mean of the whole file { #part-3 }

**0:55 to 1:30** · The same steps for every line of `weather.csv`.

---

### 7. Every line of the file in a list { #lines }

**0:55 · 10 min** · `open` reads a file, `splitlines` cuts it into a list of lines.

1. New file `scripts/mean_temp.py`. Type, save.

    ```python
    lines = open("data/raw/weather.csv").read().splitlines()
    print(len(lines))
    print(lines[0])
    print(lines[1])
    print(lines[-1])
    ```

2. Run it.

    ```text
    python scripts/mean_temp.py
    ```

    ```text
    87673
    time,temp_c,humidity_pct,wind_ms
    2016-01-01T00:00,-4.4,93,2.5
    2025-12-31T23:00,-11.3,100,4.2
    ```

    The header and 87 672 hours. `lines[-1]` is the last item.

**Check:** `87673`.

!!! warning "`FileNotFoundError: ... 'data/raw/weather.csv'`"
    The terminal is not in the project folder. `cd ~/weather-project`,
    then run again.

---

### 8. A sum in a loop { #loop }

**1:05 · 10 min** · `for` runs the indented block once for each line; `lines[1:]` leaves out the header.

1. Replace the file, save, run.

    ```python
    lines = open("data/raw/weather.csv").read().splitlines()

    total = 0.0
    count = 0
    for line in lines[1:]:
        temp = float(line.split(",")[1])
        total = total + temp
        count = count + 1

    print(count, total / count)
    ```

    ```text
    python scripts/mean_temp.py
    ```

    ```text
    87672 5.782796103659093
    ```

2. 5.78: the mean over the raw log of Seminar 4. The 120 hours of
   `-999` are in the sum.

**Check:** `5.782796103659093`.

!!! warning "`IndentationError`"
    The three lines under `for` need the same four spaces. VS Code adds
    them after the `:` and `Enter`.

---

### 9. Leave out `-999` with `if` { #skip }

**1:15 · 15 min** · `if` decides for each line; `continue` goes on to the next line at once.

1. Under `temp = ...`, add two lines, indented as shown.

    ```python
        if temp == -999:
            continue
    ```

2. Replace the last line with three, save, run.

    ```python
    mean = total / count
    print(f"{count} hours, mean {mean:.5f} °C")
    print(f"mean {mean:.2f} °C")
    ```

    ```text
    python scripts/mean_temp.py
    ```

    ```text
    87552 hours, mean 7.15997 °C
    mean 7.16 °C
    ```

3. The same number as `column_stats.py` gave in Seminar 4.

    ```text
    cat results/temp_c.txt
    ```

    ```text
    file    data/processed/weather_valid.csv
    column  temp_c
    rows    87552
    min     -16.3
    max     32.4
    mean    7.15997
    ```

    No `results/` folder: run `./scripts/rebuild.sh` first.

**Check:** `mean 7.15997 °C`, from 87 552 hours.

!!! question "Task: the mean humidity and the windiest hour"
    New script `scripts/humidity_wind.py`. It prints the mean of
    `humidity_pct` (column 2) with one decimal, and the time and speed of
    the windiest hour (`wind_ms`, column 3). Humidity has no `-999`.

??? note "Answer"
    ```python
    lines = open("data/raw/weather.csv").read().splitlines()

    total = 0
    windiest = 0.0
    windiest_time = ""
    for line in lines[1:]:
        parts = line.split(",")
        total = total + int(parts[2])
        wind = float(parts[3])
        if wind > windiest:
            windiest = wind
            windiest_time = parts[0]

    print(f"mean humidity {total / (len(lines) - 1):.1f} %")
    print(f"windiest hour: {windiest_time}, {windiest} m/s")
    ```

    ```text
    mean humidity 79.1 %
    windiest hour: 2019-12-29T16:00, 12.0 m/s
    ```

---

## Part 4 · Fix a script, record the results { #part-4 }

**1:30 to 2:00** · `scripts/coldest_hour.py` came from the course in section 1. It should print the coldest hour of the ten years.

---

### 10. A traceback in someone else's script { #nameerror }

**1:30 · 5 min** · The last line names the problem, and often the fix.

1. Run it.

    ```text
    python scripts/coldest_hour.py
    ```

    ```text
    Traceback (most recent call last):
      File "/Users/smilte/weather-project/scripts/coldest_hour.py", line 13, in <module>
        print(f"coldest hour: {coldest_tme}, {coldest} °C")
                               ^^^^^^^^^^^
    NameError: name 'coldest_tme' is not defined. Did you mean: 'coldest_time'?
    ```

2. On line 13, change `coldest_tme` to `coldest_time`, save, run.

    ```text
    python scripts/coldest_hour.py
    ```

    ```text
    coldest hour: 2019-07-22T00:00, -999.0 °C
    ```

**Check:** no traceback, and a temperature that cannot be.

---

### 11. A wrong number without a message { #wrong }

**1:35 · 10 min** · A script can run to the end and still be wrong. A `print` inside the loop shows how it got there.

1. Under line 11, `coldest_time = parts[0]`, add one line with the same
   indent, save, run.

    ```python
            print(coldest_time, coldest)
    ```

    ```text
    python scripts/coldest_hour.py
    ```

    The first four lines and the last four:

    ```text
    2016-01-01T00:00 -4.4
    2016-01-01T01:00 -4.8
    2016-01-01T02:00 -5.5
    2016-01-01T03:00 -6.0
    ...
    2017-01-15T01:00 -15.4
    2017-01-15T02:00 -16.0
    2019-07-22T00:00 -999.0
    coldest hour: 2019-07-22T00:00, -999.0 °C
    ```

    Each line is a new coldest hour; the last is the first `-999`.

2. Delete the `print` line. Change line 9 so that `-999` never counts,
   save, run.

    ```python
        if temp != -999 and temp < coldest:
    ```

    ```text
    python scripts/coldest_hour.py
    ```

    ```text
    coldest hour: 2025-01-07T05:00, -16.3 °C
    ```

**Check:** `-16.3 °C`, the `min` of `results/temp_c.txt`.

---

### 12. Record the results in the README { #readme }

**1:45 · 10 min** · The README says what was found and which script finds it; Seminar 6 puts the scripts under Git.

1. In `README.md`, under the paragraph of **Result**, add two lines and
   save.

    ```text
    Checked in Python, `scripts/mean_temp.py`: 7.15997 °C.
    The coldest hour, `scripts/coldest_hour.py`: 2025-01-07T05:00, -16.3 °C.
    ```

2. Check.

    ```text
    grep -E 'Checked|coldest' README.md
    ```

    ```text
    Checked in Python, `scripts/mean_temp.py`: 7.15997 °C.
    The coldest hour, `scripts/coldest_hour.py`: 2025-01-07T05:00, -16.3 °C.
    ```

3. The scripts of today, next to those of Seminar 4. `-1`: one name per
   line.

    ```text
    ls -1 scripts
    ```

    ```text
    clean_export.py
    coldest_hour.py
    column_stats.py
    first_row.py
    humidity_wind.py
    mean_temp.py
    rebuild.sh
    ```

    `humidity_wind.py` only if the Task of Part 3 was done.

**Check:** two new lines in the README, and `first_row.py`,
`mean_temp.py`, `coldest_hour.py` in `scripts`.

!!! question "Task: the warmest hour"
    Copy `coldest_hour.py` to `scripts/warmest_hour.py` and change it to
    print the warmest hour. Does it need the `-999` check? Add the result
    to the README.

??? note "Answer"
    ```python
    lines = open("data/raw/weather.csv").read().splitlines()

    warmest = -100.0
    warmest_time = ""
    for line in lines[1:]:
        parts = line.split(",")
        temp = float(parts[1])
        if temp > warmest:
            warmest = temp
            warmest_time = parts[0]

    print(f"warmest hour: {warmest_time}, {warmest} °C")
    ```

    ```text
    warmest hour: 2018-06-18T15:00, 32.4 °C
    ```

    No check is needed: `-999` is never the largest. The start value
    `-100.0` must be below every real temperature. The README line:

    ```text
    The warmest hour, `scripts/warmest_hour.py`: 2018-06-18T15:00, 32.4 °C.
    ```

---

### 13. Wrap up { #wrap-up }

**1:55 · 5 min**

| To | Type |
|--|--|
| run a script | `python scripts/NAME.py`, or ▶ |
| try one line | `python`, then the line at `>>>`; `exit()` |
| cut a line, convert a part | `line.split(",")`, `float(parts[1])` |
| read a file as lines | `open(PATH).read().splitlines()` |
| repeat, decide | `for line in lines[1:]:`, `if temp == -999:` |
| print with decimals | `f"{mean:.2f}"` |
| read a traceback | from the last line up |
| move a downloaded file | `mv ~/Downloads/NAME scripts/` |

Seminar 6 puts these scripts under Git.

---

## Optional, if the room is fast { #optional }

---

### 14. Stop at a line: the debugger { #debugger }

**— · 10 min** · The debugger stops the script at a line and shows every name and its value.

1. Open `coldest_hour.py`. Click left of the number of line 10,
   `coldest = temp`: a red dot, a breakpoint.
2. `F5` > **Python Debugger** > **Python File**. The script stops on line
   10, before it runs it.
3. **Run and Debug** view, **Variables** > **Locals**: `temp = -4.4`,
   `coldest = 100.0`, `coldest_time = ''`.
4. `F5` (Continue): the next stop. `temp = -4.8`, `coldest = -4.4`.
5. `Shift+F5` stops the script. Click the red dot to remove it.

**Check:** at each stop, `coldest` holds the `temp` of the stop before.

---

### 15. Hours per year in a dict { #dict }

**— · 10 min** · A dict keeps a value for each key: here, a count for each year.

1. New file `scripts/hours_per_year.py`. Type, save, run.

    ```python
    lines = open("data/raw/weather.csv").read().splitlines()

    hours = {}
    for line in lines[1:]:
        year = line[:4]
        hours[year] = hours.get(year, 0) + 1

    for year in hours:
        print(year, hours[year])
    ```

    ```text
    python scripts/hours_per_year.py
    ```

    ```text
    2016 8784
    2017 8760
    2018 8760
    2019 8760
    2020 8784
    2021 8760
    2022 8760
    2023 8760
    2024 8784
    2025 8760
    ```

    `line[:4]` is the first four characters. `hours.get(year, 0)` is the
    count so far, `0` for a year not seen yet.

**Check:** 8784 hours in 2016, 2020 and 2024, 24 more than in the others.

---

### 16. The mean in two lines { #comprehension }

**— · 5 min** · A list comprehension builds a list in one line, with an `if` to filter.

1. At the end of `mean_temp.py`, add three lines, save, run.

    ```python
    temps = [float(line.split(",")[1]) for line in lines[1:]]
    valid = [t for t in temps if t != -999]
    print(len(temps), len(valid), f"{sum(valid) / len(valid):.5f}")
    ```

    ```text
    python scripts/mean_temp.py
    ```

    ```text
    87552 hours, mean 7.15997 °C
    mean 7.16 °C
    87672 87552 7.15997
    ```

**Check:** the loop and the two lines give the same mean.

---

## Aims practised

- ♻️ **Reproducibility:** the 7.16 of the README now comes out of a script
  each student wrote and can read line by line.
- 🔧 **Tool-agnostic:** the same `python` line on macOS and Windows; the ▶
  of VS Code runs the same command.
- ⚙️ **Automation:** a loop does for 87 672 lines what was done by hand for
  one.
