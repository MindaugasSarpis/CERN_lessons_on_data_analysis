# 7: Data Visualisation

Lecture 5 ended with a module, `weather.py`, and one number: the mean of the
87 552 measured hours of the weather station, 7.16 °C. Lecture 7 draws the
hours, pictures first. It opens on the mean and asks whether more or fewer
hours lie near it than in any other degree. Two figures answer the question:
every hour at its time, and the hours in bins of 1 °C, which pile up in two
peaks, the cold months near −1 °C and the warm months near 12 °C, with the
mean in the dip between them; Anscombe's quartet then shows that this is
general: a few numbers cannot stand for the data. Then the decisions that
hold for a figure made with any program, on a gallery of examples: which
channel, which chart, which ink, colours and scale, which title. Then the
code, briefly: the figures of the start made with Matplotlib from the
plain lists `weather.py` reads (NumPy comes later), and two live blocks to
change the bin width and the scale. It closes on figures of three to five
variables of the weather log: a heatmap and a surface of ten years by day
and hour, contour lines, ten years in 3D against ten panels, a 3D scatter,
still and turning, parallel coordinates and an animation. The slides carry
one line or a few short fragments each; what the lecturer says is in the
speaker notes. After the recap come **For the Curious** (a little
statistics and the LHCb file) and **In Matplotlib**, the code of every
weather-log figure, call by call, for after the lecture.

## What the lecture covers

1. **Why a figure** (1–6): the mean of 87 552 hours, computed in six lines
   of Python, and the question of the lecture; every hour from 2016 to
   2025; the hours in bins of 1 °C, which answer the question; Anscombe's
   quartet: four tables with the same means and the same closest line,
   told apart only by a plot.
2. **Mechanics of a figure** (7–16): the visual channels and their ranking;
   the parts of a figure, built up on the histogram of the hours; the
   legend, and a legend without samples against names at the lines; axis
   labels with units and their size; the coordinate system; the aspect
   ratio.
3. **Chart families** (17–46): amounts (long labels under vertical, wider
   and horizontal bars; bars from zero; ordered categories; stacked and 3D
   bars; the dot plot, from alphabetical order through sorted bars to
   sorted dots); distributions (bin widths of ages, density, the hours as a
   boxplot, a violin and a strip; lines or fill); proportions (pie, stacked
   bar, separate bars; when a pie works); associations (the scatter plot,
   size as a third variable, the pair plot, overlapping points and
   hexagonal bins); trends (the data and the trend, the slopegraph, a line
   drawn through missing data against a gap); uncertainty (error bars with
   the standard error computed, a band or many lines); which chart for
   which question.
4. **Design principles** (47–60): the data-ink ratio; colour-vision
   deficiency; the three kinds of palette; rainbow against viridis; colour
   to highlight (US census 2010–2020), and ten overlapping yearly lines
   against one year in colour; the logarithmic scale, and linear against
   logarithmic live; small multiples and a shared axis; two y-axes against
   two panels (monthly temperature and humidity).
5. **Stating the finding** (61–66): the title as the finding; direct
   labels; annotations; a reference line; a window of years chosen for its
   story against all ten years.
6. **A first plot**, in code (67–74): Figure, Axes and artists; every hour
   in four lines of Matplotlib, drawn against its position in the list; the
   temperatures as a histogram with the default binning, then with a range
   (−17 to 33 °C) and a bin width (1 °C, 50 bins) chosen from the numbers:
   10 °C draws one hump, 1 °C two peaks, 0.05 °C the rounding of the
   station; the bin width changed live in the browser; saving as SVG and
   PNG.
7. **Beyond two axes** (75–84): the ten-year mean of every hour of every
   day as a heatmap and as a surface; humidity as contour lines over the
   temperature; all hours as ten planes stacked in 3D, where the gap of
   July 2019 hides, against ten flat panels, where it shows; temperature,
   humidity, wind and month of 3648 days in a 3D scatter, still and
   turning; five variables of each day as parallel coordinates; the
   histogram of each month as an animation, which shows where the two
   peaks of the year come from.
8. **Classics and maps** (85–90): Nightingale's roses of 1858 (month,
   cause and deaths as area); Minard's map of 1812 (six variables: the
   army's size as the band's width, place, direction, temperature, date);
   Rosling's bubble chart of 142 countries from 1952 to 2007, played and
   tapped live (income, life expectancy, population, continent, the year);
   Maunga Whau as a surface turned by hand and as a contour map; CERN's
   accelerators to scale and as a schematic, a topological map.
9. **Wrap-up** (91–94): a checklist for a figure; every choice in the two
   figures, with both figures on the slide; the recap.
10. **For the curious** (95–100), after the recap and outside the lecture
   time: the empirical CDF, the correlation heatmap, the square-root scale,
   and two figures of the LHCb file: a 2D histogram with its projections
   and a corner plot.
11. **In Matplotlib** (101–109), for after the lecture: the code of the
    weather-log figures, call by call: `weather.hours` and every hour at
    its time; `weather.group`; the hours below 0 °C per year as bars; the
    yearly means against the mean of all hours, with a legend; the monthly
    means with an annotation and a title that states the finding; one style
    for all figures.

## Statistics used before Lecture 8

Statistics is the subject of Lecture 8, Data Quality and Uncertainty. The
main path uses three of its ideas, each in plain words on the slide that
uses it; the others (the correlation *r*, the scatter √*N* of a count)
appear only in the speaker notes and in the section for the curious.

| Term | Slide | As said there |
|--|--|--|
| Density | 31 | A smoothed histogram: each age a small bump, the bumps added up; the bump width is chosen, like a bin width |
| Median | 32 | The box holds the middle half of the values; the line in it is the median, half of the values below, half above |
| Standard error | 44 | Standard deviation ÷ √*N*: 9 values with a standard deviation of 0.3 °C give 0.3 / √9 = 0.1 °C |

## The lecture, part by part

The lecture is slides 1–94 and estimates about 114 min, the teaching time of
the two-hour slot (the speaker notes plan about 118 min); if the room runs
late, **skip the slides of the second table** (about 5 min). Slides 95–100
are the optional section For the Curious, slides 101–109 the section In
Matplotlib, the code of the figures for after the lecture, and slides
110–122 the self-check quizzes; none of them takes lecture time. To jump,
type the slide number and press Enter.

| Slides | Part |
|--|--|
| 1–6 | The mean of 87 552 hours, computed on the slide (the question of the lecture), every hour from 2016 to 2025, the hours in bins of 1 °C, which answer the question on slide 5, then Anscombe's quartet: four tables that their numbers cannot tell apart |
| 7–16 | Mechanics: visual channels and their ranking, the parts of a figure on the histogram of the hours, the legend, axis labels with units and their size, the coordinate system, the aspect ratio |
| 17–29 | Amounts: long labels under vertical, wider and horizontal bars, bars from zero, ordered categories, stacked and 3D bars, the dot plot from alphabetical order to sorted dots |
| 30–33 | Distributions: bin widths of ages, density, the hours as a boxplot, a violin and a strip, lines or fill |
| 34–40 | Proportions and associations: pie, stacked bar and separate bars, when a pie works; the scatter plot, the bubble chart, the pair plot, overlapping points, hexagonal bins |
| 41–46 | Trends and uncertainty: the data and the trend, the slopegraph, a line through missing data, error bars and the standard error, a band or many lines; which chart for which question |
| 47–60 | Design: ink, colour-vision deficiency, palettes, colour to highlight, ten lines or one in colour, the logarithmic scale (live on slide 57), small multiples, a shared axis, two y-axes or two panels |
| 61–66 | The finding: title, direct labels, annotation, reference line, a window chosen for its story |
| 67–74 | A first plot, in code: Figure and Axes, every hour, the histogram, its range and bin width, the bin width live, saving |
| 75–84 | Beyond two axes: heatmap, surface, contour lines, ten years in 3D and as ten panels, four variables in a 3D scatter, still and turning, parallel coordinates, the animation of the months |
| 85–90 | Classics and maps: Nightingale's roses, Minard's map, the bubble chart (live), Maunga Whau as a surface and a contour map (live), CERN's accelerators to scale and as a schematic |
| 91–94 | Checklist, every choice in the two figures, recap |

| Skip | Slides |
|--|--|
| Label size, coordinate system, aspect ratio | 14–16 |
| The pair plot | 38 |
| Many points: hexagonal bins | 40 |

- **Do not cut** slides 3–5 (the question and the two figures that answer
  it) or slides 68–73, which draw the opening figures in code. The seminar
  draws the same file with the same calls: `subplots`, `plot`, `hist`,
  `savefig`, and the module `weather.py`, in a script `scripts/figures.py`.
- **Do not cut** slide 93 (Every Choice in the Two Figures), the closing
  slide: both figures, with the choice behind each part of them.
- **Do not cut** slides 21–22 (bars from zero), 32 (the boxplot and the
  median) or 44 (error bars and the standard error): Lecture 8 returns to
  the histogram, the spread of the values and the standard error.
- **Every figure fills the slide**: a single plot beside its caption, a
  figure of several panels under it. A caption is one line or a few short
  fragments; the explanations, the code of the advanced figures and the
  extra numbers are in the speaker notes (`Say:`, `If asked:`). Slides
  69–73 show each script with the figure it makes; nothing is opened beside
  the deck. Slide 71 is the reasoning between the default histogram and
  the chosen one.
- **Slides 43, 55, 60 and 66** are pairs drawn from the weather log, the
  mistake on the left, the repair on the right; most pairs of the gallery
  work the same way. **Slides 79 and 80** are a pair too: the ten years
  stacked in 3D hide the gap of July 2019, the ten flat panels show it.
- **Slides 12, 21 and 23** show the mistake first and the repair or the
  explanation on the next click, and slide 6 the numbers first and the four
  plots on the click: ask the room before clicking. Slide 71 shows the three
  bin widths on the first click and the conclusion on the second. Ask the
  question of slide 3 for a show of hands; slide 5 answers it, the counts
  written on the figure.
- **Slide 10** (The Parts of a Figure) builds the histogram of the hours up
  in five clicks.
- **Slides 22, 41, 53, 72, 82, 84, 88 and 89 are interactive figures** that work
  offline: drag where the bar axis starts (22), the smoothing window (41),
  switch the palette of the day-and-hour grid (53), drag the bin width from
  10 °C to 0.05 °C and press "0 to 2 °C" (72), drag the four-variable scatter
  to turn it (82; it turns slowly by itself until the first drag, a
  double-click brings back the start), step through the months or pause on
  one (84), let the bubble chart play and drag its year (88), turn Maunga
  Whau and press MAP (89). Use them on the projected window, not in the presenter view.
- **Slide 57** runs Python in the browser, the figure beside the code. The
  first run downloads the Python runtime, so run it once before the lecture.
- **Slides 69, 70 and 73** highlight the code in steps.
- **Slides 95–100** (For the Curious) are for time left at the end or for
  students afterwards. **Slides 101–109** (In Matplotlib) are the code of the
  weather-log figures, for after the lecture: slides 102 and 104 go from the
  function to its output in one click, the others highlight their code in
  steps.

Before the session, start the local copy of the slides: `node
scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/07-data-visualisation/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 111–122: twelve quiz slides for students to try afterwards. The same
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
   units wide. Which binning shows the shape of the peak: 5 bins of 20, 50 bins of 2,
   10 000 bins of 0.01, or 10 bins between 0 and 1000?
   *50 bins of 2 units. The peak covers 4 bins and a bin holds 400 values on
   average. Wider bins swallow the peak, and bins of 0.01 hold 2 values each
   and show chance.*
4. The mean of ten years of hourly temperatures is 7.16 °C. With 1 °C bins,
   3848 hours lie at −1 to 0 °C, 2706 at 7 to 8 °C and 3032 at 11 to 12 °C.
   What does this say about the mean?
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
9. Measured values run from 10 to 10 000 000 across categories. Which y-axis keeps the small
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
environment, adds the function `group` (slide 104) to the module
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
| The Pendulum Plot and the Mass Counts | Replaced by slide 3, The Mean Temperature of Ten Years | The opening is a question about the room's own number; slide 5 answers it |
| Learning Objectives; What a Figure Is For | Parked (5 Nov 2026) | Preambles without data (lecturer: "Some preambles?"); the deck opens on its question, as Lectures 4 to 6 do |
| Plot the Pendulum Table; Add Points, Labels and Units | Replaced by slide 69, and slides 102–103 of In Matplotlib | Every hour of the weather log, then at its time with `datetime`, with labels and units |
| A Histogram Counts Values in Bins; The Range and the Bin Width; The Mass Column as a Histogram | Rebuilt on the temperatures, slides 70, 71 and 73 | The bin widths are 10, 1 and 0.05 °C; the last one shows the rounding of the station |
| A Peak on a Flat Background, Live | Replaced by slide 72, Choose the Bin Width, Live | It used NumPy; `random.gauss` draws cold and warm hours in tenths, and the figure is drawn beside the code |
| A Minimal Bar Chart | Replaced by slide 105 | The hours below 0 °C per year: a count, with a true zero |
| Points and a Formula Curve | Replaced by slide 106 | The yearly means against the mean of all hours: two layers and a legend |
| Counts with Error Bars | Replaced by slide 107 | The monthly means with an annotation and a title that states the finding |
| Legends for Colour, Size and Shape; The Treemap; Trend and Seasonal Cycle | Parked (5 Nov 2026) | On the skip list already; out to keep the deck in its time band after *Beyond Two Axes* came in |
| The Ridgeline Plot; Temperatures as a Heatmap | Parked (7 Nov 2026) | Synthetic examples that a figure of the weather log now covers (the month histograms, the heatmap of day and hour); four good-and-bad pairs came in |
| The Dot Plot (five films) | Parked (8 Nov 2026) | Replaced by the life expectancy of 26 countries in three steps, alphabetical, sorted bars, sorted dots (slides 27–29): the lecturer asked for the busier dot plot that went from bad to good |
| Bin widths of ages, the empirical CDF, bubble chart, overlapping points, hexagonal bins, correlation heatmap, pair plot, slopegraph, square-root scale, a reference line (genes); the surface, the 3D scatter and the LHCb 2D histogram | Moved to For the Curious (9 Nov 2026) | Students found the lecture too complicated: new datasets, statistics (*r*, √*N*) and particle physics left the main path, which then estimated 131 min |
| The code of the hands-on figures: `weather.hours`, `weather.group`, the frost bars, the yearly and the monthly means, one style for all figures | Moved to In Matplotlib, slides 101–109 (9 Nov 2026, evening) | The lecture teaches the idea, the seminar the tool; the code stays as a reference for after the lecture |
| Visualising Uncertainty | Split into slides 44 (error bars, the standard error computed) and 45 (a band or many lines) (9 Nov 2026, night) | One idea per slide |
| Bin widths of ages, bubble chart, pair plot, overlapping points, hexagonal bins, slopegraph, a reference line; the surface, the 3D scatter, the scatter turning; Linear or Logarithmic, Live | Back on the main path, slides 30, 37–40, 42, 65, 77, 81, 82 and 57 (9 Nov 2026, night) | The lecturer asked for laconic slides, one line or a few fragments each; these figures, with no new statistics, keep the lecture at its two hours. For the Curious keeps the statistics and the LHCb file |
| Roadmap for this Lecture | Removed | It repeated the learning objectives |
| Q–Q Plots | Removed | It needs the Normal distribution and quantiles, not taught before Lecture 8 |
| Quantile Dot Plot | Removed | It needs probability, which Lecture 8 begins |
| The Seminar Dataset | Removed | The histogram of `weather.csv` is made on slides 70–73 |
| Practice Exercise | Removed | The room builds the same figures in the seminar |
| The Mental Model | Replaced by slide 68, in the code section | Matplotlib is introduced before it is used |
| Scatter with a Fit | Replaced, now by slide 106 | The room has no fitting yet |
| Histogram + Density Overlay | Replaced, now by slide 73 | It used SciPy |
| Further Reading | Parked; the list is below | Slide 93 answers the opening slide in its place |

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
