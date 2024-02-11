# Install the Python library from https://pypi.org/project/amadeus
from amadeus import *

import requests
import json

amadeus = Client(
    client_id = "VW4WHbtHi5FKIJ87hRUjVFoRQ9OkD3RA",
    client_secret = "11hTTsTumxjbEyyS",
    log_level = "warn"
)

<<<<<<< HEAD


=======
>>>>>>> 6fcdd7165c485eb894ec46001d94d5f06f421dc8
response = amadeus.shopping.flight_offers_search.get(
    # First four are required for the API
    originLocationCode='MAD',
    destinationLocationCode='ATH',
    departureDate='2024-07-26',
    adults = 2
<<<<<<< HEAD
    
)
resp = json.dumps(response.data, indent=4)
resp = json.loads(resp)

'''Data to retrive: , destination, departure and return dates,'''

prices = list(map(lambda x: float(x["price"]["grandTotal"]),resp))
cabins = list(map(lambda x: (x["travelerPricings"][0]["fareDetailsBySegment"][0]["cabin"]),resp))
currency = list(map(lambda x: (x["price"]["currency"]),resp))
departures = list(map(lambda x: (x["itineraries"][0]["segments"][0]["departure"]["iataCode"]),resp))

print(prices)
print(cabins)
print(currency)
print(departures)
=======
)
resp = json.dumps(response.data, indent=4)
resp = json.loads(resp)
print(resp)
>>>>>>> 6fcdd7165c485eb894ec46001d94d5f06f421dc8
