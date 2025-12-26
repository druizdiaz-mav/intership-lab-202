from abc import ABC, abstractmethod
from app.domain.entities.cliente import Cliente

class ClienteRepositoryInterface(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Cliente | None: #devuelve el objeto Cliente si está activo, None si no
        pass

    @abstractmethod
    def save(self, customer: Cliente) -> Cliente: #guarda el objeto Cliente y devuelve el objeto guardado
        pass

    @abstractmethod
    def delete(self, id: int) -> None: #elimina el objeto Cliente por su ID
        pass