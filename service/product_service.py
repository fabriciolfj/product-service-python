class ProductService:

    def __init__(self, repository):
        self.repository = repository

    def save(self, product):
        product = self.repository.save(product)
        return product.code

    def find_by_code(self, code):
        return self.repository.find_by_code(code)