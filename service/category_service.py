from repository.category_repository import CategoryRepository


class CategoryService:

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def save(self, category):
        return self.repository.persist(category)

    def find_by_name(self, name):
        return self.repository.get_by_name(name)

    def find_by_id(self, id):
        return self.repository.get_by_id(id)