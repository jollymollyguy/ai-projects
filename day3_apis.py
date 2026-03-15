import requests

# ── Block 2: Basic Request ─────────────────────────────────

response = requests.get("https://httpbin.org/get")
print("Status Code:", response.status_code)
print("Response Type:", type(response))
print("Response Data:", response.json())


# ── Block 3: Joke API ──────────────────────────────────────

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\nSetup: {data['setup']}")
            print(f"Punchline: {data['punchline']}")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")

    get_joke()

        
# ── Block 4: Weather API ───────────────────────────────────

API_KEY = "your_api_key_here"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\nCity: {data['name']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
        else:
            print(f"Error: {response.status_code} - City not found.")
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")

get_weather("Kathmandu")
get_weather("Pokhara")      