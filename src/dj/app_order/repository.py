from typing import Iterable
from dataclasses import asdict

from app_order.models import CartLine, Order, UserData
from app_menu.repository import RepositoryMenuItem
from app_menu.models import MenuItem
from dj.repository import BaseRepository, base_repo
from domain import order as domain
from domain.order.orders import OrderCustomer, NotFoundException
from app_payment_callbacks.utils import get_hash_data, decode_data


class OrderMixin:
    def __init__(self, model: Order):
        self._order_model = model

    @property
    def model(self):
        return self._order_model


class RepositoryOrderCartLines(OrderMixin):
    def get(self) -> Iterable[domain.LINE]:
        for it in self._order_model.cartline_set.all():
            item_repo = RepositoryMenuItem(it.menu_item)
            yield item_repo.get(), it.count

    def add(self, cart_line: domain.LINE):
        menu_item = MenuItem.objects.get(**asdict(cart_line[0]))
        CartLine.objects.update_or_create(
                order=self._order_model, 
                menu_item=menu_item, 
                defaults={'count': cart_line[1]})


class RepositoryCheckout(OrderMixin):
    def get(self):
        userdata = self._order_model.userdata
        return domain.UserData(
                name=userdata.name,
                phone=userdata.phone)

    def add(self, userdata: domain.UserData):
        UserData.objects.update_or_create(order=self._order_model, defaults={
            'name': userdata.name,
            'phone': userdata.phone})


class RepositoryOrderPayment(OrderMixin):
    def get(self) -> domain.BasePayment:
        payment = self._order_model.paymentcallbackliqpay_set.all()
        dataset = [decode_data(data.data) for data in payment]
        return domain.PaymentLIQPay(dataset)

    def add(self, payment: domain.BasePayment):
        raise NotImplementedError


class RepositoryOrder[DM: OrderCustomer, MD: Order](OrderMixin, BaseRepository):

    def get(self):
        order_domain = OrderCustomer(RepositoryOrderCartLines(self._order_model).get())
        if hasattr(self._order_model, "userdata"):
            order_domain.mark_as_checkouted(
                RepositoryCheckout(self._order_model).get())
        if self._order_model.paymentcallbackliqpay_set.all():
            order_domain.mark_as_payed(RepositoryOrderPayment(self._order_model).get())
        return order_domain
    
    def add(self, order):
        self._order_model.cartline_set.all().delete()
        for line in order.cart.lines:
            RepositoryOrderCartLines(self._order_model).add(line)
        try:
            RepositoryCheckout(self._order_model).add(order.user_data)
        except NotFoundException:
            pass


class repo[R: RepositoryOrder](base_repo):
    pass
