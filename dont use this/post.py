# Imports
from amadeus import *

import requests
import json
import csv

# Initiates Amadeus + Authentication
amadeus = Client(
    client_id = "VW4WHbtHi5FKIJ87hRUjVFoRQ9OkD3RA",
    client_secret = "11hTTsTumxjbEyyS",
    log_level = "debug"
)


## .get
'''APIResponse = amadeus.shopping.flight_offers_search.get(
    # First four are required for the API
    originLocationCode='MAD',
    destinationLocationCode='ATH',
    departureDate='2024-07-26',
    adults = 2,
    returnDate
)
'''
### Below is just assuming the user inputted these values, will change later on what to do for implementation

'''originCity = 
originState =
originCountry =

destinationCity =
destinationState =
destinationCountry = 
'''

# (YYYY-MM-DD)
dateOfDeparture = "2024-11-01"
# 24 Hour Format
timeOfDeparture = "10:00:00"

#destCode = 
#originCode = 


#.push
'''
APIResponse = amadeus.shopping.flight_offers_search.post(
    {
        "originDestinations" : [
            {
                "id": "1",
                "departureDateTimeRange": {
                    "date": dateOfDeparture,
                    "time": timeOfDeparture
                },
                "destinationLocationCode": destCode,
                "originLocationCode": originCode
            },
        ],
        "travelers": [
            {
                # ID Is probably for differing all people attending a flight
                "id": "1",
                # One Adult Required for Travel
                "travelerType": "ADULT"
            }
        ],
        "sources": [
            # Keep it at default
            "GDS"
        ]
    }

)
'''
 
apijson = json.dumps(APIResponse.data, indent=4)

