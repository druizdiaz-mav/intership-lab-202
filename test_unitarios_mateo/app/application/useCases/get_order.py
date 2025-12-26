from app.domain.entities import Orden
from app.application.interfaces.order_repository_interface import (
    OrderRepositoryInterface
)

class GetOrder:
    def __init__(self, repository: OrderRepositoryInterface):
        self.repository = repository

    def execute(self, order_id: int) -> Orden | None:
        return self.repository.get_by_id(order_id)
