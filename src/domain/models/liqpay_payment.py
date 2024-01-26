from __future__ import annotations
from pydantic import BaseModel


class ModalLiqpayPayment(BaseModel):
    order_id: str
    amount: str
    version: str
    public_key: str
    action: str
    currency: str
    description: str


class ModelLiqpayData(ModalLiqpayPayment):
    data: str
    signature: str
