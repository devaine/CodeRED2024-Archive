from amadeus import Client

# Initialize Amadeus client
amadeus = Client(
    client_id="VW4WHbtHi5FKIJ87hRUjVFoRQ9OkD3RA",
    client_secret="11hTTsTumxjbEyyS",
    log_level="warn"
)

def get_flight_options(departure_city, arrival_city, departure_date, adults):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=departure_city,
            destinationLocationCode=arrival_city,
            departureDate=departure_date,
            adults=adults
        )
        return response.data
    except Exception as e:
        print("An error occurred:", e)
        return None

def find_best_flight(flights):
    best_price = float('inf')
    best_flight = None
    for flight in flights:
        price = float(flight['price']['total'])
        if price < best_price:
            best_price = price
            best_flight = flight
    return best_flight

def display_flight_details(flight):
    if flight:
        departure_time = flight['itineraries'][0]['segments'][0]['departure']['at']
        arrival_time = flight['itineraries'][0]['segments'][-1]['arrival']['at']
        price = flight['price']['total']
        departure_city = None
        arrival_city = None
        print("Departure Time:", departure_time)
        print("Arrival Time:", arrival_time)
        print("Price: EUR", price)
    else:
        print("No flight options found.")

def main():
    # Prompt user to input details
    departure_city = input("Enter departure city: ").upper()
    arrival_city = input("Enter arrival city: ").upper()
    departure_date = input("Enter departure date (YYYY-MM-DD): ")
    adults = int(input("Enter number of adults: "))

    # Fetch flight options from Amadeus API
    flights = get_flight_options(departure_city, arrival_city, departure_date, adults)

    # Find the best flight
    best_flight = find_best_flight(flights)

    # Display flight details
    print("***********")
    print("For departure location: ",departure_city)
    print("To arrival location: ",arrival_city)
    print("Here is your best fligt option: ")
    display_flight_details(best_flight)

if __name__ == "__main__":
    main()
