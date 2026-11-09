# Weeks 8–12: the lecture teaches the idea, the seminar the tools

Date: 9 November 2026. Status: approved ("Implement and deploy", 9 Nov,
evening), with the decisions of section 12.

This brief replaces, for weeks 8 to 13, the order and the per-lecture
paragraphs of `2026-10-04-course-rework-first-principles-design.md`
(sections 2, 3 and 8) and the week-8 part of
`2026-11-05-visualisation-before-numpy-design.md`. Everything else in those
two files, and every convention in `CLAUDE.md`, still holds.

## 1. What the lecturer asked for

In his words, on 9 November 2026, after a review of every lecture and
seminar:

- "I feel like we need to integrate a bit more statistics, machine learning
  and other content in the lectures and things like "numpy" leave for the
  seminars. So a bit more textbook-like -> introduce a perceptron, introduce
  simple classification, parameter estimation and fitting (so it's not as
  black-box as people now look at it). Introduce concepts like modularity,
  reproducibility, object oriented code, but only in seminars present real
  libraries and so on. Now it's a bit of a mix. Also we would like to go all
  the way to LLMs so people understand better how to prompt them."
- Asked whether this applies to the five Tuesdays left this year or to next
  year's run: "yes, we need to show the mathematical expressions but then
  always propagate a real number or a list through say a perceptron." Read
  as: this year, from week 8.
- "But the seminars should be very gradual, like python.org or hsf training
  courses. One step at a time, very methodical. Suitable for someone who
  works with code for the first time."
- On one conda environment for weeks 8–12 instead of a fresh one per
  seminar: "That's ok, now that we know git and stuff... but should still
  learn about environments and packages."
- "students can use llm on free account"

Earlier feedback that this brief also answers: students say the course is
"a bit too complicated" (9 Nov); "L6 was too difficult" (27 Oct); "Classes -
way too steep" (20 Oct); the seminars must be followable live, "like
python.org or hsf python tutorial" (18 Oct); and the wish of 4 Oct to
"rigorously build a perceptron, explain data fitting from first principles".

## 2. Why

A review of all 16 lectures and 15 seminar pages (9 Nov, six reviewers, each
number they checked re-run on the data) found:

1. **Five Tuesdays for six lectures.** 17 Nov, 1 Dec, 8 Dec, 15 Dec and
   22 Dec remain (no session on 24 Nov; none took place on 3 Nov). In the old
   order Lecture 13, the one the grade depends on most, had no day.
2. **Lectures 8–13 cannot be given as they are.** They are built on the
   pendulum table and the LHCb file `D0_KPi.csv`, which the room has never
   seen (the pendulum appears in no deck of weeks 1–7; the LHCb file only in
   Lecture 7's For the Curious), and they cite Lecture 4 scripts that no
   longer exist (`clean_pendulum.py`, `column_stats.py` on the LHCb file).
   Their seminars already use the weather log.
3. **A mathematical cliff.** Lectures 1–8 hold almost no formulas; Lectures
   9, 10 and 11 hold about 78, 41 and 45 displayed equations, some 20
   derivations each and a proof, and no lecture teaches a derivative, a sum
   sign, a logarithm rule or a matrix.
4. **Ideas and library tutorials are mixed.** The NumPy and Pandas decks are
   tours of an API; Lecture 13 is mostly tools (venv, pip, PowerShell, which
   contradict the course's conda and Git Bash); the analysis ideas sit
   between them.
5. **No seminar touches the student's own project**, although the project is
   the whole grade and students do no homework, so it moves forward only in
   class. Lecture 1 promises "in the seminars you write about your project
   as you go".
6. **Seminars run 20–40 min over** for a beginner room: Tasks without
   minutes, two libraries in one session, long blocks, and a fresh
   environment per seminar downloaded on the room's network (seven start
   folders, `s06` and `s09`–`s14`, install JupyterLab, which no page opens;
   four, `s06` and `s09`–`s11`, still ship the old `weather.py` with
   `class Hour`).

## 3. The rules (decided)

### 3.1 A lecture teaches the idea

- A lecture is a textbook chapter. Each idea: the question it answers, the
  mathematical expression, then **a real number or a list from the weather
  log pushed through that expression on the slide**, every value computed
  by a script, so that nothing is a black box.
- Where a step is clearer as code, plain Python on lists, as Lecture 5
  taught (`for`, `if`, `def`, a list, a dict). **No library calls on a
  lecture slide**: no NumPy, pandas, SciPy, scikit-learn, pytest. Figures
  are fine; they are scripted in `figures/src/` as before.
- A derivation on the main path ends in a number. Long derivations, proofs
  and second examples go after the Recap, in `# For the **Curious**`, which
  the timing gate counts as 0 min.
- Everything else of `CLAUDE.md` holds: the weather log as the one running
  example, self-contained decks, speaker notes as `**Do:**`/`**Say:**`/
  `**Ask:**`/`**If asked:**` with minutes, quizzes after the Recap under
  `# Check **Yourself**`, no wall of code, titles that pass the
  `writing-lecture-slides` test, the timing band 105–145 min, zero overflow.
  No Learning Objectives slide and no goal "quote" (the preambles removed
  from Lectures 6 and 7).

### 3.2 A seminar teaches the tools, like the Python tutorial or HSF training

- **One step at a time, for someone who writes code for the first time**: a
  line or a few lines to type, the output right after them, one sentence on
  what to notice; interpreter work as one `pycon` block with input and
  output. The layout of `docs/seminar-page-recipe.md`, model
  `seminar_05.md` and the Seminar 7 of 9 Nov.
- **At most one new library per seminar**, introduced from its first line
  (`import pandas as pd`); nothing is used before the page has shown it.
- **The seminar applies the week's idea with the real library**, to the
  weather log, and reaches the numbers the lecture computed by hand.
- **The main path fits 120 min for a beginner room, setup included.** Tasks
  are optional, timed in their clock comment, with folded answers; `##
  Optional, if the room goes fast` holds the rest. A block longer than about
  ten lines is split (numbers first, then the figure). A seminar does not
  practise everything its lecture shows: the lecture carries the full idea.
- **The last part, "Your project", 15–20 min**: the same steps again with
  the student's own file name, nothing new, skipped by a student without
  data yet. It is the only place in the course where the graded project
  moves forward in class.
- Self-contained as before: each seminar starts from its own
  `weather-sNN.zip`; no file comes from an earlier session; no homework.

### 3.3 Environments and packages, a thread through weeks 8–12 (decided)

- One conda environment for weeks 8 to 12, created by the students in week
  8. Each seminar adds that week's package itself, one at a time: `conda
  install NAME=VERSION`, check the version, `conda env export
  --from-history -f environment.yml`, delete the `prefix:` line. Packages
  and environments are learned step by step, never handed over ready-made.
- A student who missed a week creates the environment from the zip's
  `environment.yml` with one command, so every seminar stays
  self-contained.
- Week 12 closes the thread: exact versions pinned, the environment created
  again from the file and the results rebuilt in it; Lecture 12 gives the
  ideas behind it (a dependency tree, versions, ranges and pins).
- No JupyterLab in any start folder.
- The environment's name is the builder's call; it must not clash with the
  `weather` environment of Seminar 5 or the `sNN` ones of Seminars 6 and 7.

### 3.4 The LLM part (decided)

Students use an LLM in class on a free account of their choice. The page
works with any chat LLM and says what to do without one (pair with a
neighbour; the lecturer's screen).

## 4. The calendar, 2026 (decided)

Twelve sessions; the presentations are in the exam session.

| Week | Date | Lecture | Seminar |
|--|--|--|--|
| 1 | 8 Sep | Orientation & Motivation | none |
| 2 | 29 Sep | Introduction to Data | VS Code, Markdown, the project folder |
| 3 | 6 Oct | How Computers Work | bytes in a hex editor |
| 4 | 13 Oct | Command Line & Files | the shell, a rebuild script |
| 5 | 20 Oct | Python Foundations | the interpreter, scripts, a module, conda |
| 6 | 27 Oct | Version Control | Git and GitHub |
| 7 | 10 Nov | Data Visualisation | Matplotlib |
| 8 | 17 Nov | **Data Quality and Uncertainty** | **pandas** |
| 9 | 1 Dec | **Parameter Estimation and Fitting** | **NumPy** |
| 10 | 8 Dec | **Classification and the Perceptron** | **a class of their own** |
| 11 | 15 Dec | **From Neurons to Language Models** | **a language model in plain Python; an LLM** |
| 12 | 22 Dec | **Code That Lasts** | **pytest, pinned environments, a fresh clone** |

Weeks 1–7 are delivered and stay as they are this year.

## 5. Weeks 8 to 12

The numbers below were computed on 9 Nov from
`lectures/workbook/docs/data/weather.csv` (87 672 rows, 87 552 measured
hours) or are those of the current seminar pages, re-run by the reviewers.
The builder computes every number again from the script that makes the
slide.

### Week 8 · 17 Nov · Data Quality and Uncertainty

**Question:** how sure is 7.16 °C?

Lecture, main path (my order, the builder may refine it):

1. *Is the data valid?* Missing marks, impossible values, duplicates,
   units, one rule per check with a count. The six hours of 21 July 2019,
   20:00 to 01:00 (27.3, 25.6, 24.6, 23.6, −999, −999): their mean with the
   marks and without them, 25.275; the whole log 5.78 with the marks, 7.16
   without.
2. *Describing a distribution:* the histogram of Lecture 7 again; mean,
   variance and standard deviation as expressions, the four measured hours
   pushed through them.
3. *Probability by counting:* P(frost) = 0.255 (hours below 0 °C);
   P(frost | frost the hour before) = 0.956 and P(frost | no frost the hour
   before) = 0.015, from counts.
4. *The Gaussian and the 68/95 rule,* and a check: the hours, with their two
   peaks, are not Gaussian (the builder computes the share within ±s).
5. *The standard error,* σ/√N, derived once from the variance of a sum of
   independent values: s = 8.85, N = 87 552, s/√N = 0.030.
6. *When values are not independent:* neighbouring hours are alike, so
   0.030 is too small; the ten yearly means scatter by 0.70, which gives
   7.16 ± 0.22.
7. *Correlation:* r as an expression; temperature and humidity of the hours,
   r = −0.70.

For the Curious: the binomial and the Poisson distribution, error
propagation, Bayes' rule, the probability axioms.

Sources: `09_Probability_and_Statistics.md` (reviewer, 9 Nov: keep one
derivation, σ/√N, and give the others as results with numbers; move the
axioms, the binomial and Poisson derivations, densities, N − 1, partial
derivatives and the p-value pitfalls out of the main path); the Data
Quality section of `12_Pandas_and_Data_Cleaning.md`; Seminar 9's numbers.
The LHCb examples leave the main path.

Seminar 8, **pandas**, from its first line. Main path, one step each:
create the environment from the zip's file (Python and Matplotlib-base);
`conda install pandas`, its version, write it down → `import pandas as pd` →
read the file → `head()` → one column → its mean, 5.78 → read `-999` as
missing (`na_values`) → the mean again, 7.16 → spread and count → the
standard error by hand, `s / n ** 0.5` → the mean of each month
(`groupby`) → a histogram with the Matplotlib of Seminar 7. Optional:
correlation, percentiles, the yearly means and their scatter. Your project:
the project folder (the layout of week 2), the student's file in
`data/raw`, read it, `head()`, `describe()`, one mean with its ± in the
README. Sources: `seminar_09.md` (How sure is 7.16?), `seminar_12.md` (pandas
on a messy export), `seminar_08.md` (masks, the environment step).

### Week 9 · 1 Dec · Parameter Estimation and Fitting

**Question:** is it getting warmer?

Lecture, main path:

1. A model has parameters; the mean is the value that makes the sum of
   squared deviations smallest (the four hours of week 8 pushed through).
2. From the Gaussian likelihood to least squares, χ² as an expression; two
   guessed lines through the ten yearly means and their χ².
3. The straight line in closed form: the expressions, the ten yearly means
   (7.60, 6.51, 7.97, 7.27, 6.83, 7.25, 6.60, 8.31, 7.27, 5.98) pushed
   through the five sums: −0.56 °C per decade.
4. The uncertainty of a parameter, Δχ² = 1 as a picture: −0.56 ± 0.80 °C per
   decade, so ten years cannot show a trend.
5. Gradient descent: the update rule, three steps by hand from a starting
   value, and a step that is too large.
6. A curve: the yearly cycle, a cosine with a mean, an amplitude and a
   phase, fitted to the daily means (the builder computes the amplitude and
   the coldest day).
7. Residuals and goodness of fit; too few and too many parameters.

For the Curious: the normal equations in matrix form, the covariance of
two parameters, Newton and Levenberg–Marquardt, the χ² distribution and
p-values, the D⁰ peak of LHCb (the CERN showcase), the pendulum's g.

Sources: `10_Data_Fitting.md`. A reviewer's minimum keep list for a merged
week (9 Nov, slide numbers of today): 6–10, 12–15, 22–23, 28, 39–41, 43, 45,
53–55 (redone on the yearly cycle), 60, 63–64, 70 ("Reporting a Fit", now on
the skip list and the most useful slide for projects). With a whole week,
more can stay. Teach the derivative once, where it is first used, with a
numeric check (a small nudge), as Lecture 11's slide 42 checks a gradient.

Seminar 9, **NumPy**. Main path: `conda list numpy` shows NumPy is already
there, brought by pandas, a dependency → a column as an array
(`to_numpy()`) → arithmetic on the whole array → the five sums of the
lecture → slope and intercept → `np.polyfit` gives the same numbers →
residuals → a plot of points, line and residuals. Optional: `conda install
scipy`, `curve_fit` for the yearly cycle. Your project: one straight-line
fit in the student's data, the slope in the README. Sources:
`seminar_10.md` (fix: σ = 0.70 is computed on the page, and the check
"σ matches the scatter" is not a test; the design matrix and `atan2` are
optional), `seminar_08.md` (arrays, masks).

### Week 10 · 8 Dec · Classification and the Perceptron

**Question:** will it freeze tonight?

Lecture, main path:

1. From a number to a class: frost at 06:00, given the evening at 18:00;
   the baseline "never frost" (3646 evenings, 1229 followed by frost: 66.3 %
   right) and a threshold rule.
2. The neuron: z = w·x + b and a step; one evening's temperature and
   humidity pushed through it to "frost" or "no frost".
3. The decision boundary, a line in the plane of the two inputs.
4. Rosenblatt's rule: one update with numbers; one pass of AND by hand.
5. The sigmoid: the output as a probability; the cross-entropy loss from
   the Bernoulli likelihood; its gradient (ŷ − y)·x, the same update as the
   line of week 9; one step with numbers.
6. Train on some years, test on the others; the accuracy with its ±, against
   the baseline and the threshold.
7. A model as an object: what it holds (its weights) and what it does
   (`predict`, `fit`); the class as an idea, its outline in plain Python.
   This is where object-oriented code enters the course.
8. The limit: no single line separates XOR.

For the Curious: the convergence theorem and its proof, the distance from
the line, log-odds and Bayes, the history (1958, 1969).

Sources: `11_The_Perceptron.md` (keep list of 9 Nov: 7, 9–11, 16, one AND
epoch plus 21, 27, 30, 32, 36–37, 41–43, 47, 49, 54–55, 57–59, 62; one
symbol per meaning, since L, σ and w changed meaning against Lecture 10);
`seminar_11.md` (the hand-set neuron 91.6 %, the logistic neuron 95.9 ±
0.6 % on the test years, as the rule "below 3.6 °C"); the class `Hour` in
Lecture 5's For the Curious.

Seminar 10, **a class of their own**, plain Python first. Main path: one
evening through a function `predict` → every evening and the accuracy → one
learning step → the loop → the same code as a class `Perceptron` with
`fit` and `predict`, built one method at a time. Optional: `conda install
scikit-learn`; its `Perceptron` and `LogisticRegression` take the same two
calls. Your project: a baseline for a yes/no question in the student's
data, or skip. Sources: `seminar_11.md` (fix: split the `year = ...`
one-liner; one sentence on `.T @`; keep Rosenblatt's rule in "If time runs
short").

### Week 11 · 15 Dec · From Neurons to Language Models

**Question:** what does an LLM do with a prompt?

Lecture, main path:

1. Two layers solve XOR: the four inputs pushed through a 2-2-1 network
   with weights set by hand.
2. Training a network: a loss and the chain rule; one numeric step on a
   tiny network (the derivation for the curious).
3. Text as numbers: words become ids; the simplest language model counts
   which word follows which in a short text; next-word probabilities from
   the counts; text generated by drawing from them.
4. Words as vectors: similar words, similar vectors; similarity as a dot
   product, with numbers.
5. Scores into probabilities: softmax with a temperature, three scores at
   two temperatures.
6. Context: the next word depends on the earlier ones; attention as a
   weighted average, with numbers on three words, as an idea.
7. An LLM: the same next-word prediction learned from a very large text;
   pretraining, then tuning to follow instructions; what it is not (a
   database, a calculator).
8. Prompting as a consequence: give context, an example, the format and the
   constraints; ask for code and its test; check by running; never paste
   personal data; say where an LLM was used.

For the Curious: backpropagation derived, k-means, ROC and
cross-validation (or leave these in the optional Lecture 16).

Sources: `16_Machine_Learning_and_AI.md` (the hidden layer, backpropagation,
"A Language Model by Hand", "Generating Text", "What the Model Wrote", with
the toy sentences moved to weather); the AI section of
`14_Concepts_of_Data_Analysis.md` ("What the Tool Is", "Verify Text",
"Never Paste", "Disclose"); the XOR slides of `11_The_Perceptron.md`.

Seminar 11, **no new library, then an LLM on a free account**. Main path:
split a sentence into words → count word pairs in a dict, as `group` does
→ next-word odds → generate a sentence → softmax with a temperature on
three numbers → ask an LLM to explain one small function, then to write a
test for it, and run the test to check the answer. Optional: longer
prompts, a prompt that fails and why. Your project: ask an LLM about one
function of the project, run what it wrote, add an AI-use note to the
README.

### Week 12 · 22 Dec · Code That Lasts

**Question:** will the result come out the same next year, on another
laptop?

Lecture, main path:

1. Modularity: steps as functions, functions in a module (`weather.py`),
   what goes where.
2. Objects: data with its methods, the perceptron of week 10; why library
   models are objects.
3. Tests: a test states a fact known without the code; the six hours
   pushed through `mean` must give 25.275; a failing test, read.
4. Environments and packages as ideas: a dependency tree (pandas brings
   NumPy), versions, ranges and pins, a fresh environment as the proof.
5. One command that rebuilds everything and runs the tests.
6. Delete and rebuild; a fresh clone; the checksums before and after.
7. FAIR and the four aims; the review checklist (12 questions in four
   groups: rebuild, data, method, report) as the project's self-check;
   Smiltė's 7.16 and Ben's 7.11 of Lecture 1 answered.

For the Curious: command-line arguments and a config file, rebuilding only
what changed (Make, Snakemake), continuous integration, containers.

Sources: `13_Reproducible_Workflows.md` (conda, not venv; Git Bash, not
PowerShell; `python`, not `python3`; its opening must not claim the room
has no one-command rebuild: it has had `rebuild.sh` since week 4); the
review checklist and "decide before you look" of `14_Concepts_of_Data_
Analysis.md`; `seminar_13.md`.

Seminar 12, **pytest**. Main path: `conda install pytest` → one `assert` →
the same as a test file → `pytest` runs it → a failing test, read → exact
versions pinned → one command that rebuilds and tests → delete the results,
rebuild → a fresh clone rebuilt. Your project: the same on the student's
own repository. Sources: `seminar_13.md` (fix: one "one command", the same
in lecture and seminar; replace `numbers()` with a three-line loop).

## 6. What happens to the existing files

- **Decks.** The five new lectures are built from the sources above. The
  NumPy deck (08) and the Pandas deck (12) stop being lectures: their useful
  slides feed the seminar pages, and the decks are parked (my call: parked
  in `lectures/content/parked/`, not deployed). The old 13 becomes week 12.
  Lectures 14 (Concepts), 15 (Computing Infrastructure) and 16 (ML & AI)
  stay optional extras in block E, minus the parts moved into weeks 8, 11
  and 12. File names and slugs: the builder's call, keeping the rule that
  the numeric prefix is the delivery order; decks 08–16 are drafts, so no
  live link breaks.
- **Seminar pages.** `seminar_08.md`–`seminar_12.md` are rewritten for
  weeks 8–12; `seminar_13.md`–`seminar_16.md` become optional or parked (the
  builder's call), their material reused where section 5 says.
- **Start folders.** `misc/weather_repo/starts/s08`–`s12` rebuilt: no
  JupyterLab, the functions-only `weather.py` of Lecture 7, only the files
  the page uses; zips built by `misc/weather_repo/seminar_zips.py`. Uploading
  them to the release `seminar-files` of the public repository is an
  outward step: the lecturer confirms it each time.
- **Pages.** `lecture_8.md`–`lecture_12.md` rewritten; `mkdocs.yml` nav, the
  home page's "This week", `seminars/overview.md` and `decks.json` follow.
- **Lecture 1 (live).** The Schedule slide, "The Path of the Course", "Why
  You Need These Skills" and the hours card (64 h on the card, 52 h in its
  note) are updated to section 4. Now.
- **`CLAUDE.md`.** The lecture list and the notes per week follow.

## 7. What the room knows, week by week (replaces section 3 of the 4 Oct brief)

| After | The room has | Not yet |
|--|--|--|
| 7 | VS Code, Markdown, the project folder; bytes, floats, text encodings, checksums; the shell, pipes, `grep`, a rebuild script, PATH, conda environments, `environment.yml`; Python values, lists, dicts, `for`, `if`, `def`, a module `weather.py`, `import`, f-strings and tracebacks (Seminar 5); Git's add, commit, push, history, undo, GitHub; Matplotlib from lists, histograms and bin width, choosing a chart | NumPy, pandas, classes, statistics beyond the mean, derivatives, vectors |
| 8 | data quality checks; mean, variance, standard deviation, probability by counting, the Gaussian, the standard error, correlation; pandas | fitting, derivatives |
| 9 | models with parameters, likelihood, least squares, a fitted line and its uncertainty, gradient descent, residuals; NumPy arrays | classification |
| 10 | the perceptron, the sigmoid, cross-entropy, train and test, accuracy; a class with methods | networks, text |
| 11 | a two-layer network, a language model by counting, softmax, how an LLM predicts text; prompting and checking an LLM | |
| 12 | modules, objects, tests, pinned environments, one command, a fresh clone | |

## 8. Order of work

- Week 8 (deck, seminar page, start folder, lecture page) ready and
  released by Monday 16 Nov; then each week by the Monday before it: 30 Nov,
  7 Dec, 14 Dec, 21 Dec.
- Lecture 1's schedule slides: now.
- Gates as in `CLAUDE.md`: `pnpm qa --only <slug>`, `pnpm timing:check`,
  `pnpm qa:runners` for decks with runner blocks, `mkdocs build --strict`
  in CI, and every seminar step run from its zip with its printed output
  compared, as was done for Seminar 7 on 9 Nov.

## 9. Goals, non-goals, anti-goals

- **Goals:** lectures that build statistics, fitting, classification and
  language models from their expressions, each pushed through with real
  numbers; seminars a first-time coder can follow live; one library at a
  time; environments and packages learned along the way; the student's
  project moving forward in every seminar; the course ending on the four
  aims just before the presentations.
- **Non-goals:** reworking the delivered weeks 1–7 this year (except Lecture
  1's schedule); covering every function of a library; high-performance
  computing (Lecture 15 stays optional).
- **Anti-goals:** a lecture slide that teaches an API; a derivation that
  never reaches a number; a model used as `fit()` before the room has
  computed one by hand; a seminar step that needs a file or an environment
  from an earlier week, or homework; a seminar a first-time coder cannot
  follow live.

## 10. Next run (2027), not now

From the review of 9 Nov, for the lecturer to decide later:

- Lectures 4, 5 and 7 keep their ideas (pipelines and automation; how a
  program runs, traced value by value; how a figure is read) and hand
  their commands and code to the seminars.
- Lecture 3's terminal section moves to Lecture 4; Lecture 4 ends
  shell-only, with conda in Lecture 5; Lecture 2's editing drill shrinks.
- Lecture 5 loses its detours (JSON and the web API, the Figure, the
  package-count tables) for reading a traceback, the working directory and
  f-strings; Seminar 5 fits 135 min (IDLE out, JupyterLab and the class
  optional).
- Lecture 6 versions the room's own Python scripts; Seminar 6 follows the
  lecture's order and practises the shared repository and a fork with a
  pull request in pairs.
- Every seminar from week 2 on ends with "Your project".

## 11. Left to the builder

The exact slides of each lecture within the order of section 5, the
figures, the worked numbers (computed by script), the text sample of week
11, the environment's name, file names and slugs, which old seminar pages
are parked, and the wording of every page under `CLAUDE.md` and the
`writing-lecture-slides` skill.

## 12. Decisions of 9 November, evening

The lecturer, after the outline above: "So having these ideas in mind,
review the style, flow, content of all lectures. See if the ordering is
correct. Make sure lectures are more theoretical, seminars are more
hands-on. Implement and deploy. I am giving the data visualization lecture
tomorrow, make sure it's really good, the slides should be pleasant to look
at, not too much text, just what's needed. I don't like paragraphs of text
on the slides, more laconic style, but important ideas, numbers should of
course be relayed." Then: "Also see if I can squeeze out anything good from
new slidev version or any other version. Suggest improvements to
interactivity, visuals, style, overall feel (has to be incredible)."

- **Laconic slides, every lecture (decided).** No paragraphs on a slide: a
  caption is one or two short lines, or two or three fragments with their
  numbers; the reasons and the how go into the speaker note. Every
  important number stays on the slide.
- **Lecture 7 (10 Nov) follows the rule tonight**: the code slides that
  only show calls (`weather.hours`, the hands-on section) moved to a
  reference section `# In **Matplotlib**` after For the Curious; the four-
  variable figures (contours, 3D slices against ten panels, parallel
  coordinates) joined the main path.
- **Files** (builder's calls, made): decks `08_Data_Quality_and_Uncertainty`,
  `09_Parameter_Estimation_and_Fitting`, `10_Classification_and_the_
  Perceptron`, `11_From_Neurons_to_Language_Models`, `12_Code_That_Lasts`;
  the NumPy and Pandas decks parked whole in `lectures/content/parked/decks/`;
  the optional decks keep their numbers 14–16 (no deck 13), and the cover
  takes its number from the slug, as the landing does. Blocks: A
  Foundations & Tooling (01–06), B Data & Uncertainty (07–08), C Models &
  Learning (09–11), D Reproducible Work (12), E Further Topics.
- **The environment of weeks 8–12** is called `analysis`; each start
  folder's `environment.yml` lists what the earlier weeks added (week 8:
  Python and Matplotlib-base; week 9 onward: also pandas).
- **The one command** stays `scripts/rebuild.sh` (the room has it since
  week 4); week 12 adds the tests to it as its last line. No `run_all.py`.
- **Slidev and the decks' feel**: a research review proposes upgrades and
  interactivity; nothing is upgraded before the lecturer has seen the list.

- **Interactive figures (decided)**: on the proposal "drag a perceptron's
  weights and watch its line move, change a fit's slope and watch χ²
  change, or step numbers through a formula click by click", the lecturer:
  "this sounds like a good idea". Course-wide Vue components, each showing
  the expression with live numbers pushed through it: `MeanSpread` (week 8,
  the spread of a mean against s/√N), `FitLine` (week 9, χ² of a line
  through the ten yearly means), `PerceptronPlayground` (week 10, weights,
  the boundary, one evening's z and the accuracy), `SoftmaxTemperature`
  (week 11), and a generic `FormulaSteps`. They go into the decks once those
  are built; Lecture 7 keeps its live Python block tonight.
- **The toolkit** (`slidev-videos`: the video addon, the stage, the clip
  library) and the outreach talks' theme are surveyed for what Lecture 1
  and other lectures could inherit, "to keep things uniform all across";
  proposals go to the lecturer first.
- **Interactive figures in Lecture 7 too, and back to the toolkit
  (decided).** The lecturer: "Can also do interactive ones for the lecture
  tomorrow (at least some) and feed this back to tools", then "it's a good
  feature to have". Lecture 7 gets `BinWidthExplorer` (the 87 552 hours at
  bin widths from 0.05 to 10 °C), `AxisStartBars` (where a bar axis starts),
  `PaletteHeatmap` (palettes on the day-and-hour grid) and, if ready,
  `SmoothingWindow`. Once proven in the course, the components go to the
  toolkit `slidev-videos` on a worktree branch (its main checkout never
  changes branch), for the lecturer to approve before a release.
