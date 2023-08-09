from abc import ABC, abstractmethod

class ValueObject(ABC):
    @abstractmethod
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))