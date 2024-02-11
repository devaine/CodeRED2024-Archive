# Install the Python library from https://pypi.org/project/amadeus
from amadeus import *

import requests
import json

amadeus = Client(
    client_id = "VW4WHbtHi5FKIJ87hRUjVFoRQ9OkD3RA",
    client_secret = "11hTTsTumxjbEyyS",
    log_level = "warn"
)

response = amadeus.shopping.flight_offers_search.get(
    # First four are required for the API
    originLocationCode='MAD',
    destinationLocationCode='ATH',
    departureDate='2024-07-26',
    adults = 2
)
resp = json.dumps(response.data, indent=4)
resp = json.loads(resp)
print(resp)