import pytest
from rest_framework.test import APIClient

@pytest.mark.urls('dj.dj.urls')
def test_():
    client = APIClient()
    client.get("menu_items")
    print(client)

