from pydantic import BaseModel
from typing import List, Optional


class MultiFilterRequest(BaseModel):
    airline_codes: Optional[List[str]] = None
    class_business: Optional[int] = -1
    class_economy: Optional[int] = -1
    class_first: Optional[int] = -1
