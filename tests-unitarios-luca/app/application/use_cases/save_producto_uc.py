from app.application.interfaces.producto_repository_interface import ProductoRepositoryInterface
from app.domain.entities.producto import Producto
from app.domain.entities.exceptions import DomainException

class SaveProductoUseCase:

    def __init__(self, repo: ProductoRepositoryInterface):
        self.repo = repo

    async def execute(self, producto: Producto) -> Producto:
        self.validate(producto)
        saved_producto = await self.repo.save(producto)
        return saved_producto

    def validate(self, producto: Producto) -> None:
        if not producto.nombre or producto.nombre.strip() == "":
            raise DomainException("El nombre del producto no puede estar vacío.")
        if not producto.precio or producto.precio <= 0:
            raise DomainException("El producto debe tener precio y debe ser mayor que cero.")

