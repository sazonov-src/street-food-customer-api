from .serializers import PaymentCallbackLiqpaySerializer
from .models import PaymentCallbackLiqpay

import domain

class LiqpayCallbackRepository:

    def __init__(self, order):
        self.order = order

    def get(self):
        return PaymentCallbackLiqpaySerializer(
                PaymentCallbackLiqpay.objects.filter(order=self.order), many=True).data
