"""Rebuild every result that is out of date: python run_all.py"""
import os
import subprocess
import sys

RAW = "data/raw/pendulum.csv"
TABLE = "data/processed/pendulum.csv"
PLOT = "results/pendulum_plot.png"
FIT = "results/fit.json"
REPORT = "results/report.md"

# One line per stage: the script, what it reads, what it writes.
STAGES = [
    ("scripts/clean.py", [RAW], TABLE),
    ("scripts/plot.py", [TABLE], PLOT),
    ("scripts/fit.py", [TABLE, "config.json"], FIT),
    ("scripts/report.py", [TABLE, FIT, PLOT], REPORT),
]


def out_of_date(output, sources):
    """True if output is missing or older than a source."""
    if not os.path.exists(output):
        return True
    built = os.path.getmtime(output)
    for source in sources:
        if os.path.getmtime(source) > built:
            return True
    return False


tests = subprocess.run([sys.executable, "-m", "pytest", "-q"])
if tests.returncode != 0:
    sys.exit("tests failed, nothing rebuilt")

for script, inputs, output in STAGES:
    if out_of_date(output, [script] + inputs):
        os.makedirs(os.path.dirname(output), exist_ok=True)
        command = [sys.executable, script] + inputs + [output]
        done = subprocess.run(command)
        if done.returncode != 0:
            sys.exit(f"{script} failed, stopped")
    else:
        print(f"{output}: up to date", flush=True)
