# Seminar 15 — Run Your Pipeline at Scale *(optional)*

**Paired lecture:** 15 Computing Infrastructure & HPC · **Format:** hackathon · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **Running project — this session adds:** your pipeline run as a batch/remote-style
> job. *Optional / advanced — skip if short on time.*

## Goal
Move from "runs on my laptop, in my terminal" to "runs unattended, somewhere else,
and I collect the results" — the mindset behind HPC and the WLCG.

## Prerequisites
Seminar 14 (a working `make all` pipeline).

## Tasks
1. Make the pipeline **non-interactive**: no prompts, all inputs from config/args,
   all outputs to files.
2. Wrap it in a job script (`run_job.sh`) and launch it detached:
   `nohup make all > run.log 2>&1 &` — then inspect `run.log`.
3. Scale it: run the analysis over a 10× larger sample (or loop over several input
   files), timing each. Where is the bottleneck — CPU, memory, or disk I/O?
4. If a real scheduler is available (Slurm/HTCondor), submit the job to it and
   retrieve the results.
5. Instrument task 3's timing properly: wrap the run in `/usr/bin/time -v make all`
   (or watch `top`/`htop` in another pane) and record peak memory alongside the
   wall-clock time you already measured — does the number confirm your bottleneck guess?
6. Namespace the output so concurrent jobs never clobber each other, the way batch
   systems do: write results to `results/run_$(date +%s)/` (or a job-ID directory)
   instead of overwriting `results/` in place.

## Stretch goals
- Parallelise the per-file step (GNU `parallel`, or Python `multiprocessing`).
- Estimate the resources to process the full LHCb dataset (billions of events).
- Add simple retry logic to `run_job.sh` (rerun once on a non-zero exit) — a taste of
  the fault-tolerance batch systems provide automatically.

## Wrap-up (last 10 min)
- Re-run `run_job.sh` once more into a fresh namespaced output directory and confirm
  it reproduces the same numbers as your interactive runs.
- Commit the job script and a sample `run.log`:
  `git add -A && git commit -m "Add batch-style pipeline run"`.
- Note one lesson in the README, e.g. what surprised you about resource use at 10×
  scale.

## Solution notes (instructor)
The transferable idea: a reproducible, automated pipeline is exactly what scales to
a cluster — you built the hard part in Seminar 14. Keep it lightweight if no HPC is
on hand; `nohup` + `run.log` is enough to make the point. This seminar is optional —
in a short 120-minute slot, protect task 3's scaling/timing as the highest-value 20
minutes and treat the scheduler submission (task 4) and tasks 5–6 as stretch before
letting the `nohup` mechanics of task 2 eat the room's time.

## Aims practised
⚙️ unattended automation · 🔧 same pipeline, bigger machine · ♻️ still reproducible
