import copy
from collections import abc
from enum import Enum
from typing import Optional

from domein.order import base
from domein.order.order_line import OrderLine
from domein.order.payment import Payment
from domein.order.user_data import UserData


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


def get_order(
        items: Optional[abc.Iterable[OrderLine]] = None, 
        user_data: Optional[UserData] = None, 
        payed: bool = False, 
        ready: bool = False, 
        done: bool = False):
    l = copy.copy(locals())
    key = "items"
    while l:
        key, value = l.popitem()
        if value:
            l.update({key: value})
            break
    for value in l.values():
        if not value:
            raise OrderDataError()
    return {
        "items": OrderNew,
        "user_data": OrderCheckout,
        "payed": OrderPayed,
        "ready": OrderReady,
        "done": OrderDone
    }[key](items, user_data)

