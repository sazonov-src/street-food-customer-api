import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIClient


@pytest.fixture
def user():
    return mixer.blend('auth.user')


@pytest.fixture
def client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def order(user):
    return mixer.blend("app_order.order", user=user)

@pytest.fixture
def item_22():
    return mixer.blend("app_menu.MenuItem", id=22)

@pytest.fixture
def cart_not_empty(item_22, order):
    return mixer.blend("app_order.CartLine", item=item_22, order=order, count=2)

@pytest.fixture
def user_data(order, cart_not_empty):
    return mixer.blend("app_order.UserData", order=order)
