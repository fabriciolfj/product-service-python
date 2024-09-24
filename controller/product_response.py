from pydantic.v1 import BaseModel


class ProductResponse(BaseModel):
    code: str
