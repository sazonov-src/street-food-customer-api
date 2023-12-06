from dj.serializers import BaseModelSerializer
from app_order.models import *


class OrderSerializer(BaseModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CartLineSerializer(BaseModelSerializer):
    class Meta:
        model = CartLine
        fields = '__all__'


class UserDataSerializer(BaseModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'
