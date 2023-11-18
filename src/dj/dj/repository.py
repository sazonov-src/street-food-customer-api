from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def model(self):
        pass
