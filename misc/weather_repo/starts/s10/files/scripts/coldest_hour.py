# The coldest hour in weather.csv: when it was, and how cold.
import weather

lines = weather.read_lines("data/raw/weather.csv")

coldest = weather.Hour(lines[0])
for line in lines[1:]:
    h = weather.Hour(line)
    if not h.is_missing() and h.temp < coldest.temp:
        coldest = h

print(f"coldest hour: {coldest.time}, {coldest.temp} °C")
