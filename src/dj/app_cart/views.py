from rest_framework import viewsets
from rest_framework.response import Response

from app_cart.repository import CartRepository
from app_menu.models import MenuItem
from domain.models import cart
from app_cart.serializers import MenuItemSerializer, CartLineSerializer
from django.shortcuts import get_object_or_404


class CartViewSet(viewsets.ViewSet):

    @property
    def get_user(self):
        return self.request.user

    @property
    def cart_repo(self):
        return CartRepository(self.get_user)

    def list(self, request):
        cart = self.cart_repo.get()
        return Response(cart.model_dump())

    def create(self, request):
        line = CartLineSerializer(data=request.data)
        line.is_valid(raise_exception=True)
        cart_ = self.cart_repo.get()
        cart_.add_item(
                self._get_product_or_404(line.data['menu_item']),
                line.data['quantity'])
        self.cart_repo.add(cart_)
        return Response(cart_.model_dump())

    def retrieve(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        cart_ = self.cart_repo.get()
        cart_.remove_item(self._get_product_or_404(pk))
        self.cart_repo.add(cart_)
        return Response({'message': 'Item removed from cart'})

    def _get_product_or_404(self, id):
        menuitem = get_object_or_404(MenuItem, id=id)
        return cart.Product(**MenuItemSerializer(menuitem).data)
        
