# 8: Data Visualisation

Lecture 7 ended with data in NumPy arrays: a file read with `np.loadtxt`,
rows selected with a mask, values counted with `np.histogram`. The numbers
were printed. Lecture 8 draws them. It introduces Matplotlib on the two files
of the course, the pendulum table and the mass column of `D0_KPi.csv`, and
then goes through the decisions that hold for a figure made with any
program: which chart, which axes, which colours, which title.

## What the lecture covers

1. **Why a figure** — what a figure is for; Anscombe's quartet: four tables
   with the same means, the same closest line and the same *r*, told apart
   only by a plot.
2. **A first plot** — Figure, Axes and artists; the pendulum table in four
   lines of Matplotlib, then as points with labelled axes, units and limits;
   the mass column as a histogram with the default binning, and with a range
   (1810 to 1920 MeV/c²) and a bin width (2 MeV/c², 55 bins) chosen from the
   numbers.
3. **Mechanics of a figure** — the ranking of visual channels; the parts of a
   figure; the legend; axis labels with units and their size; the coordinate
   system; the aspect ratio.
4. **Chart families** — amounts (bars from zero, sorted bars, the dot plot);
   distributions (density, bin width, boxplot, violin, strip, empirical CDF,
   ridgeline, heatmap); proportions (pie, stacked bar, treemap); associations
   (scatter, bubble, overlapping points, hexagonal bins, correlation heatmap,
   pair plot, slopegraph); trends; uncertainty (error bars, band, many lines).
5. **Design principles** — the data-ink ratio; colour-vision deficiency; the
   three kinds of palette; rainbow against viridis; colour to highlight; the
   logarithmic and the square-root scale; small multiples.
6. **Stating the finding** — the title as the finding; direct labels;
   annotations; a reference line.
7. **Hands-on Matplotlib** — a bar chart; the pendulum points with the curve
   of the formula; the mass histogram as counts with error bars, an
   annotation and a title; one style for all figures; file formats.

## Statistics used before Lecture 9

Statistics is the subject of the next lecture. This lecture uses five of its
terms, and each is defined in one sentence on the slide that uses it.

| Term | Slide | As defined there |
|--|--|--|
| Correlation *r* | 5, 52 | How near the points lie to a straight line: +1 on a rising line, −1 on a falling one, 0 with no trend |
| Scatter of a count | 16, 69, 80 | A count *N* scatters by about √*N* when the measurement is repeated |
| Kernel density | 37 | Each value replaced by a small bell-shaped bump, and the bumps added up |
| Median, quartiles, IQR | 40 | Half of the values lie below the median, a quarter below the first quartile, three quarters below the third; the IQR is the length of the box |
| Standard error | 57 | The standard deviation of the *N* values divided by √*N* |

## The lecture in 90 minutes

The lecture is slides 1–86 and estimates about 136 min. Slides 87–95 are the
self-check quizzes and take no lecture time. In a 2-hour slot nothing has to
be skipped. For a 90-minute slot, skip the slides in the second table. To
jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–5 | Objectives, what a figure is for, Anscombe's quartet |
| 0:07 | 6–12 | A first plot: Figure and Axes, the pendulum as points, the mass histogram |
| 0:21 | 13–16, 20 | Visual channels, the parts of a figure, axis labels with units |
| 0:28 | 24–28, 33 | Amounts: bars, bars from zero, the dot plot |
| 0:35 | 37, 38, 40 | Distributions: density, bin width, boxplot and its terms |
| 0:40 | 45, 46, 48, 55, 57, 58 | Proportions, the scatter plot, trends, uncertainty, which chart |
| 0:51 | 59–67, 70, 71 | Design: ink, colour, the logarithmic scale, small multiples |
| 1:07 | 72–76 | The finding: title, direct labels, annotation, reference line |
| 1:14 | 77–80, 82 | Matplotlib again: bar chart, formula curve, error bars, saving |
| 1:24 | 83–86 | Checklist, sources, recap |
| 1:30 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| The legend and its two examples | 17–19 | 4 min |
| Label size, coordinate system, aspect ratio | 21–23 | 4 min |
| Ordered categories, stacked bars, bars in three and two dimensions | 29–32 | 5 min |
| Life expectancy, three slides | 34–36 | 4 min |
| Try It — Bin Width | 39 | 3 min |
| Empirical CDF, ridgeline plot, lines or fill, heatmap | 41–44 | 7 min |
| The treemap | 47 | 1 min |
| Bubble chart, overlapping points, hexagonal bins, correlation heatmap, pair plot, slopegraph | 49–54 | 10 min |
| Trend and seasonal cycle | 56 | 1 min |
| Try It — Which Scale?, the square-root scale | 68–69 | 4 min |
| One style for all figures | 81 | 2 min |

- **Do not cut** slides 7–12 (A First Plot). The seminar makes exactly these
  two figures, with the same calls, the same range and the same bin width.
- **Do not cut** slides 27–28 (bars from zero), 40 (the boxplot and its
  terms), 57 (error bars and the standard error) or 79–80 (formula curve,
  error bars). Lectures 9 and 10 build on them.
- **Slides 8–12 are shown live.** Keep VS Code open beside the slides, with
  the project folder and Matplotlib installed. Type the script of slide 8,
  run it, open `results/pendulum_plot.png` beside it, then make the changes
  of slide 9. Do the same for slides 10 and 12 in a second script. Slide 11
  is the reasoning between them: run `bins=11` and `bins=550` once each.
- **Slide 16** (The Parts of a Figure) builds up in five clicks. The figure
  uses example values, not the course file.
- **Slides 39 and 68** run Python in the browser. The first run downloads
  the Python runtime, so run each once before the lecture.
- **Slides 78–80** highlight the code in steps. Each click moves to the next
  group of lines.

Before the session, start the local copy of the slides:
`node scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/08-data-visualisation/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 87–95: eight quiz slides for students to try afterwards. The same
questions, with their answers:

1. Four tables give the same mean of x, the same mean of y, the same closest
   straight line and the same *r*. What comes before any of these numbers is
   used?
   *A plot of each table. The same numbers can come from a line with scatter,
   a curve, a line with one point off it, or a column of points with one far
   point. This is Anscombe's quartet.*
2. A script calls `ax.hist(v, bins=40, range=(100, 300))`. How wide is one
   bin?
   *5 units: the range of 200 units is cut into 40 bins.*
3. A column holds 20 000 values between 200 and 300, with a peak about 8
   units wide. Which binning shows the peak: 5 bins of 20, 50 bins of 2,
   10 000 bins of 0.01, or 10 bins between 0 and 1000?
   *50 bins of 2 units. The peak covers 4 bins and a bin holds 400 values on
   average. Wider bins swallow the peak, and bins of 0.01 hold 2 values each
   and show chance.*
4. Two bars show the values 50 and 52, and the value axis starts at 48. How
   does the second bar look next to the first?
   *Twice as long: the bars are 2 and 4 units long. The values differ by
   4 %.*
5. Measured values run from 10 to 10 000 000. Which y-axis keeps the small
   and the large values apart?
   *A logarithmic axis. Each factor of ten takes the same length. On a linear
   axis everything below 100 000 lies in the lowest hundredth.*
6. Nine timings of a pendulum have a standard deviation of 0.3 s. What is
   the standard error of their mean?
   *0.3 s / √9 = 0.1 s.*
7. A map shows how far the temperature of each region lies below or above
   the long-term mean, from −3 °C to +3 °C. Which palette fits?
   *A diverging palette: one hue for each sign, and a neutral colour at
   zero.*
8. A figure is made with `figsize=(6, 4)` and saved with `dpi=200`. How many
   pixels does the PNG file have?
   *1200 × 800: the size in inches times the pixels per inch.*

## Paired seminar

[Seminar 8 — Two Figures with Matplotlib](../seminars/seminar_08.md) installs
Matplotlib with pip and makes the two figures of slides 8–12 from the room's
own keyboard: the pendulum table as points, and the mass column as a
histogram with a range and a bin width that the room chooses from the
numbers. Both figures are saved to `results/` and placed in
`results/report.md`, each with a sentence that says what it shows. The README
gets a table of the figures and the scripts that make them. At home students
make the same two kinds of figure from their own dataset.

## Slides that left the deck

Five slides of the earlier deck are not in this one, and three were replaced.
The earlier deck can be read with
`git show cc65310:lectures/content/slides/08_Data_Visualisation.md`.

| Earlier slide | What happened | Reason |
|--|--|--|
| Roadmap for this Lecture | Removed | It repeated the learning objectives |
| Q–Q Plots | Removed | It needs the Normal distribution and quantiles, which Lecture 9 teaches |
| Quantile Dot Plot | Removed | It needs probability, which Lecture 9 teaches |
| The Seminar Dataset | Removed | The histogram of the real file is now made on slides 10–12 |
| Practice Exercise | Removed | The same tasks are the homework of the seminar |
| The Mental Model | Replaced by slide 7, in the first section | Matplotlib is introduced before it is used |
| Scatter with a Fit | Replaced by slide 79 | The room has no fitting yet. The curve is the formula of the pendulum |
| Histogram + Density Overlay | Replaced by slide 80 | It used SciPy. The slide now shows counts with error bars from the course file |

## Take-aways

- A script makes a figure in four steps: `import matplotlib.pyplot as plt`,
  `fig, ax = plt.subplots()`, calls on `ax`, `fig.savefig(...)`.
- Measurements are drawn as points. A line between them claims values that
  were not measured.
- An axis label names the quantity and gives the unit. The y-label of a
  histogram states the bin width.
- The range and the bin width of a histogram are chosen from the numbers:
  a bin several times narrower than the feature, and wide enough that
  neighbouring bins do not differ by chance.
- Position on a common scale is read most accurately, then length, then
  angle and area, then colour.
- Bars show a value by their length, so their axis starts at zero. Dots show
  it by position, so their axis need not.
- Ink that shows no data is removed: boxes, dense grids, 3D effects.
- The palette follows the variable: qualitative for categories, sequential
  for low to high, diverging for both sides of a midpoint. Red against green
  is not the only difference between two groups.
- A logarithmic axis for values over several factors of ten, a square-root
  axis for counts.
- The title states the finding. Labels stand next to the lines they name.
- The script is kept with the figure, so that the figure can be made again
  from the data file.
