import pytest
from mixer.backend.django import mixer

from app_menu.serializer import MenuItemSerializer
from app_order.serializer import *
from dj.serializers import SaveException
from rest_framework.parsers import JSONParser


def test_menu_item_serializer():
    data = {"title": "Some Item", "description": "desc", "price": 22.00}
    serializer = MenuItemSerializer(data)
    assert serializer.data == data
    with pytest.raises(SaveException):
        serializer.save()

@pytest.mark.django_db
def test_order_serializers():
    order = mixer.blend("app_order.Order")
    lines = mixer.cycle(5).blend("app_order.CartLine", order=order)
    order_serializer = OrderSerializer(order)
    lines_serializer = CartLineSerializer(lines, many=True)
    assert len(lines_serializer.data) == 5
