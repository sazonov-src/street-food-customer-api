from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_order.models import Order
from .models import PaymentCallbackLiqpay
import domain

@api_view(['POST'])
def liqpay_callback(request):
    data = request.data
    pay_data = domain.get_valid_data(data['data'], data['signature'])
    order = Order.objects.get(id=pay_data['order_id'])
    PaymentCallbackLiqpay.objects.create(order=order, data=pay_data, sign=data['signature'])
    return Response({'status': 'OK'})
