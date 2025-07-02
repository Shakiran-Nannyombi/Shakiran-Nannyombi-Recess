#create account from https://openweathermap.org/api_keys

import requests
import pandas as pd

API_KEY = "b6baa485eac26cdfa79e3d0e4ae01225"

# Current weather API endpoint
API_url = f"http://api.openweathermap.org/data/2.5/weather?lat={{lat}}&lon={{lon}}&APPID={API_KEY}"

lat = 0.347596  # Kampala, Uganda
lon = 32.582520

response = requests.get(API_url.format(lat=lat, lon=lon))
if response.status_code == 200:
    data = response.json()
    print("Data retrieved successfully!")
    
    # Create DataFrame from the main weather data
    df = pd.DataFrame([data])  # Wrap in list for single record
    print(df.head())
    
    df.to_csv('climate_data.csv', index=False)
    print("Data saved to 'climate_data.csv'")
else:
    print(f"Error: {response.status_code}")
    print(response.text)

# get for multiple cities
cities = ["Kampala", "Nairobi", "Dar es Salaam", "Kigali", "Bujumbura","Congo", "Juba", "Mogadishu", "Addis Ababa", "Asmara"]
city_data = []
for city in cities:
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        city_data.append(data)
    else:
        print(f"Error retrieving data for {city}: {response.status_code}")

# Create DataFrame from the list of city weather data
if city_data:
    df_cities = pd.DataFrame(city_data)
    df_cities.to_csv('climate_data_cities.csv', index=False)
    print("Data saved to 'climate_data_cities.csv'")
else:
    print("No data retrieved for cities.")