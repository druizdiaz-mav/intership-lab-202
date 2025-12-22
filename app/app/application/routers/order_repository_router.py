import logging

from fastapi import APIRouter

from app.application.usecases.get_order_by_id import GetOrderByIdUseCase

def create_order_repository_router(get_order_by_id: GetOrderByIdUseCase) -> APIRouter:
    router = APIRouter()

    @router.get("/order/{order_id}")
    def get_order(order_id: int) -> dict:
        order = get_order_by_id.execute(order_id)

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)

        logger.info(f"Order retrieved: ID={order.get_order_id()}, CustomerID={order.get_customer_id()}, Total={order.get_total()}")

        return {
            "id": order.get_order_id(),
            "customer_id": order.get_customer_id(),
            "total": order.get_total()
        }

    return router