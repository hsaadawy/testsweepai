from abc import ABC, abstractmethod

class DomainService(ABC):
    @abstractmethod
    def execute(self):
        print("Execute method called in DomainService")