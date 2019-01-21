import json
from urllib.request import urlopen

gdzie= input("Podaj lokalizacje: ")

with urlopen(f"https://www.metaweather.com/api/location/search/?query={gdzie}") as file:
    data=json.loads(file.read().decode("utf-8"))

print(data)
woeid = data[0]["woeid"]
print(woeid)


with urlopen(f"https://www.metaweather.com/api/location/{woeid}")as f:
    data = json.loads(f.read().decode("utf-8"))

print(data)

prognozy = data["consolidated_weather"]
for prognoza in prognozy:
    print(f"Dzień: {prognoza['applicable_date']}")
    print(f"Temperatura: {prognoza['the_temp']:0f}C")
    print(f"Wilgotnosc: {prognoza['humidity']:0f}C")