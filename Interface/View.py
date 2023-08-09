from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def present(self, data):
        pass