import requests

api_url = 'https://pokeapi.co/api/v2/'

def getPokemon(name):
	url = f"{api_url}/pokemon/{name}"
	response = requests.get(url) #Fetch info from url

	if response.status_code == 200:
		print("Success")
		pokemon_data = response.json() #Transform data to json
		return pokemon_data

	else:
		print(f"Failed to retrieve {response.status_code}")

pokemon_info = getPokemon("articuno")

if pokemon_info:
	print(f"{pokemon_info["name"]}") #Use hashmap properties to access JSON data
	print(f"{pokemon_info["id"]}")
	print(f"{pokemon_info["weight"]}")
	print(f"{pokemon_info["abilities"][0]["ability"]["name"]}")
