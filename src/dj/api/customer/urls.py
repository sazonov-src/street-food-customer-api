from django.urls import path

from api.customer.views import MenuItemViewSet

urlpatterns = [
        path("menu/items", MenuItemViewSet.as_view({"get": "list"}), name="menu_items")
        ]
