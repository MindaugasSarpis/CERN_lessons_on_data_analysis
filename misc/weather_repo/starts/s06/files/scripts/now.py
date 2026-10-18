import json
import urllib.request

URL = ("https://api.open-meteo.com/v1/forecast"
       "?latitude=54.69&longitude=25.28&current=temperature_2m,wind_speed_10m")

with urllib.request.urlopen(URL) as response:
    data = json.load(response)

print(type(data))
print(data["current"])
print(f"Vilnius now: {data['current']['temperature_2m']} °C")
