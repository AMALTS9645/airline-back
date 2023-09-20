from pydantic import BaseModel
from typing import List

from models.basemodels.recommend import Recommend


class MultiFlightRecommendationResponse(BaseModel):
    date: str
    departure: str
    arrival: str
    results: List[Recommend]
