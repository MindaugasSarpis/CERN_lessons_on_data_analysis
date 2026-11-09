"""Read the hourly log of the weather station."""

MISSING = -999.0

def read_lines(path):
    return open(path).read().splitlines()[1:]

def temp_of(line):
    return float(line.split(",")[1])

def temps(path):
    result = []
    for line in read_lines(path):
        temp = temp_of(line)
        if temp != MISSING:
            result.append(temp)
    return result

def mean(values):
    return sum(values) / len(values)

def group(path, start, stop):
    """A list of temperatures for each key line[start:stop]."""
    groups = {}
    for line in read_lines(path):
        temp = temp_of(line)
        if temp == MISSING:
            continue
        key = line[start:stop]
        if key not in groups:
            groups[key] = []
        groups[key].append(temp)
    return groups

def word_for(temp):
    """The word for a mean temperature in °C."""
    if temp < 0:
        return "cold"
    if temp < 10:
        return "cool"
    if temp < 15:
        return "mild"
    return "warm"
