from app.application.interfaces.order_repository_interface import OrderRepositoryInterface
from app.domain.order import Order

class RepositoryRemoveOrderUseCase:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def execute(self, order_id: int):
        order = self.order_repository.remove_order(order_id)