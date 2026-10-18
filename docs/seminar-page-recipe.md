# Seminar page recipe

How a seminar page in `lectures/workbook/docs/seminars/seminar_NN.md` is
laid out. The page is read live, on a second screen, by the person at the
front of the room, who has no time to read paragraphs between the steps.
[Seminar 6](../lectures/workbook/docs/seminars/seminar_06.md) is the worked
example (since 13 October 2026; Seminar 3 was the earlier one).

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
   also easier for me"). Section 1 is "Get today's folder": download
   `weather-sNN.zip` from the release `seminar-files` of
   [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project/releases),
   `unzip ~/Downloads/weather-sNN.zip -d ~`, `cd ~/weather-sNN`, and, when
   the seminar needs packages, `conda env create -n sNN -f environment.yml`.
   The zip holds everything: data, the finished files of earlier seminars,
   the `environment.yml`. It is made by `misc/weather_repo/seminar_zips.py`
   from `misc/weather_repo/starts/sNN/`. No file or environment comes from
   an earlier session, no `git pull course main`, no pushes to the
   student's GitHub outside the Git seminars (6 and 13). Seminar 6 still
   clones the course repository, because cloning is its lesson.
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
5. **Few boxes.** A section ends with one **Check:** line in bold (not a
   box). Each part ends with one `!!! question "Task: …"` and its
   `??? note "Answer"`. A warning box only for the one slip that stops the
   room (a pager, a missing install), at most one per section. No "what to
   skip" boxes, no "Tell the room" paragraphs, no "How to use this page".
6. **Real outputs.** Every output was printed by a real run (zsh,
   Git Bash, Python of the course). Ids, dates and timings that differ
   per laptop are marked once: "Your ids differ".

## Layout

```text
# Seminar NN · Topic

**Paired lecture:** NN Title · **Format:** follow-along, in class

<!-- ~120 min: the length pnpm timing:check reads -->

**Today's goal:** one sentence: what every student has at the end.

One sentence: where the typing happens.

**If time runs short:** one sentence.

??? info "Before the session"   (room, you, keys: three short bullets)

---

## Part 1 · Name { #part-1 }

**0:00 to 0:20** · at most one sentence.

---

### 1. Title that says what is done { #anchor }

<!-- 0:00 · 10 min -->

One sentence of purpose.

1. One line of instruction.

    ```text
    the line typed
    ```

    ```text
    its output
    ```

2. ...

**Check:** the result the room should have.

!!! question "Task: …"            (once per part, after its last section)
??? note "Answer"
```

- The comment `<!-- ~120 min ... -->` under the header line must stay:
  `pnpm timing:check` reads it (a week with a `split` in decks.json, such as
  week 5 at 60 + 180, declares its seminar minutes). No clock or minutes
  are visible anywhere on the page.
- Parts are `##`, sections are `###`, a `---` rule separates them. Keep
  every `{ #anchor }` that another page links to.
- End with `## Aims practised` (three bullets). No "Stretch goals" or
  "If students ask for more" lists: an extra is an optional section.

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
