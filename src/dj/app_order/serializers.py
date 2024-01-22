from rest_framework import serializers

from .models import OrderModel


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['cart_data', 'contact_data', 'accepted', 'is_ready', 'done']
