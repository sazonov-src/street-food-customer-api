from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable
import order


class BaseOrder(ABC):
    start_state: type[BaseStateOrder]

    def __init__(
            self, 
            cart_lines: Iterable[order.LINE] | None = None, 
            user_data: order.UserData | None = None, 
            payment: order.Payment | None = None):
        self._cart_lines = cart_lines
        self._user_data = user_data
        self._payment = payment
        self._state = self.start_state(self).get_valide_state()

    def update_state(self):
        self._state = self._state.get_valide_state()


class BaseStateOrder(ABC):

    def __init__(self, order: BaseOrder) -> None:
        self._order = order

    @abstractmethod
    def get_valide_state(self) -> BaseStateOrder:
        pass

    @abstractmethod
    def to_checkout(self, checkout):
        pass


class StateCheckoutOrder(BaseStateOrder):
    def get_valide_state(self):
        return self

    def to_checkout(self, checkout):
        raise ValueError("Already checkouted")


class StateNewOrder(BaseStateOrder):
    def get_valide_state(self):
        if self._order._user_data:
            return StateCheckoutOrder(self._order).get_valide_state()
        return self

    def to_checkout(self, checkout):
        self._order._user_data = checkout


class OrderCheckout(BaseOrder):
    start_state = StateNewOrder

    def to_checkout(self, checkout: order.UserData):
        self._state.to_checkout(checkout)
        self.update_state()

