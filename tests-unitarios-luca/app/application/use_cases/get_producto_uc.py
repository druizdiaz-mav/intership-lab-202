from app.application.interfaces.producto_repository_interface import ProductoRepositoryInterface
from app.domain.entities.producto import Producto
from app.domain.entities.exceptions import EntityNotFound

class GetProductoUseCase:

    def __init__(self, repo: ProductoRepositoryInterface):
        self.repo = repo

    async def execute(self, id: int) -> Producto:
        producto = await self.repo.get_by_id(id)
        if not producto:
            raise EntityNotFound(f"El producto con id {id} no existe.")
        
        return producto