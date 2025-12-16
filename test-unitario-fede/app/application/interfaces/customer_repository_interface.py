from abc import ABC, abstractmethod
from app.domain.entities import Cliente

class RepositorioClienteInterface(ABC):
    #Se usa abstractmethod para obligar a las clases hijas a usar el metodo obtener_por_id
    @abstractmethod
    def obtener_por_id(self, id_cliente: int):
        pass

