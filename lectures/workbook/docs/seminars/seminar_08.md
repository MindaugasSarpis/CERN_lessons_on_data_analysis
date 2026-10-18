# Seminar 8 · Visualisation

**Paired lecture:** 08 Data Visualisation · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** What does a year of weather look like?

**Today's goal:** every student makes today's conda environment, adds
Matplotlib to it, and writes one script, `scripts/figures.py`, that draws
five figures of `weather.csv` into `results/`: ten years day by day, the
year's cycle, the day's cycle, the yearly means and a histogram; then
deletes the figures and draws them all again with one line.

Everything is typed in VS Code: the script in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same
in both). Each figure opens in VS Code from the Explorer. In the blocks, a
line that starts with `$` is typed in the terminal, and every other line is
what comes back; `...` stands for lines left out.

**If time runs short:** stop after section 10; sections 12 to 14 are optional.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page), internet for the download and
      for conda (Python and NumPy about 40 MB, Matplotlib about 10 MB, less
      when conda has them already). Nothing from earlier seminars is
      needed.
    - **You:** if you made `s08` before, remove it (`conda env remove -n
      s08`) to make it with the room.
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · Matplotlib in the environment { #part-1 }

<!-- 0:00 to 0:30 -->

Matplotlib draws figures from Python. It goes into the project's environment, then a first figure shows how its pieces fit.

Further reading: [Matplotlib, Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html).

---

### 1. Get today's folder { #start }

<!-- 0:00 · 10 min -->

Today's folder holds the data and `environment.yml`, the list from which conda makes today's environment: Python and NumPy.

1. On the [Releases page](https://github.com/MindaugasSarpis/weather-project/releases),
   under **Assets**, click `weather-s08.zip`. Open VS Code, then the
   terminal (**View** > **Terminal**), and unzip it into the home folder.

    ```text
    $ unzip ~/Downloads/weather-s08.zip -d ~
    Archive:  /Users/smilte/Downloads/weather-s08.zip
       creating: /Users/smilte/weather-s08/
    ...
      inflating: /Users/smilte/weather-s08/scripts/rebuild.sh
    $ cd ~/weather-s08
    $ ls
    README.md  data  environment.yml  results  scripts
    ```

    Safari unpacks a zip by itself: then `mv ~/Downloads/weather-s08 ~`
    instead.

2. **File** > **Open Folder...** > `weather-s08` > **Open**.
3. The list for today's environment.

    ```text
    $ cat environment.yml
    name: s08
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - numpy=2.5
    ```

4. Make the environment from it, then switch it on: the prompt starts
   with `(s08)`.

    ```text
    $ conda env create -n s08 -f environment.yml
    Channels:
     - conda-forge
    ...
    #     $ conda activate s08
    $ conda activate s08
    ```

5. VS Code too: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), `Python: Select
   Interpreter`, pick the entry with `envs/s08` in its path. The Status
   Bar shows `s08`.

**Check:** `(s08)` at the start of the prompt, `s08` in the Status Bar.

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

      environment location: /Users/smilte/miniforge3/envs/s08

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
    name: s08
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - numpy=2.5
      - matplotlib-base=3.11
    ```

**Check:** `3.11.2`, and `- matplotlib-base=3.11` at the end of
`environment.yml`.

!!! warning "`ModuleNotFoundError: No module named 'matplotlib'`"
    The prompt says `(base)`: `conda activate s08`, then again. VS Code's
    Status Bar must show `s08` too (section 1, step 5).

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

2. Run it.

    ```text
    $ python scripts/first_figure.py
    <class 'matplotlib.figure.Figure'> <class 'matplotlib.axes._axes.Axes'>
    ```

3. In the Explorer, click `results/first.png`: one line falling from −4.4
   to −6.0 over the hours 0 to 3. Matplotlib chose the axis ranges from the
   data.

4. New file `scripts/figures.py`: first the paths and the data. Type.

    ```python
    from pathlib import Path

    import matplotlib.pyplot as plt
    import numpy as np

    ROOT = Path(__file__).resolve().parent.parent
    path = ROOT / "data/raw/weather.csv"
    OUT = ROOT / "results"
    OUT.mkdir(exist_ok=True)

    temp = np.loadtxt(path, delimiter=",", skiprows=1, usecols=1)
    day_means = temp.reshape(3653, 24).mean(axis=1)
    dates = np.arange("2016-01-01", "2026-01-01", dtype="datetime64[D]")
    ```

    `reshape(3653, 24)`: one row of 24 hours per day; `mean(axis=1)`
    averages each row.

5. Under them, the figure, as in `first_figure.py`. Save.

    ```python
    fig, ax = plt.subplots()
    ax.plot(dates, day_means)
    fig.savefig(OUT / "daily_temp.png")
    ```

6. Run it. It prints nothing.

    ```text
    $ python scripts/figures.py
    ```

7. In the Explorer, click `results/daily_temp.png`. A wavy band near 0,
   and one line straight down to −1000 in 2019.

**Check:** the spike in 2019: the five days of `-999`.

!!! question "Task: the humidity, drawn the same way"
    In `figures.py`, change `usecols=1` to `usecols=2`, run, look at the
    figure. Is there a spike? When is the air most humid? Change it back.

??? success "Answer"
    No spike: `humidity_pct` has no `-999`. The band is highest in winter
    (the January mean is 86.8 %) and lowest in summer (71.8 % in July).

---

## Part 2 · Ten years, day by day { #part-2 }

<!-- 0:30 to 0:55 -->

One missing value can hide everything else in a figure.

---

### 4. Leave out the missing days { #mask }

<!-- 0:30 · 10 min -->

`day_means != -999` is `True` for every day with readings, a **mask**; indexing both `dates` and `day_means` with it keeps each date with its day.

1. Under the `dates = ...` line, add one line.

    ```python
    ok = day_means != -999
    ```

2. Change the `ax.plot` line, save.

    ```python
    ax.plot(dates[ok], day_means[ok])
    ```

3. Run it.

    ```text
    $ python scripts/figures.py
    ```

4. The figure in VS Code updates: ten summers and ten winters, the y-axis
   from about −15 to 30.

**Check:** no spike, and the same cycle each year.

---

### 5. Size, label, a title that says the finding { #labels }

<!-- 0:40 · 15 min -->

A figure needs a unit on its axis and a title that says what to see.

1. Replace the three lines from `fig, ax = ...` to `fig.savefig(...)`.

    ```python
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(dates[ok], day_means[ok], linewidth=0.6)
    ax.set_ylabel("Daily mean temperature (°C)")
    ax.set_title("The same cycle every year, from -13 °C to 27 °C")
    fig.savefig(OUT / "daily_temp.png", dpi=150)
    ```

    `figsize` is in inches, 10 wide and 4 high; `dpi=150` gives 1500 by
    600 pixels. The thin line shows the days.

2. Save, run, look.

    ```text
    $ python scripts/figures.py
    ```

**Check:** a wide figure, a y-axis label with °C, the title on top.

!!! question "Task: 2025 alone"
    Draw only the days of 2025 into `results/daily_2025.png`. Hint: a
    second mask on `dates`, joined to `ok` with `&`.

??? success "Answer"
    ```python
    in_2025 = ok & (dates >= np.datetime64("2025-01-01"))
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(dates[in_2025], day_means[in_2025])
    ax.set_ylabel("Daily mean temperature (°C)")
    fig.savefig(OUT / "daily_2025.png", dpi=150)
    ```

    365 days, from −13.0 °C in January to 24.0 °C in July: the weather
    moves the days up and down by several degrees around the cycle.

---

## Part 3 · The year's cycle and the day's cycle { #part-3 }

<!-- 0:55 to 1:25 -->

Averages over ten years show what the noise of single days hides.

---

### 6. One point per month { #monthly }

<!-- 0:55 · 15 min -->

Twelve means, one for each month of all ten years, as points joined by a line.

1. At the end of the file, add these lines.

    ```python
    time = np.loadtxt(path, delimiter=",", skiprows=1, usecols=0, dtype=str)
    valid = temp != -999
    month = np.array([int(t[5:7]) for t in time])
    months = range(1, 13)
    month_means = [temp[(month == m) & valid].mean() for m in months]
    print(np.round(month_means, 1))
    ```

2. Under them, the figure.

    ```python
    fig, ax = plt.subplots()
    ax.plot(months, month_means, marker="o")
    ax.set_xticks(months, list("JFMAMJJASOND"))
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean temperature, 2016 to 2025 (°C)")
    ax.set_title("July is 22 °C warmer than January")
    fig.savefig(OUT / "monthly_temp.png", dpi=150)
    ```

    `set_xticks` puts a mark at 1 to 12 and writes a letter under each.

3. Save, run, open `results/monthly_temp.png`.

    ```text
    $ python scripts/figures.py
    [-3.9 -2.4  1.2  6.4 12.2 17.2 18.5 16.1 13.   6.9  2.6 -2.3]
    ```

**Check:** a hill with its top in July, 18.5 °C, and its bottom in
January, −3.9 °C.

---

### 7. Two lines and a legend { #daily-cycle }

<!-- 1:10 · 15 min -->

The mean of each hour of the day, for January and for July; a `label` on each line, `ax.legend()` lists them.

1. At the end of the file, add these lines, save.

    ```python
    hour = np.array([int(t[11:13]) for t in time])
    hours = range(24)
    fig, ax = plt.subplots()
    for m, name in [(1, "January"), (7, "July")]:
        means = [temp[(month == m) & (hour == h) & valid].mean() for h in hours]
        print(name, round(min(means), 1), round(max(means), 1))
        ax.plot(hours, means, marker="o", label=name)
    ax.set_xticks(range(0, 24, 3))
    ax.set_xlabel("Hour of the day")
    ax.set_ylabel("Mean temperature (°C)")
    ax.set_title("A July day swings 10 °C, a January day 4 °C")
    ax.legend()
    fig.savefig(OUT / "day_cycle.png", dpi=150)
    ```

2. Run it.

    ```text
    $ python scripts/figures.py
    ...
    January -5.9 -1.8
    July 13.5 23.6
    ```

3. Open `results/day_cycle.png`: both lines are lowest at 03:00 and
   highest at 15:00.

**Check:** two lines, a legend with January and July.

!!! question "Task: spring and autumn"
    Add April and October to the figure. Which of the two days swings
    more?

??? success "Answer"
    ```python
    for m, name in [(1, "January"), (4, "April"), (7, "July"), (10, "October")]:
    ```

    ```text
    January -5.9 -1.8
    April 3.0 9.9
    July 13.5 23.6
    October 3.3 10.5
    ```

    October by a little: 7.2 °C against 6.9 °C. The two lines nearly lie
    on each other.

---

## Part 4 · Is it getting warmer, as a figure { #part-4 }

<!-- 1:25 to 2:00 -->

The mean of each of the ten years, and the 87 552 hours behind them.

---

### 8. Ten points and a reference line { #yearly }

<!-- 1:25 · 10 min -->

Points, not bars: the y-axis does not start at zero, and the eye compares the points with the line.

1. At the end of the file, add these lines, save.

    ```python
    year = np.array([int(t[:4]) for t in time])
    years = range(2016, 2026)
    year_means = [temp[(year == y) & valid].mean() for y in years]
    fig, ax = plt.subplots()
    ax.plot(years, year_means, "o")
    ax.axhline(temp[valid].mean(), color="grey", linewidth=1)
    ax.set_xticks(years)
    ax.set_ylim(5, 9)
    ax.set_ylabel("Yearly mean temperature (°C)")
    ax.set_title("No trend: the years scatter around 7.16 °C")
    fig.savefig(OUT / "yearly_temp.png", dpi=150)
    ```

2. Run it.

    ```text
    $ python scripts/figures.py
    ```

3. Open `results/yearly_temp.png`. `"o"` draws points without a line;
   `axhline` the grey line at 7.16 °C.

**Check:** ten points above and below the line, the last one, 2025, lowest.

---

### 9. A histogram of the hours { #histogram }

<!-- 1:35 · 10 min -->

`ax.hist` counts the values in bins; the bins are chosen from the smallest and largest value, −16.3 and 32.4.

1. At the end of the file, add these lines, save.

    ```python
    fig, ax = plt.subplots()
    ax.hist(temp[valid], bins=np.arange(-17, 34, 1))
    ax.set_xlabel("Hourly temperature (°C), bins of 1 °C")
    ax.set_ylabel("Hours")
    ax.set_title("Two humps: one near 0 °C, one near 12 °C")
    fig.savefig(OUT / "temp_hist.png", dpi=150)
    ```

2. Run it.

    ```text
    $ python scripts/figures.py
    ```

3. Open `results/temp_hist.png`. The highest bar, −1 to 0 °C, holds
   3848 hours: the winter hours near freezing. The second hump, around 11
   to 12 °C, holds the rest of the year.

**Check:** two humps, bars of 1 °C from −17 to 34.

!!! question "Task: other bin widths"
    Draw the histogram with bins of 0.1 °C and of 10 °C. What does each
    show, and what does it hide?

??? success "Answer"
    ```python
    ax.hist(temp[valid], bins=np.arange(-17, 34, 0.1))
    ```

    ```python
    ax.hist(temp[valid], bins=np.arange(-20, 40, 10))
    ```

    0.1 °C: about 300 hours a bin, bars that jump from one to the next; the
    noise of the counts is as large as the humps. 10 °C: five bars, and
    the two humps are gone. 1 °C is narrow enough for the shape and wide
    enough for smooth counts.

---

### 10. Draw every figure again { #commit }

<!-- 1:45 · 10 min -->

The five figures are made files: the script draws all of them again in a few seconds, so the script is what to keep and to describe.

1. Delete the five figures, run the script, list what it made.

    ```text
    $ rm results/*.png
    $ python scripts/figures.py
    [-3.9 -2.4  1.2  6.4 12.2 17.2 18.5 16.1 13.   6.9  2.6 -2.3]
    January -5.9 -1.8
    July 13.5 23.6
    $ ls -1 results
    daily_temp.png
    day_cycle.png
    monthly_temp.png
    temp_hist.png
    yearly_temp.png
    ```

    `-1`: one name per line. `first.png` is gone for good: no script in
    the list makes it.

2. In `README.md`, at the end of **How to rebuild**, add two lines and
   save: how anyone draws the figures again.

    ```text
    The figures: `python scripts/figures.py` draws five PNG files into
    `results/`, with the environment of `environment.yml`.
    ```

**Check:** five figures in `results`, and the README says which line makes
them.

---

### 11. Wrap up { #wrap-up }

<!-- 1:55 · 5 min -->


| To | Type |
|--|--|
| make the environment of a folder | `conda env create -n s08 -f environment.yml`, `conda activate s08` |
| add a package | `conda install NAME=VERSION` |
| write it down | `conda env export --from-history -f environment.yml`, delete `prefix:` |
| a figure | `fig, ax = plt.subplots()`, `ax.plot(x, y)`, `fig.savefig(PATH, dpi=150)` |
| points, a line, a legend | `ax.plot(x, y, "o")`, `ax.axhline(y)`, `label=...`, `ax.legend()` |
| labels | `ax.set_xlabel`, `ax.set_ylabel` with the unit, `ax.set_title` with the finding |
| a histogram | `ax.hist(values, bins=np.arange(start, stop, width))` |

---

## Optional, if the room goes fast { #optional }

---

### 12. A heatmap of one year { #heatmap }

<!-- — · 10 min -->

Colour as the third axis: the 365 days of 2025 across, the 24 hours up.

1. At the end of the file, add these lines, save, run.

    ```python
    last = temp.reshape(3653, 24)[-365:]
    fig, ax = plt.subplots(figsize=(10, 4))
    im = ax.imshow(last.T, aspect="auto", origin="lower")
    fig.colorbar(im, ax=ax, label="Temperature (°C)")
    ax.set_xlabel("Day of 2025")
    ax.set_ylabel("Hour of the day")
    ax.set_title("2025 hour by hour: the warmest hours are summer afternoons")
    fig.savefig(OUT / "heatmap_2025.png", dpi=150)
    ```

    `[-365:]` is the last 365 days, 2025; `.T` turns the days into columns.
    `origin="lower"` puts midnight at the bottom.

**Check:** a yellow band in the middle of the year, brightest between
hours 12 and 18.

---

### 13. One style for all figures { #style }

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

### 14. Advanced tasks { #advanced }

<!-- — · 25 min -->

Harder figures from the same script, for a room that is done early. Each answer is folded under its task; add the lines at the end of `figures.py`.

!!! question "Advanced task: two panels, one time axis"
    Draw the daily mean temperature and the daily mean humidity
    (`usecols=2`) in one Figure, one above the other, sharing the time
    axis. What do the two curves do at the same time of year?

??? success "Answer"
    `plt.subplots(2, 1, sharex=True)` makes two Axes in one column with one
    x-axis.

    ```python
    hum = np.loadtxt(path, delimiter=",", skiprows=1, usecols=2)
    hum_means = hum.reshape(3653, 24).mean(axis=1)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
    ax1.plot(dates[ok], day_means[ok], linewidth=0.6)
    ax1.set_ylabel("Temperature (°C)")
    ax2.plot(dates, hum_means, linewidth=0.6, color="tab:green")
    ax2.set_ylabel("Humidity (%)")
    ax1.set_title("Humid when cold, dry when warm")
    fig.savefig(OUT / "temp_and_humidity.png", dpi=150)
    ```

    The humidity peaks every winter, when the temperature is lowest: the
    two curves move against each other.

!!! question "Advanced task: humidity against temperature"
    Plot every valid hour as a point, temperature across and humidity up,
    and put the correlation coefficient `np.corrcoef(x, y)[0, 1]` in the
    title. 87 552 points cover each other: what makes the dense part
    visible?

??? success "Answer"
    Tiny, almost transparent points: `s=1` is their size, `alpha=0.05`
    their opacity, so only places with many points look dark.

    ```python
    r = np.corrcoef(temp[valid], hum[valid])[0, 1]
    print(f"r = {r:.2f}")
    fig, ax = plt.subplots()
    ax.scatter(temp[valid], hum[valid], s=1, alpha=0.05)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Humidity (%)")
    ax.set_title(f"87 552 hours: r = {r:.2f}")
    fig.savefig(OUT / "humidity_vs_temp.png", dpi=150)
    ```

    ```text
    $ python scripts/figures.py
    ...
    r = -0.70
    ```

    A falling cloud: below 0 °C most hours are above 80 %, above 25 °C
    most lie between 45 and 65 %. The humidity is a whole number, so the
    points stand in rows.

!!! question "Advanced task: a fitted line on the yearly means"
    Add a straight line fitted with `np.polyfit` to the ten yearly means of
    section 8, with its slope in the legend. Does the line say "colder"?

??? success "Answer"
    ```python
    slope, intercept = np.polyfit(list(years), year_means, 1)
    fig, ax = plt.subplots()
    ax.plot(years, year_means, "o", label="yearly mean")
    fit = [slope * y + intercept for y in years]
    ax.plot(years, fit, label=f"line: {slope:+.3f} °C per year")
    ax.set_xticks(years)
    ax.set_ylim(5, 9)
    ax.legend()
    fig.savefig(OUT / "yearly_trend.png", dpi=150)
    print(f"slope {slope:+.3f} °C per year")
    ```

    ```text
    $ python scripts/figures.py
    ...
    slope -0.056 °C per year
    ```

    The line falls by half a degree over the decade, but the points
    scatter around it by more than that: 2023 at 8.31 and 2025 at 5.98. A
    line through ten noisy points is not yet a trend.

!!! question "Advanced task: PNG, SVG or PDF?"
    Save the figure of section 5 also as `.svg` and `.pdf` (the format
    follows the file name). Compare the three sizes, and open each:
    which stays sharp when you zoom in?

??? success "Answer"
    Under `fig.savefig(OUT / "daily_temp.png", dpi=150)` of section 5:

    ```python
    for ext in ["svg", "pdf"]:
        fig.savefig(OUT / f"daily_temp.{ext}")
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

    macOS pads the numbers differently. PNG is pixels: zoomed in, the line
    turns into steps. SVG and PDF store the line itself and stay sharp at
    any size, for a report or a poster; PNG is for a web page or a slide.

---

## Aims practised

- ♻️ **Reproducibility:** one script draws every figure from the raw data;
  `environment.yml` lists the package it needs, with its version.
- 📁 **Files:** the figures are made files in the ignored `results/`; the
  script is what goes into the history.
- ⚙️ **Automation:** five figures in one run, again after every change.
