from app.application.interfaces.customer_repository_interface import CustomerRepositoryInterface

class CustomerRepository(CustomerRepositoryInterface):
    def __init__(self):
        self.customers = {1: True, 2: False}  # simula clientes activos/inactivos

    def is_active(self, customer_id: int) -> bool:
        return self.customers.get(customer_id, False)
