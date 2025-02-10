import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' : 'application/json'
}

def test_status_code():
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id' : '18552'})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : '18552'})
    assert response_get.json()["data"][0]["trainer_name"] == 'Dadim80'
