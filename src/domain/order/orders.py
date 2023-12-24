from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable
import order


ALREADY_PAYED_MASAGE = "Order is already payed"
ALREADY_CHECKOUT_MASAGE = "Order is already checkouted"
EMPTY_CART_MASAGE = "Cart is empty"
PAYMENT_IS_NOT_VALID_MASAGE = "Payment is not valid"
FIRST_CHECKOUT_MASAGE = "Order must be checkouted first"
NOT_FOUND_USERDATA_MASAGE = "User data not found"
NOT_FOUND_PAYMENT_MASAGE = "Payment not found"


class OrderStateException(ValueError):
    pass

class NotFoundException(ValueError):
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
    pass


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
        raise OrderStateException(ALREADY_CHECKOUT_MASAGE)

    def mark_as_payed(self, payment: order.BasePayment):
        raise OrderStateException(ALREADY_PAYED_MASAGE)


class StateCustomerCheckout(BaseCustomerState):
    cart_type = order.CartMutable

    def mark_as_checkouted(self, checkout):
        raise OrderStateException(ALREADY_CHECKOUT_MASAGE)

    def mark_as_payed(self, payment: order.BasePayment):
        if not len(self._order.cart):
            raise NotFoundException(EMPTY_CART_MASAGE)
        if payment.is_payment():
            self._order._state = StateCustomerPayed(self._order)
        else:
            raise OrderStateException(PAYMENT_IS_NOT_VALID_MASAGE)


class StateCustomerNew(BaseCustomerState):
    cart_type = order.CartMutable
    def mark_as_checkouted(self, checkout):
        if not len(self._order._cart):
            raise NotFoundException(EMPTY_CART_MASAGE)
        self._order._user_data = checkout
        self._order._state = StateCustomerCheckout(self._order)

    def mark_as_payed(self, payment: order.BasePayment):
        raise OrderStateException(FIRST_CHECKOUT_MASAGE)


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
            raise NotFoundException(NOT_FOUND_USERDATA_MASAGE)
        return self._user_data

    @property
    def payment(self) -> order.BasePayment:
        if not self._payment:
            raise NotFoundException(NOT_FOUND_PAYMENT_MASAGE)
        return self._payment

    def mark_as_checkouted(self, checkout: order.UserData):
        self._state.mark_as_checkouted(checkout)
        self._reset_cart()

    def mark_as_payed(self, payment: order.BasePayment):
        self._state.mark_as_payed(payment)
        self._reset_cart()


