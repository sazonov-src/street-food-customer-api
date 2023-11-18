from typing import Iterable
from dj.repository import BaseRepository
from app_order.models import Order
from app_menu.repository import RepositoryMenuItem
from domain import order


class RepositoryCartLines(BaseRepository):
    def __init__(self, order: Order):
        self._order = order

    def get(self) -> Iterable[order.LINE]:
        for line in self._order.cart_line_set:
            item_rep = RepositoryMenuItem(line.menu_item)
            yield item_rep.get(), line.count

    def model(self):
        return self._order
