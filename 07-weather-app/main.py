import requests

API_KEY = "515f61fdbd71a9bd240506e136fc8fd4"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    print("\nWeather Information")
    print("----------------------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
    print("Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("Error:", data.get("message", "Unable to fetch weather data."))
