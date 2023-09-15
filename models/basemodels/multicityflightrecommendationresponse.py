from pydantic import BaseModel
from typing import List

from models.basemodels.recommendationresponse import RecommendationResponse


class MultiFlightRecommendationResponse(BaseModel):
    date: str
    departure: str
    arrival: str
    results: List[RecommendationResponse]
