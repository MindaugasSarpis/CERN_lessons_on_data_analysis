#!/bin/bash
#SBATCH --job-name=warmest        # the name shown in the queue
#SBATCH --output=logs/%x_%j.log   # the log: %x is the name, %j the job number
#SBATCH --time=00:05:00           # the job is stopped after 5 minutes
#SBATCH --cpus-per-task=4         # four cores, all on one node
#SBATCH --mem=1G                  # memory for the whole job

# A job script for a cluster that runs Slurm. Submit it from the project
# folder, on the cluster:  mkdir -p logs; sbatch scripts/warmest_job.sh
# Lines that start with # are comments for bash; Slurm reads #SBATCH lines.

set -e                                 # stop at the first error
eval "$(conda shell.bash hook)"        # make `conda activate` work here
conda activate weather
echo "start on $(hostname), job $SLURM_JOB_ID"
python scripts/warmest.py --workers "$SLURM_CPUS_PER_TASK"
echo "done"
