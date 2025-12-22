from abc import ABC, abstractmethod
from app.domain.entities import Producto

class ProductRepositoryInterface(ABC):

    @abstractmethod
    def create(self, producto: Producto) -> Producto:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Producto | None:
        pass

    @abstractmethod
    def delete(self, product_id: int) -> None:
        pass
