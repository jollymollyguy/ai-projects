import json
from re import U
import requests
# Exercise 1 — JSON manipulation. Create a dictionary of 3 freelance projects, each with keys: client, service, price, completed. Write it to a JSON file. Read it back and print only the projects where completed is False.


projects = [
    {"client": "Banana","service": "Beverage","price": 200,"completed": False},
    {"client": "Apple","service": "juice","price": 250,"completed": True},
    {"client": "Orange","service": "Milk","price": 300,"completed": True} ]

with open("tojson.json","w") as f:
    json.dump(projects, f, indent=4)
print("\n Json file written.")


with open("tojson.json", "r") as f:
    content= json.load(f)
for project in content:
    if project["completed"] == False:
        print(project)


# Exercise 2 — API + JSON combined. Call the joke API 3 times in a loop. Store each joke as a dictionary {"setup": ..., "punchline": ...} in a list. Write the entire list to a JSON file called jokes.json.

def get_joke():
    url= "https://official-joke-api.appspot.com/random_joke"
    jokes= []
    try:
        for _ in range(3):
            response= requests.get(url)
            if response.status_code == 200:
                data= response.json()
                jokes.append({"setup":data["setup"], "punchline": data["punchline"]})
            else:
                print(f"Error: {response.status_code}")
        with open("joke.json", "w") as f:
            json.dump(jokes, f, indent=4)
            print("\n3 jokes saved to jokes.json.")
            print(jokes)

    except requests.exceptions.ConnectionError:
            print("Error: No internet connection.")

get_joke()


# Exercise 3 — Build your own API caller: Go to https://restcountries.com/v3.1/name/nepal in your browser. Look at the JSON response. Write a Python function that calls this API with any country name and prints:
# Country name
# Capital city
# Population
# Region


def country_info(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    try:
        response= requests.get(url)
        if response.status_code == 200:
            data= response.json()
            print(f"\nCountry: {data[0]['name']['common']}")
            print(f"Capital: {data[0]['capital'][0]}")
            print(f"Population: {data[0]['population']}")
            print(f"Region: {data[0]['region']}")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.ConnectionError:
            print("Error: No internet connection.")

country_info("nepal")