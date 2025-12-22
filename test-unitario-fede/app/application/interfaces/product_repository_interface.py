from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities import Producto

class RepositorioProductoInterface(ABC):
    
    @abstractmethod
    def obtener_por_id(self, id_producto: int) -> Optional[Producto]:
        pass

    @abstractmethod
    def guardar(self, producto: Producto) -> Producto:
        
        pass

    @abstractmethod
    def eliminar(self, id_producto: int) -> bool:
        pass