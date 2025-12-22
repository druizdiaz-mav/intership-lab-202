from app.application.interfaces.cliente_repository_interface import ClienteRepositoryInterface
from app.domain.entities.cliente import Cliente
from app.domain.entities.exceptions import EntityNotFound

class GetClienteUseCase:

    def __init__(self, repo: ClienteRepositoryInterface):
        self.repo = repo

    async def execute(self, id: int) -> Cliente:
        cliente = await self.repo.get_by_id(id)

        if not cliente:
            raise EntityNotFound(f"El cliente con id {id} no existe.")
        
        return cliente