
import requests

API_KEY = 'd7c400146cdd92fdeb56a36aeddfc297'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def weather(city):
    """
    Fetches and returns the weather information for the specified city using OpenWeatherMap API.

    :param city: Name of the city
    :return: A dictionary containing location, weather description, and temperature
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        res = requests.get(BASE_URL, params=params)
        res.raise_for_status()
        data = res.json()

       # print("API response:", data)

        location = data['name']
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return {
            "location": location,
            "description": weather_description,
            "temperature": f"{temperature}°C"
        }
    except Exception as e:
        print("Error fetching weather data:", e)
        return None

city = input("Enter the Name of City -> ")
weather_info = weather(city)
if weather_info:
    print(weather_info)
print("Have a Nice Day:)")

# This code is contributed by adityatri, with enhancements
