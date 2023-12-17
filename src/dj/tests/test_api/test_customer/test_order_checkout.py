import pytest
from rest_framework.views import Response, status


@pytest.mark.django_db
def test_add_to_cart_with_order(client, cart_not_empty):
    r: Response = client.post(
            "/api/v1/customer/new-order/checkout/", {"name": "test", "phone": "123"})
    assert r.status_code == status.HTTP_200_OK
    r: Response = client.post(
            "/api/v1/customer/new-order/checkout/", {"name": "test", "phone": "123"})
    assert r.status_code == status.HTTP_404_NOT_FOUND #not found order
