import requests

API_KEY = <API_KEY>
BASE_URL = "https://api.weatherapi.com/v1/current.json"

while True:
    location = input("Enter a location: ").strip()
    
    if not location:
        print("Please enter a valid location.")
        continue
    
    params = {"key": API_KEY, "q": location}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        loc = data["location"]
        current = data["current"]
        
        print(f"\nLocation: {loc['name']}, {loc['country']}")
        print(f"Temperature: {current['temp_c']}°C")
        print(f"Condition: {current['condition']['text']}")
        print(f"Humidity: {current['humidity']}%\n")
    else:
        print("Please enter a valid location.\n")
