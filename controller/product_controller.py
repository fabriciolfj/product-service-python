import logging
from symbol import raise_stmt

from fastapi import HTTPException
from starlette import status

from app import app
from config.UnitWork import UnitWork
from controller import mapper_product
from controller.product_request import ProductRequest
from controller.product_response import ProductResponse
from repository.product_repository import ProductRepository
from service.product_service import ProductService


@app.post("/api/v1/product", status_code=status.HTTP_201_CREATED, response_model=ProductResponse)
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
            defail=f'fail save loan {e}'
        )
