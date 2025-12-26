from abc import ABC, abstractmethod

class OrdenRepositoryInterface(ABC):
    @abstractmethod
    def save(self, orden: dict) -> None:
        #Guarda la orden en la base de datos
        pass
    @abstractmethod
    def get_by_id(self, id: int) -> dict:
        #Retorna la orden por id. Retorna None si no existe
        pass
    @abstractmethod
    def delete(self, id: int) -> None:
        #Elimina la orden por id
        pass