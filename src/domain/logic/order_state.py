from __future__ import annotations
from typing import Iterable

from models.order import ModalOrder

__all__ = [
    'StateOrder',
    'StateOrderNew',
    'StateOrderPayed',
    'get_new_order_state',
    'ErrorOrderState',
    'ErrorNewOrderState',
    'ErrorPayedOrderState',
]

class ErrorOrderState(ValueError):
    pass

class ErrorNewOrderState(ErrorOrderState):
    pass

class ErrorPayedOrderState(ErrorOrderState):
    pass


class StateOrder:
    order: ModalOrder

    def __init__(self, successor=None):
        self.successor = successor

    def handle_order(self, order: ModalOrder):
        if self.successor:
            self.successor.handle_order(order)


class StateOrderNew(StateOrder):
    def handle_order(self, order_data):
        super().handle_order(order_data)
        if len(order_data.cart_data.lines) == 0:
            raise ErrorNewOrderState("Cart is empty")
        self.order = order_data


class StateOrderPayed(StateOrder):
    def handle_order(self, order_data):
        super().handle_order(order_data)
        


def get_new_order_state(order: ModalOrder) :
    order_handler = StateOrderNew(StateOrderPayed())
    try:
        order_handler.handle_order(order)
    except ErrorPayedOrderState as e:
        pass
    return order_handler
