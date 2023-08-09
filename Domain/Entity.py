import datetime
import uuid

class Entity:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return f"Entity(id={self.id}, created_at={self.created_at})"