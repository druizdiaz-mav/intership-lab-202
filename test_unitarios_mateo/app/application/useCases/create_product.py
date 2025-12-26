from app.domain.entities import Producto
from app.application.interfaces.product_repository_interface import (
    ProductRepositoryInterface
)

class CreateProduct:
    def __init__(self, repository: ProductRepositoryInterface):
        self.repository = repository

    def execute(self, nombre: str, precio: float) -> Producto:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        producto = Producto(
            id=None,
            nombre=nombre,
            precio=precio
        )

        return self.repository.create(producto)
