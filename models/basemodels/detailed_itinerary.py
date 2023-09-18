from pydantic import BaseModel
from typing import List


class ItineraryRequest(BaseModel):
    routes: List[int]


class ItineraryResponse(BaseModel):
    id: int
    flying_from: dict
    flying_to: dict
    airline: dict
