class Payment:
    def __init__(self, order) -> None:
        self.order = order

    def get_payment_url(self) -> str:
        return ""
    
    def is_payment(self) -> bool:
        return True
