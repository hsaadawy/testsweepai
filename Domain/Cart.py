from Domain.Product import Product

class Cart:
    def __init__(self, id):
        self.id = id
        self.product_list = []
        self.total_price = 0.0

    def add_product(self, product):
        self.product_list.append(product)
        self.calculate_total_price()

    def remove_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)
            self.calculate_total_price()

    def calculate_total_price(self):
        self.total_price = sum(product.price for product in self.product_list)