from __future__ import annotations
from pydantic import BaseModel


class Order(BaseModel):
    user_id: str
    contact: Contact
    is_ready: bool
    done: bool

class Contact(BaseModel):
    name: str
    phone: str
