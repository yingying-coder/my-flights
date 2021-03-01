import os
from twilio.rest import Client
from datetime import datetime, timedelta

now = datetime.now()
DATE_FROM = now + timedelta(days=1)
DATE_TO = DATE_FROM + timedelta(days=180)

ACCOUNT = os.getenv("ACCOUNT_SID")
TOKEN = os.getenv("TOKEN")
NUMBER = os.getenv("NUMBER")
MY_NUMBER = os.getenv("MY_NUMBER")
CITY = "Sydney-SYD"


class NotificationManager:
    def __init__(self, city, price, date):
        self.city = city
        self.price = price
        self.date = date
        client = Client(ACCOUNT, TOKEN)
        client.messages.create(
            body=f"Low price alert! ${self.price} to fly from {CITY} to {self.city} "
                 f"from {DATE_FROM.strftime('%d/%m/%Y')} to {DATE_TO.strftime('%d/%m/%Y')} on {self.date}.",
            from_=NUMBER,
            to=MY_NUMBER,
        )


