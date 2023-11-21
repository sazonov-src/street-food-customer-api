import pytest
from app_menu.serializer import MenuItemSerializer
from dj.serializers import SaveException
from rest_framework.parsers import JSONParser

def test_menu_item_serializer():
    data = {"title": "Some Item", "description": "desc", "price": 22.00}
    serializer = MenuItemSerializer(data)
    assert serializer.data == data
    with pytest.raises(SaveException):
        serializer.save()
