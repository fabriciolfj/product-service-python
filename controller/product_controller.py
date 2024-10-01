import logging
from unicodedata import category

from fastapi import HTTPException
from starlette import status

from app import app
from config.UnitWork import UnitWork
from controller import mapper_product
from controller.product_request import ProductRequest
from controller.product_response import ProductResponse, ProductCodeResponse
from repository.category_repository import CategoryRepository
from repository.product_repository import ProductRepository
from service.category_service import CategoryService
from service.product_service import ProductService


@app.post("/api/v1/product", status_code=status.HTTP_201_CREATED, response_model=ProductCodeResponse)
def create_product(payload: ProductRequest):
    try:
        with UnitWork() as unit:
            logging.info("receive payload %s", payload)

            repo = ProductRepository(unit.session)
            category_repo = CategoryRepository(unit.session)

            category_service = CategoryService(category_repo)
            service = ProductService(repo, category_service)

            code = service.save(mapper_product.to_entity(payload))
            response = ProductCodeResponse(code=code)
        return response
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            status_code=400,
            detail=f'fail save product {e}'
        )


@app.get("/api/v1/product/{code}", status_code=status.HTTP_200_OK, response_model=ProductResponse)
def get_product(code: str):
    try:
        with UnitWork as unit:
            logging.info("receive code %s", code)
            repo = ProductRepository(unit)
            service = ProductService(repo)

            product = service.find_by_code(code)
            return mapper_product.to_response(product)
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            status_code=400,
            detail=f'fail get product {e}'
        )