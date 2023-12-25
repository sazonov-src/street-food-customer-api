import pytest
from app_payment_callbacks.serializers import PaymentCallbackLiqpaySerializer
from app_payment_callbacks.models import PaymentCallbackLiqpay
from rest_framework import serializers

@pytest.mark.django_db
def test_liqpay_callback(data, order):
    serializer = PaymentCallbackLiqpaySerializer(data=data)
    assert serializer.is_valid(raise_exception=True)
    assert len(serializer.validated_data) == 3
    assert PaymentCallbackLiqpay.objects.count() == 0
    serializer.save()
    assert PaymentCallbackLiqpay.objects.count() == 1

@pytest.mark.django_db
def test_liqpay_callback_another_order(data, another_order):
    serializer = PaymentCallbackLiqpaySerializer(data=data)
    with pytest.raises(serializers.ValidationError):
        assert serializer.is_valid(raise_exception=True)

@pytest.mark.django_db
def test_liqpay_callback_invalid_signature(data):
    serializer = PaymentCallbackLiqpaySerializer(data=data)
    with pytest.raises(serializers.ValidationError):
        assert serializer.is_valid(raise_exception=True)
