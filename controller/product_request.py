from pydantic import BaseModel
from decimal import Decimal

class ProductRequest(BaseModel):
    description: str
    value: Decimal
    category: str

