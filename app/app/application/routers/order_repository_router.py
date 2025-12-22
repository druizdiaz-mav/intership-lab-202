from fastapi import APIRouter
from pydantic import BaseModel

from app.application.usecases.get_order_by_id import GetOrderByIdUseCase

class OrderSchema(BaseModel):
    id: int
    customer_id: int
    total: float

def create_order_repository_router(get_order_by_id: GetOrderByIdUseCase) -> APIRouter:
    router = APIRouter()

    @router.get("/order/{order_id}")
    def get_order(order_id: int) -> OrderSchema:
        order = get_order_by_id.execute(order_id)

        return OrderSchema(
            id=order.get_order_id(),
            customer_id=order.get_customer_id(),
            total=order.get_total()
        )

    return router