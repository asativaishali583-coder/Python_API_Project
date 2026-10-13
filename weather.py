import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print("Weather Information:")
            print(response.text)
        else:
            print("Error: Weather data not found.")

    except requests.exceptions.RequestException:
        print("Error: Please check your internet connection.")

city = input("Enter city name: ").strip()

if city:
    get_weather(city)
else:
    print("Please enter a city name.")


























