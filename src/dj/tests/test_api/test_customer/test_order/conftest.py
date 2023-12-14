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
