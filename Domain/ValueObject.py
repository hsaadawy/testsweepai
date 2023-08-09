from abc import ABC, abstractmethod

class ValueObject(ABC):
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass