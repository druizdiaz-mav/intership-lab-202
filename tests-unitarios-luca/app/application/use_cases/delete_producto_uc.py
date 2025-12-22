from app.application.interfaces.producto_repository_interface import ProductoRepositoryInterface
from app.domain.entities.producto import Producto

class DeleteProductoUseCase:
    def __init__(self, repo: ProductoRepositoryInterface):
        self.repo = repo
    
    async def execute(self, id: int) -> None:
        await self.repo.delete(id)
    