import pytest
from rest_framework.views import Response, status
from mixer.backend.django import mixer

@pytest.mark.django_db
def test_get_order(client):
    r: Response = client.get("/api/v1/customer/new-order/")
    assert r.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_get_order_not_done(client, user):
    mixer.blend('app_order.Order', user=user, done=False)
    r: Response = client.get("/api/v1/customer/new-order/")
    assert r.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_get_order_with_done(client, user):
    mixer.blend('app_order.Order', user=user, done=True)
    r: Response = client.get("/api/v1/customer/new-order/")
    assert r.status_code == status.HTTP_404_NOT_FOUND

