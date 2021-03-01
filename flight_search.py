import requests
import os
from datetime import datetime, timedelta

CITY = "SYD"
now = datetime.now()
DATE_FROM = now + timedelta(days=1)
DATE_TO = DATE_FROM + timedelta(days=180)
HEADERS = {
    "apikey": os.getenv("FLIGHT_SEARCH_API")
}
ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    def __init__(self, city):
        parameters = {
            "fly_to": city,
            "fly_from": CITY,
            "max_stopovers": 0,
            "curr": "AUD",
            "selected_cabins": "M",
            "date_from": DATE_FROM.strftime("%d/%m/%Y"),
            "date_to": DATE_TO.strftime("%d/%m/%Y"),
        }
        self.response = requests.get(f"{ENDPOINT}/v2/search", params=parameters,
                                     headers=HEADERS).json()["data"]


class DestinationSearch:
    def __init__(self, city):
        parameters = {
            "term": city,
            "location_types": "city",
        }
        search = requests.get(f"{ENDPOINT}/locations/query", params=parameters,
                              headers=HEADERS).json()
        self.code = search["locations"][0]["code"]



