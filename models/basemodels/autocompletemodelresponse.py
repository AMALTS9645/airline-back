from pydantic import BaseModel


class AirportAutoResponse(BaseModel):
    name: str
    code: str
