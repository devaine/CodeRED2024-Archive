# Install the Python library from https://pypi.org/project/amadeus
from amadeus import Client, ResponseError

import requests
import json

token = 'tM2fsmUbRliFICATKxVuQgM9aowX'
headers = {'Authorization': 'Bearer ' + token}

resp = requests.get('https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=BOS&destinationLocationCode=MAD&departureDate=2024-07-10&returnDate=2024-07-14&adults=1&nonStop=false&max=250', headers=headers)

offers = resp.json()["data"]

print(offers)

prices = list(map(lambda x: float(x["price"]["grandTotal"]),offers))
print(prices)