from __future__ import annotations
from pydantic import BaseModel, model_serializer
from pydantic.functional_serializers import PlainSerializer
from typing import Annotated


class Cart(BaseModel):
    lines: list[CartLine]

    def __len__(self):
        return len(self.lines)

    def add_item(self, item: Product, quantity: int = 1):
        if not item in self.lines:
            self.lines.append(CartLine(menu_item=item, quantity=quantity))

    def remove_item(self, item: Product):
        if item in self.lines:
            self.lines.remove(item)


class CartLine(BaseModel):
    menu_item: Annotated[
            Product, 
            PlainSerializer(lambda x: x.id, when_used='json')]
    quantity: int

    def __hash__(self):
        return hash(self.menu_item.id)


class Product(BaseModel):
    id: int
    price: float
