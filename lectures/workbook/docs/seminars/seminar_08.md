# Seminar 8 — Two Figures with Matplotlib

**Paired lecture:** 08 Data Visualisation · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student makes two figures by script, the pendulum
table as points and the mass column as a histogram with a range and a bin
width chosen from the numbers, and places both in the report.

The new tool of the session is Matplotlib, installed with pip at the start.
Everything else is known: the project folder, the terminal, Python scripts,
NumPy arrays and masks, Markdown and Git.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · Matplotlib** · 20 min | | |
| 0:00 | [1. Install Matplotlib](#install) | `python -m pip install matplotlib` | A version number of Matplotlib in the terminal |
| 0:12 | [2. A figure in four lines](#first) | `scripts/first_plot.py` | A picture made by a script, open beside it |
| | **Part 2 · The pendulum table as points** · 30 min | | |
| 0:20 | [3. Read the table](#read-table) | `np.loadtxt` in `scripts/plot_pendulum.py` | Two arrays of nine numbers printed |
| 0:28 | [4. Points instead of a line](#points) | `ax.plot(length, t10, "o")` | Nine circles in `results/pendulum_plot.png` |
| 0:38 | [5. Labels, units and limits](#labels) | `ax.set_xlabel`, `ax.set_xlim`, `dpi=150` | The plot of the report, made by the room's own script |
| | **Part 3 · The mass column as a histogram** · 45 min | | |
| 0:50 | [6. Read the column](#read-column) | `usecols=0` in `scripts/plot_mass.py` | 91 583 values, the smallest and the largest |
| 0:57 | [7. The default histogram](#default) | `ax.hist(m)`, then `np.histogram(m)` | Ten bins, three bars, and the counts behind them |
| 1:07 | [8. Choose the range](#range) | `np.sort(m)`, a mask, `range=(1810, 1920)` | 91 579 values between 1810 and 1920 |
| 1:17 | [9. Choose the bin width](#width) | `bins=11`, `550`, then `55` | 55 bins of 2 MeV/c², the tallest with 3746 |
| 1:27 | [10. Labels with units](#mass-labels) | The two labels with `$` formulas | `results/mass_hist.png` with both axes labelled |
| | **Part 4 · The report** · 25 min | | |
| 1:35 | [11. Place the figures in the report](#report) | `results/report.md` and its preview | `report.md` with two figures and their sentences |
| 1:47 | [12. Say how the figures are made](#readme) | `## Figures` in `README.md`, then a commit | A **Figures** section in the README, and a commit |
| 1:55 | [13. Wrap up](#wrap-up) | The list of what was learned | |

**If time runs short:** leave out section 2, and in section 9 give
`bins=55` without trying the two other widths. Sections 11 and 12 stay: they
turn the two pictures into a result.

??? info "How to use this page"
    This page is written for the person at the front. Students follow the
    same page.

    - **Tell the room** is the paragraph to say before the steps.
    - The **numbered steps** are what to do on the projector. The room
      repeats each step on their own laptops.
    - **You should now see** closes a section. Ask for hands: "who sees
      this?" Go on when about four in five have it. The rest get help from a
      neighbour.
    - **Watch for** is the usual slip in that section.

    Keys are written for Windows, with macOS in brackets. The terminal is
    the one of VS Code: `zsh` on macOS, PowerShell 7 on Windows, as since
    [Seminar 4](seminar_04.md#shell). Where a command differs between
    systems, it has a tab for each: `python3` on macOS, `python` on
    Windows.

??? info "Before the session"
    For the room: the project folder with
    `data/processed/pendulum.csv`, `data/raw/D0_KPi.csv` and
    `results/report.md`, under Git since [Seminar 5](seminar_05.md), and
    Python with NumPy running in the terminal of VS Code, as installed in
    [Seminar 7](seminar_07.md#install). A student without one of these files
    downloads it now from the box **Files for this seminar** below.

    For you:

    - Sections 1 to 10 done once on your own laptop. Then delete the two
      scripts and `results/mass_hist.png` again, and put the handed-out
      picture back into `results/pendulum_plot.png`. You build all of it
      with the room.
    - The network of the room tried with one `pip install`. pip downloads
      Matplotlib from the internet. Have a phone ready as a hotspot.
    - Your zoom set for the projector, and this page open on a second device.

??? info "Files for this seminar"
    The files this session starts from. A browser saves
    each under the name in the second column.

    | File | Saved as | Put it in |
    |--|--|--|
    | [`pendulum.csv`](../data/pendulum.csv){ download="pendulum.csv" } | `pendulum.csv` | `data/processed` |
    | [`D0_KPi.csv`](../data/D0_KPi.csv){ download="D0_KPi.csv" } | `D0_KPi.csv` | `data/raw` |
    | [`pendulum_report.txt`](../data/pendulum_report.txt){ download="report.md" } | `report.md` | `results` |
    | [`pendulum_plot.png`](../data/pendulum_plot.png){ download="pendulum_plot.png" } | `pendulum_plot.png` | `results`. Section 4 writes over it |

---

## Part 1 · Matplotlib { #part-1 }

**0:00 to 0:20 · sections 1 and 2**

The room ends this part with Matplotlib installed and one picture made by a
script. No data file is read yet.

---

### 1. Install Matplotlib { #install }

**0:00 · 12 min**

**Tell the room.** Matplotlib is the plotting library of the lecture. It is
not a part of Python. It is installed once per laptop with pip, the program
that fetches Python packages from the internet.

1. Open the project folder in VS Code and select **Terminal** >
   **New Terminal**.

2. Check that Python answers.

    === "macOS"

        ```text
        python3 --version
        ```

    === "Windows"

        ```text
        python --version
        ```

    It prints a version, for example `Python 3.13.9`.

3. Install Matplotlib.

    === "macOS"

        ```text
        python3 -m pip install matplotlib
        ```

    === "Windows"

        ```text
        python -m pip install matplotlib
        ```

    pip downloads Matplotlib and the packages it needs, and installs them.
    This takes about a minute. The last line begins with
    `Successfully installed`. If the lines begin with
    `Requirement already satisfied`, Matplotlib was on the laptop before,
    and that is as good.

4. Ask Matplotlib for its version.

    === "macOS"

        ```text
        python3 -c "import matplotlib; print(matplotlib.__version__)"
        ```

    === "Windows"

        ```text
        python -c "import matplotlib; print(matplotlib.__version__)"
        ```

    It prints a version, for example `3.11.2`.

!!! success "You should now see"
    A version number of Matplotlib in every terminal of the room.

Say why the command is `python -m pip` and not `pip` alone: a laptop can have
more than one Python, and this form installs into the one that the word
`python` starts.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `zsh: command not found: python` | On macOS the program is `python3`, as in the macOS tab |
    | Windows: `Python was not found; run without arguments to install from the Microsoft Store, …` | A stand-in of Windows answered, not Python. Do as in [Seminar 4, section 4](seminar_04.md#shell), Watch for. Until then `py` works in place of `python`, here and in every later step |
    | `No module named pip` | Run `python -m ensurepip --upgrade` (macOS `python3 -m ensurepip --upgrade`), then step 3 again |
    | The download does not start | The network of the room blocks it. Connect the laptop to a phone hotspot |

---

### 2. A figure in four lines { #first }

**0:12 · 8 min**

**Tell the room.** Before any data is read, four lines show that Matplotlib
works: load it, make a figure, draw into it, save it. The picture is a file,
and VS Code opens it like any other file.

1. Select the `scripts` folder in the Side Bar, then **New File**, and name
   it:

    ```text
    first_plot.py
    ```

    Type into the file:

    ```text
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
    fig.savefig("results/first.png")
    ```

2. Save and run the script in the terminal.

    === "macOS"

        ```text
        python3 scripts/first_plot.py
        ```

    === "Windows"

        ```text
        python scripts/first_plot.py
        ```

    Nothing is printed. A file `first.png` appears under `results` in the
    Side Bar.

3. Select `first.png`. VS Code opens the picture in a tab. Drag the tab to
   the right edge of the Editor, so that the script and the picture stand
   side by side.

4. Change `16` to `30`, so that the line reads:

    ```text
    ax.plot([1, 2, 3, 4], [1, 4, 9, 30])
    ```

    Save, and run the script again: press `↑` in the terminal, then Enter.
    The picture changes without being opened again.

5. Delete `first.png` and `first_plot.py`: right-click each in the Side Bar
   and select **Delete**. They were a test.

!!! success "You should now see"
    Before step 5: a blue line through four points on a white picture of 640
    by 480 pixels, with numbers on both axes and no labels.

Say that these four lines are the frame of every script today: the import,
`plt.subplots()`, calls on `ax`, and `fig.savefig`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `ModuleNotFoundError: No module named 'matplotlib'` | pip installed into another Python than the one that runs the script. Repeat step 3 of section 1 with the word that runs the script: `python`, `python3` or `py` |
    | `FileNotFoundError: [Errno 2] No such file or directory: 'results/first.png'` | The terminal is not in the project folder. Run `pwd`, then `cd` to the folder that holds `results` |
    | The run button of VS Code gives an error and the terminal does not | Use the terminal today |

---

## Part 2 · The pendulum table as points { #part-2 }

**0:20 to 0:50 · sections 3 to 5**

The plot of the pendulum in `results/report.md` was handed out in
[Seminar 4](seminar_04.md#folder). The room now makes it with a script of
its own, from the cleaned table that every laptop has had since then.

---

### 3. Read the table { #read-table }

**0:20 · 8 min**

**Tell the room.** `data/processed/pendulum.csv` holds nine lengths in cm
and the time of 10 swings in s. `np.loadtxt` reads it into one array with
two columns, as in Lecture 7. Each column gets a name of its own, and the
unit goes into a comment beside it.

1. Select the `scripts` folder, then **New File**, and name it:

    ```text
    plot_pendulum.py
    ```

    Type into the file:

    ```text
    import numpy as np
    import matplotlib.pyplot as plt

    data = np.loadtxt("data/processed/pendulum.csv",
                      delimiter=",", skiprows=1)
    length = data[:, 0]    # cm
    t10 = data[:, 1]       # s
    print(length)
    print(t10)
    ```

2. Save and run it.

    === "macOS"

        ```text
        python3 scripts/plot_pendulum.py
        ```

    === "Windows"

        ```text
        python scripts/plot_pendulum.py
        ```

!!! success "You should now see"
    The two columns of the table as two arrays:

    ```text
    [ 20.  30.  40.  50.  60.  70.  80.  90. 100.]
    [ 9.02 11.05 12.61 14.23 15.49 16.84 17.9  19.1  20.01]
    ```

Say what the arguments do: `delimiter=","` names the sign between the values,
`skiprows=1` leaves out the header line, and `data[:, 0]` is every row of
column 0.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `ValueError: could not convert string '1;20;9' to float64 at row 0, column 1.` | The file that was read still has `;` and decimal commas. The path must say `processed`, and the file there must be the cleaned one. If in doubt, download [`pendulum.csv`](../data/pendulum.csv) again |
    | `FileNotFoundError` | The terminal is not in the project folder, or the file is not in `data/processed` |

---

### 4. Points instead of a line { #points }

**0:28 · 10 min**

**Tell the room.** `ax.plot` joins the points with straight lines unless it
is told otherwise. Nine measurements are nine points. A line between them
claims values that nobody measured.

1. Delete the two `print` lines and type in their place:

    ```text
    fig, ax = plt.subplots()
    ax.plot(length, t10)
    fig.savefig("results/pendulum_plot.png")
    ```

2. Run the script and open `results/pendulum_plot.png` beside it. The file
   held the picture that was handed out in Seminar 4. The script has written
   over it. The picture shows one bent line. Ask the room what is missing:
   the points, the names of the axes, the units.

3. Change the second of the three lines to

    ```text
    ax.plot(length, t10, "o")
    ```

    and run the script again. `"o"` draws a circle at each point and no
    line.

4. Let the room try each of these in place of `"o"`, and go back to `"o"`.

    ```text
    "s"
    ```

    ```text
    "x"
    ```

    ```text
    "o-"
    ```

!!! success "You should now see"
    Nine blue circles. The x-axis runs from 20 to 100 and the y-axis from 10
    to 20, and neither has a label.

---

### 5. Labels, units and limits { #labels }

**0:38 · 12 min**

**Tell the room.** A figure is read without its author beside it. Each axis
says what was measured and in which unit. Here both axes also start at zero,
so that the plot shows how the time grows with the length.

1. Add two lines between `ax.plot` and `fig.savefig`, and run the script.

    ```text
    ax.set_xlabel("length (cm)")
    ax.set_ylabel("time of 10 swings (s)")
    ```

    Every call that changes the figure stands before `fig.savefig`. A call
    after it changes nothing in the file.

2. Add the limits of the two axes under the labels, and run the script.

    ```text
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 22)
    ```

    The points now bend. From 20 cm to 100 cm the length grows 5 times and
    the time 2.2 times.

3. Change the last line to

    ```text
    fig.savefig("results/pendulum_plot.png", dpi=150)
    ```

    and run the script. Select the picture: the Status Bar gives its size,
    960 by 720 pixels. Before it was 640 by 480. The figure is 6.4 by 4.8
    inches, and `dpi` is the number of pixels per inch.

4. Open `results/report.md` and its preview with `Ctrl+K`, then `V` (macOS
   `Cmd+K`, then `V`). The plot under the table is the new one. The report
   was not touched: it names the file, and the file has changed.

!!! success "You should now see"
    In the preview of the report: nine points, an x-axis `length (cm)` from
    0 to 110 and a y-axis `time of 10 swings (s)` from 0 to 22. The script
    reads:

    ```text
    import numpy as np
    import matplotlib.pyplot as plt

    data = np.loadtxt("data/processed/pendulum.csv",
                      delimiter=",", skiprows=1)
    length = data[:, 0]    # cm
    t10 = data[:, 1]       # s

    fig, ax = plt.subplots()
    ax.plot(length, t10, "o")
    ax.set_xlabel("length (cm)")
    ax.set_ylabel("time of 10 swings (s)")
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 22)
    fig.savefig("results/pendulum_plot.png", dpi=150)
    ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The picture has no labels | The two label lines stand after `fig.savefig`. Move them above it |
    | The preview of the report shows the old plot | Close the preview and open it again |

---

## Part 3 · The mass column as a histogram { #part-3 }

**0:50 to 1:35 · sections 6 to 10**

The second figure has one variable, not two. The room draws it with the
defaults first, reads from the numbers why the defaults fail, and then
chooses a range and a bin width.

---

### 6. Read the column { #read-column }

**0:50 · 7 min**

**Tell the room.** `D0_KPi.csv` has 91 583 rows and four columns. One row is
one candidate pair of a kaon and a pion, and column `M` is the mass of the
pair in MeV/c². A single column has nothing to be plotted against. The
question is how often each value occurs.

1. Select the `scripts` folder, then **New File**, and name it:

    ```text
    plot_mass.py
    ```

    Type into the file:

    ```text
    import numpy as np
    import matplotlib.pyplot as plt

    m = np.loadtxt("data/raw/D0_KPi.csv", delimiter=",",
                   skiprows=1, usecols=0)
    print(m.size, m.min(), m.max())
    ```

2. Save and run it.

    === "macOS"

        ```text
        python3 scripts/plot_mass.py
        ```

    === "Windows"

        ```text
        python scripts/plot_mass.py
        ```

!!! success "You should now see"
    One line: the number of values, the smallest and the largest.

    ```text
    91583 1766.2096 2453.6584
    ```

Say that `usecols=0` reads the first column only, and that the script reads
the file in `data/raw` and never writes to it.

---

### 7. The default histogram { #default }

**0:57 · 10 min**

**Tell the room.** `ax.hist` cuts the range of the values into bins of equal
width, counts the values in each bin and draws one bar per bin. Without
further arguments it takes 10 bins between the smallest and the largest
value.

1. Add three lines at the end of the script.

    ```text
    fig, ax = plt.subplots()
    ax.hist(m)
    fig.savefig("results/mass_hist.png")
    ```

2. Run the script and open `results/mass_hist.png` beside it. The picture
   has three bars at its left edge, and an x-axis that runs beyond 2400.

3. Print the numbers behind the bars. `np.histogram` counts in the same way
   as `ax.hist` and draws nothing. Add at the end and run:

    ```text
    counts, edges = np.histogram(m)
    print(counts)
    print(edges)
    ```

4. Read the output with the room.

    | Question | Answer |
    |--|--|
    | How wide is a bin? | 1834.95 − 1766.21 = 68.7 MeV/c² |
    | Which bin holds 69 648 values? | The second, from 1835 to 1904 |
    | Where is the single value of the last bin? | Between 2385 and 2454: it is the largest, 2453.7 |

!!! success "You should now see"
    Three bars in the picture, and in the terminal the ten counts and the
    eleven edges of the bins:

    ```text
    [14575 69648  7359     0     0     0     0     0     0     1]
    [1766.2096  1834.95448 1903.69936 1972.44424 2041.18912 2109.934
     2178.67888 2247.42376 2316.16864 2384.91352 2453.6584 ]
    ```

Say that a default is a starting point. A single value at 2453.7 sets the
range, and a bin of 68.7 MeV/c² is wider than anything this column has to
show.

---

### 8. Choose the range { #range }

**1:07 · 10 min**

**Tell the room.** The range of a histogram is chosen by looking at where
the values are. A few values far from all others are left out of the
picture, and the report says how many.

1. Replace the three lines of step 3 of the last section by two lines, and
   run the script. `np.sort(m)` returns the values in rising order, and
   `[:5]` and `[-5:]` take the first five and the last five.

    ```text
    print(np.sort(m)[:5])
    print(np.sort(m)[-5:])
    ```

    The terminal shows:

    ```text
    [1766.2096 1808.1385 1811.0623 1811.5724 1811.7773]
    [1917.6561 1918.4805 1918.4851 1920.3453 2453.6584]
    ```

2. Read the two lines with the room. 1766.2 and 2453.7 stand alone. From
   1808 to 1920 the values follow each other closely. Round limits that hold
   them are 1810 and 1920.

3. Count what these limits leave out, with a mask as in Lecture 7. Replace
   the two `np.sort` lines by these and run the script. It prints
   `91579 4`.

    ```text
    inside = (m > 1810) & (m < 1920)
    print(inside.sum(), m.size - inside.sum())
    ```

4. Give the range to the histogram and run the script.

    ```text
    ax.hist(m, range=(1810, 1920))
    ```

!!! success "You should now see"
    Ten bars, each 11 MeV/c² wide. The fifth and the sixth reach about
    17 000 and 16 000. The others stay below 10 000.

Say that four values are not shown and that the report will say so. Leaving
values out of a picture without saying it is the step that makes a figure
misleading.

---

### 9. Choose the bin width { #width }

**1:17 · 10 min**

**Tell the room.** The bin width decides what a histogram can show. A bin
wider than a peak hides its shape. A bin that holds few values shows chance.
The width is tried, chosen and then stated.

1. Ask for 11 bins, which are 10 MeV/c² wide, and run the script.

    ```text
    ax.hist(m, bins=11, range=(1810, 1920))
    ```

    The peak is one bar with a step on each side.

2. Change `bins=11` to `bins=550`, which is 0.2 MeV/c² per bin:

    ```text
    ax.hist(m, bins=550, range=(1810, 1920))
    ```

    Run the script. The outline jumps from bin to bin.

3. Change it to `bins=55`, which is 2 MeV/c² per bin:

    ```text
    ax.hist(m, bins=55, range=(1810, 1920))
    ```

    Run the script. The peak has a shape, and the flat part on both sides is
    even.

4. Print the tallest bin. Add these two lines above `fig, ax = ...` and run
   the script. `counts.argmax()` is the position of the largest count.

    ```text
    counts, edges = np.histogram(m, bins=55, range=(1810, 1920))
    print(counts.max(), edges[counts.argmax()])
    ```

    It prints `3746 1862.0`: the tallest bin holds 3746 candidates and
    starts at 1862.

!!! success "You should now see"
    A peak near 1865 on a flat part of about 1400 per bin. Leave this table
    on the projector while the room compares:

    | `bins=` | Width of a bin | The tallest bin holds | A bin between 1820 and 1840 holds |
    |--|--|--|--|
    | 11 | 10 MeV/c² | 17 496 | about 7300 |
    | 55 | 2 MeV/c² | 3746 | about 1460 |
    | 550 | 0.2 MeV/c² | 398 | about 146 |

Say how the choice is made. The peak is 16 MeV/c² wide at half its height.
With 2 MeV/c² per bin eight bins lie across it, and neighbouring bins of the
flat part differ by 4 %. With 0.2 MeV/c² they differ by 10 %, and the picture
shows nothing more.

---

### 10. Labels with units { #mass-labels }

**1:27 · 8 min**

**Tell the room.** The x-axis gets the quantity and its unit. The y-axis of
a histogram is a count per bin, so its label states the bin width. 3746
candidates per 2 MeV/c² would be 1873 per 1 MeV/c².

1. Add two lines between `ax.hist` and `fig.savefig`.

    ```text
    ax.set_xlabel(r"$K^-\pi^+$ mass $M$ (MeV/$c^2$)")
    ax.set_ylabel(r"candidates per 2 MeV/$c^2$")
    ```

    Matplotlib sets the text between two `$` signs as a formula. `^` raises
    the character after it, and `\pi` is the letter π. The `r` before the
    quote tells Python to keep the backslash as typed.

2. Change the last line to

    ```text
    fig.savefig("results/mass_hist.png", dpi=150)
    ```

    and run the script.

!!! success "You should now see"
    The histogram with `K⁻π⁺ mass M (MeV/c²)` under the x-axis and
    `candidates per 2 MeV/c²` beside the y-axis, and three lines in the
    terminal:

    ```text
    91583 1766.2096 2453.6584
    91579 4
    3746 1862.0
    ```

    The script reads:

    ```text
    import numpy as np
    import matplotlib.pyplot as plt

    m = np.loadtxt("data/raw/D0_KPi.csv", delimiter=",",
                   skiprows=1, usecols=0)
    print(m.size, m.min(), m.max())

    inside = (m > 1810) & (m < 1920)
    print(inside.sum(), m.size - inside.sum())

    counts, edges = np.histogram(m, bins=55, range=(1810, 1920))
    print(counts.max(), edges[counts.argmax()])

    fig, ax = plt.subplots()
    ax.hist(m, bins=55, range=(1810, 1920))
    ax.set_xlabel(r"$K^-\pi^+$ mass $M$ (MeV/$c^2$)")
    ax.set_ylabel(r"candidates per 2 MeV/$c^2$")
    fig.savefig("results/mass_hist.png", dpi=150)
    ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `SyntaxWarning: invalid escape sequence '\p'` | The `r` before the quote is missing. The picture is made all the same |
    | The label shows the `$` signs and `\pi` as typed | One `$` is missing. They come in pairs |

---

## Part 4 · The report { #part-4 }

**1:35 to 2:00 · sections 11 to 13**

The two pictures become a result: each goes into the report with its
numbers, and the README names the script that makes it.

---

### 11. Place the figures in the report { #report }

**1:35 · 12 min**

**Tell the room.** A picture in `results` is not yet a result that someone
can read. The report handed out in Seminar 4 gets both figures. Under each
one stands a sentence that says what the figure shows, with the numbers the
scripts printed.

1. Open `results/report.md` and its preview. Change the first line from
   `# Pendulum` to `# Report`, and add an empty line and `## Pendulum` under
   it. The top of the file now reads:

    ```text
    # Report

    ## Pendulum
    ```

2. Go to the end of the file, below the line of the picture. Add an empty
   line and type:

    ```text
    The time of 10 swings rises from 9.02 s at 20 cm to 20.01 s at
    100 cm: 5 times the length takes 2.2 times the time.
    ```

3. Add the second figure below it. Copy this block with the button in its
   corner: the signs π and ² are not on most keyboards.

    ```text
    ## Mass of the K π pairs

    ![Histogram of the mass M](mass_hist.png)

    Column `M` of `data/raw/D0_KPi.csv`: 91 579 of the 91 583 values,
    from 1810 to 1920 MeV/c², in 55 bins of 2 MeV/c². The peak is near
    1865 MeV/c². The tallest bin, from 1862 to 1864, holds 3746
    candidates. A bin of the flat part holds about 1460.
    ```

4. Swap laptops with a neighbour. Using only the neighbour's report, say
   the range and the bin width of the histogram, and how many values it
   leaves out. This takes three minutes.

!!! success "You should now see"
    In the preview: the title, the table of the pendulum, its plot and one
    sentence, then the second heading, the histogram and four sentences.

Say what the text under a figure is for. It holds what the picture cannot
say: how many values were left out, the range, the bin width, and the
numbers a reader would otherwise have to read off the axis.

---

### 12. Say how the figures are made { #readme }

**1:47 · 8 min**

**Tell the room.** A figure whose script is known can be made again when a
label or the data changes. The README says which script makes which figure,
and Git keeps the scripts, the pictures and the report together.

1. Open `README.md` and add a section at its end.

    ```text
    ## Figures

    | Figure | Made by |
    |--|--|
    | `results/pendulum_plot.png` | `scripts/plot_pendulum.py` |
    | `results/mass_hist.png` | `scripts/plot_mass.py` |

    Run from the project folder: `python3 scripts/plot_mass.py` on
    macOS, `python scripts/plot_mass.py` on Windows.
    The scripts need NumPy and Matplotlib.
    ```

2. Try it. Delete `results/mass_hist.png` in the Side Bar and run:

    === "macOS"

        ```text
        python3 scripts/plot_mass.py
        ```

    === "Windows"

        ```text
        python scripts/plot_mass.py
        ```

    The picture is back, and the preview of the report shows it again.

3. Commit the work, as in Seminar 5. In the Source Control view, stage the
   two scripts, the two pictures, `report.md` and `README.md`, type the
   message and select **Commit**:

    ```text
    Add pendulum and mass figures
    ```

    The same in the terminal, one command after the other:

    ```text
    git add scripts results README.md
    ```

    ```text
    git commit -m "Add pendulum and mass figures"
    ```

!!! success "You should now see"
    A **Figures** section with a table of two rows in the preview of the
    README, and the six files no longer listed as changes in the Source
    Control view.

---

### 13. Wrap up { #wrap-up }

**1:55 · 5 min**

Read the list aloud. Ask on the way out which step was hardest.

- Matplotlib is installed with `python -m pip install matplotlib` (macOS
  `python3 -m pip install matplotlib`).
- A script makes a figure in four steps: the import, `plt.subplots()`, calls
  on `ax`, `fig.savefig`.
- `ax.plot(x, y, "o")` draws measurements as points.
- An axis label names the quantity and gives its unit in brackets.
- `ax.hist` counts values in bins. Its defaults are 10 bins from the
  smallest to the largest value.
- The range and the bin width of a histogram are chosen from the numbers,
  and both are stated: on the axis and in the text under the figure.
- A figure goes into the report with a sentence that says what it shows.
- The script that makes a figure is kept, named in the README and committed
  with the figure.

---

## Stretch goals

For students who finish a section early. Answers are given for the lecturer.

- Go through the slide *A Checklist for a Figure* of the lecture for both
  figures.
- Draw the formula of the pendulum over the points, as on the lecture slide
  *Points and a Formula Curve*: `L = np.linspace(0, 110, 200)`, then
  `ax.plot(L, 10 * 2 * np.pi * np.sqrt(L / 100 / 9.81))`. The answer: the
  curve passes within 0.08 s of every point.
- Plot `(t10 / 10) ** 2` against `length`. The answer: the nine points lie
  on a straight line through zero. The square of the period is 0.040 s² per
  cm of length, and 4.00 s² at 100 cm.
- Draw the whole column on a logarithmic y-axis: `ax.hist(m, bins=100)`
  without a range, then `ax.set_yscale("log")`. The answer: the two far
  values appear as bars of height 1 at both ends of the axis. Only 19 of the
  100 bins hold anything.
- Draw the counts as points with error bars, as on the lecture slide
  *Counts with Error Bars*. The answer: with 110 bins the highest point is
  1916, and its bar is ± 44.
- Read column `TAU` with `usecols=2` and draw its default histogram. The
  answer: two bars, 49 values in the first and 91 534 in the last. The 49
  are the rows with `-100`, the mark for a missing value. With the mask
  `tau[tau != -100]` the values run from −0.137 to 0.579.
- Save the histogram a second time with
  `fig.savefig("results/mass_hist.svg")` and open the file in a web browser.
  The answer: it stays sharp at every zoom, and VS Code opens the same file
  as text.
- If you have a dataset of your own: plot two of its columns of numbers
  against each other as points, and one column as a histogram with a range
  and a bin width you choose. `np.loadtxt(..., usecols=(1, 3))` reads the
  columns 1 and 3, counted from 0. A column that holds text cannot be read
  this way.

## If students ask for more

| Topic | Week |
|--|--|
| What a standard error is, and why a count of N scatters by √N | 9 (Probability & Statistics) |
| A curve fitted to the pendulum points and to the peak | 10 (Data Fitting) |
| Plots made straight from a table with Pandas | 12 (Pandas & Data Cleaning) |
| One command that makes every figure again | 13 (Reproducible Workflows) |

Leave out altogether, even if asked: Seaborn, Plotly, Jupyter notebooks,
interactive windows, animation.

## Aims practised

📁 two data files turned into two figures and a report · ♻️ each figure made again by its script · 🔧 the same script on Windows and macOS · ⚙️ one command per figure
