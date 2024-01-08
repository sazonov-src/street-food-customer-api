from abc import ABC, abstractmethod
from typing import Any


class BasePayment(ABC):
    def __init__(self, payment_dataset: list[dict[str, Any]]):
        self._payment_dataset = payment_dataset

    @abstractmethod
    def is_payment(self) -> bool:
        pass

class PaymentLIQPay(BasePayment):
    def is_payment(self) -> bool:
        for callback in self._payment_dataset:
            if callback['status'] == 'success':
                return True
        return False
