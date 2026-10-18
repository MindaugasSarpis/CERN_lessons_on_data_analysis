# The coldest hour in weather.csv: when it was, and how cold.
lines = open("data/raw/weather.csv").read().splitlines()

coldest = 100.0
coldest_time = ""
for line in lines[1:]:
    parts = line.split(",")
    temp = float(parts[1])
    if temp < coldest:
        coldest = temp
        coldest_time = parts[0]

print(f"coldest hour: {coldest_tme}, {coldest} °C")
