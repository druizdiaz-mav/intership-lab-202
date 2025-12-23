from app.domain.entities import Cliente
from app.application.interfaces.customer_repository_interface import (
    CustomerRepositoryInterface
)

class GetCustomer:
    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(self, customer_id: int) -> Cliente | None:
        return self.repository.get_by_id(customer_id)
