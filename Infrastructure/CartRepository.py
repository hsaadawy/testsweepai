from Infrastructure.BaseRepository import BaseRepository
from Domain.Cart import Cart

class CartRepository(BaseRepository):
    def create(self, cart: Cart):
        self.carts.append(cart)
        print("Cart created.")

    def read(self, id: int):
        for cart in self.carts:
            if cart.id == id:
                return cart
        return None

    def update(self, cart: Cart):
        for i, existing_cart in enumerate(self.carts):
            if existing_cart.id == cart.id:
                self.carts[i] = cart
                print("Cart updated.")
                return
        print("Cart not found.")

    def delete(self, id: int):
        for i, cart in enumerate(self.carts):
            if cart.id == id:
                del self.carts[i]
                print("Cart deleted.")
                return
        print("Cart not found.")