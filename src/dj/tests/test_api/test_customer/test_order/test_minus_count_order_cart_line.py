import pytest
from rest_framework.views import Response, status
from domain import order as ord


@pytest.mark.django_db
def test_minus_order_cartitem(client, cart_with_item22_count2):
    r: Response = client.post("/api/v1/customer/new-order/cart/22/minus_count/")
    assert r.status_code == status.HTTP_200_OK
    assert r.data == {'id_menu_item': '22', 'count': 1}

@pytest.mark.django_db
def test_bad_request_order_cartitem(client, cart_with_item22_count1):
    r: Response = client.post("/api/v1/customer/new-order/cart/22/minus_count/")
    assert r.status_code == status.HTTP_400_BAD_REQUEST
    assert r.data[0] == ord.COUNT_ERROR_MASAGE
