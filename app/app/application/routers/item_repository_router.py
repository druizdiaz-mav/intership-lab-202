from fastapi import APIRouter
from pydantic import BaseModel

from app.application.usecases.get_item_by_id import GetItemByIdUseCase

class ItemSchema(BaseModel):
    id: int
    description: str
    price: float

def create_item_repository_router(get_item_by_id: GetItemByIdUseCase) -> APIRouter:
    router = APIRouter()

    @router.get("/item/{item_id}")
    def get_item(item_id: int) -> ItemSchema:
        item = get_item_by_id.execute(item_id)

        return ItemSchema(
            id=item.get_id(),
            description=item.get_description(),
            price=item.get_price()
        )

    return router