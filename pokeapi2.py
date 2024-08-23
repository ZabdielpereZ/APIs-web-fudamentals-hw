import requests
import json


response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu") # Request information from our API

json_data = response.text
print(json_data)

poke_data = response.json() 
print(poke_data)

print(poke_data["name"].title()) # pokemon name 
print(poke_data["types"][0]["type"]["name"]) # pokemon type
print(poke_data["abilities"][0]["ability"]["name"]) # pokemon ability

print('='*70)

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}") # Request information from our API
    return response.json() #json response

# Function to calculate the average weight of a list of Pokémon
def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list) #average weight of pokemon

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

# Fetch data for each Pokémon
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

# Calculate the average weight
average_weight = calculate_average_weight(pokemon_data)

# Print the names, abilities, and average weight of the Pokémon
for pokemon in pokemon_data:
    name = pokemon['name']
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    print(f"Name: {name}")
    print(f"Abilities: {', '.join(abilities)}")
    print()

print(f"Average Weight: {average_weight}")