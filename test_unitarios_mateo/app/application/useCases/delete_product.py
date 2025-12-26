from app.application.interfaces.product_repository_interface import (
    ProductRepositoryInterface
)

class DeleteProduct:
    def __init__(self, repository: ProductRepositoryInterface):
        self.repository = repository

    def execute(self, product_id: int) -> None:
        self.repository.delete(product_id)
