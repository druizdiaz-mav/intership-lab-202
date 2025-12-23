from app.domain.entities import Orden
from app.domain.exceptions import InvalidOrderException
from app.application.interfaces.customer_repository_interface import CustomerRepositoryInterface

class ValidateOrderUseCase:
    def __init__(self, customer_repo: CustomerRepositoryInterface):
        self.customer_repo = customer_repo

    def execute(self, order: Orden) -> float:
        if not order.items:
            raise InvalidOrderException("La orden debe contener al menos un ítem.")

        total = 0
        for item in order.items:
            if item.quantity <= 0:
                raise InvalidOrderException(f"La cantidad del ítem '{item.name}' debe ser mayor a cero.")
            if item.unit_price <= 0:
                raise InvalidOrderException(f"El precio unitario del ítem '{item.name}' debe ser mayor a cero.")
            total += item.quantity * item.unit_price

        if total > 10_000:
            raise InvalidOrderException("El total de la orden no puede superar los $10.000.")

        if not self.customer_repo.is_active(order.customer_id):
            raise InvalidOrderException("El cliente no está activo.")

        return total
