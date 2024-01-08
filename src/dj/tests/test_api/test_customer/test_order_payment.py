import pytest
from rest_framework.response import Response
from rest_framework.views import status


@pytest.mark.django_db
def test_get_payment_data(client, user_data, cart_with_item22_count1):
    res = client.get("/api/v1/customer/new-order/payment-data/")
    assert res.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_get_payment_data_payed(client, cart_with_item22_count1, user_data, payment_success):
    res = client.get("/api/v1/customer/new-order/payment-data/")
    assert res.status_code == status.HTTP_404_NOT_FOUND # This order already not new
