import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import json


# -------------------------
# zadanie 1

def check_url(url: str) -> bool:
    response = requests.get(url)
    return response.status_code >= 200 and response.status_code < 300


# -------------------------
# zadanie 2

miasto = "olsztyn"

weather_url = f"https://www.meteoprog.pl/pl/weather/{miasto}/"
w_res = requests.get(weather_url)

w_s = BeautifulSoup(w_res.content.decode('utf-8'), features="html.parser")
temp_div = w_s.find("div", class_='current-temperature')
temp_today = temp_div.find("div", class_='today-temperature').find("span").text

temp_inne = temp_div.find("ul", class_="today-hourly-weather")
inne_temp = [
    (x.find("span", class_="today-hourly-weather__name").text,  int(x.find("span", class_="today-hourly-weather__temp").text[:-1]))
    for x in temp_inne.find_all("li")
]

for x in inne_temp:
    print(x)

plt.plot(pd.Series(data={ x: y for (x, y) in inne_temp}, index=[x for (x, y) in inne_temp]))
plt.ylabel("temperatura")
plt.show()


# -------------------------
# zadanie 3

stacja_id = 5766
api_url = f'https://api.gios.gov.pl/pjp-api/rest/data/getData/{stacja_id}'

response = requests.get(api_url)

api_json = json.loads(response.content.decode("utf-8"))
api_values = [(x["date"], float(x["value"])) for x in api_json["values"] if x["value"] is not None]

api_valueseries = pd.Series(
    data={x: y for (x,y) in api_values}, 
    index=[x for (x,y) in api_values])

plt.plot(api_valueseries)
plt.ylabel("pomiar")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# -------------------------
# zadanie 4

# na pewno jest to czytanie jsonów....
# strony html częściej i bardziej się zmieniają
