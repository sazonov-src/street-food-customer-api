from __future__ import annotations
from typing import Iterable

from rest_framework.exceptions import NotFound

from models.order import ModalOrder

__all__ = [
    'StateOrder',
    'StateOrderNew',
    'StateOrderPayed',
    'get_new_order',
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

    def handle_order(self, order: ModalOrder) -> ModalOrder:
        if self.successor:
            self.successor.handle_order(order)
        return order


class StateOrderNew(StateOrder):
    def handle_order(self, order_data):
        if len(order_data.cart_data.lines) == 0:
            raise ErrorNewOrderState("Cart is empty")
        return super().handle_order(order_data)


class StateOrderPayed(StateOrder):
    def handle_order(self, order_data):
        for callback in order_data.pay_callbacks:
            if callback.get('status') and callback['status'] == 'OK':
                return super().handle_order(order_data)
        raise ErrorPayedOrderState("Order not payed")



def get_new_order(orders: Iterable[ModalOrder]) -> ModalOrder:
    for order in orders:
        order_handler = StateOrderNew(StateOrderPayed())
        try:
            order_handler.handle_order(order)
        except ErrorPayedOrderState:
            return order
    raise NotFound("New order not found")


