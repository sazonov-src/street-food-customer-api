#liqpay serializers here.
from rest_framework import serializers
import base64
import json

from .models import PaymentCallbackLiqpay
from . import utils

class PaymentCallbackLiqpaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCallbackLiqpay
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        data = kwargs.get('data')
        if data:
            decoded_data = utils.decode_data(data['data'])
            data['order_id'] = decoded_data['order_id']
        super().__init__(*args, **kwargs)

    def validate(self, data):
        if data['signature'] != utils.hash_data_to_sign(data['data']):
            raise serializers.ValidationError('Invalid signature')
        return data
