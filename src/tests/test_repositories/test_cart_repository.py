import pytest
from app_cart.repository import CartRepository
from app_menu.models import MenuItem
from app_cart.serializers import MenuItemSerializer, ReadeOnlyCartLineSerializer


@pytest.mark.django_db
def test_get(user, cartlines):
    cart = CartRepository(user).get()
    assert len(cart) == 3

@pytest.mark.django_db
def test_add(user, cartlines, menuitem33_domain):
    assert len(MenuItem.objects.all()) == 4
    cart = CartRepository(user).get()
    assert len(cart) == 3
    cart.add_item(menuitem33_domain, 1)
    CartRepository(user).add(cart)
    assert len(cart) == 4
    assert len(MenuItem.objects.all()) == 4

@pytest.mark.django_db
def test_get_empty_cart(user):
    cart = CartRepository(user).get()
    assert len(cart) == 0

@pytest.mark.django_db
def test_add_empty_cart(user):
    cart = CartRepository(user).get()
    assert len(cart) == 0
    CartRepository(user).add(cart)

