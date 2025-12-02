import csv
import requests

API_KEY = 'a2e0081410a554ea375bb1854dfa33c3'  # Your Weatherstack key
CITY = 'London'
BASE_URL = 'http://api.weatherstack.com/current'

params = {
    'access_key': API_KEY,
    'query': CITY
}

response = requests.get(BASE_URL, params=params)
data = response.json()
print(data)  # Debug: See what you get

# Extract relevant data
weather_data = [[
    data.get('location', {}).get('name', ''),
    data.get('current', {}).get('temperature', ''),
    data.get('current', {}).get('humidity', ''),
    data.get('current', {}).get('weather_descriptions', [''])[0],
    data.get('current', {}).get('wind_speed', '')
]]

with open('weather_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['City', 'Temperature (C)', 'Humidity (%)', 'Weather Description', 'Wind Speed (km/h)'])
    writer.writerows(weather_data)

print("Weather data saved to weather_data.csv")