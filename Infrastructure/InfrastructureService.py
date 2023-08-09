from abc import ABC, abstractmethod

class InfrastructureService(ABC):
    @abstractmethod
    def execute(self):
        pass