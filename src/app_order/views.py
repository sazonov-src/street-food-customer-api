from types import new_class
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.decorators import api_view

from src.utils import set_repo, validate
from .repository import NewOrderRepository, create_new_order_obj

import domain


class NewOrderAPIView(APIView):
    new_order: domain.ModalOrder

    @property
    def get_user(self):
        return self.request.user
    
    @validate
    @set_repo(NewOrderRepository, add=False)
    def get(self, request):
        return Response(self.new_order.model_dump())

    @validate
    def post(self, request):
        repo = NewOrderRepository(self.get_user)
        try:
            repo.get()
        except NotFound:
            repo.add(new_order := create_new_order_obj(self.get_user))
            return Response(new_order.model_dump())
        raise ValidationError('Order already created')


@api_view(['GET'])
def get_payment_data(request):
    repo = NewOrderRepository(request.user)
    liqpay = domain.LiqpaySDK(
        domain.get_liqpay_payment_data(repo.get()))
    return Response({'data': liqpay.encode_data, 'signature': liqpay.signature})
