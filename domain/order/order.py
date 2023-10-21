import copy
from collections import abc
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from . import base
from .order_line import OrderLine
from .user_data import UserData


class OrderDataError(Exception):
    pass

class Status(Enum):
    NEW = 4
    CHECKOUTED = 3
    PAYED = 2
    READY = 1
    DONE = 0


class OrderChangeable(base.OrderItemsBase):
    def add_order_line(self, line):
        self._items.add(line)
   
    def rm_order_line(self, line):
        self._items.remove(line)


class OrderNotChangeable(base.OrderItemsBase):
    def add_order_line(self):
        raise
    
    def rm_order_line(self):
        raise


class OrderNew(OrderChangeable):
    status = Status.NEW

class OrderCheckout(OrderChangeable):
    status = Status.CHECKOUTED

class OrderPayed(OrderNotChangeable):
    status = Status.PAYED

class OrderReady(OrderNotChangeable):
    status = Status.READY

class OrderDone(OrderNotChangeable):
    status = Status.DONE


@dataclass
class OrderStatus[T: base.OrderItemsBase]:
    items: Optional[abc.Iterable[OrderLine]] = None
    user_data: Optional[UserData] = None
    payed: bool = False
    ready: bool = False
    done: bool = False
        
    @property
    def _true_data(self):
        data = copy.copy(self.__dict__)
        while data:
            key, value = data.popitem()
            if value:
                data.update({key: value})
                return data
        return {}

    def validate(self):
        for value in self._true_data.values():
            if not value:
                raise OrderDataError

    def _last_attr(self):
        try:
            return tuple(self._true_data)[-1]
        except IndexError:
            return "items"

    def get_order(self) -> T:
        return {
            "items": OrderNew,
            "user_data": OrderCheckout,
            "payed": OrderPayed,
            "ready": OrderReady,
            "done": OrderDone
       }[self._last_attr()](self.items, self.user_data)
      
    def __setattr__(self, __name, __value) :
        super().__setattr__(__name, __value)
        self.validate()
