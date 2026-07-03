# Seminar 15 — Run Your Pipeline at Scale *(optional)*

**Paired lecture:** 15 Computing Infrastructure & HPC · **Format:** hackathon · **~90 min**

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

## Stretch goals
- Parallelise the per-file step (GNU `parallel`, or Python `multiprocessing`).
- Estimate the resources to process the full LHCb dataset (billions of events).

## Solution notes (instructor)
The transferable idea: a reproducible, automated pipeline is exactly what scales to
a cluster — you built the hard part in Seminar 14. Keep it lightweight if no HPC is
on hand; `nohup` + `run.log` is enough to make the point.

## Aims practised
⚙️ unattended automation · 🔧 same pipeline, bigger machine · ♻️ still reproducible
