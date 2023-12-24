from domain.order import OrderCustomer, UserData
from app_order.serializer import UserDataSerializer

from .utils import validate

class ServiceOrderCheckout:
    def __init__(self, order: OrderCustomer) -> None:
        self._order = order

    @validate
    def mark_as_checkout(self, user_data: dict):
        data = UserData(**user_data)
        self._order.mark_as_checkouted(data)
        return user_data

    @validate
    def get_checkout(self):
        return UserDataSerializer(self._order.user_data).data
