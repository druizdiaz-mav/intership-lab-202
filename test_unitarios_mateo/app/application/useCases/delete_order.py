from app.application.interfaces.order_repository_interface import (
    OrderRepositoryInterface
)

class DeleteOrder:
    def __init__(self, repository: OrderRepositoryInterface):
        self.repository = repository

    def execute(self, order_id: int) -> None:
        self.repository.delete(order_id)
