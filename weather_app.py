import streamlit as st
import requests

# OpenWeather API key (replace with your actual key)
API_KEY = "cb16f0ab1e62cb16695b4b9ffcab00da"

# Function to get weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Wind Speed": f"{data['wind']['speed']} m/s",
        }
        return weather_info
    else:
        return None

# Streamlit UI
st.set_page_config(page_title="Weather App", page_icon="⛅")
st.title("🌤️ Weather App")

city = st.text_input("🏙️ Enter City Name", "New Delhi")

if st.button("Get Weather"):
    weather = get_weather(city)

    if weather:
        st.subheader(f"Weather in {weather['City']}")
        
        # Using columns for better layout
        col1, col2, col3 = st.columns(3)
        col1.metric("🌡️ Temperature", weather["Temperature"])
        col2.metric("💧 Humidity", weather["Humidity"])
        col3.metric("🌬️ Wind Speed", weather["Wind Speed"])

        # Display weather description
        st.markdown(f"**Condition:** {weather['Weather']}")
    else:
        st.error("❌ City not found. Please enter a valid city name.")
