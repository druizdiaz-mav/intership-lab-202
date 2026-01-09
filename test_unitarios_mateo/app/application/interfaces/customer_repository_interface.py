from abc import ABC, abstractmethod

class CustomerRepositoryInterface(ABC):
    @abstractmethod
    
    def is_active(self, customer_id: int) -> bool:
        """Devuelve True si el cliente está activo"""
        pass
