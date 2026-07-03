# Seminar 16 — Train & Honestly Evaluate a Classifier *(optional)*

**Paired lecture:** 16 Machine Learning & AI · **Format:** hackathon · **~90 min**

> **Running project — this session adds:** a trained signal-vs-background classifier
> with an honest evaluation. *Optional / advanced — the capstone.*

## Goal
Apply the whole course to a machine-learning task — and, more importantly,
**evaluate it honestly** — using the clean dataset you built.

## Prerequisites
Seminar 13 (`events_clean`). scikit-learn available.

## Tasks
1. Define the label: `signal` = events inside a resonance window (e.g. near the Z or
   J/ψ), `background` = events well outside. Choose feature columns (energies,
   momenta, `pt`, `eta`, …) — **do not** feed it `M` directly (that's cheating).
2. `train_test_split` with `stratify=` on the label. Fit a
   `RandomForestClassifier` (or logistic regression) on the **train** set.
3. Evaluate on the **held-out test** set: confusion matrix, precision, recall, F1.
   Compare against the "predict majority" baseline.
4. Report the train-vs-test gap. Are you overfitting? Write a one-paragraph honest
   verdict in the README.

## Stretch goals
- Which features matter most? (`feature_importances_`.)
- Deliberately leak `M` into the features and watch accuracy jump to ~100% — then
  explain why that result is worthless (data leakage).

## Solution notes (instructor)
The lesson is **evaluation**, not accuracy. The leakage stretch goal is the single
best teaching moment — a "perfect" model that has secretly seen the answer. Tie
back to the course thesis: data literacy > tool literacy.

## Aims practised
📊 honest evaluation · ♻️ reproducible training (seeded, scripted) · 🔧 model-agnostic workflow
