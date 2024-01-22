from __future__ import annotations
from typing import Annotated
from pydantic import AfterValidator, BaseModel, computed_field

from models.cart import Cart
from models.contact import Contact

class Order(BaseModel):
    cart_data: Cart
    contact_data: Contact
    accepted: bool = False
    is_ready: bool = False
    done: bool = False


