# type: ignore
from abc import ABC, abstractmethod

from order.order_line import OrderLine
from numbers import Number


class OrderBase(ABC):
    def __init__(self, *args: OrderLine) -> None:
        self._items = set(args)

    @abstractmethod
    def add_order_line(self, line: OrderLine):
        pass

    @abstractmethod
    def rm_order_line(self, line: OrderLine):
        pass
    
    @property
    def total_price(self) -> Number:
        return sum(i.total_price for i in self._items)

    @property
    def items() -> set[OrderLine]:
        return self._items


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
