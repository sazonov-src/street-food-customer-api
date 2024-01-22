from app_cart.repository import CartRepository
from app_contact.repository import ContactRepository

from .models import OrderModel
from .serializers import OrderSerializer

import domain


def get_new_order(user):
    order_set = OrderModel.objects.filter(user=user, accepted=False)
    for order_ in order_set:
        serializer = OrderSerializer(order_)
        if order_state_ := domain.get_new_order_handler(domain.Order(**serializer.data)):
            return order_, order_state_ 
    return None, None


def create_new_order_obj(user):
    order_handler = domain.NewOrderHandler()
    order_handler.handle_order(
        domain.Order(
            cart_data=CartRepository(user).get(),
            contact_data=ContactRepository(user).get()))
    return order_handler


class CustomNewOrderRepository:

    def __init__(self, user):
        self.user = user
        self.order, self.order_state = get_new_order(self.user)

    def get(self):
        if self.order_state:
            return self.order_state
        return create_new_order_obj(self.user)

    def add(self, order_):
        obj = [self.order] if self.order else []
        serializer = OrderSerializer(*obj, data=order_.model_dump())
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.user)
