import pytest
from rest_framework.test import APIClient
from mixer.backend.django import mixer

def _create_menu_item(id):
    return mixer.blend('app_menu.MenuItem', id=id, price=10)

@pytest.fixture
def user():
    return mixer.blend('auth.User')


@pytest.fixture
def client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def menu_items1_2_3():
    return [_create_menu_item(1), _create_menu_item(2), _create_menu_item(3)]

@pytest.fixture
def menu_item4():
    return _create_menu_item(4)

@pytest.fixture
def cart_lines1_2_3(menu_items1_2_3, user):
    return [mixer.blend('app_cart.CartLine', menu_item=i, quantity=1, user=user)
            for i in menu_items1_2_3]

@pytest.fixture
def contact(user):
    return mixer.blend('app_contact.Contact', user=user, name='name', phone='phone')

