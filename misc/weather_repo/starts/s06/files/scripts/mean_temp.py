import weather

temps = []
for line in weather.read_lines("data/raw/weather.csv"):
    h = weather.Hour(line)
    if not h.is_missing():
        temps.append(h.temp)

print(f"{len(temps)} hours, mean {weather.mean(temps):.1f} °C")
