from uuid import UUID
from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    password: str
    phone_number: str
    