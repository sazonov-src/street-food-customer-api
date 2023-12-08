import pytest
from rest_framework.views import Response, status
from mixer.backend.django import mixer

from dj.app_order.repository import RepositoryOrder


@pytest.mark.django_db
def test_add_to_cart_with_order(client, user, order):
    mixer.blend("app_menu.MenuItem", id=1)
    repo = RepositoryOrder(order)
    assert len(repo.get().cart) == 0
    r: Response = client.post(
            "/api/v1/customer/new-order/cart/", {"id_menu_item": 1, "count": 3})
    assert r.status_code == status.HTTP_200_OK
    assert len(repo.get().cart) == 1


@pytest.mark.django_db
def test_add_to_cart_with_not_order(client, user):
    mixer.blend("app_menu.MenuItem", id=1)
    r: Response = client.get("/api/v1/customer/new-order/")
    assert r.status_code == status.HTTP_404_NOT_FOUND
    r: Response = client.post(
            "/api/v1/customer/new-order/cart/", {"id_menu_item": 1, "count": 3})
    assert r.status_code == status.HTTP_200_OK
    r: Response = client.get("/api/v1/customer/new-order/")
    assert r.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_add_to_order_cart_bed_data(client, user):
    mixer.blend("app_menu.MenuItem", id=1)
    r: Response = client.post("/api/v1/customer/new-order/cart/", {})
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"count": 3})
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item": 1})
    assert r.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_add_to_order_cart_not_menuitem(client, user):
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item": 1, "count": 3})
    assert r.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_double_add_to_cart(client, user):
    mixer.blend("app_menu.MenuItem", id=1)
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item": 1, "count": 3})
    r: Response = client.post("/api/v1/customer/new-order/cart/", {"id_menu_item": 1, "count": 3})
    assert r.status_code == status.HTTP_200_OK

