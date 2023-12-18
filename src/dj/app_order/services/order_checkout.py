from domain.order import OrderCustomer, UserData

from .utils import validate

class ServiceOrderCheckout:
    def __init__(self, order: OrderCustomer) -> None:
        self._order = order

    @validate
    def mark_as_checkout(self, user_data: dict):
        data = UserData(**user_data)
        self._order.mark_as_checkouted(data)
        return user_data
