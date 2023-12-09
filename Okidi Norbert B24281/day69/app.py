import requests

def get_weather_forecast(city):
    api_key = "d7b02308f0de12e46bfc3abfe99ffe28"
    endpoint = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(endpoint)
    data = response.json()
    return data

def display_weather_forecast():
    city = input("Enter the city: ")
    forecast_data = get_weather_forecast(city)

    for entry in forecast_data['list']:
        date = entry['dt_txt']
        temperature = entry['main']['temp']
        humidity = entry['main']['humidity']
        wind_speed = entry['wind']['speed']
        weather_conditions = entry['weather'][0]['description']

        print(f"On {date}:")
        print(f"  Temperature: {temperature}°C")
        print(f"  Humidity: {humidity}%")
        print(f"  Wind Speed: {wind_speed} m/s")
        print(f"  Weather Conditions: {weather_conditions}\n")

display_weather_forecast()
