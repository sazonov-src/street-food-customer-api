from django.db import models


class MenuItem(models.Model):
    """Розширює MenuItemGeneral більш конкретними даними"""
    title = models.CharField(max_length=255, verbose_name='Назва')
    description = models.TextField(verbose_name='Опис')
    price = models.IntegerField(verbose_name='Ціна')


