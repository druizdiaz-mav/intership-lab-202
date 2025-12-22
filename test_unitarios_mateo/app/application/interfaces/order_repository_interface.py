from abc import ABC, abstractmethod
from app.domain.entities import Orden

class OrderRepositoryInterface(ABC):

    @abstractmethod
    def create(self, orden: Orden) -> Orden:
        pass

    @abstractmethod
    def get_by_id(self, order_id: int) -> Orden | None:
        pass

    @abstractmethod
    def delete(self, order_id: int) -> None:
        pass
