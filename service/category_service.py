class CategoryService:

    def __init__(self, repository):
        self.repository = repository

    def save(self, category):
        self.repository.save(category)

    def find_by_name(self, name):
        return self.repository.find_by_name(name)