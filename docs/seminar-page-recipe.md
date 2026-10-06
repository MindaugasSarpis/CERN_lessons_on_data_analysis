# Seminar page recipe

How a seminar page in `lectures/workbook/docs/seminars/seminar_NN.md` is
laid out. The page is read live, on a second screen, by the person at the
front of the room. Whoever opens it in the break before the session should
know within one screen what to do. [Seminar 3](../lectures/workbook/docs/seminars/seminar_03.md)
is the worked example.

Written on 6 October 2026, after Seminar 3: the lecturer opened a page of
500 lines, could not see at once what to do, and taught the terminal for
two hours instead.

## Rules

1. **Everything happens in class.** No homework, no "done at home", no
   "Next steps, at home". Students do not do it, so a later session must
   never depend on it. Installing software is done in class too. What does
   not fit in 120 minutes is an optional section, marked as such in the run
   sheet, or a stretch goal.
2. **The first screen is enough to run the session.** Above the first `---`
   there is only: the title, the header line, one **Today's goal** sentence,
   one or two sentences on the tools, the **Run sheet**, one **If time runs
   short** line, and collapsed boxes.
3. **One thread.** Every section follows from the one before it and ends in
   a file or a number the room can check. A section that does not serve the
   goal is a stretch goal.

## Layout

```text
# Seminar NN — Title

**Paired lecture:** NN Title · **Format:** follow-along · **~120 min**
in class

**Today's goal:** one sentence: what every student can do or has at the end.

One or two sentences: the tools of the session, and what is new.

## Run sheet

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · Name** · 40 min | | |
| 0:00 | [1. Title](#anchor) | the one thing typed or clicked | the checkable result |
...
| | **Optional, if the room is fast** | | |
| — | [9. Title](#anchor) | ... | ... |

**If time runs short:** which section to leave out, in one sentence.

??? info "How to use this page"
??? info "Before the session"      (prerequisites for the room and for you)
??? info "Files for this seminar"  (when the page hands out files)

---

## Part 1 · Name { #part-1 }

**0:00 to 0:40 · sections 1 to 3**

One or two sentences.

---

### 1. Title { #anchor }

**0:00 · 10 min**

**Tell the room.** The paragraph to say before the steps.

1. Steps. Every command, file name, search text or value the room types
   stands alone in a ```text block, so it can be read from the back row and
   copied.
2. Output goes in its own block after the step, introduced in words.

!!! success "You should now see"
    The checkpoint.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|

---

### 2. ...
```

- `**~120 min**` must stay on the header line: `pnpm timing:check` reads it.
- Parts are `##`, sections are `###`, and a `---` rule separates them.
  Keep every `{ #anchor }`: other pages link to them.
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
  on macOS and PowerShell 7 on Windows (no Git Bash); a line both shells
  share (`git ...`, `cd ...`) stands once, outside tabs. Keys stay inline in
  the old form: `Ctrl+S` (macOS `Cmd+S`).
- Run sheet: the "On the projector" column names the one thing typed or
  clicked. Optional sections have `—` as their clock and sit under their own
  row at the end of the table.
- Optional sections keep the full layout and live in a last part,
  `## Optional, if the room is fast`.
- After the wrap-up come `## Stretch goals`, `## If students ask for more`
  and `## Aims practised`, as before.
- The extensions for tabs and collapsed boxes (`pymdownx.tabbed`,
  `pymdownx.details`) are switched on in `lectures/workbook/mkdocs.yml`.
  Check a page with `mkdocs build --strict -f lectures/workbook/mkdocs.yml`.
