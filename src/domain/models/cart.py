from __future__ import annotations
from pydantic import AfterValidator, BaseModel, computed_field, field_validator
from pydantic.functional_serializers import PlainSerializer
from typing import Annotated


class ModelCart(BaseModel):
    lines: list[ModelCartLine]

    def __len__(self):
        return len(self.lines)

    def add_item(self, item: ModelCartItem, quantity: int = 1):
        if not item in self.lines:
            self.lines.append(ModelCartLine(menu_item=item, quantity=quantity))

    def remove_item(self, item: ModelCartItem):
        if item in self.lines:
            self.lines.remove(item)

    def get_line(self, item: ModelCartItem):
        for line in self.lines:
            if line.menu_item == item:
                return line
        raise ValueError

    @computed_field
    @property
    def total(self) -> float:
        return sum(line.total for line in self.lines)

    def __hash__(self):
        return hash(tuple(self.lines))


def check_is_gt_zero(value):
    if value >= 1:
        return value
    raise ValueError('Quantity must be greater than 0')

Quantity = Annotated[
    int,
    AfterValidator(check_is_gt_zero),
]

class ModelCartLine(BaseModel):
    menu_item: Annotated[
            ModelCartItem, 
            PlainSerializer(lambda x: x.id, when_used='json')]
    quantity: Quantity = 1

    def __hash__(self):
        return hash((self.menu_item, self.quantity))

    @computed_field
    @property
    def total(self) -> float:
        return self.menu_item.price * self.quantity

    def __eq__(self, other):
        return self.menu_item == other

    def plus_quantity(self):
        self.quantity += 1

    def minus_quantity(self):
        self.quantity -= 1
        check_is_gt_zero(self.quantity)


class ModelCartItem(BaseModel):
    id: int
    price: float

    def __hash__(self):
        return hash(self.id)
