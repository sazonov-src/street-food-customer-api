from typing import Any
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app_cart.repository import set_cart_repo
from app_menu.models import MenuItem
from app_cart.serializers import MenuItemSerializer, CartLineSerializer
from src.utils import validate, set_repo

import domain

from .repository import CartRepository

class CartViewSet(viewsets.ViewSet):
    cart: Any

    @property
    def get_user(self):
        return self.request.user

    @set_repo(CartRepository, add=False)
    def list(self, request):
        return Response(self.cart.model_dump())

    @set_repo(CartRepository)
    def create(self, request):
        line = CartLineSerializer(data=request.data)
        line.is_valid(raise_exception=True)
        self.cart.add_item(
                self._get_product_or_404(line.data['menu_item']),
                line.data['quantity'])
        return Response(self.cart.model_dump())

    @set_repo(CartRepository)
    def destroy(self, request, pk=None):
        self.cart.remove_item(self._get_product_or_404(pk))
        return Response({'message': 'Item removed from cart'})

    @action(detail=True, methods=['post'])
    @set_repo(CartRepository)
    def plus_quantity(self, request, pk):
        line = self.cart.get_line(
                self._get_product_or_404(pk))
        line.plus_quantity()
        return Response(line.model_dump())

    @action(detail=True, methods=['post'])
    @validate
    @set_repo(CartRepository)
    def minus_quantity(self, request, pk):
        line = self.cart.get_line(
                self._get_product_or_404(pk))
        line.minus_quantity()
        return Response(line.model_dump())

    def _get_product_or_404(self, id):
        menuitem = get_object_or_404(MenuItem, id=id)
        return domain.ModelCartItem(**MenuItemSerializer(menuitem).data)
