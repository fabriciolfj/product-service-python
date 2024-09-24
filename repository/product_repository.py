import logging

from entity.product import Product
from service.category_service import CategoryService


class ProductRepository:

    def __init__(self, session, category_service: CategoryService):
        self.session = session
        self.category_service = category_service

    def persist(self, product):
        try:
            category = self.category_service.find_by_name(product.category.name)

            if not category:
                category = self.category_service.save(category)

            product.category = category
            self.session.add(product)
            return product
        except Exception as e:
            logging.error("fail save product", e)

    def get_by_code(self, code):
        try:
            return self.session.query(Product).filter_by(code=code).first()
        except Exception as e:
            logging.error("fail get product", e)