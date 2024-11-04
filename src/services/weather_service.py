import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return round(kelvin - 273.15, 1)

    @staticmethod
    def get_weather(city):
        """
        Get weather data for a city using OpenWeatherMap API.
        """
        if not WeatherService.API_KEY:
            raise ValueError("OpenWeatherMap API key not found. Please set OPENWEATHER_API_KEY in .env file.")

        params = {
            'q': city,
            'appid': WeatherService.API_KEY,
        }

        try:
            response = requests.get(WeatherService.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

            return {
                'temperature': f"{WeatherService.kelvin_to_celsius(data['main']['temp'])}°C",
                'condition': data['weather'][0]['main'],
                'humidity': f"{data['main']['humidity']}%",
                'wind_speed': f"{data['wind']['speed']} m/s",
                'description': data['weather'][0]['description'].capitalize(),
                'feels_like': f"{WeatherService.kelvin_to_celsius(data['main']['feels_like'])}°C"
            }

        except requests.RequestException as e:
            raise Exception(f"Failed to fetch weather data: {str(e)}")