from __future__ import annotations
from typing import Iterable

from models.order import Order

__all__ = [
    'OrderHandler',
    'NewOrderHandler',
    'PayedOrderHandler',
    'get_new_order_handler',
    'OrderError',
    'NewOrderError',
    'PayedOrderError',
]

class OrderError(ValueError):
    pass

class NewOrderError(OrderError):
    pass

class PayedOrderError(OrderError):
    pass


class OrderHandler:
    order: Order

    def __init__(self, successor=None):
        self.successor = successor

    def handle_order(self, order: Order):
        if self.successor:
            self.successor.handle_order(order)


class NewOrderHandler(OrderHandler):
    def handle_order(self, order_data):
        super().handle_order(order_data)
        if len(order_data.cart_data.lines) == 0:
            raise NewOrderError("Cart is empty")
        self.order = order_data


class PayedOrderHandler(OrderHandler):
    def handle_order(self, order_data):
        super().handle_order(order_data)
        


def get_new_order_handler(order: Order) :
    order_handler = NewOrderHandler(PayedOrderHandler())
    try:
        order_handler.handle_order(order)
    except PayedOrderError as e:
        pass
    return order_handler
