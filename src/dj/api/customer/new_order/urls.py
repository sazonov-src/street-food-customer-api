from django.urls import path

from api.customer.new_order.views import CartApiView, get_order

urlpatterns = [
    path("", get_order, name="get_order"),
    path("cart/", CartApiView.as_view(), name="get_cart"),
]
