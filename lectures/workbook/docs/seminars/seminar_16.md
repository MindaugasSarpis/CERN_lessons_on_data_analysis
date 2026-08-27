# Seminar 16 — Train & Honestly Evaluate a Classifier *(optional)*

**Paired lecture:** 16 Machine Learning & AI · **Format:** hackathon · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **This session builds:** a trained signal-vs-background classifier
> with an honest evaluation. *Optional / advanced — the capstone.*

## Goal
Apply the whole course to a machine-learning task — and, more importantly,
**evaluate it honestly** — on the shared D⁰ → K⁻π⁺ sample (or a dataset from your
own field).

## Prerequisites
The D⁰ sample loaded as a table (invariant mass `M` plus the daughter momenta).
scikit-learn available.

## Tasks
1. Define the label: `signal` = events inside the D⁰ peak window (~1.84–1.89 GeV),
   `background` = events in the sidebands. Choose feature columns (momenta,
   `pt`, kinematics, …) — **do not** feed it `M` directly (that's cheating).
2. `train_test_split` with `stratify=` on the label. Fit a
   `RandomForestClassifier` (or logistic regression) on the **train** set.
3. Evaluate on the **held-out test** set: confusion matrix, precision, recall, F1.
   Compare against the "predict majority" baseline.
4. Report the train-vs-test gap. Are you overfitting? Write a one-paragraph honest
   verdict in the README.
5. Save the whole pipeline (label definition → split → fit → evaluate) as
   `scripts/train_classifier.py`, accepting a `--seed` argument (default 42) so the
   entire result — including the train/test split — is exactly reproducible on request.
6. Plot the **ROC curve** and report the **AUC** alongside your F1 score — how much
   better than the 0.5 (random-guess) baseline is it?

## Stretch goals
- Which features matter most? (`feature_importances_`.)
- Deliberately leak `M` into the features and watch accuracy jump to ~100% — then
  explain why that result is worthless (data leakage).
- Try a second classifier (logistic regression or `GradientBoostingClassifier`) and
  compare its honestly-evaluated F1 to the Random Forest's — is the ranking stable
  across a couple of random seeds?

## Wrap-up (last 10 min)
- Re-run `scripts/train_classifier.py --seed 42` and confirm you get bit-for-bit the
  same confusion matrix and F1 — the whole training run is reproducible, not just the data.
- Commit: `git add -A && git commit -m "Add honestly-evaluated classifier — course capstone"`.
- Note one lesson in the README — and, since this is the last seminar, one line on which
  of the course's four aims this exercise leaned on most.

## Solution notes (instructor)
The lesson is **evaluation**, not accuracy. The leakage stretch goal is the single
best teaching moment — a "perfect" model that has secretly seen the answer. Tie
back to the course thesis: data literacy > tool literacy. As the capstone, protect
that leakage stretch goal even if the 120 minutes run short elsewhere — cut task 6's
ROC/AUC first, since watching accuracy jump to ~100% and understanding why is the
single most memorable lesson of the term.

## Aims practised
📊 honest evaluation · ♻️ reproducible training (seeded, scripted) · 🔧 model-agnostic workflow
