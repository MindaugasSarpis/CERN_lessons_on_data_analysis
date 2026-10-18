# The Seminars — How They Work

Every lecture from week 2 on is paired with a **hands-on seminar**. Week 1 is
lecture only. A page carries the number of its lecture, except Seminar 1,
which pairs with Lecture 2; there is no Seminar 2. Each seminar takes ~120
min, all of it in class: there is no homework, and no session depends on
work done at home. The seminars practise the course's four aims:
🔧 tool-agnostic, ♻️ reproducible, ⚙️ automated, 📁 well-organised data & files.

## One project, one question per week

Every seminar works on the same project as the lectures, the weather
station, with ten years of hourly readings in `data/raw/weather.csv`. Each
seminar asks one question about it and answers it by the end.

- **Every seminar stands on its own.** It starts from its own folder,
  `weather-sNN.zip` on the
  [Releases page](https://github.com/MindaugasSarpis/weather-project/releases)
  of the project, which holds everything the session needs: the data, the
  finished files of earlier seminars, and the `environment.yml` of its
  conda environment. Missing a week costs nothing; nothing has to be
  carried over from an earlier session.
- **Seminar 5** is the first Python of the room: the interpreter, a Jupyter
  notebook, IDLE and VS Code, and the first conda environment.
- **Seminar 6** is Git: the room clones
  [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project)
  (about 0.5 MB) and publishes it to their own GitHub. Seminar 13 uses Git
  again; the other seminars do not need it.
- **The terminal:** zsh on macOS and Git Bash on Windows, in the terminal
  of VS Code. They take the same commands, so a line typed on the projector
  is the line typed on every laptop.

## How a page works

Section 1 gets the day's folder. Each section is a few short steps (the
instruction, then the typed line and its output in one block), a **Check:** line, and each part
ends with a **Task** for the room, its answer folded under it. The
**▶ Steps** button (bottom right) shows the page one step at a time.

## The project folder

```text
weather-sNN/
|- README.md            # what this is, where the data came from, how to rebuild
|- environment.yml      # the conda environment (Seminar 5 on)
|- data/
|  |- raw/              # files exactly as received, never edited
|  |- processed/        # made from data/raw by commands and scripts
|- scripts/             # one script per step
|- notebooks/           # Jupyter notebooks (Seminar 5)
|- results/             # numbers and figures the scripts produce
|- tests/               # checks of the results (Seminar 13)
|- run_all.py           # one command rebuilds everything (Seminar 13)
```

The same layout is a sound default for your own project.

**The golden rule:** you could delete everything except `data/raw/` and
`scripts/` and rebuild the whole thing with one command.

## Seminars and your project

| | **The seminars** | **Your project** |
|--|--|--|
| What | One hands-on session per week on the weather project | One project of your own, developed across the semester |
| Topic | Set by the page | **Entirely your choice**: field, data, and form (analysis, app, dashboard, educational piece) |
| Continuity | Each seminar starts from its own folder, `weather-sNN.zip` | Grows all term; the seminar skills are meant to be carried into it |
| Assessed | No | Yes: repository, one-page report, short video, final presentation (see Lecture 1) |

How much the two overlap is up to you: a seminar step can be repeated on
your own data, or your project can go somewhere else entirely.
