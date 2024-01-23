from rest_framework.exceptions import NotFound
from app_cart.repository import CartRepository
from app_contact.repository import ContactRepository

from .models import OrderModel
from .serializers import OrderSerializer

import domain


__all__ = [
    'NewOrderStateRepository',
]


def get_neworderstate_and_ordermodel_or_none(user):
    order_set = OrderModel.objects.filter(user=user, accepted=False)
    for order_ in order_set:
        serializer = OrderSerializer(order_)
        if order_state_ := domain.get_new_order_state(domain.ModalOrder(**serializer.data)):
            return order_, order_state_ 
    return None, None

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
        self.order, self.order_state = get_neworderstate_and_ordermodel_or_none(self.user)

    def get(self):
        if self.order_state:
            return self.order_state
        raise NotFound('No new order found')

    def add(self, neworder_state):
        obj = [self.order] if self.order else []
        serializer = OrderSerializer(*obj, data=neworder_state.order.model_dump())
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.user)
