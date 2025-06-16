import requests
import os

class WeatherAgent:
    def enrich(self, input_data):
        lat, lon = input_data["lat"], input_data["lon"]
        api_key = os.getenv("OPENWEATHER_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        res = requests.get(url)
        weather = res.json()
        input_data["weather"] = weather["weather"][0]["description"]
        input_data["temperature"] = weather["main"]["temp"]
        return input_data