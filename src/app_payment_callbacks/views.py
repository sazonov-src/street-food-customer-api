from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_order.models import Order
from .models import PaymentCallbackLiqpay
import domain

@api_view(['POST'])
def liqpay_callback(request):
    sdk= domain.LiqpaySDK(request.data)
    sdk.validate(request.data['signature'])
    data = sdk.decode_data(request.data['data'])
    order = Order.objects.get(id=data['order_id'])
    PaymentCallbackLiqpay.objects.create(order=order, data=data, sign=request.data['signature'])
    return Response({'status': 'OK'})
