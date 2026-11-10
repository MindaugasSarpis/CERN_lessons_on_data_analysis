# Seminar page recipe

How a seminar page in `lectures/workbook/docs/seminars/seminar_NN.md` is
laid out. The page is read live, on a second screen, by the person at the
front of the room, who has no time to read paragraphs between the steps.
[Seminar 7](../lectures/workbook/docs/seminars/seminar_07.md) is the worked
example (since 10 November 2026; Seminar 6, from 13 October, and Seminar 3
were the earlier ones).

Written on 6 October 2026, after Seminar 3: the lecturer opened a page of
500 lines, could not see at once what to do, and taught the terminal for
two hours instead. Rewritten on 13 October 2026, after Seminar 4: "too much
text, the steps are not clear, too many boxes"; "the steps should be short
and coherent, I don't have the time to read long descriptions between the
steps and orient myself". Adjusted on 18 October 2026: "make sure seminar is
self contained […] Look at python.org or hsf trainings for the type of
tutorials I like", "just make the seminars look like hsf a bit", and "don't
need the run sheet in the seminar, it clutters the text" (the run sheet
table at the top of every page was removed). Seminar 5 (18 Oct) is the
model for the HSF look.
Extended on 10 November 2026, the day of Seminar 7: every page builds up
very gradually from an empty folder and hands out no file (rules 2 and 7).
Changed the same evening, after Seminar 7 was taught (rule 7 and the
layout): a page is a showcase of complete, real examples run by the
lecturer, then a problem the students solve in pairs, LLMs included. Spec:
`docs/superpowers/specs/2026-11-10-seminars-showcase-then-problem-design.md`.

## Rules

1. **Everything happens in class.** No homework, no "done at home". What
   does not fit in 120 minutes is an optional section at the end.
2. **One question, one project.** Every seminar works on the weather
   project (`weather-project`, the same files as the lectures) and answers
   one question about it, stated in the goal line. The title is only the
   number and one or two words of its lecture, `# Seminar 5 · Python`, and
   the nav says `S5 Python` (lecturer, 18 Oct 2026: the question titles
   "look weird").
   **Every seminar is self-contained** (lecturer, 18 Oct 2026: "without
   carry over of files. Especially if someone skips a seminar, and it's
   also easier for me"). **No seminar hands out files** (lecturer, 10 Nov 2026: "very
   gradual and without downloading files (prioritize this approach in all
   of the seminars for future reference) if we do need a file, let's
   eventually use some openly available data set so we don't have to add it
   to resources. This in my opinion will be much cleaner. Already having
   data makes it look very complicated."). Section 1 makes a new, empty
   folder and, when the seminar needs packages, a conda environment typed
   with `conda create`. Data is typed from the page (a list, a small CSV
   file) or fetched by the code itself from an openly available data set
   at its public address, with its source and licence in one line (the
   Open-Meteo archive for Vilnius's real weather, CC BY 4.0, NOAA's Mauna
   Loa CO₂, NASA GISTEMP, CERN Open Data, Rdatasets, Our World in Data). No `weather-sNN.zip`, no ready-made project, module
   or script, nothing added to the course's resources. Since 10 Nov 2026
   no page starts from `weather-sNN.zip` (the rule before that date:
   release `seminar-files` of
   [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project/releases),
   made by `misc/weather_repo/seminar_zips.py` from
   `misc/weather_repo/starts/sNN/`, now unused). No file or environment comes from an earlier session, no
   `git pull course main`, no pushes to the student's GitHub outside the
   Git seminars (6 and 13). Seminar 6 still clones the course repository,
   because cloning is its lesson.
   **Seminars 1 to 5 download nothing** (lecturer, 20 Oct 2026: "it's best
   not to have prerequisite files needed (at least up until 5) it's better
   to define a small list or smth directly. Even a small csv file with a few
   lines. It's cleaner that way and people don't have to download
   anything."). Since 10 Nov 2026 (a showcase, then a problem) a page of
   Seminars 1 to 5 may open a real open file where the file itself is the
   lesson, saved from its public address with the browser (Seminars 1 and
   3, before the room has a shell) or `curl`; nothing the session needs to
   start is downloaded. The student makes the folder and types the data from the
   page: a Python list where values are enough, else the same short
   `weather.csv`, six real hours of the log, the evening the temperature
   sensor failed:

       time,temp_c,humidity_pct,wind_ms
       2019-07-21T20:00,27.3,63,4.5
       2019-07-21T21:00,25.6,65,4.0
       2019-07-21T22:00,24.6,68,3.5
       2019-07-21T23:00,23.6,74,3.4
       2019-07-22T00:00,-999,76,3.2
       2019-07-22T01:00,-999,81,3.0

   (mean 25.275 without the `-999` rows, −316.15 with them), and, where
   needed, the 11 lines of `daily_export.csv`. The full log's facts
   (87 672 rows, the mean 7.16 °C) appear in one sentence at most, never
   as something the room opens. Where byte counts matter, a step checks
   `LF` in VS Code's status bar (Windows saves a new file with CRLF).
   Software installs and a network call that is the lesson (Seminar 5's
   weather service) stay.
3. **Installs at the start.** Anything the seminar needs installed is
   section 1.
4. **Short steps, a light tutorial look** (as in the
   [Python Tutorial](https://docs.python.org/3/tutorial/introduction.html)
   and [HSF Analysis Essentials](https://hsf-training.github.io/analysis-essentials/python/README.html)).
   A step is the instruction plus at most one or two sentences on what to
   notice, then one block. Interpreter work is one ```pycon block with the
   typed lines and Python's answers together; a terminal line and its
   output share one ```text block (`$ ` before the typed line); a script
   or notebook cell is followed by its output. Every idea is explained on
   the page where it is first used, never "as in the lecture": the page is
   taught from alone. No long paragraphs between steps. A section opens with one line under its heading, the
   hidden clock and minutes (an HTML comment, for planning only: the
   lecturer does not want times on the page) and one sentence of purpose:
   `<!-- 0:20 · 10 min -->`, a blank line, `A commit is one saved state: id, author, date, message.`
5. **Few boxes.** A setup section ends with one **Check:** line in bold
   (not a box); a showcase example ends with **Notice:** and **Ask the
   room:** and its folded `??? note "Answer"`; the problem of Part 3 takes
   the place of the Tasks of earlier pages. A warning box only for the one slip that stops the
   room (a pager, a missing install), at most one per section. No "what to
   skip" boxes, no "Tell the room" paragraphs, no "How to use this page".
6. **Real outputs.** Every output was printed by a real run (zsh,
   Git Bash, Python of the course). Ids, dates and timings that differ
   per laptop are marked once: "Your ids differ".
7. **A showcase, then a problem** (lecturer, 10 Nov 2026, evening, after
   Seminar 7: "The seminar we just went to write our own plotting script
   bit by bit, I ran out of steam a bit and also forgot how to manage axes
   in matplotlib. It would be a good idea for this and all seminars to have
   a bit of a showcase with real examples, libraries and so on and then
   hand over to the students a problem they try to solve). They will all
   use claude and other LLMs so should be not just plain programming but
   more focus on ideas, intuition."). Four parts:
   - **Part 1 · Set up** (≤ 15 min): the new, empty folder; the conda
     environment and the week's package. Here, and only here, steps stay
     small and gradual (a tool's first contact in Seminars 1, 3 and 4).
   - **Part 2 · Showcase** (35–45 min): three to five complete examples the
     lecturer copies from the page and runs. Each is one script of at most
     about 25 lines that runs as it stands in the empty folder (data typed,
     or fetched from an open data set's public address), made with the
     week's real library, and shows one idea of the lecture. On the page:
     a heading that says what it shows, one line with the idea, the code,
     its real output (printed lines, or the figure as an SVG in
     `seminars/img/sNN/`), **Notice:** one line, **Ask the room:** one
     question about intuition with its answer folded. Where the idea has a
     common mistake, one example shows it next to its fix. The part ends
     with a **library card**: a table of the ten to fifteen calls the
     examples used, one line each, so nobody has to remember them.
   - **Part 3 · The problem** (45–55 min): one real question the week's idea
     answers, on an open data set at its public address (source and
     licence named), in pairs, with any tools, LLMs included (the page says
     so). Always four steps: **Predict** (a guess and one reason, before
     any code); **Solve**; **Check the machine's work** (two or three checks
     an LLM cannot do for you: a number by hand on five rows, the unit,
     axis, error bar or sample size read off the result, the answer against
     the prediction); **Hand in** (one figure or one number with its
     uncertainty and two sentences in your own words). Two or three folded
     hints (`??? tip "Hint 1"`), then a folded worked solution with its
     real output (`??? note "One solution"`). A variant for a student with
     project data: the same question on their own file.
   - **Part 4 · Show and discuss** (≈ 15 min): two or three pairs show their
     answer; two or three questions for the room with folded answers; the
     idea in one sentence.
   [Seminar 7](../lectures/workbook/docs/seminars/seminar_07.md) is the
   worked example (rebuilt 10–11 Nov 2026).

## Layout

```text
# Seminar NN · Topic

**Paired lecture:** NN Title · **Format:** a showcase, then a problem, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's question:** one real question, answered in Part 3.

One sentence: where the typing happens.

**If time runs short:** one sentence (which showcase example to leave out).

??? info "Before the session"   (room, you, the data's addresses: short bullets)

---

## Part 1 · Set up { #part-1 }

### 1. Make the folder and the environment { #start }

<!-- 0:00 · 10 min -->

1. One line of instruction.

    ```text
    $ the line typed
    its output
    ```

**Check:** the result the room should have.

---

## Part 2 · Showcase { #part-2 }

One sentence: the lecturer runs these, the room watches.

### 2. What the example shows { #anchor }

<!-- 0:15 · 8 min -->

The idea in one line.

```python
complete script, ≤ ~25 lines, runs as it stands
```

```text
its printed output
```

![What the figure shows](img/sNN/name.svg)

**Notice:** one line.

**Ask the room:** one question.

??? note "Answer"
    Two or three lines.

### 6. Library card { #card }

| Call | What it does |
|--|--|
| `ax.set_xlim(0, 12)` | the range of the x axis |

---

## Part 3 · The problem { #part-3 }

### 7. The question { #problem }

<!-- 0:55 · 50 min -->

The question, the data's address, its source and licence. Work in pairs;
any tools, an LLM too.

1. **Predict.** …
2. **Solve.** …
3. **Check the machine's work.** …
4. **Hand in.** …

??? tip "Hint 1"
??? tip "Hint 2"
??? note "One solution"   (code, real output, figure)

**With your own project data:** the same question on your file.

---

## Part 4 · Show and discuss { #part-4 }

### 8. Two or three answers { #discuss }

<!-- 1:45 · 15 min -->

**Ask the room:** … ??? note "Answer"

The idea in one sentence.

---

## Optional, if the room is fast { #optional }

## Aims practised
```

- The comment `<!-- ~120 min ... -->` under the header line must stay:
  `pnpm timing:check` reads it (a week with a `split` in decks.json, such as
  week 5 at 60 + 180, declares its seminar minutes). No clock or minutes
  are visible anywhere on the page.
- Parts are `##`, sections are `###`, a `---` rule separates them. Keep
  every `{ #anchor }` that another page links to.
- End with `## Aims practised` (three bullets). No "Stretch goals" or
  "If students ask for more" lists: an extra is an optional section.
- A showcase figure is the SVG the example's own code saved, copied to
  `lectures/workbook/docs/seminars/img/sNN/` (vector, as on the slides);
  the code on the page and the code that made the figure are the same.

- When a step differs by system, put each variant in a tab, inside the
  numbered step and indented with it:

    ```text
        === "macOS"

            ```text
            python3 --version
            ```

        === "Windows"

            ```text
            python --version
            ```
    ```

  macOS comes first, Windows second, on every page. The terminal is `zsh`
  on macOS and Git Bash on Windows (since 13 Oct 2026); a line both shells
  take stands once, outside tabs, which is almost every line. Keys stay inline in
  the old form: `Ctrl+S` (macOS `Cmd+S`).
- Optional sections keep the full layout and live in a last part,
  `## Optional, if the room is fast`.
- The extensions for tabs and collapsed boxes (`pymdownx.tabbed`,
  `pymdownx.details`) are switched on in `lectures/workbook/mkdocs.yml`.
  Check a page with `mkdocs build --strict -f lectures/workbook/mkdocs.yml`.
