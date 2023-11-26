import pytest
from mixer.backend.django import mixer

from domain import items
from domain import order
from app_menu.repository import RepositoryMenuItem

class FakePayment(order.BasePayment):
    def order(self):
        pass
    def get_payment_url(self) :
        pass

class FakePaymentTrue(FakePayment):
    def is_payment(self) -> bool:
        return True

@pytest.fixture
def item_model():
    return mixer.blend("app_menu.MenuItem")

@pytest.fixture
def item(item_model):
    return RepositoryMenuItem(item_model).get()

@pytest.fixture
def user_data():
    return order.UserData("Vasia", "01")

@pytest.fixture
def order_domain(item):
    ord = order.OrderCustomer([(item, 1)])
    return ord

@pytest.fixture
def order_model(item_model):
    model = mixer.blend("app_order.Order")
    mixer.blend("app_order.CartLine", order=model, menu_item=item_model)
    return model
