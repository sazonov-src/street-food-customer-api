import pytest
from mixer.backend.django import mixer
from app_order.repository import RepositoryOrder

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

class TestRepositoryOrder(RepositoryOrder):
    def __init__(self):
        self._order_model = mixer.blend('app_order.Order')


@pytest.fixture
def fake_repo():
    return TestRepositoryOrder()

@pytest.fixture
def model_item():
    return mixer.blend("app_menu.MenuItem")

@pytest.fixture
def domain_item(model_item):
    return RepositoryMenuItem(model_item).get()

@pytest.fixture
def domain_user_data():
    return order.UserData("Vasia", "01")

@pytest.fixture
def domain_order(domain_item):
    return order.OrderCustomer([(domain_item, 1)])

@pytest.fixture
def model_order():
    return mixer.blend("app_order.Order")
