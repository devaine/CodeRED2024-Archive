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
            currencyCode='USD',
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

def convert_to_usd(amount, currency):
    try:
        response = amadeus.reference_data.symbols.get()
        rates = response.data['currencies']
        currency_rates = {rate['code']: rate['rate'] for rate in rates}
        if currency == 'USD':
            return amount
        else:
            return round(amount / currency_rates[currency], 2)
    except Exception as e:
        print("An error occurred while converting currency:", e)
        return None

def display_flight_details(flight):
    if flight:
        departure_time = flight['itineraries'][0]['segments'][0]['departure']['at']
        arrival_time = flight['itineraries'][0]['segments'][-1]['arrival']['at']
        currency = flight['price']['currency']
        price = flight['price']['grandTotal']
        carrier = flight['itineraries'][0]['segments'][0]['carrierCode']
        departure_city = None
        arrival_city = None
        
        # Convert price to USD if currency is not USD
        if currency != 'USD':
            price_usd = convert_to_usd(price, currency)
            if price_usd:
                print("Price (USD):", price_usd)
        else:
            print("Price (USD):", price)
        
        print("Carrier:", carrier)
        print("Departure Time:", departure_time)
        print("Arrival Time:", arrival_time)
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
    print("Here is your best fligt option for ECONOMY class: ")
    display_flight_details(best_flight)

if __name__ == "__main__":
    main()
