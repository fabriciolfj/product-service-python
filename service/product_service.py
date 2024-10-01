from repository.product_repository import ProductRepository
from service.category_service import CategoryService


class ProductService:

    def __init__(self, repository: ProductRepository, categoryService: CategoryService):
        self.repository = repository
        self.category_service = categoryService

    def save(self, product):
        category = self.category_service.find_by_name(product.category.description)

        if not category:
            category = self.category_service.save(product.category)

        product.category = category
        product.category_id = category.id
        product = self.repository.persist(product)
        return str(product.code)

    def find_by_code(self, code):
        product = self.repository.get_by_code(code)
        product.category = self.category_service.find_by_id(product.category_id)

        return product