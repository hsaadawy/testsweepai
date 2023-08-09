from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def present(self, data):
        print(data)