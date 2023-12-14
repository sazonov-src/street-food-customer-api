import pytest
from rest_framework.views import Response, status
from mixer.backend.django import mixer


@pytest.mark.django_db
def test_del_order_cartitem(client, item_22):
    client.post("/api/v1/customer/new-order/cart/", {"id_menu_item": 22, "count": 1})
    r: Response = client.delete("/api/v1/customer/new-order/cart/22/")
    assert r.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_del_order_cartitem_not_in_cart(client, item_22, order):
    r: Response = client.delete("/api/v1/customer/new-order/cart/22/")
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    

@pytest.mark.django_db
def test_del_order_cartitem_not_order(client, item_22):
    r: Response = client.delete("/api/v1/customer/new-order/cart/22/")
    assert r.status_code == status.HTTP_404_NOT_FOUND
