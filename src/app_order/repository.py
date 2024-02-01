from rest_framework.exceptions import NotFound
from app_cart.repository import CartRepository
from app_contact.repository import ContactRepository

from .models import Order
from .serializers import OrderSerializer

import domain


__all__ = [
    'NewOrderRepository',
]

def get_ordermodel(order):
    serializer = OrderSerializer(order)
    return domain.ModalOrder(**serializer.data)

def get_neworderstate_and_order(user):
    order_set = Order.objects.filter(user=user, accepted=False)
    order_dict = {get_ordermodel(order): order for order in order_set}
    order = domain.get_new_order(order_dict)
    return order, order_dict[order]

def create_new_order_obj(user):
    order_handler = domain.StateOrderNew()
    return order_handler.handle_order(
        domain.ModalOrder(
            cart_data=CartRepository(user).get(),
            contact_data=ContactRepository(user).get()))


class NewOrderRepository:
    def __init__(self, user):
        self.user = user

    def get(self):
        return get_neworderstate_and_order(self.user)[0]

    def add(self, order):
        try:
            _, obj = get_neworderstate_and_order(self.user)
            serializer = OrderSerializer(obj, data=order.model_dump())
        except NotFound:
            serializer = OrderSerializer(data=order.model_dump())
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.user)
