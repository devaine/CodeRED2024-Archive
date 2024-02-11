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
    originLocationCode='BOS',
    destinationLocationCode='JFK',
    departureDate='2024-06-06',
    adults = 2,
    returnDate='2024-06-06',
    nonStop='true'

    
)
resp = json.dumps(response.data, indent=4)
resp = json.loads(resp)

'''Data to retrive:, departure and return dates,'''

prices = list(map(lambda x: float(x["price"]["grandTotal"]),resp))
cabins = list(map(lambda x: (x["travelerPricings"][0]["fareDetailsBySegment"][0]["cabin"]),resp))
currency = list(map(lambda x: (x["price"]["currency"]),resp))
departures = list(map(lambda x: (x["itineraries"][0]["segments"][0]["departure"]["iataCode"]),resp))
oneStop = list(map(lambda x: (x["oneWay"]), resp))
destination = list(map(lambda x: (x["itineraries"][0]["segments"][0]["arrival"]["iataCode"]),resp))
departureTimes = list(map(lambda x: (x["itineraries"][0]["segments"][0]["departure"]["at"]),resp))

'''print(prices)
print(cabins)
print(currency)
print(departures)
print(oneStop)
print(destination)
print(departureTime)'''

class ticket:
    def __init__(self,price,cabin,currency,departure,oneStop,departureTime):
        self.price=price
        self.cabin=cabin
        self.currency=currency
        self.departure=departure
        self.oneStop=oneStop
        self.departuretime=departureTime

    def __str__(self):
        print(f"{self.price},{self.cabin},{self.currency},{self.departure},{self.oneStop},{self.departuretime}")


tickets=[]
length=len(prices)

for i in  range (length):
    tempTicket = ticket(prices[i],cabins[i],currency[i],departures[i],oneStop[i],departureTimes[i])
    tickets.append(tempTicket)


for i in range (length):
    print(tickets[i].__str__())

