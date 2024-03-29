import functools
from django.db import transaction

import domain

from .serializers import ReadeOnlyCartLineSerializer, CartLineSerializer


class CartRepository:

    def __init__(self, user):
        self.user = user

    def get(self):
        serializer = ReadeOnlyCartLineSerializer(
            self.user.cartline_set, many=True)
        return domain.ModelCart(lines=[*serializer.data])

    @transaction.atomic
    def add(self, cart):
        self.user.cartline_set.all().delete()
        serializer = CartLineSerializer(
                data=cart.model_dump(mode='json')['lines'], many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.user)
