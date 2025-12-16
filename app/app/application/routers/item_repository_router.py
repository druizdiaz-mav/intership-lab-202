from fastapi import APIRouter

from app.application.usecases.get_item_by_id import GetItemByIdUseCase

def create_item_repository_router(get_item_by_id: GetItemByIdUseCase) -> APIRouter:
    router = APIRouter()

    @router.get("/item/{item_id}")
    def get_item(item_id: int) -> dict:
        item = get_item_by_id.execute(item_id)

        return {
            "id": item.get_id(),
            "description": item.get_description(),
            "price": item.get_price()
        }

    return router