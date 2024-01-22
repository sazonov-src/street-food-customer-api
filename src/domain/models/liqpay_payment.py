from __future__ import annotations
from pydantic import BaseModel


class LiqpayPayment(BaseModel):
    order_id: str
    amount: str
    version: str
    public_key: str
    action: str
    currency: str
    description: str
    items: list[LiqpayItem]


class LiqpayItem(BaseModel):
    id: int
    amount: int
    cost: int
    price: int
