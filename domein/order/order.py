from enum import Enum

from domein.order import base
from domein.order.payment import Payment


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


class OrderPayment(base.OrderPaymentBase):
    def payment(self):
        return Payment(self)


class OrderNotPayment(base.OrderPaymentBase):
    def payment(self):
        raise


class OrderNew(OrderNotPayment, OrderChangeable):
    status = Status.NEW

class OrderCheckout(OrderPayment, OrderChangeable):
    status = Status.CHECKOUTED

class OrderPayed(OrderPayment, OrderNotChangeable):
    status = Status.PAYED

class OrderReady(OrderPayment, OrderNotChangeable):
    status = Status.READY

class OrderDone(OrderPayment, OrderNotChangeable):
    status = Status.DONE


def get_order(items, user_data=None, ready=False, done=False):
    if done:
        return OrderDone(items, user_data, ready, done)
    if ready:
        return OrderReady(items, user_data, ready)
    if not user_data:
        return OrderNew(items)
    order = OrderCheckout(items, user_data)
    if order.payment.is_payment():
        return OrderPayed(items, user_data)
    return order


