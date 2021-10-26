import requests
import json
from connect_with_db import get_database


API_KEY = 'api_key'  # ADD THE API KEY HERE
API_END_POINT = "https://api.openweathermap.org/data/2.5/weather"


def search_data(search_data_file_path):
    cities_lat_lon = []
    with open(f'{search_data_file_path}', 'r') as file:
        input_data = json.load(file)
    for key, value in input_data.items():
        cities_lat_lon.append(value)
    return cities_lat_lon


def get_weather_data(lat, lon, api_key=API_KEY):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
    }
    weather_data = requests.get(url=API_END_POINT, params=params).json()
    return weather_data


result = []
search_data = search_data('cities.json')
for item in search_data:
    result.append(get_weather_data(item['lat'], item['lon']))

# connection with db and adding the result
db = get_database("weather")
collection_name = db["weather_api_result"]
collection_name.insert_many(result)
