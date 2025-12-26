from app.application.interfaces.cliente_repository_interface import ClienteRepositoryInterface
from app.domain.entities.exceptions import EntityNotFound

class DeleteClienteUseCase:
    def __init__(self, repo: ClienteRepositoryInterface):
        self.repo = repo
    
    async def execute(self, id: int) -> None:
        cliente_eliminado = await self.repo.delete(id)

        if not cliente_eliminado:
            raise EntityNotFound(f"El cliente con id {id} no existe")
    