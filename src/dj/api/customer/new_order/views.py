from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from app_order.services import *

@api_view()
def get_order(request):
    order_repo = get_new_repo_order_customer(user=request.user)
    return Response({
        "created_at": order_repo.model.created_at.isoformat(),
        "updated_at": order_repo.model.updated_at.isoformat(),
        "status": str(order_repo.get().state),
        })

@api_view()
def get_cart(request):
    return Response({"massage": "this is inform for your cart"})


class CartItemsViewSet(ViewSet):

    def list(self, request: Request):
        return Response([{"item":1}, {"item":2}])

    def create(self, request):
        return Response({"massage": "The order was created"})

    def retrieve(self, request, pk=None):
        return Response({"item": 1})

    def update(self, request, pk=None):
        return Response({"massage": "The order was updated"})

    def destroy(self, request, pk=None):
        return Response({"massage": "The order was deleted"})
