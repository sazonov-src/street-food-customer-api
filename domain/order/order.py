# type: ignore
from abc import ABC, abstractmethod
from collections import abc
from typing import Optional

from order.order_line import OrderLine
from order.user_data import UserData


class OrderSetKeyError(Exception):
    pass

class OrderSetNotObjError(Exception):
    pass


class OrderBase(ABC):
    def __init__(
            self, 
            items: Optional[abc.Iterable[OrderLine]] = None,
            user_data: Optional[UserData] = None,
        ) -> None:
        self._items = set(items) if items else set()
        self._user_data = user_data

    @abstractmethod
    def add_order_line(self, line: OrderLine):
        raise

    @abstractmethod
    def rm_order_line(self, line: OrderLine):
        raise
    
    @property
    def total_price(self):
        pass


class OrderChangeable(OrderBase):
    def add_order_line(self, line):
        self._items.add(line)

    def rm_order_line(self, line):
        self._items.remove(line)


class OrderNotChangeable(OrderBase):
    def add_order_line(self):
        raise

    def rm_order_line(self):
        raise


class OrderNew(OrderChangeable):
    pass

class OrderCheckout(OrderChangeable):
    pass

class OrderPayed(OrderNotChangeable):
    pass

class OrderReady(OrderNotChangeable):
    pass

class OrderDone(OrderNotChangeable):
    pass
