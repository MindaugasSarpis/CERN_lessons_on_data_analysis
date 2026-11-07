# 7: Data Visualisation

Lecture 5 ended with a module, `weather.py`, and one number: the mean of the
87 552 measured hours of the weather station, 7.16 °C. Lecture 7 draws the
hours, pictures first and code after. It opens on the mean and asks whether
more or fewer hours lie near it than in any other degree; Anscombe's quartet
shows why a number is not enough, and two figures answer the question: every
hour at its time, and the hours in bins of 1 °C, which pile up in two peaks,
the cold months near −1 °C and the warm months near 12 °C, with the mean in
the dip between them. Then the decisions that hold for a
figure made with any program, on a gallery of examples: which channel, which
chart, which ink, colours and scale, which title. Only then the code: the two
figures of the start made with Matplotlib from the plain lists `weather.py`
reads (NumPy comes in Lecture 8), two live blocks to change the bin width and
the scale, and hands-on figures of the years and months. It closes on plots
of more than two variables: a heatmap and a surface of ten years by day and
hour, four variables in one 3D scatter, an animation, and a 2D histogram of
LHCb data with its projections.

## What the lecture covers

1. **Why a figure**: the mean of 87 552 hours and the question of the
   lecture; Anscombe's quartet: four tables with the same means, the same
   closest line and the same *r*, told apart only by a plot; every hour from
   2016 to 2025; the hours in bins of 1 °C, which answer the question.
2. **Mechanics of a figure**: the visual channels and their ranking; the
   parts of a figure; the legend; axis labels with units and their size; the
   coordinate system; the aspect ratio.
3. **Chart families**: amounts (bars from zero, sorted bars, the dot plot);
   distributions (density, bin width, boxplot, violin, strip, empirical CDF,
   lines or fill); proportions (pie, stacked bar); associations (scatter,
   bubble, overlapping points, hexagonal bins, correlation heatmap, pair
   plot, slopegraph); trends, and a line drawn through missing data against
   a gap (July 2019); uncertainty (error bars, band, many lines).
4. **Design principles**: the data-ink ratio; colour-vision deficiency; the
   three kinds of palette; rainbow against viridis; colour to highlight, and
   ten overlapping yearly lines against one year in colour; the logarithmic
   and the square-root scale; small multiples; two y-axes against two panels
   (monthly temperature and humidity).
5. **Stating the finding**: the title as the finding; direct labels;
   annotations; a reference line; a window of years chosen for its story
   against all ten years.
6. **A first plot**, in code: Figure, Axes and artists; every hour in four
   lines of Matplotlib, drawn against its position in the list;
   `weather.hours` and `datetime`, so each hour stands at its time; the
   temperatures as a histogram with the default binning, then with a range
   (−17 to 33 °C) and a bin width (1 °C, 50 bins) chosen from the numbers:
   10 °C draws one hump, 1 °C two peaks, 0.05 °C the rounding of the
   station; the bin width changed live in the browser.
7. **Hands-on Matplotlib**: `weather.group`, the temperatures of each year,
   month or hour of the day; the hours below 0 °C per year as bars; the
   yearly means against the mean of all hours, with a legend; the monthly
   means with an annotation and a title that states the finding; a linear
   and a logarithmic axis, live; one style for all figures; file formats.
8. **Beyond two axes**: the ten-year mean of every hour of every day as a
   heatmap and as a surface; temperature, humidity, wind and month in one 3D
   scatter; the histogram of each month as an animation, which shows where
   the two peaks of the year come from; the D⁰ of LHCb as a 2D histogram of
   mass and momentum with its two projections.
9. **Wrap-up**: a checklist for a figure; every choice in the two figures,
   each with the number that justified it; the recap.

## Statistics used before Lecture 9

Statistics is the subject of Lecture 9. This lecture uses five of its
terms, and each is defined in one sentence on the slide that uses it.

| Term | Slide | As defined there |
|--|--|--|
| Correlation *r* | 4, 38 | How near the points lie to a straight line: +1 on a rising line, −1 on a falling one, 0 with no trend |
| Scatter of a count | 10, 55 | A count *N* scatters by about √*N* when the measurement is repeated |
| Kernel density | 27 | Each value replaced by a small bell-shaped bump, and the bumps added up |
| Median, quartiles, IQR | 29 | Half of the values lie below the median, a quarter below the first quartile, three quarters below the third; the IQR is the length of the box |
| Standard error | 43 | The standard deviation of the *N* values divided by √*N* |

## The lecture, part by part

The lecture is slides 1–91. They estimate about 145 min, so in the two-hour
slot **plan to skip the slides of the second table**. Slides 92–104 are the
self-check quizzes and take no lecture time. To jump, type the slide number
and press Enter.

| Slides | Part |
|--|--|
| 1–6 | The mean of 87 552 hours (the question of the lecture), Anscombe's quartet, every hour from 2016 to 2025, the hours in bins of 1 °C. Slide 6 answers the question |
| 7–10, 13 | Visual channels and their ranking, the parts of a figure, axis labels with units |
| 17–21, 26 | Amounts: bars, bars from zero, the dot plot |
| 27–29 | Distributions: density, bin width, boxplot and its terms |
| 32–34, 41–44 | Proportions, the scatter plot, trends, a line through missing data, uncertainty, which chart |
| 45–54, 56–58 | Design: ink, colour, ten lines or one in colour, the logarithmic scale, small multiples, two y-axes or two panels |
| 59–64 | The finding: title, direct labels, annotation, reference line, a window chosen for its story |
| 65–73 | A first plot, in code: Figure and Axes, every hour, the time on x, the histogram, its range and bin width, the bin width live |
| 74, 75, 77, 78, 81 | Hands-on: `weather.group`, yearly means against the mean of all hours, monthly means annotated, saving |
| 82–87 | Beyond two axes: heatmap, surface, four variables, animation, a 2D histogram with projections |
| 88–91 | Checklist, every choice in the two figures, recap |

| Skip | Slides |
|--|--|
| The legend and a legend without samples | 11–12 |
| Label size, coordinate system, aspect ratio | 14–16 |
| Ordered categories, stacked bars, bars in three and two dimensions | 22–25 |
| Empirical CDF, lines or fill | 30–31 |
| Bubble chart, overlapping points, hexagonal bins, correlation heatmap, pair plot, slopegraph | 35–40 |
| The square-root scale | 55 |
| Hours below 0 °C per year as bars | 76 |
| Linear or Logarithmic, Live | 79 |
| One style for all figures | 80 |

- **Do not cut** slides 3–6 (the question and the two figures that answer
  it) or slides 65–73, which make the same figures in code. The seminar
  draws the same file with the same calls: `subplots`, `plot`, `hist`,
  `savefig`, and the module `weather.py`.
- **Do not cut** slide 90 (Every Choice in the Two Figures), the closing
  slide: it lists every choice of the two figures with the number behind it.
- **Do not cut** slides 20–21 (bars from zero), 29 (the boxplot and its
  terms) or 43 (error bars and the standard error). Lectures 9 and 10 build
  on them.
- **Every figure fills the slide**: a single plot beside its caption, a
  figure of several panels under it. Slides 66–73 show each script with the
  figure it makes; nothing is opened beside the deck. Slide 68 builds
  `weather.hours` from `temps` in one click, and slide 71 is the reasoning
  between the default histogram and the chosen one.
- **Slides 42, 53, 58 and 64** are pairs drawn from the weather log: the
  mistake on the left, the repair on the right.
- **Slides 12, 20 and 22** show the figure first and the explanation on the
  next click, and slide 4 the four numbers first and the four plots on the
  click: ask the room before clicking. Slide 71 shows the three bin widths
  on the first click and the conclusion on the second. Ask the question of
  slide 3 for a show of hands; slide 6 answers it.
- **Slide 10** (The Parts of a Figure) builds up in five clicks. The figure
  uses example values, not the course file.
- **Slides 72 and 79** run Python in the browser, the figure beside the code.
  The first run downloads the Python runtime, so run each once before the
  lecture.
- **Slides 67, 69, 70, 73 and 76–78** highlight the code in steps; slide 75
  goes from the function to its output in one click.
- **Slide 86** is an animation: it plays by itself, one month every 0.66 s.

Before the session, start the local copy of the slides: `node
scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/07-data-visualisation/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 92–104: twelve quiz slides for students to try afterwards. The same
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
   *The hours form two peaks, near −1 °C from November to March and near
   12 °C from April to October, and the mean lies between them, in the dip,
   where fewer hours are. A mean is the
   balance point of the values, not the most common one.*
5. A sensor records tenths of a degree. A histogram of its values uses bins
   0.05 °C wide. What does it show?
   *About every other bin empty: from 0 to 2 °C the sensor can record 21
   values, and 40 bins cover that range. The bars show the rounding, not the
   weather.*
6. A figure shows the days of the year across, the hours of the day up, and
   the mean temperature of each cell as a colour. How many variables does it
   show, and which is read least exactly?
   *Three: two positions and a colour. The temperature of one cell, because a
   colour is read less exactly than a position; the pattern across many
   cells is what the heatmap shows well.*
7. From the cold 2017 to the warm 2023 the yearly mean rose by 1.8 °C. What
   should a figure of the station's yearly means show?
   *All ten years, with the mean of all hours as a reference line. Two years
   picked for their values make any trend: 2017 to 2023 gives +1.8 °C, 2023
   to 2025 gives −2.3 °C.*
8. Two bars show the values 50 and 52, and the value axis starts at 48. How
   does the second bar look next to the first?
   *Twice as long: the bars are 2 and 4 units long. The values differ by
   4 %.*
9. Measured values run from 10 to 10 000 000. Which y-axis keeps the small
   and the large values apart?
   *A logarithmic axis. Each factor of ten takes the same length. On a linear
   axis everything below 100 000 lies in the lowest hundredth.*
10. Nine measurements of a temperature have a standard deviation of 0.3 °C.
   What is the standard error of their mean?
   *0.3 °C / √9 = 0.1 °C.*
11. A map shows how far the temperature of each region lies below or above
   the long-term mean, from −3 °C to +3 °C. Which palette fits?
   *A diverging palette: one hue for each sign, and a neutral colour at
   zero.*
12. A figure is made with `figsize=(6, 4)` and saved with `dpi=200`. How
    many pixels does the PNG file have?
    *1200 × 800: the size in inches times the pixels per inch.*

## Paired seminar

[Seminar 7 · Visualisation](../seminars/seminar_07.md) works on the weather
project. Every student starts from today's folder, adds Matplotlib to its
environment, adds the function `group` of slide 75 to the module
`weather.py`, and writes one script, `scripts/figures.py`, that draws five
figures of `weather.csv` into `results/` from lists: ten years day by day, the year's cycle, the day's cycle, the
yearly means and a histogram, and draws them all again with one line.

## Slides that left the deck

On 5 November 2026 the lecture moved before NumPy (it was Lecture 8): the
slides that drew the pendulum table and the mass column of `D0_KPi.csv`
through NumPy were rebuilt on the weather project, with plain lists; the
code moved after the design sections, the figures were drawn to fill their
slides, and a section *Beyond Two Axes* came in. Earlier, five slides were
removed and three replaced. Parked slides are in
`lectures/content/parked/07_Data_Visualisation.md`, the sources slide among
them (its list is under *Further reading* below). The deck before the move
can be read with
`git show 16d92e9:lectures/content/slides/08_Data_Visualisation.md`.

| Earlier slide | What happened | Reason |
|--|--|--|
| The Pendulum Plot and the Mass Counts | Replaced by slide 3, The Mean of 87 552 Hours | The opening is a question about the room's own number; slide 6 answers it |
| Learning Objectives; What a Figure Is For | Parked (5 Nov 2026) | Preambles without data (lecturer: "Some preambles?"); the deck opens on its question, as Lectures 4 to 6 do |
| Plot the Pendulum Table; Add Points, Labels and Units | Replaced by slides 67–69 | Every hour of the weather log, then at its time with `datetime`, with labels and units |
| A Histogram Counts Values in Bins; The Range and the Bin Width; The Mass Column as a Histogram | Rebuilt on the temperatures, slides 70, 71 and 73 | The bin widths are 10, 1 and 0.05 °C; the last one shows the rounding of the station |
| A Peak on a Flat Background, Live | Replaced by slide 72, Choose the Bin Width, Live | It used NumPy; `random.gauss` draws cold and warm hours in tenths, and the figure is drawn beside the code |
| A Minimal Bar Chart | Replaced by slide 76 | The hours below 0 °C per year: a count, with a true zero |
| Points and a Formula Curve | Replaced by slide 77 | The yearly means against the mean of all hours: two layers and a legend |
| Counts with Error Bars | Replaced by slide 78 | The monthly means with an annotation and a title that states the finding |
| Legends for Colour, Size and Shape; Life Expectancy in Alphabetical Order; Life Expectancy as Sorted Bars; The Treemap; Trend and Seasonal Cycle | Parked (5 Nov 2026) | On the skip list already; out to keep the deck in its time band after *Beyond Two Axes* came in |
| Life Expectancy as Sorted Dots; The Ridgeline Plot; Temperatures as a Heatmap | Parked (7 Nov 2026) | Synthetic examples that a figure of the weather log now covers (the films dot plot, the month histograms, the heatmap of day and hour); four good-and-bad pairs came in |
| Roadmap for this Lecture | Removed | It repeated the learning objectives |
| Q–Q Plots | Removed | It needs the Normal distribution and quantiles, which Lecture 9 teaches |
| Quantile Dot Plot | Removed | It needs probability, which Lecture 9 teaches |
| The Seminar Dataset | Removed | The histogram of `weather.csv` is made on slides 70–73 |
| Practice Exercise | Removed | The room builds the same figures in the seminar |
| The Mental Model | Replaced by slide 66, in the code section | Matplotlib is introduced before it is used |
| Scatter with a Fit | Replaced, now by slide 77 | The room has no fitting yet |
| Histogram + Density Overlay | Replaced, now by slide 73 | It used SciPy |
| Further Reading | Parked; the list is below | Slide 90 answers the opening slide in its place |

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
- A mean can describe no single value: the mean of the cold and the warm
  months lies in the dip between their two peaks.
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
- More than two variables go on colour, a third axis, time or side panels,
  each read less exactly than a position: a heatmap for values on a grid, a
  surface or a 3D scatter for a shape, a 2D histogram with its projections
  for counts.
- The title states the finding. Labels stand next to the lines they name.
- Missing data stay missing: a gap, not a line drawn across it. Two
  quantities in different units go in two panels, not on two y-axes. The
  window of a series is chosen before the result is seen.
- The script is kept with the figure, so that the figure can be made again
  from the data file.
