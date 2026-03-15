import json
import requests

# ── PART 1: JSON ───────────────────────────────────────────

# PYTHON DICT → JSON STRING
client = {
    "name": "Himalayan Treks",
    "industry": "trekking",
    "budget": 300,
    "paid": True
}

json_string = json.dumps(client)
print("Dict → JSON String:")
print(json_string)
print(type(json_string))

# JSON STRING → PYTHON DICT
json_data = '{"name": "Pokhara Adventures", "budget": 500, "paid": false}'
python_dict = json.loads(json_data)
print("\nJSON String → Dict:")
print(python_dict)
print(type(python_dict))
print(python_dict["name"])

# WRITE JSON TO FILE
with open("client_data.json", "w") as f:
    json.dump(client, f, indent=4)
print("\nJSON file written.")

# READ JSON FROM FILE
with open("client_data.json", "r") as f:
    loaded = json.load(f)
print("JSON file loaded:")
print(loaded)
print(loaded["industry"])


# ── PART 2: REQUESTS LIBRARY ───────────────────────────────

response = requests.get("https://httpbin.org/get")
print("\nStatus Code:", response.status_code)
print("Response Type:", type(response))
print("Response Data:", response.json())


# ── PART 3: JOKE API ───────────────────────────────────────

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


# ── PART 4: WEATHER API ────────────────────────────────────

API_KEY = "your_api_key_here"  # store in .env in real projects

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