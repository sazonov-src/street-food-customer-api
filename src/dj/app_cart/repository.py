import functools
from domain.models import cart
from django.db import transaction

from .serializers import ReadeOnlyCartLineSerializer, CartLineSerializer


class CartRepository:

    def __init__(self, user):
        self.user = user

    def get(self):
        serializer = ReadeOnlyCartLineSerializer(
            self.user.cartline_set, many=True)
        return cart.Cart(lines=[*serializer.data])

    @transaction.atomic
    def add(self, cart):
        self.user.cartline_set.all().delete()
        serializer = CartLineSerializer(
                data=cart.model_dump(mode='json')['lines'], many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.user)


def set_cart_repo(add=True):
    def decorator(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            cart_repo = CartRepository(self.get_user)
            self.cart = cart_repo.get()
            res = method(self, *args, **kwargs)
            if add:
                cart_repo.add(self.cart)
            return res
        return wrapper
    return decorator

