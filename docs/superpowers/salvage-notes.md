# Salvage map — retired quizzes + video crash-course (2026-07-03)

Quizzes are discontinued and the video-lecture crash course is retired. The
source files are **deleted from the working tree but preserved in git history**
(the commit immediately before "chore: retire quizzes…"). Retrieve any item with:

```bash
git log --diff-filter=D --name-only -- '<path>'      # find the deleting commit
git show <parent-sha>:<path>                          # print the old content
```

Retired files: `misc/exams/quiz_1.yaml`, `misc/exams/Quiz_2.yaml`,
`misc/exams/quiz-1.xml`, `lectures/content/quiz_1_feedback.md`,
`lectures/content/quiz_2_feedback.md`,
`lectures/content/crash_course_for_video_lecture.md`.

This file is a **working note**; delete it once the salvage below is folded in
(tracked as part of the content phases P3–P5).

## Quiz → MCQ conversions (fold into lectures as `<MCQ>` slides)

From `misc/exams/quiz_1.yaml` — high-quality, aim-aligned questions. Target deck:

| quiz question | target lecture (deck) | aim |
|--|--|--|
| `what_is_a_file` (file = named sequence of bytes) | 03 How Computers Work | 📁 |
| `file_extensions` (extension = convention, not guarantee) | 03 How Computers Work | 📁 |
| `text_vs_binary` | 03 How Computers Work | 📁 |
| `relative_vs_absolute_paths` (portability) | 04 Command Line & File Handling | ♻️📁 |
| `here_near_far_backups` | 04 Command Line & File Handling | ♻️ |
| `scriptable_workflow` (re-runnable = reproducible) | 09 Concepts / 14 Reproducible Workflows | ♻️⚙️ |
| `gui_limits` (no record → not reproducible) | 09 Concepts / 14 Reproducible Workflows | ♻️ |
| `what_is_a_dmp`, `dmp_raw_vs_derived` | 09 Concepts of Data Analysis | ♻️📁 |
| `what_is_git`, `git_vs_copies_intuition`, `what_is_a_commit`, `why_commit_messages`, `branches_intuition`, `version_control_collaboration` | 06 Version Control with Git | ♻️🔧 |

`Quiz_2.yaml` (AI-themed) → fold the best into **16 Machine Learning & AI**.

Convert each to the deck's `<MCQ>` component (question / options / :correct /
explanation), keeping the YAML's `explanation` text. Add ≤1–2 MCQs per lecture
so decks stay tight; the rest can seed seminar self-checks.

## Crash-course → lecture salvage (verbatim card blocks in git history)

From `crash_course_for_video_lecture.md`:

- **"AI marketing labels"** grid (`"AI-Powered" Dashboard`, `"Smart" Anomaly
  Detection`, `"Predictive" Analytics`, `Actual ML Use Case` + "3 of 4 need
  data-analysis skills, not AI") → **16 ML/AI** as a *"what is NOT AI"* slide.
- **Data-science field taxonomy** (Statistics / Data Engineering / Data
  Analysis / Data Science / AI-ML) → **16 ML/AI** (or 09 Concepts) framing slide.
- **Pitfalls** list (jumping to models, correlation≠causation, overfitting
  charts, calling everything AI, no reproducibility) → reinforces the aims;
  use in **16 ML/AI** or the P5 spine pass.
- **"Data literacy > tool literacy" / "thinking matters more than the label" /
  "CERN-grade rigour is learnable" / "skills transfer everywhere"** grid →
  ideal **tool-agnosticism (🔧) capstone**; use on the L16 closer or a spine
  slide. This is the single best statement of the course's thesis — reuse it.
