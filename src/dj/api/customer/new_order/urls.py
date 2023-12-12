from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.customer.new_order.views import CartViewSet, get_order

cart = DefaultRouter()
cart.register('cart', CartViewSet, basename='cart')

urlpatterns = [
    path("", get_order, name="get_order"),
    path("", include(cart.urls)),
]
