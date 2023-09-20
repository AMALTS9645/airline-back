from pydantic import BaseModel
from typing import Optional


class Recommend(BaseModel):
    uid: int
    common_duration: int
    min_duration: int
    max_duration: int
    flights_per_day: Optional[str] = None
    flights_per_week: Optional[int] = None
    airline_name: Optional[str] = None
    airline_code: str
    day1: str
    day2: str
    day3: str
    day4: str
    day5: str
    day6: str
    day7: str
    airport_from: str
    airport_to: str
    iata_from: str
    iata_to: str
    class_business: int
    class_economy: int
    class_first: int
    is_scheduled_passenger: Optional[int] = None
    is_cargo: Optional[int] = None
