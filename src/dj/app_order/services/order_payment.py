from app_payment_callbacks.utils import *
import settings

from .utils import validate

class ServiceOrderPayment:
    def __init__(self, order):
        self.order = order

    def get_payment_data(self, pk):
        data = {}
        data |= settings.LIQPAY_PAYMENT_DATA
        data["amount"] = self.order.get_cart_for_payment().total_price
        data["order_id"] = pk
        return {"data": get_hash_data(data),
                "signature": hash_data_to_sign(get_hash_data(data))}
