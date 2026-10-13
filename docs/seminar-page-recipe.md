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
steps and orient myself".

## Rules

1. **Everything happens in class.** No homework, no "done at home". What
   does not fit in 120 minutes is an optional section at the end.
2. **One question, one project.** Every seminar works on the weather
   project (`weather-project`, the same files as the lectures) and answers
   one question about it, in its title. From Seminar 6 on the project is a
   Git repository: the room cloned
   [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project)
   in Seminar 6 (`misc/weather_repo/build.sh` makes it). A seminar that
   needs new files gets them with `git pull course main`; the files are
   added to the course repository as one commit per seminar, and they only
   add new files, never edit existing ones (so the pull never conflicts).
3. **Installs at the start.** Anything the seminar needs installed is
   section 1.
4. **Short steps.** A step is one line of instruction, then the line typed
   (its own ```text block), then the output (its own block). No paragraph
   between steps. A section opens with one line under its heading, the
   clock, the minutes and one sentence of purpose:
   `**0:20 · 10 min** · A commit is one saved state: id, author, date, message.`
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
# Seminar NN — The Question? Topic

**Paired lecture:** NN Title · **Format:** follow-along · **~120 min**
in class

**Today's goal:** one sentence: what every student has at the end.

One sentence: where the typing happens.

## Run sheet

| Clock | Section | Typed | The room ends with |
|--|--|--|--|
| | **Part 1 · Name** · 20 min | | |
| 0:00 | [1. Title](#anchor) | the one line typed | the checkable result |
...
| | **Optional, if the room is fast** | | |
| — | [13. Title](#anchor) | ... | ... |

**If time runs short:** one sentence.

??? info "Before the session"   (room, you, keys: three short bullets)

---

## Part 1 · Name { #part-1 }

**0:00 to 0:20** · at most one sentence.

---

### 1. Title that says what is done { #anchor }

**0:00 · 10 min** · One sentence of purpose.

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

- `**~120 min**` must stay on the header line: `pnpm timing:check` reads it.
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
- Run sheet: the "Typed" column names the one thing typed or clicked. Optional sections have `—` as their clock and sit under their own
  row at the end of the table.
- Optional sections keep the full layout and live in a last part,
  `## Optional, if the room is fast`.
- The extensions for tabs and collapsed boxes (`pymdownx.tabbed`,
  `pymdownx.details`) are switched on in `lectures/workbook/mkdocs.yml`.
  Check a page with `mkdocs build --strict -f lectures/workbook/mkdocs.yml`.
