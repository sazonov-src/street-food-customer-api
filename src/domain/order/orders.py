from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable
import order


class BaseOrder(ABC):

    @property
    @abstractmethod
    def cart(self) -> order.BaseCartView:
        pass

    @property
    @abstractmethod
    def state(self) -> BaseState:
        pass


class BaseOrderCheckout(ABC):

    @property
    @abstractmethod
    def user_data(self) -> order.UserData:
        pass

    @abstractmethod
    def mark_as_checkout(self, checkout: order.UserData):
        pass


class BaseOrderPayed(ABC):

    @property
    @abstractmethod
    def payment(self) -> order.BasePayment:
        pass

    @abstractmethod
    def mark_as_pay(self, payment: order.BasePayment):
        pass


class BaseCustomerOrder(BaseOrder, BaseOrderCheckout, BaseOrderPayed):
    pass


class BaseState(ABC):
    cart_type: type[order.BaseCartView]


class BaseCheckoutState(ABC):
    @abstractmethod
    def mark_as_checkout(self, checkout: order.UserData):
        pass

class BasePaymentState(ABC):
    @abstractmethod
    def mark_as_pay(self, payment: order.BasePayment):
        pass


class BaseCustomerState(BaseState, BaseCheckoutState, BasePaymentState):
    def __init__(self, order) -> None:
        self._order = order


class StateCustomerPayed(BaseCustomerState):
    cart_type = order.CartNotNutable
    def mark_as_checkout(self, checkout):
        raise ValueError

    def mark_as_pay(self, payment: order.BasePayment):
        raise ValueError


class StateCustomerCheckout(BaseCustomerState):
    cart_type = order.CartMutable
    def mark_as_checkout(self, checkout):
        raise ValueError

    def mark_as_pay(self, payment: order.BasePayment):
        if payment.is_payment():
            self._order._state = StateCustomerPayed(self._order)


class StateCustomerNew(BaseCustomerState):
    cart_type = order.CartMutable
    def mark_as_checkout(self, checkout):
        self._order._user_data = checkout
        self._order._state = StateCustomerCheckout(self._order)

    def mark_as_pay(self, payment: order.BasePayment):
        raise ValueError


class CustomerOrder(BaseCustomerOrder):
    def __init__(self, order_lines: Iterable[order.LINE] | None = None):
        self._user_data: order.UserData | None = None
        self._payment: order.BasePayment | None = None
        self._state = StateCustomerNew(self)
        self._cart = self.state.cart_type(*order_lines if order_lines else ())

    def _reset_cart(self):
        cart_data = self._cart.lines
        self._cart = self._state.cart_type(*cart_data)

    @property
    def state(self):
        return self._state

    @property
    def cart(self):
        return self._cart

    @property
    def user_data(self) -> order.UserData:
        if not self._user_data:
            raise ValueError
        return self._user_data

    @property
    def payment(self) -> order.BasePayment:
        if not self._payment:
            raise ValueError
        return self._payment

    def mark_as_checkout(self, checkout: order.UserData):
        self._state.mark_as_checkout(checkout)
        self._reset_cart()

    def mark_as_pay(self, payment: order.BasePayment):
        self._state.mark_as_pay(payment)
        self._reset_cart()


