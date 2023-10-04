import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd

# -------------------------
# zadanie 1

def check_url(url: str) -> bool:
    response = requests.get(url)
    return response.status_code >= 200 and response.status_code < 300

# -------------------------
# zadanie 2

weather_url = "https://www.meteoprog.pl/pl/weather/Olsztyn/"
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

#print(inne_temp)