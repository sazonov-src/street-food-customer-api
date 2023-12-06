from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from app_order.services import *
from dj.app_order.serializer import CartLineSerializer, OrderSerializer

@api_view()
def get_order(request):
    order_repo = get_new_order_customer_repo(user=request.user)
    return Response({
        "created_at": order_repo.model.created_at.isoformat(),
        "updated_at": order_repo.model.updated_at.isoformat(),
        "status": str(order_repo.get().state),
        })

@api_view()
def get_cart(request):
    order_repo = get_new_order_customer_repo(user=request.user)
    lines = get_order_cart_lines(order=order_repo.model)
    serializer = CartLineSerializer(lines, many=True)
    order = order_repo.get()
    return Response({
        "total-count": order.cart.total_count,
        "total-price": order.cart.total_price,
        "lines": serializer.data,})
