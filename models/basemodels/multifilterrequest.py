from pydantic import BaseModel
from typing import List, Optional


class MultiFilterRequest(BaseModel):
    airline_codes: Optional[List[str]] = None
    class_business: Optional[int] = None
    class_economy: Optional[int] = None
    class_first: Optional[int] = None
