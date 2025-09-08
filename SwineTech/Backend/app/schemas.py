from pydantic import BaseModel
from datetime import date
from typing import Optional

class PigIn(BaseModel):
    tag_id: str
    birth_date: date
    breed: Optional[str] = None
    weight: Optional[float] = None
    sex: Optional[str] = None

class PigOut(PigIn):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2