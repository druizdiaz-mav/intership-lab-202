from app.application.interfaces.customer_repository_interface import CustomerRepositoryInterface
from app.domain.customer import Customer

class GetCustomerByIdUseCase():
    def __init__(self, customer_repository: CustomerRepositoryInterface):
        self.customer_repository = customer_repository

    def execute(self, customer_id: int) -> Customer:
        return self.customer_repository.get_customer_by_id(customer_id)