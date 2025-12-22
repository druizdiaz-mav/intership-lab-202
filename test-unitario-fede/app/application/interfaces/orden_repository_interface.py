from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities import Orden

class RepositorioOrdenInterface(ABC):
    
    @abstractmethod
    def guardar(self, orden: Orden) -> Orden:
        pass

    @abstractmethod
    def obtener_por_id(self, id_orden: int) -> Optional[Orden]:
        pass

    @abstractmethod
    def eliminar(self, id_orden: int) -> bool:
        pass