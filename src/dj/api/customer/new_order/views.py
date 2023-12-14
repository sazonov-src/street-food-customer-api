from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from app_order.services import *
from app_order.serializer import CartLineSerializer

@api_view()
def get_order(request):
    order_repo = get_new_order_repo(request)
    return Response({
        "created_at": order_repo.model.created_at.isoformat(),
        "updated_at": order_repo.model.updated_at.isoformat(),
        "status": str(order_repo.get().state)})


class CartViewSet(viewsets.ViewSet):
    def list(self, request):
        order_repo = get_new_order_repo(request)
        return Response(ServiceOrederCart(order_repo).cart_info())

    def create(self, request):
        order_repo = get_or_create_new_order_repo(request)
        return Response(ServiceOrederCart(order_repo).add_line(request))

    def destroy(self, request, pk):
        order_repo = get_new_order_repo(request)
        return Response(ServiceOrederCart(order_repo).del_line(pk))

    @action(detail=True, methods=['post'])
    def plus_count(self, request, pk):
        order_repo = get_new_order_repo(request)
        return Response(ServiceOrederCart(order_repo).plus_count_line(pk))

    @action(detail=True, methods=['post'])
    def minus_count(self, request, pk):
        order_repo = get_new_order_repo(request)
        return Response(ServiceOrederCart(order_repo).minus_count_line(pk))


