from typing import Iterable
from dataclasses import asdict

from django.core.exceptions import ObjectDoesNotExist

from app_menu.models import MenuItem
from app_order.models import CartLine, Order, UserData
from app_menu.repository import RepositoryMenuItem
from dj.repository import BaseRepository
from domain import order


class RepositoryOrder(BaseRepository):

    def __init__(self, order: Order):
        self._order_model = order

    @property
    def model(self):
        return self._order_model

    @property
    def _cart_lines(self) -> Iterable[order.LINE]:
        lines_set = self._order_model.cartline_set.all()
        for line in lines_set:
            item_repo = RepositoryMenuItem(line.menu_item)
            yield item_repo.get(), line.count

    @property
    def _userdata(self):
        return order.UserData(
                name=self._order_model.userdata.user_name,
                phone=self._order_model.userdata.phone)

    def get(self) -> order.OrderCustomer:
        domain_order = order.OrderCustomer(self._cart_lines)
        try:
            self._order_model.userdata
            domain_order.mark_as_checkouted(self._userdata)
        except ObjectDoesNotExist:
            pass
        return domain_order
    
    def add(self, order_: order.OrderCustomer):
        self._order_model.cartline_set.all().delete()
        for cart_line in order_.cart.lines:
            item_model = MenuItem.objects.get(**asdict(cart_line[0]))
            CartLine.objects.create(
                    order = self._order_model,
                    menu_item = item_model,
                    count = cart_line[1])
        try:
            self._order_model.userdata.delete()
            UserData.objects.create(
                    order=self._order_model, 
                    user_name=order_.user_data.name, 
                    phone=order_.user_data.phone)
        except (ObjectDoesNotExist, order.OrderValueException):
            pass


            



