from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from app_order.services import *
from app_order.repository import repo


@api_view()
def get_order(request):
    order_repo = get_new_order_repo(request)
    return Response({
        "created_at": order_repo.model.created_at.isoformat(),
        "updated_at": order_repo.model.updated_at.isoformat(),
        "status": str(order_repo.get().state)})


class CartViewSet(viewsets.ViewSet):
    def list(self, request):
        with repo(get_new_order_repo(request)) as order:
            res = ServiceOrderCart(order.repo).cart_info()
        return Response(res)

    def retrieve(self, request, pk):
        order = get_new_order_repo(request).get()
        res = ServiceOrderCartLine(order.cart).get_line(pk)
        return Response(res)

    def create(self, request):
        with repo(get_or_create_new_order_repo(request)) as order:
            res = ServiceOrderCartLine(order.domain.cart).add_line(request)
        return Response(res)

    def destroy(self, request, pk):
        with repo(get_new_order_repo(request)) as order:
            res = ServiceOrderCartLine(order.domain.cart).del_line(pk)
        return Response(res)

    @action(detail=True, methods=['post'])
    def plus_count(self, request, pk):
        with repo(get_new_order_repo(request)) as order:
            res = ServiceOrderCartLine(order.domain.cart).plus_count_line(pk)
        return Response(res)

    @action(detail=True, methods=['post'])
    def minus_count(self, request, pk):
        with repo(get_new_order_repo(request)) as order:
            res = ServiceOrderCartLine(order.domain.cart).minus_count_line(pk)
        return Response(res)

