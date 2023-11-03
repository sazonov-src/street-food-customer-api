from __future__ import annotations
from dataclasses import dataclass
from items import Item


class Count(int):
    def __new__(cls, num):
        if int(num) < 1:
            raise ValueError
        return super().__new__(cls,num)
    

@dataclass
class CartItem:
    item: Item
    count: Count

    @property
    def total_price(self):
        return self.item.price * self.count

    def __hash__(self) -> int:
        return hash(self.item)

    def __eq__(self, value: CartItem) -> bool:
        return self.item == value.item

    def plus_count(self):
        self.count = Count(self.count + 1)

    def minus_count(self):
        self.count = Count(self.count - 1)
