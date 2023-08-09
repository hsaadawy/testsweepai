from Infrastructure.CartRepository import CartRepository
from .Controller import Controller

class CartController(Controller):
    def __init__(self):
        self.cart_repository = CartRepository()

    def handle_request(self, request):
        if request.method == 'POST':
            cart = request.data
            self.cart_repository.create(cart)
        elif request.method == 'GET':
            id = request.args.get('id')
            cart = self.cart_repository.read(id)
            return cart
        elif request.method == 'PUT':
            cart = request.data
            self.cart_repository.update(cart)
        elif request.method == 'DELETE':
            id = request.args.get('id')
            self.cart_repository.delete(id)