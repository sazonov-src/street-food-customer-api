from typing import Iterable
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

from app_order.repository import RepositoryOrder
from app_order.models import CartLine, Order
from app_menu.models import MenuItem
from app_menu.repository import RepositoryMenuItem
from domain.order.orders import StateCustomerNew


class ServiceOrders:
    def __init__(self, request: Request) -> None:
        self._request = request
    
    @property
    def not_done_orders(self):
        return Order.objects.filter(user=self._request.user, done=False)

    def create_new_order(self):
        return Order.objects.create(user=self._request.user)


class BaseServiceRepo:
    repo = RepositoryOrder

    @classmethod
    def queryset_to_repo(cls, queryset):
        return (cls.repo(obj) for obj in queryset)

    @classmethod
    def get_new_repo(cls, obj):
        return cls.repo(obj)


class ServiceRepo(BaseServiceRepo):
    repo = RepositoryOrder


class ServiceOrderNew:
    def __init__(self, _orders_repos) -> None:
        self._orders_repos = _orders_repos

    def get_new_order_repo(self):
        for order_repo in self._orders_repos:
            if isinstance(order_repo.get().state, StateCustomerNew):
                return order_repo
        raise Http404


class ServiceOrederCart:
    def __init__(self, order: RepositoryOrder) -> None:
        self._order = order

    @property
    def lines_queryset(self):
        return CartLine.objects.filter(order=self._order.model)

    def add_item(self, menu_item_id, count):
        menu_item = RepositoryMenuItem(
            get_object_or_404(MenuItem, id=menu_item_id)).get()
        order = self._order.get()
        order.cart[menu_item] = count 
        self._order.add(order)

    def del_item(self, menu_item):
        pass


def get_new_order_repo(request):
    orders_queryset = ServiceOrders(request).not_done_orders
    return ServiceOrderNew(
            ServiceRepo.queryset_to_repo(orders_queryset)
        ).get_new_order_repo()

def get_or_create_new_order_repo(request):
    service_order = ServiceOrders(request)
    try: 
        return ServiceOrderNew(
                ServiceRepo.queryset_to_repo(service_order.not_done_orders)
            ).get_new_order_repo()
    except Http404:
        return ServiceRepo.get_new_repo(service_order.create_new_order())



