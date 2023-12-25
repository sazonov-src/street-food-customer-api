
class ServiceOrderPayment:
    def __init__(self, order):
        self.order = order

    def get_payment(self):
        return self.order.get_payment()
