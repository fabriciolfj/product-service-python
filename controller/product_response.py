from pydantic.v1 import BaseModel


class ProductCodeResponse(BaseModel):
    code: str


class ProductResponse(BaseModel):
    pass