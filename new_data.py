import pandas as pd
from flight_search import DestinationSearch


def parse_csv(filename):
    return pd.read_csv(filename).to_dict("records")


def iata(city):
    return DestinationSearch(city).code


def update(filename, data):
    df = pd.DataFrame.from_records(data)
    df.to_csv(filename, index=False)


def add_to(filename, data):
    df = pd.DataFrame.from_records(data)
    df.to_csv(filename, mode="a", header=False, index=False)


def create(filename):
    data = {
        "City": [], "CityCode": [], "AirportCode": [], "LowPrice": [],
        "DptDate": [], "DptTime": [], "From": [], "To": [], "SearchingTime": []
    }
    df = pd.DataFrame(data).from_dict(data)
    df.to_csv(filename, index=False)


