# The Seminars — How They Work

Every lecture from week 2 on is paired with a **hands-on seminar**. Week 1 is
lecture only. A page carries the number of its lecture, except Seminar 1,
which pairs with Lecture 2; there is no Seminar 2. Each seminar takes ~120
min, all of it in class: there is no homework, and no session depends on
work done at home. The seminars practise the course's four aims:
🔧 tool-agnostic, ♻️ reproducible, ⚙️ automated, 📁 well-organised data & files.

## One project, one question per week

Every seminar works on the same project as the lectures, the weather
station: `weather-project`, with ten years of hourly readings in
`data/raw/weather.csv`. Each seminar asks one question about it, in its
title, and answers it by the end.

- **Seminars 1, 3 and 4** build the folder: VS Code and Markdown, the files
  as bytes, then PowerShell 7, Git and Python installed with a package
  manager. Their files come as zips from the
  [Releases page](https://github.com/MindaugasSarpis/weather-project/releases)
  of the project.
- **From Seminar 5 on** the project is a Git repository: the room clones
  [MindaugasSarpis/weather-project](https://github.com/MindaugasSarpis/weather-project)
  (about 0.5 MB) and publishes it to their own GitHub. A seminar that needs
  new files gets them with `git pull --no-edit course main`.
- **One shell:** PowerShell 7, in the terminal of VS Code, on macOS and on
  Windows. A line typed on the projector is the line typed on every laptop.

| Date in 2026 | Seminar | Question |
|--|--|--|
| 29 Sep | [1](seminar_01.md) | What Do the Weather Files Say? VS Code and Markdown |
| 6 Oct | [3](seminar_03.md) | What Are the 148 Bytes of `daily.csv`? Files as Bytes |
| 13 Oct | [4](seminar_04.md) | What Is the Mean Temperature of Ten Years? PowerShell on the Weather Project |
| 20 Oct | [5](seminar_05.md) | Who Changed the Mean? Git on the Weather Project |
| 27 Oct | [6](seminar_06.md) | Can You Compute 7.16 Yourself? Python on the Weather Project |
| 3 Nov | [7](seminar_07.md) | Is It Getting Warmer? Functions and NumPy on the Weather Project |
| 10 Nov | [8](seminar_08.md) | What Does a Year of Weather Look Like? Figures with Matplotlib |
| 17 Nov | [9](seminar_09.md) | How Sure Is 7.16? Probability on the Weather Data |
| 1 Dec | [10](seminar_10.md) | How Strong Is the Yearly Cycle? Fitting the Weather Data |
| 8 Dec | [11](seminar_11.md) | Will It Freeze Tonight? A Perceptron on the Weather Data |
| 15 Dec | [12](seminar_12.md) | How Cold Is the Hill? pandas on a Second Station's File |
| 22 Dec | [13](seminar_13.md) | Can a Stranger Rebuild Every Number? One Command for the Weather Project |

Seminars 14 to 16 belong to the further topics and are not scheduled.

| | Seminar | Question |
|--|--|--|
| — | [14](seminar_14.md) | Was October 2025 Unusually Warm? A Blind Analysis |
| — | [15](seminar_15.md) | How Long Does It Take, and How to Make It Faster? Timing the Weather Project |
| — | [16](seminar_16.md) | Can a Model Forecast Tomorrow's Temperature? scikit-learn on the Weather Project |

## How a page works

The first screen is a **run sheet**: each section with the line typed and
what the room ends with. Each section is a few short steps (the
instruction, the line to type, its output), a **Check:** line, and each part
ends with a **Task** for the room, its answer folded under it. The
**▶ Steps** button (bottom right) shows the page one step at a time.

## The project folder

```text
weather-project/
|- README.md            # what this is, where the data came from, how to rebuild
|- environment.yml      # the conda environment (Seminar 7 on)
|- data/
|  |- raw/              # files exactly as received, never edited
|  |- processed/        # made from data/raw by commands and scripts
|- scripts/             # one script per step
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
| Continuity | Each seminar starts from the repository as the last one left it | Grows all term; the seminar skills are meant to be carried into it |
| Assessed | No | Yes: repository, one-page report, short video, final presentation (see Lecture 1) |

How much the two overlap is up to you: a seminar step can be repeated on
your own data, or your project can go somewhere else entirely.
