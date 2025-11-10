from pydantic import BaseModel
from typing import Optional

class CreateContact(BaseModel):
    firstname: str
    lastname: str
    phone: str
    email: Optional[str] = None

class Contact(CreateContact):
    id: int
