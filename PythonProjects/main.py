import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "6c200ee93e77715f387b82d4e744d2b3"
HEADER = {"Content-Type" : "application/json" , "trainer_token":TOKEN}

body_pokemons = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_pokeball = {
    "pokemon_id": "315511"
}
body_name = {
    "pokemon_id": "315511",
    "name": "MIU",
    "photo_id": 2
}

'''response_pokemons = requests.post(url = f"{URL}/pokemons" , headers = HEADER , json = body_pokemons)

print(response_pokemons.json)
pokemon_id = response_pokemons.json()['id']
print(pokemon_id)'''

response_name = requests.put(url = f"{URL}/pokemons" , headers = HEADER , json = body_name)

print(response_name.json)

response_pokeball = requests.post(url = f"{URL}/trainers/add_pokeball" , headers = HEADER , json = body_pokeball)

print(response_pokeball.json)
