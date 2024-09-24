from entity.category import Category


class CategoryRepository:

    def __init__(self, session):
        self.session = session

    def persist(self, category):
        self.session.add(category)

    def get_by_name(self, name):
        return self.session.query(Category).filter_by(name=name).first()