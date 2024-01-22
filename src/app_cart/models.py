from django.db import models
from django.contrib.auth.models import User
from app_menu.models import MenuItem


class CartLine(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
