from entity.model import Category


class CategoryRepository:

    def __init__(self, session):
        self.session = session

    def persist(self, category):
        self.session.add(category)
        self.session.flush()
        return category

    def get_by_name(self, name):
        return self.session.query(Category).filter_by(description=name).first()

    def get_by_id(self, id):
        return self.session.query(Category).filter_by(id=id).first()