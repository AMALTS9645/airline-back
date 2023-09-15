from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    iatafrom: str
    iatato: str
    dateoftravel: str
    class_business: int
    class_economy: int
    class_first: int