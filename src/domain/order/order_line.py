from dataclasses import dataclass
from items import Item

@dataclass(frozen=True)
class OrderLine:
    item: Item
    count: int

    @property
    def total_price(self):
        return self.item.price * self.count
