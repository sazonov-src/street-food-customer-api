from rest_framework.request import Request
from rest_framework.exceptions import NotFound

from app_order.models import Order
from app_order.repository import RepositoryOrder
from domain.order.orders import StateCustomerNew, StateCustomerPayed


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
            if not isinstance(order_repo.get().state, StateCustomerPayed):
                return order_repo
        raise NotFound("New order not found")

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
    except NotFound:
        return ServiceRepo.get_new_repo(service_order.create_new_order())
