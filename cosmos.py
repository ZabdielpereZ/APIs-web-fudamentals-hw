import requests
import json


import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = (planet["englishName"].title()) #get planet English name
            mass = (planet["mass"]["massValue"])#get planet mass
            orbit_period = (planet["sideralOrbit"]) #get planet orbit period
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

print('=' * 80)

import requests

def fetch_planet_data(planet_name):
    response = requests.get(f"https://api.le-systeme-solaire.net/rest/bodies/{planet_name.lower()}")
    if response.status_code == 200:
        planet = response.json()
        if "mass" in planet:
            planet_data = {
                "englishName": planet["englishName"],
                "mass": {
                    "massValue": planet["mass"]["massValue"]
                },
                "sideralOrbit": planet["sideralOrbit"]
            }
            return planet_data
        else:
            return {"error": f"Mass data not available for {planet_name}."}
    else:
        return {"error": f"Planet {planet_name} not found."}

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda planet: planet["mass"]["massValue"])
    return heaviest_planet["englishName"], heaviest_planet["mass"]["massValue"]

planet_names = ["uranus", "neptune", "jupiter", "mars", "mercury", "saturn", "earth", "venus"]

planet_data = [fetch_planet_data(planet) for planet in planet_names]

# Filter out any errors
planet_data = [planet for planet in planet_data if "error" not in planet]

if planet_data:
    heaviest_planet_name, heaviest_planet_mass = find_heaviest_planet(planet_data)
    print(f"The heaviest planet is {heaviest_planet_name} with a mass of {heaviest_planet_mass} kg.")

    for planet in planet_data:
        name = planet["englishName"]
        mass = planet["mass"]["massValue"]
        print(f"Name: {name}")
        print(f"Mass: {mass} kg")
        print()
else:
    print("No valid planet data found.")