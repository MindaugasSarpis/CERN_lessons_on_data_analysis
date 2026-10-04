# Seminar 10 — Fit a Straight Line and Measure g

**Paired lecture:** 10 Data Fitting from First Principles · **Format:** follow-along · **~120 min**
in class

The seminar has four parts, in this order.

1. **The data.** SciPy is installed. The pendulum table is read into NumPy
   arrays, and each value gets an uncertainty.
2. **The fit from the closed formulas.** Five sums, then slope and intercept,
   their uncertainties and covariance, then g with its uncertainty and χ².
3. **The same fit with `curve_fit`.** One call gives the same numbers. The
   room changes the call and sees what each argument does.
4. **Residuals.** A figure of the data, the line and what is left over, and
   the result written into the report.

Everything is typed into one script, `scripts/fit_pendulum.py`, which grows
from section to section and is run after every step. The new tool of the
session is SciPy, with one function.

## How to use this page

This page is written for the person at the front. Students can follow the
same page.

- The **paragraph at the top of a section** is what to tell the room.
- The **numbered steps** are what to do on the projector. The room repeats
  each step on their own laptops.
- **You should now see** closes a section. Ask for hands: "who sees this?"
  Go on when about four in five have it. The rest get help from a neighbour.
- **Watch for** is the usual slip in that section.

Keys are written for Windows, with macOS in brackets. Commands are typed in
the terminal inside VS Code and start with `python`. **On macOS type
`python3` wherever this page says `python`.**

| Clock | Section | The room ends with |
|--|--|--|
| | **Part 1 · The data** · 20 min | |
| 0:00 | [1. Install SciPy](#install) | A version number printed |
| 0:08 | [2. Read the table](#read) | Three arrays: x, y and its uncertainty |
| | **Part 2 · The fit from the closed formulas** · 45 min | |
| 0:20 | [3. Five sums](#sums) | S, Sx, Sy, Sxx, Sxy printed |
| 0:35 | [4. Slope, intercept, uncertainties](#slope) | a and b with ± and their covariance |
| 0:50 | [5. g and χ²](#g) | g = 9.845 ± 0.090 m/s², χ² = 2.65 for 7 |
| | **Part 3 · The same fit with `curve_fit`** · 25 min | |
| 1:05 | [6. Call `curve_fit`](#curve-fit) | The same five numbers from one call |
| 1:20 | [7. Change the call](#change) | The effect of `absolute_sigma`, `sigma` and `p0` seen |
| | **Part 4 · Residuals** · 30 min | |
| 1:30 | [8. Plot the fit and the residuals](#plot) | `results/pendulum_fit.png` |
| 1:45 | [9. Write the result down](#report) | A **Fit** section in the report |
| 1:55 | [10. Wrap up](#wrap-up) | The homework known |

In a 90-minute slot, skip section 7 and leave section 9 for home.

## Prerequisites

For the room: the project folder with `data/processed/pendulum.csv`, the
table cleaned in [Seminar 1](seminar_01.md), and Python with NumPy and
Matplotlib. A student who does not have
[`pendulum.csv`](../data/pendulum.csv) downloads it now and drags it onto
the `processed` folder.

For you, before the session:

- The whole script run once on your own laptop. The numbers on this page
  were produced with NumPy 2.3 and SciPy 1.16.
- A calculator, for the hand check in section 3.

## Part 1 · The data { #part-1 }

**0:00 to 0:20 · sections 1 and 2**

## 1. Install SciPy { #install }

**0:00 · 8 min**

SciPy is a library of numerical methods that work on NumPy arrays. Today
needs one function from it, `curve_fit`. It is installed once, like NumPy.

1. Open the project folder in VS Code and open the terminal with
   **Terminal** > **New Terminal**.

2. Install SciPy.

    ```text
    python -m pip install scipy
    ```

3. Check that Python finds it.

    ```text
    python -c "import scipy; print(scipy.__version__)"
    ```

You should now see a version number, for example `1.16.2`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `No module named pip` | Python was installed without pip. Run `python -m ensurepip` and repeat step 2 |
    | `ModuleNotFoundError: No module named 'scipy'` in step 3 | Step 2 and step 3 used two different Pythons. Use the same word, `python` or `python3`, in both |

## 2. Read the table { #read }

**0:08 · 12 min**

The table has nine lengths in centimetres and the time of ten swings in
seconds. The fit needs three arrays: x, the length in metres; y, the square
of the period; and the uncertainty of y. The stopwatch was worked by hand,
so we assume 0.1 s on the time of ten swings. One period then has 0.01 s,
and its square has 2 T × 0.01, by the propagation rule of Lecture 09.

1. In the Side Bar select the `scripts` folder, then **New File**, and type
   `fit_pendulum.py`.

2. Type the script.

    ```text
    import numpy as np

    table = np.loadtxt("data/processed/pendulum.csv", delimiter=",",
                       skiprows=1)
    x = table[:, 0] / 100          # length, cm to m
    t10 = table[:, 1]              # time of 10 swings, s

    T = t10 / 10                   # one period, s
    y = T**2                       # s squared
    sy = 2 * T * 0.01              # uncertainty of y: 0.1 s on t10

    print(x)
    print(y)
    print(sy)
    ```

3. Save with `Ctrl+S` (macOS `Cmd+S`) and run it in the terminal.

    ```text
    python scripts/fit_pendulum.py
    ```

You should now see three arrays of nine numbers:

```text
[0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]
[0.813604 1.221025 1.590121 2.024929 2.399401 2.835856 3.2041   3.6481
 4.004001]
[0.01804 0.0221  0.02522 0.02846 0.03098 0.03368 0.0358  0.0382  0.04002]
```

Ask the room which point is known best. It is the first: the short pendulum
has the smallest uncertainty in T squared.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `FileNotFoundError` | The terminal is not in the project folder. Run `pwd`, then `cd` to the project folder |
    | `could not convert string '1;20;9' to float64` | This is the raw file, with semicolons. The cleaned file is `data/processed/pendulum.csv` |

## Part 2 · The fit from the closed formulas { #part-2 }

**0:20 to 1:05 · sections 3 to 5**

The model is a straight line, y = a x + b. The lecture set the two
derivatives of χ² to zero and solved for a and b. The solution needs five
sums over the data and nothing else. The room now computes them.

## 3. Five sums { #sums }

**0:20 · 15 min**

Each point enters every sum with the weight 1/σ². A point with half the
uncertainty counts four times as much.

1. Delete the three `print` lines. Add at the end of the script:

    ```text
    w = 1 / sy**2
    S = np.sum(w)
    Sx = np.sum(w * x)
    Sy = np.sum(w * y)
    Sxx = np.sum(w * x * x)
    Sxy = np.sum(w * x * y)
    print(f"S = {S:.2f}  Sx = {Sx:.2f}  Sy = {Sy:.2f}")
    print(f"Sxx = {Sxx:.2f}  Sxy = {Sxy:.2f}")
    ```

2. Run the script.

3. Check the first weight on a calculator: 1 / 0.01804² = 3072.75. Add
   `print(w)` for a moment and compare with the first element. Remove the
   line again.

4. Ask why `Sy` is a round number. Add `print(w * y)` for a moment: every
   element is 2500. The uncertainty is 2 T × 0.01, so y/σ² is
   T² / (4 T² × 0.01²) = 2500 for every row.

You should now see:

```text
S = 11940.44  Sx = 5582.56  Sy = 22500.00
Sxx = 3353.27  Sxy = 13500.00
```

!!! warning "Watch for"
    `Sxx` comes out as 3353.27 only with `w * x * x`. A student who typed
    `w * x**2` has the same number. A student who typed `(w * x)**2` has
    3 463 011.91, the sum of the squared products.

## 4. Slope, intercept, uncertainties { #slope }

**0:35 · 15 min**

The slope and the intercept are ratios of these sums. So are their
uncertainties and their covariance. The denominator is the same in all
five.

1. Add at the end of the script:

    ```text
    D = S * Sxx - Sx**2
    a = (S * Sxy - Sx * Sy) / D
    b = (Sxx * Sy - Sx * Sxy) / D
    sa = np.sqrt(S / D)
    sb = np.sqrt(Sxx / D)
    cov = -Sx / D
    print(f"a = {a:.4f} +- {sa:.4f} s2/m")
    print(f"b = {b:.4f} +- {sb:.4f} s2")
    print(f"cov = {cov:.6f}  rho = {cov / (sa * sb):.2f}")
    ```

2. Run the script.

3. Read the result with the room. The slope is 4.0102 seconds squared per
   metre. Theory says 4π²/g, which is 4.024 for g = 9.81. The intercept
   should be zero, and it is half an uncertainty away from zero.

4. Ask what `rho = -0.88` means. A steeper line through these points meets
   the axis at x = 0 lower. A larger slope goes with a smaller intercept.

You should now see:

```text
a = 4.0102 +- 0.0367 s2/m
b = 0.0095 +- 0.0194 s2
cov = -0.000629  rho = -0.88
```

Say it in these words: the uncertainties did not use the y values at all.
They follow from the lengths chosen and from the 0.1 s. They were known
before the first swing was timed.

## 5. g and χ² { #g }

**0:50 · 15 min**

The slope is 4π²/g, so g is 4π² divided by the slope. Its relative
uncertainty is that of the slope. χ² then says whether nine points scatter
around the line as much as their uncertainties allow.

1. Add at the end of the script:

    ```text
    g = 4 * np.pi**2 / a
    sg = g * sa / a
    print(f"g = {g:.3f} +- {sg:.3f} m/s2")

    pull = (y - (a * x + b)) / sy
    chi2 = np.sum(pull**2)
    ndf = len(x) - 2
    print(f"chi2 = {chi2:.2f} for {ndf} degrees of freedom")
    ```

2. Run the script.

3. Add `print(np.round(pull, 2))` for a moment and read the nine pulls:
   `[ 0.12  0.39 -0.93  0.36 -0.52  0.57 -0.38  0.77 -0.39]`. No point is
   more than one uncertainty from the line. Remove the line again.

4. Compare χ² with the number of degrees of freedom. Nine points minus two
   fitted parameters leave 7. A χ² of 2.65 is below 7: the points lie
   closer to the line than 0.1 s predicts. With 0.06 s, χ² would be about 7.

You should now see:

```text
g = 9.845 +- 0.090 m/s2
chi2 = 2.65 for 7 degrees of freedom
```

Write the result on the board in the form it is reported:
g = 9.84 ± 0.09 m/s². The value 9.81 lies 0.4 uncertainties below it.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `g = 9.845 +- 1.448` | `sg` was computed as `g * sa * a`. It is `g * sa / a` |
    | `chi2 = 3051.44` | The residual was divided by `sy**2`. It is divided by `sy`, and the pull is squared afterwards |

## Part 3 · The same fit with `curve_fit` { #part-3 }

**1:05 to 1:30 · sections 6 and 7**

The closed formulas exist for a straight line. For other models a program
searches for the minimum of χ². `curve_fit` does that for any model written
as a Python function. On the straight line it has to return what the room
just computed.

## 6. Call `curve_fit` { #curve-fit }

**1:05 · 15 min**

`curve_fit` needs the model as a function whose first argument is x and
whose other arguments are the parameters. It needs the data, starting
values, and the uncertainties.

1. Add a second line at the top of the script, under `import numpy as np`:

    ```text
    from scipy.optimize import curve_fit
    ```

2. Add at the end of the script:

    ```text
    def line(x, a, b):
        return a * x + b


    popt, pcov = curve_fit(line, x, y, p0=[4.0, 0.0], sigma=sy,
                           absolute_sigma=True)
    perr = np.sqrt(np.diag(pcov))
    print("curve_fit:")
    print(f"a = {popt[0]:.4f} +- {perr[0]:.4f}")
    print(f"b = {popt[1]:.4f} +- {perr[1]:.4f}")
    print(f"cov = {pcov[0, 1]:.6f}")
    ```

3. Run the script and compare the last four lines with the lines printed
   in section 4.

4. Name the pieces with the room. `popt` holds the two estimates, in the
   order of the arguments of `line`. `pcov` is the covariance matrix: the
   squares of the uncertainties on its diagonal, the covariance beside it.

You should now see, below the earlier output:

```text
curve_fit:
a = 4.0102 +- 0.0367
b = 0.0095 +- 0.0194
cov = -0.000629
```

The five numbers agree with the closed formulas in every digit shown.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `ModuleNotFoundError: No module named 'scipy'` | Section 1 was skipped, or done with another Python |
    | `TypeError: line() takes 2 positional arguments but 3 were given` | The function was defined as `line(a, b)`. `x` comes first |

## 7. Change the call { #change }

**1:20 · 10 min**

Each argument of the call does one thing. The room removes them one at a
time, runs the script, reads the result, and puts the argument back.

1. Remove `absolute_sigma=True` and run. The estimates stay, and the
   uncertainties shrink to 0.0226 and 0.0120. Without this argument
   `curve_fit` multiplies them by the square root of χ²/ndf, which is
   √(2.65/7) = 0.61 here. Put the argument back.

2. Remove `sigma=sy` and `absolute_sigma=True` and run. Now every point
   counts the same: a = 4.0136 ± 0.0251 and b = 0.0075 ± 0.0164. The
   estimates moved, because the weights are gone. Put both back.

3. Change `p0=[4.0, 0.0]` to `p0=[-100.0, 50.0]` and run. The result is the
   same as before. For a straight line χ² has one minimum, and the search
   finds it from any start. Put the old values back.

You should now see the output of section 6 again.

| The call | a | b |
|--|--|--|
| as in section 6 | 4.0102 ± 0.0367 | 0.0095 ± 0.0194 |
| without `absolute_sigma=True` | 4.0102 ± 0.0226 | 0.0095 ± 0.0120 |
| without `sigma` | 4.0136 ± 0.0251 | 0.0075 ± 0.0164 |
| with `p0=[-100.0, 50.0]` | 4.0102 ± 0.0367 | 0.0095 ± 0.0194 |

Say it in these words: when the uncertainties are real, in the units of y,
`absolute_sigma=True` belongs in the call. Without it the uncertainty of
the result no longer depends on the 0.1 s we assumed.

## Part 4 · Residuals { #part-4 }

**1:30 to 2:00 · sections 8 to 10**

## 8. Plot the fit and the residuals { #plot }

**1:30 · 15 min**

On a plot of the data and the line nothing can be judged: the points sit on
the line. The residuals, data minus line, are a hundred times smaller than
the data. They get their own panel, with the same error bars.

1. Add a third line at the top of the script:

    ```text
    import matplotlib.pyplot as plt
    ```

2. Add at the end of the script:

    ```text
    fig, (top, bottom) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))
    top.errorbar(x, y, yerr=sy, fmt="o", label="data")
    top.plot(x, line(x, a, b), label="fit")
    top.set_ylabel("T squared (s2)")
    top.legend()

    bottom.errorbar(x, y - line(x, a, b), yerr=sy, fmt="o")
    bottom.axhline(0, color="gray")
    bottom.set_xlabel("length (m)")
    bottom.set_ylabel("residual (s2)")

    fig.savefig("results/pendulum_fit.png", dpi=150)
    ```

3. Run the script and open `results/pendulum_fit.png` from the Side Bar.

4. Read the lower panel with the room. Three questions: do the points
   scatter on both sides of zero, is there a trend or a bend, and how many
   error bars miss the zero line.

You should now see a figure with two panels. In the upper one the nine
points lie on the line and their error bars are hidden behind the markers.
In the lower one the residuals lie between −0.03 and +0.03 s², on both
sides of zero and without a trend, and every error bar reaches the zero
line.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `FileNotFoundError` for `results/pendulum_fit.png` | The project has no `results` folder. Create it in the Side Bar |
    | The old picture is shown | VS Code kept the tab open. Close it and open the file again |

## 9. Write the result down { #report }

**1:45 · 10 min**

A fit is reported with its model, its assumptions, its numbers and its
figure. The report of the project is the place for it.

1. Open `results/report.md` and add a section at the end.

    ```text
    ## Fit

    Model: T² = a·ℓ + b, fitted by weighted least squares to the nine
    rows of `data/processed/pendulum.csv`. Assumed uncertainty: 0.1 s
    on the time of 10 swings.

    | Quantity | Value |
    |--|--|
    | a | 4.010 ± 0.037 s²/m |
    | b | 0.009 ± 0.019 s² |
    | correlation of a and b | −0.88 |
    | χ² / degrees of freedom | 2.65 / 7 |
    | g = 4π²/a | 9.84 ± 0.09 m/s² (statistical) |

    ![Fit and residuals](pendulum_fit.png)

    Made by `python scripts/fit_pendulum.py`.
    ```

2. Open the preview with `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`).

You should now see the table and the figure in the preview.

## 10. Wrap up { #wrap-up }

**1:55 · 5 min**

Commit the script, the figure and the report in the Source Control view,
with a message such as `Fit of the pendulum table`. Put the tasks of the
next section on the projector and read them aloud.

What the room has learned:

- A fit needs a model, data with uncertainties, and χ² as the measure of
  mismatch.
- For a straight line five sums give the slope, the intercept, their
  uncertainties and their covariance.
- A quantity computed from a fitted parameter gets its uncertainty by
  propagation: g = 9.84 ± 0.09 m/s².
- `curve_fit` returns the estimates and the covariance matrix. With real
  uncertainties, `sigma` and `absolute_sigma=True` belong in the call.
- χ² is compared with the number of degrees of freedom, and the residuals
  are plotted under every fit.

## Next steps, at home

**45 min, before the next session**

1. In your own dataset, find two columns where a straight line is a
   reasonable model. If there are none, find a quantity that a simple
   function should describe: a constant, an exponential, a peak.

2. Decide on the uncertainty of each y value and write down where it comes
   from: the resolution of the instrument, a repeated measurement, or √n
   for a count.

3. Fit the model with `curve_fit`, with `sigma` and `absolute_sigma=True`.
   For a straight line, check the result against the closed formulas.

4. Compute χ² and the number of degrees of freedom, and plot the residuals
   under the fit.

5. Add a **Fit** section to your own report, in the form of section 9.

## Stretch goals

For students who finish a section early. Answers are given for the lecturer.

- Fix the intercept at zero: the model is y = a x, and the closed formula is
  a = Sxy / Sxx with uncertainty 1/√Sxx. The answer is a = 4.0259 ± 0.0173
  and g = 9.806 ± 0.042 m/s², with χ² = 2.88 for 8 degrees of freedom. The
  uncertainty of g is half that of the fit with a free intercept.
- Assume 0.05 s on the time of ten swings instead of 0.1 s. The answer is
  the same a and b, half the uncertainties (g = 9.845 ± 0.045 m/s²), and
  four times the χ²: 10.59 for 7.
- Do the fit with `np.polyfit(x, y, 1, w=1 / sy, cov="unscaled")`. The
  answer is `[4.01018132 0.00945546]` for the parameters, and the square
  roots of the diagonal of the covariance matrix are
  `[0.03668084 0.01943853]`.
- Add a term c x² to the model and fit with `curve_fit`. The answer is
  c = 0.03 ± 0.16: compatible with zero. χ² falls from 2.65 to 2.60, and
  the data do not ask for the extra term.
- Fit the D⁰ peak of `data/raw/D0_KPi.csv` with the code of the lecture
  slides *Counts and Their Uncertainty* and *The Fit in Code*. The answer is
  a peak position of 1864.47 ± 0.10 MeV/c², a width of 7.65 ± 0.10 MeV/c²,
  and χ² = 53.4 for 40 degrees of freedom.

## If students ask for more

| Topic | Where to look |
|--|--|
| Limits on a parameter, such as a width that must be positive | The `bounds` argument of `curve_fit` |
| A fit to small counts, where √n fails | `scipy.optimize.minimize` on −2 ln L of the Poisson distribution |
| A fitting package with more diagnostics | `lmfit`, and `iminuit`, the minimiser used at CERN |
| The theory in a book | Hughes and Hase, *Measurements and their Uncertainties* |

## Aims practised

♻️ one script from the data file to the number and the figure · ⚙️ the fit repeated by one command · 🔧 the same result from closed formulas, NumPy and SciPy
