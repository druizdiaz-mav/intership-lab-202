from abc import ABC, abstractmethod
from app.domain.entities import Cliente

class CustomerRepositoryInterface(ABC):

    @abstractmethod
    def create(self, cliente: Cliente) -> Cliente:
        pass

    @abstractmethod
    def get_by_id(self, customer_id: int) -> Cliente | None:
        pass

    @abstractmethod
    def delete(self, customer_id: int) -> None:
        pass
