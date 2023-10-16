
from abc import ABC, abstractmethod
from collections import abc
from typing import Optional
from domein.order.order_line import OrderLine

from domein.order.user_data import UserData


class OrderBase(ABC):
    def __init__(
            self, 
            items: Optional[abc.Iterable[OrderLine]] = None,
            user_data: Optional[UserData] = None,
        ) -> None:
        self._items = set(items) if items else set()
        self._user_data = user_data


class OrderItemsBase(OrderBase, ABC):
    @abstractmethod
    def add_order_line(self, line: OrderLine):
        raise

    @abstractmethod
    def rm_order_line(self, line: OrderLine):
        raise
    
    @property
    def total_price(self):
        pass


class OrderPaymentBase(OrderBase, ABC):
    @property
    @abstractmethod
    def payment(self):
        raise
