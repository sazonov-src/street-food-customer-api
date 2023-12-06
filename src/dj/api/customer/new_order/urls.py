from django.urls import path

from api.customer.new_order.views import get_order, get_cart

urlpatterns = [
    path("", get_order, name="get_order"),
    path("cart/", get_cart, name="get_cart"),
]
