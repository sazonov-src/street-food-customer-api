from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from app_cart.views import CartViewSet


class CastomerCartViewSet(CartViewSet):
    pass


cart = routers.DefaultRouter()
cart.register('cart', CastomerCartViewSet, basename='cart')


urlpatterns = cart.urls
