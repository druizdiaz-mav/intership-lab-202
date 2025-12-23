from app.domain.entities import Orden
from app.application.interfaces.order_repository_interface import (
    OrderRepositoryInterface
)
from app.application.interfaces.customer_repository_interface import (
    CustomerRepositoryInterface
)
from app.application.useCases.validate_order import ValidateOrderUseCase

class CreateOrder:
    def __init__(
        self,
        order_repository: OrderRepositoryInterface,
        customer_repository: CustomerRepositoryInterface
    ):
        self.order_repository = order_repository
        self.customer_repository = customer_repository

    def execute(self, orden: Orden) -> Orden:
        ValidateOrderUseCase.execute(orden, self.customer_repository)
        return self.order_repository.create(orden)
