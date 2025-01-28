import requests
import json

API_KEY = "1ae51530df5b7b5d0ef43220787caef9"
#CITY = "Kolkata"  # Change to user's location
LAT = "28"  # Latitude of Kolkata
LON = "60"  # Longitude of Kolkata

def fetch_aqi():
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        aqi_value = data['list'][0]['main']['aqi']
        print(f"Current AQI: {aqi_value}")
        print(f"Latitude: {LAT}, Longitude: {LON}")
        return aqi_value
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

