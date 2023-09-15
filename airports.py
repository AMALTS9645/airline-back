import json
import requests

import mongoengine
from mongoengine import Document, StringField, DecimalField, IntField, LongField, DateTimeField
import time


class Airports(Document):
    code = StringField(unique=True)
    name = StringField()
    city = StringField()
    state = StringField()
    country = StringField()
    runway_length = LongField()
    icao = StringField()
    direct_flights = IntField()
    carriers = IntField()
    lat = DecimalField()
    lon = DecimalField()
    woeid = IntField()
    tz = StringField()
    createdAt = DateTimeField()
    updatedAt = DateTimeField()


if __name__ == '__main__':

    mongoengine.connect(host="mongodb+srv://amal:Vv14t8Ig7MukqL5R@cluster0.x4j0e.mongodb.net/flight-routes")

    airports = requests.get(
        "https://gist.githubusercontent.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588/airports.json",
        verify=False)
    airport_data = airports.json()

    for airport in airport_data:
        Airports(
            code=airport.get("code"),
            name=airport.get("name"),
            city=airport.get("city"),
            state=airport.get("state"),
            country=airport.get("country"),
            runway_length=airport.get("runway_length"),
            icao=airport.get("icao"),
            direct_flights=airport.get("direct_flights"),
            carriers=airport.get("carriers"),
            lat=airport.get("lat"),
            lon=airport.get("lon"),
            woeid=airport.get("woeid"),
            tz=airport.get("tz"),
            createdAt=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            updatedAt=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ).save()
