"""Read the hourly log of the weather station."""

MISSING = -999.0

def read_lines(path):
    """The lines of a file, without its header."""
    return open(path).read().splitlines()[1:]

class Hour:
    """One line of weather.csv: its time and temperature."""

    def __init__(self, line):
        parts = line.split(",")
        self.time = parts[0]
        self.temp = float(parts[1])

    def is_missing(self):
        return self.temp == MISSING

def mean(values):
    """The mean of a list of numbers."""
    return sum(values) / len(values)
