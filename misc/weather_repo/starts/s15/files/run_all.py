"""Make data/processed and results from data/raw: python run_all.py"""
import hashlib
import os
import subprocess
import sys

# One line per stage: the words after `python`, and the file for its output.
STAGES = [
    (["scripts/drop_missing.py"], None),
    (["scripts/clean_export.py", "data/raw/daily_export.csv",
      "data/processed/daily.csv"], None),
    (["scripts/column_stats.py", "data/processed/weather_valid.csv",
      "temp_c"], "results/temp_c.txt"),
    (["scripts/clean_hill.py"], "results/hill.txt"),
    (["-m", "pytest", "-q"], None),
]
os.makedirs("results", exist_ok=True)
for words, output in STAGES:
    print("==", " ".join(words), flush=True)
    done = subprocess.run([sys.executable] + words,
                          capture_output=True, text=True)
    print(done.stdout + done.stderr, end="")
    if done.returncode != 0:
        sys.exit(f"stopped: exit code {done.returncode}")
    if output:
        with open(output, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(done.stdout)
# The checksum of every file made: the same digits on every laptop.
for folder in ["data/processed", "results"]:
    for name in sorted(os.listdir(folder)):
        path = f"{folder}/{name}"
        with open(path, "rb") as handle:
            digest = hashlib.sha256(handle.read()).hexdigest()
        print(digest[:12], path)
