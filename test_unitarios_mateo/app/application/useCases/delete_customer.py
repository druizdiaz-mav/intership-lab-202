from app.application.interfaces.customer_repository_interface import (
    CustomerRepositoryInterface
)

class DeleteCustomer:
    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(self, customer_id: int) -> None:
        self.repository.delete(customer_id)
