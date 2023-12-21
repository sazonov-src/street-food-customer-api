import pytest
from rest_framework.views import Response, status
from mixer.backend.django import mixer


@pytest.mark.django_db
def test_plus_order_cartitem(client, cart_with_item22_count1):
    r: Response = client.post("/api/v1/customer/new-order/cart/22/plus_count/")
    assert r.status_code == status.HTTP_200_OK
    assert r.data == {'id_menu_item': '22', 'count': 2}
