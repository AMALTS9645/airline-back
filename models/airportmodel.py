from mongoengine import Document, StringField, LongField, IntField, DecimalField, DateTimeField


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
