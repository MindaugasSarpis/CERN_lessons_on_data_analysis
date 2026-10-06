# Seminar 9 — A Result with Its Uncertainty

**Paired lecture:** 09 Probability & Statistics · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student writes two results into `results/report.md`
with their uncertainties: the mean of the mass column,
1864.10 ± 0.08 MeV/c², and g = 9.80 ± 0.04 m/s² from the pendulum table.

Everything is NumPy and Matplotlib from the last two seminars. The new
tools are `np.random.default_rng`, `std(ddof=1)` and `reshape`.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · A mean with its standard error** · 40 min | | |
| 0:00 | [1. Random numbers with a seed](#seed) | `scripts/dice.py`, run twice | The same 1000 rolls on every laptop |
| 0:10 | [2. The mean of the mass column](#mean) | `scripts/mass_stats.py` | 1864.10 ± 0.08 MeV/c² |
| 0:25 | [3. More rows, a smaller standard error](#rows) | The loop over `[100, 1000, 10000, N]` | A table of four sample sizes |
| | **Part 2 · A histogram against a Gaussian** · 35 min | | |
| 0:40 | [4. The mass values against a Gaussian](#gauss) | `scripts/mass_gauss.py` | `results/mass_gauss.png`, and 62.7 % |
| 1:00 | [5. The means of 100 values](#means) | `reshape(915, 100)` | `results/mass_means.png`, and 68.2 % |
| | **Part 3 · The uncertainty of g** · 35 min | | |
| 1:15 | [6. g from each row](#g) | `scripts/pendulum_g.py` | Nine values of g with their uncertainties |
| 1:30 | [7. The weighted mean](#weighted) | `w = 1 / sg**2` | g = 9.80 ± 0.04 m/s² |
| 1:40 | [8. The same by simulation](#simulation) | `rng.normal`, 100 000 times | 0.099 from 100 000 simulated measurements |
| | **Part 4 · The report** · 10 min | | |
| 1:50 | [9. Write the results down](#report) | `results/report.md`, then the preview | Two results with uncertainties in `report.md` |
| 1:57 | [10. Wrap up](#wrap-up) | The list of what was learned | |

**If time runs short:** leave out sections 5 and 8; section 9 then places
only `mass_gauss.png`. Every part starts from files the room already has.

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

    Scripts are run in the VS Code terminal, from the project folder:
    `zsh` on macOS, PowerShell 7 on Windows. The command is `python3` on
    macOS and `python` on Windows, so each run has a tab for each.

    Keys are written for Windows, with macOS in brackets.

??? info "Before the session"
    For the room: the project folder with `data/raw/D0_KPi.csv`,
    `data/processed/pendulum.csv` and `results/report.md`, and a Python that
    has NumPy and Matplotlib, as used in the last two seminars. A student
    without one of the files downloads it now from the box below. A student
    without the project folder downloads
    [`project_after_s3.zip`](../data/project_after_s3.zip), unpacks it, and
    opens `analysis-project` with **File** > **Open Folder...**. A laptop
    without NumPy or Matplotlib installs them now, as in
    [Seminar 7](seminar_07.md#install) and [Seminar 8](seminar_08.md#install):

    === "macOS"

        ```text
        python3 -m pip install numpy matplotlib
        ```

    === "Windows"

        ```text
        python -m pip install numpy matplotlib
        ```

    For you:

    - All four scripts of this page run once on your own laptop. The numbers
      on this page are the ones your screen must show.
    - The slide "The Uncertainty of g" of the lecture at hand. Section 6 is
      that slide for nine rows.

??? info "Files for this seminar"
    A browser saves each file under the name in the second column. Drag it
    into the folder in the third.

    | File | Saved as | Goes into |
    |--|--|--|
    | [`D0_KPi.csv`](../data/D0_KPi.csv){ download="D0_KPi.csv" } | `D0_KPi.csv` | `data/raw/` |
    | [`pendulum.csv`](../data/pendulum.csv){ download="pendulum.csv" } | `pendulum.csv` | `data/processed/` |
    | [`pendulum_report.txt`](../data/pendulum_report.txt){ download="report.md" } | `report.md` | `results/` |
    | [`pendulum_plot.png`](../data/pendulum_plot.png){ download="pendulum_plot.png" } | `pendulum_plot.png` | `results/`, next to `report.md`, which shows it |
    | [`project_after_s3.zip`](../data/project_after_s3.zip) | `project_after_s3.zip` | Unpacked anywhere: the whole `analysis-project` folder with all the files above |

---

## Part 1 · A mean with its standard error { #part-1 }

**0:00 to 0:40 · sections 1 to 3**

The room computes the three numbers of the lecture on a real column: the
mean, the standard deviation and the standard error.

---

### 1. Random numbers with a seed { #seed }

**0:00 · 10 min**

**Tell the room.** A simulation needs random numbers, and a result must be
reproducible. Both hold when the generator is given a seed: the same seed
gives the same numbers on every laptop.

1. In the Side Bar select `scripts`, then **New File**, and name it:

    ```text
    dice.py
    ```

2. Type the script and save it.

    ```text
    import numpy as np

    rng = np.random.default_rng(1)
    rolls = rng.integers(1, 7, 1000)
    print(rolls[:10])
    print(rolls.mean(), rolls.std(ddof=1))
    print((rolls == 6).mean())
    ```

3. Open the terminal with **Terminal** > **New Terminal** and run it.

    === "macOS"

        ```text
        python3 scripts/dice.py
        ```

    === "Windows"

        ```text
        python scripts/dice.py
        ```

4. Run it a second time with `↑` and Enter. The output is the same.

5. Change the seed from `1` to `2`, so that the line reads as below. Save
   and run. The numbers change.

    ```text
    rng = np.random.default_rng(2)
    ```

6. Put the seed back to `1`, save and run once more. The three lines of the
   page are back.

!!! success "You should now see"
    The same three lines on every laptop:

    ```text
    [3 4 5 6 1 1 5 6 2 2]
    3.493 1.7061248084070115
    0.162
    ```

A die has the mean 3.5 and the standard deviation 1.708. A thousand rolls
give 3.493 and 1.706. The fraction of sixes is 0.162, and 1/6 is 0.167.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `zsh: command not found: python` | On macOS the program is `python3`, as in the macOS tab |
    | `No such file or directory` | The terminal is not in the project folder. Run `pwd`, then `cd` to it |
    | The numbers differ from the page | The seed is not `1`, or the upper end is `6` instead of `7`. The upper end is not included |

---

### 2. The mean of the mass column { #mean }

**0:10 · 15 min**

**Tell the room.** The column `M` holds 91 583 values of one quantity. Three
numbers describe them: the mean, the standard deviation `s` of single
values, and the standard error `s / sqrt(N)` of the mean. `ddof=1` makes
NumPy divide by N − 1.

1. In `scripts`, create a new file named:

    ```text
    mass_stats.py
    ```

2. Type the script and save it.

    ```text
    import numpy as np

    M = np.loadtxt("data/raw/D0_KPi.csv", delimiter=",",
                   skiprows=1, usecols=0)
    N = len(M)
    mean = M.mean()
    s = M.std(ddof=1)
    se = s / np.sqrt(N)
    print("N    =", N)
    print("mean =", mean)
    print("s    =", s)
    print("se   =", se)
    print(f"M = {mean:.2f} +- {se:.2f} MeV/c2")
    ```

3. Run it.

    === "macOS"

        ```text
        python3 scripts/mass_stats.py
        ```

    === "Windows"

        ```text
        python scripts/mass_stats.py
        ```

4. Ask the room which of the printed digits mean something. The standard
   error is 0.08, so the mean is known to the second decimal. The last line
   prints the mean that way.

5. Ask what the 25.57 says and what the 0.08 says. One mass value lies
   about 25.57 MeV/c² from the mean. The mean itself is known to
   0.08 MeV/c².

!!! success "You should now see"
    ```text
    N    = 91583
    mean = 1864.1045817826453
    s    = 25.565096122743306
    se   = 0.08447729461566507
    M = 1864.10 +- 0.08 MeV/c2
    ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `s = 25.564956548991027` | `ddof=1` is missing. With 91 583 values the difference is in the sixth digit. With five values it is 12 % |

---

### 3. More rows, a smaller standard error { #rows }

**0:25 · 15 min**

**Tell the room.** The standard deviation is a property of the data and
stays. The standard error falls like one over the square root of the number
of rows. The room sees both in one table.

1. Add these lines at the end of `scripts/mass_stats.py`.

    ```text
    for n in [100, 1000, 10000, N]:
        x = M[:n]
        se_n = x.std(ddof=1) / np.sqrt(n)
        print(n, round(x.mean(), 2), round(x.std(ddof=1), 2),
              round(se_n, 3))
    ```

2. Before running, ask for a prediction: by what factor does the last
   column fall from one line to the next? By √10, about 3.2.

3. Run the script.

    === "macOS"

        ```text
        python3 scripts/mass_stats.py
        ```

    === "Windows"

        ```text
        python scripts/mass_stats.py
        ```

4. Read the table with the room. The third column stays near 25. The last
   falls from 2.6 to 0.08.

5. Ask whether the four means agree. 1865.68 lies 1.6 from the final mean,
   and its own standard error is 2.6. Each mean is within about one of its
   own standard errors of the last one.

!!! success "You should now see"
    Four more lines:

    ```text
    100 1865.68 26.14 2.614
    1000 1863.58 25.38 0.803
    10000 1863.87 24.98 0.25
    91583 1864.1 25.57 0.084
    ```

**Say it in these words.** The standard deviation describes the data, the
standard error belongs to the result. Half the standard error costs four
times the rows.

---

## Part 2 · A histogram against a Gaussian { #part-2 }

**0:40 to 1:15 · sections 4 and 5**

A mean and a standard deviation define a Gaussian. Whether the data follow
it is a separate question, and a figure answers it.

---

### 4. The mass values against a Gaussian { #gauss }

**0:40 · 20 min**

**Tell the room.** A density gives a probability per unit of `M`. A
histogram shows rows per bin. To draw one over the other, the density is
multiplied by the number of rows and by the bin width.

1. In `scripts`, create a new file named:

    ```text
    mass_gauss.py
    ```

2. Type the script and save it.

    ```text
    import numpy as np
    import matplotlib.pyplot as plt

    M = np.loadtxt("data/raw/D0_KPi.csv", delimiter=",",
                   skiprows=1, usecols=0)
    mean = M.mean()
    s = M.std(ddof=1)


    def gauss(x, mu, sigma):
        return (np.exp(-(x - mu)**2 / (2 * sigma**2))
                / (sigma * np.sqrt(2 * np.pi)))


    width = 2
    bins = np.arange(1790, 1942, width)
    x = np.linspace(1790, 1940, 300)

    fig, ax = plt.subplots()
    ax.hist(M, bins=bins)
    ax.plot(x, len(M) * width * gauss(x, mean, s))
    ax.set_xlabel("M (MeV/c2)")
    ax.set_ylabel("rows per 2 MeV/c2")
    fig.savefig("results/mass_gauss.png", dpi=150)

    print("within one s:", (abs(M - mean) < s).mean())
    print("within two s:", (abs(M - mean) < 2 * s).mean())
    ```

3. Run it.

    === "macOS"

        ```text
        python3 scripts/mass_gauss.py
        ```

    === "Windows"

        ```text
        python scripts/mass_gauss.py
        ```

4. Open `results/mass_gauss.png` from the Side Bar.

5. Ask where the curve fails. The peak of the data is narrower and higher,
   3700 rows against 2900. From 1815 to 1845 and from 1885 to 1915 the
   histogram is flat near 1400 while the curve falls. Outside that range
   the curve still has area and the data have none.

6. Compare the two printed fractions with the Gaussian values 68.3 % and
   95.4 %.

!!! success "You should now see"
    The figure with a peak on a flat part and a wider curve over it, and in
    the terminal:

    ```text
    within one s: 0.626732035421421
    within two s: 0.9989408514680672
    ```

The column is a mixture: a peak of D⁰ candidates on a flat part of other
pairs. One Gaussian with the mean and `s` of the whole column describes
neither.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The curve lies flat on the axis | The factor `len(M) * width` is missing. The density alone is at most 0.016 |
    | `IndentationError` | The two lines under `def` start with four spaces |
    | No picture in `results` | The script stopped at an error before `savefig`. Read the last line of the message |

---

### 5. The means of 100 values { #means }

**1:00 · 15 min**

**Tell the room.** The central limit theorem says that a mean of many values
is Gaussian even when the values are not, with the width `s / sqrt(100)`.
The file has enough rows to test it: 915 groups of 100.

1. Add these lines at the end of `scripts/mass_gauss.py`.

    ```text
    groups = M[:91500].reshape(915, 100)
    means = groups.mean(axis=1)
    se = s / np.sqrt(100)
    print(means.std(ddof=1), se)

    width = 0.5
    bins = np.arange(1855, 1873.5, width)
    x = np.linspace(1855, 1873, 300)

    fig, ax = plt.subplots()
    ax.hist(means, bins=bins)
    ax.plot(x, len(means) * width * gauss(x, mean, se))
    ax.set_xlabel("mean of 100 values of M (MeV/c2)")
    ax.set_ylabel("groups per 0.5 MeV/c2")
    fig.savefig("results/mass_means.png", dpi=150)

    print("within one se:", (abs(means - mean) < se).mean())
    print("within two se:", (abs(means - mean) < 2 * se).mean())
    ```

2. Say what `reshape(915, 100)` does: it arranges the first 91 500 values
   as a table of 915 rows and 100 columns. `mean(axis=1)` takes the mean of
   each row.

3. Run the script and open `results/mass_means.png`.

    === "macOS"

        ```text
        python3 scripts/mass_gauss.py
        ```

    === "Windows"

        ```text
        python scripts/mass_gauss.py
        ```

4. Compare the first new line: the 915 means scatter with 2.60, and
   `s / sqrt(100)` is 2.56.

5. Compare the last two lines with 68.3 % and 95.4 %.

!!! success "You should now see"
    A histogram that follows its curve, and three more lines in the
    terminal:

    ```text
    2.5956512602849324 2.5565096122743305
    within one se: 0.6819672131147541
    within two se: 0.9508196721311475
    ```

The single values gave 62.7 % and 99.9 %. Their means give 68.2 % and
95.1 %. This is why a mean is quoted with a Gaussian uncertainty even when
the data are not Gaussian.

---

## Part 3 · The uncertainty of g { #part-3 }

**1:15 to 1:50 · sections 6 to 8**

The pendulum table gives g from every row: g = 4π²ℓ / T², with the length
ℓ in metres and the period T = t₁₀ / 10. The file holds no uncertainties.
They are stated here: 0.1 cm on the length and 0.1 s on the time of 10
swings.

---

### 6. g from each row { #g }

**1:15 · 15 min**

**Tell the room.** For a product of powers the relative uncertainties add in
quadrature, each times its power. The period enters squared, so its
relative uncertainty counts twice. The relative uncertainty of T is that of
t₁₀.

1. In `scripts`, create a new file named:

    ```text
    pendulum_g.py
    ```

2. Type the script and save it.

    ```text
    import numpy as np

    data = np.loadtxt("data/processed/pendulum.csv",
                      delimiter=",", skiprows=1)
    length = data[:, 0]        # cm
    t10 = data[:, 1]           # s, time of 10 swings
    s_length = 0.1             # cm, stated
    s_t10 = 0.1                # s, stated

    T = t10 / 10
    g = 4 * np.pi**2 * (length / 100) / T**2
    rel = np.sqrt((s_length / length)**2 + (2 * s_t10 / t10)**2)
    sg = g * rel
    for i in range(len(g)):
        print(int(length[i]), round(g[i], 2), round(sg[i], 2))
    ```

3. Run it.

    === "macOS"

        ```text
        python3 scripts/pendulum_g.py
        ```

    === "Windows"

        ```text
        python scripts/pendulum_g.py
        ```

4. Check the last line by hand with the room: 0.1 / 100 is 0.1 %,
   2 × 0.1 / 20.01 is 1.0 %, together 1.0 %, and 1.0 % of 9.86 is 0.10.

5. Ask why the first row has more than twice the uncertainty of the last.
   The same 0.1 s is 1.1 % of 9.02 s and 0.5 % of 20.01 s.

6. Ask which input to improve. In the last row the timing gives 99 % of
   the variance. A better ruler changes nothing.

!!! success "You should now see"
    Nine lines: the length in cm, g and its uncertainty in m/s².

    ```text
    20 9.7 0.22
    30 9.7 0.18
    40 9.93 0.16
    50 9.75 0.14
    60 9.87 0.13
    70 9.74 0.12
    80 9.86 0.11
    90 9.74 0.1
    100 9.86 0.1
    ```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | g near 986 or 0.0986 | The length was not divided by 100, or was divided twice |
    | All nine uncertainties near 0.01 | The factor 2 before `s_t10` is missing, or `s_t10` was divided by `T` instead of `t10` |

---

### 7. The weighted mean { #weighted }

**1:30 · 10 min**

**Tell the room.** Nine values of the same quantity with unequal
uncertainties are combined with the weights 1/σᵢ². The uncertainty of the
result is one over the square root of the sum of the weights.

1. Add these lines at the end of `scripts/pendulum_g.py`.

    ```text
    w = 1 / sg**2
    best = (w * g).sum() / w.sum()
    err = 1 / np.sqrt(w.sum())
    print(f"g = {best:.2f} +- {err:.2f} m/s2")
    print("z =", (best - 9.81) / err)
    ```

2. Run the script.

    === "macOS"

        ```text
        python3 scripts/pendulum_g.py
        ```

    === "Windows"

        ```text
        python scripts/pendulum_g.py
        ```

3. Compare with one row: 9.86 ± 0.10 from the last row alone, 9.80 ± 0.04
   from all nine.

4. Read the last line: the result lies 0.13 of its uncertainty below 9.81.
   It is compatible with it.

!!! success "You should now see"
    Two more lines:

    ```text
    g = 9.80 +- 0.04 m/s2
    z = -0.1252849750622698
    ```

---

### 8. The same by simulation { #simulation }

**1:40 · 10 min**

**Tell the room.** Error propagation replaces the function by its tangent.
A simulation needs no such step: it repeats the measurement in the
computer, with the length and the time drawn from Gaussians, and looks at
the spread of the results.

1. Add these lines at the end of `scripts/pendulum_g.py`.

    ```text
    rng = np.random.default_rng(3)
    sim_length = rng.normal(100, s_length, 100000)
    sim_t10 = rng.normal(20.01, s_t10, 100000)
    sim_g = 4 * np.pi**2 * (sim_length / 100) / (sim_t10 / 10)**2
    print(sim_g.mean(), sim_g.std())
    ```

2. Run the script.

    === "macOS"

        ```text
        python3 scripts/pendulum_g.py
        ```

    === "Windows"

        ```text
        python scripts/pendulum_g.py
        ```

3. Compare the last line with the last row of section 6: 9.86 and 0.10.

!!! success "You should now see"
    One more line. The spread of 100 000 simulated measurements is 0.099,
    as from the formula.

    ```text
    9.860474937008293 0.09899416541917415
    ```

---

## Part 4 · The report { #part-4 }

**1:50 to 2:00 · sections 9 and 10**

---

### 9. Write the results down { #report }

**1:50 · 7 min**

**Tell the room.** A result is a value, its uncertainty, its unit and a word
on what the uncertainty is. The uncertainty has one or two significant
digits, and the value is rounded to the same decimal place.

1. Open `results/report.md` and add at the end:

    ```text
    ## The mass column

    | Quantity | Value |
    |--|--|
    | Rows | 91 583 |
    | Mean | 1864.10 ± 0.08 MeV/c² (standard error) |
    | Standard deviation | 25.57 MeV/c² |

    ![M against a Gaussian](mass_gauss.png)

    ![Means of 100 values of M](mass_means.png)

    ## g from the pendulum

    g = 9.80 ± 0.04 m/s², the weighted mean of nine rows.
    Stated uncertainties: 0.1 cm on the length and 0.1 s on
    the time of 10 swings.
    ```

    If section 5 was left out, leave out the line with `mass_means.png`.

2. Save, and open the preview with `Ctrl+K`, then `V` (macOS `Cmd+K`, then
   `V`).

!!! success "You should now see"
    Two new sections in the preview, with a table, two figures and one line
    for g.

---

### 10. Wrap up { #wrap-up }

**1:57 · 3 min**

Read the list aloud. Ask on the way out which step was hardest.

- A seed makes a simulation reproducible.
- `std(ddof=1)` is the standard deviation of single values. Divided by the
  square root of the number of rows it is the standard error of the mean.
- The standard deviation stays when rows are added. The standard error
  falls like one over the square root of their number.
- A density is drawn over a histogram after multiplying it by the number
  of rows and the bin width.
- The mass values are not Gaussian. Means of 100 of them are.
- Relative uncertainties of a product add in quadrature, each times its
  power.
- Values with unequal uncertainties are combined with the weights 1/σ².
- A simulation checks a propagated uncertainty without any derivative.

---

## Stretch goals

For students who finish a section early. Answers are given for the
lecturer.

- Print `np.median(M)`. The answer is 1864.0781, 0.03 below the mean.
- Two rows lie far outside the others: 1766.21 and 2453.66. Compute the
  mean without them, with the mask `(M > 1800) & (M < 1930)`. The answer
  is 1864.099 from 91 581 rows. The mean moves by 0.005, far less than its
  standard error.
- Compute the mean and its standard error for the rows with
  1850 < M < 1880. The answer is 1864.79 ± 0.04 from 41 090 rows. It lies
  0.69 above the mean of all rows, eight standard errors of that mean. The
  standard error does not cover the choice of rows.
- With `np.histogram` and `bins=np.arange(1810, 1922, 2)`, find the largest
  count and its Poisson uncertainty. The answer is 3746 ± 61, in the bin
  from 1862 to 1864.
- Set `s_t10 = 0.05` in `pendulum_g.py`. The answer is g = 9.81 ± 0.02
  m/s²: half the timing uncertainty gives half the uncertainty of g.
- Print the plain mean of the nine values, `g.mean()`. The answer is
  9.795, against 9.805 for the weighted mean.
- For the last row, work out on paper the uncertainty of g if 50 swings
  are timed instead of 10, with the same 0.1 s. The answer is 0.022 m/s²:
  the relative uncertainty of the period falls from 0.5 % to 0.1 %.
- A student who has a dataset of their own: the mean, the standard
  deviation and the standard error of one numeric column, and its
  histogram with the Gaussian over it.

## If students ask for more

| Topic | Week |
|--|--|
| The position and the width of the peak, with the flat part separated from it | 10 (Data Fitting) |
| A straight line through the nine pendulum points | 10 (Data Fitting) |
| Tables with named columns and missing values | 12 (Pandas & Data Cleaning) |

## Aims practised

♻️ seeded simulations, the same numbers on every laptop · ⚙️ one script from the data file to the result · 📁 results and figures written to `results/` · 🔧 plain NumPy, no special package
