from app.application.interfaces.customer_repository_interface import CustomerRepositoryInterface
from app.domain.customer import Customer

class MockCustomerRepository(CustomerRepositoryInterface):
    def get_customer_by_id(self, customer_id: int) -> Customer:
        if (customer_id > 100):
            raise Exception("Customer not found")

        customer = Customer(
            customer_id=customer_id,
            name=f"Mock Customer {customer_id}",
            active=customer_id % 2 == 1
        )

        return customer