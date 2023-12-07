from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from app_order.services import *
from app_menu.repository import *
from dj.app_order.serializer import CartLineSerializer

@api_view()
def get_order(request):
    order_repo = get_new_order_customer_repo(user=request.user)
    return Response({
        "created_at": order_repo.model.created_at.isoformat(),
        "updated_at": order_repo.model.updated_at.isoformat(),
        "status": str(order_repo.get().state)})


class CartApiView(APIView):
    def get(self, request):
        order_repo = get_new_order_customer_repo(user=request.user)
        lines = get_order_cart_lines(order=order_repo.model)
        serializer = CartLineSerializer(lines, many=True)
        order = order_repo.get()
        return Response({
            "total_count": order.cart.total_count,
            "total_price": order.cart.total_price,
            "lines": serializer.data,})

    def post(self, request):
        order_repo = get_or_create_new_order_customer_repo(user=request.user)
        order = order_repo.get()
        try:
            id, count = request.data['id_menu_item'], request.data['count']
        except KeyError: 
            raise ValidationError
        menu_item = RepositoryMenuItem(
            get_object_or_404(MenuItem, id=id)).get()
        order = order_repo.get()
        order.cart[menu_item] = count 
        order_repo.add(order)
        return Response({"id_menu_item": id, "count": count})
