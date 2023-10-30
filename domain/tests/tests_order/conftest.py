from dataclasses import dataclass
import pytest
from domain import order


@dataclass
class FakePayment:
    is_payment: bool


@pytest.fixture
def order_line():
    return order.OrderLine(item=1, count=2)

@pytest.fixture
def user_data():
    return order.UserData(name="Vasia", phone="+3777887")

@pytest.fixture
def payment_true():
    return FakePayment(True)

@pytest.fixture
def payment_false():
    return FakePayment(False)
