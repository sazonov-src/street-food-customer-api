from django.db import models
from django.contrib.auth.models import User
from app_menu.models import MenuItem


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    cart = models.OneToOneField(Order, on_delete=models.CASCADE)


class CartLine(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    count = models.IntegerField()


class UserData(models.Model):
    user_name = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)

