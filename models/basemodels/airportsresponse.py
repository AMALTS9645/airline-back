from pydantic import BaseModel


class AirportsResponse(BaseModel):
    code: str
    name: str
    city: str
    state: str
    country: str
    runway_length: int
    icao: str
    direct_flights: int
    carriers: int
    lat: float
    lon: float
    woeid: int
    tz: str
