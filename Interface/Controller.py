from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass