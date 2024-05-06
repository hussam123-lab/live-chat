from uuid import UUID
from pydantic import BaseModel

class ContactsRequest(BaseModel):
    phone_number: str
    