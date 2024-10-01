import logging

from entity.model import Product


class ProductRepository:

    def __init__(self, session):
        self.session = session

    def persist(self, product):
        try:
            self.session.add(product)
            return product
        except Exception as e:
            logging.error("fail save product", e)

    def get_by_code(self, code):
        try:
            return self.session.query(Product).filter_by(code=code).first()
        except Exception as e:
            logging.error("fail get product", e)