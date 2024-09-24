from pydantic import BaseModel


class ProductRequest(BaseModel):
    description: str
    value: str
    category: str

