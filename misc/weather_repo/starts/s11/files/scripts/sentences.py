"""Write the months of weather.csv as sentences, one per month:

    in july it was warm .

The word comes from the month's mean temperature (weather.word_for).
data/processed/months.txt holds the twelve months of 2016 to 2025 together,
data/processed/months_by_year.txt each of the 120 months.

Usage, from the project folder:

    python scripts/sentences.py
"""
import weather

PATH = "data/raw/weather.csv"
NAMES = ["january", "february", "march", "april", "may", "june", "july",
         "august", "september", "october", "november", "december"]


def write(groups, path):
    lines = []
    for key in groups:
        name = NAMES[int(key[-2:]) - 1]
        word = weather.word_for(weather.mean(groups[key]))
        lines.append("in " + name + " it was " + word + " .")
    with open(path, "w", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(len(lines), "sentences in", path)


write(weather.group(PATH, 5, 7), "data/processed/months.txt")
write(weather.group(PATH, 0, 7), "data/processed/months_by_year.txt")
