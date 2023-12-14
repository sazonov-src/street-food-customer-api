from django.http.response import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.views import Response

from app_order.repository import RepositoryOrder
from app_order.models import CartLine, Order
from app_menu.models import MenuItem
from app_menu.repository import RepositoryMenuItem
from app_order.serializer import CartLineSerializer
from domain.order.orders import StateCustomerNew


def validate(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError) as ex:
            raise ValidationError(ex)
    return wrapper


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
        self._order_repo = order

    @property
    def _lines_queryset(self):
        return CartLine.objects.filter(order=self._order_repo.model)

    @staticmethod
    def _get_menu_item(menu_item_id: int):
        return RepositoryMenuItem(
            get_object_or_404(MenuItem, id=menu_item_id)).get()

    @validate
    def cart_info(self):
        serializer = CartLineSerializer(
                ServiceOrederCart(self._order_repo)._lines_queryset, many=True)
        order = self._order_repo.get()
        return {
            "total_count": order.cart.total_count,
            "total_price": order.cart.total_price,
            "lines": serializer.data,}
        
    @validate
    def add_line(self, request):
        id, count = request.data['id_menu_item'], request.data['count']
        order = self._order_repo.get()
        order.cart[self._get_menu_item(id)] = count 
        self._order_repo.add(order)
        return {"id_menu_item": id, "count": count}

    @validate
    def del_line(self, pk):
        order = self._order_repo.get()
        del order.cart[self._get_menu_item(pk)]
        self._order_repo.add(order)
        return {"id_menu_item": pk}

    @validate
    def plus_count_line(self, pk):
        order = self._order_repo.get()
        item = self._get_menu_item(pk)
        order.cart[item] += 1
        self._order_repo.add(order)
        return {"id_menu_item": pk, "count": order.cart[item]}

    @validate
    def minus_count_line(self, pk):
        order = self._order_repo.get()
        item = self._get_menu_item(pk)
        order.cart[item] -= 1
        self._order_repo.add(order)
        return {"id_menu_item": pk, "count": order.cart[item]}



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



