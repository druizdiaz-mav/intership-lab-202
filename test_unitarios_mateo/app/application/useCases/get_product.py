from app.domain.entities import Producto
from app.application.interfaces.product_repository_interface import (
    ProductRepositoryInterface
)

class GetProduct:
    def __init__(self, repository: ProductRepositoryInterface):
        self.repository = repository

    def execute(self, product_id: int) -> Producto | None:
        return self.repository.get_by_id(product_id)
