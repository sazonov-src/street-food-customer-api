import pytest
from rest_framework.views import Response, status

@pytest.mark.django_db
def test_get_order_cart(client, order):
    r: Response = client.get("/api/v1/customer/new-order/cart/")
    assert r.status_code == status.HTTP_200_OK
    assert len(r.data['lines']) == 0

@pytest.mark.django_db
def test_get_order_cart_with_item(client, cart_with_item22_count1):
    r: Response = client.get("/api/v1/customer/new-order/cart/")
    assert r.status_code == status.HTTP_200_OK
    assert len(r.data['lines']) == 1

@pytest.mark.django_db
def test_get_not_order(client):
    r: Response = client.get("/api/v1/customer/new-order/cart/")
    assert r.status_code == status.HTTP_404_NOT_FOUND
    
