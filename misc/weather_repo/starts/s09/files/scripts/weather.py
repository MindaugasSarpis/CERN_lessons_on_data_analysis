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
