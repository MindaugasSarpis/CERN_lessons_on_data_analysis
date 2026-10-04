#!/bin/bash
#SBATCH --job-name=sum_mass       # the name shown in the queue
#SBATCH --output=logs/%x_%j.log   # the log: %x is the name, %j the job number
#SBATCH --time=00:10:00           # limit hh:mm:ss, the job is stopped after it
#SBATCH --cpus-per-task=4         # cores, all on one node
#SBATCH --mem=2G                  # memory limit for the whole job

set -e                            # stop at the first command that fails
source .venv/bin/activate         # the environment of the project
echo "$(date +%H:%M:%S)  start on $(hostname), job $SLURM_JOB_ID"
python -u scripts/sum_parallel.py --workers "$SLURM_CPUS_PER_TASK"
echo "$(date +%H:%M:%S)  done"
