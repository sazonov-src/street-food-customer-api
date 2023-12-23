import pytest
from rest_framework.views import Response, status


@pytest.mark.django_db
def test_order_checkout_success(client, cart_with_item22_count1):
    r: Response = client.post(
            "/api/v1/customer/new-order/checkout/", {"name": "test", "phone": "123"})
    assert r.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_order_checkout_not_found(client, order):
    r: Response = client.post(
            "/api/v1/customer/new-order/checkout/", {"name": "test", "phone": "123"})
    assert r.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_order_already_checkouted(client, cart_with_item22_count1, user_data):
    r: Response = client.post(
            "/api/v1/customer/new-order/checkout/", {"name": "test", "phone": "123"})
    assert r.status_code == status.HTTP_400_BAD_REQUEST
