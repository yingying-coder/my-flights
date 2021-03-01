import new_data as nd
import pandas as pd
from notification_manager import NotificationManager
from flight_data import FlightData
from datetime import datetime, timedelta

now = datetime.now()
DATE_FROM = now + timedelta(days=1)
DATE_TO = DATE_FROM + timedelta(days=180)

data = nd.parse_csv("flights.csv")
for city in data:
    if type(city["IATA Code"]) != str:
        city["IATA Code"] = nd.iata(city["City"])

    flight = FlightData(city["IATA Code"]).data
    if flight["price"]:
        if flight["price"] < city["Lowest Price M"]:
            city["Lowest Price M"] = flight["price"]

            city_to = f"{city['City']}-{flight['air_to']}"
            NotificationManager(city=city_to, price=flight["price"],
                                date=flight["date"].split("T")[0])

        tracking_data = [
            {
                "City": city["City"],
                "CityCode": city["IATA Code"],
                "AirportCode": flight["air_to"],
                "LowPrice": flight["price"],
                "DptDate": flight["date"].split("T")[0],
                "DptTime": flight["date"].split("T")[1],
                "From": DATE_FROM.strftime('%d/%m/%Y'),
                "To": DATE_TO.strftime('%d/%m/%Y'),
                "SearchingTime": now.strftime("%H:%M:%S")
            }
        ]
        try:
            pd.read_csv("flights_tracking.csv")
        except FileNotFoundError:
            nd.create("flights_tracking.csv")
        finally:
            nd.add_to("flights_tracking.csv", tracking_data)

nd.update("flights.csv", data)