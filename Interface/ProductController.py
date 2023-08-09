from Interface.Controller import Controller
from Infrastructure.ProductRepository import ProductRepository

class ProductController(Controller):
    def __init__(self):
        self.product_repository = ProductRepository()

    def handle_request(self, request):
        if request.method == 'POST':
            product = request.data
            self.product_repository.create(product)
        elif request.method == 'GET':
            id = request.args.get('id')
            product = self.product_repository.read(id)
            return product
        elif request.method == 'PUT':
            product = request.data
            self.product_repository.update(product)
        elif request.method == 'DELETE':
            id = request.args.get('id')
            self.product_repository.delete(id)