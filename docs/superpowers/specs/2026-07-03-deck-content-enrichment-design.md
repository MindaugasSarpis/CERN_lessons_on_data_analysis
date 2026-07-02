# Deck-Wide Content Enrichment — Design (2026-07-03)

## Goal

Substantially enrich all 12 published lectures with textbook-grounded content so
each lecture is **self-contained** (every concept used is explained; no dangling
forward references to untaught material), **factually sound** (the 2026-07-02
content-review ledger flags for these lectures get resolved against
authoritative sources), and **expanded where thin** (deep-enrichment mandate:
roughly 5–15 added/reworked slides per lecture where the canonical treatment of
the topic demands it).

User decisions (2026-07-03): whole published deck · substantial enrichment ·
fix ledger flags · commit the in-progress five-lecture batch first.

## Non-goals

- Course-wide owner items stay open: course title vs repo name, TOC policy
  (`hideInToc` everywhere), British-vs-American **deck-wide** unification
  (within-file consistency is enforced), offline video assets, L01 grading /
  schedule slides (owned by the FF-2026 Workstream A roadmap).
- No changes to the workbook beyond fixing references the slide edits break.
- No new lectures, no reordering of the published lecture sequence.

## Approach (chosen from 3)

**Sequential lecture-by-lecture enrichment in one continuous effort**, with
targeted web verification of facts as each lecture is processed. Rejected:
parallel subagent fan-out (style drift across prose-heavy slides; the QA gate
and theme are shared state), and research-digest-first-for-all-12 (digests go
stale before editing; verification is cheap to do just-in-time).

## Canonical sources per lecture

| Lecture | Spine source(s) | Verification |
|---|---|---|
| L01 Orientation | — (admin; light touch only) | roadmap `.docx` owns grading |
| L02 Intro to CERN | CERN official pages, PDG | member states, data rates, 5-sigma wording |
| L03_1_1 Computer Science | Petzold *Code*; CS50; CS:APP (Bryant–O'Hallaron) | KB/KiB, endianness, compression taxonomy |
| L03_1_2 File Handling | Harvard HMS RDM guidance; Wilson et al. 2017 *Good Enough Practices* | add attribution; 40–50-char rule |
| L03_2 Command Line | Software Carpentry *Unix Shell* | `rm -rf /` modern behaviour |
| L03_3 Markdown | CommonMark / GFM spec | local logo asset |
| L03_4 VS Code | VS Code official docs | Dark Modern default; apt/dnf repo caveat |
| L05 Python | Official Python tutorial; Downey *Think Python* | triple-quoted-string framing; "free tiers" claim |
| L06 Concepts of DA | Wilson et al.; GO FAIR; CRISP-DM literature | FAIR attribution; SMART wording; Invenio; 23andMe; unsourced anecdotes |
| L07 Data Visualisation | Wilke *Fundamentals of Data Visualization* (already the spine); Cleveland & McGill 1984 | Bundestag pie figure; Okabe-Ito caption; disabled-slide triage |
| L08 Version Control | Chacon & Straub *Pro Git* | word-processor claim; `reset --hard`/reflog |
| L09 Probability & Statistics | OpenIntro Statistics; Blitzstein & Hwang | quote attribution; L10 forward reference |

## Per-lecture pipeline (the repeating unit)

1. **Read** the full lecture file (+ its workbook page for cross-references).
2. **Gap analysis** against the spine source's treatment: list missing
   prerequisite explanations, dangling references, thin treatments, and the
   lecture's ledger flags.
3. **Verify facts** flagged in the ledger (WebSearch/WebFetch where needed).
4. **Edit**: fix flags, rewrite thin sections, add new slides in house style
   (card system, `grid-2`/`grid-3`, type-scale discipline, kinetic
   `reveal-*`/`v-click`/`gradient-text` accents, MCQ checks where a concept
   completes). Every new concept slide ends a chain that starts from something
   already taught in this or an earlier published lecture.
5. **QA**: `pnpm qa` (or targeted `--only` ranges while iterating) — zero
   overflow, zero unrendered; screenshot review of changed slides.
6. **Ledger update**: mark resolved flags in
   `docs/superpowers/2026-07-02-content-review-ledger.md` with what was done.
7. **Commit** per lecture: `feat(LXX): textbook-grounded content enrichment`.

Processing order = published deck order: L01 → L02 → L03_2 → L03_1_1 →
L03_1_2 → L03_4 → L03_3 → L08 → L05 → L06 → L07 → L09.

## Self-containment rules (what "self-contained" means here)

- A term used on a slide is either (a) defined in this lecture, (b) defined in
  an **earlier published** lecture, or (c) explicitly labelled as a teaser with
  the lecture where it's defined ("defined formally in the Probability &
  Statistics lecture" pattern, already in use).
- Forward references to **unpublished** lectures (e.g. L10 Data Fitting) are
  removed or reworded as generic outlook.
- Code examples in pre-Python lectures (L03_x, L08) either switch to
  language-neutral text/pseudocode or carry a one-line "this is Python — a
  preview of the next lecture" label.

## Expansion guardrails

- New slides follow the house structure (section break → concept cards →
  example → MCQ/practice) and the type scale; no one-off font sizes.
- A lecture grows only where the spine source shows a genuine hole (e.g. L08
  has no "undoing things" treatment; L05 has no error-handling treatment).
  Target +5–15 slides per content lecture, less for tool lectures
  (L03_3/L03_4), ~0 for L01.
- Every added slide must clear the zero-overflow gate; dense material is split
  rather than shrunk.

## Constraints & invariants (project hard requirements)

- Zero slide overflow, verified by rendering (`pnpm qa`), not just building.
- Videos stay full-screen (`object-fit: cover`); no letterbox.
- Consistent type scale — sizes follow markdown level.
- Within-file language consistency (BrE files stay BrE, AmE stay AmE).
- Build through the published entry point so the theme loads.

## Error handling / verification

- After each lecture's edits: targeted QA on that lecture's slide range, then a
  full-deck QA before each commit (the full render is ~1 min now that media
  requests are blocked in the checker).
- Facts that cannot be verified against a source get flagged in the ledger
  rather than asserted.
- If an edit would conflict with an owner-level decision (grading, course
  title), it is skipped and noted in the ledger.

## Phase 0 (prerequisite, already in flight)

Fix QA checker video-hang + the 5 overflow slides; commit the five-lecture
in-progress batch per lecture (`feat(LXX): content fixes + kinetic restyle`),
plus `fix(qa)` and `fix(L06)` commits. Phase 1 (enrichment) starts only on a
green full-deck QA.
