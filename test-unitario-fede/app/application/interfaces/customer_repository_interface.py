from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities import Cliente

class RepositorioClienteInterface(ABC):
    #Se usa abstractmethod para obligar a las clases hijas a usar el metodo obtener_por_id
    @abstractmethod
    def obtener_por_id(self, id_cliente: int) -> Optional[Cliente]:
        """
        Busca un cliente por su ID.
        
        Retorno:
            - Objeto Cliente si se encuentra.
            - None si no existe.
        La implementación concreta (array, DB, API) se define en la capa de infraestructura.
        """
        pass

