from pydantic import BaseModel


class AirlinesResponse(BaseModel):
    name: str
    code: str
    isLowCost: bool
    logo: str
