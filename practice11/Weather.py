import requests
import json
from datetime import datetime

class Weather:

    def __init__(self, city):
        self.city = city
        self.datalist = []

    def addCityToUrl(self):
        return f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f"

    def getWeather(self):
        res = requests.get(self.addCityToUrl())
        data = json.loads(res.text)
        temp = int(data["main"]["temp"])
        weat = data["weather"][0]["description"]
        hum = data["main"]["humidity"]
        wind = int(data["wind"]["speed"])
        pres = data["main"]["pressure"]
        self.datalist = [temp, str(weat), hum, wind, pres]
        return self.datalist


    def recordToFile(self):
        now = datetime.now()
        curtime = now.strftime("%H:%M:%S")
        data = self.getWeather()
        with open("secondHalfyear/prak11/weatherReport", "a") as file:
            file.write(
f"""
______________________________________________

[{curtime}] Запрос погоды в городе: {self.city}
            
Температура: {data[0]}C, {data[1].capitalize()}
            
Влажность воздуха: {data[2]}%
            
Скорость ветра: {data[3]} м/с
            
Атмосферное давление: {data[4]} мм рт.ст.

______________________________________________
""")
            file.close()



