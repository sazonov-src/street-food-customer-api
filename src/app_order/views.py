from types import new_class
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError

from src.utils import set_repo, validate
from .repository import NewOrderStateRepository, create_new_order_obj

import domain

class NewOrderAPIView(APIView):
    new_order_state: domain.StateOrderNew

    @property
    def get_user(self):
        return self.request.user
    
    @validate
    @set_repo(NewOrderStateRepository, add=False)
    def get(self, request):
        return Response(self.new_order_state.order.model_dump())

    @validate
    def post(self, request):
        repo = NewOrderStateRepository(self.get_user)
        try:
            repo.get()
        except NotFound:
            repo.add(neworder_state := create_new_order_obj(self.get_user))
            return Response(neworder_state.order.model_dump())
        raise ValidationError('Order already created')

