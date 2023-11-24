
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.customer.new_order.views import get_order, get_cart, CartItemsViewSet

items = DefaultRouter()
items.register(r'items', CartItemsViewSet, basename='cart_items')

urlpatterns = [
    path("", get_order, name="get_order"),
    path("cart/", get_cart, name="get_cart"),
    path("cart/", include(items.urls)),
]
