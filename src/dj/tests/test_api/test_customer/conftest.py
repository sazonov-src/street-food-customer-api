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
    return mixer.blend("app_order.order", user=user, done=False)

@pytest.fixture
def order_done(user):
    return mixer.blend("app_order.order", user=user, done=True)

@pytest.fixture
def item_22():
    return mixer.blend("app_menu.MenuItem", id=22)

@pytest.fixture
def cart_with_item22_count1(item_22, order):
    return mixer.blend("app_order.CartLine", menu_item=item_22, order=order, count=1)

@pytest.fixture
def cart_with_item22_count2(item_22, order):
    return mixer.blend("app_order.CartLine", menu_item=item_22, order=order, count=2)

@pytest.fixture
def user_data(order, cart_with_item22_count1):
    return mixer.blend("app_order.UserData", order=order)

