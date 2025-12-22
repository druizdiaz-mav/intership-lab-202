from app.application.interfaces.cliente_repository_interface import ClienteRepositoryInterface
from app.domain.entities.cliente import Cliente

class DeleteClienteUseCase:
    def __init__(self, repo: ClienteRepositoryInterface):
        self.repo = repo
    
    async def execute(self, id: int) -> None:
        await self.repo.delete(id)
    