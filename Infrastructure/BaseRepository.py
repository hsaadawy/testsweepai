from abc import ABC, abstractmethod

class BaseRepository(ABC):
    def create(self, entity):
        print("Creating entity...")

    def read(self, id):
        print("Reading entity with id", id, "...")

    def update(self, entity):
        print("Updating entity...")

    def delete(self, id):
        print("Deleting entity with id", id, "...")