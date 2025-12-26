from app.domain.entities import Cliente
from app.application.interfaces.customer_repository_interface import (
    CustomerRepositoryInterface
)

class CreateCustomer:
    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(self, nombre: str, activo: bool) -> Cliente:
        cliente = Cliente(
            id=None,
            nombre=nombre,
            activo=activo
        )
        return self.repository.create(cliente)
