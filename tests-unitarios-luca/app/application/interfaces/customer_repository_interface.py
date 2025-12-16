from abc import ABC, abstractmethod

class CustomerRepositoryInterface(ABC):
    @abstractmethod
    def is_active(self, customer_id: int) -> bool: #devuelve true si está activo, false si no
        pass