from rest_framework.exceptions import NotFound
from app_cart.repository import CartRepository
from app_contact.repository import ContactRepository

from .models import Order
from .serializers import OrderSerializer

import domain


__all__ = [
    'NewOrderStateRepository',
]

def get_ordermodel(order):
    serializer = OrderSerializer(order)
    return domain.ModalOrder(**serializer.data)

def get_neworderstate_and_order(user):
    order_set = Order.objects.filter(user=user, accepted=False)
    order_dict = {get_ordermodel(order): order for order in order_set}
    neworder_state = domain.get_new_order_state(order_dict)
    return neworder_state, order_dict[neworder_state.order]

def create_new_order_obj(user):
    order_handler = domain.StateOrderNew()
    order_handler.handle_order(
        domain.ModalOrder(
            cart_data=CartRepository(user).get(),
            contact_data=ContactRepository(user).get()))
    return order_handler


class NewOrderStateRepository:
    def __init__(self, user):
        self.user = user

    def get(self):
        return get_neworderstate_and_order(self.user)[0]

    def add(self, neworder_state):
        try:
            _, obj = get_neworderstate_and_order(self.user)
            serializer = OrderSerializer(obj, data=neworder_state.order.model_dump())
        except NotFound:
            serializer = OrderSerializer(data=neworder_state.order.model_dump())
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.user)
