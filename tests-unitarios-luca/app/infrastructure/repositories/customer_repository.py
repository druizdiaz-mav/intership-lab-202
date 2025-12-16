from app.application.interfaces.customer_repository_interface import CustomerRepositoryInterface
from app.domain.entities import Persona

lista_personas = [
    Persona("Luca", 1, "activo"),
    Persona("Fede", 2, "inactivo"),
    Persona("Mateo", 3, "activo"),
    Persona("Licha", 4, "inactivo"),
]

class CustomerRepositoryInMemory(CustomerRepositoryInterface):
    def is_active(self, customer_id: int) -> bool:
        for persona in lista_personas:
            if persona.id == customer_id:
                if persona.estado == "activo":
                    return True
        return False

