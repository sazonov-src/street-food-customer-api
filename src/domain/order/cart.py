from abc import ABC, abstractmethod

from order.cart_line import CartItem

class CartNotChangeableError(Exception):
    pass


class CartBase(ABC):
    def __init__(self, *args: CartItem) -> None:
        self._lines = list(args)

    @abstractmethod
    def add_line(self, line: CartItem):
        pass

    @abstractmethod
    def rm_line(self, line: CartItem):
        pass
    
    @property
    def total_price(self):
        return sum(i.total_price for i in self._lines)

    @property
    def lines(self):
        return tuple(self._lines)


class CartChangeable(CartBase):
    def add_line(self, line: CartItem):
        if line in self._lines:
            raise ValueError 
        self._lines.append(line)

    def rm_line(self, line: CartItem):
        self._lines.remove(line)


class CartNotChangeable(CartBase):
    def add_line(self):
        raise CartNotChangeableError

    def rm_line(self):
        raise CartNotChangeableError
