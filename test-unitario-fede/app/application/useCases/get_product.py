from typing import Optional
from app.domain.entities import Producto
from app.application.interfaces.product_repository_interface import RepositorioProductoInterface

class ObtenerProductoUseCase:
    def __init__(self, repo: RepositorioProductoInterface):
        self.repo = repo

    def ejecutar(self, id_producto: int) -> Optional[Producto]:
        return self.repo.obtener_por_id(id_producto)