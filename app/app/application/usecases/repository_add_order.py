from app.application.interfaces.order_repository_interface import OrderRepositoryInterface
from app.domain.order import Order

class RepositoryAddOrderUseCase:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def execute(self, order: Order) -> Order:
        order = self.order_repository.add_order(order)

        return order