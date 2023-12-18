from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CartViewSet, get_order, CheckoutView

cart = DefaultRouter()
cart.register('cart', CartViewSet, basename='cart')

urlpatterns = [
    path("", get_order, name="get_order"),
    path("", include(cart.urls)),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]
