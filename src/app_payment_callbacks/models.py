from django.db import models

class PaymentCallbackLiqpay(models.Model):
    data = models.TextField()
    signature = models.CharField(max_length=255)
