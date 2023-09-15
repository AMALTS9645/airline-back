import requests
import json
from mongoengine import Document, StringField, DateTimeField, IntField, connect
import time


class RoutesData(Document):
    common_duration = IntField()
    min_duration = IntField()
    max_duration = IntField()
    flights_per_day = StringField()
    flights_per_week = IntField()
    airline_name = StringField()
    airline_code = StringField()
    day1 = StringField()
    day2 = StringField()
    day3 = StringField()
    day4 = StringField()
    day5 = StringField()
    day6 = StringField()
    day7 = StringField()
    iata_from = StringField()
    iata_to = StringField()
    class_business = IntField()
    class_economy = IntField()
    class_first = IntField()
    is_scheduled_passenger = IntField()
    is_cargo = IntField()
    createdAt = DateTimeField()
    updatedAt = DateTimeField()


if __name__ == '__main__':
    connect(host="mongodb+srv://amal:Vv14t8Ig7MukqL5R@cluster0.x4j0e.mongodb.net/flight-routes")

    file_path = "flightsDB.routes_v2.json"
    Routes = open(file_path, 'r', encoding='utf-8')
    data = json.load(Routes)

    # def getData(docs):
    #     return {
    #
    #     }

    for documents in data:
        print(documents.get('common_duration'))
        RoutesData(
            common_duration=documents.get('common_duration', None),
            min_duration=documents.get('min_duration'),
            max_duration=documents.get('max_duration'),
            flights_per_day=documents.get('flights_per_day'),
            flights_per_week=documents.get('flights_per_week'),
            airline_name=documents.get('airline', None).get('name', None),
            airline_code=documents.get('airline', None).get('IATA', None),
            day1=documents.get('day1', None),
            day2=documents.get('day2', None),
            day3=documents.get('day3', None),
            day4=documents.get('day4', None),
            day5=documents.get('day5', None),
            day6=documents.get('day6', None),
            day7=documents.get('day7', None),
            iata_from=documents.get('iata_from', None),
            iata_to=documents.get('iata_to', None),
            class_business=documents.get('class_business', None),
            class_economy=documents.get('class_economy', None),
            class_first=documents.get('class_first', None),
            is_scheduled_passenger=documents.get('airline').get('is_scheduled_passenger'),
            is_cargo=documents.get('airline').get('is_cargo'),
            createdAt=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            updatedAt=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ).save()

