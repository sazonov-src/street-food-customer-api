from abc import ABC, abstractmethod

from order.order_line import OrderLine


class OrderBase(ABC):
    def __init__(self, *args: OrderLine) -> None:
        self._lines = list(args)

    @abstractmethod
    def add_order_line(self, line: OrderLine):
        pass

    @abstractmethod
    def rm_order_line(self, line: OrderLine):
        pass
    
    @property
    def total_price(self):
        return sum(i.total_price for i in self._lines)

    @property
    def lines(self):
        return tuple(self._lines)


class OrderChangeable(OrderBase):
    def add_order_line(self, line: OrderLine):
        if line in self._lines:
            raise ValueError 
        self._lines.append(line)

    def rm_order_line(self, line: OrderLine):
        self._lines.remove(line)


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
