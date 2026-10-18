"""Read the hourly log of the weather station."""

MISSING = -999.0

def read_lines(path):
    """The lines of a file, without its header."""
    return open(path).read().splitlines()[1:]

def temp_of(line):
    """The temp_c of one line of weather.csv."""
    return float(line.split(",")[1])
