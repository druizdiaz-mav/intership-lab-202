from app.application.interfaces.orden_repository_interface import OrdenRepositoryInterface
from app.domain.entities.orden import Orden
from app.domain.entities.exceptions import EntityNotFound

class GetOrdenUseCase:
    def __init__(self, repo: OrdenRepositoryInterface):
        self.repo = repo

    async def execute(self, id: int) -> Orden:
        orden = await self.repo.get_by_id(id)

        if not orden:
            raise EntityNotFound(f"La orden con id {id} no existe.")
        
        return orden
