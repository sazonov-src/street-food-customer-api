import pytest
from rest_framework.views import Response, status


@pytest.mark.django_db
def test_order_checkout_get_success(client, cart_not_empty, user_data):
    r: Response = client.get("/api/v1/customer/new-order/checkout/")
    assert r.status_code == status.HTTP_200_OK
