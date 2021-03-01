from flight_search import FlightSearch
CITY = "SYD"


class FlightData:
    def __init__(self, city):
        search = FlightSearch(city)
        flights = [flight for flight in search.response if flight["availability"]["seats"]]
        self.data = {
            "city_dpt": CITY,
            "city_to": city,
            "air_dpt": flights[0]["flyFrom"] if flights else "",
            "air_to": flights[0]["flyTo"] if flights else "",
            "price": flights[0]["price"] if flights else "",
            "date": flights[0]["local_departure"] if flights else "",
        }
