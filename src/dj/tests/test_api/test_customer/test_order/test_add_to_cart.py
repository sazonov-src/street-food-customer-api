import pytest
from rest_framework.views import Response, status
from mixer.backend.django import mixer

from dj.app_order.repository import RepositoryOrder
from domain import order as ord


@pytest.mark.django_db
def test_add_to_cart_with_order(client, order, item_22):
    repo = RepositoryOrder(order)
    assert len(repo.get().cart) == 0
    r: Response = client.post(
            "/api/v1/customer/new-order/cart/", {"id_menu_item": 22, "count": 3})
    assert r.status_code == status.HTTP_200_OK
    assert len(repo.get().cart) == 1


@pytest.mark.django_db
def test_add_to_order_cart(client, item_22):
    r: Response = client.post(
            "/api/v1/customer/new-order/cart/", {"id_menu_item": 22, "count": 3})
    assert r.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_add_to_order_cart_not_found(client, item_22):
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item":2, "count": 1})
    assert r.status_code == status.HTTP_404_NOT_FOUND
    assert r.data['detail'] == "Menu item with id 2 not found"

@pytest.mark.django_db
def test_add_to_order_cart_not_id(client, item_22):
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"count": 3})
    assert r.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_add_to_order_cart_bed_count(client, item_22):
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item":22, "count": -1})
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert r.data[0] == "Count is not valide"
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item":22, "count": 0})
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item":22, "count": "pr"})
    assert r.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_add_to_order_cart_not_menuitem(client):
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item": 22, "count": 3})
    assert r.status_code == status.HTTP_404_NOT_FOUND
    assert r.data['detail'] == "Menu item with id 22 not found"

@pytest.mark.django_db
def test_double_add_to_cart(client, item_22):
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item": 22, "count": 3})
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item": 22, "count": 3})
    assert r.status_code == status.HTTP_200_OK

