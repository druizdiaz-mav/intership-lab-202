from app.domain.customer import Customer
from abc import ABC, abstractmethod

class CustomerRepositoryInterface(ABC):
    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer:
        """Retrieve a customer by its ID."""
        pass