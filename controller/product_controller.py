import logging

from fastapi import HTTPException
from starlette import status

from app import app
from config.UnitWork import UnitWork
from controller import mapper_product
from controller.product_request import ProductRequest
from controller.product_response import ProductResponse, ProductCodeResponse
from repository.product_repository import ProductRepository
from service.product_service import ProductService


@app.post("/api/v1/product", status_code=status.HTTP_201_CREATED, response_model=ProductCodeResponse)
def create_product(payload: ProductRequest):
    try:
        with UnitWork as unit:
            logging.info("receive payload %s", payload)
            repo = ProductRepository(unit)
            service = ProductService(repo)

            service.save(mapper_product.to_entity(payload))

    except Exception as e:
        logging.error(e)
        raise HTTPException(
            status_code=400,
            detail=f'fail save loan {e}'
        )


@app.get("/api/v1/product/{code}", status_code=status.HTTP_200_OK, response_model=ProductResponse)
def get_product(code: str):
    pass