from pydantic import BaseModel

class ValidateRequest(BaseModel):
    name: str
    password: str
    phone_number: str