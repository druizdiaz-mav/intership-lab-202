from app.domain.entities import Producto
from app.application.interfaces.product_repository_interface import RepositorioProductoInterface

class CrearProductoUseCase:
    def __init__(self, repo: RepositorioProductoInterface):
        self.repo = repo

    def ejecutar(self, producto: Producto) -> Producto:
        return self.repo.guardar(producto)