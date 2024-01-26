from __future__ import annotations
from typing import Annotated
from pydantic import AfterValidator, BaseModel, Field, computed_field

from models.cart import ModelCart
from models.contact import ModalContact

class ModalOrder(BaseModel):
    cart_data: ModelCart
    contact_data: ModalContact
    pay_callbacks: list[dict] = Field(default_factory=list)
    accepted: bool = False
    is_ready: bool = False
    done: bool = False

    def __hash__(self):
        return hash((self.cart_data, self.contact_data))

def get_payment_data(order: ModalOrder):
    return order
