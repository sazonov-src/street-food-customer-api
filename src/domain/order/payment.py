from abc import ABC, abstractmethod


class BasePayment(ABC):

    @property
    @abstractmethod
    def order(self):
        pass

    @abstractmethod
    def get_payment_url(self) -> str:
        pass
    
    @abstractmethod
    def is_payment(self) -> bool:
        pass
