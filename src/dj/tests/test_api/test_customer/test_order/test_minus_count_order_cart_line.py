import pytest
from rest_framework.views import Response, status
from mixer.backend.django import mixer


@pytest.mark.django_db
def test_minus_order_cartitem(client, item_22):
    client.post("/api/v1/customer/new-order/cart/", {"id_menu_item": 22, "count": 2})
    r: Response = client.post("/api/v1/customer/new-order/cart/22/minus_count/")
    assert r.status_code == status.HTTP_200_OK
    assert r.data == {'id_menu_item': '22', 'count': 1}


@pytest.mark.django_db
def test_bad_request_order_cartitem(client, item_22):
    client.post("/api/v1/customer/new-order/cart/", {"id_menu_item": 22, "count": 1})
    r: Response = client.post("/api/v1/customer/new-order/cart/22/minus_count/")
    assert r.status_code == status.HTTP_400_BAD_REQUEST
