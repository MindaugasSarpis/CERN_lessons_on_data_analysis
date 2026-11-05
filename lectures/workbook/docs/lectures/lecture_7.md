# 7: Data Visualisation

Lecture 5 ended with a module, `weather.py`, and one number: the mean of the
87 552 measured hours of the weather station, 7.16 °C. Lecture 7 draws the
hours. It introduces Matplotlib on the plain lists that `weather.py` reads
(NumPy comes in Lecture 8), and then goes through the decisions that hold for
a figure made with any program: which chart, which axes, which colours, which
title. It opens on the mean and asks whether more or fewer hours lie near it
than in any other degree. The first histogram with bins of 1 °C answers it:
the hours fall into two seasons, near −1 °C and near 12 °C, and the mean lies
in the dip between them. The closing slide lists every choice of the two
figures with the number behind it.

## What the lecture covers

1. **Why a figure**: the mean of 87 552 hours and the question of the
   lecture; what a figure is for; Anscombe's quartet: four tables with the
   same means, the same closest line and the same *r*, told apart only by a
   plot.
2. **A first plot**: Figure, Axes and artists; every hour in four lines of
   Matplotlib, drawn against its position in the list; `weather.hours` and
   `datetime`, so each hour stands at its time, with labelled axes and units;
   the temperatures as a histogram with the default binning, then with a
   range (−17 to 33 °C) and a bin width (1 °C, 50 bins) chosen from the
   numbers: 10 °C draws one hump, 1 °C two seasons, 0.05 °C the rounding of
   the station.
3. **Mechanics of a figure**: the visual channels and their ranking; the
   parts of a figure; the legend; axis labels with units and their size; the
   coordinate system; the aspect ratio.
4. **Chart families**: amounts (bars from zero, sorted bars, the dot plot);
   distributions (density, bin width, the bin width in the browser, boxplot,
   violin, strip, empirical CDF, ridgeline, heatmap); proportions (pie,
   stacked bar, treemap); associations (scatter, bubble, overlapping points,
   hexagonal bins, correlation heatmap, pair plot, slopegraph); trends;
   uncertainty (error bars, band, many lines).
5. **Design principles**: the data-ink ratio; colour-vision deficiency; the
   three kinds of palette; rainbow against viridis; colour to highlight; the
   logarithmic and the square-root scale; small multiples.
6. **Stating the finding**: the title as the finding; direct labels;
   annotations; a reference line.
7. **Hands-on Matplotlib**: `weather.group`, the temperatures of each year,
   month or hour of the day; the hours below 0 °C per year as bars; the
   yearly means against the mean of all hours, with a legend; the monthly
   means with an annotation and a title that states the finding; one style
   for all figures; file formats.
8. **Wrap-up**: a checklist for a figure; every choice in the two figures,
   each with the number that justified it; the recap.

## Statistics used before Lecture 9

Statistics is the subject of the next lecture. This lecture uses five of its
terms, and each is defined in one sentence on the slide that uses it.

| Term | Slide | As defined there |
|--|--|--|
| Correlation *r* | 6, 54 | How near the points lie to a straight line: +1 on a rising line, −1 on a falling one, 0 with no trend |
| Scatter of a count | 18, 71 | A count *N* scatters by about √*N* when the measurement is repeated |
| Kernel density | 39 | Each value replaced by a small bell-shaped bump, and the bumps added up |
| Median, quartiles, IQR | 42 | Half of the values lie below the median, a quarter below the first quartile, three quarters below the third; the IQR is the length of the box |
| Standard error | 59 | The standard deviation of the *N* values divided by √*N* |

## The lecture, part by part

The lecture is slides 1–89. They estimate about 142 min, so in the two-hour
slot **plan to skip the slides of the second table**. Slides 90–100 are the
self-check quizzes and take no lecture time. To jump, type the slide number
and press Enter.

| Slides | Part |
|--|--|
| 1–6 | The mean of 87 552 hours (the question of the lecture), objectives, what a figure is for, Anscombe's quartet |
| 7–14 | A first plot: Figure and Axes, every hour as a line, the time on x, the histogram, its range and bin width. Slide 14 answers the opening question |
| 15–18, 22 | Visual channels and their ranking, the parts of a figure, axis labels with units |
| 26–30, 35 | Amounts: bars, bars from zero, the dot plot |
| 39, 40, 42 | Distributions: density, bin width, boxplot and its terms |
| 47, 48, 50, 57, 59, 60 | Proportions, the scatter plot, trends, uncertainty, which chart |
| 61–69, 72, 73 | Design: ink, colour, the logarithmic scale, small multiples |
| 74–78 | The finding: title, direct labels, annotation, reference line |
| 79, 80, 82, 83, 85 | Matplotlib again: `weather.group`, yearly means against the mean of all hours, monthly means annotated, saving |
| 86–89 | Checklist, every choice in the two figures, recap |

| Skip | Slides |
|--|--|
| The legend and its two examples | 19–21 |
| Label size, coordinate system, aspect ratio | 23–25 |
| Ordered categories, stacked bars, bars in three and two dimensions | 31–34 |
| Life expectancy, three slides | 36–38 |
| Choose the Bin Width, Live | 41 |
| Empirical CDF, ridgeline plot, lines or fill, heatmap | 43–46 |
| The treemap | 49 |
| Bubble chart, overlapping points, hexagonal bins, correlation heatmap, pair plot, slopegraph | 51–56 |
| Trend and seasonal cycle | 58 |
| Linear or Logarithmic, Live; the square-root scale | 70–71 |
| Hours below 0 °C per year as bars | 81 |
| One style for all figures | 84 |

- **Do not cut** slide 3 (The Mean of 87 552 Hours) or slides 7–14 (A First
  Plot), which answer it. The seminar draws the same file with the same
  calls: `subplots`, `plot`, `hist`, `savefig`, and the module `weather.py`.
- **Do not cut** slide 88 (Every Choice in the Two Figures), the closing
  slide: it lists every choice of the two figures with the number behind it.
- **Do not cut** slides 29–30 (bars from zero), 42 (the boxplot and its
  terms) or 59 (error bars and the standard error). Lectures 9 and 10 build
  on them.
- **Slides 9–14** show each script with the figure it makes; nothing is
  opened beside the deck. Slide 10 builds `weather.hours` from `temps` in one
  click, and slide 13 is the reasoning between the default histogram and the
  chosen one.
- **Slides 6, 20, 29 and 31** show the figure first and the explanation on
  the next click: ask the room before clicking. Ask the question of slide 3
  for a show of hands; slide 14 answers it.
- **Slide 18** (The Parts of a Figure) builds up in five clicks. The figure
  uses example values, not the course file.
- **Slides 41 and 70** run Python in the browser. The first run downloads
  the Python runtime, so run each once before the lecture.
- **Slides 9, 11, 12, 14 and 81–83** highlight the code in steps; slide 80
  goes from the function to its output in one click. Each click moves to the
  next group of lines.

Before the session, start the local copy of the slides: `node
scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/07-data-visualisation/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 90–100: ten quiz slides for students to try afterwards. The same
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
4. The mean of ten years of hourly temperatures is 7.16 °C. With 1 °C bins,
   7 to 8 °C holds 2706 hours, −1 to 0 °C 3848 and 11 to 12 °C 3032. What
   does this say about the mean?
   *The hours fall into two seasons, near −1 °C and near 12 °C, and the mean
   lies between them, in the dip, where fewer hours are. A mean is the
   balance point of the values, not the most common one.*
5. A sensor records tenths of a degree. A histogram of its values uses bins
   0.05 °C wide. What does it show?
   *About every other bin empty: from 0 to 2 °C the sensor can record 21
   values, and 40 bins cover that range. The bars show the rounding, not the
   weather.*
6. Two bars show the values 50 and 52, and the value axis starts at 48. How
   does the second bar look next to the first?
   *Twice as long: the bars are 2 and 4 units long. The values differ by
   4 %.*
7. Measured values run from 10 to 10 000 000. Which y-axis keeps the small
   and the large values apart?
   *A logarithmic axis. Each factor of ten takes the same length. On a linear
   axis everything below 100 000 lies in the lowest hundredth.*
8. Nine measurements of a temperature have a standard deviation of 0.3 °C.
   What is the standard error of their mean?
   *0.3 °C / √9 = 0.1 °C.*
9. A map shows how far the temperature of each region lies below or above
   the long-term mean, from −3 °C to +3 °C. Which palette fits?
   *A diverging palette: one hue for each sign, and a neutral colour at
   zero.*
10. A figure is made with `figsize=(6, 4)` and saved with `dpi=200`. How
    many pixels does the PNG file have?
    *1200 × 800: the size in inches times the pixels per inch.*

## Paired seminar

[Seminar 7 · Visualisation](../seminars/seminar_07.md) works on the weather
project. Every student starts from today's folder, adds Matplotlib to its
environment, adds the function `group` of slide 80 to the module
`weather.py`, and writes one script, `scripts/figures.py`, that draws five
figures of `weather.csv` into `results/` from lists: ten years day by day, the year's cycle, the day's cycle, the
yearly means and a histogram, and draws them all again with one line.

## Slides that left the deck

On 5 November 2026 the lecture moved before NumPy (it was Lecture 8), and the
slides that drew the pendulum table and the mass column of `D0_KPi.csv`
through NumPy were rebuilt on the weather project, with plain lists. Earlier,
five slides were removed and three replaced; since 6 October 2026 the sources
slide is parked in `lectures/content/parked/08_Data_Visualisation.md`, and its
list is under *Further reading* below. The deck before the move can be read
with `git show 16d92e9:lectures/content/slides/08_Data_Visualisation.md`.

| Earlier slide | What happened | Reason |
|--|--|--|
| The Pendulum Plot and the Mass Counts | Replaced by slide 3, The Mean of 87 552 Hours | The opening is a question about the room's own number, answered by the first histogram |
| Plot the Pendulum Table; Add Points, Labels and Units | Replaced by slides 9–11 | Every hour of the weather log, then at its time with `datetime`, with labels and units |
| A Histogram Counts Values in Bins; The Range and the Bin Width; The Mass Column as a Histogram | Rebuilt on the temperatures, slides 12–14 | The bin widths are 10, 1 and 0.05 °C; the last one shows the rounding of the station |
| A Peak on a Flat Background, Live | Replaced by slide 41, Choose the Bin Width, Live | It used NumPy; `random.gauss` draws two seasons |
| A Minimal Bar Chart | Replaced by slide 81 | The hours below 0 °C per year: a count, with a true zero |
| Points and a Formula Curve | Replaced by slide 82 | The yearly means against the mean of all hours: two layers and a legend |
| Counts with Error Bars | Replaced by slide 83 | The monthly means with an annotation and a title that states the finding |
| Roadmap for this Lecture | Removed | It repeated the learning objectives |
| Q–Q Plots | Removed | It needs the Normal distribution and quantiles, which Lecture 9 teaches |
| Quantile Dot Plot | Removed | It needs probability, which Lecture 9 teaches |
| The Seminar Dataset | Removed | The histogram of `weather.csv` is made on slides 12–14 |
| Practice Exercise | Removed | The room builds the same figures in the seminar |
| The Mental Model | Replaced by slide 8, in the first section | Matplotlib is introduced before it is used |
| Scatter with a Fit | Replaced, now by slide 82 | The room has no fitting yet |
| Histogram + Density Overlay | Replaced, now by slide 14 | It used SciPy |
| Further Reading | Parked; the list is below | Slide 88 answers the opening slide in its place |

## Further reading

- **C. O. Wilke**, *Fundamentals of Data Visualization*, free online at
  clauswilke.com/dataviz: the source of most figures in this lecture.
- **W. S. Cleveland**, *The Elements of Graphing Data*: the ranking of visual
  channels.
- **A. Cairo**, *The Truthful Art*: charts and maps for a general reader.
- **E. R. Tufte**, *The Visual Display of Quantitative Information*: the
  data-ink ratio.
- Every Matplotlib call is documented at matplotlib.org, with a gallery of
  examples and their code.

## Take-aways

- A script makes a figure in four steps: `import matplotlib.pyplot as plt`,
  `fig, ax = plt.subplots()`, calls on `ax`, `fig.savefig(...)`. Matplotlib
  draws plain lists; a list of `datetime` objects gives an axis of years.
- A line between points claims values in between: right for a log measured
  every hour, wrong for ten separate yearly means, which are points.
- An axis label names the quantity and gives the unit. The y-label of a
  histogram states the bin width.
- The range and the bin width of a histogram are chosen from the numbers:
  edges on round values, bins narrow enough to show the shape and wider than
  the steps in which the data are recorded.
- A mean can describe no single value: the mean of two seasons lies in the
  dip between them.
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
