from Infrastructure.BaseRepository import BaseRepository

class ProductRepository(BaseRepository):
    def create(self, product):
        self.products.append(product)
        print("Product created.")

    def read(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None

    def update(self, product):
        for i, existing_product in enumerate(self.products):
            if existing_product.id == product.id:
                self.products[i] = product
                print("Product updated.")
                return
        print("Product not found.")

    def delete(self, id):
        for i, product in enumerate(self.products):
            if product.id == id:
                del self.products[i]
                print("Product deleted.")
                return
        print("Product not found.")