from abc import ABC, abstractmethod
from app.domain.entities.producto import Producto

class ProductoRepositoryInterface(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Producto | None: #devuelve el objeto Producto si está activo, None si no
        pass

    @abstractmethod
    def save(self, producto: Producto) -> Producto: #guarda el objeto Producto y devuelve el objeto guardado
        pass

    @abstractmethod
    def delete(self, id: int) -> None: #elimina el objeto Producto por su ID
        pass