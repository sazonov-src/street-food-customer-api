from django.db import models
from app_order.models import OrderModel

class PaymentCallbackLiqpay(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    data = models.JSONField()
    signature = models.CharField(max_length=255)
