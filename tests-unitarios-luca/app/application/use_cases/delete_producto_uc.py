from app.application.interfaces.producto_repository_interface import ProductoRepositoryInterface
from app.domain.entities.producto import Producto
from app.domain.entities.exceptions import EntityNotFound

class DeleteProductoUseCase:
    def __init__(self, repo: ProductoRepositoryInterface):
        self.repo = repo
    
    async def execute(self, id: int) -> None:
        producto_eliminado = await self.repo.delete(id)

        if not producto_eliminado:
            raise EntityNotFound(f"El producto con id {id} no existe")
    