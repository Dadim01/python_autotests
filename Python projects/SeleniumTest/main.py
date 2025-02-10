import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '99999999999999999999999999999999'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': f'{TOKEN}'
}

body_pokemon_creation={
    "name": "generate",
    "photo_id": -1
}

body_change_pokemon={
    "pokemon_id": "225377",
    "name": "generate",
    "photo_id": -1
}

body_add_pokeball={
    "pokemon_id": "225377"
}

response=requests.post(url = f"{URL}/pokemons", headers=HEADER, json=body_pokemon_creation)
print(response.text)

response_change_pokemon=requests.put(url=f"{URL}/pokemons", headers=HEADER, json=body_change_pokemon)
print(response_change_pokemon.text)

response_add_pokeball=requests.post(url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=body_add_pokeball)
print(response_add_pokeball.text)
