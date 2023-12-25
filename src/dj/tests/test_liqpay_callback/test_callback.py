import pytest
from app_payment_callbacks.serializers import PaymentCallbackLiqpaySerializer
from app_payment_callbacks.models import PaymentCallbackLiqpay

@pytest.mark.django_db
def test_liqpay_callback(data):
    serializer = PaymentCallbackLiqpaySerializer(data=data)
    assert serializer.is_valid(raise_exception=True)
    assert len(serializer.validated_data) == 3
    assert PaymentCallbackLiqpay.objects.count() == 0
    serializer.save()
    assert PaymentCallbackLiqpay.objects.count() == 1
