from app.application.interfaces.customer_repository_interface import RepositorioClienteInterface

class EliminarClienteUseCase:
    def __init__(self, repo: RepositorioClienteInterface):
        self.repo = repo

    def ejecutar(self, id_cliente: int) -> bool:
        return self.repo.eliminar(id_cliente)