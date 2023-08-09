from Domain.ValueObject import ValueObject

class Product(ValueObject):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.id == other.id and self.name == other.name and self.price == other.price
        return False

    def __hash__(self):
        return hash((self.id, self.name, self.price))