from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PaymentCallbackLiqpaySerializer

@api_view(['POST'])
def liqpay_callback(request):
    serializer = PaymentCallbackLiqpaySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)
