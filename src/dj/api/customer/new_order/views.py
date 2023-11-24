
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


@api_view()
def get_order(request):
    return Response({"massage": "this is inform for your order"})


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
