from rest_framework import serializers
from .models import PaymentCallbackLiqpay


class PaymentCallbackLiqpaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCallbackLiqpay
        fields = '__all__'
