from abc import ABC, abstractmethod
from app.domain.entities import Persona

class CustomerRepositoryInterface(ABC):
    @abstractmethod
    def get_by_id(self, customer_id: int) -> Persona | None: #devuelve el objeto Persona si está activo, None si no
        pass