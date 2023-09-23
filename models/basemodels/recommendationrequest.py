from pydantic import BaseModel
from typing import Optional, List


class RecommendationRequest(BaseModel):
    iatafrom: str
    iatato: str
    dateoftravel: str
    classfields: Optional[List[str]] = None
