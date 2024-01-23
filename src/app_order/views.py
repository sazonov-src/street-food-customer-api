from types import new_class
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

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
    @set_repo(NewOrderStateRepository, get=False)
    def post(self, request):
        self.new_order_state = create_new_order_obj(self.get_user)
        return Response(self.new_order_state.order.model_dump())

