from pydantic import BaseModel
from typing import List, Optional

from models.basemodels.singlerouterequest import SingleRouteRequest


class MultiFlightRecommendationRequest(BaseModel):
    classfields: Optional[List[str]] = None
    airlines: Optional[List[str]] = None
    routes: List[SingleRouteRequest]
