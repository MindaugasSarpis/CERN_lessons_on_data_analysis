# Seminars: a showcase, then a problem (10 November 2026, evening)

## 1. What the lecturer asked for

After Lecture 7 and Seminar 7, 10 Nov 2026:

> "Ok, lecture and seminar 7 delivered. Lecture was ok, maybe could have
> been a bit more textbook content, a few more examples of misleading or
> bad plots and then good ones. Also where we introduce error bars and
> things some people see it for the first time. Need an explainer slide of
> what they are. The seminar we just went to write our own plotting script
> bit by bit, I ran out of steam a bit and also forgot how to manage axes in
> matplotlib. It would be a good idea for this and all seminars to have a
> bit of a showcase with real examples, libraries and so on and then hand
> over to the students a problem they try to solve). They will all use
> claude and other LLMs so should be not just plain programming but more
> focus on ideas, intuition. Please implement everywhere. Also the planned
> improvements to the course can now be deployed."

## 2. Why

- Two hours of typing one script line by line tire the person at the front
  and leave no room for the idea. The lecturer had to recall Matplotlib's
  calls for axes from memory in front of the room.
- Students write code with Claude and other LLMs. Typing syntax from a page
  teaches what the LLM does anyway; what it does not give them is the idea:
  what to ask, what to expect, how to tell a right answer from a plausible
  wrong one.
- A real example made with the real library shows what the tool is for
  before anyone types a line.

## 3. The shape of a seminar page (decided)

120 minutes, four parts. Times are hidden clock comments, as before.

| Part | Minutes | Who works | What |
|--|--|--|--|
| 1 · Set up | ≤ 15 | everyone | a new, empty folder; the conda environment and this week's package |
| 2 · Showcase | 35–45 | the lecturer runs, the room watches and may type along | three to five complete, real examples on real open data, each showing one idea of the lecture |
| 3 · The problem | 45–55 | students in pairs, LLMs allowed and expected | one real question on a real open data set |
| 4 · Show and discuss | ≈ 15 | two or three pairs show, the room answers | what the answers have in common, where they differ, the idea in one sentence |

Then, as before: `## Optional, if the room is fast` (a second problem, or
the same question on the student's own project data) and
`## Aims practised`.

### 3.1 Part 2 · Showcase

- **Complete examples, run as they stand.** Each example is one script of at
  most about 25 lines that runs in the empty folder: it types its data or
  fetches it from an openly available data set at its public address. The
  lecturer copies it from the page, runs it, and talks over the result; no
  example is built up line by line.
- **Real libraries in their real use**: the week's library first
  (Matplotlib, pandas, NumPy, SciPy, scikit-learn, pytest, …); another
  library only where the example is about the ecosystem, and then named as
  such.
- Each example on the page: a heading that says what it shows; one line
  with the idea; the code; its real output (printed lines, or the figure as
  an SVG beside the page); **Notice:** one line; **Ask the room:** one
  question about intuition (what will change if…, which of the two…, why is
  this number…), its answer folded.
- **A library card** closes the showcase: the ten to fifteen calls the
  examples used, one line each (call, what it does), so that nobody has to
  remember them (the lecturer on Matplotlib's axes).
- At least one example shows a common mistake next to its fix when the
  week's idea has one (a misleading figure, a mean without its spread, a
  fit that only looks good, a test that passes for the wrong reason).

### 3.2 Part 3 · The problem

- **One real question** that the week's idea answers, on a real open data
  set at its public address (source and licence on the page). The weather
  thread continues where it can: the Open-Meteo archive gives the real daily
  or hourly weather of Vilnius since 1940 (CC BY 4.0); other open sets where
  they show the idea better (NOAA's Mauna Loa CO₂, NASA GISTEMP, CERN Open
  Data, Rdatasets, Our World in Data), each checked to answer from its
  address on the day the page is written.
- **LLMs are expected.** The page says so in one line. The work is the
  idea, not the syntax. Every problem has the same four steps:
  1. **Predict** before any code: write down a guess (a number, a shape, a
     yes/no) and one reason.
  2. **Solve** with any tools, an LLM included.
  3. **Check the machine's work** with two or three checks an LLM cannot do
     for you: one number computed by hand on five rows; the unit, the axis,
     the error bar or the sample size read off the result; the answer set
     against the prediction, and if they differ, why.
  4. **Hand in** one figure or one number with its uncertainty and two
     sentences in your own words, ready to show in Part 4.
- Two or three folded hints (`??? tip`), then a folded worked solution with
  its real output (`??? note "One solution"`) that the lecturer can show.
- A variant for a student with project data: the same question on their
  own file.

### 3.3 What stays

Everything in class, no homework; Miniforge and conda environments
(`environment.yml` by `conda env export --from-history`); zsh on macOS and
Git Bash on Windows, `python`, never `python3`; a new, empty folder made in
class and **no handed-out zip, module or script**: data is typed from the
page or fetched by the code from an open data set's public address, with
its source and licence named (the rule of 10 Nov, morning, which this one
keeps); every output from a real run; short steps, few boxes, the HSF look
for setup steps; `<!-- ~120 min -->` under the header for `pnpm timing:check`;
`{ #anchor }` ids that other pages link to kept where the section survives;
headings that pass the `writing-lecture-slides` test; no "made up" labels;
a student's semester project is their own.

### 3.4 What changes

- Recipe rule 7, "a very gradual build-up, one new thing per section"
  (10 Nov, morning), is replaced by §3.1 and §3.2. Gradual steps stay for
  setup and for a tool's very first contact in Seminars 1, 3 and 4 (VS Code,
  the terminal, the first install), inside Part 1.
- Weeks 8–12 spec §3.2 ("one step at a time … for someone who writes code
  for the first time"): the week's library is now met through complete
  examples in the showcase and used in the problem. "Your project" becomes
  the variant of the problem and the optional part.
- The zips `weather-s08` … `weather-s12` are not made or uploaded; the
  `analysis` environment of weeks 8–12 is created in Part 1 of each page
  with one `conda create` line (a student who missed a week loses nothing).

## 4. The lectures (decided)

- **Lecture 7**: an explainer slide where a figure first shows something the
  room may not know: the error bar (what its length is, with the numbers:
  √n for a count, s/√n for a mean), the fitted curve, the pull or residual
  panel; more bad-then-good pairs (misleading figure, then the honest one
  of the same data); a little more textbook content between them (why a
  channel misleads, with its numbers). Within the timing band.
- **Every deck**: anything a figure shows for the first time (an error bar,
  a fit, a residual, a log axis, a density, a CDF, a box plot's whiskers, a
  confusion matrix, …) gets its explainer on or right before that slide.
  Decks 08–12 before they are released; 01–06 in the same pass.

## 5. The planned improvements (decided by the lecturer: deploy)

Batch 3 of `docs/superpowers/plans/2026-11-09-implement-all.md`, which
waited for the end of Lecture 7: fade transitions; larger type for projector
and phones; monochrome icons for emoji in card headings; readable slide
sources (named layouts); KaTeX click-stepping in decks 08–12; the toolkit's
video addon in Lectures 1, 2, 3 and 15; Lecture 1's live particle cover;
fact citations. Also the items set aside "until after the lecture": the
interactive components in the figures' typeface, Lecture 7's For the
Curious slides without `weather.py`, the two gallery figures redrawn at
their box size, a content hash in figure URLs.

## 6. Order of work

1. Seminar 7 (the model, just taught) and Seminar 8 (17 Nov) in the new
   shape; Lecture 7's additions; Batch 3's theme changes in a worktree.
2. Seminars 9–12, then 1, 3–6 and 14–16, from the model.
3. The rest of Batch 3, the explainer audit of the other decks.
4. Each part deployed when its gates pass; a deck change never while a
   lecture is running (Tuesdays 15:05–17:00 EET).

## 7. Left to the builder

The examples, data sets and problems of each week; how many examples
(three to five); the exact split of minutes within the bands; the variant
for project data.
