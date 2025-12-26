from app.application.interfaces.orden_repository_interface import OrdenRepositoryInterface
from app.domain.entities.exceptions import EntityNotFound

class DeleteOrdenUseCase:
    def __init__(self, repo: OrdenRepositoryInterface):
        self.repo = repo

    async def execute(self, id: int) -> None:
        orden_eliminada = await self.repo.delete(id)

        if not orden_eliminada:
            raise EntityNotFound(f"La orden con id {id} no existe")