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

def evenings(path):
    """[date, temperature, humidity, frost] for each evening: 18:00 of a day
    beside 06:00 of the next. frost is 1 when 06:00 is below 0 °C, else 0."""
    lines = read_lines(path)
    result = []
    for i in range(18, len(lines) - 12, 24):    # 24 lines a day, 18:00 first
        evening = lines[i].split(",")
        temp = float(evening[1])
        humidity = float(evening[2])
        morning = temp_of(lines[i + 12])        # 12 hours later: 06:00
        if temp == MISSING or morning == MISSING:
            continue
        frost = 0
        if morning < 0:
            frost = 1
        result.append([evening[0][0:10], temp, humidity, frost])
    return result
