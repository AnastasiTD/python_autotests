import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "6c200ee93e77715f387b82d4e744d2b3"
HEADER = {"Content-Type" : "application/json" , "trainer_token":TOKEN}
TRAINER_ID = "37983"

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200
def test_piece_body():
    response = requests.get(url = f'{URL}/trainers' , params = {'trainer_id' : "37983"})
    assert response.json()["data"][0]["trainer_name"] == 'Pomello'
