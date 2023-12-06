
from typing import Iterable
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http import Http404

from app_order.repository import RepositoryOrder
from app_order.models import CartLine, Order
from domain.order.orders import StateCustomerNew


def _get_queryset_not_done_orders(user: User) -> QuerySet[Order]:
    return Order.objects.filter(user=user, done=False)

def _convert_queryset_to_repo_customer_orders(
        queryset: QuerySet[Order]
        ) -> Iterable[RepositoryOrder]:
    return (RepositoryOrder(order) for order in queryset)

def _get_new_repo_order_customer[T: RepositoryOrder](
        orders_customer_repo: Iterable[T]
        ) -> T:
    for order_repo in orders_customer_repo:
        if isinstance(order_repo.get().state, StateCustomerNew):
            return order_repo
    raise Http404


def get_new_order_customer_repo(user: User):
    queryset = _get_queryset_not_done_orders(user=user)
    orders_repo = _convert_queryset_to_repo_customer_orders(queryset=queryset)
    return _get_new_repo_order_customer(orders_customer_repo=orders_repo)

def get_order_cart_lines(order: Order):
    return CartLine.objects.filter(order=order)
