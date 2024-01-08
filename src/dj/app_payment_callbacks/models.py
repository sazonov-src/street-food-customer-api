from django.db import models

class PaymentCallbackLiqpay(models.Model):
    data = models.TextField()
    signature = models.CharField(max_length=255)
    order_id = models.ForeignKey('app_order.Order', on_delete=models.CASCADE)
