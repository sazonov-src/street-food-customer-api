from dataclasses import dataclass
import pytest

from domein.order.order_line import OrderLine
from domein.order.user_data import UserData

@dataclass
class FakePayment:
    is_payment: bool


@pytest.fixture
def order_line():
    return OrderLine(item=1, count=2)

@pytest.fixture
def user_data():
    return UserData(name="Vasia", phone="+3777887")

@pytest.fixture
def payment_true():
    return FakePayment(True)

@pytest.fixture
def payment_false():
    return FakePayment(False)
