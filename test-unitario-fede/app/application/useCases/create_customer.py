from app.domain.entities import Cliente
from app.application.interfaces.customer_repository_interface import RepositorioClienteInterface

class CrearClienteUseCase:
    def __init__(self, repo: RepositorioClienteInterface):
        self.repo = repo

    def ejecutar(self, cliente: Cliente) -> Cliente:
        return self.repo.guardar(cliente)