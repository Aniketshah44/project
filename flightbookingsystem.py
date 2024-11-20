flights = {
    "F1": {"origin": "Delhi", "destination": "Mumbai", "departure": "10:00", "arrival": "12:00", "seats": 100, "price": 5000},
    "F2": {"origin": "Mumbai", "destination": "Bangalore", "departure": "13:00", "arrival": "15:00", "seats": 80, "price": 6000},
    # ... more flights
}

bookings = []

def search_flights(origin, destination):
    for flight_id, flight_info in flights.items():
        if flight_info["origin"] == origin and flight_info["destination"] == destination:
            print(f"Flight ID: {flight_id}")
            print(f"Origin: {flight_info['origin']}")
            print(f"Destination: {flight_info['destination']}")
            print(f"Departure: {flight_info['departure']}")
            print(f"Arrival: {flight_info['arrival']}")
            print(f"Seats Available: {flight_info['seats']}")
            print(f"Price: {flight_info['price']}")
            print("-" * 30)

def book_flight(flight_id, passenger_name, age, contact):
    if flights[flight_id]["seats"] > 0:
        flights[flight_id]["seats"] -= 1
        booking_info = {
            "flight_id": flight_id,
            "passenger_name": passenger_name,
            "age": age,
            "contact": contact
        }
        bookings.append(booking_info)
        print("Booking confirmed!")
    else:
        print("Sorry, flight is fully booked.")

# Example usage
search_flights("Delhi", "Mumbai")

flight_id = "F1"
passenger_name = "Aniket"
age = 18
contact = "1234567890"
book_flight(flight_id, passenger_name, age, contact)