# Deck-Wide Content Enrichment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich all 12 published lectures with textbook-grounded content so each is self-contained, factually sound (ledger flags resolved), and substantially expanded where the canonical treatment demands it.

**Architecture:** Sequential per-lecture pipeline (read → gap-check vs spine source → verify facts → edit in house style → QA gate → ledger update → commit), processed in published-deck order. Spec: `docs/superpowers/specs/2026-07-03-deck-content-enrichment-design.md`.

**Tech Stack:** Slidev markdown + custom theme (`lectures/content/theme/`), `pnpm qa` render gate (`scripts/check-slides.mjs`), WebSearch/WebFetch for fact verification.

## Global Constraints

- Zero slide overflow at 6px tolerance, verified by `pnpm qa` rendering all 493+ slides (`Measured N/N`, `✅ No overflow`). Never commit on a red or partially-measured run.
- Type scale follows markdown level — no one-off `font-size` on content text (decorative fact-slides with existing scoped styles are grandfathered).
- Videos full-screen via existing `VideoPlayer` — do not add letterboxed media.
- House slide style: card system (`card card-{primary|secondary|accent|info|success|warning} card-glass`), `pad-tight|pad-compact`, `grid-2|grid-3 gap-md mt-md`, emoji-outside-bold headings (`## 📊 **Title**`), kinetic accents (`reveal-left|reveal-up|reveal-scale` + `v-click`, `gradient-text` on ≤1 keyword per title, `glow` sparingly).
- Language: keep each file's existing variant (BrE vs AmE); do not unify across files.
- Self-containment: a term is defined here, defined in an earlier published lecture, or explicitly labelled a teaser naming the defining lecture. No references to unpublished lectures (L10, L11, L12).
- Owner items stay untouched: course title/subtitle, `hideInToc` policy, L01 grading + schedule content, offline video assets.
- Commits: one per lecture, message `feat(LXX): textbook-grounded content enrichment (<topic>)`, with the standard Co-Authored-By + Claude-Session trailer used in this repo.
- Ledger: `docs/superpowers/2026-07-02-content-review-ledger.md` — when a flag is fixed, replace its bullet with `✅ RESOLVED (2026-07-XX): <what was done>`; when deliberately kept, annotate why.
- After each lecture's edit: run `pnpm qa` (full build + render, ~95s). While iterating, use `node scripts/check-slides.mjs lectures/content/.qa-dist --only N,M --shots <dir>` against the last build for speed, but the committing run must be a fresh full `pnpm qa`.
- Read changed slides' screenshots from `.qa-shots/` before committing (visual sanity: spacing, reveal states, image sizing).

## Slide-number lookup

`.qa-shots/slide-NNN.png` numbering follows published order: L01, L02, L03_2, L03_1_1, L03_1_2, L03_4, L03_3, L08, L05, L06, L07, L09. Recompute boundaries after any slide-count change by grepping titles in fresh shots or checking `--only` output titles.

---

### Task 1: L01 Course Orientation (self-containment audit only)

**Files:**
- Modify: `lectures/content/slides/L01_Course_Orientation.md`
- Ledger: `docs/superpowers/2026-07-02-content-review-ledger.md`

**Interfaces:** none (standalone content task).

- [ ] **Step 1: Read the full lecture.** List every forward reference (lecture names, tool names, dates). L01 is administrative — per spec, grading/contact-hours/schedule slides stay as-is (Workstream A owns them).
- [ ] **Step 2: Fix only self-containment breaks.** Any reference to an unpublished lecture (L10+) → reword to generic outlook ("later in the course" → "in the data-analysis lectures"). Any tool named before its lecture → add "(introduced in the <name> lecture)".
- [ ] **Step 3: QA.** Run `pnpm qa`. Expected: `✅ No overflow: all N slides fit the frame.`
- [ ] **Step 4: Ledger.** Annotate the three L01 bullets: `⏸ DEFERRED to FF-2026 Workstream A (2026-07-03)` — they are roadmap-owned, not forgotten.
- [ ] **Step 5: Commit** only if Step 2 changed anything: `feat(L01): self-containment fixes (orientation)`. If nothing changed, commit the ledger annotation alone with `docs: mark L01 ledger flags as roadmap-owned`.

### Task 2: L02 Introduction to CERN

**Files:**
- Modify: `lectures/content/slides/L02_Introduction_to_CERN.md`
- Possibly rename: `lectures/content/public/videos/Perseverence_Rover_Landing_NASA.mp4` → `Perseverance_...` (only if the file exists locally; otherwise fix stays deferred)
- Ledger: same as Task 1.

**Ledger flags to resolve:**
- 5-sigma: replace "less than 1 in 3.5 million chance of being wrong" with the correct semantics: "if there were no new particle, a background fluctuation this large would occur in fewer than 1 in 3.5 million experiments". Add a one-line teaser: "we make this precise in the Probability & Statistics lecture (p-values)".
- Pipeline order: swap so triggers (online filtering) precede full event reconstruction (offline). Correct order: collisions → trigger (L1 hardware → high-level software) → storage → offline reconstruction → analysis.
- Aging figures: verify each via WebSearch ("CERN member states 2026", "LHC Run 3 data rate petabytes per year", "CERN number of users scientists"). Update numbers and suffix each stat with "(as of 2026)".
- Perseverance misspelling: check `ls lectures/content/public/videos/`. If the asset is local, rename file + reference; if remote-fallback only, leave and annotate ledger ("rename requires touching the release asset").

**Enrichment candidates (verify against file before adding; target +5–10 slides):**
- Accelerator chain: LINAC4 → PS Booster → PS → SPS → LHC, one `grid` slide with energies per stage (source: CERN accelerator complex page).
- From collision to dataset: trigger cascade slide with rates (~40 MHz collisions → ~100 kHz L1 → ~1-10 kHz to storage; verify current ATLAS/CMS figures) — this is the data-analysis hook of the lecture.
- Worldwide LHC Computing Grid: tiers 0/1/2, why distributed (data volume), one slide.
- Detector anatomy: tracker → calorimeters → muon system, "onion" ordering and what each measures, one slide (if not already present).
- MCQ: 5-sigma meaning (distractor = the old wrong phrasing — turns the fixed error into a teaching point).

- [ ] **Step 1: Read the full lecture**; confirm which enrichment candidates are genuinely missing; drop any already covered.
- [ ] **Step 2: Verify facts** (WebSearch queries above). Record findings inline in the edit.
- [ ] **Step 3: Edit** — fix flags, add slides in house style. New slides get `hideInToc: true` and section-appropriate placement.
- [ ] **Step 4: QA** — `pnpm qa` green; read new slides' shots from `.qa-shots/`.
- [ ] **Step 5: Ledger** — mark the four L02 bullets resolved/annotated.
- [ ] **Step 6: Commit** — `feat(L02): textbook-grounded content enrichment (CERN, triggers, WLCG)`.

### Task 3: L03_2 Command Line

**Files:**
- Modify: `lectures/content/slides/L03_2_Command_Line.md`
- Ledger: same.

**Ledger flags to resolve:**
- `rm -rf /`: reword to "`rm -rf` on the wrong directory deletes it permanently — no trash can. (Modern `rm` refuses `/` itself without `--no-preserve-root`, but `rm -rf ~` has no such guard.)"
- Forward references (README/Markdown/version control): label each "(covered in the Markdown / Version Control lecture)".
- "Working with Processes" scope: keep, but demote to a clearly-labelled "optional / power-user" section break if not already.

**Enrichment candidates (Software Carpentry *Unix Shell* episodes; target +6–12 slides):**
- Pipes & filters: `wc`, `sort`, `head`, `|` composing one worked example (count most common words in a file, or largest files in a directory).
- Redirection: `>`, `>>`, `2>`, `<` — one slide with a before/after terminal block.
- Wildcards/globbing: `*.csv`, `?`, `[ab]` — one slide + one "which files match?" MCQ.
- `grep` and `find`: one slide each with a realistic data-file example (`grep -r "22.3" data/`, `find . -name "*.csv" -newer ...`).
- Getting help: `man`, `--help`, `tldr` — one compact slide.
- Exit codes & chaining: `&&`, `||`, `;` — one slide (foundation for scripting).

- [ ] **Step 1: Read the full lecture**; drop covered candidates.
- [ ] **Step 2: Edit** — flags + additions. Keep every example runnable on both bash and PowerShell, or dual-annotate (existing house pattern for platform splits).
- [ ] **Step 3: QA** green + shots review.
- [ ] **Step 4: Ledger** update (3 bullets).
- [ ] **Step 5: Commit** — `feat(L03_2): textbook-grounded content enrichment (pipes, grep/find, redirection)`.

### Task 4: L03_1_1 Crash Course on Computer Science

**Files:**
- Modify: `lectures/content/slides/L03_1_1_Crash_Course_on_Computer_Science.md`
- Ledger: same.

**Ledger flags to resolve:**
- KB vs KiB: state the convention explicitly — decimal units (1 kB = 1000 B) vs binary units (1 KiB = 1024 B); make the size table use one convention consistently and note the other.
- CSV/JSON under "lossless compression": split the taxonomy — uncompressed text formats (CSV/JSON) vs lossless compression (ZIP/PNG/FLAC) vs lossy (JPEG/MP3). One corrected card layout.
- ARM endianness: reword to "typically runs little-endian" (bi-endian hardware, simplification acknowledged).
- Python/NumPy examples before Python is taught: keep as teasers but add the house teaser label ("a preview — Python is introduced in the Crash Course on Python").
- `first_transisor.jpg` misspelled asset: rename file + reference (it is local in `public/figures/`).

**Enrichment candidates (Petzold *Code*, CS50 week 0; target +5–10 slides):**
- Two's complement: how negative integers are stored (follows the existing overflow slides naturally) — 2 slides: the trick (invert + 1) and why it makes subtraction free.
- Fetch–decode–execute: one slide connecting "algorithm" to "what the CPU physically does" (closes the loop the lecture opens with the algorithm "box").
- Unicode beyond ASCII: code points vs encoding, UTF-8 variable width, why `é` can break naive byte-length code — 1-2 slides after the ASCII table.
- Memory hierarchy: registers → cache → RAM → disk with latency orders of magnitude — 1 slide (motivates why data format/size matters for analysis).
- MCQ: "how many distinct values fit in 2 bytes?" (binary consolidation).

- [ ] **Step 1: Read the full lecture** (it was reordered yesterday — binary now precedes hex); confirm candidates missing.
- [ ] **Step 2: Edit** — flags + additions; keep new slides in the matching section (Data Representation / Numbers / Text).
- [ ] **Step 3: Rename asset**: `git mv lectures/content/public/figures/first_transisor.jpg lectures/content/public/figures/first_transistor.jpg` and update the reference.
- [ ] **Step 4: QA** green + shots review.
- [ ] **Step 5: Ledger** update (5 bullets).
- [ ] **Step 6: Commit** — `feat(L03_1_1): textbook-grounded content enrichment (two's complement, UTF-8, memory hierarchy)`.

### Task 5: L03_1_2 File Handling and Directory Structure

**Files:**
- Modify: `lectures/content/slides/L03_1_2_File_Handling_and_Directory_Structure.md`
- Ledger: same.

**Ledger flags to resolve:**
- Absolute-paths advice: invert to the standard recommendation — scripts use paths **relative to the project root** for portability; absolute paths for machine-specific config only. Update the comparison card.
- HMS attribution: add a source line "Naming guidance adapted from Harvard Medical School Research Data Management" with link, on the file-naming section's first slide.
- ISO-8601 duplicate bullet on consecutive slides: remove one occurrence.
- (Already fixed in the committed batch: camel-case label, 40–50-char upper bound.)

**Enrichment candidates (Wilson et al. 2017 *Good Enough Practices in Scientific Computing*; target +4–8 slides):**
- Raw data is read-only: the `data/raw/` vs `data/processed/` contract — never edit raw files, derive everything by script — 1 slide (anchors the existing skeleton exercise).
- README as lab notebook: what a minimal project README records (provenance, units, how to regenerate) — 1 slide + tie-in to the Markdown lecture.
- Metadata: sidecar files (`samples.csv` + `samples_README.txt`), why filenames can't hold everything — 1 slide (grounds the existing "master spreadsheet" bullet).
- Archive what you publish: zip + checksum + DOI concept — 1 compact slide (foreshadows FAIR in L06 without depending on it).

- [ ] **Step 1: Read the full lecture**; drop covered candidates.
- [ ] **Step 2: Edit** — flags + additions (BrE file — keep spelling).
- [ ] **Step 3: QA** green + shots review.
- [ ] **Step 4: Ledger** update (4 bullets).
- [ ] **Step 5: Commit** — `feat(L03_1_2): textbook-grounded content enrichment (raw-data contract, README, metadata)`.

### Task 6: L03_4 VS Code

**Files:**
- Modify: `lectures/content/slides/L03_4_VS_Code.md`
- Ledger: same.

**Ledger flags to resolve:**
- "(Dark+ is the default)" → "(Dark Modern is the default)" — verified: default since VS Code 1.78 (April 2023).
- Python extension "Jupyter notebook support built-in" → verify via VS Code marketplace docs; correct to "installs the Jupyter extension alongside" if that's current.
- "next lecture" (Markdown) → name the lecture instead of relying on order: "in the Markdown lecture".
- Practice slide bash-only commands: add PowerShell equivalents (`mkdir` works; `touch` → `New-Item -ItemType File` or `ni`), house dual-platform pattern.
- `python` vs `python3`: match whatever L05 teaches (check L05's install-check slide; it uses `python3 --version` with a `python --version` Windows note — mirror that).
- "install via apt/dnf" → add "after adding Microsoft's repository"; "100+ languages" → "100+ languages via extensions".

**Enrichment candidates (VS Code docs; keep small, +2-4 slides):**
- Command Palette as the universal entry point (`Ctrl+Shift+P`) with 3 concrete tasks students will actually do — 1 slide if not present.
- Integrated terminal + file explorer workflow: edit-run loop for the L05 script exercise — 1 slide if not present.

- [ ] **Step 1: Read the full lecture**; verify the Jupyter claim and current marketplace wording (WebSearch "VS Code Python extension Jupyter included 2026").
- [ ] **Step 2: Edit** — flags + minimal additions.
- [ ] **Step 3: QA** green + shots review.
- [ ] **Step 4: Ledger** update (6 bullets).
- [ ] **Step 5: Commit** — `feat(L03_4): textbook-grounded content fixes (Dark Modern, PowerShell parity)`.

### Task 7: L03_3 Markdown

**Files:**
- Modify: `lectures/content/slides/L03_3_Markdown.md`
- Possibly create: `lectures/content/public/figures/markdown_logo_light.svg` (local light-on-dark asset)
- Ledger: same.

**Ledger flags to resolve:**
- Wikimedia-hosted, near-invisible logo: download the official Markdown mark, convert/recolor to a light variant, store under `public/figures/`, reference locally.

**Enrichment candidates (CommonMark/GFM; keep small, +3-5 slides):**
- Links & images reference-style vs inline — 1 slide if only inline is shown.
- GFM tables + task lists — 1 slide if missing (tables are used throughout the course's own materials).
- "Where you'll meet Markdown again": README (Git lecture), Jupyter notebook cells, this very slide deck — 1 closing-loop slide.

- [ ] **Step 1: Read the full lecture**; drop covered candidates.
- [ ] **Step 2: Asset fix** — fetch the logo (`curl` the Wikimedia SVG), set `fill` to a light theme colour, save locally, swap the reference.
- [ ] **Step 3: Edit** additions.
- [ ] **Step 4: QA** green + shots review.
- [ ] **Step 5: Ledger** update (1 bullet).
- [ ] **Step 6: Commit** — `feat(L03_3): textbook-grounded content enrichment (local logo, GFM coverage)`.

### Task 8: L08 Version Control

**Files:**
- Modify: `lectures/content/slides/L08_Version_Control.md`
- Ledger: same.

**Ledger flags to resolve:**
- Word-processor claim: reword — modern word processors do track changes and co-edit; what they lack is **line-level semantic diffs, branching/merging, and offline distributed history** — that's git's actual value.
- "`reset --hard` cannot be undone": correct — uncommitted changes are lost for good, but committed states are recoverable via `git reflog`; add a one-line reflog rescue example.
- Python-flavoured merge-conflict examples one lecture before Python: either switch the conflict file to plain text/Markdown (`about_me.md` fits the lecture's own narrative) or label as preview. Prefer switching to `about_me.md` content.
- Verify `about_me.md` is the exercise filename in L03_3 (grep it); align the reference if not.

**Enrichment candidates (Chacon & Straub *Pro Git* ch. 2–3; target +6-10 slides):**
- The three states: working directory → staging area → repository, one mermaid/diagram slide early (Pro Git's central mental model; check if implicit only).
- Inspecting history: `git log --oneline --graph`, `git diff` vs `git diff --staged`, `git show` — 2 slides with realistic output blocks.
- Undoing things safely: `git restore <file>`, `git restore --staged`, `git commit --amend`, `git revert` vs `reset` — 2 slides (ties into the reflog fix).
- Branching visual: mermaid `gitGraph` slide showing feature-branch → merge (the deck's theme styles gitGraph already).
- MCQ: "you committed a typo to the last commit message — what's the safest fix?" (amend vs revert vs reset).

- [ ] **Step 1: Read the full lecture**; drop covered candidates; grep L03_3 for `about_me.md`.
- [ ] **Step 2: Edit** — flags + additions. Careful: never put raw conflict markers in fenced blocks (Slidev snippet-plugin gotcha) — use the `{{'<<<<<<< HEAD'}}` escape documented in CLAUDE.md.
- [ ] **Step 3: QA** green + shots review.
- [ ] **Step 4: Ledger** update (4 bullets).
- [ ] **Step 5: Commit** — `feat(L08): textbook-grounded content enrichment (three states, undoing, history)`.

### Task 9: L05 Crash Course on Python

**Files:**
- Modify: `lectures/content/slides/L05_Crash_Course_on_Python_Programming.md`
- Ledger: same.

**Ledger flags to resolve:**
- Triple-quoted strings as "multi-line comments": reframe — they are string literals; used as docstrings when first statement of a function/module; `#` is the only true comment. The lecture already teaches docstrings later — cross-link.
- "All platforms offer free tiers": soften to "most offer free content; some are fully free" and/or trim the platform list to verifiably-free ones (official tutorial, freeCodeCamp, Kaggle Learn).
- 13.6 TeV as ATLAS dict value: relabel key/value so it reads as the LHC's Run-3 collision energy, with "(Run 3)" so it ages visibly.

**Enrichment candidates (official tutorial ch. 4-8, *Think Python*; target +6-10 slides):**
- try/except: the lecture renamed a section "Functions & Exceptions" but only shows error taxonomy — add 2 slides: catching specific exceptions around `float(input())`/file-open, and "fail loudly: don't `except:` everything".
- Tuples & unpacking: `(x, y) = pair`, swap idiom, `zip` returns tuples — 1 slide (zip is already taught; tuples currently implicit).
- Sets: dedup + membership test with a physics example (`set(detector_hits)`) — 1 slide if absent.
- Modules & imports: `import math`, `from pathlib import Path`, what `import` actually runs, standard-library tour of 4 modules relevant to the course (`math`, `pathlib`, `csv`, `json`) — 2 slides.
- String methods mini-toolkit: `.strip() .split() .join() f-strings` recap — 1 slide if scattered/absent (they're needed for the file-parsing slides).
- MCQ: mutable default argument or `is` vs `==` — pick one classic gotcha matching taught material.

- [ ] **Step 1: Read the full lecture**; drop covered candidates.
- [ ] **Step 2: Edit** — flags + additions; keep every code block runnable (monaco-run where interactive value is high, plain fence otherwise); check Monaco-run output line counts fit the frame (the slide-243 lesson: outputs render after execution — keep example outputs ≤6 lines).
- [ ] **Step 3: QA** green + shots review.
- [ ] **Step 4: Ledger** update (3 bullets).
- [ ] **Step 5: Commit** — `feat(L05): textbook-grounded content enrichment (exceptions, modules, tuples/sets)`.

### Task 10: L06 Concepts of Data Analysis

**Files:**
- Modify: `lectures/content/slides/L06_Concepts_of_Data_Analysis.md`
- Ledger: same.

**Ledger flags to resolve:**
- Clinical-trial cautionary tale: replace with a **documented** case — Reinhart–Rogoff (2010) Excel range error changing austerity-policy conclusions (Herndon et al. 2013), which is sourced and famous — or keep the current story explicitly labelled "hypothetical scenario".
- FAIR quote: attribute — "Wilkinson et al. (2016), *Scientific Data*; text via GO FAIR" on the slide.
- 23andMe: update to the teaching point — filed for bankruptcy 2025, genetic database sold (verify buyer/outcome via WebSearch) — "your data can outlive the company that collected it".
- SMART: "actionable" → "Achievable" (cite Doran's original expansion).
- Invenio: replace in the metadata-schema list with actual schemas (Dublin Core, DataCite, schema.org); Invenio can stay as an example *platform* elsewhere if useful.
- "dissertation-grade dataset" → CERN Open Data terminology ("research-grade / derived datasets").
- Overfitting MCQ: reword the "depends on the test set performance" distractor so exactly one answer is defensible.
- "Cleaning is 60–80% of the work": recast as "practitioner surveys consistently report data preparation dominates analysts' time" — folklore stated as folklore.
- Facebook iframe embed: replace with a local screenshot + link card (removes third-party iframe; the VideoPlayer convention doesn't apply to a post embed).

**Enrichment candidates (CRISP-DM; Wilson et al.; target +4-8 slides):**
- The analysis lifecycle as an explicit loop (question → acquire → clean → explore → model → communicate → back), CRISP-DM named — 1-2 slides if the lecture lacks a spine diagram.
- Types of data: structured/unstructured, quantitative/qualitative, discrete/continuous — 1 slide if not present (used by L07/L09).
- Reproducibility pyramid: same data+code → same result; new data → robust result — 1 slide tying L03/L08 practices to analysis trust.

- [ ] **Step 1: Read the full lecture** (long file, ~4000 lines); drop covered candidates.
- [ ] **Step 2: Verify** 23andMe outcome + Reinhart–Rogoff details (WebSearch).
- [ ] **Step 3: Edit** — flags + additions.
- [ ] **Step 4: QA** green + shots review (this file had the `height: 100%`-below-content overflow pattern twice — re-check any slide where content is added above a flex container).
- [ ] **Step 5: Ledger** update (9 bullets).
- [ ] **Step 6: Commit** — `feat(L06): textbook-grounded content enrichment (sourced cases, FAIR attribution, lifecycle)`.

### Task 11: L07 Data Visualisation

**Files:**
- Modify: `lectures/content/slides/L07_Data_Visualisation.md`
- Ledger: same.

**Ledger flags to resolve:**
- 12 `disabled: true` draft slides: triage each — re-enable the "What's Wrong?" legend/bar-chart series if their figures exist in `public/figures/` and they read well (they're good active-recall material); delete the rest. The colourblind one has a caption/image mismatch — fix caption if re-enabled, else delete.
- 1976 Bundestag pie: verify against Wilke ch. 10 (WebFetch clauswilke.com/dataviz/visualizing-proportions.html): the figure shows CDU/CSU 243, SPD 214, FDP 39 — three groups, SPD+FDP coalition = slim majority, not "four parties / supermajority". Correct the caption.
- Okabe-Ito caption on the rainbow-fix figure: check the referenced figure — if it's a continuous viridis-like fix, credit viridis/continuous scale, not Okabe-Ito (which is the 8-colour qualitative palette).
- Perceptual hierarchy attribution: keep Cleveland & McGill (1984) for the core ranking; add "extended by later crowdsourced replications (Heer & Bostock 2010)" one-liner.

**Enrichment candidates (Wilke chapters not yet covered; target +4-8 slides):**
- Colour use taxonomy: qualitative vs sequential vs diverging scales, when each — 1-2 slides (Wilke ch. 4) if missing.
- Log scales: when multiplicative structure demands them, one before/after figure — 1 slide (Wilke ch. 3) if missing.
- Small multiples/faceting: one slide if missing (already name-dropped in the roadmap slide).
- Common pitfalls checklist: truncated axes, dual axes, overplotting — 1 slide consolidating scattered warnings if not present.

- [ ] **Step 1: Read the full lecture** including all disabled slides; inventory their figures on disk.
- [ ] **Step 2: Verify** Bundestag + Okabe-Ito against Wilke (WebFetch).
- [ ] **Step 3: Edit** — triage + flags + additions (BrE file).
- [ ] **Step 4: QA** green + shots review (re-enabled slides need overflow checks — they were drafts).
- [ ] **Step 5: Ledger** update (4 bullets).
- [ ] **Step 6: Commit** — `feat(L07): textbook-grounded content enrichment (draft triage, colour scales, Wilke fixes)`.

### Task 12: L09 Probability and Statistics

**Files:**
- Modify: `lectures/content/slides/L09_Probability_and_Statistics.md`
- Ledger: same.

**Ledger flags to resolve:**
- "Connecting to Data Fitting" (L10 tease): L10 is unpublished — reword to a generic outlook ("these tools power model fitting, which you'll meet next") without naming an absent lecture, or cut the slide.
- Motivation mentions statistical significance while hypothesis testing is deferred: align — either add a "we'll define this rigorously when we test hypotheses" label or drop the term from motivation.
- "Pattern of patterns" quote: attribute if a source exists (it doesn't, verifiably) → present as the lecture's own aphorism (no quote layout) or attribute honestly as "folklore".
- Frontmatter `mermaid: true` with no Mermaid content: remove the key.

**Enrichment candidates (OpenIntro Statistics ch. 3-5, Blitzstein; target +6-10 slides):**
- Law of large numbers vs CLT, stated separately with one simulation figure each (existing figure assets or matplotlib-generated PNGs into `public/figures/`) — 2 slides if missing.
- Distribution zoo: binomial, Poisson, exponential, normal — when each arises in physics data (counts in a detector → Poisson) — 2 slides if coverage is thin.
- Standard error vs standard deviation: the distinction L07's uncertainty slides forward-reference — 1 slide (closes a cross-lecture promise).
- Correlation ≠ causation with a quantified example — 1 slide if missing.
- MCQ: Poisson vs binomial recognition, or SE vs SD.

- [ ] **Step 1: Read the full lecture**; drop covered candidates; confirm what L07 promised gets defined here (boxplot terms: median/IQR/quantiles; standard error; confidence interval).
- [ ] **Step 2: Edit** — flags + additions; generate any new figures with matplotlib (house dark-transparent style — check existing figure-generation scripts under `misc/python/` first).
- [ ] **Step 3: QA** green + shots review.
- [ ] **Step 4: Ledger** update (4 bullets).
- [ ] **Step 5: Commit** — `feat(L09): textbook-grounded content enrichment (LLN/CLT, distribution zoo, SE vs SD)`.

### Task 13: Cross-deck verification + ledger closeout

**Files:**
- Modify: `docs/superpowers/2026-07-02-content-review-ledger.md`

- [ ] **Step 1: Full `pnpm qa`** — expected `Measured N/N` and `✅ No overflow`.
- [ ] **Step 2: Cross-reference sweep** — grep the deck for promises: "next lecture", "later", "we define", "covered in" — every one must point at a published lecture that actually delivers. Fix stragglers.
- [ ] **Step 3: Screenshot spot-review** — read `.qa-shots/` for every lecture's new slides (batch by lecture) checking style consistency (card colours rotate, emoji-outside-bold, reveal staging).
- [ ] **Step 4: Ledger closeout** — every per-lecture flag is now ✅ RESOLVED or carries an explicit ⏸ deferral reason; course-wide section annotated as owner-decisions-still-open.
- [ ] **Step 5: Commit** — `docs: close out content-review ledger after enrichment pass` (plus any Step 2 fix commits per lecture touched).

## Self-Review (done at write time)

- Spec coverage: every lecture in the spec's source table has a task (1–12); pipeline steps 1-7 of the spec map to each task's steps; Phase 0 is already committed; non-goals are excluded (L01 grading untouched, no BrE/AmE unification, no workbook edits beyond breakage).
- Placeholders: none — every flag has its concrete resolution; enrichment candidates name exact slides/sources; "verify against file" steps are real work, not deferral (the gap analysis is intentionally in-task, per spec).
- Consistency: ledger path, commit-message pattern, and QA commands identical across tasks; slide-number caveat documented once and referenced.
