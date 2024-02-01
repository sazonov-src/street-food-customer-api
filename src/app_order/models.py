from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_data = models.JSONField()
    contact_data = models.JSONField()  
    accepted = models.BooleanField(default=False)
    is_ready = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
