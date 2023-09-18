from pydantic import BaseModel


class AirportAutoRequest(BaseModel):
    search_string: str
    limit: int

