from app.domain.entities import Cliente
from typing import Optional
from app.application.interfaces.customer_repository_interface import RepositorioClienteInterface

class RepositorioClienteMemoria(RepositorioClienteInterface):
    def __init__(self):
        # Simulamos una DB
        self.db = {
            1: Cliente(1, "Mateo", True),
            2: Cliente(2, "Luca", False),
            3: Cliente(3, "Lisandro", True)
        }

    def obtener_por_id(self, id_cliente: int)-> Optional[Cliente]:
        return self.db.get(id_cliente)