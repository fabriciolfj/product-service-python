from pydantic import BaseModel


class ProductCodeResponse(BaseModel):
    code: str


class ProductResponse(BaseModel):
    code: str
    name: str
    category: str