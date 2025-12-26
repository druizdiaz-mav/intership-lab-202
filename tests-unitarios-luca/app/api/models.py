from pydantic import BaseModel, Field
from typing import List

class ItemRequest(BaseModel):
    id_producto: int = Field(..., gt=0)
    cantidad: int = Field(..., gt=0)

class CreateOrdenRequest(BaseModel):
    id_cliente: int = Field(..., gt=0)
    items: List[ItemRequest]