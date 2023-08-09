from abc import ABC, abstractmethod

class DomainService(ABC):
    @abstractmethod
    def execute(self):
        pass