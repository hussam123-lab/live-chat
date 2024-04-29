from typing import List
from uuid import UUID
from pydantic import BaseModel

class User(BaseModel):
    user_id : UUID
    name: str
    contacts: List[UUID]