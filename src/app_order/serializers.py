from rest_framework import serializers

from .models import OrderModel


class OrderSerializer(serializers.ModelSerializer):
    pay_callbacks = serializers.SerializerMethodField()

    class Meta:
        model = OrderModel
        fields = ['cart_data', 'contact_data', 'accepted', 'is_ready', 'done', 'pay_callbacks']

    def get_pay_callbacks(self, obj):
        return [call.data for call in obj.paymentcallbackliqpay_set.all()]

