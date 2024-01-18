from rest_framework import serializers

from .models import CartLine
from app_menu.models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'price']


class CartLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartLine
        fields = ['menu_item', 'quantity']


class ReadeOnlyCartLineSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)

    class Meta:
        model = CartLine
        fields = ['menu_item', 'quantity', 'created_at', 'updated_at']


