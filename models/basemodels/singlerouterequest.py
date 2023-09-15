from pydantic import BaseModel


class SingleRouteRequest(BaseModel):
    date: str
    departure: str
    arrival: str

