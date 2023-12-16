from abc import ABC, abstractmethod


class CartLine(ABC):
    @abstractmethod
    def get_line(self, pk) -> dict:
        pass

    @abstractmethod
    def add_line(self) -> dict:
        pass

    @abstractmethod
    def del_line(self, pk) -> dict:
        pass

    @abstractmethod
    def plus_count_line(self, pk) -> dict:
        pass

    @abstractmethod
    def minus_count_line(self, pk) -> dict:
        pass
