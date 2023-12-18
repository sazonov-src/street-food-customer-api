from django.shortcuts import get_object_or_404

from app_menu.models import MenuItem
from app_menu.repository import RepositoryMenuItem
from app_order.repository import RepositoryOrder

from .base import CartLine
from .utils import validate


class ServiceOrderCartLine(CartLine):
    def __init__(self, cart) -> None:
        self._cart = cart

    @staticmethod
    def _get_menu_item(menu_item_id: int):
        return RepositoryMenuItem(
            get_object_or_404(MenuItem, id=menu_item_id)).get()

    @validate
    def add_line(self, request):
        id, count = request.data['id_menu_item'], request.data['count']
        self._cart[self._get_menu_item(id)] = count 
        return {"id_menu_item": id, "count": count}

    @validate
    def del_line(self, pk):
        del self._cart[self._get_menu_item(pk)]
        return {"id_menu_item": pk}

    @validate
    def plus_count_line(self, pk):
        item = self._get_menu_item(pk)
        self._cart[item] += 1
        return {"id_menu_item": pk, "count": self._cart[item]}

    @validate
    def minus_count_line(self, pk):
        item = self._get_menu_item(pk)
        self._cart[item] -= 1
        return {"id_menu_item": pk, "count": self._cart[item]}

    @validate
    def get_line(self, pk) -> dict:
        item = self._get_menu_item(pk)
        return {"id_menu_item": pk, "count": self._cart[item]}
