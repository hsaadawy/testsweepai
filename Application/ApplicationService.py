from abc import ABC, abstractmethod

class ApplicationService(ABC):
    @abstractmethod
    def execute(self):
        pass