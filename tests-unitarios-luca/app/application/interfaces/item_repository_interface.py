from abc import ABC, abstractmethod

class ItemRepositoryInterface(ABC):
    @abstractmethod
    def get_price(self, id_producto: int) -> float:
        #Retorna el precio del producto. Retorna None si no existe
        pass