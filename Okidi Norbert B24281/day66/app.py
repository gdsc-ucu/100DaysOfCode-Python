import requests

def get_weather_data(city):
    api_key = "d7b02308f0de12e46bfc3abfe99ffe28"
    endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        data = response.json()
        main_weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather in {city}: {main_weather} - {description}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Error: Unable to fetch weather data for {city}")


user_city = input("Enter the city: ")
get_weather_data(user_city)
