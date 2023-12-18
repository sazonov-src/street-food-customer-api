from django.urls import path

from api.customer.menu.views import MenuItemViewSet


urlpatterns = [
    path("items/", MenuItemViewSet.as_view({"get": "list"}), name="menu_items"),
    path("items/<int:pk>/", MenuItemViewSet.as_view({"get": "retrieve"}), name="menu_item"),
]
