from rest_framework.decorators import api_view
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


class CartApiView(APIView):
    def get(self, request):
        order_repo = get_new_order_repo(request)
        serializer = CartLineSerializer(
                ServiceOrederCart(order_repo).lines_queryset, many=True)
        order = order_repo.get()
        return Response({
            "total_count": order.cart.total_count,
            "total_price": order.cart.total_price,
            "lines": serializer.data,})

    def post(self, request):
        order_repo = get_or_create_new_order_repo(request)
        try:
            id, count = request.data['id_menu_item'], request.data['count']
        except KeyError: 
            raise ValidationError
        ServiceOrederCart(order_repo).add_item(id, count)
        return Response({"id_menu_item": id, "count": count})
