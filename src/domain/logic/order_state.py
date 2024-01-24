from __future__ import annotations
from typing import Iterable

from rest_framework.exceptions import NotFound

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
        raise ErrorPayedOrderState("Order not payed")
        


def get_new_order_state(orders: Iterable[ModalOrder]) -> StateOrderNew:
    for order in orders:
        order_handler = StateOrderPayed()
        try:
            order_handler.handle_order(order)
        except ErrorPayedOrderState:
            order_handler = StateOrderNew()
            order_handler.handle_order(order)
            return order_handler
    raise NotFound("New order not found")

