from uuid import uuid4

from controller.product_request import ProductRequest
from entity.category import Category
from entity.product import Product
from entity.status import Status


def to_entity(request: ProductRequest):
    category = Category(description=request.description)
    return Product(
        code=uuid4.uuid4(),
        category=category,
        value=request.value,
        status=Status.PENDING.__str__()
    )