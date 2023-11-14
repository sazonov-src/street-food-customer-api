import pytest
import items
import order

class FakePayment(order.BasePayment):
    def order(self):
        pass
    def get_payment_url(self) :
        pass

class FakePaymentTrue(FakePayment):
    def is_payment(self) -> bool:
        return True

class FakePaymentFalse(FakePayment):
    def is_payment(self) -> bool:
        return False

@pytest.fixture
def payment_true():
    return FakePaymentTrue()

@pytest.fixture
def payment_false():
    return FakePaymentFalse()

@pytest.fixture
def item():
    return items.Item("Item", "good item", 30.)

@pytest.fixture
def checkout():
   return order.UserData("Vasia", "01")

@pytest.fixture
def order_new_with_empty_cart():
    return order.OrderCustomer([],) 

@pytest.fixture
def order_new(item):
    return order.OrderCustomer([(item, 1)])

@pytest.fixture
def order_checkouted(item, checkout):
    ord = order.OrderCustomer([(item, 1)])
    ord.mark_as_checkouted(checkout)
    return ord

@pytest.fixture
def order_payed(item, checkout, payment_true):
    ord = order.OrderCustomer([(item, 1)])
    ord.mark_as_checkouted(checkout)
    ord.mark_as_payed(payment_true)
    return ord


