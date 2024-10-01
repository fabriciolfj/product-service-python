import uuid

from controller.product_request import ProductRequest
from controller.product_response import ProductResponse
from entity.model import Product, Category
from entity.status import Status


def to_entity(request: ProductRequest):
    category = Category(description=request.description)
    return Product(
        code=str(uuid.uuid4()),
        category=category,
        description=request.description,
        value=request.value,
        status=Status.PENDING.value
    )

def to_response(product: Product):
    return ProductResponse(
        code=product.code,
        category=product.category.description,
        name=product.description,
    )