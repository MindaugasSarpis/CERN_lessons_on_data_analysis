# Seminar 7 · Visualisation

**Paired lecture:** 07 Data Visualisation · **Format:** type-along tutorial, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** How do twelve numbers become a figure, and how does the same script draw another file?

**Today's goal:** every student builds one script, `plot.py`, one step at a
time, in a new, empty folder: it draws a list on the screen, saves the
figure, labels and annotates it, reads its values from a CSV file typed in
class, and at the end takes the file and the labels from the command line.

Everything is typed in VS Code: the script in the editor, the commands in
its terminal (zsh on macOS, Git Bash on Windows; the lines are the same in
both). In the blocks, a line that starts with `$` is typed in the terminal,
without the `$`; every other line is what comes back; `...` stands for lines
left out. In a script, the new lines are marked.

**If time runs short:** leave out Part 7 (the open data set) first, then the
Tasks; Parts 1 to 6 are the session.

??? info "Before the session"
    - **Room:** Miniforge and VS Code with its Python extension on every
      laptop (the [Setup](../setup.md) page), internet for conda: Python
      about 25 MB on a Mac and 37 MB on Windows, Matplotlib with what it
      needs about 55 MB more on a Mac and 160 MB on Windows, less when conda
      has them already. Nothing from earlier seminars is needed.
    - **No file is handed out.** The data is typed from this page; the
      course stores no data file for today. Part 7 downloads one public
      file of 5 kB.
    - **Missing a tool?** VS Code: [Setup, step 1](../setup.md#vscode);
      `conda` (Miniforge): [Setup, steps 2–4](../setup.md#shell); the Python
      extension: [Setup, step 7](../setup.md#extensions).
    - **A laptop that already has `s07` or `weather-s07`:** remove the
      environment (`conda env remove -n s07`) and rename the old folder, to
      start empty with the room.
    - **The numbers:** the twelve values are the mean temperature of each
      month at the course's weather station, 2016 to 2025, in °C; the ten
      values of section 17 are the means of its years. The mean of the
      twelve values is 7.125 (of all hours 7.16: the months differ in
      length).
    - **Keys** are written for Windows, macOS in brackets. Paths are shown
      for a Mac (`/Users/smilte/...`); Git Bash shows `/c/Users/smilte/...`.

---

## Part 1 · One script, one list, one figure on the screen { #part-1 }

<!-- 0:00 to 0:31 -->

A folder, an environment with Matplotlib, and a script of ten lines that draws twelve numbers.

---

### 1. A new folder and an environment { #start }

<!-- 0:00 · 8 min -->

An environment is a folder with its own Python and its own packages; today's is named `s07`.

1. In VS Code, **View** > **Terminal**. Make the folder and go into it.

    ```text
    $ mkdir ~/weather-s07
    $ cd ~/weather-s07
    $ pwd
    /Users/smilte/weather-s07
    ```

2. **File** > **Open Folder...** > `weather-s07` (in your home folder) >
   **Open**, then **View** > **Terminal**. The Explorer on the left is empty.

3. Make the environment, with Python in it. At `Proceed ([y]/n)?` press `Enter`.

    ```text
    $ conda create -n s07 python=3.14
    ...
      added / updated specs:
        - python=3.14
    ...
    Proceed ([y]/n)?
    ...
    #     $ conda activate s07
    ```

    `conda: command not found`: install Miniforge as on the
    [Setup page, steps 2–4](../setup.md#shell), then open a new terminal.

4. Switch it on, and ask which Python answers.

    ```text
    $ conda activate s07
    $ python --version
    Python 3.14.10
    ```

**Check:** `(s07)` at the start of the prompt, and a Python `3.14` (the last number may be higher).

---

### 2. Install Matplotlib, write it down { #install }

<!-- 0:08 · 6 min -->

Matplotlib is the Python library that draws figures. A new package goes into the active environment, and into the file that lists it.

1. Matplotlib is not in it yet.

    ```text
    $ python -c "import matplotlib"
    Traceback (most recent call last):
    ...
    ModuleNotFoundError: No module named 'matplotlib'
    ```

2. Install it, with its version. At `Proceed ([y]/n)?` press `Enter`.

    ```text
    $ conda install matplotlib-base=3.11
    ...
    ## Package Plan ##

      environment location: /Users/smilte/miniforge3/envs/s07

      added / updated specs:
        - matplotlib-base=3.11
    ...
    Proceed ([y]/n)?
    ```

    `matplotlib-base` is Matplotlib without an extra window library of
    several hundred MB.

3. Ask for the version.

    ```text
    $ python -c "import matplotlib; print(matplotlib.__version__)"
    3.11.2
    ```

4. Write the environment into a file.

    ```text
    $ conda env export --from-history -f environment.yml
    ```

5. Click `environment.yml` in the Explorer, delete its last line,
   `prefix: ...` (a folder on this laptop), save (`Ctrl+S`, macOS `Cmd+S`).

    ```text
    name: s07
    channels:
      - conda-forge
    dependencies:
      - python=3.14
      - matplotlib-base=3.11
    ```

**Check:** `3.11.2` (the last digit may be higher), and `- matplotlib-base=3.11` at the end of
`environment.yml`.

---

### 3. One script with one list { #list }

<!-- 0:14 · 5 min -->

A list is values in square brackets, in order. These twelve are the mean temperature of each month, January to December, in °C.

1. In the Explorer, right-click > **New File...**, type `plot.py`, `Enter`.
   Type the four lines and save (`Ctrl+S`, macOS `Cmd+S`).

    ```python
    temps = [-3.9, -2.4, 1.2, 6.4, 12.2, 17.2,
             18.5, 16.1, 13.0, 6.9, 2.6, -2.3]
    print(temps)
    print(len(temps))
    ```

2. Run it.

    ```text
    $ python plot.py
    [-3.9, -2.4, 1.2, 6.4, 12.2, 17.2, 18.5, 16.1, 13.0, 6.9, 2.6, -2.3]
    12
    ```

    `len` counts the values of a list. Inside the brackets a list may go on
    in the next line.

3. Tell VS Code which Python to use: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`),
   `Python: Select Interpreter`, pick the entry with `envs/s07` in its path.
   The Status Bar shows `s07`.

**Check:** the second line says `12`.

---

### 4. Plot the list on the screen { #screen }

<!-- 0:19 · 6 min -->

Four lines draw a list: get Matplotlib, make a figure, draw the line, show the window.

1. Replace the two `print` lines. The script is now:

    ```python hl_lines="1 6 7 8"
    import matplotlib.pyplot as plt

    temps = [-3.9, -2.4, 1.2, 6.4, 12.2, 17.2,
             18.5, 16.1, 13.0, 6.9, 2.6, -2.3]

    fig, ax = plt.subplots()
    ax.plot(temps)
    plt.show()
    ```

    - `import matplotlib.pyplot as plt`: Matplotlib's plotting part, under the short name `plt`.
    - `fig, ax = plt.subplots()`: a figure `fig` (the whole picture) and its axes `ax` (the plot in it).
    - `ax.plot(temps)`: the values as a line, at the positions 0, 1, ..., 11.
    - `plt.show()`: opens the window; the script waits here until the window is closed.

2. Save and run. A window opens.

    ```text
    $ python plot.py
    ```

    The first run on a laptop may print `Matplotlib is building the font
    cache; this may take a moment.`

3. Close the window: the prompt comes back.

**Check:** a window with one line that rises to 18.5 and falls again; the x-axis counts the positions, 0 to 11 (ticks at 0, 2, ..., 10).

!!! warning "No window, or an error"
    - `ModuleNotFoundError: No module named 'matplotlib'`: the prompt says
      `(base)`. Type `conda activate s07`.
    - `UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be
      shown`: this Python cannot open a window. Go on: section 7 saves the
      figure into a file that VS Code opens.
    - No window and no new prompt: the window is open behind VS Code. Look
      for a new icon in the Dock (macOS) or on the taskbar (Windows).

---

### 5. Month names on the x-axis { #months }

<!-- 0:25 · 3 min -->

`ax.plot(x, y)` takes two lists of the same length: where each value stands, and the value.

1. Add the list `months` and give it to `ax.plot`.

    ```python hl_lines="3 4 9"
    import matplotlib.pyplot as plt

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    temps = [-3.9, -2.4, 1.2, 6.4, 12.2, 17.2,
             18.5, 16.1, 13.0, 6.9, 2.6, -2.3]

    fig, ax = plt.subplots()
    ax.plot(months, temps)
    plt.show()
    ```

2. Save, run, look, close the window.

    ```text
    $ python plot.py
    ```

**Check:** the x-axis reads `Jan` to `Dec`; the highest point stands over `Jul`.

---

### 6. A marker at every value { #markers }

<!-- 0:28 · 3 min -->

Only the twelve points are data; the line between them is drawn to guide the eye. `"o-"` means a circle at every value and a line between them.

1. Add `"o-"` to `ax.plot`.

    ```python hl_lines="2"
    fig, ax = plt.subplots()
    ax.plot(months, temps, "o-")
    plt.show()
    ```

2. Save, run, look, close the window.

**Check:** twelve circles, joined by a line.

!!! question "Task: only the markers"
    Change `"o-"` to `"o"`, run, look, and change it back.

??? success "Answer"
    Twelve circles and no line: `o` is the marker, `-` the line.

---

## Part 2 · Save the figure, label its axes { #part-2 }

<!-- 0:31 to 0:46 -->

The figure goes into a file, then gets one label at a time.

---

### 7. Save the figure: PNG, then SVG { #save }

<!-- 0:31 · 7 min -->

The window is gone when it is closed. `fig.savefig` writes the figure into a file; the ending of the name chooses the format.

1. Add one line above `plt.show()`.

    ```python hl_lines="3"
    fig, ax = plt.subplots()
    ax.plot(months, temps, "o-")
    fig.savefig("month_means.png", dpi=150)
    plt.show()
    ```

    `dpi=150`: 150 pixels per inch; the figure of 6.4 × 4.8 inches becomes 960 × 720 pixels.

2. Save, run, close the window, list the folder.

    ```text
    $ python plot.py
    $ ls
    environment.yml  month_means.png  plot.py
    ```

3. Click `month_means.png` in the Explorer: the figure opens in a tab.

4. Add a second line, with the ending `.svg`, and run again.

    ```python hl_lines="2"
    fig.savefig("month_means.png", dpi=150)
    fig.savefig("month_means.svg")
    plt.show()
    ```

    ```text
    $ python plot.py
    $ ls
    environment.yml  month_means.png  month_means.svg  plot.py
    ```

    PNG stores pixels: zoomed in, the line turns into steps. SVG stores the
    lines and the text themselves: sharp at every size, for a report or a
    slide.

The two lines stand above `plt.show()`: the script waits at `plt.show()`, so the files are written before the window opens.

**Check:** `ls` shows `month_means.png` and `month_means.svg`; the PNG opens in VS Code.

---

### 8. The y label, with its unit { #ylabel }

<!-- 0:38 · 3 min -->

A number on an axis needs to say what was measured, and in which unit.

1. Add one line under `ax.plot`.

    ```python hl_lines="3"
    fig, ax = plt.subplots()
    ax.plot(months, temps, "o-")
    ax.set_ylabel("Mean temperature (°C)")
    fig.savefig("month_means.png", dpi=150)
    fig.savefig("month_means.svg")
    plt.show()
    ```

    No `°` on your keyboard: copy it from this page.

2. Save, run, look, close the window.

**Check:** `Mean temperature (°C)` stands along the y-axis.

---

### 9. The x label { #xlabel }

<!-- 0:41 · 2 min -->

The same for the other axis.

1. Add one line above the y label.

    ```python hl_lines="2"
    ax.plot(months, temps, "o-")
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean temperature (°C)")
    ```

2. Save, run, look, close the window.

**Check:** `Month` stands under the x-axis.

---

### 10. A title that states the finding { #title }

<!-- 0:43 · 3 min -->

The axes already say what is plotted. The title says what the reader should see.

1. Add one line under the y label.

    ```python hl_lines="3"
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean temperature (°C)")
    ax.set_title("July is the warmest month, January the coldest")
    fig.savefig("month_means.png", dpi=150)
    ```

2. Save, run, look, close the window. Click `month_means.png`: the file has the labels and the title too.

**Check:** the title stands above the plot, in the window and in the PNG file.

!!! question "Task: the limits of the y-axis"
    Matplotlib chose a y-axis from about −5 to 20. Make it run from −10 to
    25 with `ax.set_ylim`, look, and delete the line again.

??? success "Answer"
    Under the title line:

    ```python
    ax.set_ylim(-10, 25)
    ```

    The same line with more empty space above and below it. Matplotlib's
    own limits fit these values, so the line goes again.

---

## Part 3 · Annotate: a reference line and an arrow { #part-3 }

<!-- 0:46 to 0:57 -->

Two marks that guide the reader: the mean as a line, the warmest month with an arrow.

---

### 11. A line at the mean, with a legend { #mean }

<!-- 0:46 · 5 min -->

A reference line gives every point something to be compared with. The script computes the mean from the list.

1. Add the four marked lines. The script is now:

    ```python hl_lines="7 8 12 16"
    import matplotlib.pyplot as plt

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    temps = [-3.9, -2.4, 1.2, 6.4, 12.2, 17.2,
             18.5, 16.1, 13.0, 6.9, 2.6, -2.3]
    mean = sum(temps) / len(temps)
    print(mean)

    fig, ax = plt.subplots()
    ax.plot(months, temps, "o-")
    ax.axhline(mean, color="grey", label=f"mean: {mean:.1f}")
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean temperature (°C)")
    ax.set_title("July is the warmest month, January the coldest")
    ax.legend(frameon=False)
    fig.savefig("month_means.png", dpi=150)
    fig.savefig("month_means.svg")
    plt.show()
    ```

    - `sum(temps) / len(temps)`: the sum of the values divided by their number, the mean.
    - `ax.axhline(mean, ...)`: a horizontal line across the plot, at the height `mean`.
    - `label=f"mean: {mean:.1f}"`: the line's text in the legend; `{mean:.1f}` puts the value in, with one decimal.
    - `ax.legend(frameon=False)`: draws the legend, without a frame, where it covers the least of the drawing: here, the upper right corner.

2. Save, run, look, close the window.

    ```text
    $ python plot.py
    7.125
    ```

**Check:** the terminal says `7.125`; a grey line crosses the plot, and the legend says `mean: 7.1`.

---

### 12. An arrow to the warmest month { #annotate }

<!-- 0:51 · 6 min -->

An annotation is a text in the plot with an arrow to one point. The script finds the point itself.

1. Add the six marked lines.

    ```python hl_lines="9 10 15 16 17 18"
    import matplotlib.pyplot as plt

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    temps = [-3.9, -2.4, 1.2, 6.4, 12.2, 17.2,
             18.5, 16.1, 13.0, 6.9, 2.6, -2.3]
    mean = sum(temps) / len(temps)
    print(mean)
    top = temps.index(max(temps))
    print(top, months[top], temps[top])

    fig, ax = plt.subplots()
    ax.plot(months, temps, "o-")
    ax.axhline(mean, color="grey", label=f"mean: {mean:.1f}")
    ax.annotate(f"{months[top]}: {temps[top]}",
                xy=(months[top], temps[top]),
                xytext=(30, 0), textcoords="offset points",
                arrowprops={"arrowstyle": "->"})
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean temperature (°C)")
    ax.set_title("July is the warmest month, January the coldest")
    ax.legend(frameon=False)
    fig.savefig("month_means.png", dpi=150)
    fig.savefig("month_means.svg")
    plt.show()
    ```

    - `max(temps)`: the largest value; `temps.index(...)`: its position in the list, counted from 0.
    - `ax.annotate(text, xy=...)`: the text, and the point `xy` the arrow points to.
    - `xytext=(30, 0), textcoords="offset points"`: the text starts 30 points to the right of that point.
    - `arrowprops={"arrowstyle": "->"}`: draw an arrow from the text to the point.

2. Save, run, look, close the window.

    ```text
    $ python plot.py
    7.125
    6 Jul 18.5
    ```

**Check:** the terminal says `6 Jul 18.5`; in the figure, `Jul: 18.5` stands to the right of the highest point, with an arrow to it.

!!! question "Task: the coldest month"
    Add two lines that print the position, the name and the value of the
    coldest month. Run, then delete them again.

??? success "Answer"
    ```python
    low = temps.index(min(temps))
    print(low, months[low], temps[low])
    ```

    ```text
    0 Jan -3.9
    ```

---

## Part 4 · The list moves to a CSV file { #part-4 }

<!-- 0:57 to 1:11 -->

Values in a script can only be changed by editing the script. In a file of their own, any program can read them.

---

### 13. Type the values into a CSV file { #csv }

<!-- 0:57 · 6 min -->

A CSV file is text: one row per line, the columns separated by commas, the names of the columns in the first line.

1. In the Explorer, right-click > **New File...**, type `month_means.csv`,
   `Enter`. Type the 13 lines, press `Enter` once after the last, and save
   (`Ctrl+S`, macOS `Cmd+S`).

    ```text
    month,temp_c
    Jan,-3.9
    Feb,-2.4
    Mar,1.2
    Apr,6.4
    May,12.2
    Jun,17.2
    Jul,18.5
    Aug,16.1
    Sep,13.0
    Oct,6.9
    Nov,2.6
    Dec,-2.3
    ```

2. Look at the file in the terminal.

    ```text
    $ cat month_means.csv
    month,temp_c
    Jan,-3.9
    ...
    Dec,-2.3
    ```

3. Count its lines.

    ```text
    $ wc -l month_means.csv
    13 month_means.csv
    ```

    `wc -l` counts the line ends: `12` if `Enter` was not pressed after the
    last row, which reads the same. macOS puts spaces before the number.

**Check:** `cat` shows the names of the two columns and twelve rows, with no empty line between them.

---

### 14. Read the CSV file in the script { #read }

<!-- 1:03 · 8 min -->

Seven lines build the same two lists from the file. The typed lists are deleted.

1. Replace the four lines of `months` and `temps` by the seven marked lines. The rest stays.

    ```python hl_lines="3 4 5 6 7 8 9"
    import matplotlib.pyplot as plt

    lines = open("month_means.csv").read().splitlines()
    months = []
    temps = []
    for line in lines[1:]:
        parts = line.split(",")
        months.append(parts[0])
        temps.append(float(parts[1]))
    mean = sum(temps) / len(temps)
    print(mean)
    ...
    ```

    - `open("month_means.csv").read()`: the whole file as one text; `.splitlines()`: a list with one text per line.
    - `lines[1:]`: every line after the first, which holds the names of the columns.
    - `line.split(",")`: `"Jul,18.5"` becomes `["Jul", "18.5"]`.
    - `float("18.5")`: the text becomes the number 18.5; `append` puts it at the end of the list.

2. Save, run, look, close the window.

    ```text
    $ python plot.py
    7.125
    6 Jul 18.5
    ```

**Check:** the same two lines and the same figure as in section 12; the script holds no temperature any more.

!!! warning "`IndexError: list index out of range`"
    ```text
    Traceback (most recent call last):
      File "/Users/smilte/weather-s07/plot.py", line 9, in <module>
        temps.append(float(parts[1]))
                           ~~~~~^^^
    IndexError: list index out of range
    ```

    An empty line in `month_means.csv`, at its end or between the rows.
    Delete it and save.

!!! question "Task: the figure follows the file"
    In `month_means.csv`, change July's `18.5` to `28.5`. Save, run, look.
    Then change it back and run again.

??? success "Answer"
    ```text
    $ python plot.py
    7.958333333333333
    6 Jul 28.5
    ```

    The point, the arrow's text and the mean line have moved; the script
    was not touched.

---

## Part 5 · One function, different files { #part-5 }

<!-- 1:11 to 1:31 -->

A function is a named piece of the script that runs when it is called, with the values given in the call.

---

### 15. The reading becomes a function { #read-function }

<!-- 1:11 · 5 min -->

The seven lines that read the file get a name, `read_csv`, and the file's name becomes its parameter `path`.

1. Change the top of the script. The rest stays.

    ```python hl_lines="4 5 6 7 8 9 10 11 12 13 16"
    import matplotlib.pyplot as plt


    def read_csv(path):
        """The labels and the values of a CSV file with two columns."""
        lines = open(path).read().splitlines()
        labels = []
        values = []
        for line in lines[1:]:
            parts = line.split(",")
            labels.append(parts[0])
            values.append(float(parts[1]))
        return labels, values


    months, temps = read_csv("month_means.csv")
    mean = sum(temps) / len(temps)
    print(mean)
    ...
    ```

    - `def read_csv(path):`: the indented lines under it run when `read_csv(...)` is called; `path` is the text given in the call.
    - The line in `"""` says what the function gives back.
    - `labels`, `values`: inside the function the names are general, because the file need not hold months.
    - `return labels, values`: hands the two lists back; `months, temps = ...` takes them.

2. Save, run, look, close the window.

    ```text
    $ python plot.py
    7.125
    6 Jul 18.5
    ```

**Check:** the same two lines and the same figure.

---

### 16. The drawing becomes a function { #draw-function }

<!-- 1:16 · 6 min -->

Everything under `read_csv` moves into a second function, `draw(path, out)`: the file to read and the file to write.

1. Select the lines from `months, temps = ...` to `fig.savefig(...)` and
   press `Tab`: they move four spaces to the right. Then change them to the
   lines below: `labels` and `values` for `months` and `temps`, one `print`,
   `out` in `savefig`. The SVG line and `plt.show()` are deleted: the script
   writes a file and stops.

    ```python hl_lines="16 17 18 19 20 21 24 26 27 34 37"
    import matplotlib.pyplot as plt


    def read_csv(path):
        """The labels and the values of a CSV file with two columns."""
        lines = open(path).read().splitlines()
        labels = []
        values = []
        for line in lines[1:]:
            parts = line.split(",")
            labels.append(parts[0])
            values.append(float(parts[1]))
        return labels, values


    def draw(path, out):
        """Draw the values of a CSV file into the file out."""
        labels, values = read_csv(path)
        mean = sum(values) / len(values)
        top = values.index(max(values))
        print(path, len(values), labels[top], values[top])

        fig, ax = plt.subplots()
        ax.plot(labels, values, "o-")
        ax.axhline(mean, color="grey", label=f"mean: {mean:.1f}")
        ax.annotate(f"{labels[top]}: {values[top]}",
                    xy=(labels[top], values[top]),
                    xytext=(30, 0), textcoords="offset points",
                    arrowprops={"arrowstyle": "->"})
        ax.set_xlabel("Month")
        ax.set_ylabel("Mean temperature (°C)")
        ax.set_title("July is the warmest month, January the coldest")
        ax.legend(frameon=False)
        fig.savefig(out, dpi=150)


    draw("month_means.csv", "month_means.png")
    ```

2. Save and run. No window opens; the script prints one line: the file, the number of values, the largest one.

    ```text
    $ python plot.py
    month_means.csv 12 Jul 18.5
    ```

3. Click `month_means.png` in the Explorer.

**Check:** one line in the terminal; `month_means.png` is the same figure as before.

---

### 17. A second file, the same function { #second-file }

<!-- 1:22 · 4 min -->

The function is worth its name when it is called twice. The second file holds the mean temperature of each year.

1. In the Explorer, **New File...**, `year_means.csv`. Type the 11 lines,
   press `Enter` once after the last, and save.

    ```text
    year,temp_c
    2016,7.60
    2017,6.51
    2018,7.97
    2019,7.27
    2020,6.83
    2021,7.25
    2022,6.60
    2023,8.31
    2024,7.27
    2025,5.98
    ```

2. Add a second call at the end of `plot.py`.

    ```python hl_lines="2"
    draw("month_means.csv", "month_means.png")
    draw("year_means.csv", "year_means.png")
    ```

3. Save and run.

    ```text
    $ python plot.py
    month_means.csv 12 Jul 18.5
    year_means.csv 10 2023 8.31
    ```

4. Click `year_means.png`: ten points, the mean line, the arrow at 2023.

**Check:** two lines in the terminal, two PNG files. The figure of the years says `Month` under its axis and has the title about July: both are wrong.

---

### 18. What differs becomes a parameter { #parameters }

<!-- 1:26 · 5 min -->

Whatever differs between two calls leaves the function and is given in the call: first the x label, then the title.

1. The x label: three changes.

    ```python
    def draw(path, out, xlabel):
    ```

    ```python
        ax.set_xlabel(xlabel)
    ```

    ```python
    draw("month_means.csv", "month_means.png", "Month")
    draw("year_means.csv", "year_means.png", "Year")
    ```

2. Save, run, click `year_means.png`: `Year` under the axis, still the title about July.

    ```text
    $ python plot.py
    month_means.csv 12 Jul 18.5
    year_means.csv 10 2023 8.31
    ```

3. The title, in the same three places.

    ```python
    def draw(path, out, xlabel, title):
    ```

    ```python
        ax.set_title(title)
    ```

    ```python
    draw("month_means.csv", "month_means.png", "Month",
         "July is the warmest month, January the coldest")
    draw("year_means.csv", "year_means.png", "Year",
         "2023 was the warmest year, 2025 the coldest")
    ```

4. Save, run, click `year_means.png`.

    ```text
    $ python plot.py
    month_means.csv 12 Jul 18.5
    year_means.csv 10 2023 8.31
    ```

**Check:** `year_means.png` has `Year` under its axis and its own title; `month_means.png` has not changed.

!!! question "Task: the yearly figure as SVG"
    Add a third call that writes the figure of the years into
    `year_means.svg`. What has to change in the function?

??? success "Answer"
    Nothing: the ending of `out` chooses the format.

    ```python
    draw("year_means.csv", "year_means.svg", "Year",
         "2023 was the warmest year, 2025 the coldest")
    ```

    ```text
    $ python plot.py
    month_means.csv 12 Jul 18.5
    year_means.csv 10 2023 8.31
    year_means.csv 10 2023 8.31
    ```

---

## Part 6 · Parameters from the command line { #part-6 }

<!-- 1:31 to 1:45 -->

The file and the labels move out of the script, into the line that runs it.

---

### 19. What the script receives: `sys.argv` { #argv }

<!-- 1:31 · 4 min -->

`sys.argv` is the list of the words typed after `python`: the script's name, then the arguments, each one a text.

1. Add `import sys` as the first line and `print(sys.argv)` as the last.

    ```python hl_lines="1"
    import sys

    import matplotlib.pyplot as plt
    ```

    ```python hl_lines="5"
    draw("month_means.csv", "month_means.png", "Month",
         "July is the warmest month, January the coldest")
    draw("year_means.csv", "year_means.png", "Year",
         "2023 was the warmest year, 2025 the coldest")
    print(sys.argv)
    ```

2. Save and run, three times: with no argument, with two, with four.

    ```text
    $ python plot.py
    month_means.csv 12 Jul 18.5
    year_means.csv 10 2023 8.31
    ['plot.py']
    $ python plot.py month_means.csv month_means.png
    month_means.csv 12 Jul 18.5
    year_means.csv 10 2023 8.31
    ['plot.py', 'month_means.csv', 'month_means.png']
    $ python plot.py month_means.csv month_means.png Month "July is the warmest month, January the coldest"
    month_means.csv 12 Jul 18.5
    year_means.csv 10 2023 8.31
    ['plot.py', 'month_means.csv', 'month_means.png', 'Month', 'July is the warmest month, January the coldest']
    ```

    A space separates two arguments. Quotes keep a text with spaces
    together as one argument.

**Check:** the last run prints a list of five texts; the title is one of them.

---

### 20. The file, the output and the labels from the command line { #cli }

<!-- 1:35 · 6 min -->

`sys.argv[1]` is the first argument, `sys.argv[2]` the second, and so on. They go straight into `draw`.

1. Replace the two calls and the `print` by one line.

    ```python
    draw(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    ```

2. Save. Draw the months, then the years, with the same script.

    ```text
    $ python plot.py month_means.csv month_means.png Month "July is the warmest month, January the coldest"
    month_means.csv 12 Jul 18.5
    $ python plot.py year_means.csv year_means.png Year "2023 was the warmest year, 2025 the coldest"
    year_means.csv 10 2023 8.31
    ```

    The `Up` key brings the last command back, to change a word in it.

**Check:** both figures are drawn again; the script names no file, no label and no title.

---

### 21. A message when an argument is missing { #usage }

<!-- 1:41 · 4 min -->

A script that takes arguments says which ones, when they are missing.

1. Run the script without arguments.

    ```text
    $ python plot.py
    Traceback (most recent call last):
      File "/Users/smilte/weather-s07/plot.py", line 39, in <module>
        draw(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
             ~~~~~~~~^^^
    IndexError: list index out of range
    ```

    The list holds only `'plot.py'`: there is no `sys.argv[1]`.

2. Add two lines above the call.

    ```python hl_lines="1 2"
    if len(sys.argv) != 5:
        sys.exit("usage: python plot.py FILE OUT XLABEL TITLE")
    draw(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    ```

    - `len(sys.argv) != 5`: the script's name and four arguments make five; `!=` means "is not equal to".
    - `sys.exit("...")`: prints the text and stops the script.

3. Save and run without arguments.

    ```text
    $ python plot.py
    usage: python plot.py FILE OUT XLABEL TITLE
    ```

**Check:** one line that says what to type, and no traceback.

!!! question "Task: an SVG file without opening the script"
    Write the figure of the months into `month_means.svg`, from the
    command line.

??? success "Answer"
    ```text
    $ python plot.py month_means.csv month_means.svg Month "July is the warmest month, January the coldest"
    month_means.csv 12 Jul 18.5
    ```

---

## Part 7 · An open data set { #part-7 }

<!-- 1:45 to 1:58 -->

The same script on a file that someone else wrote: 240 values, three columns, another unit.

---

### 22. Download one public file { #open-data }

<!-- 1:45 · 4 min -->

The file is the mean air temperature of each month at Nottingham Castle, 1920 to 1939, in °F: the data set `nottem`, distributed with R in its `datasets` package (source: O. D. Anderson, *Time Series Analysis and Forecasting*, 1976; R's licence: GPL-2 or GPL-3), as a CSV file in the public Rdatasets collection. The course keeps no copy of it.

1. Download it into the folder. `curl` prints a small table of its progress.

    ```text
    $ curl -O https://vincentarelbundock.github.io/Rdatasets/csv/datasets/nottem.csv
    ```

    `curl -O` saves what is at the address into a file of the same name, `nottem.csv`.

2. Look at its first lines, and count them all.

    ```text
    $ head -4 nottem.csv
    rownames,time,value
    1,1920,40.6
    2,1920.08333333333,40.8
    3,1920.16666666667,44.4
    $ wc -l nottem.csv
    241 nottem.csv
    ```

    Three columns: the number of the row, the time as a year with a
    fraction (`1920.0833` is February 1920), the temperature.

**Check:** `wc -l` says 241: the names of the columns and 240 months.

---

### 23. Read the last two columns { #last-columns }

<!-- 1:49 · 4 min -->

`read_csv` takes the first two columns. Here the label and the value are the last two.

1. Run the script on the new file as it is.

    ```text
    $ python plot.py nottem.csv nottem.png Year "Nottingham, 1920 to 1939"
    nottem.csv 240 240 1939.91666666667
    ```

    It has drawn the time against the number of the row: `nottem.png` is a straight line.

2. In `read_csv`, count the columns from the end.

    ```python hl_lines="2 8 9"
    def read_csv(path):
        """The labels and the values: the last two columns of a CSV file."""
        lines = open(path).read().splitlines()
        labels = []
        values = []
        for line in lines[1:]:
            parts = line.split(",")
            labels.append(parts[-2])
            values.append(float(parts[-1]))
        return labels, values
    ```

    `parts[-1]` is the last text of the list, `parts[-2]` the one before
    it. In a file with two columns these are the same two as before.

3. Save and run again. Click `nottem.png`.

    ```text
    $ python plot.py nottem.csv nottem.png Year "Nottingham, 1920 to 1939"
    nottem.csv 240 1934.5 66.5
    ```

**Check:** the line ends in `1934.5 66.5` (July 1934, 66.5 °F); the figure shows twenty yearly waves. Under the x-axis the 240 labels lie on top of each other, and the y label says °C.

---

### 24. One tick label in every 24 { #ticks }

<!-- 1:53 · 2 min -->

240 labels do not fit under one axis; about ten do.

1. Add two lines in `draw`, above `ax.set_xlabel`.

    ```python hl_lines="1 2"
        step = max(1, len(labels) // 10)
        ax.set_xticks(labels[::step])
        ax.set_xlabel(xlabel)
    ```

    - `len(labels) // 10`: division without the remainder: 240 gives 24, 12 gives 1; `max(1, ...)` keeps it at 1 or more.
    - `labels[::step]`: every 24th label; `ax.set_xticks(...)` puts tick marks and labels only there.

2. Save, run, click `nottem.png`.

    ```text
    $ python plot.py nottem.csv nottem.png Year "Nottingham, 1920 to 1939"
    nottem.csv 240 1934.5 66.5
    ```

**Check:** the x-axis reads `1920`, `1922`, ..., `1938`.

---

### 25. The y label becomes the fifth argument { #ylabel-argument }

<!-- 1:55 · 3 min -->

The unit differs between the files, so the y label leaves the function too.

1. Change five lines: `ylabel` in `def draw` and in `ax.set_ylabel`, and the last three lines. This is the whole script:

    ```python hl_lines="18 35 41 42 43"
    import sys

    import matplotlib.pyplot as plt


    def read_csv(path):
        """The labels and the values: the last two columns of a CSV file."""
        lines = open(path).read().splitlines()
        labels = []
        values = []
        for line in lines[1:]:
            parts = line.split(",")
            labels.append(parts[-2])
            values.append(float(parts[-1]))
        return labels, values


    def draw(path, out, xlabel, ylabel, title):
        """Draw the values of a CSV file into the file out."""
        labels, values = read_csv(path)
        mean = sum(values) / len(values)
        top = values.index(max(values))
        print(path, len(values), labels[top], values[top])

        fig, ax = plt.subplots()
        ax.plot(labels, values, "o-")
        ax.axhline(mean, color="grey", label=f"mean: {mean:.1f}")
        ax.annotate(f"{labels[top]}: {values[top]}",
                    xy=(labels[top], values[top]),
                    xytext=(30, 0), textcoords="offset points",
                    arrowprops={"arrowstyle": "->"})
        step = max(1, len(labels) // 10)
        ax.set_xticks(labels[::step])
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.legend(frameon=False)
        fig.savefig(out, dpi=150)


    if len(sys.argv) != 6:
        sys.exit("usage: python plot.py FILE OUT XLABEL YLABEL TITLE")
    draw(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    ```

2. Save. Draw the three files.

    ```text
    $ python plot.py nottem.csv nottem.png Year "Mean temperature (°F)" "Nottingham, 1920 to 1939"
    nottem.csv 240 1934.5 66.5
    $ python plot.py month_means.csv month_means.png Month "Mean temperature (°C)" "July is the warmest month, January the coldest"
    month_means.csv 12 Jul 18.5
    $ python plot.py year_means.csv year_means.png Year "Mean temperature (°C)" "2023 was the warmest year, 2025 the coldest"
    year_means.csv 10 2023 8.31
    ```

    If the `°` does not arrive in the figure, type `deg F` and `deg C`.

3. Run it without arguments.

    ```text
    $ python plot.py
    usage: python plot.py FILE OUT XLABEL YLABEL TITLE
    ```

**Check:** three PNG files from one script; `nottem.png` says °F on its y-axis, the other two °C.

---

### 26. Wrap up { #wrap-up }

<!-- 1:58 · 2 min -->

The script grew from four lines to 43, one step at a time.

| To | Type |
|---|---|
| make and switch on an environment | `conda create -n s07 python=3.14`, `conda activate s07` |
| write the environment down | `conda env export --from-history -f environment.yml` |
| draw two lists | `fig, ax = plt.subplots()`, `ax.plot(x, y, "o-")` |
| see the figure, save it | `plt.show()`, `fig.savefig("name.png", dpi=150)`, `fig.savefig("name.svg")` |
| label it | `ax.set_xlabel(...)`, `ax.set_ylabel(...)`, `ax.set_title(...)` |
| mark it | `ax.axhline(y, label=...)`, `ax.legend(frameon=False)`, `ax.annotate(text, xy=...)` |
| read a CSV file | `open(path).read().splitlines()`, `line.split(",")`, `float(...)` |
| reuse lines | `def draw(path, out, ...):` |
| take arguments | `sys.argv`, `sys.exit("usage: ...")` |

**Check:** the folder holds `plot.py`, `environment.yml`, two CSV files typed in class, one downloaded, and a figure of each.

---

## Aims practised

- ♻️ **Reproducibility:** the figure comes from a script and a data file, never from clicks;
  `environment.yml` lists the package it needs, with its version.
- ⚙️ **Automation:** one function draws every file of this form; one line in
  the terminal draws a figure again after the data changes.
- 🔧 **Tool-agnosticism:** the values are a plain CSV file and the figure a
  PNG or SVG file, which any program reads.
