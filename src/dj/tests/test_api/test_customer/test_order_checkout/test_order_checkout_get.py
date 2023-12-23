import pytest
from rest_framework.views import Response, status
from domain import order


@pytest.mark.django_db
def test_order_checkout_get_success(client, cart_with_item22_count1, user_data):
    r: Response = client.get("/api/v1/customer/new-order/checkout/")
    assert r.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_order_checkout_get_not_found(client, cart_with_item22_count1):
    r: Response = client.get("/api/v1/customer/new-order/checkout/")
    assert r.status_code == status.HTTP_404_NOT_FOUND
    assert r.data['detail'] == order.NOT_FOUND_USERDATA_MASAGE
