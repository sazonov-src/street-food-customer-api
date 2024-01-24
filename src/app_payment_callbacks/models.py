from django.db import models
from app_order.models import Order

class PaymentCallbackLiqpay(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    data = models.JSONField()
    signature = models.CharField(max_length=255)
