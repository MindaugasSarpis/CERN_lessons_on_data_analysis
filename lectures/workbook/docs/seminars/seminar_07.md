# Seminar 7 · Visualisation

**Paired lecture:** 07 Data Visualisation · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** What do ten years of weather look like?

**Today's goal:** every student makes today's conda environment, adds Matplotlib to it, adds a function
`group` to the module `weather.py`, and writes one script,
`scripts/figures.py`, that draws five figures of `weather.csv` into
`results/`: ten years day by day, the year's cycle, the day's cycle, the
yearly means and a histogram; then deletes the figures and draws them all
again with one line.

Everything is typed in VS Code: the script in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same
in both). Each figure opens in VS Code from the Explorer. In the blocks, a
line that starts with `$` is typed in the terminal, a line that starts with
`>>>` is typed at Python's prompt, and every other line is what comes back;
`...` stands for lines left out.

**If time runs short:** skip the Tasks of Parts 2 and 3, but keep
section 11, which draws every figure again with one line; sections 13 to
15 are optional.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page), internet for the download
      (0.6 MB) and for conda: Python about 25 MB on a Mac and 37 MB on
      Windows, Matplotlib with what it needs about 55 MB more on a Mac and
      160 MB on Windows, less when conda has them already. Nothing from
      earlier seminars is needed.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **You:** if you made `s07` before, remove it (`conda env remove -n
      s07`) to make it with the room.
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · Matplotlib in the environment { #part-1 }

<!-- 0:00 to 0:35 -->

Matplotlib draws figures from Python. It goes into the project's environment, then a first figure shows how its pieces fit.

Further reading: [Matplotlib, Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html).

---

### 1. Get today's folder { #start }

<!-- 0:00 · 10 min -->

Today's folder holds the data, the module `weather.py` and `environment.yml`, the list from which conda makes today's environment: Python alone.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s07.zip`. Open VS Code, then the
   terminal (**View** > **Terminal**), and unzip it into the home folder.

    ```text
    $ unzip ~/Downloads/weather-s07.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s07.zip
       creating: /Users/smilte/weather-s07/
    ...
      inflating: /Users/smilte/weather-s07/scripts/weather.py
    $ cd ~/weather-s07
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a zip by itself: then `mv ~/Downloads/weather-s07 ~`
    instead.

2. **File** > **Open Folder...** > `weather-s07` > **Open**.
3. The list for today's environment.

    ```text
    $ cat environment.yml
    name: s07
    channels:
      - conda-forge
    dependencies:
      - python=3.14
    ```

4. Make the environment from it, then switch it on: the prompt starts
   with `(s07)`.

    ```text
    $ conda env create -n s07 -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate s07
    $ conda activate s07
    ```

    `conda: command not found`: install Miniforge as on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

5. VS Code too: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), `Python: Select
   Interpreter`, pick the entry with `envs/s07` in its path. The Status
   Bar shows `s07`.

**Check:** `(s07)` at the start of the prompt, `s07` in the Status Bar.

---

### 2. Install Matplotlib, write it down { #install }

<!-- 0:10 · 10 min -->

A new package goes into the active environment, never into `base`, and into the file that lists it, or the next laptop cannot run the script.

1. Matplotlib is not in it yet.

    ```text
    $ python -c "import matplotlib"
    ModuleNotFoundError: No module named 'matplotlib'
    ```

2. Install it, with its version.

    ```text
    $ conda install matplotlib-base=3.11
    ## Package Plan ##

      environment location: /Users/smilte/miniforge3/envs/s07

      added / updated specs:
        - matplotlib-base=3.11
    ```

    `matplotlib-base` is Matplotlib without a window library of several
    hundred MB; the scripts write their figures to files.

3. At `Proceed ([y]/n)?` press `Enter`. Then ask for the version.

    ```text
    $ python -c "import matplotlib; print(matplotlib.__version__)"
    3.11.2
    ```

4. Export the list again, delete its last line, `prefix: ...`, save.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

5. Open `environment.yml`: Matplotlib is the new last line.

    ```text
    name: s07
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - matplotlib-base=3.11
    ```

**Check:** `3.11.2`, and `- matplotlib-base=3.11` at the end of
`environment.yml`.

!!! warning "`ModuleNotFoundError: No module named 'matplotlib'`"
    The prompt says `(base)`: `conda activate s07`, then again. VS Code's
    Status Bar must show `s07` too (section 1, step 5).

---

### 3. A first figure { #first }

<!-- 0:20 · 15 min -->

A **Figure** is the whole image; an **Axes** is one plot area in it, with its two axes; `ax.plot` draws a line on the Axes; `fig.savefig` writes the image to a file.

1. Four numbers first. New file `scripts/first_figure.py`, the first four
   hours of the log. Type, save.

    ```python
    import matplotlib.pyplot as plt

    hours = [0, 1, 2, 3]
    temps = [-4.4, -4.8, -5.5, -6.0]
    fig, ax = plt.subplots()
    print(type(fig), type(ax))
    ax.plot(hours, temps)
    fig.savefig("results/first.png")
    ```

    `plt.subplots()` makes a Figure with one Axes and hands back both.
    `fig.savefig` writes a file, where `plt.show()` would open a window.

2. Run it.

    ```text
    $ python scripts/first_figure.py
    <class 'matplotlib.figure.Figure'> <class 'matplotlib.axes._axes.Axes'>
    ```

3. In the Explorer, click `results/first.png`: one line falling from −4.4
   to −6.0 over the hours 0 to 3. Matplotlib chose the axis ranges from the
   data.

4. Open `scripts/weather.py`, which came with the folder: a **module**, a
   file of definitions that a script loads with `import weather`.
   `MISSING` is the station's mark for an hour without a temperature,
   `-999`; `read_lines(path)` gives the lines of a file without its
   header, `temp_of(line)` the temperature of one line, `temps(path)`
   every temperature that is not `MISSING`, and `mean(values)` the mean
   of a list.

5. New file `scripts/figures.py`: every hour of the log, `-999` included.
   Type, save.

    ```python
    import matplotlib.pyplot as plt

    import weather

    PATH = "data/raw/weather.csv"

    every = []
    for line in weather.read_lines(PATH):
        every.append(weather.temp_of(line))
    print(len(every), min(every), max(every))

    fig, ax = plt.subplots()
    ax.plot(every)
    fig.savefig("results/every_hour.png")
    ```

    Given one list, `ax.plot` puts each value at its position: 0, 1, 2, …

6. Run it.

    ```text
    $ python scripts/figures.py
    87672 -999.0 32.4
    ```

7. In the Explorer, click `results/every_hour.png`: a wavy band near 0,
   and one line straight down to −999 at about hour 31 000.

**Check:** the drop to −999: the five days of July 2019 without a
temperature.

!!! warning "`FileNotFoundError: ... 'data/raw/weather.csv'`"
    The terminal is not in the project folder: `cd ~/weather-s07`, then
    run again.

!!! question "Task: the humidity, drawn the same way"
    In `figures.py`, append the third value of each line,
    `float(line.split(",")[2])`, instead of `weather.temp_of(line)`. Run,
    look at the figure. Is there a spike? When is the air driest? Change
    it back.

??? success "Answer"
    ```text
    $ python scripts/figures.py
    87672 34.0 100.0
    ```

    No spike: `humidity_pct` has no `-999`; its hours run from 34 to
    100 %. The deepest dips lie where the temperature has its warm humps:
    of the 831 hours below 55 %, 774 are in May to September, 702 between
    12:00 and 18:00. Of the 2540 hours at 100 %, 2155 are in November to
    March.

---

## Part 2 · Ten years, day by day { #part-2 }

<!-- 0:35 to 1:05 -->

One missing value can hide everything else in a figure. A mean per day leaves the missing hours out and puts a date under each point.

---

### 4. Group the hours by day: `group` { #group }

<!-- 0:35 · 10 min -->

A **dictionary of lists**: one key per day, and under it the list of that day's temperatures.

1. At the end of `scripts/weather.py`, add a fifth function, save.

    ```python
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

    `line[0:10]` is the date of a line, `2016-01-01`. The first time a key
    turns up, `groups[key] = []` gives it an empty list; `append` adds each
    temperature to the list of its key; `continue` skips the hours marked
    `-999`.

2. Try it at `>>>`. Python finds `weather.py` in the terminal's folder, so
   start it in `scripts`; the data is then one folder up, `..`.

    ```pycon
    $ cd scripts
    $ python
    >>> import weather
    >>> days = weather.group("../data/raw/weather.csv", 0, 10)
    >>> len(days)
    3648
    >>> days["2016-01-01"][0:4]
    [-4.4, -4.8, -5.5, -6.0]
    >>> len(days["2016-01-01"])
    24
    >>> "2019-07-22" in days
    False
    >>> exit()
    $ cd ..
    ```

    3653 days from 2016 to 2025, less the five days of July 2019 whose
    hours are all `-999`. The first four values are the four hours of
    `first_figure.py`.

**Check:** `3648` keys, and `False` for 22 July 2019.

---

### 5. One mean per day, the date on the x-axis { #days }

<!-- 0:45 · 10 min -->

`datetime.fromisoformat` turns a text such as `2016-01-01` into a date; Matplotlib writes the years under an axis of dates.

1. Replace `figures.py` with this. The first line is new: `datetime`
   comes with Python, no install. The lines from `days = ...` replace the
   lines from `every = []`.

    ```python
    from datetime import datetime

    import matplotlib.pyplot as plt

    import weather

    PATH = "data/raw/weather.csv"

    days = weather.group(PATH, 0, 10)
    dates = []
    day_means = []
    for day in days:
        dates.append(datetime.fromisoformat(day))
        day_means.append(weather.mean(days[day]))
    print(len(dates), dates[0])

    fig, ax = plt.subplots()
    ax.plot(dates, day_means)
    fig.savefig("results/daily_temp.png")
    ```

    A dictionary keeps its keys in the order they came in: the order of
    the file, from 2016-01-01.

2. Run it. `print` writes a date with its time, midnight.

    ```text
    $ python scripts/figures.py
    3648 2016-01-01 00:00:00
    ```

3. Open `results/daily_temp.png`: the years 2016 to 2026 under the axis,
   ten summers and ten winters, from about −13 to 27 °C.

**Check:** no spike, and the years under the x-axis.

---

### 6. Size, label, a title that says the finding { #labels }

<!-- 0:55 · 10 min -->

A figure needs a unit on its axis and a title that says what to see.

1. Replace the three lines from `fig, ax = ...` to `fig.savefig(...)`.

    ```python
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(dates, day_means, linewidth=0.6)
    ax.set_ylabel("Daily mean temperature (°C)")
    ax.set_title("The same cycle every year, from -13 °C to 27 °C")
    fig.savefig("results/daily_temp.png", dpi=150)
    ```

    `figsize` is in inches, 10 wide and 4 high; `dpi=150` gives 1500 by
    600 pixels. The thin line shows the days.

2. Save, run, look.

    ```text
    $ python scripts/figures.py
    3648 2016-01-01 00:00:00
    ```

**Check:** a wide figure, a y-axis label with °C, the title on top.

!!! question "Task: 2025 alone"
    Draw only the days of 2025 into `results/daily_2025.png`. Hint: a
    second loop over `days` that keeps a day when `day[0:4]` is `"2025"`.

??? success "Answer"
    At the end of `figures.py`:

    ```python
    dates_2025 = []
    means_2025 = []
    for day in days:
        if day[0:4] == "2025":
            dates_2025.append(datetime.fromisoformat(day))
            means_2025.append(weather.mean(days[day]))
    print(len(dates_2025), f"{min(means_2025):.1f} {max(means_2025):.1f}")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(dates_2025, means_2025)
    ax.set_ylabel("Daily mean temperature (°C)")
    fig.savefig("results/daily_2025.png", dpi=150)
    ```

    ```text
    $ python scripts/figures.py
    3648 2016-01-01 00:00:00
    365 -13.0 24.0
    ```

    365 days, from −13.0 °C on 7 January to 24.0 °C on 29 July: the
    weather moves the days up and down by several degrees around the
    cycle.

---

## Part 3 · The year's cycle and the day's cycle { #part-3 }

<!-- 1:05 to 1:30 -->

Ten years of hours averaged by month and by hour of the day: the two cycles, without the weather of single days.

---

### 7. One point per month { #monthly }

<!-- 1:05 · 10 min -->

The same `group`, with the month as key, `line[5:7]`: twelve lists, a mean for each.

1. At the end of `figures.py`, add these lines, save, run.

    ```python
    months = weather.group(PATH, 5, 7)
    month_keys = []
    month_means = []
    for month in months:
        month_keys.append(month)
        month_means.append(weather.mean(months[month]))
    print(month_keys)
    print(f"{min(month_means):.1f} {max(month_means):.1f}")
    ```

    ```text
    $ python scripts/figures.py
    3648 2016-01-01 00:00:00
    ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    -3.9 18.5
    ```

    The keys come in the order of the file, January first.

2. Under them, the figure. A list of texts on the x-axis puts each text
   under its point, in the order of the list.

    ```python
    fig, ax = plt.subplots()
    ax.plot(month_keys, month_means, "o-")
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean temperature, 2016 to 2025 (°C)")
    ax.set_title("July is 22.4 °C warmer than January")
    fig.savefig("results/monthly_temp.png", dpi=150)
    ```

    `"o-"` draws a point at each value and a line between neighbours: the
    months follow each other round the year.

3. Save, run, open `results/monthly_temp.png`.

**Check:** a hill with its top at `07`, 18.5 °C, and its bottom at `01`,
−3.9 °C.

---

### 8. The day's cycle: one mean per hour { #daily-cycle }

<!-- 1:15 · 15 min -->

The hour of the day is `line[11:13]`: 24 lists, each holding one hour of every day of ten years.

1. At the end of `figures.py`, add these lines, save.

    ```python
    by_hour = weather.group(PATH, 11, 13)
    hour_keys = []
    hour_means = []
    for hour in by_hour:
        hour_keys.append(hour)
        hour_means.append(weather.mean(by_hour[hour]))
    print(f"{min(hour_means):.1f} {max(hour_means):.1f}")

    fig, ax = plt.subplots()
    ax.plot(hour_keys, hour_means, "o-")
    ax.set_xticks(["00", "03", "06", "09", "12", "15", "18", "21"])
    ax.set_xlabel("Hour of the day")
    ax.set_ylabel("Mean temperature, 2016 to 2025 (°C)")
    ax.set_title("Coldest at 03:00, warmest at 15:00, 7 °C apart")
    fig.savefig("results/day_cycle.png", dpi=150)
    ```

    `set_xticks` writes a label only under the keys it is given: every
    third hour, so the 24 labels do not crowd.

2. Run it.

    ```text
    $ python scripts/figures.py
    ...
    -3.9 18.5
    3.7 10.7
    ```

3. Open `results/day_cycle.png`: lowest at 03:00, 3.7 °C, highest at
   15:00, 10.7 °C.

**Check:** one curve with 24 points, its bottom at `03`, its top at `15`.

!!! question "Task: January and July"
    Draw the day's cycle of January and of July as two lines in one
    figure, `results/day_cycle_jan_jul.png`. Give each `ax.plot` a
    `label="January"` (or `"July"`) and call `ax.legend()` before
    `fig.savefig`: the legend lists the labels. Which day swings more?
    Hint: `group` mixes all months; copy its loop into `figures.py` and
    keep only the lines whose `line[5:7]` is the month.

??? success "Answer"
    A dictionary gives each month's name; the outer loop runs once per
    month and draws one line.

    ```python
    names = {"01": "January", "07": "July"}
    fig, ax = plt.subplots()
    for month in names:
        cycle = {}
        for line in weather.read_lines(PATH):
            temp = weather.temp_of(line)
            if temp != weather.MISSING and line[5:7] == month:
                hour = line[11:13]
                if hour not in cycle:
                    cycle[hour] = []
                cycle[hour].append(temp)
        means = []
        for hour in cycle:
            means.append(weather.mean(cycle[hour]))
        print(names[month], f"{min(means):.1f} {max(means):.1f}")
        ax.plot(hour_keys, means, "o-", label=names[month])
    ax.set_xticks(["00", "03", "06", "09", "12", "15", "18", "21"])
    ax.set_xlabel("Hour of the day")
    ax.set_ylabel("Mean temperature, 2016 to 2025 (°C)")
    ax.set_title("A July day swings 10 °C, a January day 4 °C")
    ax.legend()
    fig.savefig("results/day_cycle_jan_jul.png", dpi=150)
    ```

    ```text
    $ python scripts/figures.py
    ...
    January -5.9 -1.8
    July 13.5 23.6
    ```

    July by far: about 10 °C between 03:00 and 15:00, January about 4 °C.
    Both lines are lowest at 03:00 and highest at 15:00.

---

## Part 4 · Is it getting warmer, as a figure { #part-4 }

<!-- 1:30 to 2:00 -->

The mean of each of the ten years, and the 87 552 hours behind them.

---

### 9. Ten points, a reference line, a legend { #yearly }

<!-- 1:30 · 10 min -->

Points, not bars: the y-axis does not start at zero, and the eye compares the points with the line.

1. At the end of `figures.py`, add these lines, save.

    ```python
    by_year = weather.group(PATH, 0, 4)
    years = []
    year_means = []
    for year in by_year:
        years.append(year)
        year_means.append(weather.mean(by_year[year]))
    temps = weather.temps(PATH)
    all_mean = weather.mean(temps)
    print(len(temps), f"{all_mean:.2f}")

    fig, ax = plt.subplots()
    ax.plot(years, year_means, "o", label="mean of the year")
    ax.axhline(all_mean, color="grey", linewidth=1, label="mean of all hours")
    ax.set_ylim(5, 9)
    ax.set_xlabel("Year")
    ax.set_ylabel("Mean temperature (°C)")
    ax.set_title("Ten years around 7.16 °C, the last one the coldest")
    ax.legend()
    fig.savefig("results/yearly_temp.png", dpi=150)
    ```

2. Run it.

    ```text
    $ python scripts/figures.py
    ...
    3.7 10.7
    87552 7.16
    ```

3. Open `results/yearly_temp.png`. `"o"` draws points without a line:
   ten separate years, nothing measured between them;
   `axhline` the grey line at 7.16 °C; `label=` names each, and
   `ax.legend()` lists the names in a box.

**Check:** ten points above and below the line, the last one, 2025, lowest.

---

### 10. A histogram of the hours { #histogram }

<!-- 1:40 · 10 min -->

`ax.hist` cuts a range into bins of equal width, counts the values in each bin and draws one bar per bin.

1. At the end of `figures.py`, add these lines, save, run.

    ```python
    fig, ax = plt.subplots()
    ax.hist(temps)
    ax.set_xlabel("Hourly temperature (°C)")
    ax.set_ylabel("Hours")
    fig.savefig("results/temp_hist.png", dpi=150)
    ```

2. Open `results/temp_hist.png`: ten bars, one wide hill. By default
   `hist` cuts the range from the smallest value, −16.3, to the largest,
   32.4, into 10 bins of 4.87 °C.

3. Bins of 1 °C: 50 of them from −17 to 33. Replace the three lines from
   `ax.hist(temps)` to `ax.set_ylabel("Hours")` with these four, save,
   run.

    ```python
    ax.hist(temps, bins=50, range=(-17, 33))
    ax.set_xlabel("Hourly temperature (°C)")
    ax.set_ylabel("Hours per 1 °C")
    ax.set_title("Two peaks: winter near -1 °C, summer near 12 °C")
    ```

    The y-label states the bin width: a count per bin means nothing
    without it.

4. Open the figure again. The tallest bar, −1 to 0 °C, holds 3848 hours:
   the winter hours near freezing. The second peak is highest at 11 to
   12 °C, 3032 hours. Between them, the bar of 7 to 8 °C, where the mean
   7.16 lies, holds 2706: fewer hours are near the mean than near either
   peak.

**Check:** two peaks, 50 bars of 1 °C from −17 to 33.

!!! question "Task: other bin widths"
    Draw the histogram with bins of 0.05 °C and of 10 °C. What does each
    show, and what does it hide?

??? success "Answer"
    ```python
    ax.hist(temps, bins=1000, range=(-17, 33))
    ```

    ```python
    ax.hist(temps, bins=6, range=(-20, 40))
    ```

    0.05 °C: a comb, thin bars with gaps between them; 523 of the 1000
    bins are empty. The station writes tenths of a degree, so a bin of
    0.05 °C between two tenths stays empty: the figure shows how the
    values were written down, not the weather. 10 °C: six bars and one
    hump; the two peaks are gone. 1 °C is narrow enough for the shape and
    wide enough for smooth counts.

---

### 11. Draw every figure again { #redraw }

<!-- 1:50 · 5 min -->

The script draws all five figures again in a few seconds, so the script, not the figures, is what is kept and described.

1. Delete the figures, run the script, list what it made.

    ```text
    $ rm results/*.png
    $ python scripts/figures.py
    3648 2016-01-01 00:00:00
    ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    -3.9 18.5
    3.7 10.7
    87552 7.16
    $ ls -1 results
    daily_temp.png
    day_cycle.png
    monthly_temp.png
    temp_hist.png
    yearly_temp.png
    ```

    `-1`: one name per line. `first.png` and `every_hour.png` do not come
    back: `figures.py` no longer draws them. Lines of a Task left in
    `figures.py` print and draw theirs too.

2. In `README.md`, at the end of **How to rebuild**, add two lines and
   save: how anyone draws the figures again.

    ```text
    The figures: `python scripts/figures.py` draws five PNG files into
    `results/`, with the environment of `environment.yml`.
    ```

**Check:** five figures in `results`, and the README says which line makes
them.

---

### 12. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->

The lines of today, by what they do.

| To | Type |
|--|--|
| make the environment of a folder | `conda env create -n s07 -f environment.yml`, `conda activate s07` |
| add a package | `conda install NAME=VERSION` |
| write it down | `conda env export --from-history -f environment.yml`, delete `prefix:` |
| group the hours by a part of the time | `weather.group(PATH, 5, 7)`: one list per month |
| a text into a date | `datetime.fromisoformat("2016-01-01")` |
| a figure | `fig, ax = plt.subplots()`, `ax.plot(x, y)`, `fig.savefig(PATH, dpi=150)` |
| points, a line, a legend | `ax.plot(x, y, "o")`, `"o-"`, `ax.axhline(y)`, `label=...`, `ax.legend()` |
| labels | `ax.set_xlabel`, `ax.set_ylabel` with the unit, `ax.set_title` with the finding |
| a histogram | `ax.hist(values, bins=50, range=(-17, 33))` |

---

## Optional, if the room goes fast { #optional }

---

### 13. A heatmap of one year { #heatmap }

<!-- — · 10 min -->

Colour as the third axis: the 24 hours across, the 365 days of 2025 down.

1. At the end of `figures.py`, add these lines, save, run.

    ```python
    grid = []
    for day in days:
        if day[0:4] == "2025":
            grid.append(days[day])
    print(len(grid), len(grid[0]))

    fig, ax = plt.subplots(figsize=(6, 8))
    im = ax.imshow(grid, aspect="auto")
    fig.colorbar(im, ax=ax, label="Temperature (°C)")
    ax.set_xlabel("Hour of the day")
    ax.set_ylabel("Day of 2025")
    ax.set_title("2025: warmest on summer afternoons")
    fig.savefig("results/heatmap_2025.png", dpi=150)
    ```

    ```text
    $ python scripts/figures.py
    ...
    365 24
    ```

    `grid` is a list of 365 lists of 24 temperatures; `imshow` draws one
    coloured square per value, the first list at the top.
    `aspect="auto"` lets the squares stretch to fill the figure.

**Check:** a yellow patch in the middle rows, between the hours 10 and 18.

---

### 14. One style for all figures { #style }

<!-- — · 5 min -->

Settings in `plt.rcParams` hold for every figure the script draws after them.

1. Under the `import` lines, add these lines, save, run.

    ```python
    plt.rcParams.update({
        "savefig.bbox": "tight",
        "axes.spines.top": False,
        "axes.spines.right": False,
    })
    ```

2. Open the figures: no frame line at the top and the right, and no white
   border around the plot.

**Check:** every figure changed, by three lines in one place.

---

### 15. Advanced tasks { #advanced }

<!-- — · 25 min -->

Harder figures from the same script, for a room that is done early. Each answer is folded under its task; add the lines at the end of `figures.py`.

!!! question "Advanced task: hours below 0 °C, per year"
    Count the hours below 0 °C in each year and draw them as bars,
    `ax.bar(years, counts)`. Which year had the most? Does it fit the
    yearly means of section 9?

??? success "Answer"
    `by_year` and `years` come from section 9.

    ```python
    frost = []
    for year in by_year:
        count = 0
        for temp in by_year[year]:
            if temp < 0:
                count = count + 1
        frost.append(count)
    print(frost)

    fig, ax = plt.subplots()
    ax.bar(years, frost)
    ax.set_ylabel("Hours below 0 °C")
    ax.set_title("2025 had the most hours below 0 °C, 2023 the fewest")
    fig.savefig("results/frost_hours.png", dpi=150)
    ```

    ```text
    $ python scripts/figures.py
    ...
    [2112, 2419, 1953, 2443, 2230, 2110, 2314, 1845, 2249, 2677]
    ```

    2025, 2677 hours: also the coldest year, 5.98 °C. 2023, the warmest
    year at 8.31 °C, had the fewest, 1845. Bars start at zero, so their
    heights compare. The 120 missing hours of 2019 do not change its
    count: no July hour of the log is below 0 °C, the coldest is 5.7 °C.

!!! question "Advanced task: humidity against temperature"
    Plot every hour as a point, temperature across and humidity up
    (`ax.scatter(x, y)`). First check `humidity_pct` for a missing mark,
    and leave out the hours whose temperature is `-999`. 87 552 points
    cover each other: what makes the dense part visible?

??? success "Answer"
    `humidity_pct` runs from 34 to 100 (Task of Part 1): no mark. Tiny,
    almost transparent points: `s=1` is their size, `alpha=0.05` their
    opacity, so only places with many points look dark.

    ```python
    x = []
    y = []
    for line in weather.read_lines(PATH):
        temp = weather.temp_of(line)
        if temp != weather.MISSING:
            x.append(temp)
            y.append(float(line.split(",")[2]))

    fig, ax = plt.subplots()
    ax.scatter(x, y, s=1, alpha=0.05)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Humidity (%)")
    ax.set_title("Humid when cold, drier when warm")
    fig.savefig("results/humidity_vs_temp.png", dpi=150)
    ```

    A falling cloud: of the 22 352 hours below 0 °C, 83 % are above 80 %
    humidity; of the 1251 hours above 25 °C, 82 % lie between 45 and
    65 %. The humidity is a whole number, so the points stand in rows.

!!! question "Advanced task: mark the warmest and the coldest month"
    On the figure of section 7, write the month and its mean next to the
    highest and the lowest point, with an arrow:
    `ax.annotate(text, xy=(x, y), xytext=(30, 0), textcoords="offset points", arrowprops={"arrowstyle": "->"})`.
    `xy` is the point; `xytext` puts the text 30 points to the right of
    it.

??? success "Answer"
    `month_means.index(value)` gives the position of a value in the list.

    ```python
    warm = month_means.index(max(month_means))
    cold = month_means.index(min(month_means))
    fig, ax = plt.subplots()
    ax.plot(month_keys, month_means, "o-")
    for i in [warm, cold]:
        text = f"{month_keys[i]}: {month_means[i]:.1f} °C"
        ax.annotate(text, xy=(month_keys[i], month_means[i]),
                    xytext=(30, 0), textcoords="offset points",
                    arrowprops={"arrowstyle": "->"})
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean temperature, 2016 to 2025 (°C)")
    ax.set_title("July is 22.4 °C warmer than January")
    fig.savefig("results/monthly_annotated.png", dpi=150)
    ```

    `07: 18.5 °C` beside the top of the hill, `01: -3.9 °C` beside its
    lowest point. A label on the figure saves the reader from reading the
    value off the axis.

!!! question "Advanced task: PNG, SVG or PDF?"
    Save the figure of section 6 also as `.svg` and `.pdf` (the format
    follows the file name). Compare the three sizes, and open each:
    which stays sharp when you zoom in?

??? success "Answer"
    Under `fig.savefig("results/daily_temp.png", dpi=150)` of section 6:

    ```python
    fig.savefig("results/daily_temp.svg")
    fig.savefig("results/daily_temp.pdf")
    ```

    ```text
    $ python scripts/figures.py
    ...
    $ wc -c results/daily_temp.*
     42249 results/daily_temp.pdf
    128588 results/daily_temp.png
     95191 results/daily_temp.svg
    266028 total
    ```

    Your sizes may differ a little; macOS pads the numbers differently.
    PNG is pixels: zoomed in, the line turns into steps. SVG and PDF
    store the line itself and stay sharp at any size, for a report or a
    poster; PNG is for a web page or a slide.

---

## Aims practised

- ♻️ **Reproducibility:** one script draws every figure from the raw data;
  `environment.yml` lists the package it needs, with its version.
- 📁 **Files:** the figures in `results/` are drawn by the script;
  the script is what is kept and described.
- ⚙️ **Automation:** five figures in one run, again after every change;
  one function, `group`, groups the hours by day, month, hour and year.
