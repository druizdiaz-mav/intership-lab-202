from app.domain.order import Order
from abc import ABC, abstractmethod

class OrderRepositoryInterface(ABC):
    @abstractmethod
    def get_order_by_id(self, order_id: int) -> Order:
        """Retrieve a order by its ID."""
        pass

    @abstractmethod
    def add_order(self, order: Order) -> Order:
        """Add a new order."""
        pass

    @abstractmethod
    def remove_order(self, order_id: int):
        """Remove an existing order."""
        pass
