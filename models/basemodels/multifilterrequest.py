from pydantic import BaseModel
from typing import List, Optional


class MultiFilterRequest(BaseModel):
    airline_codes: Optional[List[str]] = None
    classfields: Optional[List[str]] = None
