from __future__ import annotations
from typing import Annotated
from pydantic import AfterValidator, BaseModel, computed_field

from models.cart import ModelCart
from models.contact import ModalContact

class ModalOrder(BaseModel):
    cart_data: ModelCart
    contact_data: ModalContact
    accepted: bool = False
    is_ready: bool = False
    done: bool = False


