from abc import ABC, abstractmethod

class ApplicationService(ABC):
    @abstractmethod
    def execute(self):
        print("Execute method called in ApplicationService")