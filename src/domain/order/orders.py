from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable
import order

class OrderException(Exception):
    pass

class OrderStateException(OrderException):
    pass

class OrderValueException(OrderException, ValueError):
    pass

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
    def mark_as_checkouted(self, checkout: order.UserData):
        pass


class BaseOrderPayed(ABC):

    @property
    @abstractmethod
    def payment(self) -> order.BasePayment:
        pass

    @abstractmethod
    def mark_as_payed(self, payment: order.BasePayment):
        pass


class BaseCustomerOrder(BaseOrder, BaseOrderCheckout, BaseOrderPayed):
    pass


class BaseState(ABC):
    cart_type: type[order.BaseCartView]


class BaseCheckoutState(ABC):
    @abstractmethod
    def mark_as_checkouted(self, checkout: order.UserData):
        pass

class BasePaymentState(ABC):
    @abstractmethod
    def mark_as_payed(self, payment: order.BasePayment):
        pass


class BaseCustomerState(BaseState, BaseCheckoutState, BasePaymentState):
    def __init__(self, order) -> None:
        self._order = order


class StateCustomerPayed(BaseCustomerState):
    cart_type = order.CartNotNutable
    def mark_as_checkouted(self, checkout):
        raise OrderStateException()

    def mark_as_payed(self, payment: order.BasePayment):
        raise OrderStateException()


class StateCustomerCheckout(BaseCustomerState):
    cart_type = order.CartMutable
    def mark_as_checkouted(self, checkout):
        raise OrderStateException()

    def mark_as_payed(self, payment: order.BasePayment):
        if not len(self._order.cart):
            raise OrderValueException()
        if payment.is_payment():
            self._order._state = StateCustomerPayed(self._order)
        else:
            raise OrderStateException()


class StateCustomerNew(BaseCustomerState):
    cart_type = order.CartMutable
    def mark_as_checkouted(self, checkout):
        if not len(self._order._cart):
            raise OrderValueException()
        self._order._user_data = checkout
        self._order._state = StateCustomerCheckout(self._order)

    def mark_as_payed(self, payment: order.BasePayment):
        raise OrderStateException()


class OrderCustomer(BaseCustomerOrder):
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
            raise OrderValueException()
        return self._user_data

    @property
    def payment(self) -> order.BasePayment:
        if not self._payment:
            raise OrderValueException()
        return self._payment

    def mark_as_checkouted(self, checkout: order.UserData):
        self._state.mark_as_checkouted(checkout)
        self._reset_cart()

    def mark_as_payed(self, payment: order.BasePayment):
        self._state.mark_as_payed(payment)
        self._reset_cart()


