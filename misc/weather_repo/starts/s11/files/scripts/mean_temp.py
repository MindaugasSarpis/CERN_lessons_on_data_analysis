import weather

total = 0.0
count = 0
for line in weather.read_lines("data/raw/weather.csv"):
    temp = weather.temp_of(line)
    if temp == weather.MISSING:
        continue
    total = total + temp
    count = count + 1

print(f"{count} hours, mean {total / count:.2f} °C")
