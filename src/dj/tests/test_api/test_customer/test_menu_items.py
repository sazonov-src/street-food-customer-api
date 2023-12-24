import pytest
from rest_framework.response import Response
from rest_framework.views import status


@pytest.mark.django_db
def test_api_menu_item_list(client, item_22):
    r: Response = client.get("/api/v1/customer/menu/items/")
    assert r.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_api_menu_item_list_post(client, item_22):
    r: Response = client.post("/api/v1/customer/menu/items/")
    assert r.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_api_menu_item_retrieve(client, item_22):
    r: Response = client.get("/api/v1/customer/menu/items/22/")
    assert r.data["id"] == 22
    assert r.status_code == status.HTTP_200_OK


