from __future__ import annotations
from django.db import models
from django.contrib.auth.models import User
from app_menu.models import MenuItem


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ready = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    cartline_set: models.QuerySet[CartLine]
    userdata: UserData


class CartLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    count = models.IntegerField()


class UserData(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)

