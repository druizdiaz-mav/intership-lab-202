from typing import Optional
from app.domain.entities import Orden
from app.application.interfaces.orden_repository_interface import RepositorioOrdenInterface

class ObtenerOrdenUseCase:
    def __init__(self, repo_orden: RepositorioOrdenInterface):
        self.repo_orden = repo_orden

    def ejecutar(self, id_orden: int) -> Optional[Orden]:
        return self.repo_orden.obtener_por_id(id_orden)