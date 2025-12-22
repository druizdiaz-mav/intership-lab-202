from app.application.interfaces.product_repository_interface import RepositorioProductoInterface

class EliminarProductoUseCase:
    def __init__(self, repo: RepositorioProductoInterface):
        self.repo = repo

    def ejecutar(self, id_producto: int) -> bool:
        return self.repo.eliminar(id_producto)