import pytest
from rest_framework.test import APIClient
from rest_framework.response import Response
from mixer.backend.django import mixer
from rest_framework.views import status

client = APIClient()

@pytest.mark.django_db
def test_api_menu_item_list():
    mixer.cycle(5).blend("app_menu.MenuItem")
    r: Response = client.get("/api/v1/customer/menu/items/")
    assert len(r.data) == 5
    assert r.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_api_menu_item_list_post():
    r: Response = client.post("/api/v1/customer/menu/items/")
    assert r.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_api_menu_item_retrieve():
    mixer.blend("app_menu.MenuItem", pk=1)
    r: Response = client.get("/api/v1/customer/menu/items/1/")
    assert r.data["id"] == 1
    assert r.status_code == status.HTTP_200_OK


