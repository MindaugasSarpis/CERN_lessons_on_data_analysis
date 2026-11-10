# 7: Data Visualisation

Lecture 5 ended with one number: the mean of the 87 552 measured hours of
the weather station, 7.16 °C. Lecture 7 draws the hours, pictures first. It
opens on the mean and asks whether more or fewer hours lie near it than in
any other degree. Two figures answer the question: every hour at its time,
and the hours in bins of 1 °C, which pile up in two peaks, the cold months
near −1 °C and the warm months near 12 °C, with the mean in the dip between
them; Anscombe's quartet then shows that this is general: a few numbers
cannot stand for the data. The parts of a figure are built up on a mass
peak of LHCb, and three short slides explain what the room may see there
for the first time: an error bar on a count, the fitted curve and its χ²,
and the pulls. Then the decisions that hold for a figure made with any
program, on a gallery of examples: which channel, which chart, which ink,
colours and scale, which title; Tufte's lie factor measures how far a
figure exaggerates, and four misleading figures are each drawn again
honestly. Then the code, briefly: the figures of the start made with
Matplotlib from a plain list that the code on the slide reads from
`weather.csv` (NumPy comes later), and two live blocks to change the bin
width and the scale. It closes on figures of three to five variables of the
weather log: a heatmap and a surface of ten years by day and hour, contour
lines, ten years in 3D against ten panels, a 3D scatter, still and turning,
parallel coordinates and an animation. The slides carry one line or a few
short fragments each; what the lecturer says is in the speaker notes. After
the recap come **For the Curious** (a little statistics and the LHCb file)
and **In Matplotlib**, the code of every weather-log figure, call by call,
for after the lecture.

## What the lecture covers

1. **Why a figure** (1–6): the mean of 87 552 hours, computed in six lines
   of Python, and the question of the lecture; every hour from 2016 to
   2025; the hours in bins of 1 °C, which answer the question; Anscombe's
   quartet: four tables with the same means and the same closest line,
   told apart only by a plot.
2. **Mechanics of a figure** (7–19): the visual channels and their ranking;
   the parts of a figure, built up on a mass peak of LHCb with its fit, and
   three explainers with that figure's numbers: an error bar on a count,
   √95 = 9.7, tested on the 61 blocks of 1500 rows of the file (39 of 60
   repeats inside the bar); the fitted curve as the smallest χ², 24.3, with
   one bin's term computed; the pulls, 21 of 30 within ±1 and
   χ²/ndf = 0.97, against the straight line alone, 5.2; the legend, and a
   legend without samples against names at the lines; axis labels with
   units and their size; the coordinate system; the aspect ratio.
3. **Chart families** (20–50): amounts (long labels under vertical, wider
   and horizontal bars; bars from zero, and Tufte's lie factor computed on
   them: 44.6 from 48, 1.0 from zero; ordered categories; stacked and 3D
   bars; the dot plot, from alphabetical order through sorted bars to
   sorted dots); distributions (bin widths of ages, density, the hours as a
   boxplot, a violin and a strip; lines or fill); proportions (pie, stacked
   bar, separate bars; when a pie works); associations (the scatter plot,
   size as a third variable, the pair plot, overlapping points and
   hexagonal bins); trends (the data and the trend, the slopegraph, a line
   drawn through missing data against a gap); uncertainty (error bars with
   the standard error computed, a band or many lines); which chart for
   which question.
4. **Design principles** (51–64): the data-ink ratio; colour-vision
   deficiency; the three kinds of palette; rainbow against viridis; colour
   to highlight (US census 2010–2020), and ten overlapping yearly lines
   against one year in colour; the logarithmic scale, and linear against
   logarithmic live; small multiples and a shared axis; two y-axes against
   two panels (monthly temperature and humidity).
5. **Stating the finding** (65–70): the title as the finding; direct
   labels; annotations; a reference line; a window of years chosen for its
   story against all ten years.
6. **Misleading figures** (71–80): the principle of proportional ink, then
   four figures that mislead with correct numbers, each followed by the
   same data drawn honestly, with its lie factor: the frost hours of each
   year as circles sized by radius (2.5) and as bars; the hours in four
   temperature bands as a pie in perspective (−3.3) and as bars; the hours
   of 20 °C or more as a running total (−0.33) and year by year; CO₂ at
   Mauna Loa every ten, then every five years drawn as equal steps (−0.95)
   and on a time axis.
7. **A first plot**, in code (81–88): Figure, Axes and artists; every hour
   in four lines of Matplotlib, drawn against its position in the list; the
   temperatures as a histogram with the default binning, then with a range
   (−17 to 33 °C) and a bin width (1 °C, 50 bins) chosen from the numbers:
   10 °C draws one hump, 1 °C two peaks, 0.05 °C the rounding of the
   station; the bin width changed live in the browser; saving as SVG and
   PNG.
8. **Beyond two axes** (89–98): the ten-year mean of every hour of every
   day as a heatmap and as a surface; humidity as contour lines over the
   temperature; all hours as ten planes stacked in 3D, where the gap of
   July 2019 hides, against ten flat panels, where it shows; temperature,
   humidity, wind and month of 3648 days in a 3D scatter, still and
   turning; five variables of each day as parallel coordinates; the
   histogram of each month as an animation, which shows where the two
   peaks of the year come from.
9. **Classics and maps** (99–104): Nightingale's roses of 1858 (month,
   cause and deaths as area); Minard's map of 1812 (six variables: the
   army's size as the band's width, place, direction, temperature, date);
   Rosling's bubble chart of 142 countries from 1952 to 2007, played and
   tapped live (income, life expectancy, population, continent, the year);
   Maunga Whau as a surface turned by hand and as a contour map; CERN's
   accelerators to scale and as a schematic, a topological map.
10. **Wrap-up** (105–108): a checklist for a figure; every choice in the two
   figures, with both figures on the slide; the recap.
11. **For the curious** (109–114), after the recap and outside the lecture
   time: the empirical CDF, the correlation heatmap, the square-root scale,
   and two figures of the LHCb file: a 2D histogram with its projections
   and a corner plot.
12. **In Matplotlib** (115–123), for after the lecture: the code of the
    weather-log figures, call by call, each reading `weather.csv` itself:
    the time of each hour with `datetime` and every hour at its time; the
    temperatures of each year with a function `group`; the hours below
    0 °C per year as bars; the yearly means against the mean of all hours,
    with a legend; the monthly means with an annotation and a title that
    states the finding; one style for all figures; the bin width live.

## Statistics used before Lecture 8

Statistics is the subject of Lecture 8, Data Quality and Uncertainty. The
main path uses these of its ideas, each in plain words and with its numbers
on the slide that uses it; the others (the correlation *r*) appear only in
the speaker notes and in the section for the curious.

| Term | Slide | As said there |
|--|--|--|
| Error bar of a count | 11 | ± √*n*: 95 pairs, √95 = 9.7; in 61 blocks of 1500 rows of the same file, 39 of the other 60 counts land inside the bar, about 2 in 3 |
| χ² and the fitted curve | 12 | χ² = Σ ((count − curve) ÷ bar)²: the top bin (13.6 ÷ 9.75)² = 1.9, all 30 bins 24.3; the fit keeps the five numbers with the smallest χ² |
| Pull | 13 | (count − fit) ÷ error bar: (95 − 81.4) ÷ 9.75 = +1.39; 21 of 30 within ±1, all within ±2; χ²/ndf = 24.3 ÷ (30 − 5) = 0.97 |
| Density | 35 | A smoothed histogram: each age a small bump, the bumps added up; the bump width is chosen, like a bin width |
| Median | 36 | The box holds the middle half of the values; the line in it is the median, half of the values below, half above; the whiskers reach 1.5 box lengths |
| Standard error | 48 | Standard deviation ÷ √*N*: 9 values with a standard deviation of 0.3 °C give 0.3 / √9 = 0.1 °C |

## The lecture, part by part

The lecture is slides 1–108 and estimates about 129 min (the speaker notes
plan about 140 min), more than the teaching time of the two-hour slot: plan
on **skipping the slides of the second table** (about 9 min) and more of
the gallery if the room runs late. Slides 109–114 are the optional section For
the Curious, slides 115–123 the section In Matplotlib, the code of the
figures for after the lecture, and slides 124–139 the self-check quizzes,
followed by the glossary; none of them takes lecture time. To jump, type
the slide number and press Enter.

| Slides | Part |
|--|--|
| 1–6 | The mean of 87 552 hours, computed on the slide (the question of the lecture), every hour from 2016 to 2025, the hours in bins of 1 °C, which answer the question on slide 5, then Anscombe's quartet: four tables that their numbers cannot tell apart |
| 7–19 | Mechanics: visual channels and their ranking, the parts of a figure on a mass peak of LHCb with its fit, then what its error bars, its fitted curve (χ²) and its pulls are (11–13), the legend, axis labels with units and their size, the coordinate system, the aspect ratio |
| 20–33 | Amounts: long labels under vertical, wider and horizontal bars, bars from zero, Tufte's lie factor, ordered categories, stacked and 3D bars, the dot plot from alphabetical order to sorted dots |
| 34–37 | Distributions: bin widths of ages, density, the hours as a boxplot, a violin and a strip, lines or fill |
| 38–44 | Proportions and associations: pie, stacked bar and separate bars, when a pie works; the scatter plot, the bubble chart, the pair plot, overlapping points, hexagonal bins |
| 45–50 | Trends and uncertainty: the data and the trend, the slopegraph, a line through missing data, error bars and the standard error, a band or many lines; which chart for which question |
| 51–64 | Design: ink, colour-vision deficiency, palettes, colour to highlight, ten lines or one in colour, the logarithmic scale (live on slide 61), small multiples, a shared axis, two y-axes or two panels |
| 65–70 | The finding: title, direct labels, annotation, reference line, a window chosen for its story |
| 71–80 | Misleading figures: proportional ink; circles sized by radius and bars; a pie in perspective and bars; a running total and each year's count; years as equal steps and on a time axis |
| 81–88 | A first plot, in code: Figure and Axes, every hour, the histogram, its range and bin width, the bin width live, saving |
| 89–98 | Beyond two axes: heatmap, surface, contour lines, ten years in 3D and as ten panels, four variables in a 3D scatter, still and turning, parallel coordinates, the animation of the months |
| 99–104 | Classics and maps: Nightingale's roses, Minard's map, the bubble chart (live), Maunga Whau as a surface and a contour map (live), CERN's accelerators to scale and as a schematic |
| 105–108 | Checklist, every choice in the two figures, recap |

| Skip | Slides |
|--|--|
| Label size, coordinate system, aspect ratio | 17–19 |
| The pair plot | 42 |
| Many points: hexagonal bins | 44 |
| A pie in perspective and its bars; years as equal steps and on a time axis | 75–76, 79–80 |

- **Do not cut** slides 3–5 (the question and the two figures that answer
  it) or slides 82–87, which draw the opening figures in code. The seminar
  uses the same calls, `subplots`, `plot` and `savefig`, on open data.
- **Do not cut** slide 107 (Every Choice in the Two Figures), the closing
  slide: both figures, with the choice behind each part of them.
- **Do not cut** slides 11–13 (the error bar, χ² and the pulls: some of
  the room meet them for the first time on slide 10), 24–26 (bars from zero
  and the lie factor), 36 (the boxplot and the median) or 48 (error bars
  and the standard error): Lecture 8 returns to the histogram, the spread
  of the values and the standard error, Lecture 9 to the fit, χ² and the
  pulls.
- **Every figure fills the slide**: a single plot beside its caption, a
  figure of several panels under it. A caption is one line or a few short
  fragments; the explanations, the code of the advanced figures and the
  extra numbers are in the speaker notes (`Say:`, `If asked:`). Slides
  83–87 show each script with the figure it makes; nothing is opened beside
  the deck. Slide 85 is the reasoning between the default histogram and
  the chosen one.
- **Slides 47, 59, 64 and 70** are pairs drawn from the weather log, the
  mistake on the left, the repair on the right; most pairs of the gallery
  work the same way. **Slides 73–80** are four pairs on two slides each,
  the misleading figure first, the honest one of the same data next, each
  with its lie factor. **Slides 93 and 94** are a pair too: the ten years
  stacked in 3D hide the gap of July 2019, the ten flat panels show it.
- **Slides 15, 24 and 27** show the mistake first and the repair or the
  explanation on the next click, and slide 6 the numbers first and the four
  plots on the click: ask the room before clicking. Slide 85 shows the three
  bin widths on the first click and the conclusion on the second. Ask the
  question of slide 3 for a show of hands; slide 5 answers it, the counts
  written on the figure.
- **Slide 10** (The Parts of a Figure) builds a figure of the D⁰ mass peak (the
  first 1500 rows of the LHCb file `D0_KPi.csv`, counted in bins of 3 MeV/c²)
  up in six clicks: the points, their error bars √n, the fitted Gaussian on a
  straight line with its two components and its result, the known D⁰ mass with
  annotation, legend and title, the pulls in the lower panel (its frame is
  there from the first click), and the names of its nineteen parts. The slide
  has no heading: the figure covers the whole screen, and the deck's two
  buttons lie over its top right corner, which the figure leaves free.
  Slides 11–13 take its numbers one part at a time: the bar of the top bin,
  95 ± 9.7, against the same count in the other 60 blocks of 1500 rows of
  the file; the 30 distances that χ² adds up, for the fit (24.3) and for the
  same curve moved by 5 MeV/c² (56.0); the pulls of the fit against those
  of the straight line alone.
- **Slides 25, 45, 57, 86, 96, 98, 102 and 103 are interactive figures**
  that work offline: drag where the bar axis starts (25), the smoothing
  window (45), switch the palette of the day-and-hour grid (57), drag the
  bin width from 10 °C to 0.05 °C and press "0 to 2 °C" (86), drag the
  four-variable scatter to turn it (96; it turns slowly by itself until the
  first drag, a double-click brings back the start), step through the
  months or pause on one (98), let the bubble chart play and drag its year
  (102), turn Maunga Whau and press MAP (103). Use them on the projected
  window, not in the presenter view.
- **Slide 61** runs Python in the browser, the figure beside the code. The
  first run downloads the Python runtime, so run it once before the lecture.
- **Slides 83, 84 and 87** highlight the code in steps.
- **Slides 109–114** (For the Curious) are for time left at the end or for
  students afterwards. **Slides 115–123** (In Matplotlib) are the code of the
  weather-log figures, for after the lecture: slides 116 and 118 go from the
  loop to its result in one click, the others highlight their code in
  steps; slide 123 runs the bin width live.

Before the session, start the local copy of the slides: `node
scripts/serve-local.mjs 8123`, then open
`http://localhost:8123/07-data-visualisation/`.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 125–139: fifteen quiz slides for students to try afterwards. The same
questions, with their answers:

1. Four tables give the same mean of x, the same mean of y, the same closest
   straight line and the same *r*. What comes before any of these numbers is
   used?
   *A plot of each table. The same numbers can come from a line with scatter,
   a curve, a line with one point off it, or a column of points with one far
   point. This is Anscombe's quartet.*
2. A bin of a histogram holds 400 counts. If the measurement were repeated
   many times, where would about two in three of its counts land?
   *380 to 420: a count of n changes by about √n from one repetition to the
   next, √400 = 20. About 19 in 20 land inside twice that, 360 to 440.*
3. A curve with 4 free numbers is fitted to 40 bins and gives χ² = 108. What
   does χ²/ndf say?
   *ndf = 40 − 4 = 36 and 108 / 36 = 3: the curve misses the points by more
   than their error bars (look for a pattern in the pulls), or the bars are
   too short. With the right curve and bars χ²/ndf is near 1.*
4. A script calls `ax.hist(v, bins=40, range=(100, 300))`. How wide is one
   bin?
   *5 units: the range of 200 units is cut into 40 bins.*
5. A column holds 20 000 values between 200 and 300, with a peak about 8
   units wide. Which binning shows the shape of the peak: 5 bins of 20, 50 bins of 2,
   10 000 bins of 0.01, or 10 bins between 0 and 1000?
   *50 bins of 2 units. The peak covers 4 bins and a bin holds 400 values on
   average. Wider bins swallow the peak, and bins of 0.01 hold 2 values each
   and show chance.*
6. The mean of ten years of hourly temperatures is 7.16 °C. With 1 °C bins,
   3848 hours lie at −1 to 0 °C, 2706 at 7 to 8 °C and 3032 at 11 to 12 °C.
   What does this say about the mean?
   *The hours form two peaks, near −1 °C from November to March and near
   12 °C from April to October, and the mean lies between them, in the dip,
   where fewer hours are. A mean is the
   balance point of the values, not the most common one.*
7. A sensor records tenths of a degree. A histogram of its values uses bins
   0.05 °C wide. What does it show?
   *About every other bin empty: from 0 to 2 °C the sensor can record 21
   values, and 40 bins cover that range. The bars show the rounding, not the
   weather.*
8. A figure shows the days of the year across, the hours of the day up, and
   the mean temperature of each cell as a colour. How many variables does it
   show, and which is read least exactly?
   *Three: two positions and a colour. The temperature of one cell, because a
   colour is read less exactly than a position; the pattern across many
   cells is what the heatmap shows well.*
9. From the cold 2017 to the warm 2023 the yearly mean rose by 1.8 °C. What
   should a figure of the station's yearly means show?
   *All ten years, with the mean of all hours as a reference line. Two years
   picked for their values make any trend: 2017 to 2023 gives +1.8 °C, 2023
   to 2025 gives −2.3 °C.*
10. Two bars show the values 50 and 52, and the value axis starts at 48. How
   does the second bar look next to the first?
   *Twice as long: the bars are 2 and 4 units long. The values differ by
   4 %.*
11. An infographic draws the values 100 and 200 as two circles whose radius
   follows the value. What is Tufte's lie factor?
   *3. The data grow by (200 − 100) / 100 = 1; the radius doubles, so the
   area grows four times, an effect of 3 in the figure; 3 / 1 = 3. With the
   area following the value it is 1.*
12. Measured values run from 10 to 10 000 000 across categories. Which y-axis keeps the small
   and the large values apart?
   *A logarithmic axis. Each factor of ten takes the same length. On a linear
   axis everything below 100 000 lies in the lowest hundredth.*
13. Nine measurements of a temperature have a standard deviation of 0.3 °C.
   What is the standard error of their mean?
   *0.3 °C / √9 = 0.1 °C.*
14. A map shows how far the temperature of each region lies below or above
   the long-term mean, from −3 °C to +3 °C. Which palette fits?
   *A diverging palette: one hue for each sign, and a neutral colour at
   zero.*
15. A figure is made with `figsize=(6, 4)` and saved with `dpi=200`. How
    many pixels does the PNG file have?
    *1200 × 800: the size in inches times the pixels per inch.*

## Paired seminar

[Seminar 7 · Visualisation](../seminars/seminar_07.md) is a showcase, then a problem. The lecturer runs four complete Matplotlib scripts, each fetching open data from its public address: a week of the hourly temperature and humidity of Vilnius in two panels on one time axis; the hours of July 2025 with the spread of the days and the standard error of their mean; CO₂ at Mauna Loa, five months cut from the record beside the whole record; life expectancy against income of 142 countries on a linear and a log axis. A library card lists the calls. Then the room, in pairs and with any tools, an LLM too, answers from the daily record of the Vilnius station since 1881 (NOAA GHCN-Daily) whether Vilnius has got warmer and by how much, and shows its figures.

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
| Plot the Pendulum Table; Add Points, Labels and Units | Replaced by slide 83, and slides 116–117 of In Matplotlib | Every hour of the weather log, then at its time with `datetime`, with labels and units |
| A Histogram Counts Values in Bins; The Range and the Bin Width; The Mass Column as a Histogram | Rebuilt on the temperatures, slides 84, 85 and 87 | The bin widths are 10, 1 and 0.05 °C; the last one shows the rounding of the station |
| A Peak on a Flat Background, Live | Replaced by slide 86, Choose the Bin Width, Live | It used NumPy; `random.gauss` draws cold and warm hours in tenths, and the figure is drawn beside the code |
| A Minimal Bar Chart | Replaced by slide 119 | The hours below 0 °C per year: a count, with a true zero |
| Points and a Formula Curve | Replaced by slide 120 | The yearly means against the mean of all hours: two layers and a legend |
| Counts with Error Bars | Replaced by slide 121 | The monthly means with an annotation and a title that states the finding |
| Legends for Colour, Size and Shape; The Treemap; Trend and Seasonal Cycle | Parked (5 Nov 2026) | On the skip list already; out to keep the deck in its time band after *Beyond Two Axes* came in |
| The Ridgeline Plot; Temperatures as a Heatmap | Parked (7 Nov 2026) | Synthetic examples that a figure of the weather log now covers (the month histograms, the heatmap of day and hour); four good-and-bad pairs came in |
| The Dot Plot (five films) | Parked (8 Nov 2026) | Replaced by the life expectancy of 26 countries in three steps, alphabetical, sorted bars, sorted dots (slides 31–33): the lecturer asked for the busier dot plot that went from bad to good |
| Bin widths of ages, the empirical CDF, bubble chart, overlapping points, hexagonal bins, correlation heatmap, pair plot, slopegraph, square-root scale, a reference line (genes); the surface, the 3D scatter and the LHCb 2D histogram | Moved to For the Curious (9 Nov 2026) | Students found the lecture too complicated: new datasets, statistics (*r*, √*N*) and particle physics left the main path, which then estimated 131 min |
| The code of the hands-on figures: `weather.hours`, `weather.group`, the frost bars, the yearly and the monthly means, one style for all figures | Moved to In Matplotlib, slides 115–123 (9 Nov 2026, evening; since 10 Nov each reads `weather.csv` itself, without `weather.py`) | The lecture teaches the idea, the seminar the tool; the code stays as a reference for after the lecture |
| Visualising Uncertainty | Split into slides 48 (error bars, the standard error computed) and 49 (a band or many lines) (9 Nov 2026, night) | One idea per slide |
| Bin widths of ages, bubble chart, pair plot, overlapping points, hexagonal bins, slopegraph, a reference line; the surface, the 3D scatter, the scatter turning; Linear or Logarithmic, Live | Back on the main path, slides 34, 41–44, 46, 69, 91, 95, 96 and 61 (9 Nov 2026, night) | The lecturer asked for laconic slides, one line or a few fragments each; these figures, with no new statistics, keep the lecture at its two hours. For the Curious keeps the statistics and the LHCb file |
| Roadmap for this Lecture | Removed | It repeated the learning objectives |
| Q–Q Plots | Removed | It needs the Normal distribution and quantiles, not taught before Lecture 8 |
| Quantile Dot Plot | Removed | It needs probability, which Lecture 8 begins |
| The Seminar Dataset | Removed | The histogram of `weather.csv` is made on slides 84–87 |
| Practice Exercise | Removed | The room builds a figure step by step in the seminar |
| The Mental Model | Replaced by slide 82, in the code section | Matplotlib is introduced before it is used |
| Scatter with a Fit | Replaced, now by slide 120 | The room has no fitting yet |
| Histogram + Density Overlay | Replaced, now by slide 87 | It used SciPy |
| Further Reading | Parked; the list is below | Slide 107 answers the opening slide in its place |

## Further reading

- **C. O. Wilke**, *Fundamentals of Data Visualization*, free online at
  clauswilke.com/dataviz: the source of most figures in this lecture.
- **W. S. Cleveland**, *The Elements of Graphing Data*: the ranking of visual
  channels.
- **A. Cairo**, *The Truthful Art*: charts and maps for a general reader.
- **E. R. Tufte**, *The Visual Display of Quantitative Information*: the
  data-ink ratio and the lie factor.
- **C. T. Bergstrom and J. D. West**, *Calling Bullshit*: the principle of
  proportional ink, with misleading figures and their repairs.
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
- The ink of a mark is in proportion to its value: a circle's area, not its
  radius. Tufte's lie factor, the effect a figure shows divided by the
  effect in the data, is near 1 for an honest figure; a running total, a
  pie in perspective or years drawn as equal steps can give a lie factor
  far from 1, even of the wrong sign.
- An error bar on a count n is ± √n: about two repeats in three land inside
  it. A fitted curve is the one with the smallest χ², the squared distances
  to the points counted in error bars; its pulls lie mostly within ±1, and
  χ²/ndf near 1 says that the curve and the bars agree.
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
