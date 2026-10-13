# Seminar 8 — What Does a Year of Weather Look Like? Figures with Matplotlib

**Paired lecture:** 08 Data Visualisation · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student adds Matplotlib to the project's
environment and writes one script, `scripts/figures.py`, that draws five
figures of `weather.csv` into `results/`: ten years day by day, the year's
cycle, the day's cycle, the yearly means and a histogram; commits and
pushes the script.

Everything is typed in VS Code: the script in the editor, the commands in
its terminal (PowerShell 7, the same lines on macOS and Windows). Each
figure opens in VS Code from the Explorer.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · Matplotlib in the environment** · 30 min | | |
| 0:00 | [1. Install Matplotlib](#install) | `conda install matplotlib-base=3.11` | `3.11.2` |
| 0:10 | [2. Add it to `environment.yml`](#yml) | `conda env export --from-history -f environment.yml` | the change committed |
| 0:20 | [3. A first figure](#first) | `fig.savefig(OUT / "daily_temp.png")` | a spike down to −999 |
| | **Part 2 · Ten years, day by day** · 25 min | | |
| 0:30 | [4. Leave out the missing days](#mask) | `dates[ok], day_means[ok]` | ten summers, ten winters |
| 0:40 | [5. Size, label, a title that says the finding](#labels) | `ax.set_title(...)` | `daily_temp.png` finished |
| | **Part 3 · The year's cycle and the day's cycle** · 30 min | | |
| 0:55 | [6. One point per month](#monthly) | `ax.set_xticks(months, ...)` | `monthly_temp.png` |
| 1:10 | [7. Two lines and a legend](#daily-cycle) | `label="July"`, `ax.legend()` | `day_cycle.png` |
| | **Part 4 · Is it getting warmer, as a figure** · 35 min | | |
| 1:25 | [8. Ten points and a reference line](#yearly) | `ax.axhline(...)` | `yearly_temp.png` |
| 1:35 | [9. A histogram of the hours](#histogram) | `ax.hist(..., bins=...)` | `temp_hist.png` |
| 1:45 | [10. Commit and push the script](#commit) | `git push` | `figures.py` on GitHub |
| 1:55 | [11. Wrap up](#wrap-up) | | |
| | **Optional, if the room is fast** | | |
| — | [12. A heatmap of one year](#heatmap) | `ax.imshow(...)` | 2025 hour by hour |
| — | [13. One style for all figures](#style) | `plt.rcParams.update(...)` | five figures restyled |

**If time runs short:** stop after section 10; sections 12 and 13 are optional.

??? info "Before the session"
    - **Room:** the weather project as Seminar 7 left it, with
      `environment.yml` and the conda environment `weather`; internet for
      conda.
    - **You:** remove Matplotlib from your `weather` environment
      (`conda remove matplotlib-base`) to install it with the room.
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Windows prints `C:\Users\smilte\...`.

---

## Part 1 · Matplotlib in the environment { #part-1 }

**0:00 to 0:30**

---

### 1. Install Matplotlib { #install }

**0:00 · 10 min** · A new package goes into the project's environment, never into `base`.

1. Open `weather-project` in VS Code, then the terminal. Switch the
   environment on; the prompt starts with `(weather)`.

    ```text
    conda activate weather
    ```

2. Install Matplotlib, with its version.

    ```text
    conda install matplotlib-base=3.11
    ```

    ```text
    ## Package Plan ##

      environment location: /Users/smilte/miniforge3/envs/weather

      added / updated specs:
        - matplotlib-base=3.11
    ```

    `matplotlib-base` is Matplotlib without a window library of several
    hundred MB; the scripts write their figures to files.

3. At `Proceed ([y]/n)?` press `Enter`. Then ask for the version.

    ```text
    python -c "import matplotlib; print(matplotlib.__version__)"
    ```

    ```text
    3.11.2
    ```

**Check:** `3.11.2`, with `(weather)` in the prompt.

!!! warning "`ModuleNotFoundError: No module named 'matplotlib'`"
    The prompt says `(base)`: `conda activate weather`, then again. VS Code's
    Status Bar must show `weather` too (Seminar 7, section 2).

---

### 2. Add it to `environment.yml` { #yml }

**0:10 · 10 min** · The file must list what the scripts need, or the next laptop cannot run them.

1. Export again.

    ```text
    conda env export --from-history -f environment.yml
    ```

2. In `environment.yml`, delete the last line, `prefix: ...`, save.
3. The change.

    ```text
    git diff
    ```

    ```text
    @@ -4,3 +4,4 @@ channels:
     dependencies:
       - python=3.14
       - numpy=2.5
    +  - matplotlib-base=3.11
    ```

4. Commit.

    ```text
    git commit -am "Add Matplotlib to the environment"
    ```

    ```text
    [main 4b52d79] Add Matplotlib to the environment
     1 file changed, 1 insertion(+)
    ```

    Your id differs.

**Check:** `git status` ends with `working tree clean`.

---

### 3. A first figure { #first }

**0:20 · 10 min** · A Figure holds one Axes; `ax.plot` draws a line on it; `fig.savefig` writes the file.

1. New file `scripts/figures.py`. Type, save.

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

    fig, ax = plt.subplots()
    ax.plot(dates, day_means)
    fig.savefig(OUT / "daily_temp.png")
    ```

    The first lines are those of `coldest_day.py` from Seminar 7.

2. Run it. It prints nothing.

    ```text
    python scripts/figures.py
    ```

3. In the Explorer, click `results/daily_temp.png` (grey: Git ignores
   it). A wavy band near 0, and one line straight down to −1000 in 2019.

**Check:** the spike in 2019: the five days of `-999`.

!!! question "Task: the humidity, drawn the same way"
    In `figures.py`, change `usecols=1` to `usecols=2`, run, look at the
    figure. Is there a spike? When is the air most humid? Change it back.

??? note "Answer"
    No spike: `humidity_pct` has no `-999`. The band is highest in winter
    (the January mean is 86.8 %) and lowest in summer (71.8 % in July).

---

## Part 2 · Ten years, day by day { #part-2 }

**0:30 to 0:55** · One missing value can hide everything else in a figure.

---

### 4. Leave out the missing days { #mask }

**0:30 · 10 min** · The mask of Seminar 7, on the days and their dates together.

1. Under the `dates = ...` line, add one line.

    ```python
    ok = day_means != -999
    ```

2. Change the `ax.plot` line, save, run.

    ```python
    ax.plot(dates[ok], day_means[ok])
    ```

    ```text
    python scripts/figures.py
    ```

3. The figure in VS Code updates: ten summers and ten winters, the y-axis
   from about −15 to 30.

**Check:** no spike, and the same cycle each year.

---

### 5. Size, label, a title that says the finding { #labels }

**0:40 · 15 min** · A figure needs a unit on its axis and a title that says what to see.

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
    python scripts/figures.py
    ```

**Check:** a wide figure, a y-axis label with °C, the title on top.

!!! question "Task: 2025 alone"
    Draw only the days of 2025 into `results/daily_2025.png`. Hint: a
    second mask on `dates`, joined to `ok` with `&`.

??? note "Answer"
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

**0:55 to 1:25** · Averages over ten years show what the noise of single days hides.

---

### 6. One point per month { #monthly }

**0:55 · 15 min** · Twelve means, one for each month of all ten years, as points joined by a line.

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
    python scripts/figures.py
    ```

    ```text
    [-3.9 -2.4  1.2  6.4 12.2 17.2 18.5 16.1 13.   6.9  2.6 -2.3]
    ```

**Check:** a hill with its top in July, 18.5 °C, and its bottom in
January, −3.9 °C.

---

### 7. Two lines and a legend { #daily-cycle }

**1:10 · 15 min** · The mean of each hour of the day, for January and for July; a `label` on each line, `ax.legend()` lists them.

1. At the end of the file, add these lines, save, run.

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

    ```text
    python scripts/figures.py
    ```

    The new lines:

    ```text
    January -5.9 -1.8
    July 13.5 23.6
    ```

2. Open `results/day_cycle.png`: both lines are lowest at 03:00 and
   highest at 15:00.

**Check:** two lines, a legend with January and July.

!!! question "Task: spring and autumn"
    Add April and October to the figure. Which of the two days swings
    more?

??? note "Answer"
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

**1:25 to 2:00** · Seminar 7's ten yearly means, and the 87 552 hours behind them.

---

### 8. Ten points and a reference line { #yearly }

**1:25 · 10 min** · Points, not bars: the y-axis does not start at zero, and the eye compares the points with the line.

1. At the end of the file, add these lines, save, run.

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

    ```text
    python scripts/figures.py
    ```

2. Open `results/yearly_temp.png`. `"o"` draws points without a line;
   `axhline` the grey line at 7.16 °C.

**Check:** ten points above and below the line, the last one, 2025, lowest.

---

### 9. A histogram of the hours { #histogram }

**1:35 · 10 min** · `ax.hist` counts the values in bins; the bins are chosen from the smallest and largest value, −16.3 and 32.4.

1. At the end of the file, add these lines, save, run.

    ```python
    fig, ax = plt.subplots()
    ax.hist(temp[valid], bins=np.arange(-17, 34, 1))
    ax.set_xlabel("Hourly temperature (°C), bins of 1 °C")
    ax.set_ylabel("Hours")
    ax.set_title("Two humps: one near 0 °C, one near 12 °C")
    fig.savefig(OUT / "temp_hist.png", dpi=150)
    ```

    ```text
    python scripts/figures.py
    ```

2. Open `results/temp_hist.png`. The highest bar, −1 to 0 °C, holds
   3848 hours: the winter hours near freezing. The second hump, around 11
   to 12 °C, holds the rest of the year.

**Check:** two humps, bars of 1 °C from −17 to 34.

!!! question "Task: other bin widths"
    Draw the histogram with bins of 0.1 °C and of 10 °C. What does each
    show, and what does it hide?

??? note "Answer"
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

### 10. Commit and push the script { #commit }

**1:45 · 10 min** · The script goes into the history; the five figures do not, since it draws them again in a second.

1. What Git sees.

    ```text
    git status --short
    ```

    ```text
    ?? scripts/figures.py
    ```

2. Commit, push.

    ```text
    git add scripts/figures.py
    ```

    ```text
    git commit -m "Draw five figures of the weather data"
    ```

    ```text
    [main d6b8c07] Draw five figures of the weather data
     1 file changed, 68 insertions(+)
     create mode 100644 scripts/figures.py
    ```

    Your id and counts differ.

    ```text
    git push
    ```

3. Check that the script remakes every figure: delete the five `.png`
   files, run, list them.

    ```text
    Remove-Item results/*.png
    ```

    ```text
    python scripts/figures.py
    ```

    ```text
    [-3.9 -2.4  1.2  6.4 12.2 17.2 18.5 16.1 13.   6.9  2.6 -2.3]
    January -5.9 -1.8
    July 13.5 23.6
    ```

    ```text
    Get-ChildItem results -Name
    ```

    ```text
    daily_temp.png
    day_cycle.png
    monthly_temp.png
    temp_hist.png
    yearly_temp.png
    yearly_temp.txt
    ```

**Check:** on GitHub, `scripts/figures.py` and no `results` folder.

---

### 11. Wrap up { #wrap-up }

**1:55 · 5 min**

| To | Type |
|--|--|
| add a package | `conda activate weather`, `conda install NAME=VERSION` |
| write it down | `conda env export --from-history -f environment.yml`, delete `prefix:` |
| a figure | `fig, ax = plt.subplots()`, `ax.plot(x, y)`, `fig.savefig(PATH, dpi=150)` |
| points, a line, a legend | `ax.plot(x, y, "o")`, `ax.axhline(y)`, `label=...`, `ax.legend()` |
| labels | `ax.set_xlabel`, `ax.set_ylabel` with the unit, `ax.set_title` with the finding |
| a histogram | `ax.hist(values, bins=np.arange(start, stop, width))` |

Seminar 9 starts from this repository.

---

## Optional, if the room is fast { #optional }

---

### 12. A heatmap of one year { #heatmap }

**— · 10 min** · Colour as the third axis: the 365 days of 2025 across, the 24 hours up.

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

**— · 5 min** · Settings in `plt.rcParams` hold for every figure the script draws after them.

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

## Aims practised

- ♻️ **Reproducibility:** one script draws every figure from the raw data;
  `environment.yml` lists the package it needs, with its version.
- 📁 **Files:** the figures are made files in the ignored `results/`; the
  script is what goes into the history.
- ⚙️ **Automation:** five figures in one run, again after every change.
