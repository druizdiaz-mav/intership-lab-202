from typing import Optional
from app.domain.entities import Cliente
from app.application.interfaces.customer_repository_interface import RepositorioClienteInterface

class ObtenerClienteUseCase:
    def __init__(self, repo: RepositorioClienteInterface):
        self.repo = repo

    def ejecutar(self, id_cliente: int) -> Optional[Cliente]:
        return self.repo.obtener_por_id(id_cliente)