from app.application.interfaces.cliente_repository_interface import ClienteRepositoryInterface
from app.domain.entities.cliente import Cliente
from app.domain.entities.exceptions import DomainException

class SaveClienteUseCase:

    def __init__(self, repo: ClienteRepositoryInterface):
        self.repo = repo
    
    async def execute(self, cliente: Cliente) -> Cliente:
        self.validateAndSet(cliente)
        saved_cliente = await self.repo.save(cliente)
        return saved_cliente

    def validateAndSet(self, cliente: Cliente) -> None:
        if not cliente.nombre or cliente.nombre.strip() == "":
            raise DomainException("El nombre del cliente no puede estar vacío.")
        cliente.activo = True

