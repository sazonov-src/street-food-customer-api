import pytest
from rest_framework.views import Response, status


@pytest.mark.django_db
def test_del_order_cartitem(client, cart_with_item22_count1):
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
