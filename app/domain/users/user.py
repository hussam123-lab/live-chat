from typing import List
from uuid import UUID
from pydantic import BaseModel

class User(BaseModel):
    user_id : UUID
    name: str
    password: str
    phone_number: str
    contacts: List[UUID]