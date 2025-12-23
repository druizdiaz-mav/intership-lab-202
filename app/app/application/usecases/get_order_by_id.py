from app.application.interfaces.order_repository_interface import OrderRepositoryInterface
from app.domain.order import Order

class GetOrderByIdUseCase():
    def __init__(self, order_repository: OrderRepositoryInterface):
        self.order_repository = order_repository

    def execute(self, order_id: int) -> Order:
        return self.order_repository.get_order_by_id(order_id)